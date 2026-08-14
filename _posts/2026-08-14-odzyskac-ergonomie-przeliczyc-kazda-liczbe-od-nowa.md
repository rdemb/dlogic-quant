---
layout: labpost
title: "Odzyskać ergonomię. Każdą liczbę policzyć od nowa"
description: "S01H potwierdził dokładne źródła i kontrakt odzyskanego CMD Desku, ale historyczne wskaźniki nadal nie mają prawa wrócić jako zwalidowana prawda rynkowa."
dek: "Stary interfejs może przechowywać świetne pomysły organizacyjne, a jednocześnie pokazywać liczby, których pochodzenia, czasu dostępności i znaczenia nie potrafimy już udowodnić."
date: 2026-08-14 06:30:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #07"
readingTime: 20
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #07"
cover_title: "ODZYSKAĆ DESK, NIE DZIEDZICZYĆ ILUZJI"
cover_subtitle: "S01H ACCEPTED / 24 FIELD GROUPS UNKNOWN / EXECUTION DISABLED"
cover_kind: research
---
<div class="article-status"><span class="primary">S01H ACCEPTED</span><span>PRODUCT VERDICT: PARTIAL</span><span>HISTORICAL METRICS: NON-AUTHORITATIVE</span><span>EXECUTION CAPABILITY: FALSE</span></div>

Na historycznych zrzutach D-LOGIC wyglądał jak gotowy terminal decyzyjny. Ekrany `PULSE`, `CANDIDATES`, `LEVELS`, `MAP` i `FLOW` porządkowały rynek, pokazywały kierunki, siłę walut, kandydatów, poziomy ryzyka, kalendarz, COT, ścieżki banków centralnych, nagłówki i korelacje. Wrażenie kompletności było silne, ponieważ wszystkie elementy znajdowały się w jednym miejscu i używały spójnego języka.

Zrzut ekranu potwierdza jednak tylko to, że pewna wartość została kiedyś wyświetlona. Nie potwierdza, skąd pochodziła, kiedy stała się dostępna, jak została policzona, czy nie korzystała z informacji przyszłej, czy uwzględniała koszty ani czy posiadała jakąkolwiek wartość prognostyczną.

S01 rozpoczął odzyskiwanie starego CMD Desku właśnie od tego rozróżnienia. Celem nie było przywrócenie wyglądu za wszelką cenę. Celem było ustalenie, które elementy interfejsu są wartościową ergonomią operatora, które posiadają nadal wiarygodne źródło, które wymagają napisania od nowa, a które należy odrzucić mimo atrakcyjnego wyglądu.

Pierwszy audyt S01 zakończył się częściowym werdyktem. Istnienie historycznego interfejsu było znane, ale dokładny producent części ekranów, pochodzenie wielu pól i pełne znaczenie dawnych liczb pozostawały niepewne. Następnie powstał S01H, czyli zamrożony pakiet przekazania, którego zadaniem nie było zmienianie produktu, ale udowodnienie dokładnych bajtów istniejącej implementacji.

Niezależna kontrola zaakceptowała artefakt S01H. Równocześnie utrzymała główny werdykt produktowy:

```text
S01H artifact acceptance = PASS
S01 product verdict = PARTIAL_RECOVERY_SOURCE_GAPS
```

Te dwa wyniki są zgodne. Wiemy, co dokładnie zostało dostarczone. Nadal nie wiemy, czy każda historyczna liczba zasługuje na powrót.

## Co S01H rzeczywiście udowodnił

Pakiet S01H został odtworzony bez importowania repozytorium i przy dwóch różnych wartościach `PYTHONHASHSEED`. Wynik był byte-identical, a próby uszkodzenia treści, skompresowanego payloadu oraz końca archiwum zostały odrzucone.

| Kontrola | Wynik |
|---|---:|
| Pliki źródłowe | 39 |
| Dokumenty schematów | 11 |
| Walidacje fixtures i schematów | 13 |
| Ukierunkowane testy S01 | 18 |
| Odzyskane testy CMD | 526 |
| Dopasowania do sekretów | 0 |
| Zdolność wykonawcza | 0 |
| Replay przy dwóch hash seeds | byte-identical |

Taki wynik daje mocne podstawy do niezależnego przeglądu implementacji. Można wskazać dokładne źródła, kontrakty i artefakty, które mają zostać rozwinięte w kolejnym etapie. Nie trzeba już polegać na pamięci autora ani na zrzutach ekranu jako jedynym śladzie produktu.

S01H nie potwierdził jednak pikselowej zgodności przeglądarkowego runtime'u, nie odnalazł pewnego producenta historycznych screenshotów i pozostawił dwadzieścia cztery grupy widocznych pól w stanie `UNKNOWN`. Dawne wartości `HIT%`, `EVbp`, `bias`, `regime`, `strength`, `COT`, ścieżki stóp, rankingi, poziomy SL/TP i tradability pozostają nieautorytatywne.

Właściwa zasada produktu brzmi więc:

> **Odzyskać ergonomię, ale każdą liczbę przeliczyć od nowa.**

## Pięć ekranów, pięć klas pytań

Historyczne ekrany można traktować jako mapę potrzeb operatora, nie jako zamrożony model alfy.

`PULSE` odpowiadał na pytanie o ogólny stan rynku. `CANDIDATES` miał redukować szeroki universe do krótszej listy. `LEVELS` porządkował miejsca, przy których plan mógł być aktywowany albo odrzucony. `MAP` łączył instrumenty i szersze relacje. `FLOW` próbował pokazać, co zmienia się szybciej niż zwykły wykres ceny.

Te funkcje pozostają sensowne. Każda widoczna liczba wymaga jednak przejścia pełnego łańcucha:

```text
field on screen
source bytes
availability time
transformation
validation status
consumer and decision impact
```

<figure>
<svg viewBox="0 0 1120 560" role="img" aria-labelledby="field-chain-title field-chain-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="field-chain-title">Łańcuch dopuszczenia pola do Semi-Algo Desk</title>
  <desc id="field-chain-desc">Pole widoczne na ekranie musi prowadzić do źródła, czasu dostępności, formuły, walidacji i sposobu użycia. Brak któregokolwiek elementu pozostawia status UNKNOWN.</desc>
  <defs><marker id="field-chain-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="35" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="215" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="395" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="575" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="755" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="935" y="116" width="150" height="100" rx="14" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="110" y="156" text-anchor="middle" font-size="16" fill="var(--ink)">FIELD</text><text x="110" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">ekran</text>
    <text x="290" y="156" text-anchor="middle" font-size="16" fill="var(--ink)">SOURCE</text><text x="290" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">dane</text>
    <text x="470" y="156" text-anchor="middle" font-size="16" fill="var(--ink)">TIME</text><text x="470" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">available_at</text>
    <text x="650" y="156" text-anchor="middle" font-size="16" fill="var(--ink)">FORMULA</text><text x="650" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">transformacja</text>
    <text x="830" y="156" text-anchor="middle" font-size="16" fill="var(--ink)">VALIDATE</text><text x="830" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">testy i koszty</text>
    <text x="1010" y="156" text-anchor="middle" font-size="16" fill="var(--up)">ADMIT</text><text x="1010" y="184" text-anchor="middle" font-size="13" fill="var(--mut)">jawny status</text>
    <path d="M185 166 H209 M365 166 H389 M545 166 H569 M725 166 H749 M905 166 H929" stroke="var(--acc)" stroke-width="3" marker-end="url(#field-chain-arrow)"/>
    <rect x="305" y="340" width="510" height="112" rx="18" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="560" y="382" text-anchor="middle" font-size="19" fill="var(--dn)">BRAK ŹRÓDŁA, CZASU LUB WALIDACJI</text>
    <text x="560" y="418" text-anchor="middle" font-size="16" fill="var(--ink)">UNKNOWN, REWRITE albo REJECT</text>
    <path d="M560 216 V334" stroke="var(--dn)" stroke-width="3" stroke-dasharray="8 7" marker-end="url(#field-chain-arrow)"/>
  </g>
</svg>
<figcaption>Zrzut ekranu jest początkiem śledztwa, nie końcem walidacji. Pole wraca do produktu dopiero po związaniu z danymi, czasem, metodą i statusem.</figcaption>
</figure>

## Klasyfikacja odzyskanego systemu

Każdy komponent i każde pole otrzymuje jedną z pięciu etykiet:

```text
REUSE
REFACTOR
REWRITE
REJECT
UNKNOWN
```

`REUSE` nie oznacza, że moduł jest idealny. Oznacza, że jego odpowiedzialność, źródło i zachowanie są wystarczająco zrozumiałe, aby zachować go bez zmiany sensu. `REFACTOR` pozwala poprawić strukturę bez dziedziczenia starej tezy. `REWRITE` zachowuje potrzebę operatora, ale odrzuca poprzednią implementację. `REJECT` usuwa element niespójny, niebezpieczny albo pozbawiony mechanizmu. `UNKNOWN` blokuje decyzję do czasu pozyskania nowych danych.

Ta klasyfikacja ma większą wartość niż proste przepisywanie starego kodu. Historyczny system mógł zawierać świetne skróty operatorskie obok wskaźników, których znaczenie zostało utracone. Traktowanie całego produktu jako jednego artefaktu zmuszałoby do wyboru między całkowitym odrzuceniem i bezkrytycznym odziedziczeniem. Rejestr pozwala zachować to, co użyteczne, bez przemycania starych twierdzeń.

## Jeden rdzeń dla człowieka i przyszłej autonomii

Po akceptacji S01H program podjął decyzję o budowie S02. Nie będzie to drugi, niezależny system automatyczny działający obok wersji semi-algo. Ma powstać jeden wspólny, typowany rdzeń decyzyjny, który obsłuży ręczny przegląd operatora oraz tryb shadow autonomy.

Publiczny przepływ ma postać:

```text
DataHealthSnapshot
MarketStateEnvelope
ForecastEnvelope
ReliabilityEnvelope
OpportunityRouter
DecisionEnvelope
Deterministic RiskTicket
ActionPolicy
Journal
```

Na tym etapie prognozy pochodzą wyłącznie z fixtures syntetycznych albo zamrożonych replayów. Brak zwalidowanej niezawodności blokuje ranking i kończy się `ABSTAIN` lub `BLOCKED_NO_VALIDATED_FORECAST`. Kandydat nie może przejść dalej dlatego, że interfejs potrzebuje wypełnić pustą tabelę.

Human Review Adapter zapisuje `ACCEPT`, `REJECT` albo `WAIT`, ale nie posiada dostępu do brokera. Shadow Autonomy Adapter wykonuje tę samą ocenę hipotetycznie i zapisuje ją do dziennika. Oba adaptery pracują na tych samych kontraktach, dlatego później można porównać decyzję człowieka z decyzją polityki bez utrzymywania dwóch różnych stosów logiki.

<figure>
<svg viewBox="0 0 1120 560" role="img" aria-labelledby="shared-core-title shared-core-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="shared-core-title">Wspólny rdzeń S02 dla operatora i shadow autonomy</title>
  <desc id="shared-core-desc">Jeden typowany rdzeń przygotowuje decyzję i ticket. Dwie odnogi prowadzą do adaptera człowieka oraz adaptera shadow, a obie kończą się w dzienniku bez dostępu do brokera.</desc>
  <defs><marker id="shared-core-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="328" y="48" width="464" height="116" rx="20" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <text x="560" y="88" text-anchor="middle" font-size="21" fill="var(--ink)">SHARED DECISION CORE</text>
    <text x="560" y="122" text-anchor="middle" font-size="14" fill="var(--mut)">state, reliability, routing, envelope, risk</text>
    <rect x="104" y="250" width="350" height="116" rx="20" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="666" y="250" width="350" height="116" rx="20" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <text x="279" y="292" text-anchor="middle" font-size="20" fill="var(--up)">HUMAN REVIEW</text>
    <text x="279" y="326" text-anchor="middle" font-size="14" fill="var(--mut)">ACCEPT / REJECT / WAIT</text>
    <text x="841" y="292" text-anchor="middle" font-size="20" fill="var(--ink)">SHADOW POLICY</text>
    <text x="841" y="326" text-anchor="middle" font-size="14" fill="var(--mut)">hypothetical only</text>
    <rect x="328" y="426" width="464" height="90" rx="18" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <text x="560" y="462" text-anchor="middle" font-size="20" fill="var(--ink)">COUNTERFACTUAL JOURNAL</text>
    <text x="560" y="491" text-anchor="middle" font-size="14" fill="var(--mut)">shown, hidden, rejected, expired, selected</text>
    <path d="M500 164 C466 207 390 214 330 244" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#shared-core-arrow)"/>
    <path d="M620 164 C654 207 730 214 790 244" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#shared-core-arrow)"/>
    <path d="M279 366 C300 405 384 420 454 424" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#shared-core-arrow)"/>
    <path d="M841 366 C820 405 736 420 666 424" stroke="var(--acc)" stroke-width="3" fill="none" marker-end="url(#shared-core-arrow)"/>
    <text x="560" y="214" text-anchor="middle" font-size="15" fill="var(--dn)">NO BROKER ADAPTER / NO ORDER API</text>
  </g>
</svg>
<figcaption>Tryb semi-algo i tryb shadow korzystają z tej samej logiki. Różni je odbiorca decyzji, ale żadna odnoga nie posiada powierzchni wykonawczej.</figcaption>
</figure>

## Shadow autonomy bez prawa do zlecenia

Zwiększenie uwagi poświęconej automatyzacji nie oznacza otwarcia drogi do `order_send`. S02 może obserwować, klasyfikować, oceniać niezawodność, porządkować okazje, przygotowywać deterministyczny Risk Ticket i zapisywać hipotetyczną decyzję. Nie może nawiązać kontaktu z brokerem, używać write-capable MT5, aktywować usług ani przejść do poziomów L3-L5.

Takie rozwiązanie pozwala budować automatyczną maszynę wcześniej, bez udawania, że posiada już prawo do działania. Polityka może zostać przetestowana pod kątem deterministyczności, monotoniczności ryzyka, wygaśnięcia, staleness, idempotency, odzyskiwania dziennika i reakcji na nieznaną niezawodność. Każda hipotetyczna akcja kończy się w journalu.

Dopiero przyszły certyfikat uprawnienia, zależny od konkretnego modelu, instrumentu, reżimu, stanu danych i stanu wykonania, mógłby w odleglejszej przyszłości zmienić zakres. S02 nie wydaje takiego certyfikatu.

## Wartość produktu przed udowodnieniem alfy

Desk może być użyteczny zanim jakikolwiek model otrzyma status `MODEL_EDGE_PROVEN`. Może utrzymywać jednolity rytuał przygotowania, odsłaniać braki danych, blokować kandydatury przy nieznanej niezawodności, zapisywać decyzje operatora i porównywać je z decyzją shadow policy.

Taka wartość nie jest tym samym co zyskowność. Powinna być mierzona osobno: czasem analizy, kompletnością materiału, częstotliwością abstencji, zgodnością danych, liczbą blokad przed decyzją, jakością dziennika i możliwością odtworzenia tego, co operator rzeczywiście widział.

Jeżeli później pojawi się model z dodatnią wartością po kosztach, będzie trafiał do produktu posiadającego już kontrakty i historię zachowania. Jeżeli model nie przejdzie badań, desk nadal może pełnić funkcję kontrolowanego laboratorium decyzji bez wymuszania sygnału.

## Co wolno powiedzieć po S01H

Publiczny status wygląda następująco:

```text
S01H immutable handoff = ACCEPTED
S01 exact source bytes = KNOWN
S01 historical interface existence = KNOWN
S01 historical screenshot producer = UNKNOWN
S01 24 visible field groups = UNKNOWN
S01 historical metrics = NON-AUTHORITATIVE
S02 shared core = AUTHORIZED FOR SYNTHETIC/REPLAY SHADOW WORK
EXECUTION_CAPABILITY = false
LIVE_TRADING_APPROVED = false
```

S01H nie udowodnił, że dawny desk przewidywał rynek. Udowodnił coś wcześniejszego i koniecznego: znamy dokładny materiał, z którego można uczciwie budować następcę.

Odzyskany interfejs nie będzie muzeum dawnych wyników. Ma stać się miejscem, w którym każda liczba posiada źródło, czas, formułę, status i możliwość odrzucenia. Ergonomia może wrócić szybko. Autorytet liczb musi zostać zbudowany od początku.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> artykuł opisuje publiczne widoki produktu, klasyfikację komponentów, kontrakty i model shadow autonomy. Nie publikuje pełnych pól schematów, wag rankingu, progów, prywatnych źródeł, danych rachunku, przyszłego certyfikatu autonomii ani mechaniki brokera.</div>
