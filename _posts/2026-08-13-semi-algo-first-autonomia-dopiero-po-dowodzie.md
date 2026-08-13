---
layout: labpost
title: "Semi-Algo First. Autonomia dopiero po dowodzie"
description: "D-LOGIC rozdziela rozwój na trzy niezależne tory: wiarygodność dowodów, praktyczny produkt wspierający operatora oraz badania przewidywalności."
dek: "System może dostarczać wartość wcześniej, pozostawiając wyższe poziomy autonomii poza zakresem do czasu spełnienia odpowiednich warunków dowodowych."
date: 2026-08-13 21:00:00 +0200
category: algo
eyebrow: "D-LOGIC Strategy #01"
readingTime: 5
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC PRODUCT STRATEGY #01"
cover_title: "SEMI-ALGO FIRST"
cover_subtitle: "PRODUCT NOW / ALPHA BY RESEARCH / AUTONOMY BY EVIDENCE"
cover_kind: research
---
<div class="article-status"><span class="primary">PRODUCT STRATEGY</span><span>S01: AUTHORIZED / DESIGN</span><span>L0-L2 ONLY</span><span>HIGHER AUTONOMY: LOCKED</span></div>

D-LOGIC rozwijał przez kolejne etapy warstwę dowodową przyszłego środowiska. Ta praca pozostaje konieczna, ale nie powinna blokować budowy narzędzia, które już wcześniej porządkuje obserwacje, przygotowuje analizy i wspiera decyzje operatora.

Nowa zasada programu brzmi:

```text
SEMI-ALGO FIRST
AUTONOMY BY EVIDENCE
```

## Trzy niezależne tory

### Evidence Plane: WP13

Ten tor odpowiada za jakość, kompletność i odtwarzalność dowodów. Nie ocenia wartości produktu ani przewidywalności.

### Product Plane: S01

Ten tor odzyskuje historyczny CMD Desk, ocenia jego komponenty i zamraża kontrakt Semi-Algo Desk V2. Pierwsza wersja ma obserwować, porządkować i przygotowywać materiał decyzyjny.

### Alpha Research Plane: A01

Ten tor bada, czy wykryta struktura utrzymuje się poza procesem dopasowania, przeżywa proste alternatywy i zachowuje wartość w nowych obserwacjach.

Każdy tor odpowiada na inne pytanie. Żaden nie może zastąpić pozostałych.

## Człowiek pozostaje częścią systemu

Pierwszy produkt nie próbuje usuwać operatora z pętli. Przeciwnie, zapisuje przygotowaną kandydaturę, decyzję człowieka i późniejszy wynik. Dzięki temu można osobno oceniać jakość modelu, selekcji oraz samego procesu decyzyjnego.

## Zakres pierwszej wersji

S01 obejmuje trzy poziomy:

| Poziom | Zakres |
|---|---|
| **L0 Observe Only** | monitoring i opis stanu |
| **L1 Analysis and Ranking** | porządkowanie kandydatów |
| **L2 Prepared Manual Ticket** | kompletny pakiet do decyzji operatora |

Wyższe poziomy pozostają poza zakresem. Nie zostaną odblokowane przez sam rozwój interfejsu ani większą liczbę modeli.

## Najpierw audyt, potem przebudowa

Historyczne komponenty otrzymają status `REUSE`, `REFACTOR`, `REWRITE`, `REJECT` albo `UNKNOWN`. Każde pole interfejsu musi mieć znane źródło, czas dostępności, sposób obliczenia i status walidacji.

Publiczny concept obejmuje kontrakty takie jak `MarketStateSnapshot`, `OpportunityCandidate`, `DecisionEnvelope`, `RiskTicket`, `HumanDecision`, `ManualExecutionRecord` i `CounterfactualOutcome`. Pełne pola, wagi i progi pozostają prywatne.

## Produkt nie może udawać alfy

Dobry interfejs może uporządkować pracę, ale nie stanowi dowodu przewidywalności. Podobnie mocna warstwa dowodowa nie zastępuje badań nad wartością modelu.

```text
dobry dowód != dobra prognoza
dobry interfejs != przewaga
```

Semi-Algo First ustawia właściwą kolejność: najpierw użyteczne wsparcie człowieka, potem pomiar jakości modelu i procesu, a autonomia dopiero po dowodzie.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje publiczne poziomy produktu i rozdzielenie torów. Nie publikuje pełnych cech, wag, progów, prywatnej topologii ani szczegółowej logiki systemu.</div>
