---
layout: labpost
title: "Czy oddychasz Cezarem? Matematyka mówi: prawdopodobnie, nie na pewno"
description: "Słynny rachunek ostatniego oddechu Cezara daje wartość oczekiwaną, a nie gwarancję. O liczbie Avogadra, mieszaniu atmosfery, rozkładzie Poissona i granicach pięknej metafory."
dek: "Dla dwóch półlitrowych oddechów idealny model daje średnio około 1,4 cząsteczki wspólnego pochodzenia, ale prawdopodobieństwo znalezienia przynajmniej jednej wynosi około 76%, nie 100%."
date: 2026-08-11 16:50:00 +0200
category: luzne
tags: [odkrywanie-niewidzialnego, fizyka, statystyka, atmosfera, prawdopodobienstwo]
eyebrow: "Odkrywanie niewidzialnego #05"
readingTime: 16
section_url: /odkrywanie-niewidzialnego/
section_label: Odkrywanie niewidzialnego
cover_brand: "FIZYKA · GRANICE INTUICJI #05"
cover_title: "ŚREDNIA NIE JEST GWARANCJĄ"
cover_subtitle: "AVOGADRO · ATMOSFERA · POISSON · CEZAR"
cover_kind: loose
---
<div class="article-status"><span class="primary">ESEJ ŹRÓDŁOWY</span><span>FIZYKA STATYSTYCZNA</span><span>RACHUNEK RZĘDU WIELKOŚCI</span><span>MODEL IDEALIZOWANY</span></div>

Właśnie bierzesz oddech. W pół litrze powietrza znajduje się około dziesięciu tryliardów cząsteczek - liczba tak ogromna, że pojedynczy wydech może po rozproszeniu w atmosferze pozostawić ślad w oddechach ludzi żyjących tysiące lat później.

Stąd bierze się jedna z najbardziej sugestywnych opowieści fizyki statystycznej: w każdym wdechu znajduje się przynajmniej jedna cząsteczka z ostatniego oddechu Juliusza Cezara.

Historia brzmi jak materialna forma nieśmiertelności. Cezar umiera w idy marcowe, powietrze opuszcza jego płuca, wiatry rozprowadzają cząsteczki po planecie, a po dwóch tysiącach lat jedna z nich trafia do ciebie. Problem polega na tym, że rachunek nie mówi dokładnie tego, co obiecuje popularne zdanie.

Dla rozsądnego zestawu założeń wynik wynosi około **1,4**. Nie oznacza to, że w każdym oddechu musi znaleźć się jedna cząsteczka i dodatkowe cztery dziesiąte. Jest to wartość oczekiwana rozkładu liczby trafień. Jeżeli cząsteczki są rozmieszczone losowo i niezależnie, część oddechów nie zawiera żadnej, część jedną, część dwie albo więcej.

> **Średnia równa 1,4 daje w idealizowanym modelu około 76% szans na przynajmniej jedno trafienie - dużo, ale nie pewność.**

Jeszcze ważniejsze jest to, że nie posiadamy próbki ostatniego wydechu Cezara, nie znamy jego objętości ani dalszych losów poszczególnych cząsteczek. Rachunek jest eksperymentem myślowym pokazującym skalę liczby Avogadra i potęgę mieszania, nie testem genealogicznym powietrza w twoich płucach.

## Ile cząsteczek znajduje się w jednym oddechu?

Dla gazu w temperaturze pokojowej możemy użyć równania gazu doskonałego:

\[
PV=nRT.
\]

Przy ciśnieniu jednej atmosfery, temperaturze około 25°C i objętości pół litra otrzymujemy około 0,0204 mola gazu. Stała Avogadra ma dokładnie zdefiniowaną wartość:

\[
N_A=6{,}02214076\times10^{23}\ \text{mol}^{-1}.
\]

Po przemnożeniu wychodzi około:

\[
N_{oddech}\approx1{,}23\times10^{22}
\]

cząsteczek.

Ta liczba jest tak wielka, że intuicja przestaje działać. Milion sekund to około jedenaście i pół dnia. Miliard sekund to ponad trzydzieści jeden lat. Liczba cząsteczek w oddechu jest jeszcze ponad dziesięć bilionów razy większa od miliarda.

## Ile cząsteczek zawiera atmosfera?

Masa ziemskiej atmosfery wynosi około \(5{,}15\times10^{18}\) kilogramów. Dzieląc ją przez średnią masę molową suchego powietrza, a następnie mnożąc przez stałą Avogadra, otrzymujemy około:

\[
N_{atm}\approx1{,}07\times10^{44}
\]

cząsteczek.

Jeżeli jeden półlitrowy wydech zawiera \(1{,}23\times10^{22}\) cząsteczek i rozprowadzi się idealnie po atmosferze, udział jego cząsteczek wyniesie w przybliżeniu:

\[
f=\frac{N_{źródło}}{N_{atm}}\approx1{,}15\times10^{-22}.
\]

W nowym półlitrowym wdechu znajduje się ponownie około \(1{,}23\times10^{22}\) cząsteczek. Oczekiwana liczba pochodząca z historycznego wydechu to:

\[
\lambda=N_{wdech}f\approx1{,}42.
\]

<figure>
<svg viewBox="0 0 1080 430" role="img" aria-labelledby="caesar-calc-title caesar-calc-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="caesar-calc-title">Rachunek oczekiwanej liczby cząsteczek</title>
 <desc id="caesar-calc-desc">Półlitrowy wydech zawiera około 1,23 razy dziesięć do dwudziestej drugiej cząsteczek, atmosfera około 1,07 razy dziesięć do czterdziestej czwartej, a oczekiwana liczba w nowym półlitrowym wdechu wynosi 1,42.</desc>
 <defs><marker id="caesar-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="var(--acc)"/></marker></defs>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <rect x="28" y="118" width="230" height="126" rx="16" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="308" y="118" width="230" height="126" rx="16" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="588" y="118" width="210" height="126" rx="16" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="848" y="98" width="204" height="166" rx="18" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
 <path d="M258 181 H302 M538 181 H582 M798 181 H842" stroke="var(--acc)" stroke-width="3" marker-end="url(#caesar-arrow)"/>
 <text x="143" y="151" text-anchor="middle" font-size="16" fill="var(--ink)">WYDECH 0,5 L</text><text x="143" y="191" text-anchor="middle" font-size="24" fill="var(--acc)">1,23×10²²</text><text x="143" y="220" text-anchor="middle" font-size="13" fill="var(--mut)">cząsteczek</text>
 <text x="423" y="151" text-anchor="middle" font-size="16" fill="var(--ink)">ATMOSFERA</text><text x="423" y="191" text-anchor="middle" font-size="24" fill="var(--acc)">1,07×10⁴⁴</text><text x="423" y="220" text-anchor="middle" font-size="13" fill="var(--mut)">cząsteczek</text>
 <text x="693" y="151" text-anchor="middle" font-size="16" fill="var(--ink)">UDZIAŁ f</text><text x="693" y="191" text-anchor="middle" font-size="22" fill="var(--acc)">1,15×10⁻²²</text><text x="693" y="220" text-anchor="middle" font-size="13" fill="var(--mut)">przy idealnym mieszaniu</text>
 <text x="950" y="140" text-anchor="middle" font-size="16" fill="var(--ink)">NOWY WDECH 0,5 L</text><text x="950" y="191" text-anchor="middle" font-size="38" fill="var(--acc)">λ ≈ 1,42</text><text x="950" y="226" text-anchor="middle" font-size="13" fill="var(--mut)">wartość oczekiwana</text>
 <text x="540" y="324" text-anchor="middle" font-size="19" fill="var(--ink)">Duże liczby upraszczają rachunek - ale nie zamieniają średniej w gwarancję.</text>
 </g>
</svg>
<figcaption>Wynik zależy liniowo od objętości wydechu źródłowego i objętości badanego wdechu, a odwrotnie od liczby cząsteczek w atmosferze.</figcaption>
</figure>

## Dlaczego 1,42 nie oznacza „co najmniej jednej”?

Załóżmy, że każda cząsteczka w nowym oddechu ma bardzo małe, niezależne prawdopodobieństwo należenia do historycznej próbki. W granicy ogromnej liczby prób i bardzo małego prawdopodobieństwa liczba trafień jest dobrze przybliżana rozkładem Poissona.

Prawdopodobieństwo braku jakiejkolwiek cząsteczki wynosi:

\[
P(0)=e^{-\lambda}.
\]

Dla \(\lambda=1{,}42\):

\[
P(0)\approx24{,}3\%,
\]

więc:

\[
P(X\geq1)=1-e^{-\lambda}\approx75{,}7\%.
\]

Najbardziej prawdopodobny pojedynczy wynik to jedna cząsteczka, ale brak trafienia nie jest rzadką anomalią. W idealnym modelu wystąpiłby mniej więcej w co czwartym półlitrowym oddechu.

<figure>
<svg viewBox="0 0 1040 430" role="img" aria-labelledby="poisson-title poisson-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="poisson-title">Rozkład Poissona dla lambda 1,42</title>
 <desc id="poisson-desc">Prawdopodobieństwa zera, jednego, dwóch, trzech, czterech i pięciu trafień wynoszą odpowiednio około 24,3, 34,4, 24,3, 11,5, 4,1 i 1,1 procent.</desc>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <line x1="100" y1="344" x2="948" y2="344" stroke="var(--line)" stroke-width="3"/>
 <rect x="132" y="150" width="96" height="194" rx="8" fill="var(--dn)" opacity=".78"/>
 <rect x="276" y="70" width="96" height="274" rx="8" fill="var(--acc)" opacity=".82"/>
 <rect x="420" y="150" width="96" height="194" rx="8" fill="var(--acc)" opacity=".66"/>
 <rect x="564" y="252" width="96" height="92" rx="8" fill="var(--acc)" opacity=".58"/>
 <rect x="708" y="312" width="96" height="32" rx="8" fill="var(--acc)" opacity=".5"/>
 <rect x="852" y="335" width="96" height="9" rx="5" fill="var(--acc)" opacity=".45"/>
 <text x="180" y="136" text-anchor="middle" font-size="16" fill="var(--dn)">24,3%</text><text x="324" y="56" text-anchor="middle" font-size="16" fill="var(--acc)">34,4%</text><text x="468" y="136" text-anchor="middle" font-size="16" fill="var(--acc)">24,3%</text><text x="612" y="238" text-anchor="middle" font-size="16" fill="var(--acc)">11,5%</text><text x="756" y="298" text-anchor="middle" font-size="16" fill="var(--acc)">4,1%</text><text x="900" y="321" text-anchor="middle" font-size="16" fill="var(--acc)">1,1%</text>
 <text x="180" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">0</text><text x="324" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">1</text><text x="468" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">2</text><text x="612" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">3</text><text x="756" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">4</text><text x="900" y="378" text-anchor="middle" font-size="17" fill="var(--ink)">5</text>
 <text x="520" y="414" text-anchor="middle" font-size="14" fill="var(--mut)">liczba cząsteczek w idealizowanym wdechu</text>
 </g>
</svg>
<figcaption>Rozkład dla λ≈1,42. Prawdopodobieństwo sześciu lub więcej trafień wynosi łącznie mniej niż pół procenta.</figcaption>
</figure>

Popularny wniosek staje się niemal pewny, gdy zmienimy założenia objętości. Jeżeli zarówno historyczny wydech, jak i obecny wdech mają po litrze, wartość oczekiwana rośnie czterokrotnie, ponieważ podwajamy jednocześnie próbkę źródłową i pobieraną.

| Wydech źródłowy | Obecny wdech | Oczekiwana liczba λ | Prawdopodobieństwo ≥1 |
|---:|---:|---:|---:|
| 0,5 L | 0,5 L | 1,42 | 75,7% |
| 0,5 L | 1,0 L | 2,83 | 94,1% |
| 1,0 L | 1,0 L | 5,66 | 99,65% |

Dlatego dwie wersje tej samej anegdoty mogą dawać wrażenie sprzeczności, choć różnią się jedynie przyjętą objętością.

## Atmosfera nie jest idealnym mieszalnikiem

Wiatry, konwekcja i turbulencja przenoszą gazy na ogromne odległości. Dla długo żyjących składników różnice między półkulami z czasem maleją, a charakterystyczny czas wymiany między półkulami jest rzędu około roku. Nie oznacza to jednak, że każda cząsteczka po roku ma dokładnie jednakowe prawdopodobieństwo znalezienia się w każdym miejscu.

Atmosfera posiada warstwy, cyrkulacje, sezony i bariery transportowe. Część gazów przechodzi do oceanu, gleby i organizmów. Para wodna kondensuje się w ciągu dni, dwutlenek węgla uczestniczy w obiegu węgla, tlen jest zużywany i odtwarzany, a azot także bierze udział w procesach biologicznych, choć jego główny rezerwuar atmosferyczny jest bardzo trwały.

Po dwóch tysiącach lat nie powinno się więc mówić o zachowaniu wszystkich **tych samych cząsteczek**. Cząsteczka tlenu z historycznego wydechu mogła wejść w reakcję, jej atomy mogły trafić do wody, skały albo organizmu, a później powrócić do atmosfery w innej cząsteczce. Bardziej odpornym twierdzeniem jest to, że w ziemskich obiegach nadal krążą ogromne liczby **atomów**, które znajdowały się kiedyś w ciałach i oddechach dawnych ludzi.

Rachunek idealnego mieszania nie śledzi chemii. Przypisuje cząsteczkom trwałą etykietę pochodzenia i losowo rozrzuca je w jednym wielkim zbiorniku. To świadoma idealizacja.

## Nie znamy ostatniego oddechu Cezara

Nie posiadamy pomiaru objętości ani składu powietrza wydychanego przez Cezara w chwili śmierci. Nie wiemy, jaka część pozostała wewnątrz pomieszczenia, została pochłonięta przez powierzchnie, rozpuszczona w wodzie albo weszła w reakcje. Nie potrafimy dziś oznaczyć konkretnego atomu i wykazać jego pochodzenia z jednego historycznego wydechu.

Nazwa „ostatni oddech Cezara” jest więc narracyjną etykietą dla dowolnej dawnej próbki gazu. Cezar działa na wyobraźnię, ponieważ znamy datę i dramat jego śmierci. Ten sam rachunek można przeprowadzić dla anonimowego człowieka żyjącego dwa tysiące lat temu, dla oddechu Kleopatry albo dla powietrza zamkniętego chwilowo w starożytnej świątyni.

Matematyka nie identyfikuje konkretnej osoby. Pokazuje, że przy astronomicznej liczbie cząsteczek mała historyczna próbka może po dostatecznym mieszaniu pozostawić niezerową oczekiwaną reprezentację w małej próbce współczesnej.

## Najciekawsza lekcja dotyczy nie Cezara, ale prawdopodobieństwa

Opowieść jest cenna właśnie dlatego, że łatwo popełnić w niej subtelny błąd.

Gdy słyszymy, że oczekiwana liczba cząsteczek wynosi jeden, umysł zamienia wartość oczekiwaną w pewny obiekt. Tymczasem średnia jednego trafienia może powstać z wielu prób bez trafienia, wielu z jednym oraz części z dwoma, trzema lub większą liczbą.

Ten sam błąd pojawia się w finansach, medycynie, epidemiologii i analizie ryzyka. Oczekiwana strata nie mówi, jaka strata wydarzy się jutro. Średnia liczba awarii nie gwarantuje jednej awarii w każdym okresie. Prawdopodobieństwo 75% nie oznacza, że zdarzenie jest „w trzech czwartych prawdziwe”.

Wartość oczekiwana opisuje środek rozkładu długiej serii możliwych realizacji. Pojedyncza realizacja nadal pozostaje losowa.

Dlatego poprawna puenta brzmi mniej magicznie, ale jest intelektualnie ciekawsza:

> **W idealnym modelu istnieje duża szansa, że twój oddech zawiera cząsteczkę z określonego dawnego oddechu. Jeżeli jej nie zawiera, model nie został obalony.**

Ziarnistość materii łączy nas z przeszłością, ale nie wydaje certyfikatów pochodzenia dla każdego wdechu.

Być może oddychasz Cezarem.

Matematyka mówi, że jest to prawdopodobne.

Nie mówi, że może ci wskazać który atom.

## Źródła i materiały

- [Podcast, od którego rozpoczęło się śledztwo](https://youtu.be/qoS5NDf3Xfk?is=zpju57p_iIk2Vtz8)
- [NIST: dokładna wartość stałej Avogadra](https://physics.nist.gov/cgi-bin/cuu/Value?na)
- [NIST: mol i redefinicja jednostek SI](https://www.nist.gov/si-redefinition/meet-constants)
- [Trenberth i Smith, „The Mass of the Atmosphere: A Constraint on Global Analyses”](https://journals.ametsoc.org/view/journals/clim/18/6/jcli-3299.1.xml)
- [Geller i in., troposferyczny SF₆ i czas wymiany między półkulami](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/97GL00813)
- [NOAA Global Monitoring Laboratory: pomiary długo żyjących gazów atmosferycznych](https://gml.noaa.gov/ccgg/)

<div class="lab-archive"><strong>Granica modelu:</strong> wartości λ≈1,42 i P≥1≈75,7% wynikają z półlitrowej próbki źródłowej i półlitrowego wdechu przy założeniu gazu doskonałego, idealnego globalnego mieszania oraz trwałych etykiet cząsteczek. Nie są empirycznym pomiarem ostatniego oddechu Cezara. Chemia, obiegi biogeochemiczne, niejednorodność atmosfery i nieznane parametry historyczne ograniczają dosłowną interpretację.</div>
