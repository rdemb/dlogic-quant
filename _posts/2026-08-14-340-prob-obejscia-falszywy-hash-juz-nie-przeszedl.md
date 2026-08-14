---
layout: labpost
title: "340 prób obejścia. Fałszywy hash już nie przeszedł"
description: "WP13 zamknął lukę odkrytą w WP12: każdy obowiązkowy identyfikator dowodowy w przenośnym pakiecie prowadzi teraz do uwierzytelnionego obiektu albo typowanego receipt."
dek: "Najlepszy test poprawki nie polegał na ponownym uruchomieniu scenariusza pozytywnego. Polegał na odtworzeniu setek sposobów, w jakie system mógłby zaakceptować poprawnie wyglądający, ale nieistniejący dowód."
date: 2026-08-14 06:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #06"
readingTime: 21
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #06"
cover_title: "FAŁSZYWY HASH JUŻ NIE PRZESZEDŁ"
cover_subtitle: "340/340 MUTATIONS / EVIDENCE OBJECT CLOSURE PASS / RUNTIME UNKNOWN"
cover_kind: evidence
---
<div class="article-status"><span class="primary">WP13 ACCEPTED</span><span>DIRECT ARCHIVE REPLAY: PASS</span><span>EVIDENCE OBJECT CLOSURE: PASS</span><span>REAL RUNTIME: NOT MEASURED</span><span>LIVE: NOT AUTHORIZED</span></div>

W poprzednim etapie pięć obowiązkowych identyfikatorów dowodowych zostało zastąpionych ciągiem złożonym z sześćdziesięciu czterech liter `f`. Wartość wyglądała jak poprawny SHA-256, ale nie wskazywała na zamrożone bajty, obiekt Git, manifest ani typowany receipt. Resolver mimo tego zwrócił sukces.

WP12 nie przegrał dlatego, że hash był błędnie zapisany. Przegrał dlatego, że system pomylił poprawny kształt identyfikatora z istnieniem obiektu, którego identyfikator miał być adresem. Była to subtelna luka, ponieważ wszystkie lokalne metadane mogły wyglądać spójnie: rodzaj węzła pasował do schematu, rola była zgodna, przedział ważności istniał, a tekst miał długość oczekiwaną od kryptograficznego skrótu. Brakowało jednego pytania: gdzie są dokładne bajty, które ten skrót identyfikuje?

WP13 powstał po to, aby zamknąć wyłącznie ten problem, bez rozpoczynania kolejnego etapu wykonawczego. Nie uruchamiał terminala, nie mierzył prawdziwego hosta, nie ładował EX5 i nie kontaktował się z brokerem. Zbudował natomiast kompletny magazyn obiektów dowodowych dla kontrolowanego pakietu syntetycznego i przepuścił przez tę samą ścieżkę scenariusz pozytywny oraz setki mutacji.

Niezależny audyt zakończył się werdyktem:

```text
PASS_WP13_INDEPENDENT_ARTIFACT_ACCEPTANCE
```

Ten status ma wąskie, ale istotne znaczenie. Luka `EvidenceObjectClosure` odkryta w WP12 została zamknięta na poziomie dostarczonego, syntetycznego artefaktu. Nie oznacza to jeszcze, że znamy zachowanie realnego środowiska Wine, MT5 albo brokera.

## Co zostało niezależnie odtworzone

WP13 został oceniony bez importowania repozytorium i bez korzystania z aktywnego środowiska. Audyt pracował na dostarczonym archiwum, zewnętrznym verifierze oraz zawartości, którą można było ponownie uwierzytelnić.

| Kontrola | Wynik |
|---|---:|
| Elementy archiwum | 88 |
| Zwykłe pliki | 78 |
| Katalogi | 10 |
| Obiekty dowodowe | 34 dla 34 obowiązkowych węzłów |
| Mutacje pełnego resolvera | 340/340 PASS |
| Testy komponentowe | 2/2 PASS |
| Predykaty statyczne | 3/3 PASS |
| Canonical gzip i USTAR | PASS |
| Import repozytorium | NIE |
| Wykonanie runtime | NIE |

Wszystkie trzydzieści cztery obowiązkowe klasy semantyczne otrzymały obiekty znajdujące się wewnątrz pakietu. Ich identyfikatory, rozmiary, tryby i hashe były ponownie sprawdzane, a graf zależności pozostał zamknięty oraz acykliczny. Osobny harness blokujący procesy i sieć nie uniemożliwił replayu, co potwierdziło, że przenośna kontrola nie korzystała ukradkiem z zewnętrznego runtime'u ani aktywnej infrastruktury.

Najważniejsza różnica wobec WP12 nie polega więc na większej liczbie dokumentów. Polega na zmianie semantyki słowa `resolved`.

## Co znaczy rozwiązać dowód

Identyfikator dowodowy może pełnić kilka funkcji. Może być wyłącznie polem tekstowym o prawidłowym formacie, może wskazywać obiekt zadeklarowany w manifeście, może prowadzić do bajtów znajdujących się w tym samym pakiecie albo do zewnętrznego obiektu, którego tożsamość potrafimy niezależnie odtworzyć.

WP13 wymaga, aby obowiązkowy węzeł kończył się na obiekcie o określonym typie. Dopuszczalne są między innymi uwierzytelnione bajty pakietu, manifest statycznego drzewa, kontrakt, obiekt źródłowy lub typowany receipt syntetycznego pomiaru. Sama deklaracja nie wystarcza.

Publiczny model można przedstawić jako cztery kroki:

```text
semantic node
object identifier
sealed evidence object
recomputed verification result
```

<figure>
<svg viewBox="0 0 1120 500" role="img" aria-labelledby="wp13-object-title wp13-object-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="wp13-object-title">Domknięcie obiektu dowodowego w WP13</title>
  <desc id="wp13-object-desc">Każdy obowiązkowy węzeł prowadzi przez identyfikator do zapakowanego obiektu, który jest ponownie hashowany i dopiero wtedy uczestniczy w werdykcie resolvera.</desc>
  <defs><marker id="wp13-object-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="42" y="110" width="230" height="122" rx="18" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="314" y="110" width="230" height="122" rx="18" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="586" y="110" width="230" height="122" rx="18" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="858" y="110" width="220" height="122" rx="18" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="157" y="151" text-anchor="middle" font-size="18" fill="var(--ink)">SEMANTIC NODE</text>
    <text x="157" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">rola i obowiązek</text>
    <text x="429" y="151" text-anchor="middle" font-size="18" fill="var(--ink)">OBJECT ID</text>
    <text x="429" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">adres zawartości</text>
    <text x="701" y="151" text-anchor="middle" font-size="18" fill="var(--ink)">SEALED OBJECT</text>
    <text x="701" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">bajty, typ, rozmiar</text>
    <text x="968" y="151" text-anchor="middle" font-size="18" fill="var(--up)">RESOLVER PASS</text>
    <text x="968" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">po recomputacji</text>
    <path d="M272 171 H308 M544 171 H580 M816 171 H852" stroke="var(--acc)" stroke-width="3" marker-end="url(#wp13-object-arrow)"/>
    <rect x="314" y="302" width="502" height="104" rx="18" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="565" y="341" text-anchor="middle" font-size="18" fill="var(--dn)">FAŁSZYWY HASH LUB BRAK OBIEKTU</text>
    <text x="565" y="372" text-anchor="middle" font-size="14" fill="var(--mut)">werdykt zatrzymuje się przed statusem EvidenceObjectResolved</text>
    <path d="M565 232 V296" stroke="var(--dn)" stroke-width="3" stroke-dasharray="8 7" marker-end="url(#wp13-object-arrow)"/>
  </g>
</svg>
<figcaption>W WP13 poprawny format identyfikatora nie wystarcza. Werdykt wymaga odnalezienia obiektu, ponownego obliczenia jego tożsamości i zgodności z przypisaną rolą.</figcaption>
</figure>

Ta zmiana ma znaczenie większe niż konkretna biblioteka lub format archiwum. System dowodowy powinien umieć odpowiedzieć nie tylko, czy pole wygląda wiarygodnie, ale także czy potrafi przejść od twierdzenia do materialnego obiektu, na którym twierdzenie się opiera.

## Dlaczego 340 prób obejścia ma znaczenie

Scenariusz pozytywny pokazuje, że system działa w jednym kontrolowanym przypadku. Mutacje sprawdzają, czy sukces można uzyskać również wtedy, gdy zmienimy element, którego integralność miała być warunkiem sukcesu.

WP13 przeprowadził 340 mutacji przez pełną ścieżkę resolvera. Nie były to wyłącznie testy formatu pojedynczego pola. Obejmowały między innymi podmianę identyfikatorów, zmiany obiektów, naruszenie typów, zależności, relacji i kontraktów wymaganych przez zamrożony spec. Wszystkie przypadki oczekiwanej blokady zakończyły się fail-closed.

Sama liczba 340 nie jest magiczna. Ważniejsze jest to, że pozytywny przypadek oraz przypadki negatywne przechodziły przez tę samą, kompletną ścieżkę. W WP12 szeroka nazwa Tier B obejmowała głównie zestaw kontraktów komponentowych. WP13 odtworzył pełny resolver z obiektów znajdujących się w archiwum, dzięki czemu nazwa testu lepiej odpowiadała właściwości, którą test faktycznie obserwował.

Warto jednak zachować dyscyplinę, która doprowadziła do powstania tego pakietu. Trzysta czterdzieści zaliczonych mutacji nie awansuje syntetycznego dowodu do obserwacji prawdziwego hosta.

## Pakiet jest kompletny w swoim świecie

Największym ryzykiem komunikacyjnym po sukcesie WP13 byłoby pominięcie słowa `synthetic`.

Dostarczony artefakt jest kompletny w kontrolowanym świecie pakietu. Zawiera obowiązkowe obiekty, zależności i reguły potrzebne do odtworzenia własnego werdyktu. Nie zawiera jednak pomiaru działającego systemu operacyjnego, aktywnego menedżera usług, realnego prefiksu Wine, prawdziwego terminala, danych brokera ani zachowania ładowanego EX5.

Można porównać to do bardzo dokładnej makiety mostu. Jeżeli wszystkie elementy makiety mają znane materiały, wymiary, połączenia i wyniki prób obciążeniowych, wiemy dużo o spójności modelu. Nadal nie wiemy, jak prawdziwa konstrukcja zachowa się przy wietrze, korozji, zmianach temperatury i błędach wykonawczych. Analogia ma ograniczenie: runtime nie jest mostem, ale dobrze pokazuje różnicę między zamkniętym modelem i zaobserwowanym zachowaniem realnego obiektu.

<figure>
<svg viewBox="0 0 1120 510" role="img" aria-labelledby="artifact-runtime-title artifact-runtime-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="artifact-runtime-title">Granica między artefaktem syntetycznym i realnym runtime'em</title>
  <desc id="artifact-runtime-desc">Lewa strona pokazuje zaakceptowany syntetyczny pakiet WP13. Prawa strona pokazuje nadal niezmierzone środowisko hosta, terminal, broker i dane.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="46" y="72" width="454" height="350" rx="22" fill="var(--soft)" stroke="var(--up)" stroke-width="4"/>
    <rect x="620" y="72" width="454" height="350" rx="22" fill="var(--soft)" stroke="var(--dn)" stroke-width="4"/>
    <text x="273" y="116" text-anchor="middle" font-size="22" fill="var(--up)">WP13 ARTIFACT</text>
    <text x="847" y="116" text-anchor="middle" font-size="22" fill="var(--dn)">REAL RUNTIME</text>
    <text x="90" y="166" font-size="16" fill="var(--ink)">34 evidence objects</text>
    <text x="90" y="202" font-size="16" fill="var(--ink)">closed dependency graph</text>
    <text x="90" y="238" font-size="16" fill="var(--ink)">full resolver replay</text>
    <text x="90" y="274" font-size="16" fill="var(--ink)">340 fail-closed mutations</text>
    <text x="90" y="310" font-size="16" fill="var(--ink)">no repository import</text>
    <text x="90" y="346" font-size="16" fill="var(--ink)">no process or network need</text>
    <text x="664" y="166" font-size="16" fill="var(--mut)">host identity: UNKNOWN</text>
    <text x="664" y="202" font-size="16" fill="var(--mut)">Wine and MT5 behavior: UNKNOWN</text>
    <text x="664" y="238" font-size="16" fill="var(--mut)">EX5 loadability: UNKNOWN</text>
    <text x="664" y="274" font-size="16" fill="var(--mut)">broker data: NOT TESTED</text>
    <text x="664" y="310" font-size="16" fill="var(--mut)">execution: DISABLED</text>
    <text x="664" y="346" font-size="16" fill="var(--mut)">LIVE: NOT AUTHORIZED</text>
    <path d="M526 90 V404" stroke="var(--dn)" stroke-width="4" stroke-dasharray="9 8"/>
    <text x="560" y="458" text-anchor="middle" font-size="17" fill="var(--mut)">Artifact acceptance nie przekracza granicy runtime observation.</text>
  </g>
</svg>
<figcaption>WP13 otrzymał mocny werdykt na poziomie artefaktu. Prawa strona pozostaje poza zakresem i nie może być dopowiedziana przez analogię.</figcaption>
</figure>

## Sukces nie uruchamia automatycznie WP14

W wielu projektach zaliczenie pakietu staje się uzasadnieniem dla natychmiastowego rozpoczęcia jeszcze większej wersji tego samego programu. W D-LOGIC przyjęto inną decyzję. WP13 zostaje zamrożony jako kanoniczny artefakt domknięcia obiektów dowodowych, a szeroka rozbudowa Evidence Plane zostaje zatrzymana.

Powód jest praktyczny. Projekt potrzebuje teraz dwóch rzeczy bardziej niż kolejnej abstrakcyjnej warstwy poświadczenia: pełnego substratu badawczego dla pierwszego uczciwego eksperymentu oraz użytecznego produktu semi-algo, który potrafi pracować w trybie obserwacyjnym i shadow bez otwierania drogi do zleceń.

Dalsza praca dowodowa ma wracać wyłącznie wtedy, gdy bezpośrednio blokuje autoryzowany gate danych, produktu lub wykonania. Taka zasada chroni przed sytuacją, w której system perfekcyjnie udowadnia własne artefakty, ale nie zbliża się do pytania, czy istnieje przewidywalność albo użyteczna decyzja.

## Ta sama luka występuje w modelach rynkowych

W badaniach quant odpowiednikiem fałszywego hashu jest poprawnie nazwana zmienna, która nie mierzy deklarowanej własności.

Pole może nazywać się `liquidity`, choć opisuje jedynie wolumen. `Net expectancy` może pomijać odrzucone wykonania, finansowanie albo minimalny rozmiar pozycji. `Forward` może oznaczać próbę wielokrotnie oglądaną podczas kolejnych decyzji. `Factor neutral` może nie kontrolować ekspozycji, która odpowiada za znaczną część wyniku.

W każdym przypadku składnia oraz etykieta są poprawne. Brakuje rozwiązania pojęcia do właściwego obiektu pomiarowego.

Dlatego WP13 ma znaczenie dla Alpha Research Plane mimo tego, że nie testuje żadnego modelu. Utrwala zasadę, że twierdzenie musi prowadzić do dowodu tego samego typu, którego wymaga jego nazwa. Liczba, hash albo wykres nie nabywają znaczenia przez samą obecność w raporcie.

## Co WP13 zmienia, a czego nie zmienia

Po niezależnym audycie można publicznie powiedzieć:

```text
WP13 packaged Evidence Object Closure = ACCEPTED
WP13 direct archive replay = ACCEPTED
WP13 full resolver mutations = 340/340 PASS
WP13 real runtime representation = UNKNOWN
WP13 loadability = UNKNOWN
```

Nie wolno natomiast dopisywać:

```text
host measured
terminal verified
EX5 loadable
broker data validated
model edge proven
execution ready
```

Końcowy stan pozostaje konserwatywny:

```text
LIFECYCLE = COMPILED
LOADABLE = UNKNOWN
CANARY_TESTED = false
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
RISK_GOVERNOR_READY = false
SAFE_TO_SIGN = false
SAFE_TO_INSTALL = false
SAFE_TO_EXECUTE = false
LIVE_TRADING_APPROVED = false
```

WP13 jest prawdziwym sukcesem, ponieważ zamknął dokładnie tę lukę, którą miał zamknąć, i nie próbował użyć tego wyniku do promowania pozostałych części systemu.

W poprzedniej wersji fałszywy hash przeszedł. W następnej został doprowadzony do miejsca, w którym powinien istnieć obiekt. Gdy obiektu nie było, system zatrzymał się.

Tak wygląda postęp w laboratorium, które mierzy swoje twierdzenia zamiast jedynie liczyć zielone pola.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> artykuł opisuje publiczny wynik WP13, typy obiektów dowodowych i granicę syntetycznego artefaktu. Nie publikuje prywatnego magazynu obiektów, dokładnego specu resolvera, korzeni runtime'u, poświadczeń, reguł autoryzacji ani powierzchni wykonawczej.</div>
