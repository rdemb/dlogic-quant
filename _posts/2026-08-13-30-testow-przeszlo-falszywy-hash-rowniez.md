---
layout: labpost
title: "30 testów przeszło. Fałszywy hash również"
description: "WP12 zbudował najmocniejszy dotąd przenośny kontrakt syntetycznego runtime'u, ale red-team wykazał, że poprawnie wyglądający hash nie zawsze prowadził do rzeczywistego obiektu dowodowego."
dek: "Pakiet odtworzył 30 z 30 kontroli bez importowania repozytorium. Następnie pięć obowiązkowych identyfikatorów zastąpiono fałszywą wartością, a resolver nadal raportował sukces."
date: 2026-08-13 20:00:00 +0200
updated: 2026-08-14 05:30:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #05"
readingTime: 19
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #05"
cover_title: "30/30 PASS. DOWÓD NADAL NIEZAMKNIĘTY"
cover_subtitle: "PORTABLE REPLAY PASS / EVIDENCE OBJECT CLOSURE FAIL / LIVE FALSE"
cover_kind: evidence
---
<div class="article-status"><span class="primary">WP12 MILESTONE</span><span>ARCHIVE REPLAY: PASS</span><span>EVIDENCE OBJECT CLOSURE: BLOCKED</span><span>HOST MEASUREMENT: NOT RUN</span><span>LIVE: NOT AUTHORIZED</span></div>

Trzydzieści testów zakończyło się wynikiem PASS. Archiwum miało kanoniczną strukturę, zewnętrzny verifier odtwarzał pakiet bez importowania repozytorium, a dostarczony korpus przypadków negatywnych nie naruszył granicy non-execution. Po wielu wcześniejszych iteracjach był to pierwszy pakiet, który potrafił samodzielnie zmaterializować własne wejścia, ponownie uwierzytelnić pliki i uruchomić cały przenośny zestaw kontroli.

Na ekranie widniało 30/30. Taki wynik naturalnie zachęca, aby zamknąć etap i przesunąć projekt dalej.

Red-team wykonał jednak prostszy eksperyment. W pięciu obowiązkowych węzłach zastąpił identyfikatory dowodowe wartością złożoną wyłącznie z liter `f`. Ciąg zachował długość i format prawidłowego SHA-256, ale pod tym adresem nie istniał uwierzytelniony obiekt, receipt ani zamrożone bajty. System powinien był zatrzymać się dokładnie w tym miejscu.

Resolver ponownie zwrócił PASS.

Problem nie unieważniał integralności archiwum ani pozostałych osiągnięć WP12. Ujawnił natomiast, że etykieta `EvidenceResolved` opisywała własność szerszą niż ta, którą rzeczywiście sprawdzał kod. Dla części węzłów system weryfikował metadane dowodu, ale nie rozwiązywał identyfikatora do konkretnego obiektu.

Najkrótszy zapis tej lekcji brzmi:

```text
HashShaped(value) != EvidenceObjectResolved(value)
```

## Co WP12 rzeczywiście osiągnął

WP12 pozostaje dużym sukcesem inżynieryjnym. Niezależny audyt odtworzył surowe archiwum i potwierdził jego podstawowe własności.

| Kontrola | Wynik |
|---|---:|
| Elementy archiwum | 82 |
| Zwykłe pliki | 69 |
| Katalogi | 13 |
| Niebezpieczne linki, urządzenia i path traversal | 0 |
| Przypadki end-to-end | 27/27 PASS |
| Testy komponentowe | 2/2 PASS |
| Predykaty statyczne | 1/1 PASS |
| Łączny replay | 30/30 PASS |

Verifier pracował na archiwum, nie importował repozytorium i zachował status `SYNTHETIC_NOT_RUNTIME_EVIDENCE`. Żadna część pakietu nie uruchomiła Wine, terminala, EX5, rachunku ani dostępu do rynku.

WP12 rozbudował także model przyszłego runtime'u. Wprowadził trzydzieści cztery obowiązkowe klasy węzłów i oddzielił między innymi system operacyjny, kernel, architekturę, runtime'y, display, Wine, terminal, zasoby MQL5, wybrany artefakt, action graph, sentinel, politykę czasu, wynik oraz cleanup.

Powstały pełniejsze manifesty syntetycznego Wine, MT5 i drzewa MQL5. Zwykłe pliki biblioteczne mogły zostać opisane poprzez zamrożony manifest, a podkatalog nie mógł samodzielnie udawać całego runtime'u. Typed link graph pozwalał z kolei opisać dozwolone relacje wewnętrzne bez naiwnego zakazu każdego symlinka.

Te zmiany zamknęły realne luki znane z WP11. Nie dowodziły jednak pomiaru prawdziwego hosta ani zgodności wykonawczej.

## Eksperyment z fałszywym hashem

Słowo `hash` bywa używane jak synonim pewności. Sześćdziesiąt cztery znaki szesnastkowe wyglądają technicznie, precyzyjnie i trudno je podważyć bez znajomości całego łańcucha.

Hash pełni funkcję dowodową dopiero wtedy, gdy system potrafi rozwiązać go do obiektu, którego integralność można ponownie sprawdzić. Sam format nie wystarcza.

W kontrolowanym eksperymencie podmieniono identyfikatory przypisane do pięciu różnych klas dowodu: runtime'u językowego, informacji o systemie operacyjnym, warstwy display, paczki kontrolnej oraz action graphu. Każda wartość została zastąpiona ciągiem:

```text
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
```

Mimo braku odpowiadających obiektów resolver nadal raportował:

```text
EvidenceResolved = PASS
SemanticNodeClosure = PASS
RuntimeManifestClosure = PASS
RoleClosure = PASS
NonMutationVerified = PASS
```

Dla części węzłów kontrolowane były format identyfikatora, deklarowany typ, rola, kontekst, przedział ważności i zgodność etykiety. Brakowało sprawdzenia, czy identyfikator prowadzi do istniejących bajtów, obiektu Git, manifestu, kontraktu albo typowanego receipt.

<figure>
<svg viewBox="0 0 1120 500" role="img" aria-labelledby="hash-title hash-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="hash-title">Hash w formacie a rozwiązany obiekt dowodowy</title>
  <desc id="hash-desc">Pierwsza ścieżka prowadzi od hashu do istniejących bajtów i pełnego dowodu. Druga zawiera fałszywy hash, brak obiektu i mimo tego wynik PASS na poziomie metadanych.</desc>
  <defs><marker id="hash-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <text x="54" y="58" font-size="20" fill="var(--up)">ŚCIEŻKA ZAMKNIĘTA</text>
    <rect x="54" y="82" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="326" y="82" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="598" y="82" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="870" y="82" width="190" height="76" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="164" y="116" text-anchor="middle" font-size="16" fill="var(--ink)">SHA-256</text><text x="164" y="140" text-anchor="middle" font-size="13" fill="var(--mut)">identyfikator</text>
    <text x="436" y="116" text-anchor="middle" font-size="16" fill="var(--ink)">OBIEKT</text><text x="436" y="140" text-anchor="middle" font-size="13" fill="var(--mut)">zamrożone bajty</text>
    <text x="708" y="116" text-anchor="middle" font-size="16" fill="var(--ink)">RECOMPUTE</text><text x="708" y="140" text-anchor="middle" font-size="13" fill="var(--mut)">ponowne hashowanie</text>
    <text x="965" y="116" text-anchor="middle" font-size="16" fill="var(--up)">PASS</text><text x="965" y="140" text-anchor="middle" font-size="13" fill="var(--mut)">dowód rozwiązany</text>
    <path d="M274 120 H320 M546 120 H592 M818 120 H864" stroke="var(--acc)" stroke-width="3" marker-end="url(#hash-arrow)"/>

    <text x="54" y="254" font-size="20" fill="var(--dn)">ŚCIEŻKA WP12 PO MUTACJI</text>
    <rect x="54" y="278" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <rect x="326" y="278" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <rect x="598" y="278" width="220" height="76" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
    <rect x="870" y="278" width="190" height="76" rx="14" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="164" y="312" text-anchor="middle" font-size="16" fill="var(--ink)">ffffffff...</text><text x="164" y="336" text-anchor="middle" font-size="13" fill="var(--mut)">format poprawny</text>
    <text x="436" y="312" text-anchor="middle" font-size="16" fill="var(--dn)">BRAK OBIEKTU</text><text x="436" y="336" text-anchor="middle" font-size="13" fill="var(--mut)">nic do rozwiązania</text>
    <text x="708" y="312" text-anchor="middle" font-size="16" fill="var(--ink)">METADANE</text><text x="708" y="336" text-anchor="middle" font-size="13" fill="var(--mut)">rola, typ, kontekst</text>
    <text x="965" y="312" text-anchor="middle" font-size="16" fill="var(--dn)">PASS</text><text x="965" y="336" text-anchor="middle" font-size="13" fill="var(--mut)">nazwa zbyt szeroka</text>
    <path d="M274 316 H320 M546 316 H592 M818 316 H864" stroke="var(--acc)" stroke-width="3" marker-end="url(#hash-arrow)"/>
    <text x="560" y="430" text-anchor="middle" font-size="18" fill="var(--ink)">MetadataValid nie oznacza EvidenceObjectResolved</text>
  </g>
</svg>
<figcaption>Hash staje się dowodem dopiero po rozwiązaniu go do konkretnego, uwierzytelnionego obiektu i ponownym sprawdzeniu jego bajtów.</figcaption>
</figure>

## Nazwa testu również jest twierdzeniem

Verifier WP12 zwracał nazwę sugerującą pełne zamknięcie runtime'u. Audyt wykazał jednak, że Tier B odtwarzał głównie kontrakty obowiązkowych węzłów, kontrole semantycznych komponentów, przyjęcie manifestów, reguły full-root, graf linków i wybrane mutacje.

Nie budował od zera wszystkich obiektów dowodowych, nie uruchamiał kompletnego pozytywnego resolvera na dokładnym, zamrożonym specu i nie przeprowadzał całego korpusu mutacji przez tę samą pełną ścieżkę.

Wynik pozostaje ważny, ale jego nazwa powinna odpowiadać zakresowi obserwacji. Bezpieczniejszy status brzmiałby:

```text
PASS_SYNTHETIC_CLOSURE_COMPONENT_CONTRACTS
```

Zamiast:

```text
PASS_FULL_RUNTIME_CLOSURE
```

Nazwa testu wpływa na decyzję człowieka. Jeżeli dashboard pokazuje `FULL_RUNTIME_CLOSURE`, odbiorca ma prawo zakładać, że odtworzono pełny obiekt, wszystkie obowiązkowe zależności i kompletną ścieżkę. Gdy pomiar obejmuje niższy poziom, nazwa musi pozostawić ten poziom widoczny.

Ta sama zasada obowiązuje w badaniach tradingowych:

```text
backtest pass != forward pass
forecast accuracy pass != net execution pass
data schema pass != data semantics pass
```

## Dowody muszą mieć typ

WP12 doprowadził do formalnego rozdzielenia kolejnych klas dowodu:

| Poziom | Znaczenie |
|---|---|
| P0 | poprawna składnia |
| P1 | poprawny kontrakt |
| P2 | zgodność roli semantycznej |
| P3 | rozwiązany obiekt dowodowy |
| P4 | kompletne zależności |
| P5 | zmierzona tożsamość realnego obiektu |
| P6 | zaobserwowane zachowanie runtime'u |
| P7 | zwalidowane znaczenie danych |
| P8 | wartość prognostyczna poza dopasowaniem |
| P9 | wartość ekonomiczna po kosztach |
| P10 | przetrwanie forward |
| P11 | bezpieczne wykonanie i recovery |

Duża liczba testów niższego poziomu nie tworzy brakującego dowodu wyższego typu.

<figure>
<svg viewBox="0 0 1120 470" role="img" aria-labelledby="proof-title proof-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="proof-title">Typy dowodu od składni do wykonania</title>
  <desc id="proof-desc">Poziomy P0 do P11 tworzą kolejne klasy dowodu. WP12 osiąga mocne kontrakty syntetyczne, ale zatrzymuje się przed pełnym P3 i przed obserwacją runtime'u.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="44" y="58" width="1032" height="318" rx="22" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
    <text x="92" y="102" font-size="17" fill="var(--up)">P0 Syntax</text><text x="92" y="142" font-size="17" fill="var(--up)">P1 Contract</text><text x="92" y="182" font-size="17" fill="var(--up)">P2 Semantic role</text>
    <text x="366" y="102" font-size="17" fill="var(--dn)">P3 Evidence object</text><text x="366" y="142" font-size="17" fill="var(--mut)">P4 Dependencies</text><text x="366" y="182" font-size="17" fill="var(--mut)">P5 Identity measured</text>
    <text x="668" y="102" font-size="17" fill="var(--mut)">P6 Runtime behavior</text><text x="668" y="142" font-size="17" fill="var(--mut)">P7 Data semantics</text><text x="668" y="182" font-size="17" fill="var(--mut)">P8 Predictive OOS</text>
    <text x="668" y="238" font-size="17" fill="var(--mut)">P9 Economic after costs</text><text x="668" y="278" font-size="17" fill="var(--mut)">P10 Forward survival</text><text x="668" y="318" font-size="17" fill="var(--mut)">P11 Safe execution</text>
    <rect x="82" y="242" width="480" height="84" rx="15" fill="var(--bg)" stroke="var(--acc)" stroke-width="2"/>
    <text x="322" y="275" text-anchor="middle" font-size="18" fill="var(--ink)">1000 wyników P2 nie tworzy dowodu P6</text>
    <text x="322" y="303" text-anchor="middle" font-size="14" fill="var(--mut)">brak obowiązkowej klasy kontroluje status łańcucha</text>
  </g>
</svg>
<figcaption>WP12 potwierdził silne kontrakty syntetyczne. Pełne EvidenceObjectResolved pozostało zadaniem następnego pakietu.</figcaption>
</figure>

Formalnie gotowość do poziomu `k` można traktować jako koniunkcję wcześniejszych dowodów:

```text
Ready(k) = Proof(0) AND Proof(1) AND ... AND Proof(k)
```

Jedna brakująca klasa kontroluje status całego łańcucha. Liczba PASS-ów nie może jej przegłosować.

## Dlaczego red-team zaczyna po sukcesie

Najbardziej wartościowe próby przeciwnika często pojawiają się po uzyskaniu zielonego wyniku. Dopiero wtedy wiadomo, jaki skrót interpretacyjny może zostać wykorzystany.

Podmiana na `ffffffff...` była skuteczna dlatego, że nie niszczyła całego pakietu. Zachowała typ, długość, rolę i kontekst, a usunęła wyłącznie relację z rzeczywistym obiektem. Test izolował jedną własność zamiast generować przypadkowy chaos.

Dobre falsyfikowanie nie polega na tworzeniu dowolnych błędów. Polega na usunięciu dokładnie tego składnika, który według nazwy werdyktu miał być konieczny, a następnie sprawdzeniu, czy sukces nadal jest możliwy.

## Ta sama luka występuje w modelach rynkowych

System może posiadać cechę nazwaną `liquidity`, choć mierzy wyłącznie wolumen. Może raportować `net expectancy`, ale pomijać odrzucone wykonania. Może ogłaszać neutralność faktorową bez kontroli ekspozycji odpowiadającej za większość wyniku. Może nazywać próbę forwardem, mimo że wynik był wielokrotnie oglądany i wpływał na kolejne decyzje.

W każdym przypadku liczba, wykres albo etykieta wyglądają poprawnie. Brakuje rozwiązania pojęcia do właściwego obiektu pomiarowego.

Dlatego formalizm D-LOGIC wymaga kilku jednoczesnych domknięć:

```text
MeasurementReady =
    RoleClosure
    AND SemanticNodeClosure
    AND RuntimeManifestClosure
    AND EvidenceObjectClosure
    AND NonMutationVerified
```

WP12 zbudował mocne pierwsze warstwy w środowisku syntetycznym. Pełne `EvidenceObjectClosure` pozostawało zablokowane.

## WP13 jako osobny następca

WP12 został zachowany jako zamrożony milestone V6. Nie przepisano go po fakcie, aby stary pakiet wyglądał na poprawny. WP13 powstał jako osobny następca i zmienił znaczenie `EvidenceResolved`.

Trzydzieści cztery obowiązkowe węzły otrzymały uwierzytelnione obiekty albo typowane receipts, a pełny resolver przeszedł 340 mutacji bez importowania repozytorium i bez wykonania runtime'u. Brak obiektu zaczął kończyć się blokadą.

Ta kontynuacja nie zmienia historycznego znaczenia WP12. Pokazuje dokładnie, kiedy właściwość systemu została naprawiona i jaki nowy dowód uzasadnia zmianę statusu.

Pełny opis następnego etapu znajduje się w Chronicle #06: [340 prób obejścia. Fałszywy hash już nie przeszedł]({{ '/2026/08/14/340-prob-obejscia-falszywy-hash-juz-nie-przeszedl/' | relative_url }}).

Aktualna granica pozostaje konserwatywna:

```text
LIFECYCLE = COMPILED
LOADABLE = UNKNOWN
CANARY_TESTED = false
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
RISK_GOVERNOR_READY = false
LIVE_TRADING_APPROVED = false
```

WP12 nie uczynił systemu gotowym do uruchomienia. Zrobił dwie rzeczy bardziej użyteczne na tym etapie: stworzył najlepszy dotąd przenośny kontrakt syntetycznego runtime'u i ujawnił dokładne miejsce, w którym metadane dowodu były mylone z rozwiązanym obiektem dowodowym.

Właśnie dlatego kronika istnieje. Zielony wynik nie kończy eksperymentu, dopóki nie wiadomo, jakiego typu dowód naprawdę powstał.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje wynik audytu, klasy dowodów i publiczne granice następnego gate'u. Nie publikuje prywatnych korzeni runtime'u, poświadczeń, pełnych kontraktów resolvera, zasad autoryzacji, mapy usług ani powierzchni umożliwiającej odtworzenie wykonania.</div>
