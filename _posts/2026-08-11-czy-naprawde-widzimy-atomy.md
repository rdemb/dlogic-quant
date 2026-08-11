---
layout: labpost
title: "Czy naprawdę widzimy atomy? Każdy obraz jest odpowiedzią aparatury"
description: "STM, AFM, promienie X i mikroskopy gazów kwantowych nie pokazują atomu w ten sam sposób. Każda technika mierzy inną interakcję i zamienia ją w obraz."
dek: "Naukowy obraz nie jest przezroczystym oknem na rzeczywistość. Jest końcem kontrolowanego łańcucha: obiekt, oddziaływanie, sygnał, rekonstrukcja i dopiero interpretacja."
date: 2026-08-11 17:10:00 +0200
category: luzne
tags: [odkrywanie-niewidzialnego, fizyka, atom, mikroskopia, pomiar]
eyebrow: "Odkrywanie niewidzialnego #03"
readingTime: 16
section_url: /odkrywanie-niewidzialnego/
section_label: Odkrywanie niewidzialnego
cover_brand: "FIZYKA · GRANICE INTUICJI #03"
cover_title: "OBRAZ NIE JEST OBIEKTEM"
cover_subtitle: "FOTON · PRĄD TUNELOWY · SIŁA · REKONSTRUKCJA"
cover_kind: loose
---
<div class="article-status"><span class="primary">ESEJ ŹRÓDŁOWY</span><span>MIKROSKOPIA</span><span>FILOZOFIA POMIARU</span><span>INVERSE PROBLEM</span></div>

W podręcznikach można znaleźć kolorowe kule ustawione w regularnej sieci, a w komunikatach prasowych obrazy opisane jako „pierwsze zdjęcie atomów”. Widz natychmiast przenosi na nie intuicję z fotografii: aparat zebrał światło odbite od małych obiektów, a ekran pokazuje po prostu ich wygląd w ogromnym powiększeniu.

W większości przypadków nic takiego się nie wydarzyło.

Promienie X nie tworzą klasycznego zdjęcia atomów w krysztale. Skaningowy mikroskop tunelowy nie mierzy twardej powierzchni złożonej z kulek. Mikroskop sił atomowych rejestruje oddziaływanie sondy z próbką, a obraz pojedynczego atomu wykonany światłem widzialnym jest zwykle plamką dyfrakcyjną wielokrotnie większą od samego atomu.

Nie oznacza to, że obrazy są fikcją albo artystyczną interpretacją. Są wynikiem eksperymentów, których relacja z badaną strukturą została opisana, skalibrowana i przetestowana. Trzeba jednak znać **kontrakt pomiarowy** każdej techniki: co oddziałuje z próbką, jaki sygnał powstaje, które przekształcenia wykonuje aparatura i jaki model pozwala przejść od sygnału do obrazu.

Najważniejsze pytanie nie brzmi więc wyłącznie: czy widzimy atom?

Brzmi:

> **Którą właściwość atomu lub układu atomowego przekształciliśmy w piksele - i jakie założenia znajdują się pomiędzy obiektem a obrazem?**

## Wykryć nie znaczy rozdzielić

Zwykła optyka ma ograniczoną zdolność rozróżniania drobnych szczegółów. Dla światła widzialnego granica dyfrakcyjna typowego mikroskopu znajduje się w skali setek nanometrów, podczas gdy charakterystyczny rozmiar atomu wynosi około dziesiątej części nanometra. Różnica sięga tysięcy razy.

Z tego często wyciąga się zbyt szeroki wniosek, że światłem widzialnym nie można zobaczyć pojedynczego atomu. Można go wykryć i zlokalizować, jeżeli zostanie uwięziony, pobudzony i wyemituje wystarczająco dużo fotonów. Kamera zarejestruje wtedy jasną plamkę o rozmiarze wyznaczonym przez układ optyczny, nie rzeczywistą średnicę atomu.

To samo dzieje się nocą z odległą gwiazdą. Jej tarcza może być znacznie mniejsza od zdolności rozdzielczej oka, a mimo to widzimy światło, ponieważ detekcja źródła nie wymaga rozdzielenia jego powierzchni.

Mikroskopy gazów kwantowych potrafią wykrywać pojedyncze atomy w miejscach sieci optycznej z bardzo wysoką wiernością. Obraz mówi, które stanowisko jest zajęte, pozwala śledzić korelacje i dynamikę wielu ciał, lecz nie jest portretem wewnętrznej budowy atomu.

<figure>
<svg viewBox="0 0 1040 410" role="img" aria-labelledby="detect-title detect-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="detect-title">Detekcja atomu a rozdzielenie jego rozmiaru</title>
 <desc id="detect-desc">Maleńki atom emituje fotony, a układ optyczny rejestruje znacznie większą plamkę dyfrakcyjną, której środek pozwala zlokalizować atom.</desc>
 <defs><radialGradient id="spot"><stop offset="0" stop-color="var(--acc)" stop-opacity=".95"/><stop offset="1" stop-color="var(--acc)" stop-opacity="0"/></radialGradient><marker id="img-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="var(--mut)"/></marker></defs>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <circle cx="176" cy="205" r="7" fill="var(--dn)"/><circle cx="176" cy="205" r="46" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="7 7"/>
 <text x="176" y="286" text-anchor="middle" font-size="17" fill="var(--ink)">POJEDYNCZY ATOM</text><text x="176" y="312" text-anchor="middle" font-size="13" fill="var(--mut)">rozmiar ~0,1 nm</text>
 <path d="M254 205 H390" stroke="var(--mut)" stroke-width="3" marker-end="url(#img-arrow)"/>
 <rect x="416" y="110" width="168" height="190" rx="16" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <path d="M458 150 L542 260 M542 150 L458 260" stroke="var(--acc)" stroke-width="4" opacity=".65"/>
 <text x="500" y="334" text-anchor="middle" font-size="17" fill="var(--ink)">UKŁAD OPTYCZNY</text>
 <path d="M610 205 H706" stroke="var(--mut)" stroke-width="3" marker-end="url(#img-arrow)"/>
 <circle cx="832" cy="205" r="116" fill="url(#spot)"/>
 <circle cx="832" cy="205" r="5" fill="var(--ink)"/>
 <text x="832" y="346" text-anchor="middle" font-size="17" fill="var(--ink)">PLAMKA NA DETEKTORZE</text><text x="832" y="372" text-anchor="middle" font-size="13" fill="var(--mut)">pozycja tak · kształt atomu nie</text>
 </g>
</svg>
<figcaption>Pojedynczy atom może być widoczny jako źródło światła, choć jego rzeczywisty rozmiar pozostaje znacznie poniżej rozdzielczości obrazu.</figcaption>
</figure>

## Promienie X pokazują wzór, z którego odtwarzamy strukturę

Długość fali promieniowania rentgenowskiego jest porównywalna z odległościami między atomami w kryształach, dlatego fale rozpraszane na regularnej strukturze tworzą wzór dyfrakcyjny. Detektor rejestruje układ plamek i ich intensywności. Nie widzi jednak pojedynczych kulek ułożonych w sieci.

Aby przejść od dyfrakcji do mapy gęstości elektronowej, trzeba rozwiązać problem odwrotny. Intensywności dostarczają informacji o amplitudach składowych Fouriera, ale fazy nie są bezpośrednio rejestrowane. Krystalografowie korzystają więc z symetrii, metod matematycznych, dodatkowych danych i modeli chemicznych, aby zrekonstruować strukturę zgodną z pomiarem.

To nadal może dać niezwykle dokładny wynik. Pozycje atomów w krysztale można wyznaczać z dokładnością znacznie lepszą niż długość fali użytego promieniowania, ponieważ precyzja estymacji parametru nie jest tym samym co optyczna rozdzielczość dwóch punktów. Obraz pozostaje jednak rekonstrukcją gęstości rozpraszającej, a model atomowy jest interpretacją tej mapy.

Im słabsze dane, większy nieporządek, ruch termiczny albo niejednorodność próbki, tym większą rolę odgrywa model i tym ostrożniej trzeba mówić o szczegółach.

## STM nie dotyka atomów. Mierzy tunelowanie

Skaningowy mikroskop tunelowy wykorzystuje ostrą, przewodzącą końcówkę umieszczoną bardzo blisko powierzchni. Po przyłożeniu napięcia elektrony mogą tunelować przez barierę próżniową, tworząc prąd niezwykle czuły na odległość końcówki od próbki.

Układ sprzężenia zwrotnego może przesuwać końcówkę tak, aby prąd pozostał stały, a zapis ruchu tworzy mapę powierzchni. Łatwo nazwać ją topografią atomową, lecz teoria STM pokazuje, że prąd zależy także od lokalnej gęstości stanów elektronowych, napięcia, struktury końcówki i właściwości próbki.

Dwa obrazy tej samej powierzchni wykonane przy różnych napięciach mogą wyglądać inaczej nie dlatego, że atomy zmieniły położenie, lecz dlatego, że instrument stał się czuły na inne stany elektronowe. Jasny punkt nie zawsze oznacza fizycznie najwyższy atom; może oznaczać region zwiększonej dostępności stanów dla tunelujących elektronów.

To nie jest wada STM. Właśnie dzięki tej zależności mikroskop pozwala badać strukturę elektronową z rozdzielczością atomową. Problem pojawia się dopiero wtedy, gdy wynik nazwiemy zwykłą fotografią powierzchni i zgubimy informację o tym, co naprawdę steruje kontrastem.

## AFM zmienia prąd na siłę

Mikroskop sił atomowych przesuwa nad próbką ostre zakończenie umieszczone na elastycznej dźwigni. Oddziaływania między końcówką i powierzchnią zmieniają ugięcie, częstotliwość albo amplitudę drgań. Z tych zmian rekonstruuje się mapę sił lub parametrów z nimi związanych.

AFM może badać również materiały nieprzewodzące, dlatego rozszerzył zakres dostępny dla mikroskopii skaningowej. W najbardziej precyzyjnych konfiguracjach kontrast wewnątrz cząsteczki bywa spektakularny, ale nadal zależy od zakończenia sondy, odległości, trybu pracy i modelu oddziaływania.

Sonda nie jest przezroczystym okiem. Jest aktywną częścią eksperymentu.

## Obraz naukowy jest łańcuchem przyczynowym

Wartość naukowego obrazu nie polega na braku przetwarzania. Polega na tym, że przetwarzanie jest opisane, testowalne i może zostać odtworzone.

<figure>
<svg viewBox="0 0 1080 360" role="img" aria-labelledby="pipeline-title pipeline-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="pipeline-title">Łańcuch tworzenia obrazu naukowego</title>
 <desc id="pipeline-desc">Badany układ oddziałuje z sondą, powstaje sygnał, detektor zapisuje dane, algorytm rekonstruuje obraz, a człowiek interpretuje wynik.</desc>
 <defs><marker id="pipe-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="var(--acc)"/></marker></defs>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
 <rect x="32" y="112" width="160" height="92" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="244" y="112" width="160" height="92" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="456" y="112" width="160" height="92" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="668" y="112" width="160" height="92" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
 <rect x="880" y="112" width="168" height="92" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
 <path d="M192 158 H238 M404 158 H450 M616 158 H662 M828 158 H874" stroke="var(--acc)" stroke-width="3" marker-end="url(#pipe-arrow)"/>
 <text x="112" y="150" text-anchor="middle" font-size="17" fill="var(--ink)">OBIEKT</text><text x="112" y="177" text-anchor="middle" font-size="13" fill="var(--mut)">atom / kryształ</text>
 <text x="324" y="150" text-anchor="middle" font-size="17" fill="var(--ink)">INTERAKCJA</text><text x="324" y="177" text-anchor="middle" font-size="13" fill="var(--mut)">foton · prąd · siła</text>
 <text x="536" y="150" text-anchor="middle" font-size="17" fill="var(--ink)">SYGNAŁ</text><text x="536" y="177" text-anchor="middle" font-size="13" fill="var(--mut)">liczby z detektora</text>
 <text x="748" y="150" text-anchor="middle" font-size="17" fill="var(--ink)">REKONSTRUKCJA</text><text x="748" y="177" text-anchor="middle" font-size="13" fill="var(--mut)">filtr · model · algorytm</text>
 <text x="964" y="150" text-anchor="middle" font-size="17" fill="var(--acc)">OBRAZ</text><text x="964" y="177" text-anchor="middle" font-size="13" fill="var(--mut)">twierdzenie wizualne</text>
 <text x="540" y="274" text-anchor="middle" font-size="18" fill="var(--ink)">Wiarygodność zależy od całego łańcucha, nie od atrakcyjności ostatniego kadru.</text>
 </g>
</svg>
<figcaption>Każdy etap posiada własne założenia, szumy, kalibrację i zakres ważności. Kontrolowany łańcuch przekształceń czyni obraz dowodem.</figcaption>
</figure>

Dla dyfrakcji rentgenowskiej interakcją jest rozpraszanie fali, sygnałem - intensywności refleksów, a rekonstrukcją - rozwiązanie problemu fazowego i budowa mapy gęstości elektronowej. Dla STM interakcją jest tunelowanie, dla AFM - siła, a dla fluorescencyjnego obrazu pojedynczych atomów - emisja i rejestracja wielu fotonów.

Wszystkie te techniki mogą być poprawne, choć pokazują odmienne aspekty tego samego układu. Konflikt pojawia się dopiero wtedy, gdy zapominamy o ich kontraktach i uznajemy każdy piksel za bezpośredni kawałek rzeczywistości.

## Czy kolory na obrazie atomowym są prawdziwe?

Wiele obrazów mikroskopowych wykorzystuje sztuczne skale barw, ponieważ detektor nie rejestruje światła widzialnego w sposób odpowiadający kolorowi prezentacji. Barwa może oznaczać wysokość, prąd, siłę, fazę, energię albo intensywność. Czerwony atom nie musi być czerwony, a niebieska dolina nie musi odbijać niebieskiego światła.

Fałszywy kolor nie jest fałszywą informacją, jeśli legenda precyzyjnie mówi, co koduje. Może nawet ujawniać różnice, których skala szarości nie pokazałaby czytelnie. Nieuczciwość zaczyna się wtedy, gdy estetyka ukrywa skalę, filtrację, saturację albo arbitralny próg.

Profesjonalny obraz naukowy powinien więc posiadać coś w rodzaju metadanych twierdzenia:

- jaka wielkość została zmierzona,
- w jakich jednostkach,
- przy jakiej rozdzielczości,
- z jakim modelem rekonstrukcji,
- po jakim filtrowaniu,
- z jaką niepewnością,
- oraz które cechy obrazu są stabilne przy zmianie parametrów analizy.

## Najbardziej bezpośredni obraz nadal wymaga teorii

Można odnieść wrażenie, że im mniej algorytmów i równań pomiędzy próbką a ekranem, tym bardziej „realny” obraz. Tymczasem nawet widzenie gołym okiem jest procesem rekonstrukcji: światło oddziałuje z obiektem, soczewka oka tworzy obraz, fotoreceptory zamieniają fotony na sygnał, a mózg buduje stabilną scenę z niepełnych i dynamicznych danych.

Nauka nie eliminuje pośrednictwa. Ujawnia je i podporządkowuje testom.

Dlatego obraz atomu nie jest mniej prawdziwy tylko dlatego, że powstał z prądu tunelowego, siły albo wzoru dyfrakcyjnego. Jest prawdziwy w takim zakresie, w jakim znamy relację między zmierzonym sygnałem i strukturą, potrafimy odtworzyć wynik oraz przewidzieć, jak zmieni się on po kontrolowanej zmianie warunków.

Najdojrzalsze pytanie nie brzmi więc: „czy to naprawdę atom?”.

Brzmi:

> **Jakie własności badanego układu muszą istnieć, aby aparatura w tych warunkach wytworzyła właśnie taki sygnał?**

W tym sensie nie widzimy atomów tak, jak widzimy jabłko na stole.

Robimy coś bardziej wymagającego: zmuszamy niewidzialny układ do pozostawienia śladu, a następnie sprawdzamy, czy model tłumaczący ten ślad przetrwa kolejne eksperymenty.

## Źródła i materiały

- [Podcast, od którego rozpoczęło się śledztwo](https://youtu.be/qoS5NDf3Xfk?is=zpju57p_iIk2Vtz8)
- [Binnig, Rohrer, Gerber i Weibel: pierwsze obrazy STM w skali atomowej](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.49.57)
- [Tersoff i Hamann: teoria obrazu skaningowego mikroskopu tunelowego](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.31.805)
- [Binnig, Quate i Gerber: Atomic Force Microscope](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.56.930)
- [Bakr i in.: mikroskop gazu kwantowego wykrywający pojedyncze atomy](https://www.nature.com/articles/nature08482)
- [Cheuk i in.: obrazowanie pojedynczych atomów fermionowych](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.193001)
- [Nobel Prize: analiza struktur krystalicznych promieniami X](https://www.nobelprize.org/prizes/physics/1915/speedread/)
- [IUCr: metody i problemy analizy struktury kryształów](https://www.iucr.org/publ/50yearsofxraydiffraction/full-text/structure-analysis)

<div class="lab-archive"><strong>Granica twierdzenia:</strong> „widzenie atomu” może oznaczać detekcję pojedynczego atomu, rozdzielenie stanowisk atomowych, mapowanie lokalnej gęstości stanów, pomiar sił albo rekonstrukcję gęstości elektronowej. Żadna z tych metod nie jest zwykłym optycznym zdjęciem twardej kulki, ale każda może dostarczać rzetelnego dowodu w ramach jawnego kontraktu pomiarowego.</div>
