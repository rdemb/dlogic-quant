---
title: "Backtest w Pythonie: wektorowy szkielet"
description: "Wektorowy backtest to pięć kroków: ceny, sygnał, pozycja przesunięta o jeden bar, zwroty pozycji i krzywa kapitału. Kluczowa linia to pozycja = sygnał.shift(1), bo sygnał z zamknięcia bara realizuje się najwcześniej na kolejnym barze, a jej brak to zaglądanie w przyszłość. Pełny szkielet w pandas i numpy, cztery metryki ze wzorami oraz lista tego, czego taki backtest nie mówi: brak kolejki zleceń, poślizgu i sizingu."
date: 2026-07-11 13:00:00 +0200
eyebrow: "Programowanie · backtest"
dek: "Kilkanaście linii w pandas wystarczy, żeby zamienić ceny w krzywą kapitału. Ten sam kod, napisany bez jednego przesunięcia, po cichu zagląda w przyszłość i produkuje wynik, którego nie da się powtórzyć na żywo. Szkielet rozłożony linia po linii: gdzie siedzi przesunięcie o bar, gdzie wchodzą koszty i dlaczego dodatni wynik brutto najczęściej znika po ich odjęciu."
readingTime: 8
tags: [backtest, programowanie, Python, pandas, numpy, Sharpe, "koszty transakcyjne", "look-ahead", "krzywa kapitału", "maksymalne obsunięcie", walidacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Wektorowy backtest liczy całą strategię naraz, bez pętli po świecach: ceny zamieniają się w sygnał, sygnał w pozycję, pozycja w zwroty, a zwroty w krzywą kapitału. Całość mieści się w kilkunastu liniach pandas i numpy.
> - Jedna linia rozstrzyga o uczciwości testu: `pozycja = sygnał.shift(1)`. Sygnał policzony z zamknięcia bara t wchodzi w rynek najwcześniej na barze t+1. Bez tego przesunięcia pozycja reaguje na cenę, która w chwili decyzji jeszcze nie zapadła, czyli zagląda w przyszłość (Chan, 2013).
> - Koszt transakcyjny nalicza się przy każdej zmianie pozycji, nie na każdym barze. Odstęp między krzywą brutto a netto bywa przepaścią: dodatni wynik brutto najczęściej znika po odjęciu spreadu i prowizji.
> - Cztery liczby streszczają wynik: zwrot skumulowany, zmienność, Sharpe w skali roku i maksymalne obsunięcie. Annualizacja przez pierwiastek z liczby barów zakłada niezależność zwrotów, więc przy autokorelacji zawyża Sharpe (Bailey i López de Prado, 2014; Lo, 2002).
> - To szkielet edukacyjny, nie dowód zyskowności. Nie modeluje kolejki zleceń, poślizgu, częściowych wypełnień ani sizingu. Pokazuje mechanikę przepływu danych, nie przewagę.

**Teza w jednym zdaniu:** wektorowy backtest składa się w kilkunastu liniach pandas, ale jego wynik znaczy cokolwiek dopiero po spełnieniu dwóch warunków, pozycja przesunięta o jeden bar względem sygnału oraz koszt odjęty przy każdej zmianie pozycji; bez nich mierzy się artefakt, nie strategię.

## Pięć kroków, jeden łańcuch

Wektorowy znaczy tu tyle, że nie ma pętli po kolejnych świecach. Zamiast iterować bar po barze, operuje się na całych kolumnach naraz, a biblioteka liczy je hurtem. Przepływ danych ma pięć etapów i każdy z nich to jedna operacja na serii:

```
ceny  →  sygnał (−1/0/1)  →  pozycja = sygnał.shift(1)  →  zwrot pozycji  →  krzywa kapitału
```

Ceny to zwykle kolumna zamknięć. Sygnał to reguła, która każdej świecy przypisuje kierunek: wartość dodatnią dla pozycji długiej, zero dla braku pozycji, wartość ujemną dla krótkiej. Pozycja to sygnał przesunięty o jeden bar do przodu, o czym za chwilę. Zwrot pozycji to iloczyn pozycji i zwrotu rynku na danym barze. Krzywa kapitału to skumulowany iloczyn tych zwrotów. Cała mechanika opiera się na trzech funkcjach pandas, opisanych w jej dokumentacji: `rolling` liczy średnie kroczące, `shift` przesuwa serię o zadaną liczbę barów, a `cumprod` daje skumulowany iloczyn potrzebny do krzywej kapitału.

## Przesunięcie o jeden bar, czyli cała uczciwość testu

Najważniejsza linia całego szkieletu wygląda niewinnie: `pozycja = sygnał.shift(1)`. Powód jest twardy. Sygnał z przecięcia średnich liczony jest z ceny zamknięcia bara t, więc jest znany dopiero w chwili, gdy ten bar się domyka. Najwcześniejszy moment, w którym można na niego zareagować realnym zleceniem, to następny bar, t+1. Jeśli pozycję zestawi się z sygnałem bez przesunięcia, backtest zarobi zwrot z tej samej świecy, która dopiero wygenerowała sygnał, a tego na żywo zrobić się nie da. To klasyczne zaglądanie w przyszłość, jeden z najczęstszych i najkosztowniejszych błędów backtestu (Chan, 2013).

Różnica to jeden znak w kodzie, a w wynikach przepaść:

```
# ZLE: pozycja reaguje na sygnal z tego samego bara (look-ahead)
zwrot_bledny = sygnal * zwrot_ceny

# DOBRZE: pozycja z bara t+1 reaguje na sygnal znany na koncu bara t
zwrot_uczciwy = sygnal.shift(1) * zwrot_ceny
```

Wersja błędna potrafi zamienić strategię bez żadnej przewagi w krzywą kapitału pięknie rosnącą pod trzydzieści stopni, bo model kupuje dokładnie te świece, o których z góry wie, że wzrosną. Po dodaniu `shift(1)` ta sama strategia zwykle traci większość rzekomego zysku. Reguła jest prosta: cokolwiek wchodzi do pozycji, musi być znane najpóźniej na zamknięciu poprzedniego bara.

## Koszty: brutto kontra netto

Zwrot brutto to iloczyn pozycji i zwrotu rynku. Zwrot netto to brutto minus koszt, a koszt nalicza się nie na każdym barze, tylko wtedy, gdy pozycja się zmienia: przy wejściu, wyjściu i odwróceniu. Zmianę wykrywa `pozycja.diff().abs()`, a jej wielkość mnoży się przez koszt jednostkowy wyrażony w punktach (spread plus prowizja), przeliczony na ułamek ceny.

```
zmiana = pozycja.diff().abs()          # 1 przy wejsciu/wyjsciu, 2 przy odwroceniu
koszt  = zmiana * koszt_pip * pip / cena
zwrot_netto = zwrot_brutto − koszt
```

Odwrócenie pozycji z krótkiej na długą kosztuje podwójnie, bo to dwie transakcje naraz. Ta jedna poprawka bywa granicą między strategią, która wygląda na dochodową, a taką, która oddaje wszystko brokerowi. Regułą kciuka dla większości prostych strategii intraday jest, że dodatni wynik brutto najczęściej znika po odjęciu realnych kosztów, bo przewaga na sygnał jest mniejsza niż spread, który trzeba zapłacić, żeby ją zrealizować.

## Cztery metryki

Krzywą kapitału streszcza się kilkoma liczbami. Cztery wystarczą, żeby nie oceniać strategii na oko:

```
zwrot skumulowany = equity[-1] / equity[0] − 1
zmiennosc (rok)   = std(zwroty) · sqrt(barow_w_roku)
Sharpe (rok)      = mean(zwroty) / std(zwroty) · sqrt(barow_w_roku)
max drawdown      = min( equity / cummax(equity) − 1 )
```

Zwrot skumulowany to końcowa wartość kapitału względem startu. Zmienność to odchylenie standardowe zwrotów przeskalowane na rok. Sharpe to średni zwrot podzielony przez odchylenie, również w skali roku, przy założeniu zerowej stopy wolnej od ryzyka. Maksymalne obsunięcie to najgłębszy spadek kapitału od dotychczasowego szczytu, czyli miara najgorszego przeżytego spadku.

Annualizacja przez mnożnik pierwiastek z liczby barów ma cichy warunek: zwroty muszą być niezależne i o stałej wariancji. Gdy są autoskorelowane albo próba jest krótka, mnożnik zawyża Sharpe, a sam wskaźnik z małej liczby obserwacji obarczony jest dużą niepewnością (Bailey i López de Prado, 2014). Andrew Lo (2002) pokazał, że przy dodatniej autokorelacji standardowa annualizacja potrafi zawyżyć Sharpe o kilkadziesiąt procent. Innymi słowy, sama liczba Sharpe bez informacji o długości próby i kształcie rozkładu jest wartością bez jednostki.

## Kompletny szkielet

Poniższy kod składa cały łańcuch w dwie funkcje: jedną liczącą backtest, drugą metryki. Przecięcie dwóch średnich jest tu wyłącznie DEMONSTRACJĄ mechaniki, nie rekomendacją ani dowodem przewagi. Chodzi o pokazanie, jak dane płyną od cen do krzywej kapitału, nie o to, że akurat ta reguła zarabia.

```
import numpy as np
import pandas as pd

# df: ramka z kolumna "close" (ceny zamkniecia), indeks czasowy o stalym interwale.
# UWAGA: przeciecie srednich to DEMONSTRACJA mechaniki, nie rekomendacja
# ani dowod zyskownosci. Sluzy tylko pokazaniu przeplywu danych.

def wektorowy_backtest(df, szybka=20, wolna=50, koszt_pip=0.6, pip=0.0001):
    cena = df["close"].astype(float)

    # 1) SYGNAL: +1 gdy szybka srednia nad wolna, -1 gdy pod nia. Wartosci -1/0/1.
    sma_szybka = cena.rolling(szybka).mean()
    sma_wolna  = cena.rolling(wolna).mean()
    sygnal = np.sign(sma_szybka - sma_wolna)

    # 2) POZYCJA: sygnal z zamkniecia bara t wchodzi najwczesniej na barze t+1.
    #    Bez shift(1) pozycja reaguje na ruch tego samego bara = look-ahead.
    pozycja = sygnal.shift(1).fillna(0.0)

    # 3) ZWROT RYNKU: prosty zwrot ceny na kazdym barze.
    zwrot_ceny = cena.pct_change().fillna(0.0)

    # 4) ZWROT BRUTTO: pozycja razy zwrot rynku.
    zwrot_brutto = pozycja * zwrot_ceny

    # 5) KOSZT: naliczany tylko przy ZMIANIE pozycji (wejscie/wyjscie/odwrocenie).
    zmiana = pozycja.diff().abs().fillna(0.0)
    koszt = zmiana * koszt_pip * pip / cena

    # 6) ZWROT NETTO i KRZYWA KAPITALU (skumulowany iloczyn).
    zwrot_netto = zwrot_brutto - koszt
    equity = (1.0 + zwrot_netto).cumprod()

    return pd.DataFrame({
        "pozycja": pozycja,
        "zwrot_brutto": zwrot_brutto,
        "zwrot_netto": zwrot_netto,
        "equity": equity,
    })


def metryki(zwrot_netto, equity, barow_w_roku=252):
    sigma = zwrot_netto.std(ddof=1)
    zwrot_skum = equity.iloc[-1] / equity.iloc[0] - 1.0
    zmiennosc_ann = sigma * np.sqrt(barow_w_roku)
    if sigma > 0:
        sharpe_ann = (zwrot_netto.mean() / sigma) * np.sqrt(barow_w_roku)
    else:
        sharpe_ann = np.nan
    obsuniecie = equity / equity.cummax() - 1.0
    return {
        "zwrot_skumulowany": zwrot_skum,
        "zmiennosc_roczna": zmiennosc_ann,
        "sharpe_roczny": sharpe_ann,
        "max_obsuniecie": obsuniecie.min(),
    }

# Przyklad uzycia (df z kolumna "close"):
# wynik = wektorowy_backtest(df, szybka=20, wolna=50, koszt_pip=0.6)
# print(metryki(wynik["zwrot_netto"], wynik["equity"]))
```

Parametr `barow_w_roku` zależy od interwału: dla świec dziennych to około 252 sesje, dla godzinowych odpowiednio więcej. To on skaluje zmienność i Sharpe na rok.

## Czego ten backtest nie mówi

Szkielet jest poprawny mechanicznie i właśnie dlatego łatwo mu zaufać za bardzo. Wektorowy backtest z założenia upraszcza rzeczywistość i pomija wszystko, co dzieje się między sygnałem a wypełnionym zleceniem. Nie ma w nim kolejki zleceń ani mechanizmu dopasowania, więc przyjmuje, że każde wejście dostaje cenę zamknięcia bara. Nie ma poślizgu, choć na żywo cena rusza się między decyzją a fillem. Nie ma częściowych wypełnień, choć realne zlecenie nie zawsze wchodzi w całości. Nie ma sizingu ani zarządzania ryzykiem, bo pozycja jest tu stała co do wielkości. Zakłada też, że w każdej chwili da się wejść i wyjść po widocznej cenie, co przy luce cenowej albo na cienkim rynku bywa fikcją.

Dlatego wektorowy backtest jest narzędziem do jednego: do szybkiego odsiania pomysłów, które nie działają nawet w idealnych, bezkosztowych warunkach. Jeśli strategia przegrywa w tym uproszczonym świecie, w realnym przegra tym bardziej. Odwrotna implikacja nie zachodzi: dodatni wynik tutaj nie jest dowodem, że przewaga przetrwa kontakt z rynkiem. Chan (2013) traktuje backtest jako warunek konieczny, nie wystarczający, a osobnym zagrożeniem jest samo przeszukiwanie parametrów, bo im więcej konfiguracji się przetestuje, tym łatwiej trafić na krzywą ładną przez przypadek (Bailey i López de Prado, 2014). Kolejne, uczciwsze kroki to walidacja poza próbą, realistyczny model kosztów i test wrażliwości na parametry. Wektorowy szkielet jest początkiem tej drogi, nie jej końcem.

Materiał czysto edukacyjny o mechanice backtestu, nie porada inwestycyjna. Przykład z przecięciem średnich służy wyłącznie pokazaniu przepływu danych i nie jest ani rekomendacją, ani dowodem zyskowności; dodatni wynik brutto najczęściej znika po odjęciu realnych kosztów.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
