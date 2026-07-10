---
title: "Algorytmy. Anatomia czarnej skrzynki"
description: "Algorytm transakcyjny to zautomatyzowana reguła decyzyjna, nie magia. Klasy strategii różnią się źródłem zarobku: market making sprzedaje natychmiastowość i zbiera spread, arbitraż domyka różnice cen tej samej rzeczy, arbitraż statystyczny gra na powrocie spreadów do średniej, trend i mean reversion to dwa przeciwne zakłady o zachowanie ceny, a TWAP i VWAP tylko obniżają koszt realizacji. Do tego wyścig latencji według Budisha, Cramtona i Shima (QJE 2015), anatomia systemu od danych po monitoring oraz flash crash z 6 maja 2010 według wspólnego raportu SEC i CFTC."
date: 2026-07-05 16:00:00 +0200
eyebrow: "Edukacja · systemy"
dek: "Słowo algorytm robi w tradingu za zaklęcie: raz jest obietnicą maszynki do pieniędzy, raz straszakiem, który rzekomo poluje na każdego detalistę. Tekst otwiera czarną skrzynkę i pokazuje, co w niej naprawdę siedzi: klasy strategii rozróżnione po źródle zarobku, szkielet systemu od danych po monitoring, wyścig zbrojeń o milisekundy i dzień, w którym elektroniczna płynność wyparowała w kwadrans. Mechanizmy i udokumentowane liczby, zero obietnic."
readingTime: 9
tags: ["algotrading", "systemy transakcyjne", "market making", "arbitraż statystyczny", "trend following", "mean reversion", HFT, "wyścig latencji", "Budish Cramton Shim", "flash crash", "SEC CFTC", Narang, "Ernest Chan", Menkveld, "151 Trading Strategies", TWAP, VWAP, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Algo to nie magia, tylko reguła decyzyjna zapisana w kodzie i wykonywana bez ręcznego klikania. Klasy strategii różnią się źródłem zarobku: market making sprzedaje natychmiastowość i zbiera spread, arbitraż domyka różnice cen tej samej rzeczy, arbitraż statystyczny gra na powrocie spreadów do średniej, trend i mean reversion to dwa przeciwne zakłady o zachowanie ceny, a algorytmy egzekucyjne typu TWAP i VWAP w ogóle nie zarabiają, tylko obniżają koszt realizacji cudzej decyzji.
> - Wyścig latencji nie jest wybrykiem chciwości, tylko konsekwencją konstrukcji rynku. Budish, Cramton i Shim (QJE 2015) pokazali na parze ES i SPY, że mediana czasu życia okazji arbitrażowej spadła z około 97 milisekund w 2005 roku do około 7 milisekund w 2011, ale zysk z pojedynczej okazji pozostał mniej więcej stały. Szybkość zmienia to, kto wygrywa, nie to, ile jest do wygrania, więc ciągła księga zleceń wymusza kosztowny wyścig zbrojeń.
> - W realnym systemie sygnał to mniejszość pracy. Łańcuch wygląda tak: dane, sygnał, sizing, egzekucja, monitoring, i to jakość danych, model kosztów oraz dyscyplina produkcyjna decydują, czy strategia przeżyje zetknięcie z rynkiem. Systemy umierają z czterech powodów: koszty zjadają cienki edge, konkurencja eroduje przewagę, overfitting produkuje zyski, których nigdy nie było, a zmiana reżimu unieważnia założenia.
> - 6 maja 2010 amerykańskie indeksy straciły kilka procent w kilka minut i odbiły. Wspólny raport SEC i CFTC opisał kaskadę: automat wolumenowy sprzedający 75 tysięcy kontraktów E-mini w nerwowym rynku, wycofanie się animatorów, ponad 20 tysięcy transakcji po cenach odchylonych o 60 procent i więcej, później anulowanych. Elektroniczna płynność bywa iluzją dokładnie wtedy, gdy jest najbardziej potrzebna.

**Teza w jednym zdaniu:** Algorytm transakcyjny to zautomatyzowana reguła, którą da się rozłożyć na źródło zarobku, koszty i infrastrukturę, a po takim rozłożeniu okazuje się, że klasy strategii różnią się głównie tym, komu i za co wystawiają rachunek, oraz że większość przewag jest cienka, śmiertelna i droższa w utrzymaniu, niż wygląda z zewnątrz.

## Czarna skrzynka otwiera się od zwykłej strony

Rishi Narang zatytułował swój przewodnik po funduszach kwantowych "Inside the Black Box" trochę przekornie, bo główna teza książki brzmi: czarna skrzynka po otwarciu wygląda znajomo. Systemy kwantowe nie robią niczego, czego nie próbowałby robić dobry trader uznaniowy. Robią to samo, tylko systematycznie: reguła jest spisana wprost, przetestowana na danych i wykonywana przez maszynę bez negocjacji z emocjami. Zdanie "kupuj, gdy cena zamknięcia jest powyżej średniej z ostatnich dwustu sesji, w przeciwnym razie trzymaj gotówkę" to już jest algorytm transakcyjny. Serwery, kolokacja i języki programowania to inżynieria wokół reguły, nie jej istota.

Z tej perspektywy pytanie "czy algotrading działa" jest źle postawione, bo algorytm to forma, nie treść. Sensowne pytanie brzmi: skąd ta konkretna reguła bierze pieniądze i kto jest po drugiej stronie. To jest najważniejsza mapa tego tekstu: klasy strategii różnią się między sobą źródłem zarobku, a nie stopniem magii. Katalog Kakushadzego i Serura "151 Trading Strategies" opisuje sto pięćdziesiąt jeden strategii w kilkunastu klasach aktywów, od akcji i obligacji po kryptowaluty i instrumenty pogodowe, i lektura tego spisu działa odczarowująco: pozycji jest dużo, ale rodzin mało. Wciąż te same mechanizmy w różnych kostiumach.

## Sześć klas, sześć źródeł zarobku

```
klasa                   źródło zarobku                             główne ryzyko
market making           spread za dostarczanie natychmiastowości   zapas + adverse selection
arbitraż czysty         ta sama rzecz w dwóch cenach               wyścig latencji, ryzyko jednej nogi
arbitraż statystyczny   powrót spreadu koszyka do średniej         relacja się psuje, spread ucieka dalej
trend / momentum        kontynuacja rozpoczętego ruchu             piła w rynku bocznym
mean reversion          powrót ceny po przereagowaniu              rzadkie, ale głębokie straty
egzekucja (TWAP/VWAP)   brak; obniża koszt realizacji              mierzona do benchmarku, nie zyskiem
```

Market making to sprzedawanie natychmiastowości. Animator wystawia jednocześnie ofertę kupna i sprzedaży i liczy, że przepływ zleceń będzie się przewalał przez jego kwotowania w obie strony, a on z każdej pary transakcji zbierze spread. To wynagrodzenie za usługę: kto chce zawrzeć transakcję natychmiast, płaci temu, kto czekał z gotową ofertą. Menkveld w przeglądzie ekonomii HFT w Annual Review of Financial Economics opisuje współczesnych animatorów jako firmy obracające ogromnym wolumenem przy marżach na pojedynczej transakcji tak cienkich, że o wyniku decydują dwa ryzyka. Pierwsze to ryzyko zapasu: gdy rynek jedzie w jedną stronę, animator kupuje od wszystkich, którzy sprzedają, i zostaje z rosnącą pozycją przeciwko ruchowi, dlatego zawodowcy trzymają zapas blisko zera i kończą dzień praktycznie na płasko. Drugie, groźniejsze, to adverse selection: ten, kto trafia w twoje kwotowanie, może wiedzieć więcej od ciebie. Spread zbiera się od niedoinformowanych, a oddaje poinformowanym, i cała ekonomia animowania sprowadza się do tego, żeby pierwszych było więcej niż drugich.

Arbitraż czysty to najprostsze źródło z listy: ta sama rzecz w dwóch miejscach w dwóch różnych cenach. ETF kontra koszyk akcji, z których się składa, kontrakt terminowy kontra rynek kasowy, ta sama spółka na dwóch giełdach. Kupujesz taniej, sprzedajesz drożej, różnica jest twoja i w teorii pozbawiona ryzyka. W praktyce różnice są mikroskopijne, znikają w milisekundy i bije się o nie garstka najszybszych firm świata. Kto przychodzi drugi, nie dostaje nic albo zostaje z jedną wypełnioną nogą transakcji i niechcianą ekspozycją. Dla wszystkich poza technologiczną czołówką ta klasa praktycznie nie istnieje.

Arbitraż statystyczny rozluźnia definicję: nie ta sama rzecz, ale rzeczy statystycznie powiązane. Dwie akcje z jednej branży, koszyk instrumentów, spread, który historycznie oscyluje wokół średniej. Gdy spread odjeżdża od normy, system sprzedaje drogą nogę, kupuje tanią i czeka na powrót. Ernest Chan poświęca temu warsztatowi dużą część "Algorithmic Trading": testy stacjonarności, kointegracja, tempo powrotu do średniej. Kluczowa różnica względem arbitrażu czystego: powrót nie jest gwarantowany. Relacja między instrumentami to statystyczna regularność, nie prawo fizyki, i potrafi się zepsuć na dobre, a spread, który "musiał" wrócić, potrafi najpierw odjechać dwa razy dalej.

Trend following i momentum to zakład, że ruch, który się zaczął, ma ciąg dalszy: kupuj to, co rosło, sprzedawaj to, co spadało, zwykle na horyzoncie tygodni i miesięcy, na szerokim koszyku rynków, bo wyraźny trend na pojedynczym rynku zdarza się rzadko. Mean reversion to zakład dokładnie odwrotny: cena po gwałtownym przereagowaniu ma wracać do normy. Obie klasy mogą działać równolegle, bo grają na różnych horyzontach i w różnych warunkach, ale mają lustrzane profile bólu. Trend myli się często i po trochu, a wygrywa rzadko i dużo. Mean reversion wygrywa często i po trochu, a myli się rzadko i boleśnie, gdy przereagowanie okazuje się początkiem nowego świata.

Osobną klasą są algorytmy egzekucyjne: TWAP, VWAP i ich krewni. One nie mają poglądu na rynek i nie zarabiają ani grosza. Rozkładają cudze duże zlecenie w czasie tak, żeby zminimalizować koszt realizacji: równo po zegarze (TWAP) albo proporcjonalnie do spodziewanego wolumenu (VWAP). Mierzy się je nie zyskiem, tylko odchyleniem od benchmarku egzekucyjnego. Mechanika tego problemu, market impact i kompromis między pośpiechem a ryzykiem czasu, jest rozebrana osobno w [tekście o optimal execution](/dlogic-quant/2026/07/09/optimal-execution-kupowac-nie-ruszajac-ceny/). Ta klasa wróci jeszcze w roli czarnego charakteru, bo to właśnie algorytm egzekucyjny stał w centrum flash crashu.

## Wyścig zbrojeń, którego nikt nie może opuścić

Budish, Cramton i Shim w pracy z Quarterly Journal of Economics (2015) pokazali, że wyścig latencji nie jest patologią chciwości, tylko logiczną konsekwencją konstrukcji rynku: ciągłej księgi zleceń, która przetwarza zlecenia sekwencyjnie. Kto pierwszy, ten lepszy, zawsze i wszędzie, więc bycie pierwszym ma cenę rynkową.

Ich materiał dowodowy jest elegancki. Kontrakt E-mini na S&P 500 w Chicago i ETF SPY w Nowym Jorku to niemal ta sama ekspozycja. Na horyzoncie minut ich ceny są skorelowane prawie doskonale, ale na horyzoncie milisekund korelacja praktycznie znika, bo informacja dociera do obu rynków w różnym tempie. Każde takie chwilowe rozjechanie to mechaniczna okazja arbitrażowa. Liczby: mediana czasu życia takiej okazji spadła z około 97 milisekund w 2005 roku do około 7 milisekund w 2011, ale zysk z pojedynczej okazji pozostał w tym okresie mniej więcej stały. Konkurencja na szybkość nie zmniejszyła nagrody, skróciła tylko okno, w którym się ją zgarnia. Wyścig wyłania zwycięzcę, ale nie obniża rachunku, który płaci reszta rynku.

Stąd nakłady, które z zewnątrz wyglądają absurdalnie. Autorzy otwierają pracę historią kabla Spread Networks: około 300 milionów dolarów za nowy światłowód między Chicago a New Jersey, który skrócił podróż sygnału w obie strony z około 16 do około 13 milisekund. Po światłowodach przyszły łącza mikrofalowe, bo sygnał w powietrzu biegnie szybciej niż w szkle, a dziś różnice mierzy się w nanosekundach na poziomie sprzętu i kolokacji.

Najciekawszy jest mechanizm, który zmusza do udziału nawet niechętnych. Kwotowanie animatora, które po nowej informacji nie zdążyło się zaktualizować, przez ułamek sekundy jest nieaktualne i najszybsi gracze snajpersko je zdejmują, zanim właściciel je wycofa. Animator nie może tego zignorować: albo sam zainwestuje w szybkość, żeby zdążać z wycofywaniem, albo wkalkuluje straty ze snipingu w szerszy spread, który zapłacą wszyscy. Budish, Cramton i Shim proponują wyjście konstrukcyjne: częste aukcje wsadowe, czyli rynek rozstrzygany co ułamek sekundy zamiast w trybie ciągłym, co zamienia wyścig o kolejność w konkurencję ceną. Rynki w większości zostały przy księdze ciągłej, ale ta praca ustawiła debatę: wyścig latencji to koszt projektu rynku, nie zła wola uczestników.

## Anatomia systemu: od pomysłu do produkcji

W wyobraźni początkującego system transakcyjny to sygnał, czyli sekretna formuła mówiąca, kiedy kupić. W praktyce sygnał jest jednym z pięciu klocków i rzadko tym, który pochłania najwięcej pracy.

```
DANE         zdobycie, czyszczenie, strefy czasowe, korekty o splity i dywidendy, łatanie luk
SYGNAŁ       reguła zamieniająca dane w decyzję: kupić, sprzedać, nic nie robić
SIZING       ile na tę decyzję postawić: ryzyko na transakcję, limity ekspozycji, korelacje pozycji
EGZEKUCJA    jak zamienić decyzję na wypełnione zlecenia, nie oddając przewagi w koszty
MONITORING   czy system na żywo robi to samo, co w teście, i kiedy go zatrzymać
```

Narang rozkłada część decyzyjną jeszcze drobniej: obok modelu alfa, który prognozuje, skąd ma przyjść zysk, stoi model ryzyka, który mówi, czego nie wolno, oraz model kosztów transakcyjnych, który wycenia każdą zmianę pozycji. Dopiero złożenie tych trzech w konstrukcję portfela decyduje, co i ile kupić, a osobny moduł egzekucji zamienia to na zlecenia. Ta rozbiórka ma praktyczny morał: model ryzyka i model kosztów nie dodają ani grosza zysku, a bez nich system nie przeżywa, bo alfa bywa cienka i niepewna, natomiast koszty i wpadki są pewne.

Druga prawda produkcyjna: większość czasu zjadają dane i monitoring, nie sygnał. Dane trzeba wyczyścić, wyrównać strefy czasowe, skorygować o zdarzenia korporacyjne i pilnować, żeby test nie podglądał przyszłości. Chan poświęca pułapkom backtestu całe rozdziały: look-ahead bias, survivorship bias, testowanie na cenach, po których nie dało się handlować. A po starcie na żywo zaczyna się najmniej romantyczna część pracy: porównywanie każdej transakcji z tym, co system powinien był zrobić w symulacji, bo rozjazd między teorią a produkcją to pierwszy sygnał, że coś pękło. Feed, broker, płynność albo sama przewaga.

## Dlaczego systemy umierają

Naturalnym stanem strategii jest śmierć i warto mieć listę przyczyn zgonu przed faktem, nie po nim.

Pierwsza: koszty zjadają cienki edge. Większość realnych przewag po stronie sygnału jest mała, rzędu ułamków spreadu na transakcję, więc rachunek za spread, prowizje i poślizg potrafi zjeść całość. Strategia zyskowna przy kosztach zerowych i martwa po kosztach to nie wyjątek, tylko najczęstszy wynik uczciwego testu. Dlatego u Naranga model kosztów jest osobnym klockiem systemu, a Chan każe wyceniać koszty pesymistycznie, zanim policzy się cokolwiek innego.

Druga: przewaga eroduje, bo konkurencja ją zauważa. Edge to w gruncie rzeczy czyjś błąd albo czyjaś powolność. Im więcej kapitału go eksploatuje, tym szybciej znika, a publikacja pomysłu w literaturze potrafi przyspieszyć wygasanie.

Trzecia: overfitting, czyli przewaga, której nigdy nie było. Kto przetestuje dostatecznie wiele wariantów, temu najlepszy z nich będzie wyglądał świetnie czystym przypadkiem; taki wynik jest artefaktem szukania, nie właściwością rynku. To temat na osobny wykład i taki wykład już tu jest: [tekst o Deflated Sharpe](/dlogic-quant/2026/07/09/dlaczego-twoj-sharpe-klamie-deflated-sharpe/) rozkłada data snooping i test na overfitting na czynniki pierwsze.

Czwarta: zmiana reżimu. Parametry strategii są zawsze wyestymowane na jakimś świecie, z określoną zmiennością, płynnością i polityką banków centralnych. Gdy świat się zmienia, strategia gra dalej według starych reguł. Chan ostrzega przed tym wprost przy strategiach powrotu do średniej: potrafią latami zbierać drobne wygrane i oddać skumulowany wynik w jednym epizodzie zmiany reżimu.

Wniosek ze wszystkich czterech przyczyn naraz: produktem firmy kwantowej nie jest strategia, tylko proces badawczy, który stale produkuje nowe strategie i uśmierca stare.

## Flash crash: kwadrans, w którym płynność wyparowała

6 maja 2010 roku amerykańskie indeksy spadły o kilka procent w kilka minut i odbiły niemal równie szybko. Dow Jones był w najgorszym momencie dnia blisko 1000 punktów pod kreską, najwięcej w ujęciu punktowym w trakcie jednej sesji do tamtej pory. Wspólny raport SEC i CFTC "Findings Regarding the Market Events of May 6, 2010" zrekonstruował ten dzień na danych transakcyjnych i do dziś jest najlepszym darmowym podręcznikiem tego, jak umiera elektroniczna płynność.

Rynek od rana był nerwowy: kryzys zadłużenia w Europie, rosnąca zmienność, malejąca głębokość arkuszy. Po godzinie 14:30 duży gracz instytucjonalny zaczął sprzedawać 75 tysięcy kontraktów E-mini na S&P 500, wartych około 4,1 miliarda dolarów, przez automat egzekucyjny nakierowany na 9 procent wolumenu z poprzedniej minuty, bez żadnego warunku na cenę ani czas. Zlecenia porównywalnej skali ten sam podmiot rozkładał wcześniej na długie godziny; tym razem automat wykonał program w około 20 minut. Sprzężenie było podręcznikowe: sprzedaż podbijała wolumen, a wyższy wolumen kazał automatowi sprzedawać jeszcze szybciej, dokładnie wtedy, gdy chętnych do kupowania ubywało.

Po drugiej stronie stali głównie animatorzy wysokich częstotliwości, którzy najpierw amortyzowali podaż, a potem, w miarę puchnięcia zapasów i rosnącego chaosu, zaczęli się wycofywać albo agresywnie pozbywać pozycji. Raport opisuje czternaście sekund, w których gracze HFT wymienili między sobą ponad 27 tysięcy kontraktów E-mini, zmieniając łączną pozycję netto ledwie o około 200 kontraktów: gorący kartofel podawany w kółko, wolumen ogromny, absorpcja praktycznie zerowa. O 14:45:28 mechanizm Stop Logic na CME wstrzymał handel kontraktem na 5 sekund i ta krótka pauza wystarczyła, żeby po obu stronach księgi znów pojawiły się realne zlecenia.

W akcjach było gorzej, bo kaskada rozlała się przez arbitraż między kontraktem, ETF i pojedynczymi spółkami dokładnie w chwili, gdy animatorzy akcyjni odpuścili. Część z nich zostawiła w księgach tylko tak zwane stub quotes, techniczne kwotowania po cenach w rodzaju jednego centa albo stu tysięcy dolarów, które nigdy nie miały zostać wykonane. Zostały wykonane. Raport zlicza ponad 20 tysięcy transakcji w ponad trzystu papierach zawartych po cenach odchylonych o 60 procent i więcej od poziomów sprzed kilku minut; giełdy anulowały je później jako ewidentnie błędne.

Lekcja z 6 maja nie brzmi "algorytmy są złe". Lekcja brzmi: płynność elektroniczna jest warunkowa. W spokojnym rynku arkusz wygląda na głęboki, bo animatorzy konkurują o przepływ; w stresie nikt nie ma obowiązku stać po drugiej stronie i głębokość znika w sekundy, dokładnie wtedy, gdy jest najbardziej potrzebna. Wolumen to nie to samo co płynność, a automat egzekucyjny bez warunku na cenę będzie sprzedawał w dziurę bez dna, bo nikt mu nie kazał sprawdzić, komu sprzedaje.

## Uczciwa perspektywa dla detalisty

Po tej wycieczce łatwiej uczciwie odpowiedzieć na pytanie, które zwykle stoi za zainteresowaniem algotradingiem: czy gracz indywidualny może w to wejść?

W wyścig latencji: nie. Konkurencja ma kolokację przy serwerach giełdy, łącza mikrofalowe między miastami, sprzęt strojony do nanosekund i zespoły, które robią to zawodowo. Market making, czysty arbitraż i wszystko, co rozstrzyga się poniżej sekundy, to gra, w której detalista technologicznie nie bierze udziału, a próba brania udziału oznacza bycie tym wolniejszym, od którego szybsi zarabiają.

Mapa klas pokazuje jednak, gdzie przewaga detalisty w ogóle może istnieć, jeśli istnieje: nie w szybkości, tylko w horyzoncie i cierpliwości. Mały kapitał mieści się w strategiach o pojemności zbyt małej, żeby opłacały się funduszowi, i Chan wskazuje właśnie takie nisze jako naturalny teren gracza indywidualnego. Detalista nie ma comiesięcznego rozliczenia przed inwestorami, więc może utrzymać horyzont, na którym instytucja nie utrzyma pozycji ze względów karierowych, nie rynkowych. I nie musi handlować wcale, co jest luksusem nieosiągalnym dla animatora.

Trzeźwa rama na koniec: automatyzacja nie tworzy przewagi, tylko ją egzekwuje. Reguła bez źródła zarobku po zautomatyzowaniu jest tą samą regułą bez źródła zarobku, wykonywaną szybciej, taniej i bardziej konsekwentnie, również w traceniu. Dlatego pytanie "jaki program do algotradingu" jest zawsze wtórne wobec pytania "skąd ta reguła bierze pieniądze i dlaczego nikt ich jeszcze nie zabrał".

To nie jest porada inwestycyjna. To mapa mechanizmów: co siedzi w czarnej skrzynce, z czego żyją poszczególne klasy strategii, dlaczego szybkość stała się osobnym przemysłem i co się dzieje, gdy elektroniczna płynność znika, żeby słowo algorytm przestało być zaklęciem, a stało się listą sprawdzalnych pytań.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
