---
title: "Strategy Tester w MT5: jak testować, żeby nie kłamać"
description: "Wbudowany w MetaTrader 5 Strategy Tester sprawdza hipotezę na danych historycznych, ale jego wynik jest wart tyle, ile założenia testu. Tekst rozkłada cztery tryby modelowania (Open prices only, 1 minute OHLC, Every tick, Every tick based on real ticks) i pokazuje, co każdy pomija: od ruchu wewnątrz bara po realny spread. Dalej ustawienia kosztów, czyli spread stały kontra bieżący, prowizja i swap z kontraktu oraz pole Delay emulujące opóźnienie egzekucji, a także pułapki, które zawyżają wynik: cena otwarcia dla strategii intrabar, zaniżony spread, brak opóźnienia zlecenia. Na końcu czytanie raportu (profit factor, oczekiwana wypłata, recovery factor, maksymalne obsunięcie) bez samooszukiwania oraz własne kryterium OnTester. Dobry wynik testera to warunek konieczny, nie wystarczający. Fakty o testerze zgodnie z dokumentacją MetaTrader 5 i MQL5 oraz Pardo (2008)."
date: 2026-07-12 17:00:00 +0200
eyebrow: "Programowanie · testowanie"
category: edukacja
dek: "Strategy Tester nie mówi, czy strategia zarabia, tylko jak zachowałaby się przy założeniach, które sam wpiszesz. Zmień tryb modelowania, spread albo pole opóźnienia i ten sam kod da inny wynik. Ten tekst pokazuje, gdzie tester bywa optymistyczny, jak ustawić go blisko realnych warunków i jak czytać raport, nie oszukując samego siebie. Sam zielony wynik niczego nie dowodzi."
readingTime: 9
tags: [programowanie, MQL5, "Strategy Tester", MetaTrader, backtest, "jakość modelowania", "realne ticki", spread, "profit factor", "walk-forward", edukacja]
---

> **W skrócie**
>
> - Strategy Tester w MetaTrader 5 przewija historię i wykonuje na niej EA, ale wynik jest tak dobry, jak założenia: tryb modelowania, spread, prowizja, swap i opóźnienie egzekucji. Ten sam kod przy różnych ustawieniach daje różne krzywe kapitału.
> - Cztery tryby modelowania różnią się tym, co pomijają. Open prices only widzi tylko otwarcia świec, 1 minute OHLC cztery ceny z bara M1, Every tick generuje sztuczne ticki z historii minutowej, a Every tick based on real ticks używa realnych ticków brokera i według dokumentacji jest najdokładniejszy, bo niesie też historyczny, zmienny spread.
> - Koszty trzeba ustawić świadomie. Spread stały zaniża prawdę wobec bieżącego albo realnego z ticków, prowizja i swap muszą pochodzić ze specyfikacji kontraktu, a pole Delay zostawione na idealnej egzekucji ukrywa opóźnienie i poślizg, które istnieją na żywo.
> - Raport czyta się z ostrożnością. Profit factor bywa napompowany jedną transakcją, oczekiwana wypłata musi przewyższać koszt jednej transakcji, recovery factor i maksymalne obsunięcie mówią o przetrwaniu, a wszystko to jest szumem przy zbyt małej liczbie transakcji.
> - Dobry wynik w testerze to warunek konieczny, nie wystarczający. Potrzeba jeszcze kodu bez look-ahead i walidacji out-of-sample, bo wynik na danych użytych do strojenia jest prawie zawsze zawyżony (Pardo, 2008).

**Teza w jednym zdaniu:** Strategy Tester nie odpowiada na pytanie, czy strategia zarabia, tylko jak zachowałaby się przy założeniach, które wpiszesz, więc jego wynik jest wiarygodny dopiero na realnych tickach, z pełnym kosztem i opóźnieniem egzekucji, a i wtedy pozostaje warunkiem koniecznym, który rozstrzyga się poza próbą.

## Po co osobny tester i czego on nie widzi

Strategy Tester to moduł MetaTrader 5, który przewija zapisaną historię symbolu i wykonuje na niej Expert Advisor tak, jakby czas płynął od nowa. Służy do jednego: taniego odrzucania pomysłów, które nie działają, zanim dotkną prawdziwych pieniędzy. To jest jego właściwa rola, filtr hipotez, a nie maszyna do produkowania pewności. Wynik testu jest funkcją danych i założeń: tego, jakie ticki podłożysz, jaki spread przyjmiesz i czy uwzględnisz opóźnienie egzekucji. Zmiana jednego z tych ustawień potrafi zamienić krzywą kapitału z rosnącej w spadającą, mimo że kod strategii pozostał ten sam. Dlatego pytanie nie brzmi, ile tester pokazał, tylko przy jakich założeniach to pokazał.

## Cztery tryby modelowania i co każdy pomija

Sercem wiarygodności jest sposób, w jaki tester odtwarza ruch ceny wewnątrz świecy. MetaTrader 5 udostępnia cztery tryby, uszeregowane od najszybszego i najzgrubszego do najdokładniejszego.

```
Tryb                             Zrodlo cen               Co pomija / uwaga
Open prices only                 otwarcia barow interwalu ruch wewnatrz bara
1 minute OHLC                    OHLC barow M1            kolejnosc ruchow w minucie
Every tick                       ticki generowane z M1    realny spread, mikrostruktura
Every tick based on real ticks   realne ticki brokera     najdokladniej; latencje ustaw w Delay
```

W trybie Open prices only tester liczy strategię na cenach otwarcia świec wybranego interwału. Zdarzenie OnTick pada raz na świecę, na jej otwarciu. Według dokumentacji MQL5 tester poprawnie sprawdza w tym trybie aktywację zleceń oczekujących oraz poziomów Stop Loss i Take Profit, bo bada je po cenach OHLC bara, ale sama decyzja EA zapada tylko na otwarciu. To wystarcza wyłącznie dla strategii, które i tak działają na zamkniętym barze. Tryb 1 minute OHLC schodzi na minutę i z każdego bara M1 generuje ograniczoną liczbę ticków opartych o cztery ceny kontrolne, więc widzi więcej niż otwarcia, ale wciąż nie zna kolejności ruchów wewnątrz minuty. Every tick generuje ticki algorytmem opartym o historię minutową, co daje gęstą, lecz sztuczną ścieżkę. Every tick based on real ticks używa realnych ticków zebranych z serwera brokera i jest, według dokumentacji, najdokładniejszym trybem, bo odtwarza faktyczne zmiany ceny razem z historycznym, zmiennym spreadem.

## Jakość modelowania i realne ticki

Dwa pierwsze tryby są dobre do szybkiego szkicu, ale każda strategia wrażliwa na to, co dzieje się w środku bara, dostanie w nich zawyżony obraz. Powód jest prosty: jeśli tester nie wie, czy w danej świecy najpierw padł szczyt czy dołek, musi zgadywać, a każde zgadywanie systematycznie sprzyja albo szkodzi konkretnej logice wejścia i wyjścia. Realne ticki usuwają to zgadywanie i, co równie ważne, niosą prawdziwy spread z każdej chwili historii zamiast jednej wartości narzuconej z góry. Dla scalpingu i wszystkiego, co liczy się w pojedynczych punktach, to różnica między testem a fikcją. Warunek jest jeden: broker musi udostępniać realne ticki dla danego symbolu, a ich kompletność bywa różna, więc przed testem warto obejrzeć w dzienniku, ile ticków i barów tester faktycznie wczytał.

## Koszty: spread, prowizja, swap, opóźnienie

Najczęstszy sposób na oszukanie samego siebie to test bez pełnych kosztów. Tester ma osobne pola, które trzeba świadomie ustawić.

```
Model:      Every tick based on real ticks    // realne ticki, nie generowane
Spread:     Current albo realny historyczny    // nie wpisuj 1, nie zanizaj
Commission: z tabeli brokera (specyfikacja)    // domyslnie bywa zero
Swap:       z kontraktu, long i short          // rollover kosztuje
Delay:      realne albo losowe opoznienie      // nie zostawiaj idealnej egzekucji
Deposit:    realny depozyt i waluta konta      // sizing ma sens tylko tu
```

Pole Spread przyjmuje wartość Current, czyli bieżący spread zamrożony na czas testu, albo stałą liczbę punktów. W trybie realnych ticków spread płynie tak, jak płynął w historii, i to jest wersja najbliższa prawdzie. Wpisanie sztywnej, niskiej wartości, na przykład jednego punktu tam, gdzie realnie bywa trzy, to prosta droga do wyniku, którego rynek nigdy nie odda. Prowizja i swap pochodzą ze specyfikacji kontraktu wczytanej do testera. Jeśli broker liczy prowizję od wolumenu, a w specyfikacji jej nie ma, test zaniża koszt każdej transakcji. Swap punktowy naliczany przy rolowaniu pozycji przez noc też trzeba mieć włączony, inaczej strategie trzymające pozycje dłużej wyglądają lepiej, niż są. Ile te koszty faktycznie ważą, rozkłada osobny materiał o [rzeczywistym koszcie transakcji](/dlogic-quant/2026/07/09/ile-naprawde-kosztuje-twoj-trade-tca/).

Osobno stoi pole Delay, które emuluje opóźnienie między wysłaniem zlecenia a jego wykonaniem. Domyślne ustawienie idealnej egzekucji bez zwłoki oznacza, że w teście zlecenie wchodzi natychmiast po cenie sygnału. W realnym handlu jest droga do serwera, czas przetworzenia i możliwy poślizg, więc ustawienie realnego albo losowego opóźnienia przybliża test do prawdy. Dla strategii czułej na cenę wejścia ta różnica bywa większa niż cały rzekomy zysk.

## Pułapki, które zawyżają wynik

Trzy błędy powtarzają się najczęściej. Pierwszy to testowanie strategii intrabar na cenach otwarcia. Jeśli logika reaguje na ruch wewnątrz świecy, a tryb modelowania widzi tylko otwarcia, tester wykona wejścia i wyjścia po cenach, których w tamtej chwili nie było, i pokaże fikcyjnie gładki przebieg. Drugi to zaniżony spread: stała, optymistyczna wartość zamiast realnego, zmiennego kosztu, który przy publikacji danych makro potrafi rozszerzyć się wielokrotnie. Trzeci to brak opóźnienia i poślizgu, czyli pozostawienie idealnej egzekucji, przez co tester wypełnia zlecenia w punkcie niemożliwym do trafienia na żywo. Każdy z tych błędów działa w tę samą stronę: podnosi wynik. Nie ma tu przypadkowości, która czasem pomaga, a czasem szkodzi, bo niedomodelowany koszt zawsze maluje strategię ładniej, niż wypadnie na rachunku.

Do tej rodziny należy też look-ahead, czyli użycie w chwili decyzji informacji, która nie była jeszcze znana. Tester nie chroni przed nim automatycznie, bo błąd siedzi w kodzie strategii, nie w silniku. Jak go rozpoznać i usunąć, rozkłada osobny tekst o [look-ahead w kodzie](/dlogic-quant/2026/07/12/look-ahead-w-kodzie-realizm/).

## Raport testera bez samooszukiwania

Po teście MetaTrader 5 zwraca raport z kilkunastoma liczbami. Cztery czyta się najczęściej i każdą łatwo źle zinterpretować.

- Profit factor to iloraz zysku brutto przez stratę brutto. Wartość powyżej jedności znaczy, że suma zysków przewyższa sumę strat, ale liczba bywa napompowana przez jedną wyjątkową transakcję, więc zawsze warto porównać ją z największą pojedynczą wygraną.
- Oczekiwana wypłata (expected payoff) to średni wynik na transakcję, czyli zysk netto podzielony przez liczbę transakcji. Musi wyraźnie przewyższać realny koszt jednej transakcji. Wynik ledwo dodatni po kosztach oznacza brak przewagi, a nie cienką przewagę.
- Recovery factor to zysk netto podzielony przez maksymalne obsunięcie. Mówi, ile zysku przypada na jednostkę najgorszego bólu. Niski oznacza, że po drodze do zysku konto przechodziło przez głębokie doły.
- Maksymalne obsunięcie MetaTrader 5 raportuje osobno dla salda i dla środków (equity), w pieniądzu i w procentach. Wersja liczona na środkach jest uczciwsza, bo uwzględnia niezrealizowaną stratę otwartych pozycji. Jeśli maksymalne obsunięcie przekracza to, co zniesie depozyt, dodatni zysk jest bez znaczenia, bo rachunek i tak by nie przetrwał.

Nad wszystkimi tymi liczbami stoi jedno pytanie: ile było transakcji. Przy próbie kilkunastu wejść każda z tych miar jest szumem, bo pojedyncze zdarzenie przesuwa ją dowolnie. Bez odpowiedniej liczby transakcji raport nie mierzy strategii, tylko przypadek.

Te progi można wpisać wprost do kodu jako własne kryterium optymalizacji. Funkcja OnTester jest wywoływana raz po każdym przebiegu testu i zwraca liczbę, którą optymalizator maksymalizuje jako kryterium Custom max. Dostęp do statystyk daje TesterStatistics.

```mql5
//+------------------------------------------------------------------+
//| Wlasne kryterium optymalizacji, wywolane raz po kazdym przebiegu.|
//| Karze mala probe i glebokie obsuniecie, nagradza zysk na trade.  |
//| To DEMONSTRACJA kodowania preferencji, nie wzor na przewage.     |
//+------------------------------------------------------------------+
double OnTester()
  {
   double trades = TesterStatistics(STAT_TRADES);          // liczba transakcji
   if(trades < 100)                                         // za mala proba
      return(0.0);                                          // odrzuc przebieg

   double payoff = TesterStatistics(STAT_EXPECTED_PAYOFF);  // sredni wynik/trade
   double pf     = TesterStatistics(STAT_PROFIT_FACTOR);    // profit factor
   double ddpct  = TesterStatistics(STAT_EQUITYDD_PERCENT); // maks. obsuniecie %

   if(payoff <= 0.0 || pf <= 1.0) return(0.0);             // brak sensu ekonomicznego
   if(ddpct  <= 0.0) ddpct = 0.01;                         // ochrona przed dzieleniem

   // wieksze payoff i PF podnosza wynik, glebszy DD go obniza
   return(payoff * pf / ddpct);
  }
```

Taki zapis wymusza minimalną próbę stu transakcji i odrzuca przebiegi, które biorą zysk kosztem obsunięcia. To nie jest formuła na przewagę, tylko sposób, żeby optymalizator nie wybrał piku wiszącego na trzech szczęśliwych transakcjach.

## Warunek konieczny, nie wystarczający

Nawet czysty test na realnych tickach, z pełnym kosztem i realnym opóźnieniem, dowodzi tylko jednego: strategia zachowała się dobrze na tym konkretnym kawałku historii. To warunek konieczny, nie wystarczający. Dobry wynik na danych, które posłużyły do dobierania parametrów, jest prawie gwarantowany przy dostatecznie szerokim przeszukiwaniu i sam z siebie nie znaczy nic. Rozstrzyga dopiero zachowanie na danych, których procedura strojenia nie widziała, co jest sednem [optymalizacji i walk-forward](/dlogic-quant/2026/07/12/optymalizacja-walk-forward-w-kodzie/). Pardo (2008) formułuje tę samą myśl jako warunek: strategia jest wiarygodna dopiero wtedy, gdy działa poza próbą, na której ją zbudowano. Kolejność jest więc stała. Najpierw kod bez look-ahead, potem uczciwy test w Strategy Tester z realnymi tickami i pełnym kosztem, na końcu walidacja out-of-sample. Pominięcie któregokolwiek kroku sprawia, że zielony wynik testera mówi o przeszłości i o założeniach, a nie o szansach na przyszłość.

Materiał czysto edukacyjny o metodyce testowania w MetaTrader 5, nie porada inwestycyjna ani zachęta do konkretnej strategii. Poprawnie skonfigurowany Strategy Tester potrafi odrzucić zły pomysł, ale nie potrafi udowodnić, że pomysł jest dobry; to zawsze wymaga danych spoza próby i świadomości kosztów. Fakty o trybach modelowania, ustawieniach i statystykach opisano zgodnie z dokumentacją MetaTrader 5 i MQL5, a myśl o warunku poza próbą za Pardo (2008). Decyzja i ryzyko zostają po stronie człowieka.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
