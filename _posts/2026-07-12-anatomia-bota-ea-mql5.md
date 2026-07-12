---
title: "Anatomia bota: pętla zdarzeń, stan, pozycja (MQL5)"
description: "Jak zbudowany jest Expert Advisor w MetaTrader 5 od strony inżynierskiej: pętla zdarzeń OnInit, OnTick, OnDeinit i opcjonalny OnTimer. OnTick wywoływany przy każdym nowym kwotowaniu wymusza bramkę nowego bara i idempotentny kod. Do tego sprawdzanie stanu pozycji przez PositionGetTicket i magic number oraz egzekucja klasą CTrade z kontrolą ResultRetcode. Na końcu kompletny, minimalny szkielet EA jako struktura, nie strategia zarobkowa."
date: 2026-07-12 10:00:00 +0200
eyebrow: "Programowanie · MQL5"
category: edukacja
dek: "Expert Advisor to nie wróżka od kursu, tylko program sterowany zdarzeniami terminala. Ten tekst rozkłada jego szkielet na części: kiedy terminal woła twój kod, jak nie liczyć tego samego na każdym ticku, jak pilnować stanu pozycji i jak bezpiecznie wysłać zlecenie. Przecięcie średnich w przykładzie jest wyłącznie demonstracją struktury."
readingTime: 8
tags: [programowanie, MQL5, "Expert Advisor", MetaTrader, OnTick, CTrade, OnInit, "magic number", "nowy bar", egzekucja, "zarządzanie ryzykiem", edukacja]
---

> **W skrócie**
>
> - Terminal steruje EA przez zdarzenia: OnInit (start), OnTick (nowy tick), OnDeinit (koniec), opcjonalnie OnTimer (cyklicznie). Według dokumentacji MQL5 OnTick leci przy każdym nowym kwotowaniu, więc kod musi być idempotentny: wielokrotne wywołanie na tej samej świecy nie może mnożyć zleceń.
> - Bramka nowego bara: porównaj czas otwarcia bieżącej świecy z zapamiętanym i wpuść logikę raz na świecę, a nie setki razy na jednej. Licz sygnał na barach zamkniętych, żeby uniknąć repaintu.
> - Stan przed akcją: PositionGetTicket automatycznie wybiera pozycję do odczytu, a magic number izoluje własne zlecenia od ręcznych i od innych EA. Nie otwieramy drugiej pozycji, gdy jedna już istnieje.
> - Egzekucja przez CTrade (Trade.mqh): Buy/Sell z SL/TP w jednym wywołaniu. Uwaga z dokumentacji: true z metody Buy oznacza tylko udany check struktury, realny wynik czytamy z ResultRetcode().
> - Zero martingale. Dokładanie do straty i uśrednianie w dół to najszybsza droga do wyzerowania rachunku. Sygnał trzymamy osobno od egzekucji.

**Teza w jednym zdaniu:** Expert Advisor to nie strategia, tylko pętla zdarzeń, w której terminal woła twoje funkcje, a twój kod ma być idempotentny, pilnować stanu i oddzielać sygnał od egzekucji; przecięcie średnich w przykładzie jest wyłącznie demonstracją tej struktury, nie źródłem przewagi.

## Pętla zdarzeń: cztery funkcje, które wywołuje terminal

Expert Advisor nie ma własnej pętli, która kręci się w kółko. Zamiast tego terminal MetaTrader 5 wywołuje z góry ustalone funkcje, gdy zajdzie odpowiednie zdarzenie. To odwrócenie sterowania: nie odpytujesz rynku w kółko, tylko czekasz, aż terminal zawoła twój kod. Szkielet tworzą cztery funkcje o zarezerwowanych nazwach.

```
int  OnInit(void)               // Init:    raz, tuż po załadowaniu EA
void OnTick(void)               // NewTick:  przy każdym nowym kwotowaniu
void OnDeinit(const int reason) // Deinit:   przy zdejmowaniu EA, reason mówi dlaczego
void OnTimer(void)              // Timer:    cyklicznie, po EventSetTimer(sekundy)
```

OnInit inicjalizuje program. Dokumentacja MQL5 zaleca wariant zwracający int, bo pozwala oddać kod błędu: zwrot INIT_SUCCEEDED oznacza start udany, INIT_FAILED wymusza wyładowanie EA. Tu tworzy się uchwyty wskaźników i ustawia parametry. OnDeinit sprząta przy końcu, a parametr reason niesie powód (zmiana parametrów, zamknięcie wykresu, rekompilacja). OnTimer jest opcjonalny i odpala się cyklicznie, ale tylko gdy w OnInit zawołasz EventSetTimer(sekundy); w OnDeinit trzeba go zdjąć przez EventKillTimer().

Kluczowa jest OnTick. Dokumentacja MQL5 określa, że zdarzenie NewTick powstaje przy nadejściu nowego kwotowania dla symbolu wykresu, do którego podpięto EA. W ruchliwym rynku to dziesiątki wywołań na minutę. Kod w OnTick musi więc być idempotentny: powtórne wywołanie na tej samej świecy nie może produkować kolejnych zleceń ani mnożyć stanu. Terminal wprawdzie nie kolejkuje duplikatów, jeśli poprzedni NewTick jest wciąż przetwarzany, kolejny nie trafia do kolejki, ale to nie zdejmuje odpowiedzialności z twojej strony.

## Bramka nowego bara: dlaczego nie działać na każdym ticku

Skoro OnTick leci co tick, a logika oparta na świecach ma sens raz na świecę, potrzebna jest bramka. Pomysł jest prosty: zapamiętaj czas otwarcia bieżącej świecy i wpuść dalszy kod tylko wtedy, gdy ten czas się zmienił.

```
datetime lastBarTime = 0;

bool IsNewBar()
  {
   datetime t = iTime(_Symbol, _Period, 0); // czas otwarcia świecy [0]
   if(t == lastBarTime) return(false);      // ta sama świeca, wychodzimy
   lastBarTime = t;                          // nowa świeca, zapamiętaj czas
   return(true);
  }
```

Po co to robić? Z trzech powodów. Pierwszy to spójność: wskaźnik liczony na świecy [0], która wciąż się formuje, zmienia wartość aż do zamknięcia, więc sygnał policzony w środku świecy potrafi zniknąć albo pojawić się ponownie. Liczenie na barach już zamkniętych, czyli [1] i starszych, usuwa ten repaint. Drugi to koszt i bezpieczeństwo: setki przeliczeń i prób zleceń na jednej świecy obciążają terminal i grożą duplikatami pozycji. Trzeci to zgodność z testerem: strategia typu bar po barze zachowuje się tak samo w backteście i na żywo, bo obie ścieżki podejmują decyzję w tym samym momencie, na zamknięciu.

## Stan i pozycja: sprawdź, zanim otworzysz

Zanim EA wyśle zlecenie, musi wiedzieć, co już ma otwarte. Bez tego przy każdym sygnale dokładałby kolejne pozycje. MQL5 rozróżnia dwa tryby konta: netting, gdzie na symbol przypada jedna pozycja, oraz hedging, gdzie może ich być wiele. Kod, który ma działać w obu, przechodzi po całej liście pozycji.

```
bool HasOwnPosition(long magic)
  {
   for(int i = PositionsTotal() - 1; i >= 0; i--)
     {
      ulong ticket = PositionGetTicket(i); // wybiera pozycję do odczytu
      if(ticket == 0) continue;
      if(PositionGetString(POSITION_SYMBOL) == _Symbol &&
         PositionGetInteger(POSITION_MAGIC) == magic)
         return(true);                     // mamy już swoją pozycję
     }
   return(false);
  }
```

Funkcja PositionGetTicket(index) zwraca ticket pozycji o danym indeksie i, jak podaje dokumentacja MQL5, automatycznie wybiera tę pozycję do pracy funkcjami PositionGetDouble, PositionGetInteger i PositionGetString. Dzięki temu zaraz po niej czytamy symbol i magic bez osobnego kroku selekcji. Magic number to liczba, którą EA znakuje swoje zlecenia: pozwala odróżnić własne pozycje od otwartych z ręki albo przez innego EA na tym samym rachunku. Dla najprostszego przypadku wystarczy PositionSelect(symbol), które kopiuje dane wybranej pozycji i zwraca true przy powodzeniu, ale pętla po PositionsTotal() jest odporna także na tryb hedging i na obce zlecenia.

## Egzekucja: klasa CTrade i kontrola wyniku

Zlecenia można składać ręcznie, wypełniając strukturę MqlTradeRequest i wołając OrderSend. Standard Library skraca to do jednej klasy. Wystarczy dołączyć nagłówek i utworzyć obiekt, a w OnInit ustawić magic, żeby każde zlecenie z tego obiektu było znaczone tą samą liczbą.

```
#include <Trade\Trade.mqh>
CTrade trade;
// w OnInit:
trade.SetExpertMagicNumber(InpMagic);
```

Otwarcie pozycji to jedno wywołanie. Sygnatura Buy z dokumentacji MQL5:

```
bool Buy(double volume, const string symbol=NULL, double price=0.0,
         double sl=0.0, double tp=0.0, const string comment="")
```

Jeśli price wynosi 0, użyta zostanie bieżąca cena Ask, więc zwykle podajemy tylko wolumen, symbol i poziomy SL oraz TP. Symetrycznie działa Sell, który dla ceny 0 bierze Bid. SL i TP to ceny, nie odległości, dlatego liczymy je od bieżącej ceny i normalizujemy do liczby cyfr symbolu funkcją NormalizeDouble.

Tu uwaga, którą łatwo przeoczyć. Dokumentacja MQL5 podkreśla, że udane zakończenie metody Buy nie zawsze oznacza udaną transakcję: zwrot true znaczy tylko, że sprawdzenie struktury się powiodło. Realny wynik trzeba odczytać z odpowiedzi serwera przez ResultRetcode(). Kod TRADE_RETCODE_DONE oznacza wykonanie, a każda inna wartość to powód do zapisu w logu i świadomej reakcji, nie do ślepego ponawiania w pętli.

## Higiena: sygnał osobno, egzekucja osobno, zero martingale

Trzy zasady oddzielają porządny szkielet od maszynki do mielenia depozytu. Rozdziel sygnał od egzekucji: funkcja licząca warunek wejścia nie powinna wysyłać zleceń. Jedna część odpowiada na pytanie czy i w którą stronę, druga na pytanie jak złożyć zlecenie. Taki podział łatwiej testować i trudniej przypadkiem popsuć.

Kontroluj błędy. Każde CopyBuffer może zwrócić mniej danych, niż prosisz, każdy uchwyt iMA może być INVALID_HANDLE, każde zlecenie może wrócić z kodem odmowy. Sprawdzaj zwroty, nie zakładaj sukcesu z góry.

I zasada najważniejsza: zero martingale. Dokładanie do stratnej pozycji, podwajanie wolumenu po stracie i uśrednianie w dół to najszybsza droga do wyzerowania rachunku. Seria strat pod prąd rośnie geometrycznie, a jeden dłuższy ciąg zjada cały kapitał, zanim rynek zdąży wrócić. Szkielet poniżej celowo otwiera najwyżej jedną pozycję i nie dokłada do niej nigdy.

## Kompletny szkielet EA

Poniższy kod składa wszystkie elementy w jeden, poprawny składniowo minimalny EA. Sygnałem jest przecięcie dwóch średnich EMA, policzone na barach zamkniętych. To wyłącznie demonstracja struktury zdarzeń i egzekucji, nie strategia z przewagą.

```mql5
//+------------------------------------------------------------------+
//| Szkielet dydaktyczny EA (MQL5). NIE jest strategia zarobkowa.     |
//| Sygnal: przeciecie EMA = wylacznie DEMONSTRACJA struktury.        |
//+------------------------------------------------------------------+
#include <Trade\Trade.mqh>

input long   InpMagic      = 20260712; // magic: izolacja wlasnych pozycji
input double InpLots       = 0.01;     // wielkosc pozycji (staly lot)
input int    InpFastPeriod = 20;       // szybka EMA
input int    InpSlowPeriod = 50;       // wolna EMA
input int    InpSLPoints   = 300;      // stop loss w punktach
input int    InpTPPoints   = 300;      // take profit w punktach

CTrade   trade;                  // klasa egzekucji ze Standard Library
int      hFast = INVALID_HANDLE; // uchwyt szybkiej EMA
int      hSlow = INVALID_HANDLE; // uchwyt wolnej EMA
datetime lastBarTime = 0;        // pamiec ostatniej swiecy

//+------------------------------------------------------------------+
int OnInit()
  {
   hFast = iMA(_Symbol, _Period, InpFastPeriod, 0, MODE_EMA, PRICE_CLOSE);
   hSlow = iMA(_Symbol, _Period, InpSlowPeriod, 0, MODE_EMA, PRICE_CLOSE);
   if(hFast == INVALID_HANDLE || hSlow == INVALID_HANDLE)
     {
      Print("Blad tworzenia uchwytu iMA");
      return(INIT_FAILED);
     }
   trade.SetExpertMagicNumber(InpMagic); // kazde zlecenie dostanie ten magic
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   if(hFast != INVALID_HANDLE) IndicatorRelease(hFast);
   if(hSlow != INVALID_HANDLE) IndicatorRelease(hSlow);
  }
//+------------------------------------------------------------------+
//| Bramka nowego bara: wpuszcza logike raz na swiece, nie co tick.   |
//+------------------------------------------------------------------+
bool IsNewBar()
  {
   datetime t = iTime(_Symbol, _Period, 0);
   if(t == lastBarTime) return(false);
   lastBarTime = t;
   return(true);
  }
//+------------------------------------------------------------------+
//| Czy istnieje juz WLASNA pozycja (ten symbol + ten magic).         |
//+------------------------------------------------------------------+
bool HasOwnPosition()
  {
   for(int i = PositionsTotal() - 1; i >= 0; i--)
     {
      ulong ticket = PositionGetTicket(i); // wybiera pozycje do odczytu
      if(ticket == 0) continue;
      if(PositionGetString(POSITION_SYMBOL) == _Symbol &&
         PositionGetInteger(POSITION_MAGIC) == InpMagic)
         return(true);
     }
   return(false);
  }
//+------------------------------------------------------------------+
void OnTick()
  {
   // 1) Egzekucja tylko na zamknieciu bara. OnTick leci co tick, wiec bez
   //    tej bramki logika liczylaby sie setki razy na jednej swiecy.
   if(!IsNewBar())
      return;

   // 2) Odczyt dwoch ostatnich ZAMKNIETYCH barow (pozycje 1 i 2).
   double fast[], slow[];
   ArraySetAsSeries(fast, true);
   ArraySetAsSeries(slow, true);
   if(CopyBuffer(hFast, 0, 1, 2, fast) < 2) return;
   if(CopyBuffer(hSlow, 0, 1, 2, slow) < 2) return;

   // [1] = starszy bar, [0] = ostatni zamkniety bar
   bool crossUp   = (fast[1] <= slow[1]) && (fast[0] > slow[0]);
   bool crossDown = (fast[1] >= slow[1]) && (fast[0] < slow[0]);

   // 3) Higiena stanu: nie dokladamy do istniejacej pozycji (zero martingale).
   if(HasOwnPosition())
      return;

   // 4) Egzekucja przez CTrade. SL/TP liczone od biezacej ceny.
   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);

   if(crossUp)
     {
      double sl = NormalizeDouble(ask - InpSLPoints * _Point, _Digits);
      double tp = NormalizeDouble(ask + InpTPPoints * _Point, _Digits);
      if(!trade.Buy(InpLots, _Symbol, 0.0, sl, tp)) // price 0 => Ask
         Print("Buy odrzucony, retcode=", trade.ResultRetcode(),
               " ", trade.ResultRetcodeDescription());
     }
   else if(crossDown)
     {
      double sl = NormalizeDouble(bid + InpSLPoints * _Point, _Digits);
      double tp = NormalizeDouble(bid - InpTPPoints * _Point, _Digits);
      if(!trade.Sell(InpLots, _Symbol, 0.0, sl, tp)) // price 0 => Bid
         Print("Sell odrzucony, retcode=", trade.ResultRetcode(),
               " ", trade.ResultRetcodeDescription());
     }
  }
//+------------------------------------------------------------------+
```

Przeczytaj ten kod jeszcze raz jako mapę, nie jako receptę. OnInit tworzy uchwyty i ustawia magic, OnTick przechodzi przez cztery bramki (nowa świeca, dane, stan, egzekucja), OnDeinit zwalnia zasoby. Cała logika sygnału mieści się w dwóch liniach z crossUp i crossDown i można ją wymienić na dowolną inną bez ruszania szkieletu. To jest sedno: struktura żyje dłużej niż pomysł na wejście.

Materiał czysto edukacyjny o strukturze programu, nie porada inwestycyjna ani gotowy bot do handlu. Przecięcie średnich to demonstracja mechaniki zdarzeń i egzekucji, nie strategia z przewagą; każdy automat wymaga własnych testów na danych historycznych i na rachunku demo, zanim dotknie realnych pieniędzy, a odpowiedzialność za ryzyko zostaje po stronie człowieka. Fakty o API opisano zgodnie z dokumentacją MQL5.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
