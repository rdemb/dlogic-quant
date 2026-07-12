---
title: "Feature engineering i etykietowanie: jak przygotować dane dla modelu"
description: "Dlaczego o wyniku modelu decydują cechy bardziej niż jego architektura: dobre cechy nie gwarantują przewagi, ale złe ją wykluczają. Cechy surowe kontra przetworzone, stacjonarność cech i różnicowanie ułamkowe jako kompromis między pamięcią a stacjonarnością, wyciek informacji z przyszłości przy ich tworzeniu. Do tego etykietowanie: słabość stałego horyzontu, metoda potrójnej bariery i meta-labeling, nierównowaga klas oraz ważność cech i jej pułapki. Źródła: López de Prado (2018) oraz Kaufman o cechach."
date: 2026-07-13 10:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
category: edukacja
dek: "Model dostaje dokładnie to, co mu się poda: zła reprezentacja danych wyklucza przewagę, zanim zacznie się dobór sieci. Kompendium bez hype o tym, jak buduje się cechy i etykiety: stacjonarność i różnicowanie ułamkowe, wyciek z przyszłości, metoda potrójnej bariery zamiast stałego horyzontu, meta-labeling, nierównowaga klas i pułapki ważności cech."
readingTime: 8
tags: ["uczenie maszynowe", "feature engineering", etykietowanie, "triple barrier", "meta-labeling", "López de Prado", "różnicowanie ułamkowe", stacjonarność, "look-ahead", "ważność cech", "nierównowaga klas", "data snooping", quant, edukacja]
---

> **W skrócie**
>
> - **Cechy ważą więcej niż wybór modelu.** Ten sam model karmiony różnymi cechami daje wyniki odległe o przepaść. Model nie widzi rynku, tylko tabelę liczb, którą się mu poda, i wydobędzie najwyżej tę strukturę, która już w niej jest. Stąd zasada: dobre cechy nie gwarantują przewagi, ale złe ją wykluczają.
> - **Stacjonarność kontra pamięć.** Surowa cena jest niestacjonarna, jej przyszłe poziomy wychodzą poza zakres widziany w treningu. Zwroty odzyskują stacjonarność, ale kasują pamięć szeregu. Różnicowanie ułamkowe (López de Prado, 2018) szuka najmniejszego rzędu różnicowania, który przechodzi test stacjonarności, zachowując maksimum pamięci.
> - **Etykieta to nie tylko znak następnego zwrotu.** Stały horyzont ignoruje ścieżkę i zmienność. Metoda potrójnej bariery (López de Prado, 2018) nadaje etykietę według tego, którą barierę cena dotknie pierwszą: górną (take profit), dolną (stop loss) czy pionową (czas).
> - **Meta-labeling odwraca zadanie ML.** Reguła podstawowa wyznacza stronę, a model wtórny, uczony na etykietach z potrójnej bariery, decyduje tylko, czy grać i ile ryzykować. ML odpowiada „z jaką pewnością", nie „w którą stronę".
> - **Ważność cechy bez kontroli prób kłamie.** Przy wielu kandydujących cechach któraś wyjdzie na ważną czystym trafem. To data snooping przeniesiony na poziom cech, więc wysoka ważność jest hipotezą do sprawdzenia poza próbą, a nie dowodem.

**Teza w jednym zdaniu:** O wyniku modelu decyduje przede wszystkim reprezentacja danych, czyli cechy stacjonarne i wolne od wycieku z przyszłości oraz etykiety opisujące realny scenariusz handlowy, a nie architektura sieci, bo dobre cechy i etykiety nie gwarantują przewagi, lecz ich brak wyklucza ją, zanim padnie pierwsza linijka kodu modelu.

## Cechy ważą więcej niż model

Marketing uczenia maszynowego skupia uwagę na modelu: architektura sieci, liczba warstw, wybór algorytmu. Praktyka odwraca ten priorytet, bo obowiązuje tu stara reguła inżynierska: garbage in, garbage out. Model nie widzi rynku, widzi wyłącznie tabelę liczb, którą się mu poda, i potrafi wydobyć jedynie tę strukturę, która już w tej tabeli jest. Jeśli sygnał nie został zakodowany w cechach, żadna architektura go nie wyczaruje.

Stąd asymetria warta zapamiętania: dobre cechy nie gwarantują przewagi, ale złe ją wykluczają. Świetny zestaw cech jest warunkiem koniecznym, nie wystarczającym, bo nad nim wciąż wisi szum rynku, koszty i niestacjonarność. Zły zestaw, na przykład sam surowy poziom ceny, zamyka sprawę, zanim model wystartuje. Perry Kaufman w „Trading Systems and Methods" podkreśla, że to dobór i transformacja zmiennych wejściowych, a nie sam algorytm, odróżniają system reagujący na rynek od dopasowania do historii.

## Cechy surowe kontra przetworzone

Cechą surową jest to, co wychodzi wprost z rynku: poziom ceny, wolumen, surowe OHLC, znacznik czasu. Cecha przetworzona to transformacja tych danych, która ma wydobyć strukturę: zwrot zamiast poziomu, zmienność zamiast pojedynczej świecy, odległość ceny od średniej ruchomej zamiast samej ceny. Klasyczne wskaźniki techniczne to feature engineering pod inną nazwą: RSI, ATR czy pasma zmienności to funkcje ceny zaprojektowane tak, żeby odsłonić jakąś jej własność. Każda taka transformacja koduje hipotezę o tym, co na rynku jest istotne. Surowa cena tej hipotezy nie zawiera, dlatego jest kiepską cechą, i to nie z powodów kosmetycznych, tylko statystycznych.

## Stacjonarność cech: cena, zwroty, różnicowanie ułamkowe

Większość metod ML zakłada po cichu, że rozkład cech jest w miarę stały: to, czego model nauczył się na treningu, ma obowiązywać na danych, których jeszcze nie widział. Surowa cena łamie to założenie wprost. Jest niestacjonarna, oznaczana I(1): dryfuje, nie ma stałej średniej, a jej przyszłe wartości wychodzą poza zakres widziany w treningu. Model wytrenowany na kursie w wąskim przedziale traktuje późniejszy poziom jako teren nieznany, bo nigdy takich liczb nie oglądał.

Naturalną odpowiedzią jest różnicowanie: zamiast poziomu bierze się zwrot, czyli różnicę kolejnych cen. Zwroty są znacznie bliższe stacjonarnym, I(0), i to jest standardowy pierwszy ruch. Ma on jednak cichy koszt, na który zwraca uwagę López de Prado (2018): pełne różnicowanie kasuje pamięć szeregu. Zwrot mówi, o ile cena się zmieniła, ale gubi informację o tym, gdzie cena jest względem historii, a to często właśnie ta informacja niesie sygnał.

Stąd pomysł różnicowania ułamkowego (fractional differentiation). Zamiast różnicować w pełni, rzędem równym jeden, różnicuje się rzędem ułamkowym, gdzieś między zero a jeden. Rząd zero to surowa cena: pełna pamięć, brak stacjonarności. Rząd jeden to zwrot: pełna stacjonarność, znikoma pamięć. Rząd ułamkowy pośredni to kompromis: usuwa dokładnie tyle pierwiastka jednostkowego, ile trzeba, żeby szereg przeszedł test stacjonarności, a resztę pamięci zachowuje. López de Prado proponuje szukać najmniejszego rzędu, który jeszcze przechodzi test, bo to maksymalizuje zachowaną pamięć przy spełnionym warunku stacjonarności.

```
Kompromis pamięć kontra stacjonarność (López de Prado, 2018):

rząd d = 0        surowa cena  → pełna pamięć, NIEstacjonarna
rząd d = 1        zwrot        → stacjonarna, pamięć skasowana
rząd 0 < d < 1    ułamkowy     → część pamięci zachowana,
                                 stacjonarność osiągnięta

zasada: wybierz najmniejsze d, przy którym szereg
przechodzi test stacjonarności (np. ADF)
```

## Wyciek z przyszłości przy tworzeniu cech

Cechy buduje się z danych historycznych, więc to naturalne miejsce na wyciek informacji z przyszłości, czyli look-ahead. Cecha ma prawo używać wyłącznie tego, co było znane w chwili, do której jest przypisana. Złamanie tej zasady zamienia bezwartościowy model w pozornie genialny, bo cecha podpowiada mu odpowiedź. Najczęstsza wpadka nie jest efektowna: normalizacja cechy średnią i odchyleniem policzonymi na całym zbiorze, przed podziałem na trening i test. Taka statystyka zawiera dane z przyszłości, które wyciekają do zbioru testowego. Poprawnie parametry skalowania liczy się wyłącznie na treningu i te same nakłada na test.

Rodzina błędów jest szersza: cecha licząca statystykę z okna, które podgląda przyszłe świece, wartość z interwału, który jeszcze się nie domknął, albo agregat przypisany do początku okresu zamiast do jego końca. Osobne opracowanie na tym blogu rozkłada look-ahead na czynniki pierwsze, tutaj wystarczy zasada operacyjna: w chwili, w której cecha przyjmuje wartość, musiała być policzalna z samej przeszłości. Trzeba przy tym pamiętać o asymetrii między cechą a etykietą. Cecha może patrzeć tylko wstecz. Etykieta z definicji patrzy w przód, bo opisuje to, co stało się po decyzji, i to jest w porządku, dopóki nie przecieka z powrotem do cech.

## Etykietowanie: słabość stałego horyzontu

Najprostsze etykietowanie przypisuje obserwacji znak zwrotu po stałym horyzoncie, na przykład po ustalonej liczbie świec albo minut. Wygodne, ale wadliwe z dwóch powodów. Po pierwsze, ignoruje ścieżkę. Transakcja, która po drodze zeszłaby głęboko pod wodę i dotknęła stop lossa, a dopiero potem wróciła na plus, dostaje etykietę dodatnią, choć w realnym handlu zostałaby zamknięta ze stratą, zanim rynek zawrócił. Etykieta opisuje wtedy wynik niemożliwy do zrealizowania. Po drugie, stały horyzont ignoruje zmienność. Ta sama liczba świec znaczy co innego w rynku spokojnym i rozchwianym, a stały próg w pipsach etykietuje szum w reżimie cichym i przegapia ruch w reżimie zmiennym. Dobra etykieta powinna być skalowana zmiennością, nie sztywna.

## Metoda potrójnej bariery

Odpowiedzią López de Prado (2018) jest metoda potrójnej bariery. Zamiast pytać o znak zwrotu po stałym czasie, wokół każdego wejścia stawia się trzy bariery i sprawdza, którą rynek dotknie jako pierwszą. Bariera górna to poziom realizacji zysku, take profit. Bariera dolna to poziom stop lossa. Bariera trzecia jest pionowa, to maksymalny czas trzymania pozycji, czyli horyzont. Etykieta zależy od tego, która bariera zostaje przecięta najpierw: górna daje etykietę dodatnią, dolna ujemną, a jeśli pierwsze wygrywa ograniczenie czasowe, etykietą jest znak zwrotu w chwili wyjścia albo zero.

Kluczowe jest to, że bariery poziome skaluje się zmiennością, zwykle wielokrotnością bieżącej zmienności, więc szerokość take profitu i stop lossa oddycha razem z rynkiem. Dzięki temu etykieta odwzorowuje realny scenariusz handlowy: pozycję z jawnym zyskiem docelowym, jawną stratą maksymalną i jawnym limitem czasu, a nie abstrakcyjny zwrot po sztywnym oknie.

<figure>
<svg viewBox="0 0 640 384" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="26" font-size="13" fill="currentColor">Metoda potrójnej bariery: etykieta zależy od pierwszego dotknięcia</text><line x1="95" y1="58" x2="95" y2="300" stroke="currentColor" stroke-width="1" opacity="0.5"/><line x1="95" y1="300" x2="580" y2="300" stroke="currentColor" stroke-width="1" opacity="0.5"/><text transform="rotate(-90 32 182)" x="32" y="182" font-size="11" fill="currentColor" opacity="0.55" text-anchor="middle">cena</text><text x="574" y="316" font-size="11" fill="currentColor" opacity="0.55" text-anchor="end">czas</text><line x1="95" y1="92" x2="555" y2="92" stroke="#1a9e6a" stroke-width="2"/><text x="100" y="84" font-size="11" fill="#1a9e6a">górna bariera: take profit</text><line x1="95" y1="272" x2="555" y2="272" stroke="#e5484d" stroke-width="2"/><text x="100" y="266" font-size="11" fill="#e5484d">dolna bariera: stop loss</text><line x1="555" y1="92" x2="555" y2="272" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4" opacity="0.6"/><text transform="rotate(-90 545 182)" x="545" y="182" font-size="10.5" fill="currentColor" opacity="0.6" text-anchor="middle">bariera czasowa (horyzont)</text><line x1="95" y1="182" x2="555" y2="182" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.35"/><circle cx="95" cy="182" r="4" fill="currentColor"/><text x="102" y="176" font-size="10.5" fill="currentColor" opacity="0.6">wejście (t0)</text><path d="M95 182 L135 196 L175 168 L215 186 L255 156 L295 164 L335 128 L375 138 L415 106 L455 92" fill="none" stroke="currentColor" stroke-width="2.2" opacity="0.9"/><circle cx="455" cy="92" r="4.6" fill="#1a9e6a"/><text x="463" y="96" font-size="11" fill="#1a9e6a">etykieta +1</text><line x1="100" y1="331" x2="124" y2="331" stroke="#1a9e6a" stroke-width="3"/><text x="132" y="335" font-size="11" fill="currentColor" opacity="0.8">pierwsze dotknięcie górnej bariery → etykieta +1</text><line x1="100" y1="349" x2="124" y2="349" stroke="#e5484d" stroke-width="3"/><text x="132" y="353" font-size="11" fill="currentColor" opacity="0.8">pierwsze dotknięcie dolnej bariery → etykieta −1</text><line x1="100" y1="367" x2="124" y2="367" stroke="currentColor" stroke-width="3" stroke-dasharray="5 4" opacity="0.6"/><text x="132" y="371" font-size="11" fill="currentColor" opacity="0.8">najpierw bariera czasowa → etykieta 0 lub znak zwrotu</text></svg>
<figcaption>Ilustracja poglądowa. Wokół wejścia (t0) stawia się trzy bariery: górną (take profit, tu zielona), dolną (stop loss, tu czerwona) i pionową barierę czasową wyznaczającą maksymalny czas trzymania pozycji. Etykietę nadaje ta bariera, którą cena dotknie jako pierwsza: górna daje etykietę dodatnią, dolna ujemną, a jeśli pierwsze wygrywa ograniczenie czasowe, etykietą jest znak zwrotu w chwili wyjścia albo zero. Bariery poziome skaluje się zwykle bieżącą zmiennością, więc ich szerokość oddycha razem z rynkiem. Na rysunku ścieżka dotyka najpierw bariery górnej, co daje etykietę dodatnią. Za López de Prado (2018).</figcaption>
</figure>

## Meta-labeling: model wtórny decyduje, czy grać

Metoda potrójnej bariery prowadzi wprost do meta-labelingu, drugiego pomysłu López de Prado (2018). Model podstawowy, na przykład reguła albo decyzja tradera, wyznacza stronę: long albo short. Dopiero na to nakłada się model wtórny, klasyfikator ML, którego jedynym zadaniem jest ocena, czy dany sygnał zagrać, i jak duży postawić na niego zakład. Etykiety do tego wtórnego modelu dostarcza właśnie potrójna bariera: uczy się on rozpoznawać, które sygnały strony podstawowej kończą się dotknięciem bariery zysku, a które bariery straty. ML odpowiada tu na pytanie „z jaką pewnością", nie „w którą stronę", co jest zadaniem lepiej postawionym i o wyższym stosunku sygnału do szumu niż wróżenie kierunku z surowej ceny.

## Nierównowaga klas

Etykietowanie niemal zawsze rodzi nierównowagę klas. Sygnałów wartych zagrania jest z natury mniej niż okazji do przeczekania, a w rynku trendującym jedna strona dominuje nad drugą. Klasyfikator, który po prostu zawsze typuje klasę większościową, osiąga wysoką trafność i jest zupełnie bezużyteczny, bo nie niesie żadnej informacji. Dlatego surowa trafność (accuracy) jest przy nierównowadze myląca, a patrzeć trzeba na miary wrażliwe na klasę rzadszą, jak precyzja, czułość albo F1. Praktyczne przeciwdziałania to ważenie próbek, tak by rzadsza klasa liczyła się mocniej, oraz techniki przepróbowania. Sama nierównowaga nie jest błędem danych, tylko własnością problemu, ale zignorowana zamienia dobre etykiety w bezwartościowy model.

## Ważność cech i jej pułapki

Gdy model już działa, pojawia się pytanie, które cechy naprawdę pracują. Odpowiada na nie analiza ważności cech (feature importance). López de Prado (2018) rozróżnia metody działające wewnątrz próby, jak spadek nieczystości drzewa (MDI), od metod działających poza próbą, jak permutacyjny spadek trafności (MDA), w którym miesza się wartości jednej cechy i mierzy, ile na tym traci model. Metody in-sample bywają obciążone, na przykład MDI faworyzuje cechy o wielu poziomach, więc rozstrzygać powinny miary out-of-sample.

Największa pułapka jest jednak ta sama, która truje cały quant: istotność z przypadku. Przy wielu kandydujących cechach i skończonych, zaszumionych danych któraś cecha wyjdzie na ważną czystym trafem, tak samo jak najlepsza z tysiąca losowych strategii wygląda świetnie z samej konstrukcji eksperymentu. To jest data snooping przeniesiony z poziomu strategii na poziom cech, i ma na tym blogu osobne opracowanie. Do tego dochodzą efekty podstawienia: dwie silnie skorelowane cechy dzielą się ważnością i obie wyglądają na słabe, choć razem niosą sygnał. Wniosek jest ostrożny: wysoka ważność cechy to hipoteza do sprawdzenia poza próbą i z kontrolą liczby prób, nie dowód, że cecha niesie realną informację.

## Co z tego wynika

Kolejność priorytetów w budowie modelu jest odwrotna do tej, którą sprzedaje marketing. Najpierw reprezentacja danych: cechy stacjonarne, ale z zachowaną pamięcią, liczone wyłącznie z przeszłości. Potem etykiety, które opisują realny scenariusz handlowy, z jawnym zyskiem, stratą i limitem czasu, a nie abstrakcyjny zwrot po sztywnym oknie. Dopiero na końcu model, i to raczej skromny niż efektowny. Dobre cechy i uczciwe etykiety nie gwarantują przewagi, bo nad wszystkim wisi szum, koszty i niestacjonarność rynku. Ale ich brak przewagę wyklucza, zanim padnie pierwsza linijka kodu modelu. To jest asymetria, dla której cała ta żmudna praca przed modelem się opłaca.

Materiał czysto edukacyjny, nie porada inwestycyjna ani obietnica przewagi. Opisane techniki, potrójna bariera, różnicowanie ułamkowe, meta-labeling czy analiza ważności cech, to narzędzia porządkujące dane i etykiety, a nie sposób na pewny zysk. Pewne jest tu wyłącznie jedno: model wydobędzie najwyżej tyle, ile zakodowano w cechach, a zignorowanie stacjonarności, wycieku z przyszłości albo liczby prób zamienia porządną z pozoru analizę w dopasowanie do szumu.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
