---
title: "Look-ahead w kodzie. Jak backtest sam siebie oszukuje"
description: "Look-ahead bias to użycie informacji, która w danym momencie nie była jeszcze dostępna: najczęstszy błąd, który robi krzywą kapitału gładką i fałszywą. Klasyczna pułapka mieści się w jednej linijce: returns = signal * ret zamiast returns = signal.shift(1) * ret, czyli wejście po cenie z tego samego bara, którą znasz dopiero na zamknięciu. Do tego high/low użyte w trakcie bara, resampling widzący całą świecę, skalowanie przed podziałem train/test i repaint na Pine. Jak to łapać: test na przesuniętych danych, realistyczne koszty i walidacja out-of-sample, z odwołaniem do Lópeza de Prado (2018) oraz PBO (2016)."
date: 2026-07-12 09:00:00 +0200
eyebrow: "Programowanie · pułapki"
dek: "Ten sam kod potrafi pokazać genialną strategię albo prawdę, a różnicą bywa jedno .shift(1). Look-ahead bias przecieka na kilka sposobów naraz: brak przesunięcia sygnału, high/low w trakcie bara, resampling i skalowanie na całym zbiorze przed podziałem. Pokazane na Pythonie, wersja błędna obok poprawnej, plus lista testów, które odsiewają iluzję."
readingTime: 8
tags: [programowanie, "look-ahead", backtest, "data snooping", walidacja, Python, pandas, overfitting, "out-of-sample", repaint, "López de Prado"]
category: edukacja
---

> **W skrócie**
>
> - Look-ahead bias to użycie w chwili t informacji, która będzie znana dopiero po t. Najczęstsza forma w kodzie: `returns = signal * ret` zamiast `returns = signal.shift(1) * ret`. W pierwszej wersji sygnał policzony z zamknięcia bara mnoży zwrot tego samego bara, więc decyzja zapada po cenie, którą poznajesz dopiero na końcu świecy.
> - Efekt jest zawsze w tę samą stronę: krzywa kapitału robi się gładka, obsunięcia znikają, Sharpe rośnie. To nie przewaga, tylko mechaniczna korelacja sygnału z ruchem, który już się wydarzył. Po jednym `shift(1)` przewaga zwykle znika.
> - Rodzina błędów jest szersza niż jeden przypadek: high/low użyte do decyzji podejmowanej w trakcie bara, resampling widzący całą świecę z góry, normalizacja policzona na całym zbiorze przed podziałem train/test oraz repaint i `request.security` z `lookahead_on` na Pine.
> - Lekarstwo jest procesem, nie jedną linijką: test na przesuniętych danych, sprawdzenie, czy wynik znika po `shift`, realistyczne koszty i walidacja out-of-sample. López de Prado (2018) pokazuje, że nawet walidacja krzyżowa przecieka w finansach, jeśli nie oczyścić jej z nakładających się próbek.

**Teza w jednym zdaniu:** Backtest, który korzysta z informacji niedostępnej w chwili decyzji, nie mierzy przewagi, tylko własny przeciek, a cały problem sprowadza się do jednego pytania: czy w momencie wejścia kod znał już każdą liczbę, której użył.

## Definicja: informacja z przyszłości w rekordzie z przeszłości

Look-ahead bias, nazywany też peeking albo data leakage, pojawia się wtedy, gdy obliczenie przypisane do chwili t korzysta z danych znanych dopiero po t. Backtest przewija historię bar po barze i w każdym punkcie ma udawać, że zna wyłącznie przeszłość. Wystarczy jedno miejsce, w którym kod podejrzy przyszłość, a cały wynik jest skażony, bo strategia podejmuje decyzje niemożliwe do powtórzenia w realnym czasie. Objaw jest charakterystyczny: wynik jest za dobry, za gładki i za stabilny. Przewaga na rynku walutowym bywa cienka i hałaśliwa, więc krzywa kapitału bez obsunięć to niemal zawsze sygnał ostrzegawczy, a nie powód do dumy.

## Klasyczny błąd: signal razy ret

Najczęstszy przeciek mieści się w jednej linijce. Zmienna `ret` to zwrot bara, liczony od zamknięcia poprzedniego do zamknięcia bieżącego. Sygnał jest policzony z ceny zamknięcia tego samego bara. Jeśli pomnożymy jedno przez drugie bez przesunięcia, decyzja zapada po cenie, którą poznajemy dopiero na końcu świecy.

```
import pandas as pd

# ret[t]: zwrot od close[t-1] do close[t]
ret = close.pct_change()

# sygnal policzony z close[t]: 1 = long, 0 = poza rynkiem
signal = (close > close.rolling(20).mean()).astype(int)

# WERSJA BLEDNA: signal[t] mnozy ret[t]
# decyzja z zamkniecia bara t "lapie" ruch, ktory juz sie wydarzyl
returns_bad = signal * ret

# WERSJA POPRAWNA: decyzja z bara t dziala dopiero na barze t+1
# signal[t-1] mnozy ret[t]
returns_ok = signal.shift(1) * ret
```

Różnicę robi jedno `shift(1)`, bo w błędnej wersji sygnał i zwrot pochodzą z tego samego bara. Skoro `signal` jest funkcją `close[t]`, a `ret[t]` to właśnie ruch, który ukształtował `close[t]`, obie wielkości są mechanicznie skorelowane. Model kupuje wtedy, gdy cena już wzrosła, i zapisuje ten wzrost jako własny zysk.

```
# schemat jakosciowy, nie pomiar
signal * ret          -> krzywa rosnie gladko, Sharpe nierealnie wysoki
signal.shift(1) * ret -> po realistycznych kosztach zwykle plasko lub pod kreska
```

Dlatego pierwsza wersja rysuje równą, niemal bezobsunięciową krzywą kapitału, a druga, poprawna, zwykle ogląda przewagę znikającą po odjęciu spreadu i prowizji. To nie jest subtelność kosmetyczna, tylko różnica między pomiarem strategii a pomiarem własnego błędu.

## Cała rodzina przecieków

Brak `shift` to tylko najsłynniejszy przypadek. Ten sam mechanizm wraca w kilku przebraniach.

Użycie high i low bara do decyzji podejmowanej w jego trakcie. Ekstrema świecy są kompletne dopiero po jej zamknięciu, więc założenie "kupiłem na dołku, sprzedałem na szczycie" jest fizycznie niewykonalne w realnym czasie.

```
# high[t], low[t] znane dopiero po zamknieciu bara t
wejscie = np.where(low <= poziom, 1, 0)  # zaklada wejscie na dolku bara
zysk = high - entry                       # i wyjscie na szczycie tego samego bara
```

Resampling, który widzi całą świecę. Agregacja do wyższego interwału zamyka się na końcu okresu, ale po złączeniu z danymi o niższej rozdzielczości łatwo przypisać ją do początku okresu i użyć wewnątrz niego.

```
# M1 -> D1: dzienny close jest znany dopiero o 23:59
daily_close = m1['close'].resample('1D').last()
# przypisany do 00:00 i wpuszczony do decyzji o 09:00 = caly dzien z gory
```

Normalizacja albo skalowanie na całym zbiorze przed podziałem na trening i test. Średnia oraz odchylenie policzone z pełnych danych zawierają informację z przyszłości, która wycieka do zbioru testowego.

```
# BLEDNIE: statystyki z calego X, wiec takze z przyszlosci
X = (X - X.mean()) / X.std()
X_train, X_test = split(X)

# POPRAWNIE: mu, sd wylacznie z treningu, te same nakladane na test
mu, sd = X_train.mean(), X_train.std()
X_train = (X_train - mu) / sd
X_test  = (X_test  - mu) / sd
```

López de Prado w "Advances in Financial Machine Learning" (2018) pokazuje, że ten typ przecieku bywa subtelniejszy, niż się wydaje. Nawet klasyczna walidacja krzyżowa przecieka w finansach, bo próbki są skorelowane w czasie, a etykiety się nakładają. Lekarstwem są purging i embargo, czyli wycinanie z treningu obserwacji stykających się czasowo ze zbiorem testowym.

## Repaint: kiedy wykres kłamie w czasie rzeczywistym

Na platformach wykresowych look-ahead ma własną nazwę: repaint. Wskaźnik przelicza przeszłość po fakcie, więc na historii pokazuje sygnały w miejscach, których w danym momencie by nie wskazał. W Pine Script klasycznym źródłem jest `request.security` z parametrem `barmerge.lookahead_on`, który wciąga wartości z wyższego interwału, zanim ten interwał się domknie. Strzałka, która na historycznym wykresie leży idealnie na dołku, w realnym czasie pojawi się o kilka barów później albo zniknie. Każdy sygnał oceniany na "gotowej" świecy, która w praktyce jeszcze trwa, należy do tej samej rodziny błędów co brak `shift`.

## Survivorship bias i data snooping

Look-ahead to nie jedyny sposób, w jaki backtest podkrada informację. Survivorship bias polega na testowaniu wyłącznie instrumentów, które dotrwały do dzisiaj. Spółki wycofane z obrotu oraz pary i produkty, które zniknęły, wypadają z próby, a wraz z nimi najgorsze scenariusze. Wynik jest zawyżony, bo historia została po cichu wyczyszczona ze zwycięzcami.

Osobna, równie groźna rodzina to data snooping, czyli przeszukiwanie wielu wariantów i pokazywanie zwycięzcy bez licznika prób. Temat ma u nas osobne opracowanie o data snoopingu, więc tutaj tylko puenta ilościowa. Bailey i López de Prado (2014) w pracy o Deflated Sharpe Ratio pokazują, jak skorygować Sharpe o liczbę wypróbowanych konfiguracji i kształt ogona rozkładu, bo maksimum z wielu prób prawie zawsze wygląda dobrze. Bailey, Borwein, López de Prado i Zhu (2016) idą dalej: ich Probability of Backtest Overfitting szacuje, jak często konfiguracja najlepsza in-sample wypada poniżej mediany out-of-sample. Im szersze przeszukiwanie, tym większa szansa, że wybrany "najlepszy" wariant jest po prostu najlepiej dopasowanym szumem.

## Jak to łapać

Dobrą wiadomością jest to, że look-ahead zostawia ślady i daje się testować mechanicznie.

Test przesunięcia. Jeśli wynik załamuje się po dodaniu jednego `shift(1)` na sygnale, oryginał niemal na pewno korzystał z informacji z tego samego bara. Przewaga, która znika od przesunięcia o jeden bar, nigdy nie była przewagą.

Sprawdzenie, czy wynik przeżywa koszty. Wiele przecieków generuje mikroskopijną przewagę na trade, która w surowym backteście wygląda gładko, a pod realistycznym spreadem, prowizją i poślizgiem schodzi pod kreskę. Koszt to naturalny wykrywacz iluzji.

Rozdzielenie danych na trening i test raz, a nie wielokrotnie. Wszystkie transformacje, które uczą się ze średnich albo skrajności, trzeba dopasowywać wyłącznie na treningu. Walidacja out-of-sample, a najlepiej walk-forward z purgingiem i embargo w duchu Lópeza de Prado (2018), jest ostatnią linią obrony przed przeciekiem, którego nie wychwyciły wcześniejsze testy. To samo pytanie zadają Bailey, Borwein, López de Prado i Zhu (2016): czy zwycięzca in-sample utrzymuje się out-of-sample, czy tylko dobrze dopasował się do jednej próby.

Pojedyncze pytanie streszcza cały proces: czy w chwili wejścia kod znał już każdą liczbę, której użył. Jeśli choć jedna z nich, cena zamknięcia, ekstremum świecy, statystyka ze zbioru albo wartość z niezamkniętego interwału, będzie znana dopiero później, backtest mierzy fikcję.

To materiał czysto edukacyjny o pułapkach backtestu, nie porada inwestycyjna ani obietnica przewagi. Jego cel jest odwrotny: pokazać, jak nie dać się oszukać własnemu kodowi, zanim zaufa mu się z prawdziwym ryzykiem.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
