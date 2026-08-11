---
layout: labpost
title: "Pierwszy model zaczyna się przed modelem"
description: "Dlaczego poważny research alfy powinien najpierw zamrozić informację dostępną w chwili decyzji, target, koszty, baseline’y i budżet prób."
dek: "Najłatwiej otworzyć notebook i trenować. Znacznie trudniej najpierw zdefiniować warunki, w których atrakcyjny wynik będzie miał prawo cokolwiek znaczyć."
date: 2026-08-11 09:00:00 +0200
category: research
eyebrow: "D-LOGIC Research Note #02"
readingTime: 9
section_url: /research/
section_label: Research
cover_brand: "D-LOGIC RESEARCH NOTE #02"
cover_title: "INFORMACJA PRZED MODELEM"
cover_subtitle: "DATA · TIME · TARGET · COSTS · BASELINES · HOLDOUT"
cover_kind: research
---
<div class="article-status"><span class="primary">RESEARCH DESIGN</span><span>STATUS: UNTESTED</span><span>OUTER HOLDOUT: SEALED</span><span>MODEL PROMOTION: FORBIDDEN</span><span>LIVE: NOT AUTHORIZED</span></div>

Najbardziej kuszący moment w badaniu strategii pojawia się wtedy, gdy dane są już w zasięgu ręki. Można otworzyć notebook, wygenerować dziesiątki cech, uruchomić kilka modeli, przesunąć horyzont, zmienić próg i po kilku godzinach zobaczyć pierwszą krzywą wyników.

Właśnie wtedy research może zostać statystycznie zużyty, zanim formalnie się rozpocznie.

Każdy obejrzany rezultat wpływa na następną decyzję. Jeżeli po słabym wyniku zmienimy feature, po niestabilnym miesiącu przesuniemy sesję, a po wysokich kosztach wybierzemy inny instrument, test przestaje być niezależną oceną wcześniej postawionej hipotezy. Staje się częścią procesu poszukiwania - nawet jeśli w kodzie nadal nazywa się `validation` albo `test`.

Dlatego pierwszy poważny pakiet researchu alfy w obecnym D-LOGIC został zaprojektowany tak, aby **nie zaczynał się od treningu modelu**. Jego zadaniem jest zamrożenie podłoża, na którym późniejszy eksperyment będzie mógł zostać przeprowadzony bez cichego dopisywania reguł po zobaczeniu wyniku.

To nie jest jeszcze informacja, że taki model działa. Jest to opis metodologii, która ma dopiero stworzyć prawo do wykonania pierwszego prerejestrowanego eksperymentu.

## Najpierw trzeba udowodnić, co system mógł wiedzieć

W backteście wszystkie obserwacje leżą w jednym pliku. Dla komputera kolumna z dzisiejszego poranka i kolumna z jutrzejszego zamknięcia są równie łatwo dostępne, dlatego sama obecność timestampu nie chroni przed wykorzystaniem przyszłości.

Istotne jest nie tylko to, kiedy coś wydarzyło się na rynku, lecz również kiedy informacja stała się dostępna dla konkretnego procesu decyzyjnego.

Notowanie może mieć czas giełdowy, czas odebrania przez dostawcę, czas zapisania na dysku i czas zakończenia transformacji. Wartość makro może zostać opublikowana o określonej godzinie, a później zrewidowana. Skład indeksu widoczny dzisiaj nie musi odpowiadać składowi z badanego dnia. Świeca posiada ostateczne high i low dopiero po zamknięciu, chociaż kod potrafi wczytać te wartości dla całej historii jednym poleceniem.

Dlatego podstawową zasadą jest:

> **Cecha może wejść do modelu tylko wtedy, gdy da się wykazać, że była rzeczywiście dostępna przed decyzją, w jakości i wersji odpowiadającej tamtemu momentowi.**

Nie publikuję dokładnego rejestru informacji, reguł dostępności ani prywatnych definicji cech. Publicznie istotny jest mechanizm: czas zdarzenia i czas poznania zdarzenia nie są tym samym.

<figure>
<svg viewBox="0 0 980 430" role="img" aria-labelledby="freeze-title freeze-desc" xmlns="http://www.w3.org/2000/svg">
 <title id="freeze-title">Siedem bram przed pierwszym modelem</title>
 <desc id="freeze-desc">Dane, czas, target, koszty, baseline, podział i budżet prób muszą zostać zamrożone przed treningiem.</desc>
 <defs><marker id="a2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
 <path d="M72 213 H900" stroke="var(--mut)" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#a2)"/>
 <g font-family="-apple-system,Segoe UI,Roboto,sans-serif" text-anchor="middle">
 <rect x="34" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="166" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="298" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="430" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="562" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="694" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <rect x="826" y="108" width="116" height="112" rx="13" fill="var(--soft)" stroke="var(--acc)" stroke-width="2"/>
 <text x="92" y="145" font-size="15" font-weight="700" fill="var(--ink)">DANE</text><text x="92" y="173" font-size="12" fill="var(--mut)">provenance</text><text x="92" y="192" font-size="12" fill="var(--mut)">jakość</text>
 <text x="224" y="145" font-size="15" font-weight="700" fill="var(--ink)">CZAS</text><text x="224" y="173" font-size="12" fill="var(--mut)">available-at</text><text x="224" y="192" font-size="12" fill="var(--mut)">point-in-time</text>
 <text x="356" y="145" font-size="15" font-weight="700" fill="var(--ink)">TARGET</text><text x="356" y="173" font-size="12" fill="var(--mut)">wykonalny</text><text x="356" y="192" font-size="12" fill="var(--mut)">po decyzji</text>
 <text x="488" y="145" font-size="15" font-weight="700" fill="var(--ink)">KOSZTY</text><text x="488" y="173" font-size="12" fill="var(--mut)">spread</text><text x="488" y="192" font-size="12" fill="var(--mut)">slippage</text>
 <text x="620" y="145" font-size="15" font-weight="700" fill="var(--ink)">BASELINE</text><text x="620" y="173" font-size="12" fill="var(--mut)">prosty</text><text x="620" y="192" font-size="12" fill="var(--mut)">do pobicia</text>
 <text x="752" y="145" font-size="15" font-weight="700" fill="var(--ink)">PODZIAŁ</text><text x="752" y="173" font-size="12" fill="var(--mut)">purge</text><text x="752" y="192" font-size="12" fill="var(--mut)">holdout</text>
 <text x="884" y="145" font-size="15" font-weight="700" fill="var(--ink)">BUDŻET</text><text x="884" y="173" font-size="12" fill="var(--mut)">power</text><text x="884" y="192" font-size="12" fill="var(--mut)">liczba prób</text>
 </g>
 <rect x="330" y="300" width="320" height="76" rx="15" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
 <text x="490" y="333" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="20" font-weight="700" fill="var(--ink)">DOPIERO TERAZ: MODEL</text>
 <text x="490" y="359" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">złożoność jest ostatnią decyzją, nie pierwszą</text>
 <path d="M490 220 V292" stroke="var(--dn)" stroke-width="3" marker-end="url(#a2)"/>
</svg>
<figcaption>Każda brama ogranicza inną drogę, przez którą przyszła informacja, niewykonalny target albo data snooping mogłyby stworzyć pozorną przewagę.</figcaption>
</figure>

## Plik nie staje się zbiorem badawczym tylko dlatego, że istnieje

Przed budową modelu trzeba sporządzić inwentarz danych, który odpowiada na więcej pytań niż nazwa pliku i liczba wierszy. Potrzebne są źródło, wersja, zakres czasu, typ zdarzenia, precyzja, semantyka cen, polityka duplikatów, luki, reconnecty, rewizje, koszty oraz możliwość deterministycznego odtworzenia.

W D-LOGIC istnieją zbiory o bardzo różnym statusie: aktualne snapshoty metadanych, historyczne ticki i bary, duże archiwa zdarzeń kryptowalutowych, wcześniejsze dane badawcze, ledgery o znanych problemach oraz materiały syntetyczne. Ich obecność na dysku nie oznacza, że wolno je połączyć w jeden „duży dataset”.

Każdy podzbiór musi otrzymać własny werdykt jakości i dozwoloną rolę: development, validation, test, sealed holdout, forward albo forbidden. Jeżeli nie da się ustalić pochodzenia, czasu dostępności lub ceny wykonawczej, poprawnym statusem jest `DATA_REQUIRED` albo `INVALID_FOR_ALPHA`, a nie ciche założenie wypełniające lukę.

## Target musi opisywać wynik, który można było zrealizować

Najprostsza etykieta `UP/DOWN` wygląda neutralnie, ale może ukrywać najważniejszy problem. Cena może wzrosnąć od bieżącego mid do przyszłego mid, choć wejście wymagało zakupu po ask, a wyjście sprzedaży po bid. Przy małym ruchu kierunek będzie statystycznie poprawny, natomiast transakcja ekonomicznie ujemna.

Target powinien więc odpowiadać na pytanie bliższe rzeczywistej decyzji. Nie wystarczy przewidzieć, że rynek później znajdzie się wyżej; trzeba ustalić, czy ruch przekroczył koszty, w jakim horyzoncie, przy jakiej konwencji wejścia i wyjścia, czy po drodze aktywował barierę ryzyka oraz kiedy etykieta naprawdę dojrzała.

Dokładne targety, progi i reguły ścieżki pozostają częścią prywatnego programu badawczego. Publiczna zasada jest jednak jednoznaczna:

> **Statystycznie przewidywalny wynik, którego nie można przekształcić w wykonalną wartość netto, nie wystarcza do promocji modelu.**

## Koszty nie są przypisem pod wykresem

W słabym backteście koszty pojawiają się na końcu jako stała liczba odejmowana od każdej transakcji. W rzeczywistości spread zależy od instrumentu, sesji, zmienności i stanu płynności, poślizg rośnie wraz z agresywnością oraz rozmiarem, finansowanie zależy od horyzontu, a ograniczenia kontraktu mogą całkowicie zablokować realizację teoretycznie atrakcyjnego sygnału.

Dlatego model kosztów musi powstać przed wyborem hipotezy. W przeciwnym razie istnieje silna pokusa, aby po wyniku wybrać założenia, które pozwalają zachować atrakcyjną krzywą.

Nie chodzi o osiągnięcie absolutnej dokładności symulacji. Chodzi o uczciwe zaznaczenie niepewności i twarde zatrzymanie tam, gdzie kluczowa składowa kosztu pozostaje nieznana.

## Najpierw trzeba pokonać coś prostego

Złożony model ma naturalną przewagę prezentacyjną. Potrafi wytworzyć wykres ważności cech, rozbudowaną narrację i wiele parametrów, które można później interpretować. Nie oznacza to jednak, że wnosi więcej informacji niż prosta reguła sesyjna, ostatnia obserwacja, historyczna częstość klasy albo regularizowany model liniowy.

Dlatego baseline’y powinny zostać zamrożone przed modelem zaawansowanym. Każda kolejna warstwa złożoności musi raportować wartość przyrostową względem najsilniejszej sensownej alternatywy, a nie wyłącznie własny wynik bez punktu odniesienia.

D-LOGIC zakłada również pełnoprawny baseline `ABSTAIN / NO TRADE`. Model nie wygrywa tylko dlatego, że jego prognoza jest trochę lepsza od losowej, jeżeli po kosztach lepszą decyzją było niewykonanie transakcji.

## Holdout jest zasobem nieodnawialnym

Zewnętrzny holdout przypomina zapieczętowaną kopertę. Jego wartość wynika z tego, że nie wpływał na wybór hipotezy, danych, cech ani parametrów. Po otwarciu wynik staje się częścią wiedzy badacza i będzie oddziaływał na kolejne decyzje, nawet jeśli nikt nie skopiuje liczby bezpośrednio do kodu.

Dlatego końcowy holdout w projektowanym pakiecie ma pozostać zamknięty, a sam brak dostępu powinien otrzymać własny receipt. To nie przesada: system dowodowy musi potrafić wykazać nie tylko, co przeczytał, lecz czasem również czego **nie przeczytał**.

Warto myśleć o tym jako o kapitale statystycznym. Każda niezależna próba zużywa część zdolności do formułowania nowych twierdzeń. Jeżeli otwieramy wiele wariantów, horyzontów i modeli, rośnie prawdopodobieństwo, że najbardziej atrakcyjny wynik będzie przypadkiem.

## Budżet prób powstaje przed wynikami

Research nie powinien mieć nieograniczonego prawa do szukania. Przed treningiem trzeba oszacować rozmiar i efektywną niezależność próby, minimalną poprawę, którą da się wykryć, ekonomicznie istotny efekt oraz maksymalną liczbę rodzin hipotez.

Jeżeli danych jest zbyt mało, właściwym wynikiem może być `BLOCKED_INSUFFICIENT_POWER`. Jeżeli plan wymaga sprawdzenia zbyt wielu wariantów względem dostępnego budżetu, eksperyment powinien zostać ograniczony albo zatrzymany przed rozpoczęciem.

To odwraca częsty sposób pracy. Zamiast trenować do chwili znalezienia czegoś interesującego, ustalamy wcześniej, ile pytań możemy zadać i jak duża odpowiedź byłaby wystarczająca, aby odróżnić ją od szumu.

## Preregistracja nie jest przepowiednią sukcesu

Jeżeli wszystkie wcześniejsze warstwy przejdą, powstaje jedna formalna prerejestracja pierwszego pilota. Zawiera pytanie, mechanizm, dopuszczony zbiór informacji, rodziny cech, główny target, instrumenty, dane, baseline’y, koszty, split, budżet prób, kryterium sukcesu i warunek odrzucenia.

Status takiego dokumentu brzmi `UNTESTED`. Preregistracja nie oznacza, że hipoteza jest dobra; oznacza, że po wyniku nie będzie można bez śladu zmienić pytania, aby dopasować je do odpowiedzi.

Dopiero osobny eksperyment otrzyma prawo do treningu. Nawet jego pozytywny rezultat nie otworzy automatycznie holdoutu, nie wypromuje modelu i nie zezwoli na trading.

## Złożoność modelu przychodzi ostatnia

Najważniejszym produktem pierwszego etapu researchu nie będzie nowa sieć, ensemble ani architektura agentowa. Będzie nim zamrożony kontrakt mówiący:

- z jakich danych wolno korzystać,
- co system mógł wiedzieć w chwili decyzji,
- jaki wynik ma znaczenie po kosztach,
- które proste alternatywy trzeba pokonać,
- jak podzielono czas,
- ile prób wolno wykonać,
- co zakończy eksperyment wynikiem FAIL albo INCONCLUSIVE.

Dopiero wtedy pytanie „jaki model wybrać?” staje się naukowo sensowne.

Najłatwiej jest zwiększać inteligencję systemu przez dodawanie kolejnych algorytmów. Znacznie trudniej zbudować środowisko, w którym algorytm nie może korzystać z przyszłości, negocjować z kosztami ani zużywać niezależnego testu bez pozostawienia śladu.

Właśnie dlatego pierwszy model zaczyna się przed modelem.

Zaczyna się w chwili, gdy badacz zamyka sobie drogi ucieczki przed własnym wynikiem.

<div class="lab-archive"><strong>Status źródłowy:</strong> tekst opisuje aktualny projekt pakietu A01 - metodologię przygotowania pierwszego prerejestrowanego researchu alfy. Pakiet nie jest wynikiem modelowym, nie otwiera holdoutu, nie dowodzi przewagi i nie autoryzuje egzekucji. Prywatne definicje targetów, cech, kosztów i kryteriów promocji nie zostały ujawnione.</div>
