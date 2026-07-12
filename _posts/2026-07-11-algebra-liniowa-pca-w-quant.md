---
title: "Algebra liniowa w quant: kowariancja, PCA i czynniki"
description: "Macierz kowariancji zbiera w jednej tablicy zmienność każdego aktywa na przekątnej i współruch par poza nią, a korelacja to ta sama liczba pozbawiona jednostek. Rozkład na wartości i wektory własne (Strang, Introduction to Linear Algebra) wskazuje kierunki największej zmienności, a analiza głównych składowych (Jolliffe, Principal Component Analysis) obraca dane do osi nieskorelowanych i pozwala opisać wiele instrumentów kilkoma liczbami. Klasyczny przykład: Litterman i Scheinkman (1991) pokazali, że trzy składowe krzywej dochodowości, poziom, nachylenie i krzywizna, tłumaczą niemal całą jej zmienność. To samo obliczenie stoi za modelami czynnikowymi i CAPM."
date: 2026-07-11 17:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Portfel to nie lista pojedynczych aktywów, tylko splot ich wspólnych ruchów. Język, który ten splot opisuje, to algebra liniowa: wektory zwrotów, macierz kowariancji i jej rozkład na kierunki własne. Analiza głównych składowych obraca chmurę danych tak, aby pierwsza oś chwytała najwięcej zmienności, a kolejne coraz mniej. Na krzywej dochodowości te osie mają nazwy: poziom, nachylenie, krzywizna. To samo obliczenie jest matematycznym zapleczem czynników i CAPM."
readingTime: 9
tags: [matematyka, "algebra liniowa", PCA, kowariancja, korelacja, czynniki, "wartości własne", "wektory własne", "krzywa dochodowości", "Litterman i Scheinkman", "redukcja wymiaru", "model czynnikowy", CAPM, quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Wektor zwrotów zbiera zmiany cen wielu instrumentów naraz, a macierz kowariancji opisuje ich wspólną strukturę ryzyka. Na przekątnej stoją wariancje, czyli własna zmienność każdego aktywa, poza przekątną kowariancje, czyli siła wspólnego ruchu par. Ta jedna symetryczna tablica wystarcza, żeby policzyć ryzyko dowolnego portfela z tych aktywów.
> - Korelacja to kowariancja pozbawiona jednostek: kowariancja podzielona przez iloczyn odchyleń standardowych, zawsze w przedziale od minus jeden do jeden. Dzięki normalizacji można porównać współruch pary walut ze współruchem pary obligacji, a macierz korelacji czyta się łatwiej niż surową kowariancję.
> - Rozkład macierzy kowariancji na wartości i wektory własne (Strang, Introduction to Linear Algebra) wskazuje prostopadłe kierunki, wzdłuż których dane zmieniają się najsilniej. Analiza głównych składowych (Jolliffe, Principal Component Analysis) to obrót układu współrzędnych do tych kierunków: nowe osie są nieskorelowane, a pierwsza chwyta najwięcej wariancji.
> - Redukcja wymiaru bierze się stąd, że kilka pierwszych składowych często tłumaczy większość zmienności. Litterman i Scheinkman (1991) pokazali, że trzy składowe krzywej dochodowości, poziom, nachylenie i krzywizna, opisują niemal całą jej ruchomość. Ostrożność jest jednak konieczna: składowe bywają niestabilne w czasie, trudne do interpretacji i wrażliwe na estymację kowariancji przy krótkiej próbie.

**Teza w jednym zdaniu:** Kowariancja, jej rozkład własny i analiza głównych składowych to jeden ciąg algebry liniowej, który zamienia wiele skorelowanych instrumentów w kilka nieskorelowanych kierunków zmienności, daje modelom czynnikowym i CAPM matematyczne zaplecze, a zarazem wymaga ostrożności, bo obrót wyliczony z krótkiej próby potrafi być niestabilny i trudny do zinterpretowania.

## Wektor zwrotów i macierz kowariancji

Pojedynczy zwrot to jedna liczba. Portfel wielu instrumentów opisuje wektor zwrotów: uporządkowana lista zmian, po jednej współrzędnej na aktywo. Ryzyko takiego wektora nie sprowadza się do sumy ryzyk pojedynczych pozycji, bo instrumenty poruszają się razem. Całą tę wspólną strukturę zbiera macierz kowariancji.

```
r = (r₁, r₂, ..., rₙ)          wektor zwrotów n aktywów

macierz kowariancji (n × n), symetryczna:

        r₁      r₂      r₃
r₁   [ σ₁²    σ₁₂    σ₁₃ ]
r₂   [ σ₂₁    σ₂²    σ₂₃ ]
r₃   [ σ₃₁    σ₃₂    σ₃² ]

przekątna   σᵢ²  = wariancja aktywa i     (jego własna zmienność)
poza nią    σᵢⱼ  = kowariancja i oraz j    (σᵢⱼ = σⱼᵢ)
```

Przekątna mówi, jak bardzo każde aktywo waha się samo z siebie. Wartości poza przekątną mówią, jak pary aktywów wahają się wspólnie: dodatnia kowariancja oznacza, że nadwyżki nad średnią pojawiają się zwykle razem, ujemna, że jedno rośnie, gdy drugie spada. Macierz jest symetryczna, bo kowariancja pary nie zależy od kolejności. Z tej jednej tablicy oblicza się wariancję dowolnego portfela złożonego z tych aktywów: wystarczą wagi pozycji i wartości z macierzy. Dlatego kowariancja jest punktem wyjścia u Markowitza i w każdym modelu, który liczy ryzyko portfela, a nie ryzyko pojedynczej pozycji.

## Korelacja: kowariancja bez jednostek

Kowariancja ma niewygodną cechę: jej wielkość zależy od skali. Dwa bardzo zmienne aktywa dadzą dużą kowariancję nawet przy słabym współruchu, tylko dlatego że same mocno się wahają. Korelacja usuwa ten problem, dzieląc kowariancję przez iloczyn odchyleń standardowych.

```
ρᵢⱼ = σᵢⱼ / (σᵢ · σⱼ)           korelacja Pearsona

ρᵢⱼ ∈ [−1, 1]
ρ = 1     ruch idealnie zgodny
ρ = 0     brak liniowego związku
ρ = −1    ruch idealnie przeciwny
```

Po normalizacji liczba mieści się zawsze między minus jeden a jeden i nie zależy od jednostek, więc współruch pary walut można wprost porównać ze współruchem pary obligacji. Warto pamiętać, co ta miara chwyta, a czego nie: mierzy tylko związek liniowy i jest wrażliwa na obserwacje skrajne, więc niska korelacja nie oznacza niezależności, a wysoka nie przesądza o związku przyczynowym. Macierz korelacji i macierz kowariancji niosą tę samą informację o strukturze współruchu, jedna przeskalowana do wspólnej miary, druga w jednostkach naturalnych.

## Wartości i wektory własne po ludzku

Macierz kowariancji można czytać jako opis kształtu chmury zwrotów. Ta chmura rzadko jest kulą, zwykle jest wydłużoną elipsoidą: w pewnych kierunkach dane rozrzucone są szeroko, w innych wąsko. Kierunki tej elipsoidy i ich długości to właśnie wektory i wartości własne.

```
(macierz kowariancji) · v = λ · v

v = wektor własny    kierunek, który macierz jedynie wydłuża lub skraca
λ = wartość własna   ile wariancji leży wzdłuż kierunku v

macierz symetryczna i dodatnio półokreślona:
  wektory własne wzajemnie prostopadłe
  wartości własne rzeczywiste, λ₁ ≥ λ₂ ≥ ... ≥ λₙ ≥ 0
```

Wektor własny to kierunek, którego macierz nie obraca, a jedynie rozciąga albo ściska, a odpowiadająca mu wartość własna mówi, o ile. Dla macierzy kowariancji ma to bezpośredni sens: wartość własna to ilość wariancji leżąca wzdłuż danego kierunku. Twierdzenie spektralne dla macierzy symetrycznych (Strang, Introduction to Linear Algebra) gwarantuje, że taka macierz ma komplet rzeczywistych wartości własnych i prostopadłych wektorów własnych, więc chmurę zawsze da się opisać zestawem wzajemnie niezależnych osi. Największa wartość własna wskazuje kierunek, wzdłuż którego dane zmieniają się najsilniej, najmniejsza kierunek najbardziej płaski.

## PCA: obrót do osi nieskorelowanych

Analiza głównych składowych (PCA) to zapisanie danych w układzie wektorów własnych kowariancji. Zamiast opisywać zwroty w oryginalnych współrzędnych, czyli po jednym silnie skorelowanym aktywie na oś, opisuje się je w nowych osiach, uporządkowanych według malejącej wartości własnej.

```
PC₁ = kierunek największej wariancji                    (największe λ₁)
PC₂ = największa wariancja wśród kierunków prostopadłych do PC₁   (λ₂)
...   każda kolejna prostopadła do wszystkich wcześniejszych

udział składowej k = λₖ / (λ₁ + λ₂ + ... + λₙ)
```

Dwie własności czynią ten obrót użytecznym. Po pierwsze, nowe osie są nieskorelowane, bo wektory własne są prostopadłe, więc splątany współruch aktywów rozkłada się na niezależne składowe. Po drugie, składowe są posortowane: pierwsza chwyta najwięcej zmienności, każda następna mniej. Jeśli kilka pierwszych wartości własnych skupia większość ich sumy, resztę można pominąć niemal bez straty informacji. Na tym polega redukcja wymiaru: wiele skorelowanych szeregów opisuje się kilkoma liczbami. Jolliffe (Principal Component Analysis) traktuje ten rozkład jako podstawowe narzędzie zbijania wymiaru w danych o silnej strukturze korelacyjnej. Poniższy diagram pokazuje sam obrót: chmurę punktów i dwie osie własne, dłuższą pierwszą i krótszą drugą.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="28" font-size="13" fill="currentColor">PCA: obrót do osi największej zmienności</text><circle cx="198" cy="226" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="205" cy="194" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="239" cy="217" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="224" cy="174" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="250" cy="195" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="244" cy="159" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="277" cy="204" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="266" cy="170" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="291" cy="186" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="280" cy="152" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="311" cy="193" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="295" cy="150" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="315" cy="167" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="303" cy="132" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="328" cy="171" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="321" cy="146" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="343" cy="168" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="329" cy="128" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="352" cy="153" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="349" cy="124" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="376" cy="156" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="366" cy="124" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="385" cy="140" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="378" cy="102" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="401" cy="127" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="400" cy="102" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="422" cy="125" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="416" cy="88" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="436" cy="107" r="2.6" fill="currentColor" opacity="0.42"/><circle cx="442" cy="84" r="2.6" fill="currentColor" opacity="0.42"/><line x1="185" y1="221" x2="455" y2="89" stroke="#0b66c3" stroke-width="2.4"/><path d="M446.4 98.8 L455 89 L442 89.8" fill="none" stroke="#0b66c3" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><line x1="344" y1="205" x2="296" y2="106" stroke="#1a9e6a" stroke-width="2.4"/><path d="M305.8 114.6 L296 106 L296.8 119" fill="none" stroke="#1a9e6a" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="320" cy="155" r="2.2" fill="currentColor" opacity="0.75"/><text x="330" y="71" font-size="10.5" fill="#0b66c3">PC₁: pierwsza składowa, największa wariancja</text><text x="60" y="92" font-size="10.5" fill="#1a9e6a">PC₂: prostopadła, mniejsza wariancja</text><text x="322" y="238" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">osie przecinają się w średniej danych</text></svg>
<figcaption>Chmura zwrotów dwóch aktywów i jej osie własne. Niebieska pierwsza składowa (PC1) biegnie wzdłuż kierunku największej zmienności, zielona druga (PC2) jest do niej prostopadła i krótsza, bo w tym kierunku dane są rozrzucone słabiej. PCA to zapisanie punktów w tym właśnie obróconym układzie: nowe osie są nieskorelowane, a ich długości odpowiadają wartościom własnym. Kierunek osi wynika z danych, a nie z wyjściowego wyboru współrzędnych.</figcaption>
</figure>

## Krzywa dochodowości: poziom, nachylenie, krzywizna

Najbardziej znane zastosowanie PCA w finansach dotyczy stóp procentowych. Rentowności obligacji o różnych terminach są silnie skorelowane: gdy rośnie jedna, zwykle rosną pozostałe. Litterman i Scheinkman w pracy "Common Factors Affecting Bond Returns" (Journal of Fixed Income, 1991) rozłożyli zmienność krzywej dochodowości na główne składowe i pokazali, że wystarczą trzy, aby opisać niemal całą jej ruchomość, a każda ma czytelną interpretację.

```
Litterman i Scheinkman (1991), krzywa dochodowości obligacji USA
(udziały przybliżone, po zaokrągleniu):

PC₁  poziom       ~ 90%    równoległe przesunięcie całej krzywej
PC₂  nachylenie   ~  8%    krótki koniec kontra długi
PC₃  krzywizna    ~  2%    środek kontra oba końce
```

Pierwsza składowa to poziom: jej wektor własny ma zbliżone współrzędne dla wszystkich terminów, więc odpowiada równoległemu ruchowi całej krzywej w górę lub w dół i sama tłumaczy około dziewięćdziesięciu procent zmienności. Druga to nachylenie: dodatnia na jednym końcu, ujemna na drugim, czyli stromienie i wypłaszczanie. Trzecia to krzywizna: odmienny ruch środka względem obu końców. Ten sam schemat, jedna dominująca składowa wspólna plus kilka o mniejszym udziale, pojawia się na innych rynkach o silnym współruchu, na przykład w koszykach walut, gdzie pierwsza składowa bywa czytana jako wspólny czynnik ryzyka, zbliżony do ogólnej siły dolara. Interpretacja składowych nie jest jednak z góry dana przez matematykę, tylko odczytana z kształtu wektorów własnych po fakcie, i akurat na krzywej dochodowości wychodzi wyjątkowo czysto.

## Zaplecze modeli czynnikowych i CAPM

Rachunek własny kowariancji jest tym samym obliczeniem, które stoi za modelami czynnikowymi. Model czynnikowy zakłada, że zwroty są napędzane przez kilka wspólnych czynników plus składnik specyficzny dla aktywa. PCA wyprowadza kandydatów na te czynniki wprost z danych, jako kierunki największej wspólnej zmienności. W CAPM (Sharpe 1964) rolę jedynego czynnika gra portfel rynkowy, a beta to nachylenie zwrotu aktywa względem niego. W modelach wieloczynnikowych, jak trójczynnikowy Famy i Frencha (1993), czynników jest kilka. PCA pokazuje, dlaczego tak niewiele wystarcza: skoro pierwsza składowa rynku akcji czy krzywej stóp tłumaczy większość wariancji, kilka kierunków rzeczywiście niesie prawie całą wspólną strukturę. Kowariancja daje strukturę, rozkład własny nazywa jej kierunki, a model czynnikowy przypisuje im premie.

## Ryzyko PCA

Obrót do osi własnych jest dokładny co do algebry, ale krucha jest sama macierz kowariancji, z której się go liczy. Trzy ostrzeżenia wracają najczęściej.

Pierwsze to niestabilność w czasie. Kowariancje zmieniają się wraz z reżimem rynku, a w okresach stresu korelacje rosną, więc wektory własne policzone z jednego okna potrafią wskazywać inne kierunki niż z okna następnego. Obrót nie jest stałą natury, tylko funkcją próby.

Drugie to interpretacja. Poziom, nachylenie i krzywizna krzywej dochodowości to szczęśliwy przypadek czytelności. Zwykle składowe są kombinacjami wielu aktywów bez nazwy ekonomicznej, a ich znak oraz porządek są kwestią umowną, więc łatwo dorobić do nich historię, której dane nie potwierdzają.

Trzecie to estymacja przy krótkiej próbie. Gdy liczba obserwacji nie jest znacznie większa od liczby aktywów, oszacowana kowariancja jest obarczona dużym błędem, a najmniejsze wartości własne bywają zaniżone i niestabilne. Jolliffe (Principal Component Analysis) oraz literatura o estymacji macierzy kowariancji zalecają wtedy ostrożność i techniki uodparniające, jak regularyzacja czy ściąganie ku prostszej strukturze. Wniosek jest spójny z całą serią: algebra jest pewna, dane nie, więc składowe warto traktować jako opis konkretnej próby, a nie jako trwałe prawo rynku.

## Co z tego zostaje

Algebra liniowa daje kowariancji zwięzły język: przekątna to własne ryzyko, reszta to współruch, a rozkład na wartości i wektory własne zamienia splątaną chmurę w garść nieskorelowanych kierunków. PCA porządkuje te kierunki według wagi i pozwala opisać wiele instrumentów kilkoma liczbami, co na krzywej dochodowości daje czytelne poziom, nachylenie i krzywiznę (Litterman i Scheinkman 1991), a w modelach czynnikowych i CAPM stanowi matematyczne zaplecze. Cena tej zwięzłości to zależność od próby: obrót jest tak wiarygodny, jak kowariancja, z której powstał.

To nie jest porada inwestycyjna. To edukacyjne omówienie algebry liniowej w analizie rynków: definicje kowariancji, korelacji, wartości i wektorów własnych oraz analizy głównych składowych są zreferowane za podręcznikami (Strang; Jolliffe), a przykład krzywej dochodowości za pracą Littermana i Scheinkmana (1991).

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
