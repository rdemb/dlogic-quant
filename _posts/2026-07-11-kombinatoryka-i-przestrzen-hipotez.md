---
title: "Kombinatoryka i przestrzeń hipotez. Dlaczego szukanie prawie zawsze coś znajdzie"
description: "Reguła iloczynu zamienia kilka wskaźników po kilka progów w tysiące strategii: cztery progi na siedem parametrów to już 16 384 konfiguracje, a z kierunkiem i interwałem blisko 100 000. Przy poziomie istotności 5% oczekiwana liczba fałszywych odkryć to iloczyn poziomu istotności i liczby prób, więc z 16 384 wariantów czystego szumu wychodzi około 819 „istotnych". Podstawy zliczania, paradoks urodzin (23 osoby, ponad 50%), próg t powyżej 3 z pracy Harveya, Liu i Zhu (2016) oraz kontrola FDR Benjaminiego i Hochberga (1995)."
date: 2026-07-11 20:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Ile strategii da się zbudować z kilku wskaźników i kilku progów? Reguła iloczynu odpowiada: wykładniczo wiele. Im większa przeszukiwana przestrzeń, tym pewniejsze, że coś w niej wygląda na przewagę, nawet gdy jej nie ma. Podstawy kombinatoryki, oczekiwana liczba fałszywych trafień, paradoks urodzin i korekty na wielokrotne testowanie, czyli dlaczego rozmiar przestrzeni hipotez jest mianownikiem każdego wyniku."
readingTime: 8
tags: [matematyka, kombinatoryka, "przestrzeń hipotez", "wielokrotne testowanie", "data snooping", Bonferroni, FDR, "symbol Newtona", "paradoks urodzin", "Harvey Liu Zhu", "López de Prado", overfitting, "istotność statystyczna", edukacja]
category: edukacja
---

> **W skrócie**
>
> - Reguła iloczynu: kilka niezależnych wyborów mnoży się przez siebie, więc przestrzeń strategii rośnie wykładniczo. Cztery progi na parametr i siedem łączonych parametrów to 4^7 = 16 384 konfiguracje, a dorzucenie dwóch kierunków i trzech interwałów podnosi liczbę do około 98 000. Kilka „prostych" list generuje dziesiątki tysięcy wariantów.
> - Przy poziomie istotności 5% co dwudziesty test czystego szumu wypada „istotnie", a oczekiwana liczba fałszywych odkryć to poziom istotności razy liczba prób. Sto testów daje średnio pięć fałszywych trafień, 1 024 dają około 51, a 16 384 około 819. Im większa przestrzeń, tym pewniejsze fałszywe odkrycie.
> - Paradoks urodzin pokazuje, że zbieżności są częstsze, niż podpowiada intuicja: wśród 23 osób prawdopodobieństwo wspólnej daty urodzin przekracza 50%, bo liczy się nie liczba osób, tylko liczba par, czyli C(23,2) = 253. Tak samo dwie strategie „pasujące" do siebie w danych to zwykle przypadek z wielkiej liczby możliwych par.
> - Korekty istnieją: Bonferroni dzieli poziom istotności przez liczbę testów (kontrola FWER), a FDR Benjaminiego i Hochberga (1995) pilnuje odsetka fałszywych wśród ogłoszonych odkryć. Harvey, Liu i Zhu (2016) policzyli, że po dekadach przeszukiwania tych samych danych nowy faktor powinien przekraczać t równe 3, a nie klasyczne 2.

**Teza w jednym zdaniu:** Pojedynczy dobry wynik nie znaczy nic bez liczby hipotez, z których go wyłowiono, bo kombinatoryka sprawia, że przestrzeń możliwych strategii rośnie wykładniczo, a w dostatecznie wielkiej przestrzeni znalezienie czegoś imponującego w czystym szumie jest nie ryzykiem, tylko pewnością.

## Reguła iloczynu, permutacje, kombinacje

Zliczanie zaczyna się od jednej zasady: jeśli decyzja składa się z kilku niezależnych wyborów, liczba wszystkich wariantów jest iloczynem liczby możliwości w każdym kroku. To reguła iloczynu. Trzy wskaźniki, każdy w jednym z czterech ustawień, to nie trzy dodać cztery, tylko cztery razy cztery razy cztery, czyli 64 kombinacje. Dodanie czwartego wskaźnika nie dokłada kilku wariantów, tylko mnoży całość przez cztery.

Z reguły iloczynu wynikają dwa dalsze narzędzia. Permutacje liczą, na ile sposobów można ustawić n różnych elementów w kolejności: to n silnia, czyli iloczyn wszystkich liczb od n do jednego. Kombinacje liczą, na ile sposobów można wybrać k elementów z n, gdy kolejność nie ma znaczenia. Ta druga liczba to symbol Newtona, czytany „n po k"; jego wartość to n silnia podzielona przez k silnia i przez silnię różnicy między n a k. Rośnie zaskakująco szybko: wybór pięciu wskaźników z pięćdziesięciu dostępnych to ponad dwa miliony możliwych zestawów.

```
REGUŁA ILOCZYNU
k niezależnych wyborów: n1, n2, ..., nk możliwości
liczba wariantów = n1 · n2 · ... · nk

PERMUTACJE   ustawienia n różnych elementów w kolejności
P(n) = n! = n · (n−1) · ... · 2 · 1
wariacje k z n (kolejność ważna) = n! / (n−k)!

KOMBINACJE   wybór k z n, kolejność nieważna = symbol Newtona
C(n,k) = n! / ( k! · (n−k)! )        czytane „n po k"

3! = 6      5! = 120      10! = 3 628 800
C(10,3) = 120        C(50,5) = 2 118 760
```

## Jak przestrzeń strategii puchnie

Budowa strategii to właśnie łańcuch takich wyborów: który wskaźnik, jaki próg wejścia i wyjścia, jaki interwał, kierunek, filtr sesji. Każdy z tych wymiarów ma po kilka rozsądnych ustawień, a reguła iloczynu spina je w jedną liczbę. Przy czterech progach na parametr każdy dołączony wymiar mnoży przestrzeń przez cztery, więc liczba konfiguracji rośnie jak cztery do potęgi równej liczbie parametrów.

<figure>
<svg viewBox="0 0 640 348" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="70" y="24" font-size="13" fill="currentColor">Przestrzeń strategii rośnie wykładniczo z liczbą łączonych parametrów</text><rect x="70" y="32" width="12" height="12" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><text x="88" y="42" font-size="11" fill="currentColor" opacity="0.8">liczba kombinacji (4 progi na parametr)</text><line x1="330" y1="38" x2="356" y2="38" stroke="#e5484d" stroke-width="2.2" stroke-dasharray="5 4"/><circle cx="343" cy="38" r="3.2" fill="#e5484d"/><text x="362" y="42" font-size="11" fill="currentColor" opacity="0.8">oczekiwane fałszywe odkrycia, α = 5%</text><line x1="70" y1="80" x2="600" y2="80" stroke="currentColor" stroke-width="1" opacity="0.12"/><line x1="70" y1="122" x2="600" y2="122" stroke="currentColor" stroke-width="1" opacity="0.12"/><line x1="70" y1="164" x2="600" y2="164" stroke="currentColor" stroke-width="1" opacity="0.12"/><line x1="70" y1="206" x2="600" y2="206" stroke="currentColor" stroke-width="1" opacity="0.12"/><line x1="70" y1="248" x2="600" y2="248" stroke="currentColor" stroke-width="1" opacity="0.12"/><line x1="70" y1="290" x2="600" y2="290" stroke="currentColor" stroke-width="1" opacity="0.5"/><line x1="70" y1="80" x2="70" y2="290" stroke="currentColor" stroke-width="1" opacity="0.5"/><text x="63" y="293" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">1</text><text x="63" y="251" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">10</text><text x="63" y="209" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">100</text><text x="63" y="167" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">1 000</text><text x="63" y="125" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">10 000</text><text x="63" y="83" font-size="10" fill="currentColor" opacity="0.55" text-anchor="end">100 000</text><text transform="rotate(-90 26 185)" x="26" y="185" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">liczba kombinacji, skala log</text><rect x="96.8" y="264.7" width="40" height="25.3" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="170.4" y="239.4" width="40" height="50.6" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="243.9" y="214.1" width="40" height="75.9" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="317.5" y="188.9" width="40" height="101.1" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="391.1" y="163.6" width="40" height="126.4" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="464.6" y="138.3" width="40" height="151.7" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><rect x="538.2" y="113.0" width="40" height="177.0" fill="#0b66c3" fill-opacity="0.15" stroke="#0b66c3" stroke-width="1.5"/><text x="116.8" y="259.7" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">4</text><text x="190.4" y="234.4" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">16</text><text x="263.9" y="209.1" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">64</text><text x="337.5" y="183.9" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">256</text><text x="411.1" y="158.6" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">1 024</text><text x="484.6" y="133.3" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">4 096</text><text x="558.2" y="108.0" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">16 384</text><polyline points="263.9,268.8 337.5,243.5 411.1,218.2 484.6,192.9 558.2,167.6" fill="none" stroke="#e5484d" stroke-width="2.2" stroke-dasharray="5 4"/><circle cx="263.9" cy="268.8" r="3.2" fill="#e5484d"/><circle cx="337.5" cy="243.5" r="3.2" fill="#e5484d"/><circle cx="411.1" cy="218.2" r="3.2" fill="#e5484d"/><circle cx="484.6" cy="192.9" r="3.2" fill="#e5484d"/><circle cx="558.2" cy="167.6" r="3.2" fill="#e5484d"/><text x="548" y="180" font-size="10" fill="#e5484d" text-anchor="end">≈ 819</text><text x="116.8" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">1</text><text x="190.4" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">2</text><text x="263.9" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">3</text><text x="337.5" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">4</text><text x="411.1" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">5</text><text x="484.6" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">6</text><text x="558.2" y="306" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">7</text><text x="335" y="330" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">liczba łączonych parametrów</text></svg>
<figcaption>Oś pionowa jest logarytmiczna, więc wykładniczy wzrost liczby kombinacji układa się w prostą linię słupków. Czerwona linia to oczekiwana liczba fałszywych odkryć przy istotności 5%, czyli jedna dwudziesta wysokości słupków: biegnie równolegle do ich wierzchołków, zawsze 20 razy niżej, ale w tym samym tempie. Przy 16 384 kombinacjach to wciąż około 819 fałszywych trafień.</figcaption>
</figure>

Wzrost jest wykładniczy, a intuicja liniowa. Nikt nie planuje testować stu tysięcy strategii; ta liczba powstaje sama, jako iloczyn kilku list, z których każda z osobna wydaje się krótka.

```
b progów na parametr, d łączonych parametrów  →  b^d konfiguracji

b = 4:
  d = 1  →       4
  d = 2  →      16
  d = 3  →      64
  d = 4  →     256
  d = 5  →   1 024
  d = 6  →   4 096
  d = 7  →  16 384

dorzuć 2 kierunki i 3 interwały:  16 384 · 2 · 3 ≈ 98 000
```

## Im większa przestrzeń, tym pewniejsze fałszywe odkrycie

Tu kombinatoryka spotyka statystykę. Pojedynczy test na poziomie istotności 5% z definicji myli się raz na dwadzieścia: godzimy się, że coś, co nie działa, czasem pokaże „efekt". Przy jednym teście to rozsądny kompromis. Przy przeszukiwaniu całej przestrzeni przestaje nim być, bo oczekiwana liczba fałszywych odkryć rośnie liniowo z liczbą prób i wynosi po prostu poziom istotności pomnożony przez liczbę testów.

```
oczekiwane fałszywe odkrycia, gdy żaden wariant nie działa:
E[fałszywe] = α · N

α = 5%:
  N =    100   →     5
  N =  1 024   →   ~51
  N = 16 384   →  ~819
  N = 98 000   → ~4 900

pojedynczy test bez korekty: raz na 20 prób „istotny"
```

Liczby z poprzednich sekcji wchodzą tu wprost: grid 1 024 konfiguracji przy zerowej przewadze wyprodukuje średnio pięćdziesiąt „istotnych" wariantów. Przestrzeń 16 384 strategii da ich około ośmiuset. To nie pech ani błąd w kodzie, tylko arytmetyka: maksimum z wielkiej liczby losowych wyników prawie zawsze leży daleko w prawym ogonie rozkładu. Bailey, Borwein, López de Prado i Zhu (2014) doprowadzili tę obserwację do wniosku granicznego: przy dostatecznie wielu wypróbowanych konfiguracjach znalezienie strategii ze świetnym wynikiem w próbie jest gwarantowane, nawet gdy wszystkie konfiguracje to czysty szum, a minimalna długość danych potrzebna, żeby odróżnić najlepszy wynik od przypadku, rośnie razem z liczbą prób.

## Paradoks urodzin: zbieżności są częstsze, niż się wydaje

Dlaczego przeszukiwanie tak łatwo produkuje zbieżności, dobrze tłumaczy klasyczna zagadka. Ile osób musi znaleźć się w pokoju, żeby szansa na dwie te same daty urodzin przekroczyła połowę? Intuicja podpowiada setki, bo dni w roku jest 365. Odpowiedź to 23. Sekret polega na tym, że nie liczy się liczba osób, tylko liczba par, które można z nich utworzyć, a tych jest C(23,2) = 253. Prawdopodobieństwo, że żadna para nie trafi we wspólną datę, to iloczyn kurczących się ułamków, który przy 23 osobach spada poniżej połowy.

```
PARADOKS URODZIN
P(brak wspólnej daty wśród g osób) =
    365/365 · 364/365 · ... · (365 − g + 1)/365
P(co najmniej jedna wspólna data) = 1 − powyższe

g = 23   →  ~50,7 %      (wystarczą 23 osoby)
g = 41   →  ~90,3 %
g = 57   →  ~99,0 %

liczba par:  C(g,2) = g · (g − 1) / 2
C(23,2) = 253 pary możliwych zbieżności
```

Morał jest ogólny i dotyczy każdego przeszukiwania: zbieżności skalują się z liczbą par, a nie z liczbą obiektów, więc pojawiają się znacznie wcześniej, niż podpowiada zdrowy rozsądek. Dwa wskaźniki, które „ładnie się potwierdzają" na wykresie, albo strategia dziwnie dobrze dopasowana do jednego rynku, to zwykle jedna z bardzo wielu możliwych par, a nie ślad prawdziwej struktury.

## Liczba prób efektywnych: Bonferroni i FDR

Skoro problem jest ilościowy, to i lekarstwo jest ilościowe. Najprostsza korekta na wielokrotne testowanie to Bonferroni: przy N testach każdy pojedynczy prowadzi się na poziomie istotności podzielonym przez N. Chroni przed choćby jednym fałszywym odkryciem w całej rodzinie prób, czyli kontroluje tak zwane FWER, ale przy tysiącach testów robi się drakońska i wycina razem z szumem większość prawdziwych efektów.

Bonferroni zakłada przy tym, że testy są niezależne, a w praktyce rzadko są. Warianty tej samej strategii z lekko przesuniętym progiem dają niemal identyczne wyniki, więc liczą się prawie jak jeden test. Dlatego mówi się o liczbie prób efektywnych, mniejszej od surowej liczby konfiguracji: silnie skorelowane warianty nie mnożą ryzyka fałszywego odkrycia tak, jak sugerowałaby ich liczba. To jednocześnie pułapka, bo łatwo oszukać samego siebie, licząc dziesięć tysięcy powiązanych wariantów jako „kilka pomysłów".

Druga rodzina korekt odpuszcza perfekcję. Kontrola FDR, zaproponowana przez Benjaminiego i Hochberga (1995), nie obiecuje zera pomyłek, tylko trzyma oczekiwany odsetek fałszywych wśród ogłoszonych odkryć poniżej ustalonego progu. Przy skanowaniu tysięcy kandydatów zachowuje moc: nadal cokolwiek znajduje, ale z jawną etykietą jakości zamiast iluzji pewności.

```
BONFERRONI   (kontrola FWER)
każdy z N testów na poziomie α / N
N = 1 000, α = 5%  →  próg jednego testu = 0,005 %

PRÓBY EFEKTYWNE
testy skorelowane liczą się prawie jak jeden:  N_eff < N

FDR   (Benjamini i Hochberg, 1995)
kontroluj odsetek fałszywych wśród ogłoszonych odkryć ≤ q
posortuj p rosnąco; przyjmij do największego k: p(k) ≤ (k/N) · q
```

Że to nie jest problem czysto teoretyczny, pokazuje literatura o faktorach giełdowych. Harvey, Liu i Zhu (2016) zauważyli, że przez dekady setki badaczy przeszukiwały w dużej mierze te same dane, więc klasyczny próg t około 2, odpowiednik istotności 5% dla jednego testu, jest za niski. Po uwzględnieniu skali zbiorowego przeszukiwania nowy faktor powinien przekraczać t równe 3, a około połowy faktorów ogłoszonych w literaturze jest prawdopodobnie fałszywa. To rachunek na poziomie całej profesji, nie zarzut wobec pojedynczych autorów.

## Mianownik, bez którego wynik nic nie znaczy

Wszystkie wątki schodzą się w jednej myśli. Rozmiar przeszukiwanej przestrzeni to mianownik każdego wyniku. Sharpe, win rate czy „istotność" mówią coś dopiero wtedy, gdy obok stoi liczba hipotez, z których ten jeden wynik wyłowiono. Ta sama metryka znaczy co innego po jednej próbie i po dziesięciu tysiącach: w drugim przypadku porównywać ją trzeba nie z zerem, tylko z najlepszym z dziesięciu tysięcy wyników na czystym szumie.

Praktyczny odruch jest prosty: przed oceną wyniku policzyć próby. Każdy dołączony wskaźnik, każdy przesunięty próg, każda zmiana rynku czy okresu, nawet „szybki rzut oka" na wykres z nową hipotezą, to kolejny element iloczynu, który powiększa przestrzeń i podnosi poprzeczkę dla wszystkiego, co znajdzie się później. Kombinatoryka nie jest tu przeszkodą do obejścia, tylko licznikiem, który trzeba prowadzić uczciwie. Bez niego pojedyncze odkrycie jest tym, czym maksimum z wielkiego zbioru losowych liczb: ładną liczbą bez znaczenia.

Materiał czysto edukacyjny, nie porada inwestycyjna. Przykłady liczbowe służą pokazaniu, jak szybko rośnie przestrzeń hipotez i jak skaluje się w niej liczba fałszywych odkryć; nie opisują żadnej konkretnej strategii ani wyniku. Pewna jest tu wyłącznie matematyka zliczania: reguła iloczynu, symbol Newtona, iloczyn poziomu istotności i liczby prób oraz korekty na wielokrotne testowanie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
