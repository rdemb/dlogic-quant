---
layout: labpost
title: "Semi-Algo First. Autonomia dopiero po dowodzie"
description: "D-LOGIC rozdziela rozwój na wiarygodność dowodów, praktyczny produkt wspierający operatora oraz badania przewidywalności, a automatyzację rozwija najpierw w trybie shadow."
dek: "System może dostarczać wartość wcześniej, pozostawiając wyższe poziomy autonomii poza zakresem do czasu spełnienia warunków danych, modelu, kosztów, ryzyka i wykonania."
date: 2026-08-13 21:00:00 +0200
updated: 2026-08-14 05:45:00 +0200
category: algo
eyebrow: "D-LOGIC Strategy #01"
readingTime: 21
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC PRODUCT STRATEGY #01"
cover_title: "SEMI-ALGO FIRST"
cover_subtitle: "PRODUCT NOW / ALPHA BY RESEARCH / AUTONOMY BY EVIDENCE"
cover_kind: research
---
<div class="article-status"><span class="primary">PRODUCT STRATEGY</span><span>S01H: ACCEPTED</span><span>S02: SHADOW ONLY</span><span>ORDER SURFACE: ABSENT</span><span>LIVE: NOT AUTHORIZED</span></div>

Przez długi czas rozwój D-LOGIC przypominał budowę mostu, na który nie wolno wejść, dopóki każda śruba, warstwa asfaltu i procedura ewakuacji nie zostaną opisane oraz sprawdzone. Taka dyscyplina chroni przed pochopnym uruchomieniem systemu, ale niesie własne ryzyko: infrastruktura dowodowa może zacząć pochłaniać cały projekt, podczas gdy narzędzie nie pomaga jeszcze operatorowi w codziennej pracy.

Decyzja `Semi-Algo First` zmienia kolejność, ale nie obniża standardu. D-LOGIC ma najpierw stać się użytecznym, kontrolowanym deskem analitycznym z człowiekiem w pętli. Program automatyzacji rozwija się równolegle, początkowo jako shadow policy pozbawiona brokera, sieci i powierzchni zleceń. Prawo do działania pozostaje zależne od osobnych dowodów.

Nowa zasada brzmi:

```text
SEMI-ALGO FIRST
AUTONOMY BY EVIDENCE
```

Semi-algo nie jest niedokończoną autonomią. Jest pełnoprawnym produktem o innym podziale odpowiedzialności. Maszyna obserwuje, porządkuje, ocenia jakość danych, przygotowuje kandydatury i ogranicza ryzyko. Człowiek rozstrzyga, czy zaakceptować, odrzucić albo odłożyć decyzję, a wykonanie pozostaje ręczne. Wszystkie kroki są zapisywane tak, aby później można było oddzielić wartość modelu od wartości ludzkiej selekcji.

## Dlaczego projekt potrzebował nowej kolejności

D-LOGIC zgromadził rozbudowaną historię audytów, negatywnych wyników, kontraktów danych, warstw stanu rynku i pomysłów produktowych. Jednocześnie coraz więcej pracy trafiało do Evidence Plane, czyli programu poświadczania przyszłego środowiska runtime.

Ta praca była potrzebna. WP12 i WP13 pokazały, że nawet poprawnie wyglądający hash może nie prowadzić do obiektu dowodowego, a nazwa testu może sugerować szerszy sukces niż faktyczny zakres pomiaru. Po zamknięciu tej luki broad Evidence Plane został jednak zamrożony. Kolejna wielka iteracja poświadczenia nie otrzymała automatycznej zgody wyłącznie dlatego, że poprzednia przeszła audyt.

Projekt wraca więc do dwóch pytań, które bezpośrednio tworzą wartość:

1. Czy można zbudować desk, który poprawia jakość i powtarzalność decyzji operatora już teraz?
2. Czy można równolegle stworzyć automatyczny rdzeń decyzyjny, który uczy się obserwować, abstainować i ograniczać ryzyko, nie posiadając możliwości handlu?

Odpowiedzią są tory S01H oraz S02.

## Trzy niezależne płaszczyzny

D-LOGIC rozwija trzy programy, które korzystają z części wspólnej infrastruktury, ale nie mogą udawać własnych dowodów.

### Evidence Plane

Ten tor odpowiada za tożsamość artefaktów, odtwarzalność, kompletność dowodów i granice wykonania. WP13 został zaakceptowany jako syntetyczny artefakt Evidence Object Closure. Nie potwierdził realnego hosta, terminala ani danych brokera.

### Product and Automation Plane

Ten tor odzyskuje ergonomię CMD Desku, zamraża kontrakty produktu i buduje wspólny rdzeń decyzji dla operatora oraz shadow autonomy. Nie ocenia alfy historycznych liczb i nie posiada order API.

### Alpha Research Plane

Ten tor odpowiada za dane, czas dostępności, targety, koszty, baseline'y, multiple testing, holdout, OOS i forward. A01 Wave 02 naprawiła trzy problemy artefaktu, ale pełny stan naukowy pozostaje zablokowany. A01R ma dopiero ustalić, czy jeden prerejestrowany eksperyment może zostać autoryzowany.

<figure>
<svg viewBox="0 0 1120 510" role="img" aria-labelledby="tracks-title tracks-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="tracks-title">Trzy płaszczyzny D-LOGIC</title>
  <desc id="tracks-desc">Evidence Plane, Product and Automation Plane oraz Alpha Research Plane rozwijają się niezależnie. Dopiero ich przyszłe przecięcie może prowadzić do uprawnionej autonomii.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <circle cx="350" cy="222" r="155" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <circle cx="560" cy="222" r="155" fill="var(--soft)" stroke="var(--up)" stroke-width="4"/>
    <circle cx="770" cy="222" r="155" fill="var(--soft)" stroke="var(--dn)" stroke-width="4"/>
    <text x="280" y="132" text-anchor="middle" font-size="20" fill="var(--acc)">EVIDENCE</text>
    <text x="560" y="132" text-anchor="middle" font-size="20" fill="var(--up)">PRODUCT</text>
    <text x="840" y="132" text-anchor="middle" font-size="20" fill="var(--dn)">ALPHA</text>
    <text x="270" y="235" text-anchor="middle" font-size="14" fill="var(--mut)">identity</text>
    <text x="270" y="263" text-anchor="middle" font-size="14" fill="var(--mut)">replay</text>
    <text x="560" y="235" text-anchor="middle" font-size="14" fill="var(--mut)">desk</text>
    <text x="560" y="263" text-anchor="middle" font-size="14" fill="var(--mut)">decision core</text>
    <text x="850" y="235" text-anchor="middle" font-size="14" fill="var(--mut)">data and target</text>
    <text x="850" y="263" text-anchor="middle" font-size="14" fill="var(--mut)">OOS and forward</text>
    <circle cx="560" cy="222" r="48" fill="var(--ink)" opacity=".9"/>
    <text x="560" y="218" text-anchor="middle" font-size="14" fill="var(--bg)">FUTURE</text>
    <text x="560" y="240" text-anchor="middle" font-size="14" fill="var(--bg)">AUTHORITY</text>
    <text x="560" y="448" text-anchor="middle" font-size="17" fill="var(--mut)">Sukces jednej płaszczyzny nie promuje dwóch pozostałych.</text>
  </g>
</svg>
<figcaption>Produkt może powstawać wcześniej, ale wyższa autonomia wymaga przyszłego przecięcia dowodów produktu, modelu i wykonania.</figcaption>
</figure>

## Odzyskanie CMD Desku bez dziedziczenia starych twierdzeń

Historyczny CMD Desk posiadał widoki `PULSE`, `CANDIDATES`, `LEVELS`, `MAP` i `FLOW`. Łączył stan rynku, rankingi, poziomy, przepływ, kalendarz, COT, ścieżki banków centralnych i relacje między instrumentami. Interfejs przechowywał wartościową wiedzę o tym, jak operator chce przeglądać rynek.

Zrzuty ekranu nie potwierdzały jednak pochodzenia i znaczenia każdej liczby. Nie było podstaw, aby odziedziczyć dawne `HIT%`, `EVbp`, `bias`, `regime`, `strength`, rankingi, poziomy SL/TP albo tradability jako zwalidowane metryki.

S01 sklasyfikował odzyskane komponenty i pola jako:

```text
REUSE
REFACTOR
REWRITE
REJECT
UNKNOWN
```

S01H zamknął później dokładny handoff źródeł. Niezależny replay potwierdził trzydzieści dziewięć plików źródłowych, jedenaście dokumentów schematów, osiemnaście ukierunkowanych testów S01, pięćset dwadzieścia sześć odzyskanych testów CMD, brak sekretów oraz brak zdolności wykonawczej.

Jednocześnie dwadzieścia cztery grupy widocznych pól pozostały `UNKNOWN`, historyczny producent screenshotów nie został pewnie zidentyfikowany, a dawne metryki zachowały status non-authoritative.

Zasada odzyskania brzmi:

> **Zachować ergonomię operatora. Każdą liczbę policzyć i zwalidować od początku.**

Pełne rozwinięcie tego etapu znajduje się w Chronicle #07: [Odzyskać ergonomię. Każdą liczbę policzyć od nowa]({{ '/2026/08/14/odzyskac-ergonomie-przeliczyc-kazda-liczbe-od-nowa/' | relative_url }}).

## Poziomy produktu

Pierwszy produkt kończy się na poziomie L2.

| Poziom | Funkcja | Status |
|---|---|---|
| L0 Observe Only | monitoring, zdrowie danych i opis stanu | dozwolony zakres |
| L1 Analysis and Ranking | typowane kandydatury i abstencja | syntetyczne lub replay |
| L2 Prepared Manual Ticket | pełny materiał do ręcznej decyzji | bez broker action |
| L3 Human Confirmed Execution | potwierdzane wykonanie | zablokowane |
| L4 Bounded Autonomy | automatyczne działanie w granicach | zablokowane |
| L5 Broader Autonomy | szersza władza systemu | zablokowane |

Poziomy nie są nazwami kolejnych wersji interfejsu. Są klasami uprawnień. L2 może przygotować kompletny Risk Ticket i nadal nie posiadać technicznej możliwości wysłania zlecenia. L3 wymagałby osobnego adaptera, tożsamości, autoryzacji, kontroli ryzyka, reconciliation, recovery i dowodów wykonania. Obecny program nie buduje tej powierzchni.

## Jeden rdzeń dla człowieka i shadow autonomy

S02 ma uniknąć częstego błędu architektonicznego, w którym wersja ręczna i automatyczna rozwijają dwa różne stosy logiki. Jeden typowany rdzeń będzie przygotowywał stan, niezawodność, okazję, decyzję i ograniczenie ryzyka. Dopiero na końcu wynik trafi do adaptera człowieka albo adaptera shadow.

Publiczny przepływ wygląda następująco:

```text
DataHealthSnapshot
MarketStateEnvelope
ForecastEnvelope
ReliabilityEnvelope
OpportunityRouter
DecisionEnvelope
Deterministic RiskGovernor
ActionPolicy
CounterfactualJournal
```

`DataHealthSnapshot` opisuje świeżość i kompletność wejścia. `ReliabilityEnvelope` może zatrzymać prognozę, jeśli jej wiarygodność pozostaje nieznana albo niewalidowana. `OpportunityRouter` nie ma prawa wypełniać rankingu kandydatami tylko dlatego, że interfejs oczekuje tabeli. Brak koniecznego składnika kończy się abstencją.

`DecisionEnvelope` przechowuje uzasadnienie, ograniczenia, czas ważności i kontekst. Deterministyczny Risk Ticket może utrzymać albo zmniejszyć dopuszczone ryzyko, ale nie zwiększyć go w kolejnych warstwach.

Human Review Adapter rejestruje `ACCEPT`, `REJECT` albo `WAIT`. Shadow Autonomy Adapter generuje własną hipotetyczną decyzję na tych samych wejściach. Oba kończą się w dzienniku. Żaden nie posiada dostępu do brokera.

<figure>
<svg viewBox="0 0 1120 560" role="img" aria-labelledby="core-title core-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="core-title">Wspólny rdzeń decyzji i dwie odnogi</title>
  <desc id="core-desc">Typowany rdzeń prowadzi do adaptera człowieka i adaptera shadow. Obie odnogi kończą się w kontrfaktycznym dzienniku, bez powierzchni wykonawczej.</desc>
  <defs><marker id="core-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="314" y="42" width="492" height="120" rx="20" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <text x="560" y="84" text-anchor="middle" font-size="21" fill="var(--ink)">SHARED DECISION CORE</text>
    <text x="560" y="119" text-anchor="middle" font-size="14" fill="var(--mut)">health, state, reliability, routing, decision, risk</text>
    <rect x="88" y="248" width="370" height="118" rx="20" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="662" y="248" width="370" height="118" rx="20" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <text x="273" y="292" text-anchor="middle" font-size="20" fill="var(--up)">HUMAN REVIEW</text>
    <text x="273" y="326" text-anchor="middle" font-size="14" fill="var(--mut)">ACCEPT / REJECT / WAIT</text>
    <text x="847" y="292" text-anchor="middle" font-size="20" fill="var(--ink)">SHADOW POLICY</text>
    <text x="847" y="326" text-anchor="middle" font-size="14" fill="var(--mut)">hypothetical decision</text>
    <rect x="314" y="430" width="492" height="92" rx="18" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <text x="560" y="468" text-anchor="middle" font-size="20" fill="var(--ink)">COUNTERFACTUAL JOURNAL</text>
    <text x="560" y="497" text-anchor="middle" font-size="14" fill="var(--mut)">shown, hidden, rejected, expired, selected</text>
    <path d="M498 162 C450 205 380 217 322 242" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#core-arrow)"/>
    <path d="M622 162 C670 205 740 217 798 242" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#core-arrow)"/>
    <path d="M273 366 C308 404 400 420 474 426" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#core-arrow)"/>
    <path d="M847 366 C812 404 720 420 646 426" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#core-arrow)"/>
    <text x="560" y="210" text-anchor="middle" font-size="15" fill="var(--dn)">NO NETWORK / NO BROKER / NO ORDER API</text>
  </g>
</svg>
<figcaption>Manualny i automatyczny tryb obserwacyjny korzystają z tego samego rdzenia. Różni je odbiorca decyzji, ale żadna odnoga nie może wykonać transakcji.</figcaption>
</figure>

## Dziennik, który mierzy model i człowieka

Zwykły dziennik transakcyjny zapisuje wykonane decyzje. Counterfactual Journal musi zapisywać również kandydatury pokazane, ukryte, odrzucone, przeterminowane i wybrane przez politykę shadow.

Dzięki temu można później odróżnić kilka efektów:

- wartość prognozy przed selekcją,
- wartość routingu okazji,
- wpływ filtra niezawodności,
- wpływ decyzji operatora,
- wpływ ograniczeń ryzyka,
- koszt opóźnienia i braku działania.

Jeżeli człowiek odrzuci dobrą kandydaturę, journal zachowa wynik kontrfaktyczny. Jeżeli system ukryje słabą kandydaturę, również pozostawi ślad. Bez takiego zapisu łatwo przypisać sukces modelowi albo człowiekowi na podstawie niewielkiej, wyselekcjonowanej części historii.

S02 nie ma jeszcze dostarczać wyników rynkowych. Ma udowodnić, że rdzeń jest deterministyczny, odporny na staleness, unknown reliability, duplikaty, wygaśnięcie, crash i restart, a ryzyko nie rośnie w kolejnych etapach.

## Autonomia jest certyfikatem, nie przełącznikiem

Przyszła zgoda nie będzie dotyczyła abstrakcyjnego systemu jako całości. Musi być indeksowana co najmniej przez model, instrument, reżim, stan danych i stan wykonania.

Model może posiadać dowody w jednym instrumencie i nie mieć ich w drugim. Może działać w określonej płynności, ale nie przy starych kwotowaniach. Może przejść OOS, lecz nie przeżyć forward albo kosztów. W takim przypadku nie istnieje ogólne `AUTONOMY = ON`.

Publiczny schemat przyszłego certyfikatu wymaga osobnych klas dowodu dla danych, czasu, OOS, holdoutu, forward, kosztów, ryzyka, wykonania i bezpieczeństwa. S02 jedynie przygotowuje format. Nie wydaje żadnego certyfikatu.

## Wartość produktu przed udowodnieniem alfy

Semi-Algo Desk może przynosić wartość operacyjną zanim jakikolwiek model otrzyma status `MODEL_EDGE_PROVEN`. Może skrócić przygotowanie, utrzymać jednolity rytuał analizy, pokazać brakujące dane, wymusić abstencję, uporządkować kandydatury i zachować dokładny stan, który widział operator.

Te korzyści nie są dowodem zyskowności. Powinny być mierzone oddzielnie: czasem analizy, kompletnością materiału, liczbą poprawnych blokad, częstotliwością unknown, jakością dziennika i odtwarzalnością decyzji.

Jeżeli A01R dopuści później pierwszy prerejestrowany eksperyment, a model przejdzie kolejne bramy, trafi do produktu posiadającego już kontrakty i historię bezpiecznego zachowania. Jeżeli model zostanie odrzucony, desk nadal pozostanie użytecznym laboratorium decyzji, które nie wymusza sygnału.

## Aktualna granica

```text
WP13 synthetic artifact = ACCEPTED
S01H immutable handoff = ACCEPTED
S01 product verdict = PARTIAL_RECOVERY_SOURCE_GAPS
S02 = AUTHORIZED FOR SYNTHETIC/REPLAY SHADOW WORK
A01 scientific state = BLOCKED
A02 model fitting = NOT AUTHORIZED
EXECUTION_CAPABILITY = false
LOADABLE = UNKNOWN
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
LIVE_TRADING_APPROVED = false
```

Semi-Algo First nie skraca drogi do autonomii. Rozdziela dwie drogi, które wcześniej były niepotrzebnie związane. Produkt może zacząć pomagać człowiekowi, podczas gdy model nadal walczy o prawo do eksperymentu, a automat uczy się działać wyłącznie w cieniu.

Autonomia nie zostanie przyznana za ambicję, atrakcyjny interfejs ani liczbę komponentów. Otrzyma ją tylko dokładny model w dokładnym środowisku, gdy przeżyje pełny łańcuch dowodowy.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje publiczne poziomy produktu, wspólny rdzeń, dziennik i model uprawnień. Nie publikuje pełnych pól schematów, formuł rankingu, wag, progów, prywatnych źródeł, danych rachunku, konfiguracji brokera ani przyszłej powierzchni wykonawczej.</div>
