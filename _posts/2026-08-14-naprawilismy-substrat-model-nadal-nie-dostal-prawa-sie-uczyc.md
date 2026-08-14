---
layout: labpost
title: "Naprawiliśmy substrat. Model nadal nie dostał prawa się uczyć"
description: "A01 Fix Wave 02 zamknęła trzy konkretne błędy implementacyjne i przeszła niezależny replay, ale naukowy stan programu nadal blokuje A02 i model fitting."
dek: "Poprawne bajty, deterministyczny replay i testy adwersarialne mogą potwierdzić jakość artefaktu. Nie rozwiązują automatycznie stanu danych, władzy nad holdoutem ani prawa do formułowania hipotezy o przewadze."
date: 2026-08-14 07:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #08"
readingTime: 19
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #08"
cover_title: "ARTEFAKT PRZESZEDŁ. EKSPERYMENT JESZCZE NIE"
cover_subtitle: "A01 WAVE 02 ACCEPTED / RESEARCH STATE BLOCKED / MODEL FITTING FORBIDDEN"
cover_kind: research
---
<div class="article-status"><span class="primary">A01 WAVE 02 ACCEPTED</span><span>ARTIFACT EVIDENCE: GRADE A</span><span>SCIENTIFIC STATE: BLOCKED</span><span>A02: NOT AUTHORIZED</span></div>

Najłatwiej pomylić postęp inżynieryjny z postępem naukowym wtedy, gdy poprawka jest prawdziwa, testy są mocne, a cały pakiet daje się niezależnie odtworzyć. Wszystkie te warunki zostały spełnione przez A01 Fix Wave 02.

Dostarczone archiwum miało kanoniczną strukturę, przechodziło replay przy dwóch różnych wartościach `PYTHONHASHSEED`, a próby uszkodzenia zawartości, skompresowanego payloadu i końca archiwum były odrzucane. Trzy autoryzowane problemy implementacyjne zostały zamknięte na poziomie artefaktu.

Mimo tego kolejny etap modelowy pozostał zabroniony.

Nie wynikało to z braku zaufania do wykonanej poprawki. Wynikało z rozdzielenia dwóch pytań:

```text
Czy poprawiono dokładnie te trzy błędy?
```

i:

```text
Czy cały program A01 posiada już spójny, zaakceptowany stan naukowy?
```

Na pierwsze pytanie odpowiedź brzmi `PASS`. Na drugie nadal brzmi `BLOCKED_RESEARCH_STATE_RECONCILIATION_FAILED`.

To rozróżnienie może wydawać się nadmiernie ostrożne, dopóki nie przypomnimy sobie, że model fitting jest procesem zużywającym informację. Każda decyzja o rodzinie cech, targetach, baseline'ach i parametrach może pośrednio dostosowywać projekt do danych. Jeżeli stan holdoutu, czasu dostępności, kosztów albo budżetu eksperymentów pozostaje niepewny, rozpoczęcie treningu nie przyspiesza badań. Może jedynie utrudnić późniejsze odróżnienie odkrycia od adaptacji do procesu.

## Co A01 Fix Wave 02 rzeczywiście zamknęła

Niezależny audyt zaakceptował trzy konkretne poprawki.

### Tożsamość aliasu przed metadanymi

Obiekt osiągalny przez kilka ścieżek musi zostać sklasyfikowany jako klasa tożsamości, zanim kod zacznie czytać jego metadane. W przeciwnym razie dozwolona nazwa może sprowokować dostęp, zanim drugi alias ujawni, że ten sam obiekt należy do powierzchni zabronionej.

Wave 02 zmieniła kolejność: najpierw tożsamość i dominacja reguł, dopiero później operacje na pliku.

### Stabilne, typowane błędy USTAR

Surowe komunikaty biblioteki archiwów mogą różnić się pomiędzy platformami i wersjami środowiska. Jeżeli testy albo downstream logic polegają na dokładnym tekście wyjątku, portowalność staje się iluzją.

Poprawka mapuje błędy platformowe na stabilne, typowane znaczenie. System zachowuje informację o klasie naruszenia, ale nie uzależnia werdyktu od przypadkowej interpunkcji albo komunikatu konkretnej biblioteki.

### Zgodność power i multiplicity z metodą wykonaną naprawdę

Raport badawczy może deklarować jedną metodę korekty i mocy, podczas gdy kod wykonuje inną albo zapisuje metadane niezgodne z przebiegiem. Taka rozbieżność jest szczególnie niebezpieczna, ponieważ wynik wygląda statystycznie profesjonalnie, ale audyt nie potrafi odtworzyć znaczenia liczb.

Wave 02 związała metadane multiplicity i power z rzeczywiście wykonaną procedurą. Poprawa nie udowadnia mocy przyszłego eksperymentu, ale usuwa sprzeczność między metodą i opisem.

## Co zostało odtworzone

| Kontrola | Wynik |
|---|---:|
| Elementy archiwum | 39 |
| Zwykłe pliki | 30 |
| Katalogi | 9 |
| Przypadki kolejności aliasów | 18 |
| Przypadki mutacyjne | 5 |
| Pełne przypadki power | 2 |
| Typowane przypadki USTAR | 4 |
| Callbacki holdoutu w build process | 0 |
| Replay przy dwóch hash seeds | byte-identical |

Niezależne próby zmiany kanonicznej treści, odwrócenia bitu w skompresowanym payloadzie oraz dopisania trailera zakończyły się blokadą. Dla dokładnie dostarczonych bajtów i publicznego replayu przyznano evidence grade A.

Taki werdykt ma dużą wartość. Oznacza, że kolejny etap nie musi wracać do tych samych trzech problemów. Nie oznacza jednak, że cały stan badawczy A01 został zamrożony.

<figure>
<svg viewBox="0 0 1120 500" role="img" aria-labelledby="artifact-science-title artifact-science-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="artifact-science-title">Akceptacja artefaktu i promocja naukowa</title>
  <desc id="artifact-science-desc">Lewa ścieżka przedstawia zamknięte poprawki Wave 02 i zaakceptowany artefakt. Prawa ścieżka pokazuje nadal otwarte bramy stanu badawczego przed model fitting.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="46" y="70" width="456" height="344" rx="22" fill="var(--soft)" stroke="var(--up)" stroke-width="4"/>
    <rect x="618" y="70" width="456" height="344" rx="22" fill="var(--soft)" stroke="var(--dn)" stroke-width="4"/>
    <text x="274" y="116" text-anchor="middle" font-size="22" fill="var(--up)">ARTIFACT ACCEPTANCE</text>
    <text x="846" y="116" text-anchor="middle" font-size="22" fill="var(--dn)">SCIENTIFIC PROMOTION</text>
    <text x="88" y="166" font-size="16" fill="var(--ink)">alias ordering closed</text>
    <text x="88" y="204" font-size="16" fill="var(--ink)">typed USTAR errors</text>
    <text x="88" y="242" font-size="16" fill="var(--ink)">power metadata aligned</text>
    <text x="88" y="280" font-size="16" fill="var(--ink)">deterministic replay</text>
    <text x="88" y="318" font-size="16" fill="var(--ink)">negative mutations fail closed</text>
    <text x="660" y="166" font-size="16" fill="var(--mut)">global holdout authority: UNKNOWN</text>
    <text x="660" y="204" font-size="16" fill="var(--mut)">research-state reconciliation: BLOCKED</text>
    <text x="660" y="242" font-size="16" fill="var(--mut)">data and timestamp gates: OPEN</text>
    <text x="660" y="280" font-size="16" fill="var(--mut)">cost and capital gates: OPEN</text>
    <text x="660" y="318" font-size="16" fill="var(--mut)">A02 model fitting: FORBIDDEN</text>
    <path d="M530 90 V394" stroke="var(--dn)" stroke-width="4" stroke-dasharray="9 8"/>
    <text x="560" y="462" text-anchor="middle" font-size="17" fill="var(--mut)">Dobry artefakt nie przeskakuje brakujących bram naukowych.</text>
  </g>
</svg>
<figcaption>Wave 02 zamyka dokładny zakres implementacyjny. Prawo do eksperymentu wymaga osobnego domknięcia stanu badawczego.</figcaption>
</figure>

## Dlaczego zero callbacków nie zamyka holdoutu

Pakiet odnotował zero callbacków do zewnętrznego holdoutu podczas własnego procesu budowy. Jest to potrzebny dowód negatywny, ale obejmuje wyłącznie obserwowany proces i jego lokalną powierzchnię.

Globalna władza nad holdoutem jest szerszym problemem. Trzeba wiedzieć, czy istnieją inne worktree, archiwa, procesy, skrypty, notebooki albo kopie danych, które mogą odczytać wyniki i wpłynąć na decyzje. Nawet gdy nikt nie otworzył finalnej tabeli, wielokrotne zaglądanie do pośrednich ocen może stopniowo zamienić holdout w część pętli optymalizacyjnej.

Dlatego `zero callbacks` nie oznacza automatycznie `global holdout authority closed`.

<figure>
<svg viewBox="0 0 1120 540" role="img" aria-labelledby="holdout-title holdout-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="holdout-title">Lokalny brak dostępu i globalna władza nad holdoutem</title>
  <desc id="holdout-desc">Jeden proces może nie wywołać holdoutu, ale inne worktree, archiwa lub narzędzia nadal mogą posiadać dostęp. Globalna władza wymaga inwentaryzacji wszystkich ścieżek.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <circle cx="560" cy="270" r="104" fill="var(--soft)" stroke="var(--dn)" stroke-width="4"/>
    <text x="560" y="258" text-anchor="middle" font-size="21" fill="var(--dn)">OUTER</text>
    <text x="560" y="287" text-anchor="middle" font-size="21" fill="var(--dn)">HOLDOUT</text>
    <rect x="70" y="84" width="250" height="94" rx="16" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="800" y="84" width="250" height="94" rx="16" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <rect x="70" y="362" width="250" height="94" rx="16" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <rect x="800" y="362" width="250" height="94" rx="16" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <text x="195" y="120" text-anchor="middle" font-size="17" fill="var(--up)">WAVE 02 BUILD</text>
    <text x="195" y="149" text-anchor="middle" font-size="14" fill="var(--mut)">0 callbacks observed</text>
    <text x="925" y="120" text-anchor="middle" font-size="17" fill="var(--ink)">OTHER WORKTREES</text>
    <text x="925" y="149" text-anchor="middle" font-size="14" fill="var(--mut)">authority unknown</text>
    <text x="195" y="398" text-anchor="middle" font-size="17" fill="var(--ink)">ARCHIVES / COPIES</text>
    <text x="195" y="427" text-anchor="middle" font-size="14" fill="var(--mut)">membership unknown</text>
    <text x="925" y="398" text-anchor="middle" font-size="17" fill="var(--ink)">PROCESSES / TOOLS</text>
    <text x="925" y="427" text-anchor="middle" font-size="14" fill="var(--mut)">access history unknown</text>
    <path d="M320 142 C410 162 430 196 474 222" stroke="var(--up)" stroke-width="3" fill="none"/>
    <path d="M800 142 C710 162 690 196 646 222" stroke="var(--mut)" stroke-width="3" fill="none" stroke-dasharray="7 7"/>
    <path d="M320 409 C410 386 430 348 474 318" stroke="var(--mut)" stroke-width="3" fill="none" stroke-dasharray="7 7"/>
    <path d="M800 409 C710 386 690 348 646 318" stroke="var(--mut)" stroke-width="3" fill="none" stroke-dasharray="7 7"/>
  </g>
</svg>
<figcaption>Brak dostępu w jednym procesie jest lokalnym faktem. Globalna ochrona holdoutu wymaga zamknięcia wszystkich tożsamości, uprawnień i historii dostępu.</figcaption>
</figure>

## Najpierw stan badawczy, później model

Kolejny tor otrzymał nazwę A01R. Jego zadaniem nie jest znalezienie najlepszego modelu. Ma stworzyć jeden samodzielny, odtwarzalny substrat, który albo pozwoli zarejestrować pojedynczy eksperyment pilotażowy, albo zwróci precyzyjny blocker.

A01R musi odtworzyć kanoniczny stan poprzednich artefaktów, rejestru eksperymentów i negatywnych wyników. Powinien zamknąć globalną władzę nad holdoutem bez odczytywania jego wyników, zinwentaryzować jakość danych i znaczenie timestampów, wybrać niewielką liczbę rodzin pilotażowych, zamrozić target oraz koszty, opisać dostępność każdej cechy, przygotować baseline'y, budżet prób i warunki `INCONCLUSIVE_NO_CLAIM`.

Model fitting nadal jest zabroniony. W prerejestracji nie ma miejsca na wynik performance, ponieważ prerejestracja ma powstać przed wynikiem.

Możliwe są dwa uczciwe zakończenia:

```text
READY_FOR_ONE_PREREGISTERED_EXPERIMENT
```

albo:

```text
TYPED_BLOCKER
```

Drugi werdykt nie byłby porażką projektu. Oznaczałby, że system potrafi zatrzymać eksperyment przed wykorzystaniem danych, gdy jego warunki nie pozwalają jeszcze na interpretację wyniku.

## Dlaczego ten etap jest potrzebny

W badaniach tradingowych najdroższy błąd nie zawsze powstaje w samym modelu. Często pojawia się wcześniej, gdy zbiory danych, znaczenie czasu, koszty, universe i zasady dostępu do holdoutu pozostają częściowo określone, ale proces zachowuje się tak, jakby wszystkie te elementy były znane.

Im bardziej rozbudowany model, tym łatwiej zamaskować problem atrakcyjną krzywą wyników. Dlatego A01R ma zredukować swobodę interpretacji przed pierwszym fittingiem. Wymaga to pracy mniej efektownej niż trenowanie modelu, ale bez niej wynik może być precyzyjną odpowiedzią na źle zadane pytanie.

## Co wolno powiedzieć po Wave 02

```text
A01 Wave 02 exact artifact = ACCEPTED
A01 three authorized fixes = CLOSED
A01 deterministic public replay = PASS
A01 global holdout authority = UNKNOWN
A01 research-state reconciliation = BLOCKED
A02 model fitting = NOT AUTHORIZED
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
LIVE_TRADING_APPROVED = false
```

Wave 02 jest mocnym wynikiem, ponieważ poprawka przeszła niezależny audyt i może zostać zamrożona. Program naukowy pozostaje zablokowany, ponieważ jego brakujące bramy dotyczą innych własności.

Naprawiliśmy substrat. Teraz trzeba udowodnić, że eksperyment posiada spójny stan, zanim system nauczy się czegokolwiek z danych.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje publiczny zakres trzech poprawek, zasady ochrony holdoutu i kolejny gate A01R. Nie publikuje datasetów, definicji targetów, pełnego rejestru cech, progów mocy, budżetu prób, wielkości kapitału ani prywatnych warunków promocji modelu.</div>
