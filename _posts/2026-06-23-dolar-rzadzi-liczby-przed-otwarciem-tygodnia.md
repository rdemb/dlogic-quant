---
title: "Dolar znów rządzi. Anatomia reżimu mocnego dolara"
description: "EUR/USD 1.1470, DXY ponad 100, CPI 4.2%. Rozkładam reżim mocnego dolara na czynniki pierwsze: z-score siły walut, czynnik dolara (PCA 69%, R² 0.83), percentyl ATR i variance-ratio, krzywą i realne stopy. Same liczby, policzone z danych."
date: 2026-06-23 08:00:00 +0200
dek: "Dolar jest najmocniejszy od roku, a rynek przyjmuje to spokojnie. Rozkładam to na mechanikę: siła walut, czynnik dolara, zmienność, krzywa i realne stopy. Wszystko policzone z danych."
readingTime: 9
tags: [EUR/USD, dolar, DXY, PCA, ATR, carry, reżim rynku, analiza makro, Forex]
image: /assets/og.png
cover: strength
---

> **W skrócie**
>
> - W skali tygodnia prowadzi dolar: **+106 bp** na koszyku G8, najwięcej z całej ósemki. W ujęciu jednodniowym najmocniej odbijają funt (z **+1.52**) i jen (**+0.98**). To krótkoterminowy hałas na tle trendu.
> - **EUR/USD 1.1470.** Pierwsza składowa par dolarowych tłumaczy **69%** ich wspólnej wariancji, a EUR/USD jest w **83%** pochodną tego czynnika. Handel na tej parze to w 83% handel dolarem.
> - Reżim zmienności normalny: ATR(14) w **52. percentylu**, dzienna realizacja 30 pip to połowa średniej (**RV/ATR = 0.51**). Rynek oddycha wolniej.
> - Krzywa **2s10s +30 bp**, nieodwrócona, więc sygnał recesyjny milczy. Realne stopy **+0.3%**, carry **+137.5 bp**. Wszystko po stronie dolara.

**Teza w jednym zdaniu:** dopóki realne stopy są dodatnie, krzywa się nie odwraca, a VIX siedzi przy 17, mocny dolar pozostaje stanem spoczynku rynku, a nie wyjątkiem do tłumaczenia.

## Siła walut: kto naprawdę prowadzi

Siłę liczę z całej macierzy 28 krzyżów G8, nie z pojedynczej pary. Dla każdej waluty biorę jej średni zwrot względem pozostałych siedmiu i standaryzuję wynik: `z = (r − μ) / σ`. Suma ośmiu z-score'ów wychodzi zero. To gra o sumie zerowej. Żeby ktoś urósł, ktoś inny musi oddać.

Tu robi się ciekawie. W ujęciu jednodniowym prowadzi funt (+1.52) i jen (+0.98), a dolar jest dopiero trzeci (+0.59). Rozszerz okno do pięciu dni, a obraz się odwraca: dolar +106 bp na czele, funt −76 bp przy dnie. Te same waluty wyglądają inaczej w zależności od skali. Funt nadrabia jedną sesję, dolar trzyma kierunek przez cały tydzień. Krótkoterminowy powrót do średniej nie kasuje średnioterminowego pływu.

| Waluta | z (1D) | Σ 5D (bps) | Jak to czytać |
|---|---|---|---|
| GBP | +1.52 | −76 | odbicie w spadku |
| JPY | +0.98 | +29 | cichy bezpieczny port |
| USD | +0.59 | +106 | trend tygodnia |
| EUR | +0.52 | −25 | słabość względna |
| CAD | −0.45 | −87 | pod presją surowców |
| AUD | −0.47 | +18 | mieszany sygnał |
| NZD | −1.17 | −125 | najsłabszy w koszyku |
| CHF | −1.52 | −96 | oddaje najwięcej |

<figure>
<svg viewBox="0 0 640 244" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><line x1="170" y1="12" x2="170" y2="236" stroke="#e6e6e6" stroke-dasharray="3 4"/><text x="170" y="9" font-size="10" fill="#9b9b9b" text-anchor="middle">-1σ</text><line x1="320" y1="12" x2="320" y2="236" stroke="#e6e6e6"/><text x="320" y="9" font-size="10" fill="#9b9b9b" text-anchor="middle">0</text><line x1="470" y1="12" x2="470" y2="236" stroke="#e6e6e6" stroke-dasharray="3 4"/><text x="470" y="9" font-size="10" fill="#9b9b9b" text-anchor="middle">+1σ</text><rect x="320" y="18" width="228" height="14" rx="3" fill="#1a9e6a"/><text x="8" y="29" font-size="12" fill="#1a1a1a">GBP</text><text x="554" y="29" font-size="11" fill="#6b6b6b" text-anchor="start" font-family="monospace">+1.52</text><text x="632" y="29" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D -76</text><rect x="320" y="46" width="147" height="14" rx="3" fill="#1a9e6a"/><text x="8" y="57" font-size="12" fill="#1a1a1a">JPY</text><text x="473" y="57" font-size="11" fill="#6b6b6b" text-anchor="start" font-family="monospace">+0.98</text><text x="632" y="57" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D +29</text><rect x="320" y="74" width="88" height="14" rx="3" fill="#1a9e6a"/><text x="8" y="85" font-size="12" fill="#1a1a1a">USD</text><text x="414" y="85" font-size="11" fill="#6b6b6b" text-anchor="start" font-family="monospace">+0.59</text><text x="632" y="85" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D +106</text><rect x="320" y="102" width="78" height="14" rx="3" fill="#1a9e6a"/><text x="8" y="113" font-size="12" fill="#1a1a1a">EUR</text><text x="404" y="113" font-size="11" fill="#6b6b6b" text-anchor="start" font-family="monospace">+0.52</text><text x="632" y="113" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D -25</text><rect x="252" y="130" width="68" height="14" rx="3" fill="#d64545"/><text x="8" y="141" font-size="12" fill="#1a1a1a">CAD</text><text x="246" y="141" font-size="11" fill="#6b6b6b" text-anchor="end" font-family="monospace">-0.45</text><text x="632" y="141" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D -87</text><rect x="250" y="158" width="70" height="14" rx="3" fill="#d64545"/><text x="8" y="169" font-size="12" fill="#1a1a1a">AUD</text><text x="244" y="169" font-size="11" fill="#6b6b6b" text-anchor="end" font-family="monospace">-0.47</text><text x="632" y="169" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D +18</text><rect x="144" y="186" width="176" height="14" rx="3" fill="#d64545"/><text x="8" y="197" font-size="12" fill="#1a1a1a">NZD</text><text x="138" y="197" font-size="11" fill="#6b6b6b" text-anchor="end" font-family="monospace">-1.17</text><text x="632" y="197" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D -125</text><rect x="92" y="214" width="228" height="14" rx="3" fill="#d64545"/><text x="8" y="225" font-size="12" fill="#1a1a1a">CHF</text><text x="86" y="225" font-size="11" fill="#6b6b6b" text-anchor="end" font-family="monospace">-1.52</text><text x="632" y="225" font-size="10" fill="#9b9b9b" text-anchor="end" font-family="monospace">5D -96</text></svg>
<figcaption>Siła walut G8 w ujęciu jednodniowym (z-score). Zielony to waluta mocniejsza od koszyka, czerwony słabsza. Po prawej skumulowana zmiana 5D w bps.</figcaption>
</figure>

## EUR/USD to w 83% historia dolara

Pary dolarowe nie poruszają się niezależnie. Rozkładam ich wspólną kowariancję na składowe główne i pierwsza z nich tłumaczy **69%** całej wariancji. Po ludzku: istnieje jeden wspólny pływ, czynnik dolara, który rządzi większością ruchu w koszyku.

Nakładam na ten czynnik EUR/USD. Współczynnik determinacji wynosi `R² = 0.83`. Zostaje raptem 17% zmienności pary na czystą historię euro. Konsekwencja jest twarda: kto analizuje EUR/USD bez dolara, czyta co drugą stronę książki. Dopóki czynnik dolara jest mocny, byczy scenariusz na euro potrzebuje albo własnego paliwa, albo cierpliwości, aż dolar odpuści.

<figure>
<svg viewBox="0 0 640 196" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="40" y="28" font-size="13" fill="#1a1a1a">Wspólny czynnik dolara (PC1): udział w wariancji par USD</text><rect x="40" y="40" width="560" height="14" rx="7" fill="#ececec"/><rect x="40" y="40" width="386" height="14" rx="7" fill="#0b66c3"/><text x="434" y="51" font-size="12" fill="#0b66c3" font-family="monospace">69%</text><text x="40" y="96" font-size="13" fill="#1a1a1a">EUR/USD: dekompozycja wariancji (R² do czynnika dolara)</text><rect x="40" y="108" width="465" height="22" rx="4" fill="#0b66c3"/><rect x="505" y="108" width="95" height="22" rx="4" fill="#9bbce0"/><text x="272" y="123" font-size="12" fill="#ffffff" text-anchor="middle">83% dolar</text><text x="552" y="123" font-size="11" fill="#14416f" text-anchor="middle">17%</text><text x="40" y="170" font-size="12" fill="#6b6b6b">Carry: Fed 3.625% − EBC 2.25% = +137.5 bp na korzyść dolara</text></svg>
<figcaption>Dekompozycja wariancji. Jeden wspólny czynnik dolara rządzi koszykiem, a EUR/USD jest w 83 procentach jego pochodną.</figcaption>
</figure>

## Zmienność: rynek oddycha wolniej niż zwykle

ATR(14) wynosi 59 pip i siedzi w 52. percentylu własnego rozkładu, czyli dokładnie w środku. Dzienna realizacja to 30 pip, połowa normy, więc `RV/ATR = 0.51`. To czysta kompresja.

Druga warstwa jest ciekawsza. W błądzeniu losowym zakres rośnie z pierwiastkiem czasu, więc pięć dni powinno dać około `59 × √5 ≈ 132 pip`. Rynek zrobił 204. Iloraz **1.54** to variance-ratio powyżej jedności, sygnatura trwałości kierunku. Niska zmienność dzienna i ponadnormatywny zakres tygodniowy składają się na ciche, uporządkowane zsuwanie z trendem. Taki reżim premiuje kierunek i karze łapanie dołków.

<figure>
<svg viewBox="0 0 640 224" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="40" y="26" font-size="13" fill="#1a1a1a">Reżim zmienności: percentyl ATR(14)</text><rect x="40" y="38" width="560" height="12" rx="6" fill="#ececec"/><rect x="40" y="38" width="291" height="12" rx="6" fill="#0b66c3"/><line x1="331" y1="32" x2="331" y2="56" stroke="#1a1a1a" stroke-width="2"/><text x="331" y="70" font-size="11" fill="#1a1a1a" text-anchor="middle" font-family="monospace">52 (NORMAL)</text><text x="40" y="70" font-size="10" fill="#9b9b9b">0</text><text x="600" y="70" font-size="10" fill="#9b9b9b" text-anchor="end">100</text><rect x="166" y="108" width="307" height="26" rx="4" fill="#f6f8fb" stroke="#9bbce0"/><line x1="320" y1="100" x2="320" y2="142" stroke="#1a1a1a"/><text x="320" y="96" font-size="12" fill="#1a1a1a" text-anchor="middle" font-family="monospace">1.1470</text><text x="320" y="160" font-size="11" fill="#6b6b6b" text-anchor="middle">±ATR(14) = ±59 pip → 1.1410–1.1529</text><text x="320" y="190" font-size="11" fill="#6b6b6b" text-anchor="middle">RV(1d) = 30 pip · RV/ATR = 0.51 → kompresja</text><text x="320" y="210" font-size="11" fill="#6b6b6b" text-anchor="middle">Zakres 5D = 204 pip vs ATR·√5 = 132 → 1.54× → trend, nie błądzenie</text></svg>
<figcaption>Reżim zmienności EUR/USD: percentyl ATR, koperta ±ATR oraz variance-ratio z pięciu sesji.</figcaption>
</figure>

## Łańcuch makro: od CPI do EUR/USD

Mechanikę da się prześledzić ogniwo po ogniwie. Inflacja w USA wróciła do 4.2%, lepka i napędzana energią. Przy takim odczycie Fed nie ma miejsca na cięcia i trzyma stopy w przedziale 3.50–3.75% jastrzębim tonem. Wysoka stopa nominalna ponad inflacją daje dodatnią realną rentowność, +0.3% na dziesięciolatce. Do tego dochodzi dysparytet wobec EBC: Fed 3.625% przy EBC 2.25% daje **+137.5 bp carry** po stronie dolara. Dodatnie realne stopy i carry działają jak magnes na kapitał. Stąd DXY ponad 100 i EUR/USD spychany w dół.

Dwa bezpieczniki potwierdzają, że mówimy o reżimie, a nie o panice. Krzywa 2s10s ma +30 bp i się nie odwraca, więc klasyczny sygnał recesyjny milczy. VIX przy 17.3 oznacza spokój. Mocny dolar przy nieodwróconej krzywej i niskim VIX zwykle daje handel w zakresie: silny kierunek bez gwałtowności.

| Wskaźnik | Wartość | Implikacja |
|---|---|---|
| CPI USA | 4.2% | lepka inflacja, Fed bez cięć |
| Fed | 3.50–3.75% (mid 3.625) | hold jastrzębi |
| EBC | 2.25% | pierwsza podwyżka od 2023 |
| Carry Fed–EBC | +137.5 bp | na korzyść USD |
| Realna 10Y | +0.3% | magnes na kapitał |
| Krzywa 2s10s | +30 bp | brak inwersji |
| VIX | 17.28 | reżim spokoju |
| Złoto 5D | −1.24% | spójne z realnymi stopami |
| DXY | ponad 100 | potwierdzenie trendu |

<figure>
<svg viewBox="0 0 640 320" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#6b6b6b" stroke-width="1.5"/></marker></defs><rect x="40" y="14" width="300" height="38" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="54" y="31" font-size="12" fill="#1a1a1a">Inflacja: CPI 4.2%</text><text x="54" y="45" font-size="10" fill="#6b6b6b">lepka: ogranicza Fed</text><rect x="40" y="66" width="300" height="38" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="54" y="83" font-size="12" fill="#1a1a1a">Fed: hold 3.50–3.75%</text><text x="54" y="97" font-size="10" fill="#6b6b6b">ton jastrzębi (17.06)</text><rect x="40" y="118" width="300" height="38" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="54" y="135" font-size="12" fill="#1a1a1a">Realne stopy +0.3% · carry +137.5 bp</text><text x="54" y="149" font-size="10" fill="#6b6b6b">magnes na kapitał</text><rect x="40" y="170" width="300" height="38" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="54" y="187" font-size="12" fill="#1a1a1a">Napływ kapitału → DXY > 100</text><text x="54" y="201" font-size="10" fill="#6b6b6b">dolar mocny w koszyku</text><rect x="40" y="222" width="300" height="38" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="54" y="239" font-size="12" fill="#1a1a1a">EUR/USD: bias bearish</text><text x="54" y="253" font-size="10" fill="#6b6b6b">w 83% pochodna dolara</text><line x1="190" y1="52" x2="190" y2="66" stroke="#6b6b6b" marker-end="url(#ar)"/><line x1="190" y1="104" x2="190" y2="118" stroke="#6b6b6b" marker-end="url(#ar)"/><line x1="190" y1="156" x2="190" y2="170" stroke="#6b6b6b" marker-end="url(#ar)"/><line x1="190" y1="208" x2="190" y2="222" stroke="#6b6b6b" marker-end="url(#ar)"/><rect x="400" y="92" width="220" height="34" rx="8" fill="#ffffff" stroke="#e6e6e6"/><text x="414" y="109" font-size="12" fill="#1a1a1a">Krzywa 2s10s +30 bp</text><text x="414" y="123" font-size="10" fill="#6b6b6b">brak inwersji</text><rect x="400" y="174" width="220" height="34" rx="8" fill="#ffffff" stroke="#e6e6e6"/><text x="414" y="191" font-size="12" fill="#1a1a1a">VIX 17.3</text><text x="414" y="205" font-size="10" fill="#6b6b6b">reżim spokoju</text><rect x="40" y="276" width="580" height="34" rx="8" fill="#eef4fb" stroke="#e6e6e6"/><text x="54" y="293" font-size="12" fill="#1a1a1a">Reżim dnia: mocny USD, handel w zakresie</text><line x1="190" y1="260" x2="190" y2="276" stroke="#6b6b6b" marker-end="url(#ar)"/><line x1="510" y1="126" x2="470" y2="276" stroke="#9bbce0" stroke-dasharray="4 4"/><line x1="510" y1="208" x2="500" y2="276" stroke="#9bbce0" stroke-dasharray="4 4"/></svg>
<figcaption>Łańcuch transmisji makro: od lepkiej inflacji po bearish bias na EUR/USD, z krzywą i VIX jako bezpiecznikami reżimu.</figcaption>
</figure>

## Dwa scenariusze i ich wyzwalacze

Nie prognozuję ceny. Opisuję reżim i to, co musiałoby pęknąć, żeby się zmienił.

**Bazowy, kontynuacja.** Dopóki krzywa się nie odwraca, a realne stopy są dodatnie, próby trwałego osłabienia dolara wyglądają raczej na okazję do jego odkupienia niż na początek zwrotu. Rynek oddycha między poziomami.

**Warunkowy, złamanie schematu.** Układ zmieniłby jeden z trzech wyzwalaczy: gołębi zwrot Fedu, nagła inwersja krzywej albo skok VIX powyżej 25. Każdy uderza w inny filar reżimu. Ten scenariusz uzbraja się dopiero wtedy, gdy któryś trigger faktycznie się odpali.

<figure>
<svg viewBox="0 0 640 210" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ar2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#6b6b6b" stroke-width="1.5"/></marker></defs><rect x="20" y="80" width="180" height="52" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="34" y="100" font-size="12.5" fill="#1a1a1a">Reżim: mocny USD</text><text x="34" y="118" font-size="10.5" fill="#6b6b6b">handel w zakresie</text><rect x="300" y="22" width="320" height="64" rx="8" fill="#f6f8fb" stroke="#e6e6e6"/><text x="314" y="42" font-size="12.5" fill="#1a1a1a">Scenariusz bazowy</text><text x="314" y="60" font-size="10.5" fill="#6b6b6b">Krzywa nieodwrócona, realne stopy > 0.</text><text x="314" y="76" font-size="10.5" fill="#6b6b6b">Spadki USD = okazja do odkupu.</text><rect x="300" y="120" width="320" height="72" rx="8" fill="#fbf2ee" stroke="#e6e6e6"/><text x="314" y="140" font-size="12.5" fill="#1a1a1a">Scenariusz warunkowy</text><text x="314" y="158" font-size="10.5" fill="#6b6b6b">Trigger: gołębi Fed · inwersja · VIX > 25</text><text x="314" y="174" font-size="10.5" fill="#6b6b6b">Wtedy miejsce na korektę dolara.</text><path d="M200 100 H250 V54 H300" fill="none" stroke="#6b6b6b" marker-end="url(#ar2)"/><path d="M200 112 H250 V156 H300" fill="none" stroke="#6b6b6b" marker-end="url(#ar2)"/></svg>
<figcaption>Scenariusze i ich wyzwalacze. Bazowy to kontynuacja reżimu, warunkowy uzbraja się dopiero po triggerze.</figcaption>
</figure>

## Jak to liczę

Cztery moduły, wszystkie z publicznych danych.

- **Siła walut.** Z-score średnich zwrotów z macierzy krzyżowej G8 o sumie zerowej.
- **Czynnik dolara.** PCA na zwrotach par USD, udział PC1 w wariancji i `R²` pary do tego czynnika.
- **Reżim zmienności.** Percentyl ATR(14) oraz variance-ratio, czyli zakres 5D do `ATR·√5`.
- **Reżim makro.** Reguły na realnych stopach, nachyleniu krzywej i carry.

```
# 1. Sila walut (z-score, suma zerowa)
for ccy in G8:
    r[ccy] = mean(ret(ccy / other) for other in G8 if other != ccy)
z = (r - mean(r)) / std(r)                        # Suma z = 0

# 2. Czynnik dolara (PCA na parach USD)
pc1_var   = eig(cov(returns_usd_pairs))[0] / total_var    # = 0.69
r2_eurusd = corr(eurusd, pc1) ** 2                         # = 0.83

# 3. Rezim zmiennosci
atr_pctile     = percentile_rank(ATR14, lookback=252)      # = 52
variance_ratio = range_5d / (ATR14 * sqrt(5))              # = 1.54

# 4. Rezim makro (reguly, nie predykcja)
real_10y = us_10y - cpi_proxy        # +0.3
slope    = us_10y - us_2y            # +30 bp
carry    = fed_mid - ecb_rate        # +137.5 bp
usd_bias = "strong" if (real_10y > 0 and slope > 0 and carry > 0) else "mixed"
```

Dane: pary M5 do D1 z własnego eksportu (stan rynku 2026-06-19), makro z publicznych źródeł (TradingEconomics, FRED, Investing, stan 2026-06-23). Liczby przeliczam przy każdym raporcie.

To kontekst i prawdopodobieństwa, nie sygnał wejścia. Pokazuję, co prowadzi rynek i co musiałoby się stać, żeby teza przestała działać. Decyzję podejmujesz sam. To nie porada inwestycyjna.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
