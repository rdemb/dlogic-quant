---
layout: labpost
title: "Semi-Algo First. Autonomia dopiero po dowodzie"
description: "D-LOGIC rozdziela rozwój na trzy niezależne tory: wiarygodność dowodów, praktyczny produkt wspierający operatora oraz badania przewidywalności."
dek: "System może dostarczać wartość wcześniej, pozostawiając wyższe poziomy autonomii poza zakresem do czasu spełnienia odpowiednich warunków dowodowych."
date: 2026-08-13 21:00:00 +0200
category: algo
eyebrow: "D-LOGIC Strategy #01"
readingTime: 14
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC PRODUCT STRATEGY #01"
cover_title: "SEMI-ALGO FIRST"
cover_subtitle: "PRODUCT NOW / ALPHA BY RESEARCH / AUTONOMY BY EVIDENCE"
cover_kind: research
---
<div class="article-status"><span class="primary">PRODUCT STRATEGY</span><span>S01: PRODUCT RECOVERY</span><span>L0-L2 ONLY</span><span>HIGHER AUTONOMY: LOCKED</span></div>

D-LOGIC przez długi czas rozwijał się w stronę systemu, który miał kiedyś rozumieć rynek, oceniać własną wiarygodność, kontrolować ryzyko i działać bez stałej ingerencji człowieka. Każda kolejna warstwa ujawniała jednak nowy problem: poprawność danych, uczciwość czasu, koszty, odtwarzalność eksperymentu, granice zaufania, zgodność runtime'u, niezależność decyzji oraz możliwość odzyskania stanu po awarii.

Rozbudowa tych zabezpieczeń była konieczna, ale zaczęła tworzyć paradoks. Im poważniej projekt traktował autonomię, tym dalej odsuwał moment, w którym system mógł realnie pomagać operatorowi. Laboratorium stawało się coraz lepsze w udowadnianiu, czego jeszcze nie wolno uruchomić, podczas gdy część istniejącej wiedzy, narzędzi i doświadczenia nadal mogła dostarczać wartość w trybie całkowicie kontrolowanym przez człowieka.

Decyzja `Semi-Algo First` zmienia kolejność, a nie ambicję.

```text
SEMI-ALGO FIRST
AUTONOMY BY EVIDENCE
```

Pierwszym produktem operacyjnym ma być analityczny desk, który porządkuje stan rynku, wykrywa kandydatów, przygotowuje pełny materiał decyzyjny i zapisuje reakcję operatora. Wyższa autonomia pozostaje osobnym programem, uzależnionym od dowodów właściwych dla konkretnego modelu, instrumentu, horyzontu i sposobu wykonania.

## Dlaczego semi-algo nie jest krokiem wstecz

W języku marketingowym semi-algo bywa przedstawiane jako automat, którego nie udało się dokończyć. W D-LOGIC oznacza coś innego: świadomie zaprojektowany system, w którym człowiek pozostaje częścią architektury, a jego decyzje są mierzone zamiast ukrywane.

Operator może zobaczyć propozycję, odrzucić ją, poczekać, zmienić założenie albo wykonać transakcję ręcznie. System zapisuje wtedy nie tylko wynik rynku, ale także własną kandydaturę, poziom wiarygodności, warunki ryzyka, decyzję człowieka i późniejszy rezultat. Pozwala to osobno badać:

- jakość obserwacji rynku,
- jakość rankingu kandydatów,
- kalibrację wiarygodności,
- jakość przygotowanego ticketu,
- wartość decyzji człowieka,
- różnicę między wynikiem faktycznym i kontrfaktycznym.

Taki produkt może być użyteczny przed uzyskaniem prawa do automatycznej egzekucji, a jednocześnie generuje dane potrzebne do oceny, czy człowiek poprawia decyzję modelu, czy systematycznie niszczy jej wartość.

## Trzy tory, trzy różne pytania

Projekt został podzielony na niezależne ścieżki, ponieważ sukces jednej z nich nie odpowiada na pytania pozostałych.

### Evidence Plane

Ten tor bada, czy dowody są kompletne, prawidłowo nazwane, związane z konkretnymi obiektami i odtwarzalne. Odpowiada na pytanie: czy system ma prawo twierdzić, że zmierzył dokładnie to, co deklaruje?

### Product Plane

Ten tor buduje narzędzie dla operatora. Odpowiada na pytanie: czy istniejące dane, komponenty i interfejs można przekształcić w stabilny desk, który codziennie skraca drogę od obserwacji do świadomej decyzji?

### Alpha Research Plane

Ten tor bada przewidywalność. Odpowiada na pytanie: czy sygnał wnosi informację poza prostymi baseline'ami, przeżywa koszty, walidację poza próbą, kolejne reżimy i nowe obserwacje?

<figure>
<svg viewBox="0 0 1080 520" role="img" aria-labelledby="tracks-title tracks-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="tracks-title">Trzy niezależne tory rozwoju D-LOGIC</title>
  <desc id="tracks-desc">Evidence Plane, Product Plane i Alpha Research Plane biegną równolegle i spotykają się dopiero przed wyższą autonomią.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="55" y="64" width="285" height="250" rx="20" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="397" y="64" width="285" height="250" rx="20" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="739" y="64" width="285" height="250" rx="20" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <text x="197" y="108" text-anchor="middle" font-size="19" fill="var(--ink)">EVIDENCE PLANE</text>
    <text x="539" y="108" text-anchor="middle" font-size="19" fill="var(--ink)">PRODUCT PLANE</text>
    <text x="881" y="108" text-anchor="middle" font-size="19" fill="var(--ink)">ALPHA RESEARCH</text>
    <text x="197" y="158" text-anchor="middle" font-size="14" fill="var(--mut)">co zostało zmierzone</text>
    <text x="197" y="187" text-anchor="middle" font-size="14" fill="var(--mut)">jakim dowodem</text>
    <text x="197" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">z jaką kompletnością</text>
    <text x="539" y="158" text-anchor="middle" font-size="14" fill="var(--mut)">stan rynku</text>
    <text x="539" y="187" text-anchor="middle" font-size="14" fill="var(--mut)">ranking okazji</text>
    <text x="539" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">ticket dla operatora</text>
    <text x="881" y="158" text-anchor="middle" font-size="14" fill="var(--mut)">przewidywalność OOS</text>
    <text x="881" y="187" text-anchor="middle" font-size="14" fill="var(--mut)">wartość po kosztach</text>
    <text x="881" y="216" text-anchor="middle" font-size="14" fill="var(--mut)">forward survival</text>
    <line x1="197" y1="314" x2="197" y2="386" stroke="var(--acc)" stroke-width="4"/>
    <line x1="539" y1="314" x2="539" y2="386" stroke="var(--up)" stroke-width="4"/>
    <line x1="881" y1="314" x2="881" y2="386" stroke="var(--mut)" stroke-width="4"/>
    <rect x="290" y="386" width="500" height="80" rx="18" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="540" y="418" text-anchor="middle" font-size="18" fill="var(--ink)">WYŻSZA AUTONOMIA</text>
    <text x="540" y="446" text-anchor="middle" font-size="14" fill="var(--dn)">dostępna dopiero po przejściu wszystkich wymaganych bram</text>
  </g>
</svg>
<figcaption>Każdy tor może rozwijać się niezależnie, ale wyższa autonomia wymaga ich wspólnego domknięcia. Dobrze działający interfejs nie zastępuje alfy, a poprawny model nie zastępuje bezpiecznego wykonania.</figcaption>
</figure>

## Pierwsze trzy poziomy produktu

Semi-Algo Desk V2 zaczyna się od poziomów L0-L2.

| Poziom | Zakres | Odpowiedzialność człowieka |
|---|---|---|
| L0 Observe Only | monitoring, świeżość danych, stan systemu | interpretacja i brak działania |
| L1 Analysis and Ranking | ranking kandydatów i warunki odrzucenia | wybór tego, co warto zbadać |
| L2 Prepared Manual Ticket | przygotowany scenariusz, ryzyko, warunki unieważnienia | ACCEPT, REJECT albo WAIT oraz ręczne wykonanie |

L3 rozpoczynałby automatyczną egzekucję ograniczonego intentu, L4 większą autonomię modelu, a L5 pełną samodzielność. Te poziomy pozostają wyłączone. Nie odblokuje ich liczba funkcji interfejsu, szybkość działania ani atrakcyjny wynik testów syntetycznych.

## Najpierw odzyskanie, potem zaufanie

D-LOGIC posiada historyczny CMD Desk z widokami PULSE, CANDIDATES, LEVELS, MAP i FLOW. Zrzuty ekranu pokazują, że taki interfejs istniał i prezentował między innymi reżimy, siłę walut, rankingi kandydatów, hit rate, oczekiwaną wartość, bias, poziomy ryzyka, kalendarz, COT, ścieżki banków centralnych, nagłówki i korelacje.

Zrzut ekranu potwierdza jednak tylko istnienie widoku oraz wyświetlanej liczby. Nie potwierdza formuły, źródła danych, czasu dostępności, kosztów, kalibracji ani przewidywalności.

Dlatego odzyskiwane komponenty i pola otrzymują status:

```text
REUSE
REFACTOR
REWRITE
REJECT
UNKNOWN
```

Zasada produktu brzmi: zachować ergonomię operatora, ale ponownie zwalidować każdą liczbę. Element może być znakomitym rozwiązaniem interfejsowym i jednocześnie nie mieć żadnego prawa do odziedziczenia historycznej interpretacji statystycznej.

## Kontrakt decyzji zamiast pojedynczego sygnału

Sygnał `BUY` albo `SELL` jest zbyt ubogi, aby reprezentować poważną decyzję. Semi-Algo Desk ma budować typowane obiekty, które oddzielają kolejne etapy:

```text
MarketStateSnapshot
OpportunityCandidate
DecisionEnvelope
RiskTicket
HumanDecision
ManualExecutionRecord
CounterfactualOutcome
```

`MarketStateSnapshot` opisuje stan informacji w konkretnym momencie. `OpportunityCandidate` wskazuje hipotezę oraz warunki, w których ma sens. `DecisionEnvelope` niesie prognozę, wiarygodność, horyzont i powody abstencji. `RiskTicket` tłumaczy scenariusz na ograniczenia możliwe do oceny przez człowieka. `HumanDecision` zapisuje ACCEPT, REJECT albo WAIT. `ManualExecutionRecord` przechowuje to, co operator rzeczywiście zrobił, a `CounterfactualOutcome` pozwala porównać wynik działania z wynikiem niewykonanej alternatywy.

Pełne pola, wagi, progi oraz reguły routingu pozostają prywatne. Publiczny concept jest jednak czytelny: system ma tworzyć kompletny, audytowalny kontekst decyzji, nie pojedynczą komendę bez historii.

## Dwie historie każdej okazji

Po każdej kandydaturze istnieją co najmniej dwie ścieżki. Jedna pokazuje wynik rzeczywistej decyzji operatora. Druga zapisuje, co wydarzyłoby się w zdefiniowanym scenariuszu kontrfaktycznym.

<figure>
<svg viewBox="0 0 1060 460" role="img" aria-labelledby="counter-title counter-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="counter-title">Dwie historie okazji w Semi-Algo Desk</title>
  <desc id="counter-desc">Opportunity Candidate przechodzi do decyzji człowieka, a następnie rozdziela się na rzeczywisty rekord wykonania i kontrfaktyczny wynik alternatywy.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="355" y="40" width="350" height="70" rx="15" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <text x="530" y="82" text-anchor="middle" font-size="18" fill="var(--ink)">OPPORTUNITY CANDIDATE</text>
    <line x1="530" y1="110" x2="530" y2="170" stroke="var(--acc)" stroke-width="4"/>
    <rect x="355" y="170" width="350" height="70" rx="15" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="530" y="212" text-anchor="middle" font-size="18" fill="var(--ink)">HUMAN DECISION</text>
    <line x1="530" y1="240" x2="315" y2="310" stroke="var(--up)" stroke-width="4"/>
    <line x1="530" y1="240" x2="745" y2="310" stroke="var(--mut)" stroke-width="4"/>
    <rect x="90" y="310" width="390" height="92" rx="16" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="580" y="310" width="390" height="92" rx="16" fill="var(--soft)" stroke="var(--mut)" stroke-width="3"/>
    <text x="285" y="348" text-anchor="middle" font-size="17" fill="var(--ink)">MANUAL EXECUTION RECORD</text>
    <text x="285" y="377" text-anchor="middle" font-size="14" fill="var(--mut)">co operator rzeczywiście zrobił</text>
    <text x="775" y="348" text-anchor="middle" font-size="17" fill="var(--ink)">COUNTERFACTUAL OUTCOME</text>
    <text x="775" y="377" text-anchor="middle" font-size="14" fill="var(--mut)">co stało się z odrzuconą alternatywą</text>
  </g>
</svg>
<figcaption>Kontrfaktyczny dziennik pozwala oddzielić wartość modelu od wartości ingerencji człowieka. Bez tego dobry lub zły wynik końcowy łatwo przypisać niewłaściwej części procesu.</figcaption>
</figure>

## Produkt nie może udawać alfy

Atrakcyjny desk może przyspieszyć pracę, wymusić dyscyplinę i ograniczyć pomijanie informacji. Nie dowodzi jednak, że ranking kandydatów przewiduje rynek. Również świetnie zweryfikowany pakiet infrastrukturalny nie dowodzi wartości prognozy.

```text
dobry dowód != dobra prognoza
dobry interfejs != przewaga
dobra prognoza != bezpieczne wykonanie
```

Każdy tor zachowuje własne kryteria promocji. Dzięki temu produkt może rozwijać się bez pożyczania wiarygodności od warstwy dowodowej, a badania alfy nie muszą czekać, aż cały interfejs osiągnie finalną formę.

## Autonomia jako status dowodowy

W wielu systemach autonomia jest przełącznikiem. Najpierw istnieje tryb manualny, później ktoś włącza automatyzację i od tej chwili model działa sam. D-LOGIC traktuje autonomię jako wynik przypisany do konkretnego modelu, instrumentu, horyzontu i środowiska wykonania.

Model może mieć prawo do rankingu na jednym rynku i jednocześnie brak prawa do przygotowania ticketu na innym. Może przejść walidację predykcyjną, ale nie przejść kontroli kosztów. Może być ekonomicznie wartościowy, ale nie posiadać sprawdzonego recovery po awarii. W każdym z tych przypadków zakres autonomii pozostaje ograniczony.

Semi-Algo First nie rezygnuje z autonomii. Wymusza, aby została przyznana dopiero wtedy, gdy przestała być obietnicą architektoniczną, a stała się właściwością popartą odpowiednim dowodem.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje publiczne poziomy produktu, role człowieka i rozdzielenie torów. Nie publikuje pełnych cech, wag, progów, prywatnej topologii, szczegółowej logiki rankingu ani reguł wykonawczych.</div>
