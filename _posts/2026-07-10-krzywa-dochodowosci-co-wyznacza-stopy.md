---
title: "Krzywa dochodowości: co wyznacza stopy i co przewiduje"
description: "Rentowność i cena obligacji jako odwrotność, długa stopa jako średnia oczekiwanych stóp krótkich powiększona o premię terminową, trzy kształty krzywej oraz inwersja spreadu 10y minus 3m jako historyczny predyktor recesji w USA. Z ograniczeniami sygnału: zmienna premia, efekt skupu aktywów, mała próba i ruchome wyprzedzenie, plus przełożenie na różnice stóp w FX. Źródła: Fama i Bliss (1987), Campbell i Shiller (1991), Estrella i Mishkin (1998), Kim i Wright (2005), model recesji Fed w Nowym Jorku."
date: 2026-07-10 08:00:00 +0200
eyebrow: "Edukacja · makro"
dek: "Krzywa dochodowości to cena pieniądza w funkcji czasu. Ten tekst rozkłada ją na części pierwsze: dlaczego cena obligacji spada, gdy rośnie rentowność, dlaczego długa stopa to oczekiwane przyszłe stopy krótkie powiększone o premię terminową, co znaczą kształty normalny, płaski i odwrócony, oraz dlaczego odwrócenie krzywej od dekad wyprzedza recesje w USA i gdzie ten sygnał się myli."
readingTime: 8
tags: [makro, "krzywa dochodowości", stopy, obligacje, recesja, "premia terminowa", "hipoteza oczekiwań", "Estrella Mishkin", FX, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Rentowność i cena obligacji poruszają się w przeciwne strony, i nie jest to prawidłowość empiryczna, tylko algebra dyskontowania. Im dłuższa duracja, tym silniej cena reaguje na zmianę rentowności: papier o duracji 8 traci około 8% ceny, gdy rentowność rośnie o punkt procentowy.
> - Długa stopa w przybliżeniu równa się średniej oczekiwanych przyszłych stóp krótkich powiększonej o premię terminową. Fama i Bliss (1987) pokazali, że stopy forward z krzywej niosą informację o obu tych składnikach, a Campbell i Shiller (1991) odrzucili czystą hipotezę oczekiwań, wskazując na premię zmienną w czasie.
> - Trzy kształty: normalny (rosnąca), płaski, odwrócony. Inwersja to sytuacja, gdy krótkie stopy przewyższają długie, co rynek wiąże z oczekiwaniem przyszłych obniżek, a te bank centralny robi zwykle w słabnącej gospodarce.
> - Spread 10y minus 3m lub 10y minus 2y jako predyktor recesji w USA: Estrella i Mishkin (1998) wykazali jego przewagę nad innymi zmiennymi na horyzoncie kilku kwartałów, a Fed w Nowym Jorku publikuje na tej podstawie miesięczne prawdopodobieństwo recesji.
> - Sygnał ma granice: premia terminowa jest zmienna i bywa ujemna (model Kima i Wrighta, 2005), skup aktywów ją ściska, wyprzedzenie waha się od kilku kwartałów do ponad dwóch lat, a cała statystyka opiera się na kilkunastu recesjach. To korelacja historyczna, nie prawo fizyki.

**Teza w jednym zdaniu:** Krzywa dochodowości koduje naraz dwie rzeczy, oczekiwaną ścieżkę stóp krótkich oraz premię za ryzyko czasu, a jej nachylenie od dekad wyprzedza recesje w USA, choć jest to prawidłowość statystyczna z realnymi wyjątkami, nie przełącznik przyszłości.

## Czym jest krzywa dochodowości

Krzywa dochodowości to wykres rentowności obligacji jednego emitenta w funkcji terminu do wykupu. Na osi poziomej czas: od kilkutygodniowych bonów skarbowych po papiery trzydziestoletnie. Na osi pionowej roczna rentowność do wykupu, czyli yield to maturity. Jeden emitent, jedna waluta, różne terminy, dzięki czemu krzywa izoluje samą cenę czasu, oczyszczoną z ryzyka kredytowego. W USA punktem odniesienia są obligacje skarbowe, których rentowności publikuje codziennie Departament Skarbu.

Standardowe punkty na krzywej to bon 3-miesięczny (3m), obligacje 2-letnie (2y), 10-letnie (10y) i 30-letnie (30y). Różnica rentowności między dwoma punktami to spread, a jego znak i wielkość opisują nachylenie krzywej. To nachylenie, a nie sam poziom stóp, niesie większość informacji, o którą chodzi w dalszej części.

## Rentowność a cena: odwrotna zależność i duracja

Rentowność i cena obligacji są związane odwrotnie, i nie jest to obserwacja rynkowa, tylko konsekwencja arytmetyki. Obligacja wypłaca ustalone kupony oraz nominał. Jej cena to suma tych przepływów zdyskontowanych stopą. Gdy stopa dyskontowa rośnie, każdy przyszły przepływ jest wart dziś mniej, więc cena spada. Gdy stopa maleje, cena rośnie.

```
cena = Σ  przepływ_t / (1 + y)^t

y w górę  →  mianowniki większe  →  cena spada
y w dół   →  mianowniki mniejsze  →  cena rośnie
```

Duracja mierzy siłę tej reakcji. W przybliżeniu to średni ważony czas do otrzymania przepływów, a zarazem procentowa zmiana ceny przypadająca na jednostkową zmianę rentowności. Papier o duracji 8 traci w przybliżeniu 8% ceny, gdy rentowność rośnie o 1 punkt procentowy. Stąd praktyczny wniosek: długi koniec krzywej jest znacznie wrażliwszy na ruch stóp niż koniec krótki, i o tym warto pamiętać przy każdej rozmowie o kształcie krzywej.

```
przybliżenie:   ΔCena / Cena  ≈  −duracja · Δy

duracja 2:  Δy = +1 p.p.  →  cena ≈ −2%
duracja 8:  Δy = +1 p.p.  →  cena ≈ −8%
```

## Skąd biorą się długie stopy: oczekiwania plus premia

Dlaczego dziesięcioletnia stopa jest taka, a nie inna? Punktem wyjścia jest hipoteza oczekiwań: długa stopa to średnia oczekiwanych przyszłych stóp krótkich w okresie życia obligacji. Jeśli rynek spodziewa się, że przez dekadę średnia stopa krótka wyniesie 3%, dziesięciolatka powinna dawać mniej więcej 3%.

```
hipoteza oczekiwań (wersja czysta):
y(10 lat)  ≈  średnia oczekiwanych stóp krótkich przez 10 lat

wersja realistyczna:
y(10 lat)  ≈  średnia oczekiwanych stóp krótkich  +  premia terminowa
```

Czysta wersja nie wytrzymuje jednak konfrontacji z danymi. Inwestor trzymający długą obligację ponosi ryzyko: jeśli stopy wzrosną, poniesie stratę cenową, tym większą, im dłuższa duracja. Za to ryzyko żąda rekompensaty, którą nazywa się premią terminową. Fama i Bliss (1987) pokazali, że stopy forward wyliczane z krzywej niosą informację jednocześnie o przyszłych stopach krótkich i o oczekiwanej premii z trzymania dłuższego papieru. Campbell i Shiller (1991) poszli dalej i odrzucili czystą hipotezę oczekiwań: nachylenie krzywej faktycznie przewiduje przyszłe zmiany stóp, ale nie w taki sposób, jaki wynikałby z samych oczekiwań, co jest empirycznym śladem premii zmiennej w czasie.

Kłopot w tym, że obu składników nie da się odczytać wprost, bo krzywa pokazuje tylko ich sumę. Szacuje się je modelami. Kim i Wright (2005) z Rezerwy Federalnej zbudowali model struktury terminowej, który rozkłada długą stopę na oczekiwaną ścieżkę stóp krótkich oraz premię terminową; ich szacunki pokazują, że premia jest zmienna, a w niektórych okresach schodzi poniżej zera. To będzie kluczowe dalej: kształt krzywej nie mówi wprost, ile w nim oczekiwań, a ile premii.

## Trzy kształty krzywej

```
normalna (rosnąca):    krótkie < długie    nachylenie dodatnie
płaska:                krótkie ≈ długie    nachylenie bliskie zera
odwrócona (inwersja):  krótkie > długie    nachylenie ujemne
```

Krzywa normalna, rosnąca, jest stanem typowym: dłuższe terminy dają wyższą rentowność, bo zawierają dodatnią premię terminową i często założenie, że gospodarka rośnie, a stopy z czasem będą wyższe. Krzywa płaska sygnalizuje niepewność co do dalszej ścieżki. Krzywa odwrócona, gdy krótkie stopy przewyższają długie, jest nietypowa i to ona przyciąga uwagę. Odwrócenie oznacza, że rynek wycenia przyszłe obniżki stóp krótkich, a takie obniżki bank centralny wykonuje zwykle wtedy, gdy gospodarka słabnie. Stąd inwersja bywa czytana jako zbiorowy zakład rynku na spowolnienie.

## Inwersja jako predyktor recesji

To nie jest wyłącznie teoria. Estrella i Mishkin (1998) przebadali wiele zmiennych finansowych jako wyprzedzające wskaźniki recesji w USA i wykazali, że spread między rentownością obligacji 10-letniej a bonu 3-miesięcznego bije inne pojedyncze zmienne na horyzoncie od kilku kwartałów do około roku. Na tej pracy opiera się model Banku Rezerwy Federalnej w Nowym Jorku, który co miesiąc publikuje prawdopodobieństwo recesji w perspektywie dwunastu miesięcy, liczone właśnie ze spreadu 10y minus 3m.

```
popularne miary nachylenia:

spread 10y − 2y   klasyczny, rynkowy
spread 10y − 3m   preferowany w modelach Fed

spread poniżej zera  =  inwersja  =  historyczny sygnał ostrzegawczy
```

Regularność jest uderzająca: dokumentują to badania Fed (m.in. Bauer i Mertens, 2018), według których w USA odwrócenie krzywej wyprzedziło każdą recesję od połowy lat pięćdziesiątych, przy zasadniczo jednym fałszywym alarmie w połowie lat sześćdziesiątych. Dwie najczęściej używane miary, 10y minus 2y oraz 10y minus 3m, dają zbliżony obraz, choć nie zawsze odwracają się dokładnie w tym samym momencie.

## Gdzie ten sygnał zawodzi

Sam fakt, że coś od dekad wyprzedzało kolejne recesje, nie czyni z tego prawa. Ograniczeń jest kilka i wszystkie są poważne.

Po pierwsze, wyprzedzenie jest ruchome. Od inwersji do początku recesji mijało od kilku kwartałów do ponad dwóch lat. Sygnał mówi "prawdopodobnie", nie "kiedy", a dwuletnie okno to dla praktyka wieczność.

Po drugie, mała próba. Recesji w USA w erze powojennej było kilkanaście, więc cała statystyka opiera się na kilkunastu zdarzeniach. Wnioskowanie z tak małej liczby przypadków jest z natury kruche, o czym przypominają sami autorzy modeli.

Po trzecie, premia terminowa. Skoro krzywa to oczekiwania plus premia, to inwersja może wynikać nie z oczekiwanych obniżek, lecz ze ściśniętej premii. Skup aktywów przez banki centralne, czyli QE, obniża premię na długim końcu, więc krzywa może się spłaszczyć lub odwrócić z powodu, który z recesją ma niewiele wspólnego. Szacunki premii w duchu Kima i Wrighta pokazują, że w ostatnich dwóch dekadach bywała ona niska, a okresami ujemna, co osłabia czytelność sygnału.

Po czwarte, mechanizm kontra korelacja. Odwrócenie z 2019 roku poprzedziło recesję z 2020, lecz jej bezpośrednim wyzwalaczem była pandemia, czyli szok spoza modelu. To dobra ilustracja, że krzywa niczego nie wywołuje, a jedynie odbija zbiorowe oczekiwania, które bywają trafne, a bywają mylne.

## Krzywe a kursy walut

Dla rynku walutowego najistotniejszy jest krótki koniec krzywej, bo odbija oczekiwaną ścieżkę stóp banku centralnego. Różnica między krzywymi dwóch krajów to różnica stóp, a ta jest jednym z głównych wyznaczników relatywnej atrakcyjności waluty. Gdy rynek wycenia, że jeden bank centralny podniesie stopy mocniej niż drugi, front tej krzywej rośnie, a różnica stóp między krajami się rozszerza.

Tu jednak konieczne jest zastrzeżenie, bez którego rozdział byłby marketingiem. Związek różnicy stóp z kursem jest empirycznie słaby i notorycznie zawodny. Klasyczny wynik Famy (1984) o forward premium mówi, że waluty krajów o wyższych stopach nie osłabiają się tak, jak przewidywałby parytet stóp procentowych, a często wręcz się umacniają, co stoi u podstaw carry trade i zarazem u podstaw jego ryzyka. Innymi słowy: krzywe i różnice stóp są kontekstem, informują o oczekiwanej polityce pieniężnej, ale nie są dźwignią, która w przewidywalny sposób pcha kurs w jedną stronę.

Materiał czysto edukacyjny, nie porada inwestycyjna. Opisane zależności to matematyka wyceny obligacji oraz prawidłowości statystyczne z literatury, nie prognoza stóp, recesji ani kursów. Inwersja krzywej jest sygnałem historycznym z realnymi wyjątkami i zmiennym wyprzedzeniem, a nie pewnikiem; premia terminowa jest nieobserwowalna wprost i szacowana modelami, które same bywają obarczone błędem. Poziomy i liczby w przykładach służą arytmetyce, nie przewidywaniu.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
