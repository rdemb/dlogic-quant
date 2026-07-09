---
title: "Jak rozpoznać reżim rynku. Trend, zakres, kryzys i modele stanów"
description: "Reżim rynku to ukryty stan (trend, zakres, kryzys), który decyduje, czy dana strategia zarabia, czy traci. Ukryte modele Markowa (HMM) szacują prawdopodobieństwo stanu ze zwrotów i zmienności, changepoint detection wykrywa moment jego pęknięcia, a intuicja GARCH tłumaczy, czemu zmienność chodzi stadami. Przegląd mechanizmów i prac: Hamilton, Rabiner, Adams i MacKay, Two Sigma."
date: 2026-07-09 16:00:00 +0200
eyebrow: "Edukacja · reżimy"
dek: "Ta sama strategia potrafi zarabiać w trendzie i oddawać wszystko w zakresie, a różnicą nie jest jej jakość, tylko reżim rynku. Modele stanów (HMM, GARCH, changepoint) szacują, w którym reżimie właśnie jest rynek. To filtr nadrzędny nad każdym systemem, a po polsku pisze o nim niewielu."
readingTime: 8
tags: [reżimy, HMM, "ukryte modele Markowa", changepoint, GARCH, GMM, "regime switching", Hamilton, Rabiner, "Adams & MacKay", "Two Sigma", trend, zakres, kryzys, zmienność, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Reżim rynku to utrzymujący się stan o określonych własnościach statystycznych: średnim zwrocie, zmienności i korelacjach. Ta sama strategia zarabia w jednym reżimie, a oddaje wszystko w innym, bo jej przewaga jest warunkowa względem procesu, który generuje ceny. Dlatego rozpoznanie reżimu jest filtrem nadrzędnym nad wyborem strategii, a nie kolejnym wskaźnikiem obok niej.
> - Trzy archetypy wystarczą do intuicji: spokój i trend (umiarkowana zmienność, kierunkowy dryf), zakres (niska zmienność, powrót do średniej, brak dryfu) oraz kryzys (eksplozja zmienności, grube ogony, korelacje skaczące do jedynki). Strategia dopasowana do jednego z tych stanów zwykle jest przeciwna do drugiego.
> - Ukryte modele Markowa (HMM) traktują reżim jako stan, którego nie widać wprost, ale który zdradza się rozkładem zwrotów i zmienności. Model szacuje prawdopodobieństwo, że rynek jest teraz w danym stanie, oraz prawdopodobieństwa przejść między stanami. Formalną podstawę dał Hamilton (regime switching), a klasyczny wykład algorytmów to tutorial Rabinera.
> - Wykrywanie zmiany reżimu (changepoint detection) pyta o co innego: nie w którym stanie jesteś, tylko czy przed chwilą proces pękł. Metoda online Adamsa i MacKaya utrzymuje rozkład czasu od ostatniej zmiany i sygnalizuje moment, w którym warto wyłączyć strategię, zanim nowy reżim się potwierdzi.

**Teza w jednym zdaniu:** Reżim rynku, czyli ukryty stan procesu generującego ceny, decyduje o tym, która strategia w ogóle ma sens, więc jego rozpoznanie (przez modele stanów, klasteryzację zmienności albo wykrywanie punktów zmiany) jest filtrem nadrzędnym, bo mówi nie w którą stronę pójdzie cena, tylko w jaką grę właśnie grasz.

## Reżim to nie prognoza kierunku, tylko opis środowiska

Reżim rynku to okres, w którym cena zachowuje się według w miarę stałego zestawu reguł statystycznych: charakterystyczny dryf (średni zwrot), charakterystyczna zmienność, charakterystyczna autokorelacja zwrotów i charakterystyczne korelacje z innymi rynkami. Kiedy te reguły się zmieniają, zmienia się reżim. To wszystko.

Najważniejsze zdanie o reżimie brzmi tak: reżim opisuje środowisko, a nie kierunek. Reżim trendowy mówi „ruchy mają skłonność do kontynuacji", reżim zakresowy mówi „ruchy mają skłonność do powrotu", a reżim kryzysowy mówi „ruchy są duże i skorelowane". Żaden z nich nie mówi, czy będzie w górę, czy w dół. To jest różnica między pytaniem „w jaką grę gramy" a pytaniem „jak się ta konkretna partia skończy".

Stąd bierze się mechanika, przez którą jedna strategia raz zarabia, raz traci, bez żadnego błędu w samej strategii. Przewaga strategii to eksploatacja jednej konkretnej reguły. Podążanie za trendem żywi się dodatnią autokorelacją zwrotów (momentum). Powrót do średniej żywi się autokorelacją ujemną. Gdy reżim odwraca znak tej autokorelacji, dokładnie te same reguły, które wcześniej zarabiały, zaczynają tracić, w sposób czysto mechaniczny. Nie zepsuł się system, zmieniło się środowisko, w którym on działa.

## Trzy archetypy: trend, zakres, kryzys

Do intuicji wystarczą trzy stany. Każdy ma inny podpis statystyczny, i to podpis, a nie nazwa, decyduje o tym, co w nim działa.

```
Reżim    Zmienność     Autokorelacja        Dryf         Co zwykle działa
trend    umiarkowana   dodatnia (momentum)  kierunkowy   podążanie za trendem
zakres   niska         ujemna (rewersja)    brak         powrót do średniej / fade
kryzys   wysoka        niestabilna          chaotyczny   redukcja ryzyka / bez pozycji
```

W trendzie zmienność jest umiarkowana i stabilna, wybicia się utrzymują, a zwroty wykazują dodatnią autokorelację na horyzoncie strategii. Zarabia tu momentum i podążanie za trendem, a fade oraz gra na powrót do średniej systematycznie krwawi, bo obstawia odwrócenie, które nie nadchodzi.

W zakresie zmienność jest niska, cena oscyluje wokół pewnej wartości, a zwroty wracają do średniej (autokorelacja ujemna). Zarabia fade i powrót do średniej, a systemy wybiciowe i trendowe są siekane przez fałszywe sygnały, bo każde wybicie gaśnie.

Kryzys jest jakościowo inny. Zmienność eksploduje, często do wielokrotności poziomu bazowego. Pojawia się gruby lewy ogon i ujemny skos. Korelacje między rynkami zbiegają do jedynki, więc dywersyfikacja paruje akurat wtedy, gdy jest najbardziej potrzebna. Poślizgi i luki się rozszerzają. Wielkość pozycji dobrana do spokojnej zmienności oznacza teraz znacznie większe realne ryzyko na tej samej liczbie lotów. Większość systemów pęka tu nie dlatego, że sygnał się odwrócił, tylko dlatego, że ryzyko na jednostkę pozycji nagle urosło kilkukrotnie.

## Dlaczego reżim jest filtrem nadrzędnym

Standardowy backtest miesza wszystkie reżimy w jednej próbie i podaje średnią. Ta średnia ukrywa najważniejszą rzecz: strategia mogła zarobić cały wynik w jednym reżimie i oddać część w drugim, a raport pokazuje różnicę jako jedną, gładką liczbę. Gdy zbramkujesz strategię reżimem, czyli włączasz ją tylko wtedy, gdy środowisko pasuje do jej przewagi, zostawiasz sobie dobrą część rozkładu i pomijasz złą. Dlatego rozpoznanie reżimu nie jest kolejnym wskaźnikiem obok strategii, tylko piętro wyżej: decyduje, którą strategię uruchomić albo czy w ogóle stać z boku.

Filtr ma sens tylko dlatego, że reżimy są lepkie. W modelach stanów widać to jako wysoką przekątną macierzy przejść: jeśli jesteś w danym stanie, najprawdopodobniej zostaniesz w nim jeszcze przez jakiś czas. Gdyby reżim przeskakiwał co świecę, jego wykrywanie nie miałoby wartości, bo zanim byś go rozpoznał, już by go nie było. Lepkość reżimu to warunek, który w ogóle czyni całą tę dyscyplinę użyteczną.

Jest jeszcze głębszy powód. Domyślne założenie większości backtestów brzmi: proces generujący ceny jest stacjonarny przez całą próbę. Modele reżimu istnieją właśnie po to, żeby to założenie odrzucić. Nie próbują przewidzieć kierunku, tylko przyznają wprost, że reguły gry zmieniają się w czasie, i próbują oszacować, które reguły obowiązują teraz.

## Zmienność chodzi stadami: intuicja GARCH

Zanim wprowadzi się dyskretne stany, warto zobaczyć najprostszy fakt reżimowy, jaki widać w danych: zmienność chodzi stadami. Duże ruchy następują po dużych, a spokój po spokoju. Zauważył to już Mandelbrot, a sformalizowały modele z rodziny ARCH i GARCH (Engle, Bollerslev). To ciągłe, miękkie spojrzenie na reżim.

GARCH(1,1) mówi, że dzisiejsza wariancja warunkowa jest ważoną sumą stałej, kwadratu wczorajszego szoku i wczorajszej wariancji.

```
σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}

σ²_t     = wariancja warunkowa na dziś
ε²_{t-1} = kwadrat wczorajszej niespodzianki w zwrocie
σ²_{t-1} = wczorajsza wariancja warunkowa
ω, α, β  = parametry (α + β blisko 1 = zmienność bardzo uporczywa)
```

Czyta się to tak: α mówi, jak mocno świeży szok wchodzi w zmienność, a β mówi, jak długo zmienność pamięta samą siebie. Gdy suma α + β jest bliska jedności, wybuch zmienności opada powoli, co jest dokładnie tym zjawiskiem, w którym kryzys „się rozlewa" i utrzymuje przez wiele dni.

Tu leży kluczowy kontrast z dalszą częścią. GARCH podaje ciągły poziom zmienności, a nie dyskretną etykietę. Mówi „wariancja jest teraz podwyższona", ale nigdy nie powie „jesteśmy w stanie numer dwa". Opisuje intensywność reżimu (jak dziko), a nie jego tożsamość (trend czy zakres). Do tożsamości potrzeba stanów dyskretnych, i to jest most do ukrytych modeli Markowa.

## Ukryte stany: model Markowa

Ukryty model Markowa (HMM) zakłada, że istnieje stan `s_t`, czyli reżim, którego nie widać wprost. Każdy stan „emituje" obserwacje (zwroty, zmienność zrealizowaną) losowane z rozkładu przypisanego do tego stanu. Sam stan zmienia się jak łańcuch Markowa: następny stan zależy wyłącznie od bieżącego, przez macierz przejść.

```
stan ukryty:  s_t ∈ {1, ..., K}          np. {spokój, trend, kryzys}
przejścia:    P(s_t = j | s_{t-1} = i) = A[i,j]     macierz przejść
emisje:       P(o_t | s_t = i)                       rozkład obserwacji w stanie i
Markow:       P(s_t | cała przeszłość) = P(s_t | s_{t-1})
```

Nie widzisz `s_t`. Widzisz strumień obserwacji `o_t` (zwroty i zmienność). Model wnioskuje z tego strumienia rozkład prawdopodobieństwa po stanach, czyli szacuje, z jaką szansą rynek jest teraz w każdym z reżimów. Rozkłady emisji mogą być wielowymiarowe: nie tylko zwrot, ale i zmienność czy skos. To właśnie pozwala rozdzielić trend od zakresu (oba bywają spokojne, różni je dryf i znak autokorelacji) oraz oba od kryzysu (który zdradza się przede wszystkim wariancją).

Do ekonomii i finansów przyniósł to Hamilton (1989) jako Markov regime switching: autoregresja, której parametry przełączają się wraz z ukrytym stanem Markowa, zastosowana najpierw do dynamiki wzrostu i recesji. Finansowe odczytanie jest proste: hossa i bessa, albo spokój i kryzys, jako ukryte stany z własną średnią i wariancją oraz z prawdopodobieństwem przełączenia między nimi. Rabiner z kolei dał kanoniczny, czytelny wykład samych algorytmów (pierwotnie dla rozpoznawania mowy), i jego trwała wartość polega na ujęciu HMM jako trzech pytań.

## Trzy pytania modelu HMM

Rabiner porządkuje całą maszynerię w trzy problemy, i warto je znać, bo każdy odpowiada na inne praktyczne pytanie.

```
1. Ocena:      P(obserwacje | model)              algorytm forward
2. Dekodowanie: najbardziej prawdopodobny stan     Viterbi / forward-backward
3. Uczenie:    estymacja A oraz rozkładów emisji   Baum-Welch (EM)
```

Ocena pyta, jak bardzo prawdopodobny jest zaobserwowany ciąg przy danym modelu. Służy do porównywania modeli i do sprawdzenia, czy dane w ogóle pasują do założonej struktury reżimów.

Dekodowanie pyta, jaki stan (albo cała ścieżka stanów) najlepiej tłumaczy obserwacje. Ma dwa smaki: pojedyncza najbardziej prawdopodobna ścieżka (Viterbi) albo prawdopodobieństwo każdego stanu w każdej chwili (forward-backward). Do odczytu reżimu na żywo interesuje cię wersja filtrowana, czyli `P(s_t | obserwacje do chwili t)`, bo korzysta wyłącznie z przeszłości.

Uczenie estymuje parametry, czyli macierz przejść i rozkłady emisji, z danych. Robi to algorytm Baum-Welch, odmiana EM, która na przemian zgaduje stany i przelicza parametry, aż się ustabilizują.

Tu jest miejsce na najważniejsze ostrzeżenie praktyczne, czyli przyczynowość i brak podglądania przyszłości. Dopasowanie HMM na całej próbie, a potem etykietowanie historycznych stanów, używa danych z przyszłości do orzekania o przeszłości, bo estymata wygładzona (smoothing) zerka do przodu. Powstaje z tego piękna, ale bezużyteczna mapa in-sample, która na żywo się nie powtórzy. Do czegokolwiek, co mogłoby dotykać decyzji, parametry muszą być ustalone na przeszłości, a stan musi być prawdopodobieństwem filtrowanym z informacji dostępnej w danej chwili. Inaczej sygnał reżimu „przemalowuje się" po fakcie.

Osobna decyzja to liczba stanów K. W praktyce zwykle od dwóch do czterech. Dwa stany (spokój kontra turbulencja) łapią już większość wartości, trzy dokładają rozdział trendu i zakresu, a powyżej tego rośnie ryzyko, że model zacznie dzielić szum na pseudoreżimy, które nie mają odpowiednika w rzeczywistości.

## GMM kontra HMM: klaster bez pamięci i stan z pamięcią

Two Sigma opisało podejście do reżimów oparte na mieszance rozkładów Gaussa (Gaussian Mixture Model, GMM). GMM grupuje obserwacje, czyli wektory cech w rodzaju zwrotu, zmienności i korelacji, w K gaussowskich skupień. Każdy okres zostaje przypisany do najbardziej prawdopodobnego skupienia. To jest właściwie model emisji z HMM, tylko pozbawiony struktury przejść.

Różnica jest jednym słowem: pamięć. GMM przypisuje każdą obserwację niezależnie, więc etykieta może migotać z świecy na świecę. HMM dokłada dokładnie to, czego GMM nie ma, czyli lepkość w czasie przez macierz przejść. Struktura Markowa mówi „skoro wczoraj byłeś w stanie spokojnym, dziś prawdopodobnie nadal w nim jesteś", co wygładza etykietowanie i odpowiada empirycznej lepkości reżimów.

```
GARCH   ciągła intensywność, bez etykiet     jak dziko jest teraz
GMM     dyskretne skupienia, bez pamięci     jakie są reżimy i jak wyglądają
HMM     dyskretne stany z macierzą przejść   w którym stanie jesteś teraz
```

Praktyczny podział jest taki: GMM jest prosty i szybki, dobry do eksploracji („ile jest reżimów i jak wyglądają"), ale jako przełącznik na żywo bywa nerwowy. HMM dokłada przejścia, więc etykiety są bardziej lepkie, a wykrywanie zwrotów bardziej zasadne, kosztem większej liczby parametrów i staranniejszego dopasowania. GARCH nie robi ani jednego, ani drugiego, ale najczyściej opisuje oś intensywności. W realnych układach te warstwy często współpracują: cechy w stylu GARCH karmią GMM albo HMM, którego stany dopiero bramkują strategię.

## Kiedy reżim pęka: wykrywanie punktów zmiany

Wykrywanie punktów zmiany (changepoint detection) zadaje inne pytanie niż HMM. Nie „w którym z K ustalonych stanów jesteś", tylko „czy proces generujący dane właśnie pękł". Nie trzeba z góry ustalać, jakie są stany.

Adams i MacKay (2007) podali metodę bayesowską działającą online (Bayesian Online Changepoint Detection). Centralnym obiektem jest długość biegu (run length) `r_t`, czyli liczba kroków od ostatniej zmiany. Algorytm utrzymuje rozkład prawdopodobieństwa po tej długości, aktualizowany po każdej nowej obserwacji, a funkcja hazardu koduje wcześniejsze przekonanie o tym, jak często zmiany się zdarzają.

```
run length:  r_t = liczba kroków od ostatniej zmiany reżimu
             r_t = r_{t-1} + 1     reżim trwa
             r_t = 0               właśnie nastąpiła zmiana

utrzymuj:    P(r_t | dane do t)    rozkład długości bieżącego reżimu
sygnał:      skok masy na r_t = 0  = prawdopodobny punkt zmiany
```

Mechanizm jest intuicyjny. Przy każdej nowej obserwacji model pyta, jak dobrze pasuje ona do parametrów oszacowanych z bieżącego biegu. Jeśli pasuje, długość biegu rośnie, a pewność co do trwającego reżimu się umacnia. Jeśli obserwacja jest skrajnie mało prawdopodobna w świetle bieżącego biegu, masa prawdopodobieństwa przeskakuje na długość zero, sygnalizując, że stary reżim właśnie się skończył.

Dla decyzji przy stole ważne jest słowo online: model aktualizuje się przyczynowo, obserwacja po obserwacji, tylko z przeszłości, więc potrafi zgłosić pęknięcie niemal w czasie rzeczywistym, a nie długo po fakcie. Zastosowanie jest defensywne. Skok prawdopodobieństwa zmiany to sygnał, żeby zredukować albo wyłączyć strategię, której przewaga zakładała stary reżim, zanim nowy się potwierdzi i zanim wolniejszy HMM zdąży przeetykietować stany.

Jest oczywisty kompromis: czułość kontra fałszywe alarmy. Wysoki hazard zgłasza zmiany ochoczo (dużo fałszywych trafień, piłowanie), niski hazard jest spokojny, ale reaguje z opóźnieniem. To pokrętło jest changepointowym odpowiednikiem klasycznego opóźnienia detekcji: nie da się mieć naraz natychmiastowego wykrycia i zera fałszywych alarmów.

## Co z tego wynika przy stole

Reżim jest filtrem, nie sygnałem. Decyduje o tym, czy uruchomić strategię, a nie o tym, w którą stronę obstawić. Uczciwsza forma zdania brzmi „strategia X ma sens w reżimie trendowym, a model daje teraz 70 procent na zakres, więc X czeka", a nie „kupuję, bo trend". To jest cała zmiana w sposobie mówienia.

Detekcja spóźnia się na zakręcie. Każda metoda, filtrowany HMM, changepoint czy reżim zmienności, jest najbardziej niepewna dokładnie w chwili, gdy reżim się odwraca, bo do zobaczenia zmiany potrzebuje danych. Potwierdzenie kosztuje cię pierwszą część ruchu. To koszt strukturalny, a nie błąd do naprawienia.

Uważaj na podglądanie przyszłości. Dopasowania na całej próbie, stany wygładzone i przemalowujące się etykiety sprawiają, że historyczna mapa reżimów wygląda prorocko, a odczyt na żywo rozczarowuje. Do czegokolwiek, co mogłoby dotknąć decyzji, legalne są tylko estymaty przyczynowe, filtrowane, liczone wyłącznie z przeszłości.

Mniej stanów uczciwie oszacowanych bije wiele stanów precyzyjnie dostrojonych. Dwa do czterech stanów, lepka macierz przejść i zmienność jako główna cecha niosą większość wartości. Więcej stanów zwykle znaczy dopasowanie do szumu.

Warstwy się składają. Cechy typu GARCH opisują intensywność, GMM i HMM opisują tożsamość, a changepoint opisuje pęknięcie. Razem odpowiadają na trzy pytania: jak dziko, w jaką grę gramy i czy właśnie się to zmieniło. To jest praktycznie cała treść świadomości reżimu.

To nie jest porada inwestycyjna. To przegląd mechanizmów rozpoznawania reżimu rynku, pokazany z intuicją i wzorami, żeby odróżnić opis środowiska (w jaką grę grasz) od prognozy kierunku (w którą stronę pójdzie cena), zanim któremukolwiek z tych narzędzi powierzy się decyzję.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
