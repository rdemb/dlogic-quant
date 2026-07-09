---
title: "Deep learning w tradingu. Czy transformery naprawdę działają"
description: "Prognoza szeregów finansowych to wrogi teren dla sieci głębokich: niski stosunek sygnału do szumu, niestacjonarność i mało danych względem liczby parametrów. Kiedy transformery (Temporal Fusion Transformer, Momentum Transformer) realnie dokładają wartość, dlaczego prosty DLinear potrafi je pobić na benchmarkach i czemu o wyniku decyduje benchmark naiwny oraz walidacja, nie rozmiar sieci. Źródła: Lim i Zohren, Temporal Fusion Transformers, Momentum Transformer, DLinear (Zeng i wsp., 2023)."
date: 2026-07-08 15:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
category: edukacja
dek: "Deep learning obiecuje, że sieć sama wychwyci wzorce w cenie. Kompendium bez hype'u: dlaczego szeregi finansowe są dla niej wyjątkowo trudne, kiedy transformery naprawdę dokładają wartość, a kiedy prosty model liniowy wystarcza, i jak benchmark naiwny odróżnia jedno od drugiego."
readingTime: 8
tags: ["deep learning", "uczenie głębokie", transformery, LSTM, "Temporal Fusion Transformer", "Momentum Transformer", DLinear, "Lim i Zohren", "szeregi czasowe", overfitting, walidacja, "benchmark naiwny", quant, Forex]
---

> **W skrócie**
>
> - **Prognoza szeregów finansowych to wrogi teren dla sieci głębokich**, z trzech niezależnych powodów: niski stosunek sygnału do szumu (przewidywalna część zwrotów to ułamek wariancji), niestacjonarność (proces generujący dane zmienia się pod modelem) oraz mała liczba danych względem liczby parametrów (transformer ma miliony wag, a niezależnych obserwacji rynkowych są tysiące). To nie problem doboru sieci, tylko własność danych.
> - **Obietnica deep learningu to automatyczne wychwytywanie wzorców.** Zamiast ręcznie liczyć wskaźniki, sieć (LSTM, Temporal Fusion Transformer, Momentum Transformer) ma sama nauczyć się reprezentacji wprost z danych. W domenach z obfitością danych i mocnym sygnałem, jak obraz czy język, działa to spektakularnie; pytanie, czy przenosi się na rynek, gdzie sygnał jest nikły.
> - **Prosty model bywa lepszy od transformera.** Jednowarstwowy DLinear dorównał rozbudowanym architekturom transformerowym, a na wielu benchmarkach prognozy długiego horyzontu je przewyższył (Zeng i wsp., 2023). To podważa tezę, że złożoność zawsze pomaga: przy nikłym sygnale wygrywa model skromniejszy, bo ma mniej sposobów, żeby dopasować się do szumu.
> - **Benchmark naiwny to test sensu.** Zanim uwierzysz w sieć, musi pobić naiwną persystencję i model liniowy pod uczciwą walidacją (walk-forward, bez podglądania przyszłości). Jeśli nie bije, nie odkryła wzorca, tylko dołożyła ryzyko przeuczenia i koszt obliczeń.

**Teza w jednym zdaniu:** sieci głębokie nie są maszyną, która z surowej ceny wywróży kierunek; bywają realnie użyteczne, gdy danych i cech jest dużo, a interakcje są nieliniowe, ale o tym, czy naprawdę pomagają, decyduje pobicie naiwnego benchmarku pod uczciwą walidacją, nie rozmiar sieci i moda na architekturę.

## Obietnica: sieć, która sama znajdzie wzorzec

Deep learning zbudował swoją reputację na jednej rzeczy: uczeniu reprezentacji. W rozpoznawaniu obrazu i przetwarzaniu języka głębokie sieci wyparły ręcznie projektowane cechy, bo same nauczyły się wyciągać z surowych pikseli i tokenów struktury lepsze niż te, które wymyśliłby człowiek. Stąd naturalna pokusa w tradingu: zamiast liczyć średnie kroczące i RSI, wystarczy podać sieci surową cenę i wolumen, a ona sama znajdzie wzorce, których ręczna inżynieria cech nie widzi.

Ta obietnica jest szczera tam, gdzie spełnione są dwa warunki: danych jest bardzo dużo, a sygnał jest mocny. Sieć rozpoznająca koty ma miliony oznaczonych zdjęć i jednoznaczny cel. Model języka ma biliony tokenów i bogatą, powtarzalną strukturę. Rynek finansowy leży w przeciwległym rogu tej mapy: danych jest mało, a sygnał jest nikły. Zanim więc padnie pytanie o architekturę, trzeba zapytać, czy w ogóle jest się czego nauczyć.

## Dlaczego prognoza finansów to wrogi teren

Pierwszy powód to stosunek sygnału do szumu. Na krótkim horyzoncie przewidywalna część zwrotu to drobny ułamek wariancji, reszta to szum. Sieć głęboka to model o największej pojemności, więc jest maksymalnie narażona na jedną pułapkę: ma dość parametrów, żeby dopasować się do szumu i podać go jako regularność. Im większa pojemność, tym więcej sposobów na znalezienie wzorca, którego nie ma.

Drugi powód to niestacjonarność. Uczenie maszynowe zakłada po cichu, że dane treningowe i dane produkcyjne pochodzą z podobnego rozkładu. Na rynku ta zgodność nie zachodzi: reżimy się obracają, polityka banków centralnych się zmienia, mikrostruktura się zmienia. Sieć dostrojona do jednego reżimu degraduje się, gdy reżim się przełącza. Do tego cel jest ruchomy w sposób adwersaryjny, bo jeśli wzorzec naprawdę zarabia i zostanie odkryty, kapitał go zamyka.

Trzeci powód jest specyficzny dla sieci głębokich: liczba danych względem liczby parametrów. Transformer potrafi mieć miliony wag. Dwadzieścia lat danych dziennych to około pięciu tysięcy punktów; nawet na wysokiej częstotliwości efektywna liczba niezależnych obserwacji jest ograniczona przez autokorelację i trwałość reżimów. Miliony parametrów na tysiącach efektywnych próbek to podręcznikowy przepis na zapamiętywanie zamiast uogólniania. Sztuczki augmentacji danych, które ratują widzenie komputerowe (obrót, kadrowanie), nie mają czystego odpowiednika w przyczynowym szeregu cenowym, bo nie wolno mieszać czasu.

## Architektury i ich obietnica

LSTM to sieć rekurencyjna z bramkami, która uczy się zależności czasowych, zapamiętując istotne informacje i zapominając nieistotne; jej konstrukcja łagodzi zanikanie gradientu, przez co radzi sobie z dłuższą pamięcią niż zwykła rekurencja (Hochreiter i Schmidhuber, 1997). W tradingu ciekawym jej użyciem są Deep Momentum Networks (Lim, Zohren i Roberts, 2019): sieć uczy się sygnału trendu i wielkości pozycji od razu, optymalizując miarę zbliżoną do Sharpe'a, zamiast najpierw prognozować cenę, a potem osobno dobierać ryzyko. To sensowne przeramowanie problemu.

Temporal Fusion Transformer (Lim, Arık, Loeff i Pfister, 2021) łączy koder LSTM z mechanizmem uwagi. Obsługuje różne typy wejść (statyczne cechy, znane z góry wejścia przyszłe, obserwowane wejścia z przeszłości), ma sieci selekcji zmiennych, zwraca prognozy kwantylowe (czyli niepewność, a nie pojedynczy punkt) i pozwala odczytać, na co model patrzył. To realnie mocne narzędzie tam, gdzie prognozuje się wiele powiązanych szeregów naraz z bogatym zestawem zmiennych.

Momentum Transformer (Wood, Giegerich, Roberts i Zohren, Oxford-Man) idzie o krok dalej: przez mechanizm uwagi uczy się przełączać między podążaniem za trendem a powrotem do średniej w zależności od reżimu i adaptować wielkość pozycji, zachowując interpretowalność wag uwagi. Zastosowano go do przekroju kontraktów terminowych, i to jest bliższe uczciwemu użyciu deep learningu: wiele instrumentów, niska częstotliwość, uczenie zależności od reżimu. Szeroki przegląd tej rodziny metod dają Lim i Zohren (2021), i co ważne, robią to bez przemilczania ograniczeń.

## Kontrapunkt DLinear: prostszy potrafi wygrać

W 2023 roku Zeng i współautorzy zadali w tytule pracy prowokacyjne pytanie: czy transformery są w ogóle skuteczne w prognozowaniu szeregów czasowych. Odpowiedzią była rodzina jednowarstwowych modeli liniowych, z DLinear na czele, który rozkłada szereg na trend i resztę, a potem stosuje zwykłe warstwy liniowe. Na standardowych, publicznych benchmarkach prognozy długiego horyzontu te proste modele dorównały modnym architekturom transformerowym, a na wielu zbiorach je przewyższyły.

Powód jest statystyczny, nie ideologiczny. Rdzeń mechanizmu uwagi jest niewrażliwy na kolejność (permutacja wejść nie zmienia wyniku), a kodowanie pozycji tylko łata ten problem; tymczasem w szeregu czasowym to właśnie kolejność niesie najwięcej informacji. Gdy zależność jest w dużej mierze gładka i niemal liniowa, dodatkowa pojemność transformera kupuje wariancję, a nie sygnał. A przy nikłym stosunku sygnału do szumu wariancja estymatora dominuje nad obciążeniem, więc model skromniejszy wygrywa nie dlatego, że jest mądrzejszy, tylko dlatego, że ma mniej sposobów, żeby dopasować się do szumu.

Uczciwe zastrzeżenie: DLinear testowano na ogólnych benchmarkach prognozy (zużycie energii, ruch drogowy, pogoda, kursy), a nie na rachunku zysków i strat strategii. Wniosek metodologiczny przenosi się jednak na finanse tym mocniej, że tam sygnał jest jeszcze słabszy niż w tamtych zbiorach. Sens jest niezależny od domeny: złożoność musi zapracować na siebie, bijąc prosty punkt odniesienia, a zaskakująco często tego nie robi.

## Kiedy deep learning naprawdę ma sens

Sieci głębokie zwracają włożony w nie koszt, gdy problem ma trzy cechy naraz:

```
Deep learning zarabia na siebie, gdy:
1. danych jest dużo         (wysoka częstotliwość albo szeroki przekrój wielu instrumentów)
2. cech jest dużo           (arkusz zleceń, wolumen, wiele aktywów, news i dane alternatywne)
3. interakcje są nieliniowe (progi i zależność od reżimu, których model liniowy nie wyrazi)
```

Gdy wejścia są bogate i wielomodalne, uczenie reprezentacji ma z czego korzystać; gdy interakcje są prawdziwie nieliniowe, model liniowy strukturalnie ich nie złapie. Przełączanie reżimów w Momentum Transformerze jest tego przykładem. Kluczowy jest tu przekrój rynku: wartość bierze się z ujarzmienia wielu słabych, nieliniowo współdziałających predyktorów w szerokim panelu aktywów, a nie z jednej mocnej wyroczni na jednej parze.

Odwrotny biegun to przerost formy nad treścią: pojedynczy instrument, surowa cena, prognoza kierunku na krótki horyzont, mało danych i brak punktu odniesienia. W tym rogu transformer jest ozdobą, nie narzędziem. Sukces w bogatej domenie przekrojowej nie przenosi się automatycznie na „zgadnij następną świecę EURUSD".

## Test sensu: benchmark naiwny i walidacja

Największa dźwignia nie siedzi w architekturze, tylko w protokole sprawdzania. Zanim uwierzysz w sieć, musi przejść drabinę odniesień:

```
Zanim uwierzysz w sieć głęboką, pobij po kolei:
1. naiwną persystencję   (prognoza: jutro = dziś)
2. model liniowy         (regresja albo DLinear na sensownych cechach)
3. dopiero potem transformer ma prawo się liczyć
```

Zaskakująco wiele wyników „state of the art" wyparowuje na pierwszym albo drugim szczeblu. Do tego walidacja szeregu czasowego musi respektować przyczynowość: nigdy nie mieszaj obserwacji (shuffle), trenuj na przeszłości, testuj na przyszłości, tnij przecieki przez purging i embargo, licz realne koszty i uczciwy out-of-sample. Sieć głęboka ma jeszcze więcej pokręteł niż zwykły model (głębokość, szerokość, tempo uczenia, regularyzacja, ziarno losowe), więc przestrzeń przeszukiwania jest ogromna, a poprzeczka istotności powinna być odpowiednio wyższa. Osobna, typowa dla deep learningu pułapka to wynik zależny od ziarna: jeśli zmiana ziarna losowego decyduje o tym, czy model „działa", to model nie działa. Rzetelny raport pokazuje rozrzut po wielu ziarnach, nie jeden szczęśliwy przebieg.

## Co z tego wynika

Uczciwa mapa jest prosta. Deep learning to potężny aproksymator funkcji, który błyszczy przy obfitości danych, bogactwie cech i prawdziwej nieliniowości. Prognoza kierunku pojedynczego instrumentu na surowej cenie i krótkim horyzoncie to dokładnie ten róg, w którym jest najsłabszy, a naiwna persystencja i model liniowy są tam brutalnie uczciwym benchmarkiem. Transformery bywają realnie użyteczne (Temporal Fusion Transformer do bogatej, probabilistycznej prognozy wielu szeregów, Momentum Transformer do świadomego reżimu trendu w przekroju), ale to nigdy architektura jest powodem, że coś działa; powodem jest bogactwo danych i uczciwa walidacja.

Zanim postawisz na dowolnej sieci pieniądze, warto zadać cztery pytania: czy pobiła naiwną persystencję i model liniowy, czy walidacja respektowała przyczynowość (bez shuffle, z purging i embargo), ile konfiguracji i ziaren przeszukano, zanim ta wygrała, i czy wynik przeżywa realne koszty oraz deflację o liczbę prób. Po transformer sięga się wtedy, gdy problem ma dane i strukturę, które to uzasadniają, a nie dlatego, że nazwa dobrze się sprzedaje.

To nie jest porada inwestycyjna. To uczciwa ocena narzędzia: dlaczego szeregi finansowe są dla sieci głębokich wyjątkowo trudne, kiedy transformery naprawdę dokładają wartość, a kiedy to przerost formy nad treścią, i jaką dyscypliną odróżnić jedno od drugiego, zanim zaufasz liczbie na wykresie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
