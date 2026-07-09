---
title: "Zmienność: zrealizowana, implikowana i premia za ryzyko"
description: "Zmienność zrealizowana liczy, ile rynek już się poruszał; implikowana wyciąga z cen opcji, ile ruchu rynek wycenia na przyszłość. Systematyczna różnica między nimi to premia za ryzyko zmienności (VRP), działająca jak składka ubezpieczeniowa. Do tego klasterowanie zmienności i modele GARCH jako narzędzie prognozy poziomu, a nie kierunku, oraz smile i risk reversal na FX jako miara asymetrii oczekiwań. Koncepcje jakościowo, ze wzorami, jako kontekst ryzyka."
date: 2026-07-09 16:30:00 +0200
eyebrow: "Edukacja · zmienność"
dek: "Zmienność zrealizowana mówi, ile rynek już się ruszał; implikowana, ile ruchu wyceniają opcje. Różnica między nimi to premia za ryzyko zmienności, rodzaj składki ubezpieczeniowej. Do tego uśmiech i risk reversal na FX, czyli miara tego, której strony rynek bardziej się boi. Koncepcje i wzory, jako kontekst, nie sygnał."
readingTime: 8
tags: ["zmienność", "zmienność implikowana", "zmienność zrealizowana", VRP, "premia za ryzyko zmienności", GARCH, ARCH, "risk reversal", smile, "opcje FX", "zmienność stochastyczna", Bennett, Gatheral, "Carr & Wu", "Reiswich & Wystup", Sheppard, "Daníelsson", Forex, edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Zmienność ma dwie twarze. Zrealizowana liczy, ile rynek już się poruszał, na podstawie historii zwrotów. Implikowana wyciąga z cen opcji, ile ruchu rynek wycenia na przyszłość. Pierwsza patrzy wstecz, druga do przodu, i prawie nigdy nie są sobie równe.
> - Implikowana jest przeciętnie wyższa od zrealizowanej, a ta systematyczna różnica to premia za ryzyko zmienności (VRP). Działa jak składka ubezpieczeniowa: kupujący opcję płaci ją za ochronę, sprzedający inkasuje ją za przyjęcie ryzyka gwałtownego ruchu (Carr i Wu).
> - Zmienność przychodzi seriami. Po spokoju następuje spokój, po burzy burza, a modele z rodziny GARCH opisują to klasterowanie jako powrót do średniej długoterminowej. To narzędzie prognozy poziomu zmienności, nie kierunku ceny.
> - Rynek opcji FX wycenia asymetrię. Znak risk reversal mówi, której strony rynek bardziej się boi, spadku czy wzrostu waluty, a butterfly mówi, jak grube ogony są wyceniane. To kontekst ryzyka, nie sygnał wejścia.

**Teza w jednym zdaniu:** Zmienność zrealizowana i implikowana to dwie różne liczby, przeszłość kontra wycena przyszłości, ich różnica to premia za ryzyko zmienności, a kształt rynku opcji (smile, risk reversal) pokazuje asymetrię oczekiwań, ale całość jest kontekstem ryzyka, a nie sygnałem kierunku.

## Dwie zmienności, które łatwo pomylić

Słowo „zmienność" kryje dwie zupełnie różne wielkości, a mylenie ich jest jednym z częstszych nieporozumień na rynku. Zmienność zrealizowana (nazywana też historyczną) to rozproszenie zwrotów, które już się wydarzyły. Zmienność implikowana to liczba wyciągnięta z bieżących cen opcji, mówiąca, jak duży ruch rynek wycenia na przyszłość. Jedna jest pomiarem przeszłości, druga oczekiwaniem zapisanym w cenie ubezpieczenia. Bennett, w praktycznym kompendium o handlu zmiennością, opisuje tę parę jako podstawowy układ współrzędnych każdej analizy opcyjnej: bez rozdzielenia tych dwóch pojęć reszta rozważań się rozpada.

## Zmienność zrealizowana: ile rynek faktycznie się ruszał

Zrealizowana zmienność to po prostu odchylenie standardowe zwrotów, przeliczone na skalę roczną. Liczy się ją z logarytmicznych zwrotów, a następnie skaluje pierwiastkiem z liczby okresów w roku, bo wariancja narasta liniowo w czasie, a odchylenie standardowe z pierwiastkiem.

```
σ_zreal = odchylenie_std(r_t) · √(K)

r_t = ln(P_t / P_{t−1})       # log-zwrot z okresu t
K   = liczba okresów w roku    # np. 252 dni, 52 tygodnie, 12 miesięcy
```

Istnieje też dokładniejszy wariant liczony z danych o wysokiej częstotliwości: realizowana wariancja to suma kwadratów zwrotów śróddziennych w obrębie jednego dnia. Im gęstsza siatka pomiaru, tym wierniej odtwarza faktyczną drogę, jaką cena przebyła danego dnia.

```
RV = Σ r²_i    # suma kwadratów zwrotów śróddziennych w danym dniu
```

Cechą wspólną wszystkich tych miar jest kierunek patrzenia: wstecz. Zrealizowana zmienność nic nie zakłada o przyszłości, mówi wyłącznie, jak burzliwa była przeszłość.

## Zmienność implikowana: czego rynek oczekuje, wyceniona w opcjach

Zmienność implikowana idzie w drugą stronę. Cena opcji zależy od kilku obserwowalnych wielkości (kurs bieżący, kurs wykonania, czas do wygaśnięcia, stopy procentowe) oraz jednej nieobserwowalnej: przyszłej zmienności. Jeżeli wszystkie pozostałe wielkości są znane, a cena opcji jest widoczna na rynku, to można odwrócić model wyceny i zapytać: jaka wartość zmienności musiałaby być prawdziwa, żeby model odtworzył tę cenę. Ta wartość to zmienność implikowana. Na rynku walutowym standardem jest model Garmana-Kohlhagena, będący wersją Blacka-Scholesa z dwiema stopami procentowymi, krajową i zagraniczną.

```
cena_rynkowa_opcji = GK(S, K, T, r_d, r_f, σ)   # model Garmana-Kohlhagena (FX)
σ_impl = ta wartość σ, przy której model odtwarza rynkową cenę opcji
```

Kluczowe jest to, że zmienność implikowana jest wielkością patrzącą w przód. Nie mówi, co się wydarzyło, lecz ile niepewności rynek wycenia na okres do wygaśnięcia opcji. Dlatego rośnie przed zaplanowanymi wydarzeniami wysokiego ryzyka (decyzje banków centralnych, publikacje danych) i opada, gdy niepewność się rozładowuje.

## Premia za ryzyko zmienności: dlaczego implikowana zwykle przewyższa zrealizowaną

Gdyby rynek wyceniał zmienność bezstronnie, implikowana byłaby średnio równa późniejszej zrealizowanej. W praktyce tak nie jest: implikowana jest przeciętnie wyższa od tego, co rynek następnie faktycznie zrealizuje. Ta systematyczna nadwyżka to premia za ryzyko zmienności (VRP).

```
VRP = IV − RV        # w jednostkach zmienności
VRP = IV² − RV²      # częściej liczona w jednostkach wariancji

przeciętnie:  IV > RV   →   VRP > 0
```

Najprostsza intuicja to ubezpieczenie. Kto kupuje opcję, kupuje ochronę przed gwałtownym ruchem i jest skłonny zapłacić za nią trochę więcej, niż wynosi statystycznie uczciwa cena, tak samo jak za polisę płaci się więcej, niż wynosi oczekiwana szkoda. Kto opcję wystawia, przejmuje ryzyko rzadkiego, dużego ruchu i za to przejęcie inkasuje premię. Carr i Wu w pracy poświęconej premiom za ryzyko wariancji pokazali, jak tę premię wyodrębnić i zmierzyć za pomocą syntetycznych kontraktów na wariancję, i udokumentowali, że przeciętnie jest ona dodatnia. Dla inwestora płynie stąd prosty morał: dodatnia VRP nie jest darmowym obiadem, lecz zapłatą za bycie po stronie, która obrywa, gdy przychodzi szok. Jest to premia za przyjęcie ryzyka, nie nagroda za spryt.

## Klasterowanie zmienności i modele GARCH

Zmienność ma jeszcze jedną wygodną cechę: przychodzi seriami. Dni spokojne skupiają się przy dniach spokojnych, a gwałtowne przy gwałtownych. To zjawisko nazywa się klasterowaniem zmienności i jest jedną z najtrwalszych regularności na rynkach finansowych. Formalnie ujmuje je rodzina modeli ARCH i GARCH, zapoczątkowana przez Engle'a i Bollersleva. Najprostszy użyteczny wariant, GARCH(1,1), modeluje dzisiejszą wariancję jako mieszankę trzech składników: stałej kotwicy, wczorajszego szoku i wczorajszej wariancji.

```
σ²_t = ω + α·r²_{t−1} + β·σ²_{t−1}     # GARCH(1,1)

ω = kotwica (stała, poziom długookresowy),  α = siła reakcji na ostatni szok
β = trwałość (pamięć) zmienności,   warunek stabilności:  α + β < 1
poziom długookresowy:  σ²_∞ = ω / (1 − α − β)
```

Czyta się to jak opis bezwładności. Duży wczorajszy ruch (wysokie r²) podbija dzisiejszą prognozę zmienności przez składnik α. Wysoka wczorajsza zmienność ciągnie się dalej przez składnik β. A ponieważ suma α i β jest mniejsza od jedności, prognoza z czasem powraca do poziomu długookresowego σ²_∞: po burzy rynek stopniowo się uspokaja, po nienaturalnym spokoju zmienność wraca do normy. Praktyczne wersje tych modeli są dostępne od ręki, na przykład w bibliotece arch autorstwa Shepparda, a Daníelsson w podręczniku o prognozowaniu ryzyka finansowego pokazuje, jak z takich prognoz budować miary ryzyka. Warto podkreślić jedno: GARCH prognozuje poziom zmienności, czyli jak bardzo rynek będzie się ruszał, a nie w którą stronę. To model amplitudy, nie kierunku.

Na dalszym horyzoncie badawczym klasyczny obraz zmienności stochastycznej dodatkowo się zaostrza. Gatheral, znany z pracy nad powierzchnią zmienności implikowanej, wraz ze współautorami zaproponował koncepcję rough volatility, w której ścieżka logarytmu zmienności jest bardziej „poszarpana", niż zakładają starsze modele. Dla inwestora manualnego to raczej wiedza o kierunku, w jakim zmierza modelowanie ryzyka, niż codzienne narzędzie, ale dobrze pokazuje, że zmienność sama w sobie jest złożonym, dynamicznym obiektem, a nie pojedynczą stałą liczbą.

## Uśmiech i risk reversal: asymetria strachu na FX

Jedna liczba zmienności implikowanej nie wystarcza, bo opcje o różnych kursach wykonania mają różne implikowane zmienności. Wykres zmienności implikowanej w funkcji kursu wykonania (albo delty) układa się zwykle w kształt uśmiechu: opcje głęboko poza pieniądzem po obu stronach mają wyższą implikowaną zmienność niż opcje przy pieniądzu. Ten uśmiech to zapis tego, że rynek wycenia grubsze ogony, niż przewiduje rozkład normalny. Na rynku walutowym uśmiech opisuje się nie punkt po punkcie, lecz trzema liczbami na daną deltę: zmiennością ATM (przy pieniądzu), risk reversal i butterfly.

```
RR25 = σ_impl(25Δ call) − σ_impl(25Δ put)                    # skos: asymetria
BF25 = [σ_impl(25Δ call) + σ_impl(25Δ put)] / 2 − σ_impl(ATM)  # wypukłość: ogony
```

Risk reversal mierzy przechył uśmiechu, czyli asymetrię. Jest to różnica implikowanych zmienności między symetryczną opcją call a put (na przykład o delcie 25). Znak tej różnicy mówi, po której stronie rynek płaci drożej za ochronę. Dodatni risk reversal na EURUSD oznacza, że opcje zarabiające na wzroście euro są względnie droższe, czyli rynek bardziej płaci za scenariusz umocnienia euro. Ujemny risk reversal oznacza sytuację odwrotną: droższe są opcje chroniące przed spadkiem euro, więc rynek bardziej boi się osłabienia euro (co często zbiega się z ucieczką do dolara jako waluty bezpiecznej przystani). Butterfly z kolei mierzy wypukłość uśmiechu, czyli jak mocno oba skrzydła są uniesione ponad poziom ATM. Wyższy butterfly to grubsze ogony wyceniane po obu stronach, czyli większa premia za scenariusze skrajne niezależnie od kierunku. Reiswich i Wystup w pracy o konstrukcji uśmiechu zmienności na FX pokazują dokładnie, jak z tych trzech kwotowań (ATM, risk reversal, butterfly) odtworzyć całą krzywą implikowanej zmienności dla danego terminu.

## Po co to inwestorowi: kontekst, nie sygnał

Dla manualnego day-tradera te pojęcia nie są sygnałem wejścia i nie zastępują decyzji o kierunku. Są warstwą kontekstu ryzyka, którą warto czytać przed podjęciem decyzji, a nie zamiast niej. Wysoka zmienność implikowana względem zrealizowanej mówi, że ochrona jest droga i że rynek wycenia sporo niepokoju, co bywa ostrzeżeniem przed zbliżającym się wydarzeniem wysokiego ryzyka. Prognoza z modelu GARCH mówi, czy najbliższe sesje zapowiadają się na spokojne czy burzliwe, co przekłada się na rozsądny dobór wielkości pozycji i szerokości ewentualnych poziomów obronnych. Znak risk reversal mówi, której strony rynek bardziej się boi, co jest cenną informacją o asymetrii nastrojów, zwłaszcza w zestawieniu z własnym poglądem na kierunek.

Wszystkie te wielkości łączy to samo ograniczenie: opisują rozkład możliwych ruchów, a nie przesądzają, który się zdarzy. Zmienność mówi, jak szeroko, nie mówi, dokąd. Dlatego uczciwe użycie tej wiedzy polega na wpisaniu jej w kontekst decyzji (ile ryzyka jest w cenie, czego rynek się boi, jak burzliwe będzie tło), a nie na traktowaniu jej jako mechanicznego sygnału kupna czy sprzedaży.

To nie jest porada inwestycyjna. To materiał edukacyjny, który porządkuje pojęcia zmienności, ze wzorami i odniesieniami do literatury, żeby odróżnić pomiar przeszłości od wyceny przyszłości i czytać rynek opcji jako kontekst ryzyka.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
