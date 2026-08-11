---
layout: post
title: "Nie buduję bota. Buduję system, który ma prawo powiedzieć: „nie wiem”"
description: "Dlaczego system tradingowy powinien najpierw nauczyć się odrzucać własne złudzenia, zanim otrzyma prawo do ryzykowania kapitału."
dek: "Architektura może być imponująca, testy zielone, a backtest atrakcyjny - i nadal może nie istnieć żadna przewaga."
category: algo
eyebrow: "D-LOGIC Chronicle #01"
readingTime: 12
cover: risk
---
<div class="article-status"><span class="primary">MANIFEST</span><span>RESEARCH / SHADOW</span><span>MODEL EDGE: UNPROVEN</span><span>LIVE: NOT AUTHORIZED</span></div>

Najbardziej niebezpieczny moment w budowie systemu tradingowego nie pojawia się wtedy, gdy kod przestaje działać, test kończy się błędem albo połączenie z brokerem zostaje zerwane. Znacznie groźniejsza jest chwila, w której wszystko wygląda poprawnie: testy są zielone, wykres wyników staje się atrakcyjny, model zachowuje się logicznie, a człowiek zaczyna wierzyć, że znalazł coś, czego rynek jeszcze nie wycenił.

Właśnie wtedy system może przestać być narzędziem badawczym i stać się maszyną do produkowania przekonujących złudzeń.

Przez kolejne etapy budowałem własne środowisko tradingowe, które zaczynało od kilku wyspecjalizowanych modeli rynku walutowego. Jeden próbował rozpoznawać kierunkowe zmiany, drugi szukał powrotu do średniej, a kolejny reagował na statystycznie nietypowe ruchy. Nad nimi znajdowała się warstwa określająca reżim rynku, natomiast pomiędzy modelem i zleceniem pozostawał człowiek.

Już wtedy pojawiła się idea, która przetrwała wszystkie późniejsze pivoty: **model nie powinien próbować działać zawsze**.

Sygnał może mieć sens w jednym reżimie, a stać się bezużyteczny po zmianie zmienności, płynności, zachowania uczestników albo kosztu wykonania. Zamiast więc pytać wyłącznie, czy dany sygnał działa, zacząłem pytać, kiedy w ogóle ma prawo działać.

## Architektura nie jest przewagą

Z czasem system obrósł w modele mikrostruktury, mechanizmy oceny reżimu, filtry ryzyka, warstwy agregacji, relacje między instrumentami oraz próby wykorzystania AI do interpretacji szerszego kontekstu. W pewnym okresie projekt zbliżył się nawet do idei detalicznego HFT i market makingu.

Architektura wyglądała ambitnie. Problem polegał na tym, że ambitna architektura nie jest jeszcze przewagą rynkową.

Lokalna pętla programu może działać szybko, ale zlecenie nadal musi przejść przez system operacyjny, sieć, infrastrukturę brokera i mechanizm realizacji. Do tego dochodzą opóźnienia danych, kolejka zleceń, adverse selection, poślizg oraz ryzyko, że widoczna płynność zniknie przed dotarciem zlecenia.

Kilka milisekund zaoszczędzonych w kodzie nie tworzy automatycznie przewagi nad uczestnikami posiadającymi kolokację, bezpośredni dostęp do giełdy i pełniejszy obraz książki zleceń.

To wymusiło rozróżnienie dwóch rzeczy, które w projektach tradingowych często są ze sobą mylone:

- dobrze zaprojektowanego frameworku,
- mechanizmu posiadającego dodatnią wartość oczekiwaną po wszystkich kosztach.

Można stworzyć imponujący system wieloagentowy, rozbudowany dashboard i adaptacyjne zarządzanie ryzykiem, a mimo to nie posiadać ani jednej przewagi możliwej do wykonania w realnym środowisku.

## Najładniejszy backtest może być najbardziej niebezpiecznym wynikiem

Backtest przedstawia uporządkowaną historię. Pokazuje moment wejścia, późniejszy ruch ceny, wynik transakcji i krzywą kapitału, która z dzisiejszej perspektywy wydaje się logiczna.

Rynek w czasie rzeczywistym nie daje jednak dostępu do zakończonej historii. W chwili decyzji przyszłość nie jest jeszcze podzielona na prawidłowo opisane reżimy, potwierdzone ekstrema i świece, o których wiemy już, że były punktem zwrotnym.

Wystarczy subtelne przesunięcie informacji w czasie, aby model zaczął korzystać z wiedzy, której w rzeczywistości nie mógł posiadać. Leakage może powstać w targecie, cesze, sposobie normalizacji albo selekcji najlepszego wariantu spośród tak dużej liczby prób, że któryś niemal na pewno wygląda wyjątkowo przez przypadek.

Inny problem pojawia się wtedy, gdy strategia osiąga dodatni wynik nie dlatego, że przewiduje rynek, ale dlatego, że instrument w badanym okresie posiadał określony dryf. Model może wyglądać na skuteczny, chociaż wykonuje jedynie bardziej skomplikowaną wersję ekspozycji kierunkowej.

Dlatego D-LOGIC ma zadawać sygnałowi serię niewygodnych pytań:

- Czy informacja była dostępna dokładnie w momencie decyzji?
- Czy wynik utrzymuje się po realistycznych kosztach?
- Czy przewaga istnieje poza okresem, w którym model został wymyślony?
- Czy prostszy baseline osiąga podobny wynik?
- Czy placebo uzyskuje to samo?
- Czy rezultat przetrwał korektę na liczbę wykonanych prób?
- Czy sygnał da się zrealizować przy rzeczywistym spreadzie, poślizgu i ograniczeniach wykonania?

Jeżeli system nie potrafi odpowiedzieć, prawidłowym wynikiem nie jest BUY ani SELL.

Prawidłowym wynikiem jest **UNKNOWN**.

## Prawo do abstencji

Wiele prostych botów projektuje się tak, aby zawsze posiadały opinię. Jeżeli wskaźnik przekracza próg, pojawia się kupno; jeżeli spada poniżej innego poziomu, pojawia się sprzedaż. Niepewność zostaje zredukowana do liczby, a liczba natychmiast zamienia się w zlecenie.

Rynek nie ma jednak obowiązku codziennie oferować przewidywalnej okazji, która po kosztach pasuje do konkretnego środowiska i sposobu wykonania. Dlatego abstencja nie jest w D-LOGIC awarią ani brakiem zdecydowania. Jest pełnoprawną decyzją systemową.

Model może rozpoznać interesującą strukturę, ale jednocześnie ocenić, że jego wiarygodność jest zbyt niska. Prognoza może być statystycznie atrakcyjna, ale niewykonalna przy bieżącym spreadzie. Kierunek może być poprawny, natomiast relacja potencjalnej korzyści do minimalnego ryzyka może pozostać nieakceptowalna.

System ma więc nie tylko przewidywać. Musi również wiedzieć, kiedy nie powinien ufać własnej prognozie.

Jednym z rozwijanych kierunków jest odrębna warstwa oceniająca wiarygodność modeli. Jej zadaniem nie jest przewidywanie ceny w identyczny sposób jak model podstawowy, ale ocena, czy bieżące warunki nadal przypominają środowisko, w którym model był testowany.

Pełna definicja tej warstwy, zestaw cech, funkcja celu i sposób agregacji pozostają prywatne. Publiczna jest zasada: **system powinien równocześnie prognozować rynek i szacować, czy posiada podstawy, aby własnej prognozie zaufać**.

## Trzy problemy, których nie wolno mieszać

Obecna filozofia D-LOGIC rozdziela proces na trzy klasy problemów.

Pierwszą jest nauka. Tutaj powstają hipotezy, cechy, targety, testy placebo, procedury walidacji oraz rejestr wyników negatywnych. Żaden atrakcyjny wykres nie powinien zostać uznany za odkrycie, dopóki nie przejdzie właściwej ścieżki dowodowej.

Drugą jest stan rynku. Przewidywalność nie musi być trwałą cechą strategii; może pojawiać się lokalnie, zależeć od reżimu, przepływu, relacji między instrumentami oraz jakości bieżących danych.

Trzecią jest wykonanie. Nawet poprawna prognoza może prowadzić do straty, jeśli nie przetrwa spreadu, poślizgu, opóźnienia, finansowania i reguł brokera.

Z tego powodu model badawczy nie może przejść bezpośrednio do zlecenia. Prognoza musi najpierw przejść przez ocenę stanu rynku, a następnie przez osobną kontrolę wykonalności i ryzyka.

> **Prediction edge i execution edge są dwoma różnymi problemami.**

## Rynek jako sieć czujników

Jednym z bardziej eksperymentalnych kierunków jest odejście od traktowania każdego instrumentu wyłącznie jako niezależnej okazji transakcyjnej.

Duże środowisko może zawierać setki symboli, ale nie oznacza to, że każdy powinien być bezpośrednio handlowany. Część może pełnić rolę celu, część źródła informacji, część punktu odniesienia, natomiast inne mogą być nieprzydatne z powodu kosztów, płynności albo konstrukcji kontraktu.

Instrument, którego nie warto kupować, może nadal przekazywać informację o szerokości rynku, dyspersji, zachowaniu sektora lub zmianie relacji między regionami. Universe przestaje wtedy być listą tickerów i staje się siecią sensorów.

Publicznie będę opisywał pytania badawcze stojące za tym podejściem, ale nie dokładne konstrukcje cech, schemat ważenia źródeł ani prywatny routing predykcji.

## Pierwszym zadaniem systemu jest nie kłamać o własnych danych

Model może być wyrafinowany matematycznie, a mimo to uczyć się na niekompletnym, nadpisanym albo źle zsynchronizowanym zbiorze. W takim przypadku kolejne warstwy inteligencji zwiększają jedynie precyzję, z jaką system analizuje fałszywą rzeczywistość.

Dlatego część aktualnej pracy nie polega na trenowaniu kolejnego modelu, ale na utwardzaniu narzędzi, które mają zbierać i publikować dowody. Niepełny snapshot, duplikaty, mieszanie przebiegów, nadpisanie artefaktu czy niezgodność deklarowanej i faktycznej zawartości powinny kończyć się twardym odrzuceniem.

Najważniejszym osiągnięciem takiego etapu nie jest dodanie inteligencji. Jest nim ograniczenie liczby sposobów, na jakie system może przekonać badacza, że posiada prawidłowe dane, chociaż w rzeczywistości ich nie posiada.

## AI jako zespół badawczy, nie zarządzający kapitałem

D-LOGIC rozwijam przy intensywnym wykorzystaniu narzędzi AI, ale ich role pozostają rozdzielone. Jedna warstwa pomaga analizować kod i artefakty, inna wspiera research, projektowanie eksperymentów oraz red-team. Ostateczna decyzja, odpowiedzialność i kontrola ryzyka pozostają po stronie operatora.

Żaden model językowy nie powinien posiadać bezpośredniej drogi do wysłania zlecenia tylko dlatego, że wygenerował przekonujące uzasadnienie. Płynność języka nie jest pewnością statystyczną.

Nie buduję systemu, w którym AI ma zawsze rację. Buduję system, w którym kilka niezależnych warstw próbuje wykazać, że może się mylić.

## Co będę publikował

Publiczna kronika nie będzie repozytorium kompletnego systemu ani instrukcją jego odtworzenia. Będę publikował genezę projektu, zmiany architektoniczne, problemy badawcze, kryteria falsyfikacji, wyniki negatywne, status gate’ów i granice twierdzeń.

Nie będę publikował danych rachunku, wielkości kapitału, pełnych wzorów, zestawów cech, wag, progów, funkcji celu, konfiguracji bezpieczeństwa ani reguł egzekucji umożliwiających bezpośrednie skopiowanie rozwiązania.

Transparentność dotyczy sposobu dowodzenia, nie rezygnacji z własności intelektualnej.

## Gdzie projekt znajduje się dzisiaj

D-LOGIC nie jest obecnie gotowym systemem live i nie będę przedstawiał go jako maszyny posiadającej udowodnioną przewagę. Nie ma jeszcze podstaw, aby publicznie twierdzić, że istnieje potwierdzony model edge, wystarczający forward albo gotowy pełny łańcuch wykonawczy.

Nie jest to zastrzeżenie dodane drobnym drukiem. To aktualny wynik procesu badawczego.

Kolejne przejścia mają własne kryteria. Test offline nie będzie przedstawiany jako działanie w runtime. Dobry zbiór danych nie będzie dowodem alfy. OOS nie stanie się automatycznie forwardem, a forward nie będzie oznaczał gotowości live bez osobnej walidacji wykonania i ryzyka.

W tej kronice słowo „zbudowałem” oznacza, że artefakt istnieje. „Przetestowałem” oznacza, że eksperyment posiada protokół. „Odrzuciłem” wymaga spełnienia kryterium falsyfikacji. „Odkryłem” pozostaje zarezerwowane dla wyniku, który przeszedł właściwą ścieżkę dowodową.

Nie chcę tworzyć legendy o genialnej maszynie, która pewnego dnia pojawiła się w gotowej postaci. Chcę zachować historię tego, jak ambitna wizja była rozbijana na mierzalne problemy, testowana, falsyfikowana i rekonstruowana w system, który ma coraz mniej sposobów, aby oszukiwać własnego twórcę.

D-LOGIC ma kiedyś podejmować decyzje na rynku. Zanim jednak otrzyma prawo do ryzykowania kapitału, musi nauczyć się podejmować decyzję znacznie trudniejszą:

> **Nie mam wystarczających dowodów.**

Od tego zaczyna się ta kronika.
