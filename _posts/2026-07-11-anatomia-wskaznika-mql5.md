---
title: "Anatomia wskaźnika w MQL5: OnCalculate i bufory"
description: "Rozbiór budowy wskaźnika w MetaTrader 5: blok #property (okno, indicator_buffers, indicator_plots), funkcja OnInit z SetIndexBuffer i PlotIndexSetInteger oraz OnCalculate z parametrami rates_total i prev_calculated. Wyjaśnienie, dlaczego prev_calculated pozwala liczyć tylko nowe bary zamiast całej historii przy każdym ticku, oraz na czym polega pułapka odwrotnej indeksacji tablic po ArraySetAsSeries. Na końcu kompletny, minimalny wskaźnik SMA jako szkielet dydaktyczny. Fakty API oparte na dokumentacji MQL5."
date: 2026-07-11 11:00:00 +0200
eyebrow: "Programowanie · MQL5"
dek: "Wskaźnik w MT5 to dwie funkcje zdarzeniowe i kilka tablic. Ten tekst rozkłada szkielet na części: gdzie terminal wpina kod, jak bufory łączą się z tablicami i dlaczego prev_calculated decyduje o tym, czy wskaźnik liczy sprawnie. Kod SMA na końcu to struktura do czytania, nie strategia."
readingTime: 8
tags: [programowanie, MQL5, wskaźniki, MetaTrader, OnCalculate, bufory, SetIndexBuffer, prev_calculated, ArraySetAsSeries, SMA, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Wskaźnik w MT5 składa się z trzech warstw: nagłówka `#property` (gdzie rysować, ile buforów i linii), funkcji `OnInit` (wiązanie tablic z buforami i wygląd) oraz `OnCalculate` (właściwe liczenie).
> - Sercem wydajności jest `prev_calculated`. Terminal podaje, ile barów policzono w poprzednim wywołaniu, dzięki czemu pętla obsługuje tylko nowe bary, a nie całą historię przy każdym ticku.
> - Tablice w `OnCalculate` są domyślnie indeksowane jak zwykłe tablice: indeks `0` to najstarszy bar, `rates_total - 1` to najnowszy. `ArraySetAsSeries` odwraca ten kierunek i tu leży najczęstsza pułapka.
> - Przykład na końcu to kompletny, minimalny wskaźnik SMA. Szkielet dydaktyczny pokazujący strukturę, nie sygnał do handlu.

**Teza w jednym zdaniu:** wskaźnik w MQL5 to dwie funkcje zdarzeniowe i kilka tablic, a zrozumienie roli `prev_calculated` oraz kierunku indeksacji wystarcza, by czytać i pisać poprawny kod, zanim w ogóle padnie pytanie, co ten kod ma liczyć.

## Szkielet: okno, bufory, linie

Każdy wskaźnik zaczyna się od bloku dyrektyw `#property`, który terminal czyta jeszcze przed uruchomieniem kodu. Pierwsza decyzja to miejsce rysowania. Dyrektywa `#property indicator_chart_window` umieszcza wskaźnik na wykresie ceny, tak jak średnią kroczącą, a `#property indicator_separate_window` tworzy osobne podokno pod wykresem, tak jak oscylator. Wybór jest rozłączny: jeden wskaźnik rysuje albo tu, albo tam.

Dalej dwie liczby, które łatwo pomylić. `#property indicator_buffers` deklaruje, ile buforów, czyli tablic z danymi, wskaźnik trzyma w pamięci. `#property indicator_plots` mówi, ile serii graficznych faktycznie trafia na ekran. Zgodnie z dokumentacją MQL5 nie musi to być ta sama liczba: linia kolorowana typu `DRAW_COLOR_LINE` potrzebuje dodatkowego bufora na indeks koloru, a bufory pomocnicze do obliczeń pośrednich w ogóle nie są rysowane. Prosty wskaźnik z jedną linią ma jeden bufor i jedną linię.

## OnInit: wiązanie buforów i wygląd

Funkcja `OnInit` uruchamia się raz, przy dołączaniu wskaźnika do wykresu i przy każdej zmianie parametrów. Jej zadaniem jest połączyć zadeklarowane globalnie tablice z numerami buforów oraz ustawić wygląd.

Kluczowe jest `SetIndexBuffer`. Pierwszy argument to numer bufora liczony od zera, drugi to nazwa tablicy, trzeci to typ. Dokumentacja MQL5 wymienia trzy typy: `INDICATOR_DATA` dla wartości rysowanych, `INDICATOR_COLOR_INDEX` dla indeksu koloru oraz `INDICATOR_CALCULATIONS` dla obliczeń pośrednich, których nie widać na wykresie. Tablica podawana do `SetIndexBuffer` musi być globalną tablicą dynamiczną typu `double`. Po powiązaniu terminal sam zarządza jej rozmiarem: rośnie ona razem z historią, a kod nie wywołuje na niej `ArrayResize`.

`PlotIndexSetInteger` ustawia właściwości całkowitoliczbowe danej serii. Pod stałą `PLOT_DRAW_TYPE` kryje się typ rysowania, na przykład `DRAW_LINE`, a pod `PLOT_DRAW_BEGIN` numer pierwszego bara, od którego linia ma się pojawić. To drugie jest istotne przy średnich: pierwsze `okres - 1` barów nie ma jeszcze pełnego okna, więc nie powinno być rysowane. Na koniec `IndicatorSetString` ze stałą `INDICATOR_SHORTNAME` nadaje krótką nazwę widoczną w oknie danych i na liście wskaźników.

## OnCalculate: policzyć tylko nowe bary

Cała praca dzieje się w `OnCalculate`. Terminal wywołuje tę funkcję przy każdym nowym ticku oraz przy każdej nowej świecy. Dokumentacja MQL5 opisuje dwie wersje sygnatury. Pierwsza operuje na jednej wybranej cenie:

```
int OnCalculate(const int rates_total,        // liczba wszystkich barow
                const int prev_calculated,    // ile barow policzono w poprzednim wywolaniu
                const int begin,              // od ktorego baru dane wejsciowe maja sens
                const double &price[]);        // tablica ceny (typ ceny wybiera uzytkownik)
```

Druga daje dostęp do kompletu szeregów bieżącego instrumentu:

```
int OnCalculate(const int        rates_total,
                const int        prev_calculated,
                const datetime  &time[],
                const double    &open[],
                const double    &high[],
                const double    &low[],
                const double    &close[],
                const long      &tick_volume[],
                const long      &volume[],
                const int       &spread[]);
```

Znaczenie dwóch pierwszych parametrów jest tu najważniejsze. Parametr `rates_total` to liczba wszystkich barów dostępnych wskaźnikowi. Parametr `prev_calculated` to wartość, którą `OnCalculate` zwróciło w poprzednim wywołaniu, czyli, zgodnie z dokumentacją MQL5, liczba barów obsłużonych do tej pory. Przy pierwszym wywołaniu `prev_calculated` wynosi zero.

Stąd wynika cała optymalizacja. Bez tego mechanizmu wskaźnik przeliczałby całą historię przy każdym ticku, co przy tysiącach barów byłoby czystym marnotrawstwem. Zamiast tego pętla rusza od miejsca, w którym skończyła poprzednio:

```
int start;
if(prev_calculated == 0)
   start = okres - 1;           // pierwszy bar z pelnym oknem
else
   start = prev_calculated - 1; // ostatni znany bar liczymy jeszcze raz

for(int i = start; i < rates_total; i++)
   { /* liczenie wartosci dla bara i */ }
```

Ostatni policzony bar liczony jest ponownie celowo. Bieżąca świeca nie jest domknięta, jej cena zamknięcia zmienia się z każdym tickiem, więc wartość wskaźnika dla niej trzeba aktualizować aż do zamknięcia bara. Na końcu funkcja zwraca `rates_total`, co dokumentacja MQL5 opisuje jako zapamiętanie liczby policzonych barów, przekazywanej potem jako `prev_calculated` przy kolejnym wywołaniu. Zwrot zera wymusza pełne przeliczenie od nowa, co bywa przydatne po wykryciu błędu danych.

## Kierunek indeksacji i pułapka serii

Zostaje pytanie, który koniec tablicy jest który. Domyślnie tablice w `OnCalculate`, zarówno bufory, jak i szeregi `open`, `close` i pozostałe, są indeksowane jak zwykłe tablice programistyczne. Zgodnie z dokumentacją MQL5 oznacza to, że indeks `0` wskazuje najstarszy bar, a `rates_total - 1` najnowszy. Kierunek biegnie od przeszłości do teraźniejszości.

```
// Domyslnie (indeksacja jak w zwyklej tablicy):
//   price[0]              →  najstarszy bar w historii
//   price[rates_total-1]  →  najnowszy, biezacy bar

// Po wywolaniu ArraySetAsSeries(price, true):
//   price[0]              →  najnowszy, biezacy bar
//   price[rates_total-1]  →  najstarszy bar
```

Funkcja `ArraySetAsSeries` odwraca ten kierunek na taki, jaki znają użytkownicy funkcji dostępu do szeregów czasowych, gdzie indeks `0` to bieżąca świeca. I tu leży klasyczna pułapka. Pętla `for(i = prev_calculated; i < rates_total; i++)` zakłada indeksację zwykłą, od najstarszego bara. Jeśli w tym samym kodzie któraś tablica zostanie przełączona przez `ArraySetAsSeries` na tryb serii, ta sama pętla zacznie czytać dane od złego końca, a wartości wyjdą odbite w czasie. Zasada praktyczna jest prosta: ustawić kierunek indeksacji świadomie i dopasować do niego pętlę, zamiast zakładać którykolwiek w ciemno.

## Kompletny przykład: prosty wskaźnik SMA

Poniższy kod zbiera wszystkie elementy w jeden minimalny wskaźnik prostej średniej kroczącej (SMA). Rysuje jedną linię w oknie ceny, liczy średnią z `InpPeriod` ostatnich barów i aktualizuje tylko nowe bary. To szkielet dydaktyczny, pokazujący budowę wskaźnika, a nie sygnał do handlu ani gotowa strategia.

```
//+------------------------------------------------------------------+
//|   DLOGIC_SMA_Demo.mq5                                            |
//|   Szkielet dydaktyczny prostej sredniej kroczacej.               |
//|   Pokazuje strukture wskaznika, nie jest sygnalem do handlu.     |
//+------------------------------------------------------------------+
#property copyright "D-LOGIC Quant. Material edukacyjny."
#property version   "1.00"

//--- Rysowanie w oknie ceny (nie w osobnym podoknie)
#property indicator_chart_window
//--- Jeden bufor danych i jedna linia na ekranie
#property indicator_buffers 1
#property indicator_plots   1
//--- Opis i wyglad linii nr 0
#property indicator_label1  "SMA"
#property indicator_color1  clrDodgerBlue
#property indicator_width1  1

//--- Parametr wejsciowy: dlugosc okna sredniej
input int InpPeriod = 20;   // Okres SMA

//--- Bufor wskaznika: globalna tablica dynamiczna
double SmaBuffer[];

//+------------------------------------------------------------------+
//| Inicjalizacja (raz przy starcie i zmianie parametrow)            |
//+------------------------------------------------------------------+
int OnInit()
  {
   //--- Zabezpieczenie: okres musi byc dodatni
   if(InpPeriod < 1)
      return(INIT_PARAMETERS_INCORRECT);

   //--- Powiazanie tablicy z buforem nr 0 (dane do rysowania)
   SetIndexBuffer(0, SmaBuffer, INDICATOR_DATA);

   //--- Typ rysowania: linia ciagla
   PlotIndexSetInteger(0, PLOT_DRAW_TYPE, DRAW_LINE);

   //--- Nie rysuj pierwszych InpPeriod-1 barow (brak pelnego okna)
   PlotIndexSetInteger(0, PLOT_DRAW_BEGIN, InpPeriod - 1);

   //--- Krotka nazwa w oknie danych
   IndicatorSetString(INDICATOR_SHORTNAME, "DLOGIC SMA(" + (string)InpPeriod + ")");

   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
//| Liczenie wartosci wskaznika                                      |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,        // ile barow jest dostepnych
                const int prev_calculated,    // ile policzono w poprzednim wywolaniu
                const int begin,              // od ktorego baru dane maja sens
                const double &price[])         // tablica ceny wejsciowej
  {
   //--- Za malo danych na pelne okno: nic nie liczymy
   if(rates_total < InpPeriod)
      return(0);

   //--- Start petli: od poczatku albo od ostatniego policzonego baru
   int start;
   if(prev_calculated == 0)
      start = InpPeriod - 1;        // pierwszy bar z pelnym oknem
   else
      start = prev_calculated - 1;  // ostatni bar liczymy jeszcze raz (moze byc niedomkniety)

   //--- Petla tylko po nowych barach, nie po calej historii
   for(int i = start; i < rates_total; i++)
     {
      double sum = 0.0;
      //--- Suma ceny z InpPeriod ostatnich barow (indeks i-j biegnie w przeszlosc)
      for(int j = 0; j < InpPeriod; j++)
         sum += price[i - j];

      SmaBuffer[i] = sum / InpPeriod;
     }

   //--- Zwrot: tyle barow uznajemy za policzone (trafi do prev_calculated)
   return(rates_total);
  }
//+------------------------------------------------------------------+
```

Ten szkielet celowo pomija wszystko, co odróżnia narzędzie użytkowe od ćwiczenia: obsługę wielu buforów, kolor zależny od stanu, kontrolę wartości pustych czy liczenie na cenie innego wskaźnika przez parametr `begin`. Wartość przykładu jest wyłącznie strukturalna. Pokazuje, gdzie terminal wpina kod, jak `prev_calculated` chroni przed liczeniem historii od zera i dlaczego kierunek indeksacji trzeba znać, zanim zaufa się jednej linii na wykresie. Prosta średnia krocząca jest tu tylko pretekstem do pokazania rusztowania.

Materiał czysto edukacyjny o strukturze wskaźnika, nie porada inwestycyjna. Kod ilustruje mechanikę MQL5, a nie przewagę rynkową. SMA służy za przykład dydaktyczny i nie jest sygnałem transakcyjnym.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
