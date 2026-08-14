---
layout: labpost
title: "Trzy blokady, które zadziałały. System nadal nie ma prawa ruszyć"
description: "Audit 19 zaakceptował trzy dokładne artefakty, ale każdy z nich zatrzymał kolejny krok: holdout bez udowodnionej custody, pomiar brokera bez autoryzowanej ścieżki i warstwę bezpieczeństwa bez przypiętego zewnętrznego testu RED."
dek: "Dojrzałość systemu nie objawiła się tym, że trzy odpowiedzi zmieniły się na PASS. Objawiła się tym, że trzy niezależne ścieżki potrafiły powiedzieć: tym bajtom ufamy, ale następnego działania nadal nie wolno wykonać."
date: 2026-08-14 12:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #09"
readingTime: 18
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #09"
cover_title: "TRZY BLOKADY, KTÓRE ZADZIAŁAŁY"
cover_subtitle: "A01HR TIME-ANCHORED / A01DM NO MEASUREMENT / S02G LOCKDOWN"
cover_kind: evidence
---
<div class="article-status"><span class="primary">AUDIT 19 REVIEWED</span><span>A01C / A02 / S03: NOT AUTHORIZED</span><span>BROKER MEASUREMENT: FALSE</span><span>LIVE: FALSE</span></div>

W dobrym systemie badawczym blokada nie jest awarią. Awarią jest dopiero sytuacja, w której system nie potrafi zatrzymać działania mimo braku dowodu.

Najnowszy niezależny przegląd D-LOGIC objął trzy równoległe tory: władzę nad prospective holdoutem, przygotowanie pierwszego ograniczonego pomiaru brokera oraz warstwę bezpieczeństwa przyszłej automatyzacji. Każdy tor dostarczył artefakt, który można było odtworzyć, ponownie uwierzytelnić i poddać próbom uszkodzenia. Żaden nie otrzymał jednak prawa do wykonania kolejnego, bardziej ryzykownego kroku.

To nie jest sprzeczność.

Można zaakceptować dokładne bajty i jednocześnie odrzucić wniosek, który ktoś próbuje z nich wyprowadzić. Można potwierdzić, że polityka holdoutu została zamrożona przed rozpoczęciem obserwacji, ale nadal nie mieć dowodu, że nikt nie będzie mógł czytać wyników. Można zaakceptować preflight pomiaru i jednocześnie nie wykonać ani jednego zapytania do brokera. Można odtworzyć systemowe odmowy procesu oraz sieci i nadal nie uznać firewalla za zamknięty, jeżeli brakuje niezależnego obiektu RED.

Audit 19 zakończył się właśnie takim potrójnym werdyktem:

| Tor | Co zaakceptowano | Co nadal blokuje następny krok |
|---|---|---|
| A01HR | dokładną prospective policy oraz zewnętrzny znacznik czasu jej istnienia | brak operacyjnej custody, osobnego podmiotu bezpieczeństwa i wymuszonej ścieżki bez odczytu |
| A01DM | uczciwy artefakt preflight, który niczego nie zmierzył | brak zatwierdzonej, związanej z konkretnym workerem autoryzacji pomiaru |
| S02G | lockdown core i świeży replay odmów procesu oraz sieci | brak przypiętego, niezależnego obiektu RED w autorytecie verifiera |

Najbardziej wartościowy wynik brzmi więc mało widowiskowo:

```text
exact artifacts accepted
next actions denied
```

## Jeden PASS nie może awansować całego programu

W D-LOGIC coraz większą rolę odgrywa rozdzielenie czterech pytań:

```text
Czy plik jest dokładnie tym plikiem?
Czy verifier sprawdza właściwe znaczenie?
Czy warunki operacyjne są naprawdę wymuszone?
Czy wolno wykonać następny krok?
```

Pierwsze pytanie dotyczy tożsamości artefaktu. Drugie dotyczy semantyki dowodu. Trzecie obejmuje realne uprawnienia, środowisko i zachowanie runtime'u. Czwarte jest decyzją programu badawczego.

Wiele systemów łączy te poziomy w jeden zielony znacznik. Jeżeli archiwum przechodzi test integralności, dashboard pokazuje `READY`. Jeżeli preflight nie zgłasza błędu, uruchamiany jest pomiar. Jeżeli sandbox odmówił kilku wywołań, warstwa bezpieczeństwa otrzymuje status zamkniętej.

Audit 19 utrzymał te poziomy osobno.

<figure>
<svg viewBox="0 0 1120 560" role="img" aria-labelledby="audit19-gates-title audit19-gates-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="audit19-gates-title">Trzy tory Audit 19 i ich blokady</title>
  <desc id="audit19-gates-desc">A01HR, A01DM i S02G posiadają zaakceptowane artefakty, ale każdy tor kończy się osobną czerwoną bramą przed dalszym działaniem.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="45" y="70" width="310" height="360" rx="22" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <rect x="405" y="70" width="310" height="360" rx="22" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <rect x="765" y="70" width="310" height="360" rx="22" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>

    <text x="200" y="120" text-anchor="middle" font-size="24" fill="var(--acc)">A01HR</text>
    <text x="560" y="120" text-anchor="middle" font-size="24" fill="var(--acc)">A01DM</text>
    <text x="920" y="120" text-anchor="middle" font-size="24" fill="var(--acc)">S02G</text>

    <text x="200" y="165" text-anchor="middle" font-size="15" fill="var(--ink)">POLICY BYTES</text>
    <text x="200" y="194" text-anchor="middle" font-size="14" fill="var(--up)">ACCEPTED</text>
    <line x1="200" y1="220" x2="200" y2="285" stroke="var(--line)" stroke-width="8"/>
    <rect x="88" y="285" width="224" height="82" rx="14" fill="none" stroke="var(--dn)" stroke-width="4"/>
    <text x="200" y="319" text-anchor="middle" font-size="14" fill="var(--dn)">CUSTODY</text>
    <text x="200" y="343" text-anchor="middle" font-size="13" fill="var(--mut)">NOT PROVEN</text>

    <text x="560" y="165" text-anchor="middle" font-size="15" fill="var(--ink)">PREFLIGHT</text>
    <text x="560" y="194" text-anchor="middle" font-size="14" fill="var(--up)">ACCEPTED</text>
    <line x1="560" y1="220" x2="560" y2="285" stroke="var(--line)" stroke-width="8"/>
    <rect x="448" y="285" width="224" height="82" rx="14" fill="none" stroke="var(--dn)" stroke-width="4"/>
    <text x="560" y="319" text-anchor="middle" font-size="14" fill="var(--dn)">MEASUREMENT</text>
    <text x="560" y="343" text-anchor="middle" font-size="13" fill="var(--mut)">NOT AUTHORIZED</text>

    <text x="920" y="165" text-anchor="middle" font-size="15" fill="var(--ink)">LOCKDOWN CORE</text>
    <text x="920" y="194" text-anchor="middle" font-size="14" fill="var(--up)">ACCEPTED</text>
    <line x1="920" y1="220" x2="920" y2="285" stroke="var(--line)" stroke-width="8"/>
    <rect x="808" y="285" width="224" height="82" rx="14" fill="none" stroke="var(--dn)" stroke-width="4"/>
    <text x="920" y="319" text-anchor="middle" font-size="14" fill="var(--dn)">RED AUTHORITY</text>
    <text x="920" y="343" text-anchor="middle" font-size="13" fill="var(--mut)">NOT CLOSED</text>

    <text x="560" y="492" text-anchor="middle" font-size="17" fill="var(--ink)">ACCEPTED ARTIFACT DOES NOT IMPLY PERMISSION TO ACT</text>
  </g>
</svg>
<figcaption>Każdy tor ma własny obiekt, własną semantykę i własne kryterium promocji.</figcaption>
</figure>

## A01HR: polityka powstała przed obserwacją, ale custody nie wynika z daty

Pierwszy tor dotyczy outer holdoutu, czyli zbioru, który powinien pozostać poza procesem dostrajania decyzji badawczych. Jeżeli jego wyniki są dostępne przed zakończeniem eksperymentu, holdout przestaje być niezależnym sprawdzianem. Staje się kolejnym źródłem informacji, do którego projekt może dopasowywać się świadomie albo pośrednio.

A01HR wycofał wcześniejszego, niejednoznacznego kandydata i zamroził dokładną politykę prospective holdoutu. Zewnętrzny znacznik czasu dostawcy obiektu potwierdził, że konkretne bajty istniały przed pierwszym zaplanowanym oknem. Polityka obejmuje pierwszych dwadzieścia zaplanowanych sesji roboczych UTC od 18 sierpnia 2026. W chwili zamrożenia liczba obiektów wynikowych oraz odczytów wynosiła zero.

To jest realny postęp. Nie wystarcza jednak do stwierdzenia, że custody jest gotowa.

Znacznik czasu potwierdza istnienie pliku. Nie tworzy osobnego podmiotu bezpieczeństwa. Nie wymusza write-only ingestion. Nie zapewnia append-only access history. Nie blokuje operatorowi późniejszego odczytu wyników.

Red-team pokazał dodatkowo, że ogólny verifier opierał się na czasie zadeklarowanym wewnątrz artefaktu. Spójnie przebudowana wersja mogła przesunąć deklarowaną datę wstecz, przeliczyć zależne pola i nadal otrzymać pełny werdykt pozytywny. Verifier potwierdzał wewnętrzną zgodność chronologii, ale nie posiadał samodzielnego, zaufanego zegara.

Dlatego należy odróżnić dwa zdania:

```text
Te dokładne bajty istniały przed aktywacją.
```

oraz:

```text
Przyszłe wyniki są technicznie odseparowane i nie mogą zostać odczytane.
```

Pierwsze zostało zaakceptowane dla A01HR. Drugie pozostaje nieudowodnione.

Następny tor A01HC ma zbudować operacyjną custody: związać zewnętrzny czas, obiekt dostawcy, rozdzielenie ról, historię dostępu i brak zdolności odczytu. Dopiero potem można wrócić do pytania o prawo uruchomienia A01C. A02 oraz model fitting nadal są wyłączone.

## A01DM: prawidłowy pomiar, który nie wykonał żadnego pomiaru

Drugi tor przygotowuje ograniczone rozpoznanie fizyki rachunku i instrumentu. Ustalony graf dotyczy `EURUSD.pro`, maksymalnie sześćdziesięciu obserwacji oraz sześćdziesięciu sekund. Brzmi to jak niewielki, read-only eksperyment.

Niewielki zakres nie usuwa jednak problemu autoryzacji.

Dostarczony worker nie posiadał zatwierdzonej ścieżki wykonania. Nie powstał łańcuch request-response, snapshot brokera, próbka spreadu, kalkulacja margin lub PnL, ocena jakości danych ani zamrożony wynik pilota. Artefakt zakończył pracę statusem:

```text
BLOCKED_A01DM_CAPABILITY_PREFLIGHT
measurement_executed = false
```

Taki wynik jest poprawny. Preflight nie powinien udawać pomiaru tylko dlatego, że znamy przyszły symbol, limit czasu i maksymalną liczbę obserwacji.

Przed pierwszym kontaktem read-only potrzebne są trzy związania:

1. dokładna tożsamość workera, który został przeskanowany,
2. dokładny graf akcji, który może zostać wykonany,
3. autoryzacja operatora związana hashem z tym samym żądaniem.

Jeżeli skanowany kod, importowany kod i wywoływany obiekt mogą się różnić, kontrola bezpieczeństwa sprawdza jedną rzecz, a runtime wykonuje inną. Jeżeli autoryzacja mówi jedynie „pomiar brokera”, nie ogranicza symbolu, operacji, czasu ani liczby odpowiedzi.

A01DMP ma przygotować właśnie tę zamkniętą powierzchnię. Nadal nie jest to pozwolenie na pomiar. Jest to kandydat preflight do niezależnego przeglądu.

## S02G: odmowa systemu działa, ale historia RED musi być częścią dowodu

Trzeci tor dotyczy wspólnego rdzenia przyszłego Semi-Algo i shadow autonomy. Jego podstawowy stan pozostaje absorpcyjnym `LOCKDOWN`. W świeżym replayu system ponownie potwierdził:

```text
mode = LOCKDOWN
execution_capability = false
network_capability = false
```

Verifier uruchomił rzeczywisty harness odmów zamiast ufać zapisanym wcześniej deklaracjom. Próby uzyskania zdolności procesu, egzekucji oraz sieci zostały zablokowane. To ważniejszy dowód niż receipt mówiący, że blokada kiedyś zadziałała.

S02G nadal nie mógł jednak zamknąć zewnętrznego autorytetu bezpieczeństwa. Historyczny artefakt RED, który pokazywał wyjście poza dozwolony katalog, był znany przez hash i opis, ale dokładne bajty nie były dostępne do niezależnego replayu.

Brakujący kształt dowodu został odtworzony od nowa. Nowy zewnętrzny test użył wyłącznie nazw wywołań dozwolonych przez poprzednią politykę, a mimo tego zapisał plik przez absolutną ścieżkę poza zarządzanym katalogiem dziennika. Poprzedni verifier zaakceptował pakiet. Semantyka S02G poprawnie rozpoznała naruszenie jako:

```text
PATH_ABSOLUTE_FORBIDDEN
```

To pokazuje, dlaczego lista dozwolonych nazw funkcji nie jest jeszcze firewallem możliwości. Trzeba kontrolować także argumenty, ścieżki, rzeczywisty cel wywołania, niezmienność bindingów oraz pełną powierzchnię kodu wykonywalnego.

S02G2 może przypiąć nowy obiekt RED jako zewnętrzny autorytet. Musi jednak zachować wszystkie dotychczasowe testy capability, powierzchni zarządzanej, argumentów, ścieżek oraz runtime denial. S03 pozostaje niedozwolony.

## Integralność archiwum nie zastępuje odtworzenia środowiska

Wszystkie trzy dostarczone archiwa miały bezpieczną topologię, bez linków, urządzeń oraz ścieżek wychodzących poza paczkę. Ich wyniki verifierów były byte-identical przy dwóch różnych ustawieniach hash seed. Odwrócenie bitu, obcięcie danych oraz dopisanie trailera gzip kończyły się blokadą.

| Artefakt | Elementy archiwum | Zwykłe pliki | Wynik integralności |
|---|---:|---:|---|
| A01HR | 196 | 189 | deterministyczny replay i fail-closed mutations |
| A01DM | 50 | 33 | deterministyczny replay i fail-closed mutations |
| S02G | 77 | 61 | deterministyczny replay i fail-closed mutations |

To daje mocny dowód dotyczący dostarczonych pakietów. Nie odtwarza jednak całego aktywnego repozytorium VPS, środowiska Wine i MT5, rachunku ani historii brokera.

W materiałach źródłowych znajdują się również raportowane liczby testów z pełnego repozytorium. Audit 19 nie mógł ich niezależnie powtórzyć z samych przekazanych archiwów, więc pozostają uwierzytelnionymi twierdzeniami źródłowymi, a nie wynikiem odtworzonym przez zewnętrzny replay. Publiczny tekst nie powinien zacierać tej różnicy.

## Dlaczego trzy blokady są postępem

Projekt tradingowy bardzo łatwo nagradza ruch. Każde kolejne uruchomienie daje wykres, log, tabelę albo nowy wynik. System kontroli musi natomiast nagradzać brak ruchu wtedy, gdy dowód jest niepełny.

Audit 19 potwierdził trzy praktyczne właściwości:

- polityka może zostać zamrożona bez udawania, że zamrożono już custody,
- preflight może zakończyć się poprawnie bez kontaktu z brokerem,
- lockdown może odtworzyć realne odmowy i nadal żądać kompletnego obiektu RED.

Żaden z tych wyników nie tworzy alfy. Każdy zmniejsza jednak ryzyko, że przyszły wynik zostanie uznany za prawdziwy na podstawie niepełnej historii.

Obecna granica pozostaje jednoznaczna:

```text
A01C_AUTHORIZED = false
A02_AUTHORIZED = false
S03_AUTHORIZED = false
BROKER_MEASUREMENT_AUTHORIZED = false
SAFE_TO_INSTALL = false
SAFE_TO_EXECUTE = false
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
LIVE_TRADING_APPROVED = false
```

Następne autoryzowane prace to A01HC, A01DMP oraz S02G2. Każda ma zakończyć się osobnym, niezmiennym handoffem i kolejnym niezależnym raw-archive review. Plan następnego pakietu nie jest jeszcze wynikiem i nie będzie opisywany jak ukończony milestone.

To właśnie odróżnia kronikę procesu od kroniki sukcesów.

<section class="ip-boundary">
  <h2>Granica dowodu</h2>
  <p>Tekst opiera się na niezależnym Audit Reconciliation 19 z 14 sierpnia 2026 oraz dokładnych powierzchniach przekazanych archiwów. Publiczna wersja pomija prywatne ścieżki, topologię środowiska, pełny kod, parametry i reguły wykonawcze. Akceptacja artefaktu nie oznacza walidacji danych, przewagi modelu ani gotowości LIVE.</p>
</section>
