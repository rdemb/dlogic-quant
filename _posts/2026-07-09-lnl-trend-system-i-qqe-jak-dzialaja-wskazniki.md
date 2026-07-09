---
title: "Pod maską: L&L Trend System i QQE. Co naprawdę liczą dwa wskaźniki"
description: "Dokładny rozbiór dwóch popularnych wskaźników z TradingView. L&L Trend System (EMA 13, stop line na ATR, DMI/ADX) i QQE (wygładzony RSI, trailing na zmienności RSI, Fibonacci 4,236). Mechanika i matematyka po ludzku."
date: 2026-07-09 12:00:00 +0200
eyebrow: "Edukacja · wskaźniki"
category: edukacja
dek: "Większość ludzi patrzy na kolor wskaźnika i klika. Ja lubię wiedzieć, co liczy każda linia. Rozkładam dwa narzędzia, które łączę na MT5: L&L Trend System i QQE. Trochę matematyki, ale wszystko po ludzku."
readingTime: 9
tags: ["L&L Trend System", QQE, RSI, ATR, EMA, DMI, ADX, analiza techniczna, wskaźniki, TradingView, momentum, trend, Forex]
---

> **W skrócie**
>
> - **L&L Trend System** (autor: L&L Capital) to system trendowy zbudowany na zmienności. Linia z 13 świec jako trend, druga linia odsunięta o porcję ATR jako reżim i trailing. Przełącza kierunek dopiero po przebiciu z zapasem, nie przy każdym drgnięciu.
> - **QQE** (autor: Kivanc Ozbilgic) to wygładzony RSI z drugą linią, która działa jak trailing liczony na zmienności samego RSI, mnożonej przez stałą Fibonacciego **4,236**. Sygnał to przecięcie linii szybkiej z wolną.
> - **Hybryda.** QQE mówi KIEDY, bo łapie moment przyspieszenia. L&L mówi W KTÓRĄ STRONĘ, bo daje reżim i kierunek. Wejście bierzemy pod uwagę tylko przy zgodzie obu.
> - **Największa wartość jest w rozjeździe.** Gdy oba narzędzia się kłócą, to czerwona lampka, filtr chaosu. Dobry wskaźnik równie często mówi, żeby siedzieć na rękach.

**Teza w jednym zdaniu:** dobry wskaźnik nie obiecuje zysku, tylko porządkuje to, co i tak masz na wykresie, a te dwa robią to dwuwarstwowo, jeden liczy reżim na zmienności ceny, drugi momentum na zmienności RSI.

## L&L Trend System: reżim zbudowany na zmienności

Autorem jest L&L Capital. To system trendowy oparty na zmienności, a nie na samej cenie. Ma jeden cel: pokazać reżim rynku i dać oddychającą linię wyjścia.

**Linia trendu** to wykładnicza średnia z 13 świec. EMA różni się od zwykłej średniej tym, że świeższym świecom nadaje większą wagę.

```
EMA(t) = α · cena(t) + (1 − α) · EMA(t−1),   α = 2 / (n + 1)
dla n = 13:  α ≈ 0,143
```

**Stop line to serce systemu.** To nie zwykła średnia, tylko linia odsunięta od trendu o porcję zmienności. Najpierw liczymy zasięg świecy, czyli True Range, potem wygładzamy go krótką EMA i skalujemy trybem.

```
TR = max( high − low,  |high − close(t−1)|,  |low − close(t−1)| )
ATR_L&L = (Tryb / 100) · EMA(TR, 8)
Tryb:  Tight 60 · Normal 80 · Loose 100 · FOMC 120 · Net 140
```

Teraz definicja reżimu. Oznaczmy stan jako T.

```
close > Trend + ATR_L&L   →   T = +1   (reżim długi)
close < Trend − ATR_L&L   →   T = −1   (reżim krótki)
w innym wypadku           →   T = T(t−1)   (bez zmiany)

linia rysowana po przeciwnej stronie ceny:
stop = Trend − ATR_L&L   gdy T = +1
stop = Trend + ATR_L&L   gdy T = −1
```

Zwróć uwagę na trzeci warunek. Reżim nie zmienia się przy każdym drgnięciu, cena musi przebić pasmo z zapasem. To celowe. W spokoju linia siedzi blisko ceny, w rozchwianiu odsuwa się, żeby nie wyrzucało Cię przy szumie. To jest ta oddychająca dyscyplina wyjścia.

**Kolor trendu** L&L bierze z ułożenia czterech średnich ważonych wolumenem, czyli VWMA.

```
VWMA(n) = Σ(cena · wolumen) / Σ(wolumen),  po ostatnich n świecach
ułożenie bycze:     VWMA8 > VWMA13 > VWMA21 > VWMA34
ułożenie niedźwiedzie:  odwrotna kolejność
```

**Siła trendu** to klasyka Wildera, DMI i ADX. Odpowiada na pytanie, czy w ogóle jest trend, niezależnie od kierunku.

```
+DI = 100 · RMA(+DM, 14) / RMA(TR, 14)
−DI = 100 · RMA(−DM, 14) / RMA(TR, 14)
DX  = 100 · |+DI − −DI| / (+DI + −DI)
ADX = RMA(DX, 14)              RMA = wygładzanie Wildera, α = 1/n
```

Reguła jest prosta. Gdy ADX przekracza 20, jest trend, a jego kierunek wyznacza to, czy +DI jest nad −DI. Poniżej 20 rynek dryfuje. L&L koloruje tym świece: zielone w byczym trendzie z siłą, czerwone w niedźwiedzim, neutralne w dryfie.

L&L jednym zdaniem: linia z 13 świec mówi gdzie jesteśmy, stop line z ATR pilnuje reżimu i daje trailing, VWMA i ADX potwierdzają, czy ten reżim ma poparcie.

## QQE: momentum na zmienności RSI

Autorem jest Kivanc Ozbilgic. Nazwa to Quantitative Qualitative Estimation. To oscylator momentum, który bierze RSI i porządkuje go tak, żeby wyciąć większość szumu.

**Baza to RSI** liczony na 14 świecach.

```
RSI = 100 − 100 / (1 + RS),   RS = RMA(przyrosty) / RMA(spadki)
```

**Pierwsze wygładzenie.** Goły RSI drga, więc QQE nakłada na niego krótką EMA i tworzy linię szybką.

```
QQEF = EMA(RSI, 5)
```

**Druga warstwa to ATR na RSI** i tu jest cały pomysł. QQE liczy zmienność samego RSI, podwójnym wygładzeniem Wildera.

```
TR_rsi = |QQEF(t) − QQEF(t−1)|
WWMA   = α · TR_rsi + (1 − α) · WWMA(t−1)
ATRRSI = α · WWMA   + (1 − α) · ATRRSI(t−1)      α = 1/14
```

**Pasma i linia wolna.** Wokół linii szybkiej budujemy kanał, mnożąc zmienność RSI przez stałą Fibonacciego 4,236. Linia wolna QQES to trailing, który działa dokładnie jak SuperTrend, tylko przeniesiony na RSI.

```
QUP = QQEF + 4,236 · ATRRSI
QDN = QQEF − 4,236 · ATRRSI

QQES = QUP,  gdy QUP < QQES(t−1)
QQES = QDN,  gdy QQEF przebija QQES od dołu
QQES = QDN,  gdy QDN > QQES(t−1)
QQES = QUP,  gdy QQEF przebija QQES od góry
QQES = QQES(t−1)  w innym wypadku
```

**Sygnał** pada, gdy linia szybka przecina wolną. W górę to impuls kupujących, w dół sprzedających. Poziom 50 pełni rolę osi, bo to środek skali RSI. Mnożnik 4,236 nie jest przypadkowy, to rozszerzenie Fibonacciego, które ustawia szerokość kanału tak, żeby reagował na realne zmiany momentum, a nie na drobne falowanie.

QQE jednym zdaniem: to RSI wygładzony EMA, opleciony własnym trailingiem liczonym na zmienności RSI, który daje czyste momenty przecięć zamiast drgającego oscylatora.

## Hybryda: po co je łączyć

Oba wskaźniki mówią o czym innym i to jest powód. QQE odpowiada na pytanie KIEDY, bo łapie moment przyspieszenia momentum. L&L odpowiada na pytanie W KTÓRĄ STRONĘ, bo daje reżim i kierunek z całą oprawą zmienności. Osobno każdy zostawia Cię z połową obrazu.

Reguła składania jest jednozdaniowa. Impuls QQE bierzemy pod uwagę tylko wtedy, gdy zgadza się z reżimem L&L.

```
wejście długie:   QQEF przecina QQES w górę   ORAZ   T = +1
wejście krótkie:  QQEF przecina QQES w dół     ORAZ   T = −1
reżimy sprzeczne: brak akcji
```

I tu jest najważniejsza część, wcale nie tam, gdzie większość szuka. Najcenniejsze są momenty, gdy oba narzędzia się kłócą. Przecięcie QQE w górę przy reżimie spadkowym L&L to nie okazja, to czerwona lampka. Confluence działa więc głównie jako filtr chaosu, który mówi, kiedy nie wchodzić.

## Jak tego używam i jaka jest wartość

Zbudowałem z tego panel na MT5: reżim L&L, stan QQE, siła trendu z ADX i moment zgody w jednym miejscu, z twardą linią wyjścia z ATR. Traktuję go jako kontekst do własnych, ręcznych decyzji i jako dyscyplinę, a nie jako automat, który ma myśleć za mnie.

Bo tak trzeba to ustawić w głowie. Żaden wskaźnik nie jest wyrocznią i żaden nie zwalnia z zarządzania ryzykiem. To jest obraz rynku policzony w konkretny sposób, który ma pomóc podejmować spokojniejsze decyzje i rzadziej wchodzić w bałagan. Wielkość pozycji, moment wyjścia i cierpliwość dalej są po Twojej stronie. Wartość dobrego wskaźnika nie polega na tym, że coś obieca, tylko na tym, że uporządkuje to, co i tak masz na wykresie.

To nie jest porada inwestycyjna. Pokazuję mechanikę i matematykę narzędzi, których sam używam, żebyś rozumiał, co dokładnie liczy każda linia, zanim oprzesz na niej decyzję.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
