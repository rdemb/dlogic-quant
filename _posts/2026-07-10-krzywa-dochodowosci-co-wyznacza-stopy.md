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

<figure class="yield-curve-shapes">
<svg viewBox="0 0 720 424" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Trzy kształty krzywej dochodowości na wspólnych osiach: normalna rosnąca, płaska oraz odwrócona malejąca." font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif">
  <text x="62" y="30" font-size="17" font-weight="600" fill="currentColor" opacity="0.85">Trzy kształty krzywej dochodowości</text>
  <g stroke="currentColor" stroke-opacity="0.14" stroke-width="1">
    <line x1="62" y1="110" x2="590" y2="110"/>
    <line x1="62" y1="150" x2="590" y2="150"/>
    <line x1="62" y1="190" x2="590" y2="190"/>
    <line x1="62" y1="230" x2="590" y2="230"/>
    <line x1="62" y1="270" x2="590" y2="270"/>
    <line x1="62" y1="310" x2="590" y2="310"/>
  </g>
  <g stroke="currentColor" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="3 4">
    <line x1="95" y1="72" x2="95" y2="330"/>
    <line x1="210" y1="72" x2="210" y2="330"/>
    <line x1="325" y1="72" x2="325" y2="330"/>
    <line x1="440" y1="72" x2="440" y2="330"/>
    <line x1="555" y1="72" x2="555" y2="330"/>
  </g>
  <g stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" fill="none">
    <line x1="62" y1="66" x2="62" y2="330"/>
    <line x1="62" y1="330" x2="596" y2="330"/>
  </g>
  <g fill="currentColor" fill-opacity="0.55">
    <polygon points="62,60 58,70 66,70"/>
    <polygon points="602,330 592,326 592,334"/>
  </g>
  <text x="326" y="372" text-anchor="middle" font-size="13" fill="currentColor" opacity="0.7">zapadalność</text>
  <text transform="rotate(-90 22 198)" x="22" y="198" text-anchor="middle" font-size="13" fill="currentColor" opacity="0.7">rentowność</text>
  <g fill="currentColor" opacity="0.7" font-size="12.5" text-anchor="middle">
    <text x="95" y="349">3M</text>
    <text x="210" y="349">2Y</text>
    <text x="325" y="349">5Y</text>
    <text x="440" y="349">10Y</text>
    <text x="555" y="349">30Y</text>
  </g>
  <path d="M 95,198 C 152.5,198 152.5,197 210,197 C 267.5,197 267.5,196 325,196 C 382.5,196 382.5,195 440,195 C 497.5,195 497.5,194 555,194" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round"/>
  <path d="M 95,250 C 152.5,250 152.5,225 210,225 C 267.5,225 267.5,200 325,200 C 382.5,200 382.5,180 440,180 C 497.5,180 497.5,165 555,165" fill="none" stroke="#1a9e6a" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M 95,140 C 152.5,140 152.5,165 210,165 C 267.5,165 267.5,190 325,190 C 382.5,190 382.5,205 440,205 C 497.5,205 497.5,215 555,215" fill="none" stroke="#e5484d" stroke-width="2.6" stroke-linecap="round"/>
  <g>
    <circle cx="95" cy="250" r="3.2" fill="#1a9e6a"/>
    <circle cx="555" cy="165" r="3.2" fill="#1a9e6a"/>
    <circle cx="95" cy="140" r="3.2" fill="#e5484d"/>
    <circle cx="555" cy="215" r="3.2" fill="#e5484d"/>
    <circle cx="95" cy="198" r="3.2" fill="currentColor" fill-opacity="0.6"/>
    <circle cx="555" cy="194" r="3.2" fill="currentColor" fill-opacity="0.6"/>
  </g>
  <text x="566" y="169" font-size="13.5" font-weight="600" fill="#1a9e6a">normalna</text>
  <text x="566" y="198" font-size="13.5" font-weight="600" fill="currentColor" opacity="0.6">płaska</text>
  <text x="566" y="219" font-size="13.5" font-weight="600" fill="#e5484d">odwrócona</text>
  <text x="62" y="402" font-size="12.5" fill="currentColor" opacity="0.6">Odwrócenie krzywej, krótkie stopy powyżej długich, historycznie wyprzedzało recesje w USA.</text>
</svg>
<figcaption>Trzy typowe kształty krzywej dochodowości na wspólnych osiach rentowności i zapadalności: normalna rosnąca, płaska oraz odwrócona malejąca. Odwrócenie, w którym krótkie stopy przewyższają długie, było w USA historycznym sygnałem wyprzedzającym recesje, choć z ruchomym wyprzedzeniem.</figcaption>
</figure>

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
