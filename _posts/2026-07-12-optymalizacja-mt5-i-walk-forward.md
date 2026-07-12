---
title: "Optymalizacja w MT5: genetyczna i walk-forward w praktyce"
description: "Tester MetaTrader 5 stroi parametry na dwa sposoby: pełny przegląd sprawdza wszystkie kombinacje siatki, a szybki algorytm genetyczny przez selekcję, krzyżowanie i mutację dochodzi do dobrych obszarów bez testowania wszystkiego. Tekst pokazuje, dlaczego maksymalizacja jednej metryki dopasowuje krzywą do szumu, jak czytać mapę wyników (pojedynczy pik kontra szerokie plateau), jak działa forward test z podziałem okna na część optymalizacyjną i forward, czym jest walk-forward efficiency jako stosunek wyniku forward do in-sample oraz jak zastąpić profit własnym kryterium w OnTester. Fakty o API zgodnie z dokumentacją MQL5 i pomocą MetaTrader 5; ostrzeżenia o overfittingu i kosztach za Pardo (2008) i López de Prado (2018)."
date: 2026-07-12 18:00:00 +0200
eyebrow: "Programowanie · optymalizacja"
category: edukacja
dek: "Optymalizacja w testerze nie tworzy przewagi, tylko dopasowuje parametry do danych, które już się wydarzyły. Ten tekst rozkłada praktykę na części: pełny przegląd kontra genetyka, mapa wyników i różnica między pikiem a plateau, forward test i walk-forward efficiency, własne kryterium w OnTester zamiast samego zysku. Wszystko na faktach z dokumentacji, bez obietnic wyniku."
readingTime: 9
tags: [programowanie, MQL5, optymalizacja, "walk-forward", genetyczna, overfitting, MetaTrader, "Strategy Tester", OnTester, "forward test", Pardo, "López de Prado", edukacja]
---

> **W skrócie**
>
> - Tester MetaTrader 5 stroi parametry na dwa sposoby: pełny przegląd (slow complete algorithm) sprawdza każdą kombinację siatki, a szybki algorytm genetyczny (fast genetic based algorithm) dochodzi do dobrych obszarów przez selekcję, krzyżowanie i mutację, bez testowania wszystkich wariantów. Genetyka jest szybsza, ale stochastyczna i może ominąć globalne maksimum (pomoc MetaTrader 5).
> - Maksymalizacja jednej metryki, najczęściej salda końcowego, dopasowuje krzywą do szumu. Ten sam przebieg z umiarkowanym zyskiem, niskim obsunięciem i sensowną liczbą transakcji jest zwykle bardziej wiarygodny niż rekordowy zysk oparty na garstce transakcji.
> - Krajobraz wyników mówi więcej niż samo maksimum: pojedynczy wysoki pik, wokół którego sąsiednie ustawienia wypadają słabo, jest podejrzany, a szerokie plateau sąsiadujących, podobnie dobrych ustawień bardziej wiarygodne (Pardo, 2008).
> - Forward test dzieli okno na część optymalizacyjną i forward (1/2, 1/3, 1/4 lub własna data); najlepsze przebiegi z części pierwszej tester automatycznie sprawdza na forward, a wyniki trafiają na osobną zakładkę. Walk-forward efficiency to stosunek jakości forward do in-sample.
> - Optymalizacja niczego nie gwarantuje. Własne kryterium w OnTester (Custom max) pozwala oceniać przebiegi mądrzej niż samym profitem, ale ryzyko overfittingu i zniknięcia wyniku po kosztach zostaje. Uczciwą miarą jest rezultat out-of-sample po spreadzie i prowizji.

**Teza w jednym zdaniu:** Optymalizacja w MetaTrader 5, czy pełnym przeglądem, czy genetyką, nie tworzy przewagi, tylko dopasowuje parametry do przeszłości, więc jej jedynym uczciwym produktem jest wynik na danych, których procedura nie widziała podczas strojenia, a forward, walk-forward i własne kryterium służą wyłącznie temu, żeby to dopasowanie odróżnić od złudzenia.

## Dwa tryby optymalizacji: pełny przegląd i genetyka

Tester Strategii w MetaTrader 5 ma w ustawieniach pole wyboru trybu optymalizacji. Pierwszy to pełny przegląd (slow complete algorithm): tester uruchamia strategię dla każdej kombinacji parametrów z zadanej siatki. Siatkę definiuje się w zakładce wejść, podając dla każdego parametru wartość początkową, krok i wartość końcową. Metoda jest wyczerpująca i deterministyczna, ale liczba przebiegów rośnie iloczynowo: pięć parametrów po dwadzieścia wartości każdy to już ponad trzy miliony kombinacji, czyli wiele godzin liczenia.

Drugi tryb to szybki algorytm genetyczny (fast genetic based algorithm), który nie sprawdza wszystkich kombinacji. Według pomocy MetaTrader 5 działa etapami: z całej przestrzeni losowane są zestawy parametrów, a te o najlepszych wynikach zostają zachowane; następnie ich elementy są ze sobą krzyżowane, poddawane losowym mutacjom i inwersjom, a powstałe potomstwo znów sortuje się według wyniku i krzyżuje dalej. Proces trwa, dopóki wyniki się poprawiają, i zatrzymuje się, gdy przez kolejne pokolenia kryterium przestaje rosnąć. Dzięki temu genetyka dochodzi do dobrych obszarów siatki po ułamku przebiegów, jakich wymagałby pełny przegląd. Cena jest dwojaka: procedura jest stochastyczna, więc dwa uruchomienia mogą dać nieco inny wynik, i może utknąć w lokalnym maksimum, mijając globalne. Jest jeszcze trzeci tryb, testowanie tego samego zestawu na wszystkich symbolach z Market Watch, ale on służy do czego innego.

W kodzie parametr wystawia się do optymalizacji zwykłym input, a zakres ustawia się w testerze, nie w źródle. Słowo kluczowe sinput oznacza parametr statyczny, który celowo nie bierze udziału w optymalizacji.

```mql5
// Parametr do optymalizacji. Zakres Start/Krok/Stop ustawia sie
// w zakladce "Wejscia" testera, nie w kodzie zrodlowym.
input int   InpMaPeriod = 20;   // np. Start=10, Krok=5, Stop=60

// sinput = static input: celowo NIE bierze udzialu w optymalizacji.
sinput long InpMagic    = 20260712;
```

## Pułapka jednej metryki

Domyślnie tester szuka maksimum jednej liczby, najczęściej salda końcowego (Balance max). To właśnie tu rodzi się dopasowanie do szumu. Każdy szereg cenowy zawiera przypadkowe układy, które nigdy się nie powtórzą, a optymalizacja pod jedną metrykę wybiera ustawienie, które najlepiej w te konkretne przypadki trafiło. Rekordowy zysk in-sample potrafi wisieć na kilku szczęśliwych transakcjach, których na żywo nie da się powtórzyć.

MetaTrader 5 daje w zamian szereg kryteriów: obok Balance max są między innymi Profit Factor max, Expected Payoff max, Recovery Factor max, Sharpe Ratio max oraz kryterium minimalizujące obsunięcie kapitału. Osobno stoi Complex Criterion max, wprowadzony w buildzie 2615: to złożona miara jakości przebiegu, łącząca liczbę transakcji, obsunięcie, Sharpe, oczekiwaną wypłatę i recovery factor. Jego celem jest wybór przebiegu zrównoważonego, a nie po prostu najbardziej zyskownego. To krok w dobrą stronę, ale żadne wbudowane kryterium nie usuwa sedna problemu: przy dostatecznie gęstej siatce najlepszy wynik in-sample jest wysoki z samej konstrukcji, nawet gdy żadne ustawienie nie ma przewagi. O tej arytmetyce przeszukiwania jest osobny materiał o [data snoopingu](/dlogic-quant/2026/07/05/data-snooping-jak-finanse-sie-oszukuja/).

## Krajobraz wyników: pik kontra plateau

Optymalizacja nie zwraca jednej liczby, lecz całą powierzchnię: każdej kombinacji parametrów odpowiada jakiś wynik. W testerze widać to na zakładce wyników optymalizacji, dostępnej jako tabela oraz jako wykres. Gdy na osie mapy trafią dwa parametry, a wynik zostanie zakodowany kolorem, całość czyta się jak mapę terenu. Intuicja jest trójwymiarowa: parametry leżą na dwóch osiach, a wynik jest wysokością nad nimi.

Ten kształt mówi więcej niż samo maksimum. Pojedynczy, wysoki pik otoczony ustawieniami, które wypadają słabo, jest podejrzany: całość wisi na jednej wartości parametru, a krok w bok psuje wszystko. Taki szczyt to zwykle dopasowanie do przypadkowego układu w danych. Odwrotnie wygląda szerokie plateau, obszar sąsiadujących ustawień dających podobnie przyzwoite wyniki. Wtedy rezultat nie zależy od zgadnięcia jednej magicznej liczby i znosi drobne zmiany parametrów bez rozpadu. Pardo w "The Evaluation and Optimization of Trading Strategies" (2008) formułuje tę zasadę wprost: parametry bierze się ze środka stabilnego regionu, nie z izolowanego szczytu. Plateau nie dowodzi przewagi, ale jest warunkiem koniecznym wiarygodności: mechanizm działający tylko przy jednym ustawieniu na tysiąc prawie na pewno nie działa wcale.

## Forward test: podział okna na optymalizację i forward

Sam kształt krajobrazu nie wystarczy, bo wybór najlepszego ustawienia wciąż odbywa się na tych samych danych, na których policzono wyniki. Tester ma na to wbudowane narzędzie: forward test. W ustawieniach pole Forward pozwala podzielić zakres dat na dwie części w proporcji 1/2, 1/3, 1/4 albo według własnej daty. Pierwsza, wcześniejsza część to okno optymalizacji (in-sample), druga, późniejsza to okno forward (out-of-sample).

Mechanika jest prosta. Tester optymalizuje parametry wyłącznie na pierwszej części, a następnie najlepsze przebiegi automatycznie uruchamia na części forward, której podczas strojenia nie dotknął. Wyniki obu etapów trafiają na osobne zakładki, więc można je zestawić obok siebie. Ustawienie, które błyszczało in-sample, a na forward się rozpada, to klasyczny podpis przeoptymalizowania. Odwrotnie, zestaw parametrów, który trzyma się przyzwoicie na obu częściach, jest bardziej wiarygodny. To ten sam pomysł, co rozcięcie danych na część treningową i testową, tyle że wykonany w testerze jednym ustawieniem.

## Walk-forward i walk-forward efficiency

Pojedynczy forward to jedno okno out-of-sample. Walk-forward analysis rozwija ten pomysł w procedurę ruchomą: stroisz parametry na oknie, testujesz je na kolejnym, przylegającym oknie, przesuwasz oba w przód i powtarzasz, a sklejone odcinki out-of-sample tworzą jedną krzywą, bliższą temu, jak strategia działałaby na żywo. Wbudowany forward w MT5 odpowiada jednemu krokowi takiej analizy; pełną wersję kroczącą składa się zwykle z serii przebiegów testera po przesuwanych zakresach dat. Szkielet samej pętli, w oderwaniu od konkretnej platformy, rozłożony jest w materiale o [walk-forward w kodzie](/dlogic-quant/2026/07/12/optymalizacja-walk-forward-w-kodzie/).

Pardo (2008) wprowadza tu miarę o nazwie walk-forward efficiency: stosunek jakości osiągniętej na forward do jakości na oknie in-sample. Wartość bliska jedności albo wyższa sugeruje, że parametry przenoszą się poza okno strojenia, a wyraźny spadek jest sygnałem, że wynik in-sample był w dużej części dopasowaniem do szumu. To nie jest test istotności, tylko szybki wskaźnik, o ile realistyczny handel odbiega od wypolerowanej krzywej optymalizacji.

## Własne kryterium: OnTester zamiast profitu

Kryterium Custom max nie liczy żadnej ze standardowych metryk, tylko bierze wartość zwróconą przez funkcję OnTester w kodzie eksperta. Jej sygnatura to double OnTester(void), a według dokumentacji MQL5 jest wywoływana po zakończeniu przebiegu testu. W optymalizacji genetycznej wyniki w obrębie jednego pokolenia sortowane są malejąco właśnie po tej wartości: najwyższe uchodzą za najlepsze, a najsłabsze nie biorą udziału w tworzeniu następnego pokolenia. To znaczy, że własne kryterium wprost steruje kierunkiem poszukiwań.

W środku funkcji dane o przebiegu czyta się przez TesterStatistics, podając stałą z wyliczenia ENUM_STATISTICS. Poniżej profit netto zostaje skarcony obsunięciem kapitału, a przebiegi z garstką transakcji są odrzucane, bo nie mają mocy statystycznej.

```mql5
// OnTester: wywolywane po zakonczeniu przebiegu testu.
// Zwrocona wartosc = kryterium "Custom max" w optymalizacji.
double OnTester()
  {
   double profit = TesterStatistics(STAT_PROFIT);               // zysk netto
   double dd     = TesterStatistics(STAT_EQUITY_DDREL_PERCENT); // maks. obsun. kapitalu [%]
   int    trades = (int)TesterStatistics(STAT_TRADES);          // liczba transakcji

   // Za malo transakcji = brak mocy statystycznej: odrzuc przebieg.
   if(trades < 30)
      return(0.0);

   // Ten sam zysk przy mniejszym obsunieciu jest lepszy.
   if(dd < 0.01)
      dd = 0.01;                  // zabezpieczenie przed dzieleniem przez zero
   return(profit / dd);           // wlasna miara jakosci przebiegu
  }
```

Taka funkcja pozwala nagradzać stabilność zamiast surowego zysku i odsiewać przebiegi oparte na kilku transakcjach. Nie zmienia to jednak natury rzeczy: mądrzejsze kryterium lepiej prowadzi przeszukiwanie, ale samo w sobie nie tworzy przewagi.

## Optymalizacja nie tworzy przewagi

Warto powtórzyć to jasno: optymalizacja niczego nie tworzy, tylko dopasowuje. W najlepszym razie rozpoznaje strukturę, która istniała w danych niezależnie od strojenia; w najgorszym lepi z szumu kształt, który rozpada się przy pierwszym zetknięciu ze świeżymi notowaniami. Nawet komplet narzędzi, genetyka, forward i własne kryterium w OnTester, nie zdejmuje dwóch ryzyk.

Pierwsze to overfitting przez liczbę prób. Każde powtórzenie całej procedury, każda zmiana siatki czy kryterium to kolejna próba, a im więcej prób, tym wyżej trzeba postawić poprzeczkę, żeby wynik znaczył więcej niż przypadek. Forward sprawdza jedno okno, ale wielokrotne przestrajanie strategii pod jego rezultat zamienia i tę część w kolejny zbiór strojenia. Drugie ryzyko to koszty. Wynik z testera bywa liczony blisko brutto, a spread, prowizja i poślizg potrafią zamienić dodatni rezultat netto w ujemny. Uczciwa ocena wymaga realistycznych kosztów wpisanych w test, nie ich pominięcia.

Wspólny wniosek literatury jest trzeźwiący. López de Prado w "Advances in Financial Machine Learning" (2018) pokazuje, że po korekcie na liczbę prób i poza oknem, w którym dokonano wyboru, większość pozornych przewag znika. To nie jest wada metody, lecz jej działanie: normalnym produktem uczciwej optymalizacji jest odrzucenie, a nie kolejna zielona krzywa kapitału.

Materiał czysto edukacyjny o metodyce optymalizacji w testerze, nie porada inwestycyjna ani gotowa strategia. Opisane ustawienia i funkcje służą walidacji, nie obiecują wyniku; każdy zestaw parametrów wymaga oceny na danych out-of-sample i po realnych kosztach, zanim w ogóle rozważy się realny kapitał, a odpowiedzialność za ryzyko zostaje po stronie człowieka. Fakty o API opisano zgodnie z dokumentacją MQL5 i pomocą MetaTrader 5.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
