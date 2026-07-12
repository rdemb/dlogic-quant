---
title: "Struktury danych i wydajność w MQL5: bufor cykliczny i szybkie OnTick"
description: "Rozbiór wydajności i struktur danych w MQL5: dlaczego kod w OnTick oraz OnCalculate wykonuje się bardzo często i co z tego wynika dla kosztu obliczeń. Omówienie tablic w trybie serii (ArraySetAsSeries) i kierunku indeksowania, wzorców kosztownych (przeliczanie całego okna co tick, kopiowanie dużych tablic, alokacje w pętli) kontra tanich (suma krocząca, praca tylko na nowym barze, rezerwacja pamięci w ArrayResize). Wyjaśnienie bufora cyklicznego jako struktury do okna kroczącego bez realokacji, ze złożonością O(1) na aktualizacji zamiast O(n), oraz rozsądnego użycia CopyBuffer i CopyRates. Fakty API oparte na dokumentacji MQL5. Wydajność ujęta jako higiena inżynierska, nie źródło przewagi."
date: 2026-07-12 20:00:00 +0200
eyebrow: "Programowanie · wydajność"
dek: "Kod wskaźnika i eksperta w MetaTrader 5 uruchamia się przy każdym ticku, więc koszt pojedynczej aktualizacji mnoży się przez tysiące wywołań. Ten tekst pokazuje, skąd bierze się różnica między wzorcem tanim a kosztownym, jak bufor cykliczny utrzymuje okno kroczące bez realokacji pamięci i dlaczego złożoność O(1) na barze bywa istotna. Kod jest szkieletem dydaktycznym, a wydajność to higiena inżynierska, nie przewaga rynkowa."
readingTime: 9
tags: [programowanie, MQL5, "struktury danych", "bufor cykliczny", wydajność, "złożoność obliczeniowa", OnTick, ArraySetAsSeries, CopyBuffer, "suma krocząca", edukacja]
category: edukacja
---

> **W skrócie**
>
> - `OnTick` w ekspertach i `OnCalculate` we wskaźnikach wykonują się przy każdym ticku, a przy aktywnym rynku to nawet kilkadziesiąt wywołań na sekundę. Koszt jednej aktualizacji mnoży się przez tę częstotliwość, dlatego drobny wybór implementacyjny robi realną różnicę w obciążeniu.
> - Wzorce kosztowne to przeliczanie całego okna od nowa przy każdym ticku, kopiowanie dużych tablic bez potrzeby i alokacja pamięci w pętli. Wzorce tanie to suma krocząca, praca tylko na nowo domkniętym barze i rezerwacja pamięci z góry.
> - Bufor cykliczny (ring buffer) to tablica o stałym rozmiarze z indeksem zapisu biegnącym po module. Pozwala utrzymać okno N ostatnich barów bez realokacji, z aktualizacją o koszcie O(1) zamiast O(n).
> - Wydajność to higiena inżynierska, nie źródło przewagi. Szybszy kod liczy to samo szybciej, nie liczy niczego lepszego. Przykłady są szkieletem dydaktycznym, nie sygnałem transakcyjnym.

**Teza w jednym zdaniu:** wydajność w MQL5 sprowadza się do jednej zasady, nie licz przy każdym ticku tego, co można policzyć raz na bar albo zaktualizować jednym krokiem, a bufor cykliczny jest strukturą, która tę zasadę realizuje dla okna kroczącego.

## Dlaczego OnTick liczy się bardzo często

W ekspercie zdarzenie `OnTick` wywoływane jest przy każdym przychodzącym ticku, czyli przy każdej zmianie ceny instrumentu (dokumentacja MQL5, OnTick). We wskaźniku analogiczną rolę pełni `OnCalculate`, uruchamiane przy każdym ticku oraz przy każdej nowej świecy. W spokojnym rynku to kilka wywołań na sekundę, w czasie publikacji danych makro nawet kilkadziesiąt. Konsekwencja jest arytmetyczna: jeśli pojedyncze wywołanie wykonuje pracę proporcjonalną do długości okna, a okno ma N barów, to koszt na minutę rośnie jak liczba ticków razy N.

Stąd pierwszy podział, który organizuje cały temat: co musi dziać się przy każdym ticku, a co wystarczy policzyć raz na domknięty bar. Wartość wskaźnika dla bieżącej, jeszcze niedomkniętej świecy faktycznie zmienia się z każdym tickiem. Ale historia barów już zamkniętych się nie zmienia, więc przeliczanie jej w kółko to czysta strata. Wykrycie nowego bara jest tanie: wystarczy zapamiętać czas otwarcia bara zerowego i porównać go przy kolejnym wywołaniu.

```
datetime g_last_bar_time = 0;   // czas otwarcia ostatnio obsluzonego bara

bool NowyBar()
  {
   datetime t = iTime(_Symbol, _Period, 0);  // czas otwarcia biezacego bara
   if(t != g_last_bar_time)                   // pojawil sie nowy bar
     {
      g_last_bar_time = t;
      return(true);
     }
   return(false);                             // wciaz ten sam bar
  }
```

## Tablice jako serie i pułapka indeksowania

Dynamiczna tablica w MQL5 domyślnie indeksowana jest jak zwykła tablica programistyczna: pozycja `0` to element najstarszy, ostatnia pozycja to najnowszy. Funkcja `ArraySetAsSeries` ustawia flagę `AS_SERIES`, która odwraca kierunek dostępu: po jej włączeniu indeks `0` wskazuje najnowszy bar, a wyższe indeksy sięgają w przeszłość (dokumentacja MQL5, ArraySetAsSeries). Sama flaga nie przenosi danych w pamięci, zmienia tylko sposób adresowania.

```
// Domyslnie (tablica dynamiczna, nie-seria):
//   arr[0]     →  element najstarszy
//   arr[N-1]   →  element najnowszy

// Po ArraySetAsSeries(arr, true):
//   arr[0]     →  najnowszy bar
//   arr[N-1]   →  najstarszy bar
```

Pułapka jest zawsze ta sama i bierze się z pomieszania obu konwencji w jednym kodzie. Pętla napisana od najstarszego bara ku najnowszemu zakłada indeksację zwykłą. Jeśli tablica jest w trybie serii, odwołanie do poprzedniego bara to indeks o jeden wyższy, nie niższy. Wartość policzona przy złym założeniu wychodzi odbita w czasie, a w najgorszym wariancie sięga po bar jeszcze nieistniejący, co jest look-ahead. Zasada praktyczna: ustawić kierunek świadomie, jawnym `ArraySetAsSeries` dla każdej tablicy roboczej, i dopasować do niego pętlę.

## Wzorce kosztowne kontra tanie

Trzy wzorce psują wydajność najczęściej.

Pierwszy to przeliczanie całego okna przy każdym ticku. Suma z N barów liczona od zera kosztuje N operacji, a wykonana przy każdym ticku i dla każdego bara historii daje koszt rzędu liczby barów razy N. To ten sam problem, który przy średniej kroczącej rozwiązuje suma krocząca: sąsiednie okna różnią się tylko dwoma elementami, więc zamiast sumować wszystko, wystarczy dodać wchodzący bar i odjąć wypadający.

Drugi to kopiowanie dużych tablic bez potrzeby. Każde `CopyBuffer` albo `CopyRates` po całą dostępną historię, powtórzone przy każdym ticku, przenosi tysiące elementów, z których zmienił się co najwyżej jeden. Zwykle wystarczy skopiować kilka ostatnich barów, a nie cały szereg.

Trzeci to alokacja pamięci w pętli. Wywołanie `ArrayResize` wewnątrz pętli po barach każe środowisku wielokrotnie powiększać tablicę, a realokacja to fizyczne przeniesienie dotychczasowej zawartości w nowe miejsce.

Dokumentacja MQL5 opisuje na ten ostatni problem konkretny mechanizm. Funkcja `ArrayResize` przyjmuje trzeci, opcjonalny parametr `reserve_size`, który rezerwuje pamięć ponad bieżący rozmiar tablicy. Dzięki rezerwie kolejne powiększenia nie wymagają fizycznej realokacji, dopóki mieszczą się w zarezerwowanym zapasie (dokumentacja MQL5, ArrayResize). Rezerwacja z góry zamienia wiele drobnych realokacji na jedną.

Po tej samej, tańszej stronie leżą trzy nawyki: utrzymywać sumę kroczącą zamiast sumować okno, wykonywać ciężką pracę raz na domknięty bar zamiast przy każdym ticku, i rezerwować pamięć raz zamiast rosnąć element po elemencie.

## Złożoność na aktualizacji: O(n) kontra O(1)

Różnicę między tymi wzorcami wygodnie opisać złożonością obliczeniową, czyli tempem, w jakim koszt rośnie z rozmiarem danych (Cormen i inni, 2009). Interesuje tu koszt jednej aktualizacji, przypadającej na jeden nowy bar.

Naiwna średnia z okna N ma na aktualizacji złożoność O(n): przeczytanie i zsumowanie N elementów. Suma krocząca ma O(1): jeden dodaj, jeden odejmij, niezależnie od długości okna. Zapis O(1) i O(n) pomija stałe i mówi tylko o tempie wzrostu, ale to właśnie tempo decyduje, gdy okno i liczba ticków rosną. Dla okna dziesięciu barów różnica jest niezauważalna, dla okna kilkuset barów liczonych na wielu instrumentach naraz przestaje być.

## Bufor cykliczny: okno kroczące bez realokacji

Zostaje pytanie, jaka struktura danych realizuje sumę kroczącą w praktyce, skoro okno musi pamiętać, który bar wypada. Odpowiedzią jest bufor cykliczny, nazywany też pierścieniowym (ring buffer). To tablica o stałym rozmiarze N z jednym indeksem zapisu, który po dojściu do końca wraca na początek, licząc pozycje po module N. Nowy element nadpisuje najstarszy, bo ten właśnie wypada z okna. Struktura nigdy nie rośnie ani się nie kurczy, więc nie ma realokacji, i nie przesuwa elementów, więc nie ma kopiowania całości (Cormen i inni, 2009).

```
//+------------------------------------------------------------------+
//|   Bufor cykliczny z suma kroczaca (okno N barow).                |
//|   Aktualizacja O(1): jeden zapis, jeden dodaj, jeden odejmij.    |
//|   Szkielet dydaktyczny, nie sygnal transakcyjny.                 |
//+------------------------------------------------------------------+
class CRingSum
  {
private:
   double  m_buf[];      // tablica robocza o stalym rozmiarze N
   int     m_size;       // dlugosc okna N
   int     m_head;       // indeks zapisu (biegnie po module N)
   int     m_count;      // ile realnych probek juz weszlo (do N)
   double  m_sum;        // biezaca suma elementow w oknie

public:
   //--- Inicjalizacja: alokacja RAZ, poza jakakolwiek petla po barach
   void Init(const int n)
     {
      m_size  = (n < 1 ? 1 : n);
      ArrayResize(m_buf, m_size);      // jedna alokacja na caly czas zycia
      ArrayInitialize(m_buf, 0.0);
      m_head  = 0;
      m_count = 0;
      m_sum   = 0.0;
     }

   //--- Dodanie nowej probki (np. ceny domknietego bara). Koszt O(1).
   void Push(const double value)
     {
      m_sum -= m_buf[m_head];          // odejmij element, ktory wypada z okna
      m_buf[m_head] = value;           // nadpisz najstarsza pozycje nowa wartoscia
      m_sum += value;                  // dodaj wchodzacy element do sumy
      m_head = (m_head + 1) % m_size;  // przesun indeks po module N
      if(m_count < m_size)
         m_count++;                    // okno napelnia sie tylko na starcie
     }

   //--- Czy okno jest juz pelne (N probek)
   bool IsFull() const { return(m_count >= m_size); }

   //--- Srednia z okna. Wazna dopiero, gdy IsFull() zwraca true.
   double Mean() const
     {
      if(m_count == 0)
         return(0.0);
      return(m_sum / m_count);
     }
  };
```

Użycie łączy wszystkie wątki tekstu w jeden wzorzec. Obiekt tworzony jest raz, alokacja pamięci następuje w `Init`, poza pętlą po barach. Metoda `Push` wykonuje się tylko wtedy, gdy domknie się nowy bar, więc ciężka praca nie powtarza się przy każdym ticku. Sama aktualizacja ma koszt stały, bo nie zależy od długości okna.

```
CRingSum g_sma;   // obiekt globalny, tworzony raz

int OnInit()
  {
   g_sma.Init(20);          // jedna alokacja okna na 20 barow
   g_last_bar_time = 0;
   return(INIT_SUCCEEDED);
  }

void OnTick()
  {
   if(!NowyBar())           // pracuj tylko na nowo domknietym barze
      return;               // ten sam bar: nic nie licz

   double c = iClose(_Symbol, _Period, 1);  // zamkniecie ostatniego DOMKNIETEGO bara
   g_sma.Push(c);           // aktualizacja O(1), bez realokacji

   if(g_sma.IsFull())
     {
      double srednia = g_sma.Mean();
      // srednia gotowa do dalszej analizy (bez decyzji handlowej)
     }
  }
```

Bar o numerze 1 jest ostatnim barem zamkniętym, bo bar 0 dopiero się tworzy. Praca na barze 1 gwarantuje, że do sumy trafia wartość ostateczna, a nie chwilowa cena niedomkniętej świecy.

## CopyBuffer i CopyRates z rozsądkiem

Dane spoza własnych obliczeń pobiera się w MQL5 funkcjami rodziny Copy. `CopyBuffer` przenosi wartości bufora innego wskaźnika do tablicy, a `CopyRates` wypełnia tablicę struktur `MqlRates` kompletem danych barów: czas, OHLC oraz wolumeny. Obie zwracają liczbę skopiowanych elementów albo minus jeden przy błędzie (dokumentacja MQL5, CopyBuffer, CopyRates).

Rozsądek sprowadza się do trzech nawyków. Po pierwsze, kopiować tylko tyle, ile trzeba: parametry `start_pos` i `count` pozwalają pobrać kilka ostatnich barów zamiast całej historii. Po drugie, sprawdzać wartość zwracaną, bo dane mogą być jeszcze niegotowe, a wynik minus jeden oznacza nieudane kopiowanie. Po trzecie, ustawić kierunek tablicy odbiorczej świadomie: wywołanie `ArraySetAsSeries` na tablicy wynikowej sprawia, że indeks `0` odpowiada najnowszemu barowi, co ułatwia spójne indeksowanie w reszcie kodu.

```
double buf[];                        // tablica odbiorcza
ArraySetAsSeries(buf, true);         // indeks 0 = najnowszy bar

// handle: uchwyt wskaznika pobrany raz w OnInit (np. przez iMA)
int skopiowane = CopyBuffer(handle, 0, 0, 3, buf);  // tylko 3 ostatnie bary
if(skopiowane <= 0)                  // -1 blad, 0 brak danych
   return;                           // dane niegotowe: nic nie licz
// buf[0] to najnowsza wartosc bufora wskaznika o uchwycie handle
```

Wszystkie te techniki łączy jedna granica interpretacyjna. Suma krocząca, bufor cykliczny, praca raz na bar i rezerwacja pamięci zmieniają wyłącznie koszt liczenia, nie jego wynik. Szybszy wskaźnik pokazuje dokładnie to samo co wolny, tylko mniej obciąża terminal i szybciej reaguje. Wydajność jest więc higieną inżynierską, warunkiem, by kod dało się w ogóle uruchomić na żywym rynku bez zacięć, a nie źródłem przewagi. Przewaga, jeśli istnieje, bierze się z tego, co kod liczy i jak ta wartość jest używana, a to jest pytanie z zupełnie innego porządku.

Materiał czysto edukacyjny o wydajności i strukturach danych w MQL5, nie porada inwestycyjna. Kod ilustruje mechanikę optymalizacji, nie strategię, i niczego nie obiecuje. Bufor cykliczny oraz suma krocząca są przykładami dydaktycznymi, a nie sygnałem transakcyjnym.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
