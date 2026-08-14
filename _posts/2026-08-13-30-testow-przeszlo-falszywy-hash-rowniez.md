---
layout: labpost
title: "30 testów przeszło. Fałszywy hash również"
description: "WP12 zbudował najmocniejszy dotąd przenośny kontrakt syntetycznego runtime'u, ale test przeciwnika wykazał różnicę między identyfikatorem o poprawnym formacie a dowodem rozwiązanym do rzeczywistych bajtów."
dek: "Zielony wynik nie kończy eksperymentu, dopóki nie wiadomo, jakiego typu dowód naprawdę powstał i do jakiego obiektu prowadzi jego identyfikator."
date: 2026-08-13 20:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #05"
readingTime: 15
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #05"
cover_title: "30/30 PASS. DOWÓD NADAL NIEZAMKNIĘTY"
cover_subtitle: "PORTABLE REPLAY PASS / EVIDENCE OBJECT CLOSURE BLOCKED"
cover_kind: evidence
---
<div class="article-status"><span class="primary">WP12 MILESTONE</span><span>PORTABLE REPLAY: PASS</span><span>EVIDENCE CLOSURE: BLOCKED</span><span>REAL RUNTIME: NOT MEASURED</span></div>

Najbardziej kuszący moment w pracy nad systemem badawczym pojawia się wtedy, gdy wszystko zaczyna świecić na zielono. Archiwum ma poprawny hash, verifier przechodzi kolejne etapy, trzydzieści testów kończy się wynikiem PASS, a raport wygląda tak, jakby następny krok był już tylko formalnością. W takiej chwili łatwo pomylić liczbę zaliczonych kontroli z siłą wniosku, który można na ich podstawie ogłosić.

WP12 był dokładnie takim momentem. Pakiet rzeczywiście wykonał ogromną pracę. Po raz pierwszy w tej części D-LOGIC powstał przenośny, odtwarzalny kontrakt syntetycznego runtime'u, który można było uruchomić bez importowania repozytorium i bez dotykania aktywnego terminala. Zewnętrzny verifier uwierzytelniał archiwum, materializował je w prywatnym katalogu, kontrolował topologię, ustawiał zamrożone tryby plików, uruchamiał Tier A, Tier B oraz korpus mutacji, a następnie zachowywał granicę non-execution.

Wynik był mocny:

```text
PASS_WP12_DIRECT_ARCHIVE_REPLAY
PASS_V6_TIER_A_PACKAGE_INTEGRITY
PASS_V6_TIER_B_FULL_RUNTIME_CLOSURE
PASS_V6_ARCHIVE_ONLY_ADVERSARIAL_CORPUS
30/30 PASS
```

Mimo tego niezależna kontrola nie zakończyła się akceptacją gotowości do pomiaru hosta. Red-team zadał pytanie prostsze od całej architektury: czy identyfikator nazywany dowodem rzeczywiście prowadzi do istniejącego obiektu dowodowego?

Odpowiedź brzmiała: nie zawsze.

## Co WP12 naprawdę osiągnął

Archiwum miało 514 872 bajty, zawierało 82 elementy, w tym 69 plików regularnych i 13 katalogów, a kontrola nie wykazała niebezpiecznych dowiązań, urządzeń, FIFO ani path traversal. Canonical gzip, USTAR, sidecar i struktura pakietu przeszły weryfikację.

W samym kontrakcie pojawiło się 34 obowiązkowych rodzajów węzłów, które rozdzielały między innymi system operacyjny, kernel, architekturę hosta, Pythona, OpenSSL, systemd, display, Wine, pełny Wine prefix, pełny runtime MT5, drzewo MQL5, terminal, wybrany EX5, konfigurację startową, action graph, sentinel, politykę czasu, wynik i cleanup.

Była to istotna poprawa wobec wcześniejszych etapów. Python przestał udawać tożsamość hosta, `kernel32.dll` nie był już przedstawiany jako dowód kernela Linux, a zwykły plik biblioteki MQL5 nie musiał być automatycznie odrzucany tylko dlatego, że nie znajdował się na krótkiej liście znanych nazw.

WP12 wprowadził również pełniejsze manifesty syntetycznych środowisk:

- pełnego jednorazowego Wine prefixu,
- pełnego runtime'u MT5,
- pełnego drzewa zasobów MQL5.

Dzięki regule full-root/no-proxy podkatalog `drive_c` nie mógł już samodzielnie udawać całego Wine prefixu, podobnie jak katalog `MQL5` albo `Profiles` nie mógł zastępować całego runtime'u terminala. Typed link graph pozwalał z kolei opisać dozwolone relacje typowe dla Wine bez wprowadzania naiwnego zakazu wszystkich dowiązań.

<figure>
<svg viewBox="0 0 1060 470" role="img" aria-labelledby="wp12-title wp12-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="wp12-title">Zakres rzeczywiście potwierdzony przez WP12</title>
  <desc id="wp12-desc">Pakiet, kontrakt i syntetyczne manifesty przeszły replay. Rozwiązanie każdego identyfikatora do obiektu dowodowego oraz realny pomiar hosta pozostały niezamknięte.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="55" y="58" width="280" height="300" rx="20" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="390" y="58" width="280" height="300" rx="20" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="725" y="58" width="280" height="300" rx="20" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="195" y="100" text-anchor="middle" font-size="20" fill="var(--ink)">PAKIET</text>
    <text x="530" y="100" text-anchor="middle" font-size="20" fill="var(--ink)">KONTRAKT</text>
    <text x="865" y="100" text-anchor="middle" font-size="20" fill="var(--ink)">DOWÓD REALNY</text>
    <text x="195" y="142" text-anchor="middle" font-size="15" fill="var(--up)">PASS</text>
    <text x="530" y="142" text-anchor="middle" font-size="15" fill="var(--up)">PASS SYNTHETIC</text>
    <text x="865" y="142" text-anchor="middle" font-size="15" fill="var(--dn)">BLOCKED</text>
    <text x="195" y="188" text-anchor="middle" font-size="14" fill="var(--mut)">canonical archive</text>
    <text x="195" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">external verifier</text>
    <text x="195" y="244" text-anchor="middle" font-size="14" fill="var(--mut)">archive-only replay</text>
    <text x="195" y="272" text-anchor="middle" font-size="14" fill="var(--mut)">30 controls</text>
    <text x="530" y="188" text-anchor="middle" font-size="14" fill="var(--mut)">34 mandatory nodes</text>
    <text x="530" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">sealed manifests</text>
    <text x="530" y="244" text-anchor="middle" font-size="14" fill="var(--mut)">full-root rules</text>
    <text x="530" y="272" text-anchor="middle" font-size="14" fill="var(--mut)">typed link graph</text>
    <text x="865" y="188" text-anchor="middle" font-size="14" fill="var(--mut)">evidence objects</text>
    <text x="865" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">full resolver replay</text>
    <text x="865" y="244" text-anchor="middle" font-size="14" fill="var(--mut)">real dependencies</text>
    <text x="865" y="272" text-anchor="middle" font-size="14" fill="var(--mut)">host measurement</text>
    <text x="530" y="416" text-anchor="middle" font-size="18" fill="var(--ink)">Sukces pakietu nie awansuje automatycznie typu dowodu</text>
  </g>
</svg>
<figcaption>WP12 zamknął mocny poziom pakietu i kontraktu syntetycznego. Nie zamknął jeszcze przejścia od identyfikatora do uwierzytelnionego obiektu ani od modelu runtime'u do jego realnego pomiaru.</figcaption>
</figure>

## Eksperyment z fałszywym hashem

Builder WP12 tworzył bezpośrednio związane hashe dla sześciu najważniejszych obiektów, między innymi pełnych drzew Wine, MT5 i MQL5, terminala, konfiguracji startowej oraz wybranego EX5. Dla wielu pozostałych węzłów obowiązkowych generował jednak wartość o poprawnym formacie SHA-256 na podstawie kontrolowanego opisu syntetycznego.

Resolver sprawdzał typ dowodu, rolę, kontekst, okres ważności i format hashu. Nie zawsze sprawdzał, czy identyfikator prowadzi do konkretnych bajtów, obiektu Git, manifestu albo typowanego receipt.

Red-team zbudował pełny syntetyczny spec przy użyciu uwierzytelnionego buildera, a następnie podmienił `evidence_sha256` dla pięciu obowiązkowych węzłów na ciąg sześćdziesięciu czterech liter `f`.

Zmiana objęła między innymi węzły reprezentujące runtime Pythona, system operacyjny hosta, display server, pakiet brokera i stały action graph. Każda z tych wartości wyglądała jak poprawny SHA-256, ale nie wskazywała na żaden dostarczony obiekt.

Resolver nadal zwrócił sukces oraz:

```text
EvidenceResolved = PASS
SemanticNodeClosure = PASS
RuntimeManifestClosure = PASS
RoleClosure = PASS
NonMutationVerified = PASS
```

W tym momencie trzydzieści zielonych testów przestało być końcem historii. Stały się początkiem nowego pytania.

```text
HashShaped(value) != EvidenceObjectResolved(value)
```

<figure>
<svg viewBox="0 0 1040 430" role="img" aria-labelledby="hash-title hash-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="hash-title">Poprawny format i rozwiązany obiekt dowodowy</title>
  <desc id="hash-desc">Dwie wartości mają poprawny format SHA-256. Tylko pierwsza prowadzi do uwierzytelnionych bajtów, druga kończy się pustym odwołaniem.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="55" y="55" width="930" height="130" rx="18" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="55" y="245" width="930" height="130" rx="18" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="95" y="98" font-size="18" fill="var(--ink)">Poprawny hash</text>
    <text x="95" y="128" font-size="14" fill="var(--mut)">format, typ, rola, kontekst</text>
    <line x1="355" y1="120" x2="610" y2="120" stroke="var(--up)" stroke-width="4"/>
    <circle cx="660" cy="120" r="34" fill="var(--up)" opacity=".18"/>
    <text x="660" y="126" text-anchor="middle" font-size="15" fill="var(--up)">BYTES</text>
    <text x="760" y="126" font-size="15" fill="var(--ink)">authenticated object</text>
    <text x="95" y="288" font-size="18" fill="var(--ink)">Hash o poprawnym kształcie</text>
    <text x="95" y="318" font-size="14" fill="var(--mut)">format, typ, rola, kontekst</text>
    <line x1="355" y1="310" x2="610" y2="310" stroke="var(--dn)" stroke-width="4" stroke-dasharray="9 8"/>
    <circle cx="660" cy="310" r="34" fill="var(--dn)" opacity=".16"/>
    <text x="660" y="316" text-anchor="middle" font-size="20" fill="var(--dn)">?</text>
    <text x="760" y="316" font-size="15" fill="var(--dn)">brak obiektu</text>
  </g>
</svg>
<figcaption>Metadane mogą być wewnętrznie spójne, a mimo to nie dowodzić istnienia obiektu, którego identyfikator został wpisany do kontraktu.</figcaption>
</figure>

## Dlaczego nazwa testu również jest twierdzeniem

Verifier raportował `PASS_V6_TIER_B_FULL_RUNTIME_CLOSURE`, ale Tier B odtwarzał przede wszystkim kontrakty komponentowe, reguły manifestów, ograniczenia pełnego korzenia, graf linków i wybrane mutacje. Nie rekonstruował od początku wszystkich trzydziestu czterech obiektów dowodowych, nie budował pełnego specu i nie przeprowadzał całego pozytywnego przypadku przez ten sam kompletny resolver.

Nazwa testu była więc szersza od jego faktycznej powierzchni. Nie oznacza to, że test był bezużyteczny. Oznacza, że etykieta `FULL_RUNTIME_CLOSURE` sugerowała mocniejszą klasę dowodu niż ta, którą wykonano.

W D-LOGIC nazwa PASS nie jest ozdobą raportu. Jest publicznym twierdzeniem, dlatego musi odpowiadać dokładnie temu, co zostało zaobserwowane.

## Replay działał, ale całe repozytorium nie było zielone

WP12 przechodził własny, zamknięty pakiet testów. Pełny suite repozytorium zakończył się jednak wynikiem:

```text
3692 passed
8 failed
37 setup errors
1 deselected
2 warnings
```

Błędy dotyczyły historycznych pinów środowiska WP08 i WP09, a nie wykazanej regresji WP12. Właściwa interpretacja brzmi więc: brak dowodu regresji WP12, potwierdzony dryf historycznego hosta oraz brak prawa do hasła `FULL REPOSITORY PASS`.

Zielony moduł może istnieć wewnątrz repozytorium, którego inne zamrożone kontrakty przestały odpowiadać bieżącemu hostowi. Oba fakty mogą być prawdziwe równocześnie.

## Dowody muszą mieć typ

WP12 doprowadził do rozdzielenia poziomów, które w wielu projektach są wrzucane do jednego worka z napisem „zweryfikowane”.

| Poziom | Pytanie |
|---|---|
| P0 SyntaxValid | Czy zapis jest poprawny składniowo? |
| P1 ContractValid | Czy spełnia deklarowany kontrakt? |
| P2 SemanticRoleCompatible | Czy znaczenie pasuje do roli? |
| P3 EvidenceObjectResolved | Czy identyfikator prowadzi do uwierzytelnionego obiektu? |
| P4 DependencyClosureComplete | Czy zamknięto wszystkie zależności? |
| P5 IdentityMeasured | Czy zmierzono właściwy obiekt w realnym środowisku? |
| P6 RuntimeBehaviorObserved | Czy zaobserwowano zachowanie runtime'u? |
| P7 DataSemanticsValidated | Czy dane znaczą to, co deklarujemy? |
| P8 PredictiveValueOOS | Czy istnieje wartość poza dopasowaniem? |
| P9 EconomicValueAfterCosts | Czy wynik przeżywa koszty i wykonanie? |
| P10 ForwardSurvival | Czy przeżywa nowe obserwacje w czasie? |
| P11 SafeExecutionAndRecovery | Czy działanie i awaria są kontrolowane? |

Tysiąc testów P2 nie tworzy automatycznie jednego dowodu P6. Podobnie sto atrakcyjnych backtestów nie tworzy forward edge, jeśli żaden eksperyment nie obserwował nowych decyzji w realnym czasie.

Formalnie gotowość poziomu `k` wymaga wszystkich obowiązkowych klas niższych:

```text
Ready(k) = AND Proof(i), dla i od 0 do k
```

Brak jednego obowiązkowego poziomu zatrzymuje promocję, nawet jeśli wszystkie niższe warstwy wyglądają perfekcyjnie.

## Ten sam błąd pojawia się w badaniach alfy

Feature może nazywać się `liquidity`, a mierzyć wyłącznie obrót. Metryka `net expectancy` może nie uwzględniać odrzuconych wykonań. Model opisany jako neutralny względem faktorów może pomijać ekspozycję, która wyjaśnia cały wynik. Forward może być jedynie wielokrotnie oglądanym holdoutem.

W każdym z tych przypadków liczba ma poprawny format, kod działa, a opis brzmi profesjonalnie. Problem dotyczy relacji między etykietą a obiektem, który ma ją uzasadniać.

```text
prawidłowa liczba + błędne znaczenie = błędny dowód
```

## Następny gate

WP12 pozostał zamrożonym milestone'em syntetycznego V6. Następca miał zamknąć `Evidence Object Closure`, dostarczyć pełny spec, przeprowadzić pozytywny przypadek i mutacje przez dokładnie tę samą ścieżkę resolvera oraz sprawić, aby fałszywe identyfikatory przestały przechodzić jako rozwiązane dowody.

Do tego momentu status tradingowy nie zmienił się ani o jeden poziom:

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

Największą wartością WP12 nie było samo 30/30. Była nią możliwość wskazania dokładnej granicy pomiędzy kontraktem, który wyglądał na domknięty, a dowodem, którego system jeszcze nie potrafił odnaleźć.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> publikacja opisuje wynik niezależnego audytu, publiczną hierarchię dowodów i klasy blockerów. Nie ujawnia prywatnych ścieżek, poświadczeń, pełnych manifestów, reguł autoryzacji ani powierzchni wykonawczej.</div>
