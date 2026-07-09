---
title: "Polowanie na stopy istnieje i udowodnił to bank centralny. Osler, kaskady i okrągłe poziomy"
description: "Carol Osler (NY Fed Staff Report 150, 2002) przebadała ~9700 rzeczywistych zleceń dużego dealera FX i pokazała, gdzie naprawdę leżą stop-lossy i take-profity wokół okrągłych poziomów. Trzy tezy o kaskadach zleceń i praktyczna nauka dla ustawiania stop-lossa."
date: 2026-07-09 15:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
category: edukacja
dek: "Większość traderów słyszała o 'polowaniu na stopy' i macha ręką jak na teorię spiskową. Tymczasem bank centralny USA policzył to na prawdziwych zleceniach dużego dealera FX. Rozkładam trzy tezy Osler i pokazuję, co z nich wynika dla ustawiania twojego stopa."
readingTime: 8
tags: ["order flow", "stop loss", "kaskady", "okrągłe poziomy", "mikrostruktura", "Osler", "NY Fed", "EUR/USD", "Forex"]
---

> **W skrócie**
>
> - **Carol Osler, NY Fed Staff Report 150 (2002)** przebadała ~9700 rzeczywistych zleceń stop-loss i take-profit jednego dużego dealera FX z lat 1999-2000. Wniosek: zlecenia nie są rozrzucone losowo, klastrują się przy okrągłych poziomach xx00 w sposób ASYMETRYCZNY.
> - **Take-profity siadają NA 00** (stąd odbicia od okrągłych cen), a **stop-lossy leżą tuż ZA 00** (buy-stopy nad poziomem, sell-stopy pod nim). Przebicie okrągłej ceny odpala falę zleceń w kierunku ruchu, bez żadnej nowej informacji. To jest właśnie kaskada.
> - **Praktyka dla ciebie:** nie kładź stop-lossa 2 pipsy za okrągłym poziomem. Siedzisz wtedy dokładnie w klastrze, po który rynek regularnie sięga.
> - **Uczciwa rama:** Osler pokazuje mechanikę (gdzie leżą zlecenia), a nie edge po kosztach. Dane mają ponad dwie dekady i pochodzą od jednego dealera, więc traktuj to jako kontekst mikrostruktury, nie gotowy sygnał wejścia.

**Teza w jednym zdaniu:** mechanika polowania na stopy jest realna i policzona na danych banku centralnego, ale to opis mikrostruktury (gdzie leżą zlecenia i dlaczego okrągłe poziomy produkują odbicia oraz kaskady), a nie gotowy sygnał wejścia z dodatnią wartością oczekiwaną po kosztach.

## "Polowanie na stopy" i czemu akurat policzył je bank centralny

Fraza "stop hunt" żyje na forach jako półzarzut, półteoria spiskowa: broker albo "smart money" celowo dociska cenę do miejsca, gdzie wisi twój stop, zbiera go i zawraca. Reakcja większości traderów jest słuszna: pokaż dane, bo bez danych to opowieść.

I tu jest cała soczystość tej historii. Dane pokazał nie youtuber, tylko ekonomistka Rezerwy Federalnej. Carol Osler w Staff Report numer 150 z 2002 roku dostała dostęp do prawdziwej książki zleceń dużego dealera FX i przeanalizowała około 9700 rzeczywistych zleceń stop-loss oraz take-profit z lat 1999-2000. To nie jest wykres z domalowanymi strzałkami. To zlecenia, które ktoś naprawdę złożył, z ceną i kierunkiem.

Najważniejsze rozróżnienie na starcie: Osler nie udowodniła, że ktoś "poluje" na ciebie z premedytacją. Udowodniła coś mocniejszego i mniej spiskowego: zlecenia całego rynku układają się wokół okrągłych poziomów tak regularnie, że sam ich układ produkuje odbicia i kaskady. Nie trzeba złego brokera. Wystarczy tłum, który wiesza zlecenia w tych samych miejscach.

## Trzy tezy Osler: gdzie naprawdę leżą zlecenia

Cała praca sprowadza się do jednej geometrii wokół ceny kończącej się na 00. Zanim przejdziemy do trzech tez, oto ta geometria w jednym obrazku.

```
   cena rośnie ↑
   1.1003   strefa buy-stopów     przebicie w górę → fala KUPNA (kaskada)
   1.1001
   1.1000   POZIOM 00 (xx00)      gęsto: take-profity → efekt odbicia
   1.0999
   1.0997   strefa sell-stopów    przebicie w dół → fala SPRZEDAŻY (kaskada)
   cena spada ↓
```

### Teza 1: take-profity siadają NA okrągłym poziomie

**Teza.** Zlecenia realizacji zysku (take-profit) gromadzą się nieproporcjonalnie na cenach kończących się na 00. Ludzie ustawiają cel na "ładnej" liczbie: 1.1000, nie 1.0997.

**Dowód.** W próbie ~9700 zleceń egzekucje take-profit skupiają się na końcówce 00 znacznie gęściej, niż wynikałoby z przypadku (sekcja III raportu). Praktyczny skutek: gdy cena dochodzi do 00, natrafia na ścianę zleceń przeciwnych do ruchu (kto kupował, tu sprzedaje z zyskiem, i odwrotnie). Ta ściana zatrzymuje ruch. Stąd znane wszystkim "odbicie od okrągłego poziomu": to nie magia liczby, to gęstość take-profitów w tym punkcie.

**Kontrargument.** Odbicie nie jest gwarancją, tylko podwyższonym prawdopodobieństwem zatrzymania. Jeśli za ruchem stoi realny popyt (news, duży flow), take-profity zostaną wchłonięte i poziom pęknie.

### Teza 2: stop-lossy leżą tuż ZA poziomem

**Teza.** Stop-lossy są rozłożone asymetrycznie względem 00: buy-stopy tuż POWYŻEJ okrągłej ceny, sell-stopy tuż PONIŻEJ.

**Dowód.** To wynika z logiki samego zlecenia. Kto gra na spadek, chroni się stopem kupna ustawionym nad poziomem oporu, czyli nad 00. Kto gra na wzrost, trzyma stop sprzedaży pod wsparciem, czyli pod 00. Osler pokazuje ten rozkład na danych (sekcje III oraz IV): za okrągłą ceną, po obu jej stronach, wisi klaster zleceń warunkowych, które uruchamiają się dopiero po przebiciu.

**Warunek błędu.** Poziomy z końcówką 50 są w danych zbadane słabiej niż 00, więc efekt najmocniej udokumentowany jest dla pełnych setek, nie dla połówek.

### Teza 3: przebicie odpala kaskadę

**Teza.** Kiedy cena przebije klaster stopów, uruchamia falę zleceń w tym samym kierunku, co ruch, i ta fala wzmacnia sama siebie bez żadnej nowej informacji.

**Dowód.** Stop-loss z definicji staje się zleceniem rynkowym w kierunku wybicia: przebite buy-stopy kupują, co pcha cenę wyżej, co odpala kolejne buy-stopy nad nimi. Powstaje zamknięta pętla, w której realizacja jednego stopa dostarcza popytu potrzebnego do sięgnięcia po następny. Osler pokazuje, że reakcja kursu na przebicie poziomu z klastrem stopów jest szybsza i większa niż na zwykły ruch tej samej wielkości (sekcja V). To definicja mechanizmu samowzmacniającego: ruch karmi ruch. Nie potrzeba nowej wiadomości, wystarczy geometria zleceń.

**Kontrargument.** Kaskada jest zjawiskiem krótkim i lokalnym. Wygasa, gdy zapas stopów się wyczerpie. Nie jest to trend, tylko impuls, który po kilku, kilkunastu pipsach traci paliwo.

## Co to znaczy dla twojego stopa na EURUSD

Z trzech tez płynie jedna konkretna, praktyczna nauka, i jest niewygodna: **nie kładź stop-lossa dwa pipsy za okrągłym poziomem.** Ustawiając stop tuż nad 1.1000 albo tuż pod nim, wkładasz go dokładnie do klastra, po który rynek strukturalnie sięga. Nie dlatego, że ktoś "poluje na ciebie", tylko dlatego, że tam jest gęsto od takich samych stopów jak twój, a gęstość przyciąga cenę.

**Co z tego wynika operacyjnie.** Jeśli logika pozycji pozwala, odsuń stop dalej za okrągły poziom albo schowaj go za realną strukturą: poprzednim dołkiem lub szczytem, ekstremum sesji, krawędzią konsolidacji, a nie za "ładną" liczbą. Chodzi o to, żeby twój stop nie stał tam, gdzie stoi tłum, bo to tłum jest paliwem kaskady. Odwrotna strona tej samej monety: świadomość, że tuż za 00 jest gęsto od stopów, tłumaczy, czemu tak często widzisz szybki wystrzał o kilka pipsów za poziom i natychmiastowy powrót. To zebrany klaster, nie zmiana kierunku.

**Warunek, w którym ta nauka zawodzi.** Gdy poziom pęka na realnej informacji (odczyt makro, wypowiedź banku centralnego, duży flow), klaster stopów przestaje być głównym aktorem. Wtedy 00 jest przebijane bez zatrzymania, bo napływa prawdziwy popyt lub podaż, a nie tylko mechanika zleceń. Mechanika Osler opisuje spokojny rynek bez nowej informacji, nie sesję newsową.

## Kontrargument: te dane mają ponad dwie dekady

Osler nie jest wyrocznią i sam raport ma słabe punkty, które trzeba wyłożyć.

Po pierwsze, dane pochodzą z lat 1999-2000 i od jednego dealera. Struktura rynku FX zmieniła się od tego czasu radykalnie: algorytmy, internalizacja flow u brokerów, rozdrobnienie płynności. Każdy z tych czynników mógł osłabić albo przesunąć efekt klastrowania. Możliwe, że dziś stopy są mniej "ładne", bo część ustawia je algorytm, a nie człowiek lubiący okrągłe liczby.

Po drugie, i to kluczowe dla nas jako traderów, Osler pokazuje mechanikę, nie edge po kosztach. Raport nie testuje żadnej strategii i nie twierdzi, że da się na tym zarobić po spreadzie i poślizgu. Wiedza "gdzie leżą zlecenia" to kontekst, nie sygnał. Odległość od kontekstu do systemu z dodatnią wartością oczekiwaną po kosztach jest długa, a większość pomysłów tę drogę przegrywa właśnie na koszcie.

Zestawienie obu stron jest więc takie: mechanika jest dobrze udokumentowana i intuicyjnie spójna z tym, co każdy widzi wokół okrągłych poziomów, ale jej siła dzisiaj oraz jej gralność po kosztach to dwa osobne, otwarte pytania. Oba rozstrzyga dopiero rzetelny pomiar na aktualnych danych, z realnym spreadem i poślizgiem, a nie sama lektura raportu. Dlatego bezpieczny status tej wiedzy brzmi: cenny kontekst mikrostruktury, nie gotowy system.

## Jak to ustawić w głowie

Bierz z tego jedno zdanie i jedną dyscyplinę. Zdanie: okrągły poziom to nie magia liczby, to miejsce, gdzie tłum wiesza take-profity i stopy, więc odbicia i wystrzały za poziom mają mechaniczne, a nie mistyczne wytłumaczenie. Dyscyplina: nie chowaj stopa dwa pipsy za pełną setką, bo wkładasz go w klaster.

Cała reszta to kontekst do twoich własnych, ręcznych decyzji, a nie automat. Nawet dowód z banku centralnego nie zwalnia z ostrożności: mechanika mówi, gdzie leżą zlecenia, ale nie obiecuje, że da się na tym zarobić po kosztach. Ta pokora jest częścią metody, nie słabością. Wielkość pozycji, moment wejścia i wyjścia oraz cierpliwość dalej są po twojej stronie.

To nie jest porada inwestycyjna. To wykład mechaniki mikrostruktury z publicznego raportu Rezerwy Federalnej, żebyś rozumiał, co jest udokumentowane w danych, a co pozostaje otwartym pytaniem, zanim oprzesz na tym decyzję.

Źródło: Carol Osler, "Stop-Loss Orders and Price Cascades in Currency Markets", Federal Reserve Bank of New York Staff Report No. 150, 2002.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
