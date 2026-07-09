---
title: "ML w tradingu: co naprawdę działa, a co jest marketingiem"
description: "Naiwne uczenie maszynowe na surowej cenie zwykle zawodzi: niski stosunek sygnału do szumu, niestacjonarność i overfitting zjadają wynik. Gdzie ML realnie pomaga (meta-labeling, prognoza zmienności, egzekucja, przekrój rynku), dlaczego prosty model liniowy bywa lepszym benchmarkiem niż transformer i czemu walidacja waży więcej niż architektura. Źródła: López de Prado, Kelly i Xiu, praca o DLinear, przeglądy reinforcement learning."
date: 2026-07-09 19:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
category: edukacja
dek: "Uczenie maszynowe w tradingu to nie wyrocznia cenowa, tylko zestaw narzędzi do wąskich podproblemów. Kompendium bez hype'u: dlaczego naiwne sieci na cenie przegrywają z szumem, gdzie ML naprawdę pomaga i czemu o wyniku decyduje walidacja, a nie rozmiar modelu."
readingTime: 8
tags: ["uczenie maszynowe", "machine learning", "meta-labeling", "López de Prado", "Kelly i Xiu", DLinear, transformery, overfitting, walidacja, "reinforcement learning", "szeregi czasowe", quant, Forex]
---

> **W skrócie**
>
> - **Naiwne ML na surowej cenie zwykle zawodzi**, i to z trzech niezależnych powodów: niski stosunek sygnału do szumu (przewidywalna część zwrotów to ułamek wariancji), niestacjonarność (proces generujący dane zmienia się pod modelem) oraz overfitting (model o dużej pojemności zapamiętuje szum jako strukturę). To nie jest problem doboru sieci, tylko własność rynku.
> - **Meta-labeling to zdrowe zastosowanie ML.** Model nie generuje sygnału. Reguła podstawowa decyduje o stronie (long albo short), a model ML decyduje tylko, czy w ogóle grać i ile ryzykować. ML odpowiada na pytanie „z jaką pewnością", nie „w którą stronę" (López de Prado, 2018).
> - **Prosty model to nie gorszy model.** Jednowarstwowy model liniowy DLinear dorównał złożonym transformerom, a często je przewyższył, na standardowych benchmarkach prognozowania szeregów czasowych (Zeng i wsp., 2023). Jeśli wielka sieć nie bije naiwnej persystencji ani modelu liniowego, nie wnosi nic poza ryzykiem przeuczenia.
> - **Walidacja waży więcej niż architektura.** Typowa porażka to nie zła sieć, tylko przeciekający albo przeszukany backtest. Purged cross-validation, walk-forward oraz Deflated Sharpe i PBO rozstrzygają więcej niż liczba warstw.

**Teza w jednym zdaniu:** uczenie maszynowe nie jest maszyną do przewidywania ceny, tylko narzędziem do konkretnych podproblemów (filtrowania sygnału, prognozy zmienności, egzekucji, przekroju rynku), a o tym, czy realnie działa, decyduje dyscyplina walidacji, nie rozmiar sieci.

## Punkt wyjścia: ML to nie wyrocznia cenowa

Marketing sprzedaje jedną obietnicę: dosypać danych, postawić większą sieć, a ona nauczy się przewidywać cenę. Inżynieria dostarcza coś zupełnie innego: zestaw aproksymatorów funkcji, które działają wtedy, gdy problem jest dobrze postawiony, a danych jest dużo w stosunku do złożoności wzorca. Rynek jest dla takiego założenia środowiskiem wrogim. Jest adaptacyjny (gdy edge staje się znany, zostaje zarbitrażowany), przeciwnika ma inteligentnego, a jego zwroty na krótkim horyzoncie to niemal czysty szum.

Dlatego uczciwe pytanie nie brzmi „czy ML działa w tradingu", tylko „na jakim podproblemie i pod jaką walidacją". To rozróżnienie oddziela narzędzie od magii. Ta sama regresja gradient boosting, która potrafi realnie poprawić prognozę zmienności, na zadaniu „zgadnij kierunek następnej świecy" będzie produkować głównie przeuczony szum. Nie dlatego, że jest zła, tylko dlatego, że drugie zadanie prawie nie zawiera sygnału do wyuczenia.

## Dlaczego naiwne ML na surowej cenie zawodzi

Pierwszy powód to stosunek sygnału do szumu. W zwrotach finansowych na krótkim horyzoncie przewidywalna część to ułamek całej wariancji, reszta to szum. Model o dużej pojemności ma dość parametrów, żeby dopasować się do tego szumu i przedstawić go jako regularność. Im większa sieć, tym więcej sposobów, żeby znaleźć wzorzec, którego nie ma.

Drugi powód to niestacjonarność. Większość metod ML zakłada po cichu, że rozkład danych treningowych jest ten sam, co rozkład danych, na których model potem działa. Na rynku ta zgodność nie zachodzi. Reżimy się zmieniają, polityka banków centralnych się zmienia, mikrostruktura się zmienia, a model dostrojony do jednego reżimu degraduje się, gdy reżim się obraca. Co gorsza, cel jest ruchomy w sposób adwersaryjny: jeśli wzorzec naprawdę zarabia i zostanie odkryty, kapitał go zamyka.

Trzeci powód to overfitting spleciony z przeciekiem danych. Duża pojemność modelu plus przeszukiwanie wielu architektur i hiperparametrów gwarantuje, że najlepszy wynik będzie zawyżony przez samo szukanie. Do tego dochodzą pułapki specyficzne dla szeregów czasowych: nakładające się etykiety i autokorelacja łamią założenia zwykłej walidacji krzyżowej, a przypadkowe wstawienie informacji z przyszłości (look-ahead) potrafi zamienić bezwartościowy model w pozornie genialny. To jest dokładnie ten mechanizm, który karze Deflated Sharpe Ratio: liczba wypróbowanych prób podnosi poprzeczkę istotności, a naiwna miara jakości tego nie widzi.

## Prosty model to nie gorszy model

W 2023 roku Zeng i współautorzy zadali w tytule pracy złośliwe pytanie: czy transformery są w ogóle skuteczne w prognozowaniu szeregów czasowych. Odpowiedzią był DLinear, model tak prosty, że mieści się w jednej warstwie liniowej. Na standardowych, publicznych benchmarkach prognozowania długiego horyzontu dorównał on rozbudowanym architekturom transformerowym, a na wielu zbiorach je przewyższył. To nie jest anegdota o jednym datasecie, to systematyczny sygnał ostrzegawczy: złożoność architektury sama w sobie nie kupuje jakości prognozy.

Powód jest statystyczny, nie ideologiczny. Przy niskim stosunku sygnału do szumu wariancja estymatora dominuje nad jego obciążeniem. Prosty model ma niższą wariancję i mniej sposobów, żeby dopasować się do szumu, więc w takim reżimie wygrywa nie dlatego, że jest mądrzejszy, tylko dlatego, że jest skromniejszy. Stąd praktyczna dyscyplina benchmarku:

```
Zanim uwierzysz w model, pobij po kolei:
1. naiwną persystencję   (prognoza: jutro = dziś)
2. model liniowy         (regresja na kilku sensownych cechach)
3. dopiero potem sieć czy transformer ma prawo się liczyć
```

Zaskakująco wiele efektownych wyników „state of the art" wyparowuje na pierwszym albo drugim szczeblu tej drabiny. Jeśli wielka sieć nie potrafi pobić naiwnej persystencji, nie odkryła żadnego wzorca, tylko dołożyła ryzyko przeuczenia i koszt obliczeń.

## Walidacja waży więcej niż architektura

Największa dźwignia w ML dla rynków nie siedzi w wyborze modelu, tylko w protokole sprawdzania. Szeregi czasowe mają kierunek, więc walidacja musi respektować przyczynowość: nigdy nie mieszaj (shuffle) obserwacji, trenuj na przeszłości, testuj na przyszłości. López de Prado opisuje na to konkretne narzędzia: purged cross-validation, która usuwa z próby treningowej etykiety nakładające się w czasie z próbą testową, oraz embargo, które dokłada bufor po każdym cięciu. Bez tego model podgląda własną odpowiedź i backtest kłamie.

Druga warstwa dyscypliny to problem wielokrotnego testowania. Każda dodatkowa próbowana konfiguracja podnosi oczekiwane maksimum wyniku pod hipotezą zerową, więc „najlepszy" model z gridu jest z definicji zawyżony. Deflated Sharpe Ratio deflauje wynik o liczbę prób, a PBO (probability of backtest overfitting) szacuje, jak często zwycięzca in-sample wypada poniżej mediany out-of-sample. Wniosek jest niewygodny dla zwolenników coraz większych sieci: skromny model uczciwie zwalidowany bije efektowny model na przeciekającym backteście za każdym razem. Godzina włożona w protokół walidacji zwraca się mocniej niż tydzień strojenia architektury.

## Meta-labeling: ML jako filtr, nie generator

Najzdrowsze zastosowanie ML w tradingu odwraca zwykłą intuicję. Zamiast kazać modelowi zgadywać kierunek, dajesz mu do oceny gotowy sygnał. To jest meta-labeling z „Advances in Financial Machine Learning" López de Prado (2018). Architektura ma dwa piętra:

```
Model podstawowy (reguła, dyskrecja)  ->  decyduje STRONĘ  (long / short)
Model wtórny (klasyfikator ML)        ->  decyduje CZY grać i ILE ryzykować (0..1)
```

Model podstawowy, na przykład prosta reguła albo decyzja tradera, wyznacza stronę. Model wtórny uczy się tylko jednej rzeczy: które z tych sygnałów są warte zagrania, a które to fałszywe alarmy, i jak duży postawić na nie zakład. ML odpowiada więc na pytanie „z jaką pewnością i za ile", a nie „w którą stronę". To przesunięcie ma trzy zalety. Po pierwsze, jest to problem klasyfikacji z sensowniejszym stosunkiem sygnału do szumu niż surowa prognoza ceny. Po drugie, poprawia precyzję, bo tnie fałszywe pozytywy tam, gdzie reguła podstawowa jest zawodna. Po trzecie, naturalnie łączy się z zarządzaniem ryzykiem, bo wyjście modelu można potraktować jako frakcję wielkości pozycji. To wciąż nie magia, ale to jest dobrze postawione zadanie, a nie próba wywróżenia rynku.

## Gdzie ML naprawdę pomaga

Poza meta-labelingiem jest cały zestaw podproblemów, w których ML realnie dokłada wartość, bo wszystkie mają wspólny mianownik: dużo danych, dobrze zdefiniowany cel i tolerancję na wiele słabych predyktorów naraz.

Prognoza zmienności jest przewidywalna dużo bardziej niż kierunek, bo zmienność się klastruje (skupia w seriach), więc modele nieliniowe potrafią poprawić prognozy realized volatility używane do sizingu i wyceny ryzyka. Egzekucja i modelowanie wpływu na rynek (market impact) to zadanie z jasno mierzalnym kosztem, idealne dla uczenia. Odszumianie macierzy kowariancji i konstrukcja portfela (na przykład hierarchical risk parity López de Prado) korzystają z metod ML do stabilizacji estymatorów, gdy aktywów jest dużo, a próby mało. NLP na newsach i sentymencie zamienia tekst w cechy, których model cenowy sam nie ma.

Osobny, ważny przypadek to przekrój rynku. Gu, Kelly i Xiu (2020) oraz przeglądowa praca Kelly i Xiu (Financial Machine Learning, 2023) pokazują, że metody ML poprawiają prognozę przekrojową zwrotów względem modeli liniowych, gdy masz szeroki panel aktywów i wiele cech. Ale to jest inna gra niż intraday na jednej parze: niska częstotliwość, ogromne N instrumentów, a wartość bierze się z ujarzmienia wielu słabych, nieliniowo współdziałających predyktorów, nie z jednej mocnej wyroczni. Sukces w tej domenie nie przenosi się automatycznie na „zgadnij następną świecę EURUSD".

## Reinforcement learning: obietnica i pułapka

Reinforcement learning kusi najmocniej, bo obiecuje ominąć problem prognozy: zamiast przewidywać cenę, ucz agenta polityki działania wprost, a on sam nauczy się kupować, sprzedawać i wychodzić. Przeglądy tej literatury (na przykład Hambly, Xu i Yang, 2023) studzą entuzjazm. RL jest ekstremalnie głodny próbek, a historia rynku to w praktyce jedna albo kilka ścieżek, więc agent łatwo przeucza się do tej konkretnej przeszłości. Projektowanie funkcji nagrody jest kruche (mała zmiana nagrody, inne zachowanie), niestacjonarność podkopuje wyuczoną politykę, a większość opublikowanych sukcesów nie przeżywa realistycznych kosztów transakcyjnych i uczciwego out-of-sample.

Realne zwycięstwa RL są wąskie i konkretne: optymalna egzekucja i harmonogramowanie zleceń, gdzie istnieje dobry symulator i jasno zdefiniowany koszt do minimalizacji. To cenne, ale to nie jest skrót omijający problem sygnału. RL nie wyczaruje przewagi tam, gdzie jej nie ma, przesuwa tylko trudność z prognozy na projekt środowiska i nagrody.

## Co z tego wynika przy stole

Uczciwa mapa jest prosta. Uczenie maszynowe to skrzynka narzędzi do dobrze postawionych podproblemów: filtrowania i sizingu istniejącego sygnału (meta-labeling), prognozy zmienności, egzekucji, odszumiania portfela, rankingu przekrojowego. Nie jest to wyrocznia, która z surowej ceny jednego instrumentu wyprodukuje kierunek. Marketing sprzedaje wyrocznię, bo dobrze się sprzedaje. Inżynieria dostarcza narzędzia, bo tylko one przechodzą walidację.

Wiążącym ograniczeniem prawie nigdy nie jest rozmiar modelu, tylko dyscyplina sprawdzania. Zanim postawisz na dowolnym modelu pieniądze, warto zadać cztery pytania: czy pobił naiwną persystencję i model liniowy, czy walidacja respektowała przyczynowość (bez shuffle, z purging i embargo), ile konfiguracji przeszukano, zanim ta wygrała, i czy wynik przeżywa deflację o tę liczbę prób. Model, który przechodzi ten filtr, jest skromniejszy, niż obiecuje marketing, ale za to prawdziwy.

To nie jest porada inwestycyjna. To uczciwa ocena narzędzia: gdzie ML w tradingu realnie pomaga, gdzie jest tylko hype, i jaką dyscypliną odróżnić jedno od drugiego, zanim zaufasz liczbie na wykresie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
