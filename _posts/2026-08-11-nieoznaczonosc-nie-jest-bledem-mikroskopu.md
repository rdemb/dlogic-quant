---
layout: labpost
title: "Nieoznaczoność nie jest błędem mikroskopu"
description: "Zasada Heisenberga nie mówi jedynie, że pomiar potrąca elektron. Opisuje strukturę stanów kwantowych - i nie jest tym samym co twierdzenie Bella ani zakaz wszystkich zmiennych ukrytych."
dek: "Możemy zbudować lepszy instrument, ale nie przygotujemy stanu, w którym położenie i pęd mają jednocześnie dowolnie wąskie rozkłady. To ograniczenie teorii, nie jakość soczewki."
date: 2026-08-11 17:00:00 +0200
category: luzne
tags: [odkrywanie-niewidzialnego, fizyka, Heisenberg, mechanika-kwantowa, pomiar]
eyebrow: "Odkrywanie niewidzialnego #04"
readingTime: 18
section_url: /odkrywanie-niewidzialnego/
section_label: Odkrywanie niewidzialnego
cover_brand: "FIZYKA · GRANICE INTUICJI #04"
cover_title: "NIEPEWNOŚĆ MA STRUKTURĘ"
cover_subtitle: "STAN · POMIAR · KOMUTATOR · BELL"
cover_kind: loose
---
<div class="article-status"><span class="primary">ESEJ ŹRÓDŁOWY</span><span>MECHANIKA KWANTOWA</span><span>GRANICE POMIARU</span><span>HEISENBERG ≠ BELL</span></div>

Najbardziej znane wyjaśnienie zasady nieoznaczoności przedstawia mikroskop próbujący zlokalizować elektron. Aby zobaczyć coraz mniejszy obiekt, trzeba użyć promieniowania o coraz krótszej długości fali, a więc fotonów posiadających większy pęd. Foton zderza się z elektronem, zmienia jego ruch i niszczy informację, którą chcieliśmy uzyskać. Wniosek brzmi intuicyjnie: im dokładniej mierzymy położenie, tym bardziej zaburzamy pęd.

Ten obraz pochodzi z tradycji samego Heisenberga i nadal ma wartość pedagogiczną. Nie jest jednak pełnym znaczeniem zasady nieoznaczoności.

Gdyby problem polegał wyłącznie na potrącaniu elektronu przez niedoskonałą sondę, moglibyśmy marzyć o instrumencie delikatniejszym, szybszym albo inteligentniej zaprojektowanym. Mechanika kwantowa stawia ograniczenie wcześniej - już na etapie **przygotowania stanu**.

Możemy stworzyć stan, w którym wyniki pomiaru położenia są skupione bardzo wąsko. W tym samym stanie rozkład możliwych wyników pomiaru pędu musi być szeroki. Możemy przygotować niemal określony pęd, ale wtedy stan rozciąga się przestrzennie. Nie jest to opowieść o tym, że elektron zna obie wartości, a niezdarny obserwator nie potrafi ich odczytać bez szkody.

> **Nieoznaczoność opisuje wzajemną geometrię możliwych rozkładów wyników dla jednego stanu kwantowego.**

Pomiar dodaje kolejny problem - wpływ aparatury na układ - ale nie jest źródłem całego ograniczenia.

## Rozkład, nie pojedyncza pomyłka

W fizyce niepewność może oznaczać kilka różnych rzeczy. Termometr może być źle skalibrowany. Seria pomiarów może być zaszumiona. Parametr może być nieznany, choć w każdej chwili posiada jedną dokładną wartość. Zasada Heisenberga nie jest zwykłym przykładem żadnego z tych przypadków.

Standardowe odchylenie położenia, oznaczane jako Δx, opisuje szerokość rozkładu wyników uzyskiwanych przy wielokrotnym przygotowaniu tego samego stanu i pomiarze położenia. Δp analogicznie opisuje rozrzut wyników pomiaru pędu. Dla położenia i pędu zachodzi relacja:

\[
\Delta x\,\Delta p \geq \frac{\hbar}{2}.
\]

W bardziej ogólnej postaci nierówność Robertsona wiąże nieoznaczoności dwóch obserwabli z wartością oczekiwaną ich komutatora. Jeżeli operatory nie komutują, istnieją stany, dla których nie można dowolnie zmniejszyć obu rozrzutów jednocześnie.

To ważne: nierówność nie mówi, że pojedynczy wynik pomiaru musi być „niedokładny” o określoną wartość. Detektor może zarejestrować położenie z bardzo wysoką precyzją. Ograniczenie dotyczy statystyki wyników dwóch niekomutujących wielkości w przygotowanym stanie.

## Fala, która nie potrafi być jednocześnie wąska w dwóch przestrzeniach

Relację można zrozumieć bez wyobrażania sobie zderzenia z fotonem. Funkcja falowa w przestrzeni położeń i amplituda w przestrzeni pędów są powiązane transformacją Fouriera.

Pojedyncza fala sinusoidalna posiada dokładnie określoną długość fali, a więc określony pęd, ale rozciąga się przez całą przestrzeń. Aby zbudować pakiet zlokalizowany w małym obszarze, trzeba złożyć wiele fal o różnych długościach. Im węższy pakiet tworzymy, tym szerszego zakresu składowych pędu potrzebujemy.

<figure>
<svg viewBox="0 0 1040 470" role="img" aria-labelledby="fourier-title fourier-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="fourier-title">Położenie i pęd jako pary Fouriera</title>
 <desc id="fourier-desc">Wąski pakiet w położeniu odpowiada szerokiemu rozkładowi pędu, a szeroki pakiet położenia odpowiada wąskiemu rozkładowi pędu.</desc>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <rect x="36" y="44" width="968" height="170" rx="18" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="36" y="256" width="968" height="170" rx="18" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <text x="92" y="80" font-size="18" fill="var(--ink)">STAN A</text><text x="92" y="292" font-size="18" fill="var(--ink)">STAN B</text>
 <line x1="170" y1="174" x2="500" y2="174" stroke="var(--mut)" stroke-width="2"/><line x1="612" y1="174" x2="942" y2="174" stroke="var(--mut)" stroke-width="2"/>
 <line x1="170" y1="386" x2="500" y2="386" stroke="var(--mut)" stroke-width="2"/><line x1="612" y1="386" x2="942" y2="386" stroke="var(--mut)" stroke-width="2"/>
 <path d="M170 174 C310 174 322 74 335 74 C348 74 360 174 500 174" fill="none" stroke="var(--acc)" stroke-width="5"/>
 <path d="M612 174 C676 174 710 116 777 104 C844 116 878 174 942 174" fill="none" stroke="var(--dn)" stroke-width="5"/>
 <path d="M170 386 C234 386 268 328 335 316 C402 328 436 386 500 386" fill="none" stroke="var(--acc)" stroke-width="5"/>
 <path d="M612 386 C752 386 764 286 777 286 C790 286 802 386 942 386" fill="none" stroke="var(--dn)" stroke-width="5"/>
 <text x="335" y="202" text-anchor="middle" font-size="14" fill="var(--mut)">wąskie Δx</text><text x="777" y="202" text-anchor="middle" font-size="14" fill="var(--mut)">szerokie Δp</text>
 <text x="335" y="414" text-anchor="middle" font-size="14" fill="var(--mut)">szerokie Δx</text><text x="777" y="414" text-anchor="middle" font-size="14" fill="var(--mut)">wąskie Δp</text>
 <text x="335" y="110" text-anchor="middle" font-size="13" fill="var(--acc)">POŁOŻENIE</text><text x="777" y="110" text-anchor="middle" font-size="13" fill="var(--dn)">PĘD</text>
 <text x="335" y="322" text-anchor="middle" font-size="13" fill="var(--acc)">POŁOŻENIE</text><text x="777" y="322" text-anchor="middle" font-size="13" fill="var(--dn)">PĘD</text>
 </g>
</svg>
<figcaption>Diagram przedstawia jakościową relację Fouriera. Nie jest wykresem konkretnego eksperymentu ani dowodem samym w sobie.</figcaption>
</figure>

Nieoznaczoność nie jest więc arbitralnym zakazem nałożonym na pomiar. Wynika z matematycznej struktury przestrzeni stanów i sposobu reprezentowania par wielkości sprzężonych.

## Mikroskop Heisenberga dotyczy innego pytania

Heurystyczny mikroskop próbuje opisać relację między błędem pomiaru położenia i zaburzeniem pędu wywołanym przez procedurę pomiarową. Przez dziesięciolecia często zapisywano ją w formie podobnej do relacji przygotowania:

\[
\varepsilon(x)\,\eta(p) \gtrsim \frac{\hbar}{2},
\]

gdzie ε oznacza błąd pomiaru, a η - zaburzenie drugiej wielkości.

Problem polega na tym, że prosta iloczynowa postać nie jest uniwersalnie prawdziwa dla wszystkich możliwych pomiarów kwantowych. Masanao Ozawa wyprowadził ogólniejszą relację, w której oprócz błędu i zaburzenia pojawiają się także początkowe nieoznaczoności stanu:

\[
\varepsilon(A)\eta(B)+\varepsilon(A)\Delta B+\Delta A\eta(B)
\geq \frac{1}{2}|\langle[A,B]\rangle|.
\]

Nie oznacza to obalenia zasady Heisenberga. Oznacza doprecyzowanie, że trzeba rozdzielić dwie klasy twierdzeń:

1. **relacje przygotowania** - ograniczające rozrzuty obserwabli w stanie,
2. **relacje błędu i zaburzenia** - opisujące konkretną procedurę pomiarową.

Eksperyment może zostać zaprojektowany tak, aby zaburzenie mierzone według określonej definicji było mniejsze, niż sugerował prosty obraz mikroskopu. Nadal nie pozwala to przygotować stanu z dowolnie małymi Δx i Δp.

<figure>
<svg viewBox="0 0 1040 390" role="img" aria-labelledby="layers-title layers-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="layers-title">Trzy warstwy problemu nieoznaczoności</title>
 <desc id="layers-desc">Przygotowanie stanu, oddziaływanie pomiarowe i filozoficzna interpretacja są odrębnymi poziomami, których nie należy mieszać.</desc>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <rect x="80" y="48" width="880" height="82" rx="16" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
 <rect x="118" y="154" width="804" height="82" rx="16" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
 <rect x="156" y="260" width="728" height="82" rx="16" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
 <text x="520" y="80" text-anchor="middle" font-size="20" fill="var(--acc)">PRZYGOTOWANIE STANU</text><text x="520" y="108" text-anchor="middle" font-size="14" fill="var(--mut)">ΔA i ΔB · Robertson · struktura operatorów</text>
 <text x="520" y="186" text-anchor="middle" font-size="20" fill="var(--up)">PROCEDURA POMIAROWA</text><text x="520" y="214" text-anchor="middle" font-size="14" fill="var(--mut)">błąd ε · zaburzenie η · relacje Ozawy</text>
 <text x="520" y="292" text-anchor="middle" font-size="20" fill="var(--dn)">INTERPRETACJA ONTOLOGICZNA</text><text x="520" y="320" text-anchor="middle" font-size="14" fill="var(--mut)">co istnieje przed pomiarem? różne interpretacje</text>
 </g>
</svg>
<figcaption>Wynik matematyczny, zachowanie aparatury i filozofia teorii są powiązane, ale nie są tym samym twierdzeniem.</figcaption>
</figure>

## Pomiar nie wymaga świadomego człowieka

W popularnych opowieściach mechanika kwantowa bywa przedstawiana tak, jakby elektron czekał na ludzkie spojrzenie, a świadomość obserwatora fizycznie tworzyła wynik. Standardowy formalizm eksperymentalny nie wymaga takiego założenia.

Pomiar jest procesem fizycznego sprzężenia układu z aparaturą, powstania korelacji i utrwalenia wyniku w stopniach swobody, które mogą zostać później odczytane. Dekohorencja opisuje, jak kontakt ze środowiskiem tłumi obserwowalną interferencję pomiędzy składnikami superpozycji w określonej bazie.

Interpretacje mechaniki kwantowej różnią się w odpowiedzi na pytanie, co dokładnie oznacza pojedynczy wynik oraz czy i kiedy zachodzi rzeczywisty kolaps. Nie należy jednak zamieniać tego sporu w twierdzenie, że bez ludzkiego umysłu detektor nie rejestruje zdarzeń. Aparatura może zakończyć pomiar, zapisać dane i zostać odczytana wiele godzin później.

## Heisenberg nie obalił wszystkich zmiennych ukrytych

Kolejne popularne uproszczenie brzmi: skoro położenie i pęd są nieoznaczone, w przyrodzie nie mogą istnieć żadne głębsze zmienne określające wyniki. Takie zdanie wykracza poza samą nierówność Heisenberga.

Relacja nieoznaczoności ogranicza statystyki obserwabli reprezentowanych przez niekomutujące operatory. Sama nie dowodzi, że niemożliwa jest każda teoria zmiennych ukrytych. Mechanika Bohma jest przykładem teorii posiadającej dodatkowe zmienne, ale jest jawnie nielokalna.

Innego rodzaju ograniczenie wprowadza twierdzenie Bella. Pokazuje ono, że żadna teoria spełniająca określone założenia lokalności i niezależności ustawień nie może odtworzyć wszystkich korelacji przewidywanych przez mechanikę kwantową. Eksperymenty naruszające nierówności Bella, w tym testy zamykające główne luki doświadczalne, wspierają kwantowe przewidywania i wykluczają szeroką klasę **lokalnych** modeli zmiennych ukrytych.

<figure>
<svg viewBox="0 0 1040 380" role="img" aria-labelledby="bell-title bell-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="bell-title">Heisenberg i Bell odpowiadają na różne pytania</title>
 <desc id="bell-desc">Heisenberg ogranicza wspólne rozrzuty obserwabli w stanie. Bell ogranicza lokalne modele zmiennych ukrytych na podstawie korelacji między odległymi pomiarami.</desc>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <rect x="52" y="54" width="430" height="268" rx="20" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
 <rect x="558" y="54" width="430" height="268" rx="20" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
 <text x="267" y="94" text-anchor="middle" font-size="22" fill="var(--acc)">HEISENBERG / ROBERTSON</text>
 <text x="773" y="94" text-anchor="middle" font-size="22" fill="var(--dn)">BELL</text>
 <text x="267" y="142" text-anchor="middle" font-size="16" fill="var(--ink)">jeden stan</text><text x="267" y="172" text-anchor="middle" font-size="16" fill="var(--ink)">dwie niekomutujące obserwable</text><text x="267" y="202" text-anchor="middle" font-size="16" fill="var(--ink)">ograniczenie rozrzutów</text>
 <text x="773" y="142" text-anchor="middle" font-size="16" fill="var(--ink)">dwa odległe układy</text><text x="773" y="172" text-anchor="middle" font-size="16" fill="var(--ink)">alternatywne ustawienia</text><text x="773" y="202" text-anchor="middle" font-size="16" fill="var(--ink)">ograniczenie lokalnych modeli</text>
 <text x="267" y="272" text-anchor="middle" font-size="14" fill="var(--mut)">nie jest twierdzeniem o wszystkich ontologiach</text>
 <text x="773" y="272" text-anchor="middle" font-size="14" fill="var(--mut)">naruszenie nierówności w eksperymencie</text>
 </g>
</svg>
<figcaption>Połączenie obu zagadnień bez rozróżnienia prowadzi do twierdzeń mocniejszych, niż uzasadnia którykolwiek wynik osobno.</figcaption>
</figure>

Nieoznaczoność i nielokalność kwantowa należą do tej samej teorii, ale odpowiadają na różne pytania.

## Granica wiedzy - ale nie kapitulacja poznawcza

Zasada Heisenberga bywa przedstawiana jako ostateczny dowód, że świata nie można poznać. W rzeczywistości jest jednym z najbardziej precyzyjnych przykładów tego, jak nauka zamienia ogólne słowo „niemożliwe” w matematyczną, testowalną granicę.

Nie mówi: niczego nie wiemy.

Mówi: dla danego stanu rozrzuty wyników dwóch wielkości są związane określoną nierównością. Możemy obliczyć minimalny iloczyn, przygotować stany zbliżające się do granicy, badać relacje błędu i zaburzenia oraz testować przewidywania na fotonach, neutronach, atomach i układach makroskopowych.

Nie jest to porażka pomiaru. Jest to odkrycie struktury, której klasyczna intuicja nie przewidywała.

Największym błędem byłoby sprowadzenie tej struktury do zdania: „kiedy patrzymy, przeszkadzamy”. Każdy pomiar jest interakcją, ale nie każda nieoznaczoność powstaje podczas pomiaru.

Instrument może być doskonały.

Stan nadal nie pozwoli jednocześnie skupić wszystkich niekomutujących wielkości w dowolnie wąskich rozkładach.

Nie dlatego, że natura ukrywa przed nami gotową kartkę z liczbami.

Dlatego, że kwantowy stan nie jest kartką, na której wszystkie klasyczne wartości zostały wcześniej zapisane.

## Źródła i materiały

- [Podcast, od którego rozpoczęło się śledztwo](https://youtu.be/qoS5NDf3Xfk?is=zpju57p_iIk2Vtz8)
- [H. P. Robertson, „The Uncertainty Principle”, Physical Review, 1929](https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163)
- [Masanao Ozawa, „Universally valid reformulation of the Heisenberg uncertainty principle”, Physical Review A](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.67.042105)
- [Nobel Prize: Werner Heisenberg i stworzenie mechaniki kwantowej](https://www.nobelprize.org/prizes/physics/1932/summary/)
- [John S. Bell, „On the Einstein Podolsky Rosen paradox”, CERN](https://cds.cern.ch/record/111654/files/vol1p195-200_001.pdf)
- [Hensen i in., loophole-free Bell inequality violation, Nature](https://www.nature.com/articles/nature15759)
- [Giustina i in., significant-loophole-free Bell test, Physical Review Letters](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.115.250401)

<div class="lab-archive"><strong>Granica twierdzenia:</strong> relacja Robertsona opisuje rozrzuty obserwabli w przygotowanym stanie. Nie jest identyczna z prostą relacją błędu pomiarowego i zaburzenia ani z twierdzeniem Bella. Sama zasada nieoznaczoności nie wyklucza każdej możliwej teorii zmiennych ukrytych; eksperymenty Bella ograniczają przede wszystkim modele lokalne spełniające określone założenia.</div>
