---
title: "Bootstrap i testy istotności. Ile w wyniku jest przypadku"
description: "Klasyczny test istotności zakłada rozkłady, których zwroty finansowe nie spełniają: cienkie ogony i niezależność w czasie. Bootstrap Efrona (1979) szacuje rozkład statystyki wprost z próby, bez założeń parametrycznych, a block bootstrap oraz stationary bootstrap Politisa i Romano (1994) rozszerzają go na dane zależne w czasie. Test permutacyjny i randomizacja znaku budują hipotezę zerową braku przewagi, a Reality Check White'a (2000) i test SPA Hansena (2005) urealniają poprzeczkę przy wielu hipotezach naraz. Wartość p wyjaśniona bez czterech najczęstszych błędów interpretacji."
date: 2026-07-10 14:00:00 +0200
eyebrow: "Edukacja · statystyka"
dek: "Pojedynczy imponujący wynik bez testu na tło jest liczbą bez kontekstu. Przegląd narzędzi, które odróżniają sygnał od szumu, gdy dane mają grube ogony i pamięć: bootstrap zamiast założeń o rozkładzie, resampling blokami zamiast pojedynczych obserwacji, randomizacja znaku jako hipoteza zerowa braku przewagi oraz korekta na liczbę prób w Reality Check i teście SPA."
readingTime: 8
tags: [statystyka, bootstrap, "testy istotności", "wartość p", "block bootstrap", "test permutacyjny", "Reality Check", "test SPA", Efron, White, Hansen, Ioannidis, quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Test istotności odpowiada na jedno pytanie: czy wynik da się odróżnić od tła, jakie wyprodukowałby czysty przypadek. Bez tła pojedyncza liczba, choćby imponująca, nie mówi nic.
> - Wartość p to prawdopodobieństwo uzyskania statystyki co najmniej tak skrajnej jak zaobserwowana, gdy prawdziwa jest hipoteza zerowa. To NIE jest prawdopodobieństwo, że hipoteza zerowa jest prawdziwa, ani że wynik jest dziełem przypadku, ani odsetek szansy na powtórzenie. Te błędy zebrała American Statistical Association w oświadczeniu Wassersteina i Lazar (2016).
> - Klasyczne testy zakładają rozkłady, których zwroty finansowe nie spełniają: grube ogony i autokorelację. Bootstrap Efrona (1979) omija te założenia, szacując rozkład statystyki wprost z resamplingu próby. Dla danych zależnych w czasie służą block bootstrap i stationary bootstrap Politisa i Romano (1994).
> - Test permutacyjny i randomizacja znaku zwrotu budują rozkład przy hipotezie zerowej braku przewagi bez żadnego wzoru na rozkład.
> - Przy wielu testach naraz poprzeczkę urealniają Reality Check White'a (2000) i mocniejszy test SPA Hansena (2005). Systemowe tło daje Ioannidis (2005): im więcej zespołów przeszukuje te same dane, tym mniejsza szansa, że ogłoszone odkrycie jest prawdziwe.

**Teza w jednym zdaniu:** Test istotności nie pyta „czy wynik jest dobry", tylko „czy jest lepszy, niż wypadłoby tło z samego przypadku"; gdy dane mają grube ogony i pamięć, tłem nie jest wzór z podręcznika, lecz rozkład zbudowany z samej próby przez resampling.

## Po co test istotności: sygnał kontra tło

Każdy wynik ma dwa możliwe źródła: realną zależność w danych albo przypadek. Backtest z dodatnim wynikiem, faktor z dodatnim t, reguła z ładną krzywą kapitału mogą być prawdziwe albo być jednym z wielu losowań, które akurat wypadło korzystnie. Test istotności to procedura oddzielająca te dwie możliwości ilościowo. Buduje model tła, czyli świata, w którym badany efekt nie istnieje, i sprawdza, jak często takie tło samo z siebie wyprodukowałoby wynik równie dobry jak zaobserwowany. Jeśli często, wynik nie wyróżnia się z szumu. Jeśli skrajnie rzadko, jest kandydatem na coś realnego.

Kluczowe jest słowo tło. Liczba bez tła nie ma znaczenia: Sharpe 1.5 bywa mocny albo słaby, zależnie od tego, jak wyglądałby najlepszy z prób na czystym szumie w tym samym otoczeniu. Cała statystyka istotności to różne sposoby zbudowania tego tła i zmierzenia, gdzie na jego tle leży obserwacja.

## Wartość p i jej najczęstsze błędne odczyty

Narzędziem, które podsumowuje odległość obserwacji od tła, jest wartość p. Definicja jest wąska i warto trzymać ją dosłownie.

```
wartość p = P(statystyka co najmniej tak skrajna jak zaobserwowana | H0 prawdziwa)

H0     = hipoteza zerowa, np. „strategia nie ma przewagi, prawdziwa średnia = 0"
małe p → dane słabo pasują do świata bez efektu
duże p → dane spokojnie mieszczą się w świecie bez efektu
```

Wartość p mierzy zgodność danych z hipotezą zerową, i tylko to. Wokół tej definicji narosły cztery uporczywe błędy, wszystkie wypunktowane w oświadczeniu American Statistical Association autorstwa Wassersteina i Lazar (2016):

```
czym wartość p NIE jest:
− nie jest P(H0 prawdziwa | dane): p zakłada H0, nie ocenia jej
− nie jest prawdopodobieństwem, że wynik to przypadek
− 1 − p nie jest prawdopodobieństwem, że strategia działa
− nie jest odsetkiem powtórzeń ani miarą wielkości efektu
```

Najgroźniejszy jest pierwszy z tych błędów. Wartość p jest liczona przy założeniu, że hipoteza zerowa jest prawdziwa, więc z definicji nie może orzekać, jak prawdopodobna jest sama hipoteza zerowa. Do odwrócenia warunku potrzebne są jeszcze bazowe szanse, że badany efekt w ogóle istnieje, a te przy szerokim przeszukiwaniu bywają bardzo niskie. Dokładnie ten mechanizm rozwija Ioannidis (2005) na końcu tekstu.

## Dlaczego klasyczne testy nie pasują do rynków

Klasyczny test parametryczny, na przykład test t dla średniego zwrotu, wylicza wartość p ze wzoru na rozkład statystyki. Ten wzór nie bierze się znikąd: zakłada, że obserwacje są niezależne i pochodzą z rozkładu bliskiego normalnemu, albo że jest ich dość, by zadziałało twierdzenie graniczne. Zwroty finansowe łamią oba założenia w sposób dobrze udokumentowany. Rozkłady mają grube ogony: skrajne ruchy zdarzają się znacznie częściej, niż przewiduje krzywa normalna, więc wariancja bywa niedoszacowana. Dane mają też pamięć: zmienność układa się w skupiska (spokój po spokoju, burza po burzy), a wiele szeregów wykazuje autokorelację. Autokorelacja jest szczególnie zdradliwa, bo zawyża efektywną liczbę niezależnych obserwacji. Naiwny błąd standardowy wychodzi wtedy za mały, statystyka t za duża, a wartość p optymistycznie za niska, i test melduje istotność, której w danych nie ma.

Wniosek nie brzmi „test t jest bezużyteczny", tylko „jego wartość p jest tak dobra jak założenia o rozkładzie, a na rynkach te założenia zwykle nie obowiązują". Potrzebny jest sposób szacowania rozkładu statystyki, który nie zakłada z góry jego kształtu.

## Bootstrap: rozkład statystyki wprost z próby

Tę lukę wypełnia bootstrap, zaproponowany przez Efrona (1979). Pomysł jest prosty do zuchwałości: skoro prawdziwy rozkład jest nieznany, traktuje się zebraną próbę jako najlepsze przybliżenie populacji i losuje z niej wielokrotnie ze zwracaniem. Każde takie losowanie daje nową pseudopróbę tej samej długości, dla której liczy się interesującą statystykę. Po tysiącach powtórzeń zbiór tych statystyk sam rysuje ich rozkład, z którego czyta się błąd standardowy, przedział ufności czy wartość p, bez żadnego wzoru zakładającego normalność.

```
bootstrap (Efron 1979), próba x1..xn, statystyka S (np. średnia, Sharpe):
powtórz B razy (np. B = 10 000):
    wylosuj n obserwacji ZE ZWRACANIEM z {x1..xn}   → pseudopróba
    policz S na pseudopróbie                          → S*_b
rozkład {S*_1..S*_B} przybliża rozkład S
błąd standardowy ≈ odchylenie std z {S*_b}
przedział ufności ≈ kwantyle z {S*_b}
```

Siła metody to brak założeń parametrycznych: grube ogony czy skośność próby przenoszą się do pseudoprób automatycznie, bo losowanie idzie z realnych danych. Jest jednak warunek, który zwykłemu bootstrapowi łatwo złamać na rynkach. Losowanie pojedynczych obserwacji ze zwracaniem zakłada, że są one wymienne, czyli niezależne. Dla szeregu z autokorelacją i skupiskami zmienności to założenie znów jest fałszywe, a wynik bootstrapu bywa równie mylący jak wzór, który miał zastąpić.

## Zależność w czasie: block i stationary bootstrap

Rozwiązanie: zamiast losować pojedyncze obserwacje, losować całe bloki kolejnych obserwacji. Blok zachowuje wewnętrzną strukturę zależności (autokorelację, lokalne skupisko zmienności), a losowanie bloków ze zwracaniem odtwarza serię o podobnej pamięci. To block bootstrap. Jego słabość to sztywna długość bloku oraz to, że sklejona seria nie jest ściśle stacjonarna. Politis i Romano (1994) zaproponowali stationary bootstrap: długość każdego bloku jest losowa, ciągnięta z rozkładu geometrycznego, dzięki czemu pseudoseria jest stacjonarna, a wynik mniej wrażliwy na arbitralny wybór jednej długości bloku.

```
block bootstrap:            sklejaj losowane bloki o stałej długości L
stationary bootstrap        długość każdego bloku losowa (rozkład geometryczny),
(Politis i Romano 1994):    średnia długość = 1/p; pseudoseria stacjonarna

dobór L (lub 1/p) rośnie z siłą autokorelacji:
za krótki blok → gubi pamięć, za długi → mało niezależnych bloków
```

Dla danych finansowych to zwykle właściwy wariant bootstrapu: zachowuje tę część struktury, która jest realna (pamięć zmienności), i nie udaje, że obserwacje są niezależne.

## Test permutacyjny i randomizacja znaku

Bootstrap szacuje rozkład statystyki. Blisko spokrewniona rodzina, testy permutacyjne, buduje wprost rozkład przy konkretnej hipotezie zerowej braku zależności. Zamiast losować ze zwracaniem, przetasowuje etykiety. Jeśli hipoteza mówi „sygnał nie ma związku ze zwrotem następnego dnia", wystarczy wielokrotnie pomieszać przyporządkowanie sygnałów do dni i za każdym razem policzyć wynik strategii. Rozkład wyników z przetasowanych danych to tło: świat, w którym sygnał nie niesie informacji. Jeśli prawdziwy wynik leży w skrajnym ogonie tego rozkładu, tło rzadko go produkuje.

Szczególnie prostą i wymowną wersją jest randomizacja znaku zwrotu. Przy hipotezie zerowej braku kierunkowej przewagi i w przybliżeniu symetrycznych zwrotach losowe odwrócenie znaku każdego zwrotu strategii nie powinno zmieniać rozkładu wyniku. Po tysiącach powtórzeń powstaje rozkład sumarycznego wyniku „na monetę", z którym porównuje się wynik realny.

```
randomizacja znaku (H0: brak kierunkowej przewagi):
r1..rn = zwroty strategii, obserwowany wynik = suma(r)
powtórz B razy:
    dla każdego t: znak = ±1 z prawd. 1/2
    wynik*_b = suma(znak_t · r_t)
p ≈ udział {wynik*_b ≥ obserwowany wynik}
```

Zaletą jest przejrzystość założeń: hipoteza zerowa jest dokładnie tym, co mówi procedura tasowania, bez ukrytego wzoru na rozkład.

## Wiele hipotez naraz: Reality Check i SPA

Wszystkie powyższe testy oceniają jedną strategię. Praktyka wygląda inaczej: testuje się dziesiątki albo tysiące wariantów i pokazuje najlepszy. Wtedy właściwą hipotezą zerową nie jest „ta strategia nie ma przewagi", lecz „najlepsza z całego przeszukiwanego zbioru nie ma przewagi nad benchmarkiem". White (2000) sformalizował to jako Reality Check: statystyką jest maksimum po wszystkich modelach, a jej rozkład przy hipotezie zerowej buduje się bootstrapem bloków (dokładnie stationary bootstrap Politisa i Romano), tak by uwzględnić zależność w czasie i całe uniwersum prób naraz. Zwycięzca jest porównywany nie z zerem, lecz z rozkładem zwycięzców, jakich tło produkuje z samego przeszukiwania. To samo narzędzie stoi za testem 7846 reguł technicznych, opisanym osobno w tekście o [data snoopingu](/dlogic-quant/2026/07/05/data-snooping-jak-finanse-sie-oszukuja/).

Hansen (2005) wskazał słabość Reality Check i ją naprawił. Test White'a traci moc, gdy do uniwersum trafia wiele beznadziejnych modeli: zawyżają one rozkład tła i chowają prawdziwego zwycięzcę. Test SPA (superior predictive ability) Hansena używa statystyki studentyzowanej oraz rozkładu zerowego zależnego od danych, przez co jest mocniejszy i mniej podatny na zaśmiecenie uniwersum słabymi kandydatami. W obu wypadkach idea jest ta sama: poprzeczką nie jest zero, lecz najlepszy wynik, jakiego należy oczekiwać od tła przy tej liczbie prób.

## Wniosek: liczba bez tła nie znaczy nic

Za każdym imponującym wynikiem stoi jakieś tło, a jedyne uczciwe pytanie brzmi, jak wynik wygląda na jego tle. Bootstrap Efrona (1979) buduje to tło bez założeń o rozkładzie, block i stationary bootstrap Politisa i Romano (1994) rozszerzają je na dane z pamięcią, testy permutacyjne i randomizacja znaku definiują hipotezę zerową braku przewagi wprost, a Reality Check White'a (2000) i test SPA Hansena (2005) urealniają poprzeczkę, gdy prób jest wiele. Szersze, systemowe uzasadnienie daje Ioannidis (2005): pozytywna wartość predykcyjna ogłoszonego odkrycia spada wraz z liczbą zespołów przeszukujących te same dane, więc w polu tak zatłoczonym jak finanse ostrożność wobec pojedynczej efektownej liczby jest postawą domyślną, a nie przesadną.

Praktyczny odruch mieści się w jednym zdaniu: zanim uwierzysz w wynik, zbuduj tło i sprawdź, jak często samo tło dałoby coś równie dobrego. Wynik bez takiego porównania, choćby najładniejszy, pozostaje liczbą bez kontekstu.

Materiał czysto edukacyjny, nie porada inwestycyjna. Tekst opisuje metody oceny, czy wynik da się odróżnić od przypadku, i nie obiecuje żadnej przewagi ani nie opisuje konkretnej strategii. Pewna jest tu wyłącznie logika testu: bez modelu tła pojedyncza statystyka nie niesie informacji o tym, czy stoi za nią sygnał, czy szum.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
