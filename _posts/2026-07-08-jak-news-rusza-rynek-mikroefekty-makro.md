---
title: "Jak news rusza rynkiem. Liczy się zaskoczenie, nie liczba"
description: "Rynek nie reaguje na samą wartość odczytu makro, tylko na zaskoczenie względem konsensusu prognoz, bo oczekiwana część liczby siedzi już w cenie. Dlatego dobra liczba potrafi przecenić walutę, gdy rynek liczył na jeszcze lepszą. Praca Andersena, Bollersleva, Diebolda i Vegi pokazała, że kurs skacze na standaryzowanym zaskoczeniu w ułamku minuty, a zmienność normalizuje się wolniej. Mikrostruktura okna publikacji, rola order flow i flash events jako ostrzeżenie przed handlem w sekundę po odczycie."
date: 2026-07-08 17:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
dek: "Rynek nie płaci za liczbę, tylko za różnicę między liczbą a tym, czego oczekiwano. Konsensus jest już w cenie, więc rusza dopiero zaskoczenie, i to tak szybko, że w sekundę po publikacji spread się rozjeżdża, a płynność znika. Dlaczego dobra dana bywa złą daną, co robi order flow w oknie newsa i czego uczy flash w funcie z 2016 roku."
readingTime: 8
tags: ["zaskoczenie", "konsensus", "surprise", mikrostruktura, "news trading", "Andersen Bollerslev Diebold Vega", "micro effects", "flash crash", "Sterling Flash 2016", "order flow", "poślizg", spread, płynność, zmienność, BIS, "kurs walutowy", edukacja, Forex]
category: edukacja
---

> **W skrócie**
>
> - Rynek wycenia oczekiwania, więc w cenie siedzi już konsensus prognoz. Rusza dopiero zaskoczenie, czyli różnica między odczytem a tym, czego oczekiwano. Dlatego dobra liczba potrafi przecenić walutę, jeśli rynek liczył na jeszcze lepszą.
> - Andersen, Bollerslev, Diebold i Vega w pracy Micro Effects of Macro Announcements pokazali na danych wysokiej częstotliwości, że kurs skacze na standaryzowanym zaskoczeniu niemal natychmiast, kierunek wyznacza znak zaskoczenia, a reakcja bywa asymetryczna: złe wiadomości ruszają mocniej niż dobre.
> - Reakcja jest skoncentrowana wokół publikacji. Tuż przed odczytem dostawcy płynności wycofują kwotowania i rozszerzają spread, w momencie publikacji zmienność skacze, a płynność wraca stopniowo. To najdroższy moment na przekroczenie spreadu.
> - W skrajnych przypadkach jednostronny order flow w cienkim oknie potrafi przytłoczyć płynność i wywołać flash event, jak załamanie funta 7 października 2016 opisane przez BIS. Praktyczna nauka: nie wchodź marketem w sekundę po publikacji, bo spread i poślizg zjadają przewagę.

**Teza w jednym zdaniu:** Odczyt makro rusza kursem nie samą wartością, tylko zaskoczeniem względem konsensusu, a robi to w wąskim, cienkim i drogim oknie wokół publikacji, gdzie spread i poślizg potrafią zjeść całą przewagę.

## Zaskoczenie, nie liczba: co naprawdę wchodzi w cenę

Podręcznikowa intuicja mówi, że dobry odczyt umacnia walutę, a zły ją osłabia. W praktyce liczy się co innego: nie sama wartość, tylko jej odległość od tego, czego rynek oczekiwał. Powód jest prosty. Cena w każdej chwili wycenia oczekiwania, a oczekiwania co do najbliższego odczytu są zbierane wprost, jako konsensus prognoz analityków, zwykle mediana ankiety. Jeśli dana wychodzi dokładnie na konsensusie, w zasadzie nie wnosi nowej informacji, bo ta liczba siedziała już w cenie. Nowa jest dopiero różnica.

Tę różnicę nazywa się zaskoczeniem: wartość odczytu minus konsensus. Ma znak, dodatni gdy dana wypadła powyżej oczekiwań, ujemny gdy poniżej, i to znak wyznacza kierunek reakcji. Żeby porównywać zaskoczenia z odczytów mierzonych w różnych jednostkach, na przykład zatrudnienie w tysiącach etatów i inflacja w procentach, standaryzuje się je, dzieląc przez typowy rozrzut danego wskaźnika. Zostaje czysta miara: o ile odczyt rozminął się z oczekiwaniami. To ona, a nie goła liczba, jest paliwem ruchu.

## Dlaczego dobra liczba potrafi przecenić walutę

Z tej optyki wynika rzecz, która myli początkujących. Dobra liczba potrafi przecenić aktywo. Wyobraź sobie, że rynek liczy na bardzo mocny odczyt zatrudnienia, a wychodzi odczyt tylko przyzwoity, wyraźnie powyżej zera, ale poniżej rozdmuchanego konsensusu. W ujęciu bezwzględnym to dobra dana. W ujęciu względem oczekiwań to zaskoczenie negatywne, więc waluta może się osłabić mimo dobrego nagłówka. Punktem odniesienia nie jest zero ani ocena, czy liczba jest wysoka, tylko konsensus.

Rynkowe porzekadło kupuj plotkę, sprzedawaj fakt opisuje ten sam mechanizm od strony pozycjonowania. Oczekiwania wbudowują się w cenę na długo przed publikacją, uczestnicy ustawiają się pod spodziewany wynik, a kiedy fakt tylko potwierdza to, co już wyceniono, ustawieni realizują zysk i cena idzie wbrew oczywistej lekturze odczytu. Ta sama liczba w innym kontekście oczekiwań ruszy rynek w przeciwną stronę. Dlatego bez konsensusu odczyt jest nieczytelny.

## Micro Effects of Macro Announcements: co pokazały dane

Najczęściej przywoływanym dowodem na to jest praca Torbena Andersena, Tima Bollersleva, Francisa Diebolda i Clary Vegi Micro Effects of Macro Announcements z 2003 roku. Autorzy zestawili kwotowania kursów o wysokiej częstotliwości z kalendarzem ogłoszeń makro i ankietowymi oczekiwaniami rynku, a potem zmierzyli, jak kurs reaguje na standaryzowane zaskoczenie w wąskich oknach wokół publikacji.

Wyniki układają się w kilka jasnych obserwacji, wszystkie bez konieczności podawania liczb. Średni kurs skacze na zaskoczeniu niemal natychmiast, price discovery jest szybki i mieści się w minutach po odczycie. Kierunek ruchu wyznacza znak zaskoczenia, a nie poziom samej danej. Reakcja bywa asymetryczna: rynek mocniej reaguje na złe wiadomości niż na dobre. I wreszcie zmienność dostosowuje się wolniej niż średnia, sam skok poziomu jest błyskawiczny, ale podwyższona zmienność utrzymuje się dłużej, w miarę jak rynek trawi odczyt. To jest twardy fundament tezy, że rusza zaskoczenie, nie liczba.

## Okno publikacji od środka: skok zmienności, szerszy spread, cieńsza płynność

Reakcja jest nie tylko szybka, ale i skoncentrowana, a jej mikrostruktura ma stały kształt. Tuż przed zaplanowanym odczytem dostawcy płynności wiedzą, że za chwilę padnie zaskoczenie, którego nie znają. Żeby nie dać się przejechać komuś, kto zareaguje szybciej, wycofują część kwotowań i rozszerzają spread. Głębokość arkusza topnieje w ostatnich sekundach przed publikacją. To ochrona przed negatywną selekcją, czyli przed handlem z lepiej poinformowanym.

W momencie publikacji zmienność skacze, cena luką przesuwa się w stronę zaskoczenia, pojawia się seria transakcji. Zaraz po odczycie spread pozostaje szeroki, a arkusz cienki, bo price discovery trwa jeszcze kilka, kilkanaście sekund, a płynność wraca stopniowo. Efekt netto jest niewygodny: dokładnie wtedy, gdy cena rusza się najmocniej, koszt zawarcia transakcji jest najwyższy. Badania BIS nad mikrostrukturą i elektronicznym handlem FX opisują to wycofywanie płynności wokół zaplanowanych zdarzeń jako regularną cechę rynku, nie wyjątek.

## Order flow: kto pierwszy, ten lepszy, ale i poślizg

Zaskoczenie jest publiczne, ale jego przełożenie na cenę dokonuje się przez handel, czyli przez order flow. Szybcy, często zautomatyzowani uczestnicy czytają liczbę w milisekundach i uderzają w arkusz, a ich jednostronny przepływ popycha cenę. Dealer po drugiej stronie nie zdąży odróżnić poinformowanego od przypadkowego, więc broni się, rozszerzając kwotowanie. Dla szybkiego, poinformowanego gracza istnieje przewaga pierwszego ruchu, zdąży zanim cena w pełni się przestawi.

Ta sama dynamika jest pułapką dla wolniejszego. Wejście zleceniem rynkowym w cienki, rozpędzony arkusz oznacza poślizg: realizacja ląduje daleko od ceny, którą widziałeś klikając, a zapłacony spread jest szeroki. Przewaga, którą wydawało się, że masz z trafnego odczytania danej, zostaje zjedzona przez koszt przekroczenia rynku w najgorszym momencie. Zasada kto pierwszy, ten lepszy działa na korzyść maszyn liczonych w mikrosekundach, nie człowieka klikającego po odczycie.

## Zdarzenia ekstremalne: flash events jako ostrzeżenie

Czasem dynamika okna wymyka się w coś gwałtownego. Sztandarowym przykładem jest załamanie funta z 7 października 2016 roku. W cienkiej płynności wczesnych godzin sesji azjatyckiej kurs GBP/USD spadł o kilka procent w ciągu kilku minut, po czym częściowo się odbił. Raport komitetu rynkowego BIS, który to zbadał, nie wskazał jednej przyczyny, tylko splot: bardzo cienką płynność o tej porze, wybuch jednokierunkowego order flow, zachowanie zautomatyzowanej egzekucji i zleceń stop, oraz zabezpieczenia związane z opcjami, które nakręcały się nawzajem.

Morał jest ostrzeżeniem, nie ciekawostką. W cienkim i szybkim oknie order flow potrafi przytłoczyć płynność i wypchnąć cenę daleko poza to, co uzasadniałaby sama treść wiadomości. Flash event to skrajny przypadek tego samego mechanizmu, który w łagodniejszej formie działa wokół każdego większego odczytu. Handel dokładnie w tym oknie to wystawianie się na ryzyko ogona, na ruch, którego wielkości i kierunku nie da się kontrolować zleceniem rynkowym.

## Praktyczna nauka: nie klikaj marketem w sekundę po odczycie

Zapłata za ten wywód nie jest sygnałem, tylko modelem mentalnym i lekcją o kosztach. Wejście zleceniem rynkowym sekundę po publikacji oznacza zapłatę najszerszego spreadu i najgorszego poślizgu, dokładnie wtedy, gdy arkusz jest najcieńszy i najszybszy. Ruch, za którym się goni, jest w tym momencie często w dużej mierze już wykonany, bo maszyny przestawiły cenę, zanim człowiek zdążył kliknąć. Okno newsa to najdroższy moment na przekroczenie spreadu, a nie najłatwiejszy zarobek.

Wartość edukacyjna jest więc dwojaka. Po pierwsze, czytaj odczyt zawsze przez pryzmat konsensusu, bo bez punktu odniesienia liczba nic nie mówi, a dobra dana bywa złą daną. Po drugie, traktuj samo okno publikacji jako strefę podwyższonego kosztu i ryzyka, a nie okazję do impulsywnego wejścia. To jest kontekst do rozumienia, dlaczego rynek zrobił to, co zrobił, a nie spust do klikania w sekundę po odczycie.

To nie jest porada inwestycyjna. To wyłożenie mechanizmu z literatury: mikroefektów ogłoszeń makro u Andersena, Bollersleva, Diebolda i Vegi, oraz obrazu mikrostruktury i flash events z badań BIS, żebyś rozumiał, dlaczego cena reaguje na zaskoczenie, a nie na samą liczbę, dlaczego okno publikacji jest cienkie i drogie, i dlaczego kliknięcie marketem sekundę po odczycie płaci najgorszą cenę.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
