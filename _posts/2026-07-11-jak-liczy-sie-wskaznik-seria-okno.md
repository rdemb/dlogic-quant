---
title: "Jak liczy się wskaźnik: seria, okno kroczące, rekurencja"
description: "Wskaźnik jako funkcja szeregu czasowego: na wejściu seria cen, na wyjściu nowa seria tej samej długości. SMA liczona oknem kroczącym (naiwnie O(N) na bar, sumą kroczącą O(1)), EMA jako filtr rekurencyjny ema[t] = alfa*cena[t] + (1-alfa)*ema[t-1] z alfa = 2/(N+1) i seedem. Do tego kierunek czasu i pułapka indeksacji jako seria (indeks 0 to najnowszy bar) kontra indeksacja chronologiczna w pandas oraz to samo SMA i EMA wektorowo (rolling.mean, ewm) i w pętli."
date: 2026-07-11 10:00:00 +0200
eyebrow: "Programowanie · wskaźniki"
dek: "Wskaźnik to przepis na zamianę serii cen w nową serię, a dwie rodziny tego przepisu różnią się pamięcią i kosztem. Okno kroczące (SMA) pamięta N barów i płaci za krok tyle, ile zażąda implementacja. Rekurencja (EMA) trzyma jeden stan streszczający całą przeszłość z malejącą wagą, ale wymaga uwagi na seed i kierunek czasu."
readingTime: 8
tags: [programowanie, wskaźniki, SMA, EMA, pandas, "okno kroczące", "szereg czasowy", rekurencja, Python, "średnia krocząca", edukacja]
category: edukacja
---

> **W skrócie**
>
> - Wskaźnik to funkcja szeregu czasowego: na wejściu seria cen, na wyjściu nowa seria tej samej długości. Każda wartość wyjścia zależy od okna wejścia, nie od pojedynczej liczby.
> - SMA to średnia z N ostatnich barów. Naiwne przeliczanie całego okna kosztuje rzędu O(N) na bar, suma krocząca (dodaj wchodzący bar, odejmij wypadający) schodzi do O(1) na bar. Wynik ten sam, koszt inny.
> - EMA to filtr rekurencyjny: ema[t] = alfa*cena[t] + (1-alfa)*ema[t-1], alfa = 2/(N+1). Trzyma stan z poprzedniego kroku, dlatego pamięta całą historię z wagą malejącą wykładniczo (Kaufman, 2013).
> - Kierunek czasu jest kluczowy. [t-1] to poprzedni bar chronologicznie, ale przy tablicy indeksowanej jako seria (najnowszy bar ma indeks 0) poprzedni bar to indeks o jeden wyższy. Pomylenie kierunku to klasyczny look-ahead.

**Teza w jednym zdaniu:** Wskaźnik to przepis na przekształcenie serii w serię, a dwie rodziny tego przepisu, okno kroczące i rekurencja, różnią się tym, ile stanu pamiętają i ile kosztuje pojedynczy krok.

## Wskaźnik to funkcja szeregu czasowego

Punkt wyjścia jest prosty: wskaźnik nie działa na jednej liczbie, tylko na całej serii. Wejściem jest szereg czasowy, na przykład ciąg cen zamknięcia close[t] dla kolejnych barów t = 0, 1, 2 i dalej. Wyjściem jest nowy szereg tej samej długości, w którym wartość w chwili t powstaje z pewnego zbioru wartości wejścia.

Ta perspektywa porządkuje myślenie. Zamiast pytać, ile wynosi wskaźnik, warto pytać, jak wartość w chwili t zależy od wejścia do chwili t. Odpowiedź dzieli wskaźniki na dwie rodziny. Pierwsza patrzy na okno ostatnich N barów i liczy je za każdym razem od nowa. Druga trzyma stan i aktualizuje go jednym krokiem. SMA to przykład pierwszej, EMA drugiej (Kaufman, 2013).

```
wejście:  close[0], close[1], ..., close[t]   (szereg cen)
wyjście:  out[0],   out[1],   ..., out[t]     (nowy szereg)

out[t] = f( wycinek wejścia do chwili t )
```

Kluczowe słowa to "do chwili t". Poprawny wskaźnik przyczynowy używa tylko przeszłości i teraźniejszości. Sięgnięcie po close[t+1] przy liczeniu out[t] to look-ahead, czyli zaglądanie w przyszłość, o którym więcej w części o kierunku czasu.

## Okno kroczące: SMA i koszt przeliczania

Prosta średnia krocząca (SMA) to średnia arytmetyczna z N ostatnich barów. Definicja jest dosłowna:

```
SMA[t] = (close[t] + close[t-1] + ... + close[t-N+1]) / N
```

Dla pierwszych N-1 barów okno jest niepełne, więc wartości nie ma (w pandas to NaN). Od bara o numerze N-1 okno jest pełne i przesuwa się o jeden przy każdym nowym barze: wchodzi najnowszy, wypada najstarszy.

Tu pojawia się pytanie o koszt. Naiwna implementacja sumuje N liczb przy każdym barze. Dla serii długości T daje to koszt rzędu O(N*T). Sąsiednie okna różnią się jednak tylko dwoma elementami, więc wystarczy suma krocząca: do bieżącej sumy dodaj wchodzący bar i odejmij wypadający.

```
# suma kroczaca zamiast sumowania calego okna
suma = suma + close[t] - close[t-N]   # jeden dodaj, jeden odejmij
SMA[t] = suma / N                      # koszt O(1) na bar, nie O(N)
```

Wynik jest identyczny co do liczby, różni się tylko koszt: O(T) zamiast O(N*T). Przy krótkich oknach różnica jest bez znaczenia, przy długich oknach i wielu instrumentach liczy się realnie. Implementacja rolling w pandas korzysta z takich zoptymalizowanych przejść, dlatego rolling.mean nie płaci naiwnego kosztu (dokumentacja pandas, rolling).

## Rekurencja i stan: EMA jako filtr

Wykładnicza średnia krocząca (EMA) liczy się inaczej. Nie sumuje okna, tylko aktualizuje poprzednią wartość:

```
ema[t] = alfa * cena[t] + (1 - alfa) * ema[t-1]
alfa   = 2 / (N + 1)          # dla N = 20:  alfa ≈ 0,095
```

To jest filtr rekurencyjny: wynik w chwili t zależy od wejścia w chwili t oraz od własnego wyniku z chwili t-1. Dwie własności wynikają wprost z tego wzoru.

Po pierwsze, EMA pamięta. Podstawiając ema[t-1] w to samo równanie, potem ema[t-2] i tak dalej, otrzymuje się sumę wszystkich przeszłych cen z wagami (1-alfa) podniesionymi do rosnących potęg. Wagi maleją wykładniczo, ale nigdy nie są zerem: najstarszy bar wciąż ma wpływ, tylko coraz mniejszy. To odróżnia EMA od SMA, która twardo zapomina wszystko sprzed okna (Kaufman, 2013). W języku przetwarzania sygnałów SMA to filtr o skończonej odpowiedzi impulsowej, a EMA o nieskończonej (Ehlers, 2004).

Po drugie, EMA potrzebuje startu, czyli wartości ema[t-1] dla pierwszego kroku. Ten problem nazywa się seed. Spotyka się dwa podejścia: przyjąć pierwszą cenę jako pierwszą wartość EMA albo zasiać EMA średnią SMA z pierwszych N barów. Wybór wpływa tylko na początek serii, bo wraz z upływem barów udział seeda gaśnie wykładniczo. Wygładzanie wykładnicze w tej samej rekurencyjnej postaci jest klasyczną metodą prognozowania (Hyndman i Athanasopoulos, 2021).

```
# start (seed) wariant prosty: pierwsza wartosc EMA = pierwsza cena
ema[0] = cena[0]
# dalej juz rekurencja:
# ema[1] = alfa*cena[1] + (1-alfa)*ema[0], i tak dalej
```

## Kierunek czasu i pułapka indeksacji

Wzory powyżej zapisano w konwencji, w której indeks rośnie z czasem: close[t-1] to bar wcześniejszy niż close[t], a najnowszy bar ma najwyższy indeks. Tak liczy pandas i numpy: pozycja 0 to najstarszy bar, ostatnia pozycja to najnowszy.

Nie każda platforma tak indeksuje. Gdy tablica jest indeksowana jako seria (na przykład w MQL5 po wywołaniu ArraySetAsSeries), indeks 0 to najnowszy bar, a starsze bary mają wyższe indeksy. Wtedy poprzedni bar w czasie to indeks o jeden wyższy, nie niższy.

```
indeksacja chronologiczna (pandas, numpy):
  pozycja 0 = najstarszy bar, ostatnia pozycja = najnowszy
  poprzedni bar wzgledem t:  indeks t-1  (nizszy)

indeksacja jako seria (MQL5 z ArraySetAsSeries):
  indeks 0 = najnowszy bar, wyzsze indeksy = starsze bary
  poprzedni bar wzgledem i:  indeks i+1  (wyzszy)
```

To nie jest kosmetyka. Rekurencja EMA napisana jako ema[i] = alfa*cena[i] + (1-alfa)*ema[i-1] jest poprawna w indeksacji chronologicznej, ale w indeksacji jako seria sięga po ema[i-1], czyli po bar nowszy, a więc po przyszłość. To jest look-ahead wprowadzony przez sam kierunek indeksu. Przy takiej tablicy poprawny odnośnik do przeszłości to i+1. Przenoszenie wzoru między platformami bez sprawdzenia kierunku czasu to jeden z częstszych cichych błędów.

## Wektorowo kontra iteracyjnie

To samo SMA i EMA można policzyć na dwa sposoby: wektorowo, jedną operacją na całej serii, albo iteracyjnie, w pętli po barach. Wynik jest ten sam, różni się czytelność i szybkość.

Wektorowo w pandas:

```python
import pandas as pd

# close: pandas Series z cenami zamkniecia, indeks rosnacy w czasie
N = 20

# SMA: srednia z okna N barow
sma = close.rolling(window=N).mean()          # pierwsze N-1 wartosci to NaN

# EMA: filtr rekurencyjny, alfa = 2/(N+1)
# adjust=False daje dokladnie wzor rekurencyjny z seedem na pierwszej probce
ema = close.ewm(span=N, adjust=False).mean()
```

Jedna uwaga techniczna do ewm. Domyślnie pandas liczy z adjust=True, czyli jako średnią ważoną z wagami (1-alfa) w rosnących potęgach, co na początku serii daje inne liczby niż czysta rekurencja. Aby otrzymać dokładnie wzór ema[t] = alfa*cena[t] + (1-alfa)*ema[t-1] znany z platform tradingowych, trzeba ustawić adjust=False (dokumentacja pandas, ewm).

Iteracyjnie ta sama EMA, żeby zobaczyć rekurencję wprost:

```python
def ema_petla(ceny, N):
    alfa = 2.0 / (N + 1)          # waga nowej ceny
    out = [None] * len(ceny)
    out[0] = ceny[0]              # seed: pierwsza wartosc = pierwsza cena
    for t in range(1, len(ceny)):
        # nowy stan z poprzedniego stanu i biezacej ceny
        out[t] = alfa * ceny[t] + (1 - alfa) * out[t-1]
    return out
```

Pętla jest wolniejsza od wersji wektorowej, ale pokazuje istotę: EMA niesie jeden stan (out[t-1]) i aktualizuje go w każdym kroku. SMA w pętli wyglądałaby podobnie, tyle że zamiast jednego stanu utrzymywałaby sumę kroczącą okna. To jest cała różnica między dwiema rodzinami: okno kroczące pamięta N ostatnich barów i po nich zapomina, rekurencja pamięta jeden stan, który streszcza całą przeszłość z malejącą wagą.

Materiał czysto edukacyjny o tym, jak liczy się wskaźnik, nie porada inwestycyjna. Kod pokazuje strukturę obliczeń, a nie strategię, i niczego nie obiecuje. Poprawność wskaźnika zaczyna się od jednego warunku: wartość w chwili t używa wyłącznie danych do chwili t.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
