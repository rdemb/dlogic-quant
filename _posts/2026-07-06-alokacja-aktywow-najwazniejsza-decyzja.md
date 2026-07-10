---
title: "Alokacja aktywów. Najczęściej błędnie cytowane badanie w finansach"
description: "Polityka alokacji, czyli podział kapitału między akcje, obligacje, gotówkę i aktywa realne, ustawia profil wahań portfela zanim padnie decyzja o pierwszej konkretnej spółce. Brinson, Hood i Beebower (1986) pokazali na 91 funduszach emerytalnych, że polityka wyjaśnia średnio 93,6% wariancji zwrotów funduszu w czasie, a branża cytuje ten wynik błędnie jako udział w poziomie zwrotu. Poprawną dekompozycję dali Ibbotson i Kaplan (2000): około 90% zmienności w czasie, około 40% różnic między funduszami, około 100% poziomu zwrotu. Do tego 126 lat premii klas aktywów według Dimsona, Marsha i Stauntona, rebalancing jako mechaniczna dyscyplina oraz horyzont i tolerancja ryzyka jako wejścia do decyzji."
date: 2026-07-06 14:00:00 +0200
eyebrow: "Edukacja · długi termin"
dek: "Hasło, że 90% wyniku inwestycyjnego to alokacja aktywów, powtarza pół branży. Problem w tym, że badanie, na które wszyscy się powołują, mierzyło coś innego: 93,6% dotyczy wariancji zwrotów w czasie, nie poziomu wyniku. Poprawna odpowiedź ma trzy liczby, 90, 40 i 100, a każda odpowiada na inne pytanie."
readingTime: 8
tags: ["alokacja aktywów", "Brinson Hood Beebower", "Ibbotson Kaplan", "polityka inwestycyjna", akcje, obligacje, rebalancing, "premia za ryzyko", "Dimson Marsh Staunton", "all-weather", "tolerancja ryzyka", "horyzont inwestycyjny", quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Polityka alokacji to podział kapitału między klasy aktywów: akcje, obligacje, gotówkę i aktywa realne. To decyzja innego rzędu niż wybór konkretnych papierów czy timing i w praktyce nadrzędna wobec obu, bo ustala, na jakich źródłach ryzyka portfel jedzie na co dzień.
> - Brinson, Hood i Beebower (Financial Analysts Journal, 1986) policzyli na 91 dużych amerykańskich funduszach emerytalnych za lata 1974-1983, że polityka alokacji wyjaśnia średnio 93,6% wariancji zwrotów funduszu w czasie. To R kwadrat regresji szeregów czasowych, miara współchodzenia, a nie udział w poziomie zwrotu. "90% wyniku to alokacja" jest błędnym cytatem z tej pracy.
> - Ibbotson i Kaplan (Financial Analysts Journal, 2000) rozplątali nieporozumienie trzema liczbami: polityka wyjaśnia około 90% zmienności funduszu w czasie, około 40% różnic w zwrotach między funduszami i około 100% poziomu zwrotu, bo aktywne zarządzanie w agregacie sumuje się do zera przed kosztami i poniżej zera po kosztach.
> - Skalę nagród za ryzyko pokazuje 126 lat danych (Dimson, Marsh, Staunton, Global Investment Returns Yearbook, obecnie UBS; lata 1900-2025, 35 rynków): akcje globalnie dały realnie około 6,6% rocznie, obligacje około 1,6%, przy czym obie klasy przechodziły wieloletnie posuchy.

**Teza w jednym zdaniu:** O profilu wahań portfela i o rzędzie wielkości oczekiwanego zwrotu decyduje przede wszystkim podział kapitału między klasy aktywów, a słynne "90% wyniku to alokacja" jest błędnym odczytaniem badania, które mierzyło zgodność wahań funduszu z wahaniami jego benchmarku, czyli zupełnie inną wielkość.

## Trzy decyzje, z których jedna ustawia całą resztę

Wynik każdego portfela da się rozłożyć na trzy decyzje. Pierwsza to polityka alokacji: jaki procent kapitału trafia do akcji, jaki do obligacji, ile zostaje w gotówce, a ile idzie w aktywa realne, na przykład nieruchomości czy surowce. Druga to selekcja: które konkretnie papiery kupić wewnątrz każdej klasy. Trzecia to timing: kiedy odchylić wagi od polityki, bo jakiś rynek wygląda na tani albo drogi.

Polityka jest decyzją innego rzędu niż dwie pozostałe, bo klasy aktywów to różne umowy ekonomiczne. Akcja to udział w zyskach firm: wysoka zmienność, głębokie obsunięcia, historycznie najwyższa nagroda. Obligacja to umowa o odsetki: płytsze wahania, ale wrażliwość na inflację, która potrafi zjeść kupon. Gotówka nie waha się nominalnie i właśnie dlatego przegrywa z inflacją bez żadnej osłony. Aktywa realne chodzą własnym rytmem i bywają kotwicą w okresach inflacyjnych. Portfel złożony w 90% z akcji i portfel złożony w 90% z obligacji to dwa różne zwierzęta niezależnie od tego, jak genialnie dobrano w nich pojedyncze pozycje. Selekcja i timing personalizują wynik wewnątrz ram, które ustawiła polityka.

Tyle intuicji. Pytanie, ile ta hierarchia waży w liczbach, ma swoją słynną odpowiedź i jeszcze słynniejsze przekłamanie.

## Badanie, które zna każdy, i cytat, którego w nim nie ma

W 1986 roku Gary Brinson, Randolph Hood i Gilbert Beebower opublikowali w Financial Analysts Journal pracę "Determinants of Portfolio Performance". Wzięli 91 dużych amerykańskich funduszy emerytalnych i ich kwartalne zwroty z lat 1974-1983. Dla każdego funduszu zbudowali zwrot polityki: to, co fundusz by zarobił, gdyby swoje normalne wagi klas aktywów trzymał w pasywnych indeksach, bez żadnej selekcji i bez timingu. Potem policzyli regresję szeregów czasowych: jak mocno faktyczne kwartalne zwroty funduszu chodzą za zwrotami jego własnej polityki.

Wynik: średni R kwadrat 93,6%. Wahania funduszu z kwartału na kwartał niemal w całości odwzorowują wahania pasywnego benchmarku jego polityki. Gdy rynek akcji spada, fundusz o polityce 60/40 spada razem z nim i nie ma większego znaczenia, które spółki akurat trzyma.

I teraz najważniejsze zdanie tego tekstu. R kwadrat regresji szeregów czasowych mierzy współchodzenie w czasie, a nie to, skąd bierze się poziom wyniku. Z 93,6% wariancji nie wynika, że "93% zarobku pochodzi z alokacji". A dokładnie w tę stronę spora część branży cytuje tę pracę od czterech dekad: "badania pokazują, że ponad 90% wyniku inwestycyjnego to alokacja aktywów". Zdanie świetnie brzmi w materiałach sprzedażowych i nie jest tym, co pokazali autorzy.

Obrazek pomocniczy: łódka na fali. Falowanie morza wyjaśnia prawie całą zmienność wysokości łódki z minuty na minutę. Nie mówi jednak nic o tym, czy łódka płynie do przodu i czy szybciej niż sąsiednia. Brinson, Hood i Beebower zmierzyli falowanie. Cytowani są tak, jakby zmierzyli prędkość.

Na marginesie pracy warto odnotować rzecz często pomijaną: w badanej próbce przeciętny fundusz osiągnął wynik niższy niż jego własny pasywny benchmark polityki. Selekcja i timing razem wzięte średnio odejmowały wartość zamiast ją dodawać.

## 90, 40 czy 100. Trzy pytania, trzy odpowiedzi

Nieporozumienie urosło do tego stopnia, że w 2000 roku Roger Ibbotson i Paul Kaplan opublikowali w Financial Analysts Journal pracę pod tytułem będącym pytaniem: "Does Asset Allocation Policy Explain 40, 90, or 100 Percent of Performance?". Odpowiedź brzmi: zależy, o co dokładnie pytasz, bo pod hasłem "ile znaczy alokacja" kryją się trzy różne pytania i trzy różne liczby.

```
Pytanie                                             Odpowiedź    Miara
Ile wahań funduszu W CZASIE wyjaśnia polityka?      ok. 90%      R² regresji szeregów czasowych
Ile RÓŻNIC MIĘDZY funduszami wyjaśnia polityka?     ok. 40%      R² regresji przekrojowej
Jaką część POZIOMU zwrotu dostarcza polityka?       ok. 100%     zwrot polityki / zwrot faktyczny
```

Pierwsza liczba to potwierdzenie wyniku z 1986 roku na świeższych danych funduszy mieszanych i emerytalnych: około 90% zmienności zwrotów typowego funduszu w czasie wyjaśnia jego polityka. Ibbotson i Kaplan dodali niuans, który dodatkowo studzi marketing: ten wysoki R kwadrat bierze się głównie z samego faktu bycia na rynku, a nie z konkretnej proporcji. Fundusze o całkiem różnych politykach i tak chodzą podobnie, bo wszystkie jadą na tych samych szerokich rynkach akcji i obligacji.

Druga liczba odpowiada na pytanie, które branża naprawdę ma na myśli, gdy cytuje pracę z 1986 roku: dlaczego fundusz A zarobił przez dekadę więcej niż fundusz B. Różnice polityk wyjaśniają około 40% różnic w zwrotach między funduszami. Resztę robią selekcja, timing, opłaty i zwykły los. Tam, gdzie porównujemy się z innymi, alokacja znaczy więc dużo, ale daleko jej do "ponad 90%".

Trzecia liczba brzmi najbardziej zaskakująco: polityka dostarcza średnio około 100% poziomu zwrotu. Mechanizm jest arytmetyczny, nie tajemniczy. Każda transakcja ma dwie strony, więc przeciętny aktywny portfel to po prostu portfel rynkowy. W agregacie aktywne zarządzanie sumuje się do zera przed kosztami, a po kosztach do wartości ujemnej. Skoro średnio aktywność dokłada zero minus koszty, to średnio cały poziom zwrotu pochodzi z polityki. Dla przeciętnego funduszu pasywna realizacja jego własnej polityki była co najmniej równie dobra jak faktyczny wynik.

Trzy liczby, trzy pytania, zero sprzeczności. Błędny cytat powstaje przez sklejenie liczby z pierwszego pytania z treścią trzeciego.

## Co z tego wynika przy budowie portfela

Praktyczna translacja jest prosta. To, jak bardzo portfel buja i jak głębokie obsunięcia funduje po drodze, ustawia proporcja akcji do obligacji, a nie lista konkretnych spółek. Dwa portfele o tej samej polityce pójdą podobną drogą nawet przy zupełnie różnej selekcji. Dwa portfele o różnych politykach pójdą różnymi drogami nawet przy selekcji identycznej.

Dlatego pierwsze pytanie przy budowie portfela nie brzmi "co kupić", tylko "jaki podział zniosę". Jeśli głębokie obsunięcie wywróci plan, to żadna selekcja tego nie naprawi, bo o skali obsunięć zdecydowała już sama waga akcji. Selekcja i timing są dopracowaniem szczegółów wewnątrz decyzji, która zapadła wcześniej i wyżej.

## Ile historycznie płaciły klasy aktywów: 126 lat danych

Skoro alokacja ustawia profil portfela, potrzebna jest wiedza, co poszczególne klasy historycznie płaciły za znoszenie ich ryzyka. Najdłuższą i najszerszą bazą jest Global Investment Returns Yearbook Dimsona, Marsha i Stauntona, wydawany obecnie przez UBS (wcześniej przez Credit Suisse): dane od 1900 roku, w edycji 2026 obejmujące 126 lat i 35 rynków.

```
Zwroty realne (po inflacji), średniorocznie, lata 1900-2025:

akcje globalnie              ok. 6,6% rocznie
obligacje                    ok. 1,6% rocznie
```

Dwie rzeczy z tego zestawienia są ważniejsze niż same liczby. Po pierwsze, różnica rzędu kilku punktów procentowych rocznie, składana procentem przez dekady, tworzy przepaść w wyniku końcowym: to jest premia za ryzyko akcji i to ona jest głównym silnikiem długoterminowych portfeli. Po drugie, premia nie jest rentą wypłacaną co miesiąc. W 126 latach danych zdarzały się wieloletnie okresy, w których akcje realnie nie zarabiały nic albo traciły, i to na wielu rynkach naraz. Premia jest zapłatą właśnie za gotowość przetrwania takich posuch. Kto ich nie przetrwa, ten premii nie odbierze.

## Rebalancing: dyscyplina zamiast prognozy

Polityka alokacji nie utrzymuje się sama. Wagi dryfują: klasa, która urosła, sama się przeważa. Portfel 60/40 po mocnym roku akcji potrafi zmienić się w 70/30, czyli w portfel bardziej ryzykowny, niż zaplanowano, i to dokładnie w momencie, w którym akcje są droższe niż wcześniej.

Rebalancing to mechaniczne przywracanie wag docelowych: sprzedaje się część tego, co urosło, dokupuje to, co staniało, bez prognozy i bez opinii o rynku. W tym sensie to wbudowany mechanizm kupowania taniej i sprzedawania drożej, tyle że wymuszony arytmetyką wag, a nie odwagą inwestora. Uczciwie trzeba dodać, że rebalancing nie jest maszynką do dodatkowego zwrotu: w długich, jednostajnych trendach przycinanie zwycięzcy kosztuje. Jego zadanie jest inne. Utrzymuje ryzyko portfela przy poziomie, który świadomie wybrano, i zdejmuje z człowieka decyzję, którą emocje podejmują najgorzej, czyli dokupowanie klasy, która właśnie spadła. Wykonanie bywa kalendarzowe (na przykład raz do roku) albo progowe (gdy waga odjedzie od celu o ustalony margines); wspólnym mianownikiem jest to, że regułę ustala się z góry, zanim rynek zacznie testować nerwy.

## Horyzont, tolerancja ryzyka i myślenie reżimowe

Nie istnieje jedna poprawna alokacja. Decyzja ma dwa wejścia. Pierwsze to horyzont: kiedy pieniądze będą potrzebne. Im bliżej terminu, tym mniej miejsca na klasę, która potrafi być głęboko pod wodą przez lata. Drugie to tolerancja ryzyka: jak głębokie obsunięcie inwestor realnie zniesie, nie w deklaracji, tylko w nocy, w której portfel świeci na czerwono. Plan ostrożniejszy, ale utrzymany, bije plan ambitny porzucony w dołku, bo porzucenie zamienia przejściowe obsunięcie w trwałą stratę.

Osobną szkołą myślenia o alokacji jest podejście all-weather kojarzone z Rayem Dalio. Zamiast zgadywać, który scenariusz makro nadejdzie, buduje się portfel z klas, które różnie reagują na reżimy wzrostu i inflacji, tak aby żaden pojedynczy scenariusz nie wywracał całości. Nie trzeba kupować tej konkretnej konstrukcji, żeby docenić sposób stawiania pytania: nie "co wzrośnie", tylko "jak podzielić kapitał, żeby portfel przetrwał każdą pogodę". To dokładnie ten sam rodzaj decyzji, którą mierzyli Brinson, Hood i Beebower oraz Ibbotson i Kaplan: polityka, nie selekcja.

## Co z tego zostaje

Alokacja aktywów to największa pojedyncza decyzja portfela i zapada, zanim zostanie kupiony pierwszy papier. Badania z tego tekstu składają się na spójny obraz. Wahania portfela w czasie niemal w całości dziedziczy się z polityki: około 90%, a w oryginalnej próbce funduszy emerytalnych 93,6%. Różnice wyników między portfelami polityka wyjaśnia w około 40%, więc miejsce na selekcję i timing istnieje, tylko jest mniejsze, niż głosi marketing. Poziom zwrotu przeciętnego inwestora pochodzi z polityki w około 100%, bo aktywność w agregacie sumuje się do zera minus koszty. Do tego 126 lat danych przypomina, że premia akcji jest realna, ale wypłacana nieregularnie i tylko tym, którzy przetrwają posuchy. Rebalancing pilnuje, żeby wybrany profil ryzyka nie rozjechał się z faktycznym, a horyzont i tolerancja ryzyka są wejściami, bez których żadna tabela premii nie wskaże właściwego podziału.

Gdy następnym razem ktoś powie, że badania dowodzą, iż 90% wyniku to alokacja, można odpowiedzieć uprzejmie i precyzyjnie: zależy, o które z trzech pytań chodzi, bo odpowiedzi brzmią 90, 40 i 100, a każda mówi co innego.

To nie jest porada inwestycyjna. To edukacyjne omówienie badań o alokacji aktywów: liczby pochodzą z cytowanych prac, dotyczą przeszłości i konkretnych prób badawczych, a historyczne premie nie są obietnicą przyszłych.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
