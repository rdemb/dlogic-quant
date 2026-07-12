---
title: "Optymalizacja: gradient, wypukłość i jedno minimum"
description: "Każdy problem optymalizacji ma ten sam szkielet: minimalizuj funkcję celu przy ograniczeniach. Gradient wskazuje kierunek najszybszego wzrostu, więc spadek gradientowy idzie w stronę przeciwną, małymi, samoczynnie malejącymi krokami. O wiarygodności wyniku decyduje wypukłość: funkcja wypukła ma jedno minimum globalne, więc znaleziony punkt jest tym punktem (Boyd i Vandenberghe, 2004). Do tego portfel Markowitza (1952) jako wypukły problem kwadratowy z mnożnikami Lagrange'a, przeuczenie jako dopasowanie do szumu, regularyzacja jako kara za złożoność i granica, za którą zaczyna się świat niewypukły z wieloma minimami lokalnymi."
date: 2026-07-11 18:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Cztery pojęcia porządkują całą optymalizację: funkcja celu i ograniczenia jako język problemu, gradient jako kierunek najszybszego wzrostu, spadek gradientowy jako mechanika schodzenia do dna i wypukłość jako gwarancja, że tego dna jest tylko jedno. Do tego portfel Markowitza jako problem kwadratowy, regularyzacja przeciw dopasowaniu do szumu oraz granica, za którą pojawiają się minima lokalne."
readingTime: 8
tags: [matematyka, optymalizacja, gradient, wypukłość, "spadek gradientowy", "funkcja celu", "mnożniki Lagrange'a", Markowitz, regularyzacja, overfitting, "problem kwadratowy", "Boyd Vandenberghe", "Nocedal Wright", edukacja]
category: edukacja
---

> **W skrócie**
>
> - Każdy problem optymalizacji ma ten sam szkielet: funkcja celu do zminimalizowania, zmienne decyzyjne i ograniczenia wyznaczające zbiór dopuszczalny. Maksymalizacja dowolnej wielkości to minimalizacja jej przeciwności, więc jeden aparat wystarcza do obu zadań.
> - Gradient to wektor pochodnych cząstkowych funkcji celu, wskazujący kierunek jej najszybszego wzrostu. Metoda spadku gradientowego idzie w kierunku dokładnie przeciwnym, a w pobliżu minimum gradient zanika, więc kroki maleją samoczynnie (Nocedal i Wright, 2006).
> - O wiarygodności rozwiązania decyduje wypukłość. W funkcji wypukłej każde minimum lokalne jest zarazem globalne, więc procedura, która trafiła w punkt o zerowym gradiencie, trafiła w najlepszy punkt, jaki istnieje (Boyd i Vandenberghe, 2004).
> - Optymalizacja portfela Markowitza (1952) to wypukły problem kwadratowy: minimalizacja wariancji przy liniowych ograniczeniach na wagi, rozwiązywana mnożnikami Lagrange'a w postaci zamkniętej. Wypukłość gwarantuje, że wyliczona granica efektywna jest prawdziwym minimum, a nie jednym z wielu.
> - Nadmiar stopni swobody pozwala dopasować funkcję celu do szumu zamiast do struktury. Regularyzacja dokłada karę za złożoność. W problemach niewypukłych, takich jak trening sieci neuronowych, minimów lokalnych jest wiele i żadna teoria nie gwarantuje trafienia w najlepsze.

**Teza w jednym zdaniu:** Optymalizacja nie zgaduje, tylko schodzi po zboczu funkcji celu w stronę minimum; o tym, czy znaleziony punkt jest naprawdę najlepszy, rozstrzyga wypukłość, a o tym, czy cokolwiek znaczy, rozstrzyga to, czy minimalizowano strukturę, czy szum.

## Jeden szkielet: funkcja celu, zmienne, ograniczenia

Optymalizacja to matematyczny zapis pytania, które w praktyce pada bez przerwy: która decyzja jest najlepsza. Żeby to pytanie stało się policzalne, potrzebne są trzy elementy. Funkcja celu, czyli liczba mierząca jakość rozwiązania: koszt do obniżenia, ryzyko do stłumienia, błąd modelu do zmniejszenia. Zmienne decyzyjne, czyli to, co wolno ustawiać. Oraz ograniczenia, które odsiewają rozwiązania niedopuszczalne, na przykład wagi portfela muszą sumować się do jedności, a zapas nie może być ujemny. Reszta jest już tylko techniką szukania najlepszego punktu w dozwolonym obszarze.

Jedna obserwacja upraszcza cały krajobraz. Maksymalizacja dowolnej wielkości to minimalizacja jej przeciwności, więc nie trzeba dwóch osobnych aparatów. Umiejętność minimalizowania wystarcza do wszystkiego, a cała teoria mówi zwykle językiem minimum.

```
min  f(x)              funkcja celu (koszt, ryzyko, błąd)
 x
przy: g_i(x) ≤ 0       ograniczenia nierównościowe
      h_j(x) = 0       ograniczenia równościowe

maksymalizacja f(x)  =  minimalizacja −f(x)
zbiór punktów spełniających ograniczenia = zbiór dopuszczalny
```

## Gradient: kierunek najszybszego wzrostu

Skoro celem jest zejście na dno funkcji, potrzebny jest kompas: informacja, w którą stronę iść. Tym kompasem jest gradient. Dla funkcji wielu zmiennych to wektor złożony z pochodnych cząstkowych, po jednej na każdą zmienną. Każda pochodna mówi, jak szybko rośnie funkcja przy poruszeniu jednej współrzędnej, a złożone razem wskazują kierunek najszybszego wzrostu całej funkcji. Długość gradientu mierzy stromość zbocza: im większa, tym mocniej funkcja się zmienia.

Dwie konsekwencje są bezpośrednie. Kierunek przeciwny do gradientu to kierunek najszybszego spadku, więc właśnie w tę stronę opłaca się schodzić przy minimalizacji. A w samym minimum, o ile leży wewnątrz zbioru dopuszczalnego, gradient znika: nie ma już kierunku, w którym dałoby się zejść niżej. Zerowanie się gradientu to warunek pierwszego rzędu, standardowy punkt wyjścia każdej analizy optymalizacyjnej (Nocedal i Wright, 2006).

```
∇f(x) = [ ∂f/∂x₁ , ∂f/∂x₂ , ... , ∂f/∂xₙ ]

kierunek  ∇f    → najszybszy wzrost f
kierunek −∇f    → najszybszy spadek f
w minimum:  ∇f(x*) = 0        (warunek pierwszego rzędu)
```

## Spadek gradientowy: schodzenie krok po kroku

Najprostszy algorytm optymalizacji bierze te dwa fakty dosłownie. Startuje z dowolnego punktu, liczy gradient, robi krok w kierunku przeciwnym, po czym powtarza. Długość kroku steruje parametr nazywany współczynnikiem uczenia. Wbudowany jest w to naturalny hamulec: w miarę zbliżania się do minimum gradient słabnie, więc kolejne kroki same się skracają, a procedura zwalnia dokładnie tam, gdzie robi się precyzyjnie.

Dobór długości kroku bywa jednak delikatny. Zbyt duży krok przeskakuje minimum i procedura potrafi się rozbiegać zamiast zbiegać. Zbyt mały ciągnie zbieżność w nieskończoność. Ten sam schemat, od regresji po trening sieci neuronowych, jest dziś roboczym koniem numerycznej optymalizacji (Nocedal i Wright, 2006).

```
xₖ₊₁ = xₖ − α · ∇f(xₖ)

α  = długość kroku (współczynnik uczenia)
α za duże  → przeskakiwanie minimum, rozbieżność
α za małe  → zbieżność, ale wolna

przykład f(x) = x²,  ∇f = 2x,  α = 0.25:
x₀ = 4 → 2 → 1 → 0.5 → 0.25 → ...    (kroki maleją same)
```

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Spadek gradientowy: kroki maleją w miarę zbliżania do minimum</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">wartość funkcji celu f(x)</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">zmienna decyzyjna x</text><path d="M120 78 Q348 332 576 78" fill="none" stroke="currentColor" stroke-width="1.8" opacity="0.55"/><line x1="348" y1="205" x2="348" y2="232" stroke="currentColor" stroke-width="1" opacity="0.4" stroke-dasharray="2 4"/><path d="M164 122 L244 179 L292 197 L320 203 L336 205 L348 205" fill="none" stroke="#0b66c3" stroke-width="2"/><circle cx="164" cy="122" r="3.5" fill="#0b66c3"/><circle cx="244" cy="179" r="3.5" fill="#0b66c3"/><circle cx="292" cy="197" r="3.5" fill="#0b66c3"/><circle cx="320" cy="203" r="3.5" fill="#0b66c3"/><circle cx="336" cy="205" r="3.5" fill="#0b66c3"/><circle cx="348" cy="205" r="5" fill="#1a9e6a"/><text x="168" y="110" font-size="10.5" fill="#0b66c3" text-anchor="middle">start</text><text x="300" y="176" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">kroki maleją</text><text x="362" y="201" font-size="10.5" fill="#1a9e6a">minimum globalne</text><text x="486" y="140" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle">f wypukła: jedna dolina</text><text x="348" y="248" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">x*</text></svg>
<figcaption>Funkcja celu wypukła (parabola) ma jedną dolinę. Spadek gradientowy startuje z lewej i schodzi w stronę minimum, za każdym razem w kierunku przeciwnym do gradientu. W miarę zbliżania się do dna gradient słabnie, więc kolejne kroki są coraz krótsze, a punkty gęstnieją. Zielony punkt to minimum globalne: w funkcji wypukłej jedyne, więc jego znalezienie kończy zadanie.</figcaption>
</figure>

## Wypukłość: dlaczego dno jest jedno

Spadek gradientowy zawsze coś znajdzie: punkt, w którym gradient znika i schodzenie się zatrzymuje. Pozostaje pytanie warte całej reszty tekstu: czy ten punkt jest najlepszy, czy tylko lokalnie najniższy. Odpowiedź zależy od kształtu funkcji celu, a konkretnie od jej wypukłości.

Funkcja jest wypukła, jeśli odcinek łączący dowolne dwa punkty jej wykresu leży w całości nad wykresem. Intuicyjnie to jedna gładka dolina, bez wgłębień i garbów. Dla funkcji dwukrotnie różniczkowalnej warunek sprowadza się do nieujemnej drugiej pochodnej, a w wielu wymiarach do dodatniej półokreśloności hesjanu.

Znaczenie tej własności trudno przecenić i formułuje je klasyczny podręcznik Boyda i Vandenberghe (2004): w funkcji wypukłej każde minimum lokalne jest automatycznie minimum globalnym. Konsekwencja praktyczna jest mocna. Gdy problem jest wypukły, procedura schodząca po gradiencie nie może utknąć w gorszym z wielu dołków, bo dołek jest tylko jeden. Znaleziony punkt to rozwiązanie, kropka. Ta gwarancja jest powodem, dla którego w teorii optymalizacji przebiega najważniejsza granica: nie między liniowym a nieliniowym, lecz między wypukłym a niewypukłym.

```
f wypukła  ⇔  odcinek łączący dwa punkty wykresu
              leży nad wykresem:

f(λx + (1−λ)y) ≤ λ·f(x) + (1−λ)·f(y),   λ ∈ [0,1]

dla f dwukrotnie różniczkowalnej:  f''(x) ≥ 0     (jeden wymiar)
                                   hesjan ⪰ 0     (wiele zmiennych)

własność kluczowa: w funkcji wypukłej
każde minimum lokalne JEST minimum globalnym
```

## Portfel Markowitza jako problem kwadratowy

Najbardziej znany finansowy przykład problemu wypukłego to optymalizacja portfela z pracy Markowitza (1952). Zadanie brzmi: dobrać wagi aktywów tak, by przy zadanym oczekiwanym zwrocie wariancja portfela była najmniejsza. Funkcją celu jest wariancja, wyrażona formą kwadratową z macierzą kowariancji, a ograniczenia są liniowe: wagi mają dać zadany zwrot i zsumować się do jedności. Ponieważ macierz kowariancji jest z definicji dodatnio półokreślona, funkcja celu jest wypukła, a całość to wypukły problem kwadratowy.

Taki problem ma rozwiązanie w postaci zamkniętej, a narzędziem są mnożniki Lagrange'a: każdemu ograniczeniu przypisuje się mnożnik, dokłada je do funkcji celu i szuka punktu, w którym gradient całości znika. Wychodzi układ równań liniowych, którego rozwiązanie zakreśla granicę efektywną. Kluczowe jest to, co daje tu wypukłość: znaleziony punkt nie jest jednym z wielu kandydatów, lecz globalnym minimum wariancji przy danym zwrocie. Granica efektywna staje się więc obiektem policzalnym i jednoznacznym, opisanym szerzej w materiale o [teorii portfela Markowitza](/dlogic-quant/2026/07/07/teoria-portfela-markowitza-dywersyfikacja/).

```
min  ½ · wᵀ Σ w             wariancja portfela (wypukła, bo Σ ⪰ 0)
 w
przy: wᵀ μ = R              zadany oczekiwany zwrot
      wᵀ 1 = 1              wagi sumują się do jedności

Lagranżjan:
L(w, λ₁, λ₂) = ½·wᵀΣw − λ₁·(wᵀμ − R) − λ₂·(wᵀ1 − 1)

∂L/∂w = 0  →  Σw = λ₁·μ + λ₂·1     (układ liniowy, rozwiązanie zamknięte)
```

To pewność matematyczna, nie inwestycyjna. Wypukłość gwarantuje, że wagi są dokładnie optymalne dla podanej macierzy kowariancji i podanych zwrotów. Nie gwarantuje, że te wejścia są prawdziwe, i właśnie z tej luki bierze się kruchość optymalizacji portfelowej, omówiona w tamtym tekście osobno.

## Przeuczenie: kiedy minimalizuje się szum

Wypukłość mówi, że minimum funkcji celu zostanie znalezione dokładnie. Milczy o tym, czy sama funkcja celu jest dobrze postawiona. Tu wchodzi przeuczenie. Gdy model ma dużo parametrów, czyli dużo stopni swobody, minimalizacja błędu na próbce potrafi zejść bardzo nisko, ale nie dlatego, że model uchwycił strukturę. Zejść nisko można też, dopasowując się do przypadkowego szumu w konkretnych danych. Im więcej swobody, tym łatwiej funkcja celu myli szum ze wzorem, a rozwiązanie idealne na próbce rozpada się poza nią.

Standardową odpowiedzią jest regularyzacja: do funkcji celu dokłada się karę rosnącą wraz ze złożonością rozwiązania. Zamiast minimalizować sam błąd, minimalizuje się błąd powiększony o człon karzący duże współczynniki. Kara grzbietowa (ridge, znana też jako regularyzacja Tichonowa) tłumi wszystkie współczynniki, kara lasso dodatkowo zeruje część z nich, upraszczając model. Siłę kary ustawia jeden parametr: im większy, tym prostsze rozwiązanie, kosztem gorszego dopasowania na próbce, ale zwykle lepszego poza nią.

```
bez kary:   min  błąd_na_próbce(x)
             x        → przy nadmiarze parametrów dopasowuje szum

z karą:     min  błąd_na_próbce(x) + λ · kara(x)
             x

kara(x) = ‖x‖²   → grzbietowa (ridge): tłumi wszystkie współczynniki
kara(x) = ‖x‖₁   → lasso: dodatkowo zeruje część współczynników
λ  = siła regularyzacji (cena złożoności); λ = 0 znosi karę
```

Mechanizm ma bliski odpowiednik w finansach. Optymalizator Markowitza, karmiony estymatami z próbki, wzmacnia ich błędy i produkuje skrajne wagi, co bywa nazywane maksymalizacją błędu. To ten sam problem: procedura minimalizuje dokładnie to, co dostała, łącznie z szumem wejść. Dlatego uczciwe strojenie parametrów strategii wymaga oceny poza oknem dopasowania, o czym mówi osobny tekst o [walk-forward i dopasowaniu do szumu](/dlogic-quant/2026/07/12/optymalizacja-walk-forward-w-kodzie/).

## Kiedy minimów jest wiele: świat niewypukły

Cała pewność wypukłego świata znika, gdy funkcja celu ma wiele dolin. W problemie niewypukłym punktów o zerowym gradiencie jest wiele: minima lokalne różnej głębokości oraz siodła, w których gradient też się zeruje, choć nie są minimami. Spadek gradientowy zatrzyma się w tym dołku, do którego doprowadzi go punkt startowy i ścieżka schodzenia, i nie ma gwarancji, że to dołek najgłębszy. Dwie próby z różnych punktów startowych mogą dać różne rozwiązania.

Najgłośniejszym przykładem jest trening sieci neuronowych: funkcja straty jest tam głęboko niewypukła, o ogromnej liczbie parametrów i mnóstwie minimów lokalnych. Praktyka radzi sobie sztuczkami, wielokrotnymi startami i wariantami spadku gradientowego, ale twarda gwarancja globalnego minimum, oczywista w świecie wypukłym, po prostu nie obowiązuje. Dlatego Boyd i Vandenberghe (2004) stawiają wypukłość w centrum: to ona oddziela problemy, które umie się rozwiązać pewnie, od tych, w których trzeba się zadowolić rozwiązaniem dobrym, bez dowodu, że najlepszym.

```
wypukła:      jedna dolina   → −∇f zawsze prowadzi do globalnego minimum
niewypukła:   wiele dolin    → wynik zależy od punktu startowego i ścieżki
                               (minima lokalne i siodła; np. strata sieci)
```

## Co z tego zostaje

Trzy pojęcia układają się w jedno zdanie robocze. Gradient daje kierunek, spadek gradientowy daje mechanikę schodzenia, a wypukłość daje pewność, że dno jest jedno. Kiedy problem jest wypukły, ta układanka jest kompletna i wynik zasługuje na zaufanie w ścisłym, matematycznym sensie.

Zaufanie to ma jednak wyraźną granicę i warto ją nazwać bez upiększeń. Optymalizacja jest pewna wyłącznie co do funkcji celu, którą naprawdę zapisano, i danych, które naprawdę podano. Wypukłość zapewnia, że znaleziono minimum tej funkcji na tej próbce. Nie orzeka, że funkcja celu jest właściwa ani że próbka to sygnał, a nie szum. Stąd dwa ostrzeżenia z tego tekstu: portfel Markowitza jest optymalny tylko dla wejść, które trzeba było zgadnąć, a strojenie parametrów bywa minimalizowaniem szumu w przebraniu. Matematyka schodzenia jest solidna. Odpowiedzialność za to, po czym się schodzi, zostaje po stronie człowieka.

Materiał czysto edukacyjny, nie porada inwestycyjna ani zachęta do jakiejkolwiek strategii. Pewna jest tu wyłącznie matematyka optymalizacji: definicja gradientu, mechanika spadku gradientowego i gwarancja globalnego minimum dla funkcji wypukłych. Wszystko, co dotyczy trafności funkcji celu i wiarygodności danych, pozostaje poza tą pewnością.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
