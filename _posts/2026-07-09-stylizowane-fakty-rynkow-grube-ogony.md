---
title: "Stylizowane fakty rynków. Dlaczego Gauss kłamie o ryzyku"
description: "Rozkład zwrotów finansowych nie jest normalny i literatura wie o tym od dekad. Stylizowane fakty Ramy Conta (2001): grube ogony, klasterowanie zmienności, brak autokorelacji zwrotów przy silnej autokorelacji ich kwadratów oraz efekt dźwigni. Dlaczego modele gaussowskie, w tym naiwny VaR, systematycznie zaniżają ryzyko ogona."
date: 2026-07-09 20:30:00 +0200
eyebrow: "Edukacja · statystyka"
dek: "Rynki mają garść własności, które powtarzają się w akcjach, walutach i towarach niezależnie od epoki. Rozkład zwrotów ma grubsze ogony niż Gauss, zmienność się klastruje, kierunek jest prawie nieprzewidywalny, a zmienność już nie. Przegląd stylizowanych faktów Ramy Conta i tego, czemu normalność zaniża ryzyko."
readingTime: 7
tags: ["stylizowane fakty", "stylized facts", "grube ogony", "fat tails", leptokurtoza, "klasterowanie zmienności", "volatility clustering", autokorelacja, "efekt dźwigni", "leverage effect", "Rama Cont", Mandelbrot, VaR, "rozkład zwrotów", statystyka, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Stylizowane fakty to zestaw empirycznych własności zwrotów, które powtarzają się w różnych aktywach (akcje, waluty, towary), na różnych rynkach i w różnych epokach. Skatalogował je Rama Cont w pracy z 2001 roku, kontynuując obserwacje Benoita Mandelbrota z lat sześćdziesiątych. Wspólny mianownik jest jeden: rozkład zwrotów nie jest normalny.
> - Grube ogony oznaczają, że duże ruchy zdarzają się znacznie częściej, niż przewiduje krzywa Gaussa. Rozkład zwrotów jest leptokurtyczny, czyli ma wyższy i węższy szczyt oraz cięższe ogony niż rozkład normalny o tej samej wariancji. Ruchy kilkusigmowe, które w modelu normalnym byłyby zdarzeniem raz na wieki, w danych wracają co kilka lat.
> - Pamięć rynku siedzi w zmienności, nie w kierunku. Liniowa autokorelacja samych zwrotów jest bliska zeru, więc kierunku prawie nie da się wyczytać z przeszłych zwrotów. Za to autokorelacja kwadratów i wartości bezwzględnych zwrotów jest wyraźnie dodatnia i opada powoli. To jest klasterowanie zmienności: po spokoju idzie spokój, po burzy burza.
> - Reakcja bywa asymetryczna, a błędny model kosztuje. Spadki podnoszą przyszłą zmienność mocniej niż wzrosty tej samej wielkości (efekt dźwigni, najsilniejszy w akcjach i indeksach, słabszy i zależny od kontekstu na rynku walutowym). Każde narzędzie liczące ryzyko po gaussowsku, w tym naiwny VaR, zaniża prawdopodobieństwo dużej straty.

**Teza w jednym zdaniu:** Rozkład zwrotów nie jest normalny i nigdy nie był, ma grube ogony, pamięć zaszytą w zmienności zamiast w kierunku oraz asymetryczną reakcję na spadki, więc narzędzie liczące ryzyko po gaussowsku zaniża szansę na duży ruch dokładnie tam, gdzie kosztuje to najwięcej.

## Czym są stylizowane fakty

Termin „stylizowane fakty" pochodzi z ekonomii, gdzie oznacza obserwacje na tyle stabilne i powtarzalne, że każdy porządny model powinien je odtwarzać, ale na tyle ogólne, że nie wskazują jednego konkretnego modelu. Dla zwrotów z aktywów kanoniczny katalog takich własności zebrał Rama Cont w pracy „Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues" z 2001 roku. Ich siła bierze się z uniwersalności: te same wzorce widać w akcjach, indeksach, kursach walut i cenach towarów, na danych z różnych dekad i różnych stref czasowych. To nie są ciekawostki jednego rynku, tylko regularności, które trzymają się danych niezależnie od instrumentu.

Punktem wyjścia jest zwrot, najczęściej logarytmiczny, bo dobrze sumuje się w czasie i jest zbliżony do zwrotu prostego przy małych zmianach.

```
r_t = ln(P_t) - ln(P_{t-1})     zwrot logarytmiczny w okresie t
P_t                              cena zamknięcia okresu t
```

Naturalnym punktem odniesienia dla rozkładu takich zwrotów przez dekady był rozkład normalny, bo jest wygodny: opisują go dwie liczby (średnia i wariancja), a suma niezależnych zwrotów zmierza do niego na mocy centralnego twierdzenia granicznego. Kłopot w tym, że dane konsekwentnie odmawiają współpracy. Już Benoit Mandelbrot, analizując w latach sześćdziesiątych ceny bawełny, pokazał, że rozkład zmian cen jest zbyt „dziki" na krzywą Gaussa: ma za dużo ekstremów i za dużo spokoju naraz. Stylizowane fakty Conta są uporządkowaniem tej obserwacji w listę własności, które można sprawdzić na dowolnym szeregu.

## Grube ogony: duże ruchy nie są rzadkie

Pierwsza i najważniejsza własność dotyczy kształtu bezwarunkowego rozkładu zwrotów. Jest on leptokurtyczny, czyli w porównaniu z rozkładem normalnym o tej samej wariancji ma wyższy, węższy środek i wyraźnie cięższe ogony. Praktycznie znaczy to, że rynek przez większość czasu porusza się mniej, niż sugerowałby Gauss (stąd wysoki szczyt), a od czasu do czasu wykonuje ruch znacznie większy, niż Gauss dopuszcza (stąd grube ogony).

```
Kurtoza(r) = E[(r - μ)^4] / σ^4

rozkład normalny:   Kurtoza = 3   (odniesienie)
zwroty rynkowe:     Kurtoza > 3   (leptokurtoza, grube ogony)
```

Kurtoza mierzy właśnie masę w ogonach. Dla rozkładu normalnego wynosi 3 i to jest punkt odniesienia; dla zwrotów rynkowych wychodzi wyraźnie wyżej, i to tym wyżej, im krótszy horyzont (dane minutowe i dzienne są grubsze w ogonach niż miesięczne). Kształt samego ogona bada się osobno, dopasowując zależność potęgową.

```
P(|r| > x) ≈ x^(-α)     ogon opada jak potęga, nie wykładniczo

α = indeks ogona
α > 2  ⇒  wariancja istnieje, ale ogon i tak grubszy niż normalny
```

Ogon potęgowy opada wolniej niż wykładniczy ogon rozkładu normalnego, dlatego skrajne zdarzenia mają pod nim istotnie większe prawdopodobieństwo. Co ważne, przeglądy empiryczne (w tym praca Conta) znajdują indeks ogona skończony i zwykle większy od 2. To subtelna, ale ważna korekta pierwotnej hipotezy Mandelbrota: tak, ogony są grube, ale wariancja zwykle jednak istnieje, więc nie są to czyste stabilne prawa o nieskończonej wariancji. Zwroty siedzą gdzieś pomiędzy wygodnym Gaussem a dzikim rozkładem stabilnym, i właśnie ta pośrednia pozycja jest źródłem większości praktycznych kłopotów z ryzykiem.

## Klasterowanie zmienności: burza rodzi burzę

Druga własność dotyczy nie pojedynczego zwrotu, lecz układu zwrotów w czasie. Duże ruchy nie są rozsiane równomiernie, tylko skupiają się w seriach. Mandelbrot ujął to zdaniem, które stało się mottem całej dziedziny: duże zmiany bywają następowane przez duże zmiany dowolnego znaku, a małe przez małe. Po spokojnej sesji bardziej prawdopodobna jest kolejna spokojna, po gwałtownej kolejna gwałtowna. To zjawisko nazywa się klasterowaniem zmienności.

Kluczowe jest tu słowo „dowolnego znaku". Klasteruje się wielkość ruchu, a nie jego kierunek. Wysoka zmienność mówi, że jutro świeca może być duża, ale nie mówi, czy w górę, czy w dół. To rozróżnienie wraca w następnej własności i jest jednym z najbardziej praktycznych wniosków całej listy: przewidywalna bywa energia rynku, nie jego kierunek.

## Zwroty bez pamięci, zmienność z pamięcią

Trzecia własność to pozorny paradoks, który po rozłożeniu okazuje się spójny. Same zwroty są liniowo prawie nieskorelowane w czasie, ale ich kwadraty i wartości bezwzględne są skorelowane silnie i trwale.

```
Corr(r_t, r_{t+k}) ≈ 0        dla k ≥ 1 (poza skalą sekund i minut)
Corr(r_t^2, r_{t+k}^2) > 0    dodatnia i opadająca powoli z opóźnieniem k
Corr(|r_t|, |r_{t+k}|) > 0    często jeszcze wyraźniejsza niż dla kwadratów
```

Górny wiersz to statystyczna wersja słabej efektywności rynku: z samego znaku i wielkości wczorajszego zwrotu nie da się liniowo przewidzieć jutrzejszego, bo gdyby się dało, kapitał szybko zjadłby tę zależność. Jedyny wyjątek pojawia się na bardzo krótkich skalach (sekundy, pojedyncze minuty), gdzie efekty mikrostruktury, jak odbijanie się ceny między bid i ask, potrafią dać słabą, zwykle ujemną autokorelację. Poza tym kierunek jest praktycznie nieprzewidywalny liniowo.

Dolne wiersze mówią coś przeciwnego o zmienności. Autokorelacja kwadratów i modułów zwrotów jest dodatnia i, co istotne, opada wolno, wolniej niż wykładniczo, bardziej jak funkcja potęgowa. Ta powolność bywa interpretowana jako długa pamięć zmienności: ślad po dzisiejszym poruszeniu widać w danych jeszcze wiele okresów później. To jest ilościowy zapis klasterowania z poprzedniej sekcji i zarazem fundament, na którym stoją modele rodziny GARCH, opisujące zmienną w czasie, „lepką" wariancję zamiast stałej.

Warto dodać jeden niuans z listy Conta: nawet po odfiltrowaniu klasterowania modelem typu GARCH w resztach dalej zostają grube ogony, choć już cieńsze. Klasterowanie tłumaczy więc część leptokurtozy, ale nie całą. Ogon to osobne zjawisko, nie tylko produkt uboczny zmiennej zmienności.

## Efekt dźwigni: spadki straszą bardziej

Czwarta własność to asymetria między kierunkiem a zmiennością. Statystycznie zwroty są ujemnie skorelowane z przyszłą zmiennością: po spadku zmienność rośnie mocniej niż po wzroście tej samej wielkości.

```
Corr(r_t, σ_{t+k}) < 0     spadek dziś ⇒ wyższa zmienność jutro (przeciętnie)
```

Nazwa „efekt dźwigni" pochodzi od klasycznego wyjaśnienia dla akcji (Black, 1976): gdy kurs spółki spada, jej dług w relacji do kapitału własnego rośnie, spółka staje się bardziej „lewarowana", a jej akcje bardziej zmienne. Z tym zjawiskiem spokrewniona jest asymetria zysków i strat, którą Cont wymienia osobno: na akcjach i indeksach obserwuje się głębokie, gwałtowne spadki, którym nie odpowiadają równie gwałtowne wzrosty. Ogon strat bywa cięższy niż ogon zysków.

Tu jednak konieczne jest uczciwe zastrzeżenie, bo efekt nie jest uniwersalny. Najsilniej widać go na akcjach i indeksach giełdowych. Na rynku walutowym jest znacznie słabszy i zależny od kontekstu, bo para walutowa jest z definicji względna: spadek EUR/USD to jednocześnie wzrost USD/EUR, więc nie istnieje jeden globalny „zły kierunek", który zawsze podnosi zmienność. Asymetria na rynku walutowym pojawia się raczej wtedy, gdy jedna waluta pełni rolę bezpiecznej przystani, i przywiązuje się do konkretnej pary, a nie do rynku jako całości. Przenoszenie intuicji „spadek zawsze podnosi zmienność" wprost z akcji na waluty jest więc uproszczeniem, o którym trzeba pamiętać.

## Agregacja: na dłuższym horyzoncie Gauss wraca

Piąta własność jest pocieszająca i jednocześnie ostrzegawcza. W miarę wydłużania horyzontu, na którym liczy się zwrot (z minut na dni, z dni na tygodnie i miesiące), rozkład staje się coraz bliższy normalnemu. Nazywa się to gaussowskością agregacyjną i jest praktycznym przejawem centralnego twierdzenia granicznego działającego na sumach kolejnych zwrotów.

Wniosek jest asymetryczny w zależności od horyzontu. Grube ogony najmocniej uderzają tam, gdzie zwroty liczy się często, czyli w handlu intraday i dziennym. Inwestor o horyzoncie wielomiesięcznym widzi rozkład bliższy normalnemu i realnie mniej cierpi z powodu leptokurtozy. Kto działa na krótkich interwałach, ten mierzy się z najgrubszą wersją ogona, więc akurat dla niego założenie normalności jest najbardziej mylące.

## Dlaczego to ważne: naiwny VaR nie docenia ogona

Wszystkie te własności zbiegają się w jednym praktycznym punkcie: modele ryzyka, które zakładają normalność, systematycznie zaniżają prawdopodobieństwo dużych strat. Najczystszy przykład to naiwna wartość zagrożona (VaR) liczona wprost z rozkładu normalnego.

```
q_normal(1%) = μ - z · σ      z ≈ 2.33 dla poziomu 99%

q(1%) = próg 1% najgorszych zwrotów (kwantyl dolnego ogona)
z     = kwantyl rozkładu normalnego dla żądanej ufności
```

Mechanizm jest prosty. Kwantyl normalny (dla 99 procent około 2,33 odchylenia od średniej) zakłada, że dalej ogon opada wykładniczo. W prawdziwych danych ogon opada potęgowo, czyli wolniej, więc rzeczywisty próg jednego procenta najgorszych zwrotów leży dalej, a strata jest większa, niż mówi wzór normalny. Efekt: model obiecuje, że stratę większą od tego progu zobaczy się raz na sto sesji, a w danych takie przekroczenia zdarzają się częściej i bywają głębsze, niż zakładano. Do tego dochodzi klasterowanie, przez które przekroczenia nie są rozsiane równomiernie, tylko przychodzą seriami w tych samych burzliwych okienkach, dokładnie wtedy, gdy najtrudniej je udźwignąć.

Stąd biorą się poprawki, które weszły do standardu zarządzania ryzykiem: liczenie VaR z rozkładów o grubszych ogonach (na przykład t-Studenta), stosowanie teorii wartości ekstremalnych do samego ogona, uzupełnianie VaR o oczekiwaną stratę w ogonie (Expected Shortfall) oraz modele zmienności rodziny GARCH, które wprost odwzorowują klasterowanie. Każda z tych poprawek to reakcja na jeden ze stylizowanych faktów, a nie akademicka ozdoba.

Praktyczna lekcja domyka się bez żadnej porady inwestycyjnej. Rozkład zwrotów ma grube ogony, więc duże ruchy są normalniejsze, niż podpowiada nazwa krzywej Gaussa. Pamięć rynku jest w zmienności, nie w kierunku, więc przewidywalna bywa energia, a nie znak następnej świecy. Reakcja bywa asymetryczna, więc spadki i wzrosty nie znaczą tego samego dla przyszłej zmienności. Kto liczy ryzyko tak, jakby świat był gaussowski, ten nie tyle myli się w szczegółach, ile zaniża dokładnie tę wielkość, która najbardziej boli: prawdopodobieństwo i głębokość dużej straty.

To nie jest porada inwestycyjna. To opis empirycznych własności rozkładu zwrotów, znanych z literatury od Mandelbrota po Conta, po to, by odróżnić realny kształt ryzyka od jego wygodnej, gaussowskiej karykatury.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
