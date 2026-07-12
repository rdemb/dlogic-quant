---
title: "Procesy stochastyczne: błądzenie losowe i ruch Browna"
description: "Proces stochastyczny jako rodzina zmiennych losowych w czasie; błądzenie losowe i dlaczego ceny są do niego bliskie (hipoteza rynku efektywnego, Fama 1970); martyngał, czyli oczekiwana przyszła wartość równa bieżącej, i jego związek z brakiem łatwej przewagi; ruch Browna (proces Wienera) jako ciągła granica błądzenia, z ciągłymi ścieżkami, niezależnymi przyrostami i wariancją rosnącą liniowo z czasem, skąd skala pierwiastka czasu; geometryczny ruch Browna jako model ceny w wycenie Blacka i Scholesa. Źródła: Bachelier 1900, Einstein 1905, Samuelson 1965, Shreve."
date: 2026-07-11 15:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Od definicji procesu stochastycznego do modelu, na którym stoi wycena opcji. Błądzenie losowe i jego ciągła granica, czyli ruch Browna; martyngał jako matematyczny zapis gry sprawiedliwej i braku łatwej przewagi z samej przeszłości ceny; liniowy wzrost wariancji i wynikająca z niego reguła pierwiastka czasu; geometryczny ruch Browna, dryf i zmienność. Z twardym zastrzeżeniem: to idealizacja, a prawdziwe ceny mają grube ogony, zmienną zmienność i skoki."
readingTime: 8
tags: [matematyka, "procesy stochastyczne", "błądzenie losowe", "ruch Browna", "proces Wienera", martyngał, "geometryczny ruch Browna", "Black-Scholes", "hipoteza rynku efektywnego", Bachelier, Samuelson, Shreve, quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Proces stochastyczny to rodzina zmiennych losowych indeksowana czasem; jego pojedyncza realizacja to ścieżka, na przykład jeden przebieg kursu. Zanim ścieżka się zrealizuje, jest tylko rozkład możliwości, po realizacji zostaje jedna linia z nieskończenie wielu.
> - Błądzenie losowe: kolejna wartość to poprzednia powiększona o niezależny szok o zerowej średniej. Bachelier (1900) pierwszy użył go do opisu cen, a obserwowana bliskość cen do błądzenia jest tłem hipotezy rynku efektywnego w ujęciu Famy (1970).
> - Martyngał: oczekiwana przyszła wartość, przy pełnej dostępnej informacji, równa się wartości bieżącej. To matematyczny zapis gry sprawiedliwej i braku łatwej przewagi opartej wyłącznie na przeszłości ceny (Samuelson 1965).
> - Ruch Browna, czyli proces Wienera, to ciągła granica błądzenia losowego: ścieżki ciągłe, przyrosty niezależne, wariancja rośnie liniowo z czasem, więc typowy rozrzut skaluje się jak pierwiastek z czasu. Fizyczny opis dał Einstein (1905), finansowy wyprzedził go Bachelier (1900).
> - Geometryczny ruch Browna, w którym błądzeniu podlega logarytm ceny, to model instrumentu bazowego w wycenie opcji Blacka i Scholesa (1973), a jego postać dla cen spopularyzował Samuelson (1965). Ma dwa parametry: dryf i zmienność. Ścisły wykład daje podręcznik Shreve'a.

**Teza w jednym zdaniu:** Ceny bywają modelowane jako błądzenie losowe, którego ciągłą granicą jest ruch Browna; własność martyngału tłumaczy, dlaczego z samej przeszłości ceny trudno o przewagę, a liniowy wzrost wariancji, skala pierwiastka czasu i geometryczny ruch Browna stoją u podstaw wyceny opcji, przy czym jest to model, a nie wierny obraz rynku.

## Proces stochastyczny: losowość rozłożona w czasie

Proces stochastyczny to rodzina zmiennych losowych indeksowana czasem. Dla każdej chwili istnieje osobna zmienna losowa, opisująca możliwe stany układu w tym momencie, a cały proces spina te zmienne w jeden obiekt rozciągnięty w czasie. Pojedyncze losowanie całego procesu daje jedną ścieżkę, czyli konkretny przebieg: jeden wykres kursu albo jedną trajektorię cząstki. Zanim ścieżka się zrealizuje, istnieje tylko rozkład możliwości, a po realizacji zostaje jedna linia z wielu, które mogły powstać.

To odróżnia proces stochastyczny od funkcji deterministycznej: funkcja przypisuje czasowi jedną wartość, a proces cały rozkład, z którego wykres pokazuje jedną próbkę. Dwa najważniejsze dla rynków przykłady to błądzenie losowe w czasie dyskretnym oraz ruch Browna w czasie ciągłym.

## Błądzenie losowe i dlaczego ceny są blisko niego

Najprostszym procesem tego rodzaju jest błądzenie losowe. Kolejna wartość to poprzednia powiększona o niezależny, losowy szok o zerowej średniej.

```
Błądzenie losowe (czas dyskretny):
    X_t = X_{t-1} + e_t

    e_t = niezależne szoki o zerowej średniej (biały szum)
    brak stałej średniej, wariancja rośnie z czasem
    szok e_t wchodzi w poziom na trwałe (brak powrotu do średniej)
```

Trzy własności są tu kluczowe. Błądzenie nie ma stałej średniej, do której wraca. Jego wariancja rośnie z czasem, więc im dłuższy horyzont, tym szerszy wachlarz możliwych położeń. I każdy szok wchodzi w poziom na trwałe, ponieważ nowe położenie staje się punktem wyjścia dla następnego kroku.

Pomysł, by traktować ceny jak taki proces, jest starszy, niż się zwykle sądzi. Louis Bachelier w rozprawie o teorii spekulacji (1900) opisał wahania cen na paryskiej giełdzie modelem, który dziś rozpoznaje się jako błądzenie losowe i jego ciągłą granicę. Praca wyprzedziła fizykę i przez dekady pozostawała w cieniu. Do myślenia o rynkach wróciła w połowie dwudziestego wieku, gdy empiryczne badania kursów pokazały, że zmiany cen są bardzo słabo przewidywalne z samej przeszłości, a wykres ceny przypomina realizację błądzenia.

Jest to bliskość, nie tożsamość. Tłem jest hipoteza rynku efektywnego w ujęciu Famy (1970): jeśli cena szybko wchłania dostępną informację, to przewidywalna część przyszłego ruchu jest już w niej zawarta, a zostaje głównie nieprzewidywalny szok. Obserwowana bliskość cen do błądzenia losowego nie jest więc założeniem wygody rachunkowej, tylko konsekwencją tego, że łatwe do wykorzystania regularności są wymazywane przez samych uczestników rynku. Słowo bliskie jest jednak istotne, bo rzeczywiste ceny odchylają się od czystego błądzenia, o czym dalej.

## Martyngał: brak łatwej przewagi w języku matematyki

Ściślejszym pojęciem niż błądzenie losowe jest martyngał. Proces jest martyngałem, gdy jego oczekiwana wartość w następnej chwili, przy pełnej dostępnej dziś informacji, równa się wartości bieżącej.

```
Martyngał (proces {X_t} wobec informacji F_t):
    E[ X_{t+1} | F_t ] = X_t

    najlepsza prognoza przyszłej wartości = wartość dzisiejsza
    warunkowa średnia przyrostu X_{t+1} − X_t = 0 (gra sprawiedliwa)
```

Warunek wygląda skromnie, a niesie mocną treść. Najlepsza prognoza jutrzejszej wartości to wartość dzisiejsza, a oczekiwany przyrost, warunkowo, wynosi zero. W języku hazardu to definicja gry sprawiedliwej: znajomość całej przeszłości nie pozwala przewidzieć kierunku następnego ruchu lepiej niż rzut monetą. Właśnie dlatego martyngał jest matematycznym zapisem braku łatwej, systematycznej przewagi opartej wyłącznie na historii ceny.

Związek z rynkiem sformalizował Samuelson w pracy o tym, że poprawnie antycypowane ceny wahają się losowo (1965). Argument jest subtelny: martyngałem nie musi być sama cena, lecz cena odpowiednio zdyskontowana, przy neutralnej względem ryzyka wycenie. Model dopuszcza zatem dryf, czyli średni trend wynagradzający ryzyko, a mimo to zachowuje własność, że sama przeszłość nie daje darmowej prognozy kierunku. Martyngał nie mówi, że rynek nie rośnie. Mówi, że ta część ruchu, którą da się przewidzieć z przeszłości, w cenie efektywnej jest już rozliczona.

Warto rozróżnić dwa pojęcia, które łatwo pomylić. Błądzenie losowe zakłada, że kolejne przyrosty są niezależne i mają jednakowy rozkład. Martyngał wymaga mniej, bo tylko tego, by warunkowa średnia przyrostu była zerowa, dopuszczając na przykład zmienną w czasie zmienność. Każde błądzenie losowe bez dryfu jest martyngałem, ale nie każdy martyngał jest błądzeniem losowym. Dla rynków to rozróżnienie jest wygodne, ponieważ realna zmienność faktycznie skupia się w klastry, więc słabsze założenie martyngału bywa bliższe danym.

## Ruch Browna jako granica błądzenia

Gdy w błądzeniu losowym kroki stają się coraz częstsze i coraz mniejsze, a ich skalę dobiera się właściwie, proces w granicy przechodzi w ruch Browna, nazywany także procesem Wienera od nazwiska matematyka, który podał jego ścisłą konstrukcję. To ciągła w czasie wersja błądzenia i centralny obiekt rachunku stochastycznego.

<figure>
<svg viewBox="0 0 640 350" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="24" font-size="13" fill="currentColor">Błądzenie losowe: kilka ścieżek z jednego punktu</text><text x="34" y="42" font-size="11" fill="currentColor" opacity="0.6">im dłuższy czas, tym szerszy wachlarz możliwych ścieżek</text><line x1="95" y1="52" x2="95" y2="292" stroke="currentColor" stroke-width="1" opacity="0.35"/><line x1="95" y1="292" x2="610" y2="292" stroke="currentColor" stroke-width="1" opacity="0.35"/><line x1="95" y1="170" x2="600" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="1 4" opacity="0.45"/><text x="606" y="174" font-size="10" fill="currentColor" opacity="0.7">E[X]</text><path d="M95 170 L126.6 145 L158.1 134.6 L189.7 126.7 L221.25 120 L284.4 108.8 L347.5 99.3 L410.6 90.9 L473.75 83.4 L536.9 76.5 L600 70" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="6 5" opacity="0.55"/><path d="M95 170 L126.6 195 L158.1 205.4 L189.7 213.3 L221.25 220 L284.4 231.2 L347.5 240.7 L410.6 249.1 L473.75 256.6 L536.9 263.5 L600 270" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="6 5" opacity="0.55"/><path d="M95 170 L120 176 L145 170 L170 178 L195 172 L220 180 L245 174 L270 168 L295 176 L320 170 L345 164 L370 172 L395 166 L420 174 L445 168 L470 160 L495 168 L520 162 L545 156 L570 164 L595 158 L600 158" fill="none" stroke="#0b66c3" stroke-width="1.5" opacity="0.7"/><path d="M95 170 L120 178 L145 172 L170 184 L195 190 L220 182 L245 192 L270 200 L295 194 L320 204 L345 210 L370 202 L395 212 L420 220 L445 214 L470 224 L495 218 L520 228 L545 234 L570 226 L595 236 L600 238" fill="none" stroke="#0b66c3" stroke-width="1.5" opacity="0.7"/><path d="M95 170 L120 164 L145 172 L170 166 L195 174 L220 182 L245 176 L270 186 L295 194 L320 188 L345 198 L370 206 L395 214 L420 208 L445 218 L470 228 L495 236 L520 244 L545 238 L570 248 L595 256 L600 258" fill="none" stroke="#0b66c3" stroke-width="1.5" opacity="0.7"/><path d="M95 170 L120 168 L145 160 L170 166 L195 158 L220 152 L245 160 L270 154 L295 148 L320 156 L345 150 L370 144 L395 152 L420 146 L445 140 L470 148 L495 142 L520 136 L545 130 L570 138 L595 132 L600 130" fill="none" stroke="#0b66c3" stroke-width="1.5" opacity="0.7"/><path d="M95 170 L120 162 L145 168 L170 156 L195 150 L220 158 L245 146 L270 138 L295 144 L320 132 L345 126 L370 134 L395 122 L420 116 L445 108 L470 114 L495 104 L520 96 L545 102 L570 92 L595 86 L600 85" fill="none" stroke="#1a9e6a" stroke-width="2.2"/><circle cx="95" cy="170" r="3" fill="currentColor" opacity="0.75"/><text x="58" y="173" font-size="10" fill="currentColor" opacity="0.6">start</text><text x="548" y="306" font-size="10.5" fill="currentColor" opacity="0.7">czas t →</text><line x1="95" y1="317" x2="113" y2="317" stroke="#1a9e6a" stroke-width="2.2"/><text x="118" y="321" font-size="10.5" fill="currentColor" fill-opacity="0.85">ścieżka wyróżniona</text><line x1="250" y1="317" x2="268" y2="317" stroke="#0b66c3" stroke-width="1.5"/><text x="273" y="321" font-size="10.5" fill="currentColor" fill-opacity="0.85">błądzenie losowe</text><line x1="405" y1="317" x2="423" y2="317" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4" opacity="0.6"/><text x="428" y="321" font-size="10.5" fill="currentColor" fill-opacity="0.85">obwiednia √t</text><text x="34" y="340" font-size="10" fill="currentColor" fill-opacity="0.6">Środek stoi w miejscu: wartość oczekiwana równa startowi (martyngał). Rozrzut ścieżek rośnie jak √t, nie liniowo.</text></svg>
<figcaption>Ilustracja poglądowa. Pięć realizacji błądzenia losowego wychodzi z jednego punktu, jedna została wyróżniona kolorem. Pozioma linia przerywana to wartość oczekiwana, która nie zmienia się w czasie, co jest istotą martyngału. Przerywana obwiednia pokazuje typowy rozrzut, rosnący jak pierwiastek z czasu, dlatego rozszerza się coraz wolniej, a nie po linii prostej.</figcaption>
</figure>

```
Ruch Browna / proces Wienera W_t:
    W_0 = 0
    ścieżki ciągłe (bez skoków)
    przyrosty niezależne na rozłącznych odcinkach czasu
    W_t − W_s ~ N(0, t − s)          (przyrost normalny, średnia 0)
    Var(W_t) = t                     (wariancja rośnie liniowo)
    odch. std. = pierwiastek(t)      (skala pierwiastka czasu)
```

Własności są następujące. Ścieżki są ciągłe, czyli rysują się bez przeskoków, choć nigdzie nie są gładkie. Przyrosty na rozłącznych odcinkach czasu są niezależne, a rozkład przyrostu zależy tylko od długości odcinka, nie od chwili, w której się zaczyna. Ten rozkład jest normalny o średniej zero. I najważniejsze dla intuicji: wariancja narasta liniowo z czasem, więc odchylenie standardowe, czyli typowy rozrzut, rośnie jak pierwiastek z czasu. Na diagramie widać to jako obwiednię rozszerzającą się coraz wolniej, w tempie pierwiastka, a nie po linii prostej.

Fizyczny rodowód pojęcia jest osobny od finansowego. Einstein (1905) wyjaśnił chaotyczny ruch drobin pyłku w wodzie, obserwowany wcześniej przez botanika Roberta Browna, jako skutek zderzeń z cząsteczkami cieczy i wyprowadził, że średni kwadrat przemieszczenia rośnie liniowo z czasem. To samo prawo pierwiastka czasu, które w finansach opisał wcześniej Bachelier (1900). Dwie odległe dziedziny trafiły na tę samą matematykę, ponieważ obie opisują sumę wielu drobnych, niezależnych wstrząsów. Ścisły wykład tej konstrukcji, wraz z rachunkiem różniczkowym dla takich procesów, daje podręcznik Shreve'a "Stochastic Calculus for Finance".

## Skala pierwiastka: dlaczego czas rządzi zmiennością

Liniowy wzrost wariancji jest cichym bohaterem całej konstrukcji, ponieważ przekłada się wprost na sposób, w jaki skaluje się zmienność. Skoro wariancja jest proporcjonalna do czasu, to odchylenie standardowe jest proporcjonalne do pierwiastka z czasu.

```
Skala pierwiastka czasu (przyrosty niezależne, stała wariancja na jednostkę):
    Var(zmiana w czasie T) = sigma^2 · T
    odch. std.(zmiana w czasie T) = sigma · pierwiastek(T)

    zmienność dzienna → roczna:  sigma_rok = sigma_dzień · pierwiastek(252)
    dwa razy dłuższy horyzont → rozrzut większy pierwiastek(2) raza, nie 2 razy
```

Praktyczna konsekwencja pojawia się wszędzie tam, gdzie porównuje się zmienność na różnych horyzontach. Zmienność dzienną przelicza się na roczną, mnożąc przez pierwiastek z liczby dni handlowych, a nie przez samą liczbę dni. Rozrzut na dwa dni jest większy od dziennego o pierwiastek z dwóch, czyli około czterdziestu procent, a nie dwukrotnie. Ta sama reguła stoi za tym, że pasma oparte na zmienności rozchodzą się parabolicznie, a nie liniowo, oraz za tym, że dłuższy horyzont zwiększa niepewność wolniej, niżby podpowiadała intuicja liniowa. Reguła pierwiastka czasu jest przy tym własnością modelu z niezależnymi przyrostami. Gdy przyrosty są skorelowane, na przykład przy skupianiu się zmienności w klastry, skalowanie odbiega od czystego pierwiastka.

## Geometryczny ruch Browna i Black-Scholes

Zwykły ruch Browna ma wadę jako model ceny: może zejść poniżej zera, ponieważ jego przyrosty są addytywne i normalne. Cena akcji czy pary walutowej poniżej zera nie schodzi. Rozwiązanie polega na przeniesieniu błądzenia z poziomu ceny na jej logarytm. Tak powstaje geometryczny ruch Browna, w którym losowe są procentowe, a nie kwotowe zmiany ceny.

```
Geometryczny ruch Browna (model ceny S_t):
    dS_t = mu · S_t · dt + sigma · S_t · dW_t

    mu    = dryf (średni trend)
    sigma = zmienność (skala losowych wstrząsów)
    log(S_t) podlega ruchowi Browna z dryfem → cena zawsze dodatnia

    na tym stoi wzór Blacka i Scholesa (1973) na wycenę opcji
```

Model ma dwa parametry o czytelnym sensie. Dryf to średni trend, składnik odpowiadający oczekiwanemu tempu wzrostu. Zmienność to skala losowych wstrząsów wokół tego trendu. Ponieważ losowaniu podlega logarytm ceny, sama cena pozostaje dodatnia, a jej rozkład jest logarytmicznie normalny. Taką postać modelu cen spopularyzował Samuelson (1965), poprawiając arytmetyczny model Bacheliera właśnie w punkcie ujemnych cen.

Na geometrycznym ruchu Browna stoi wzór Blacka i Scholesa (1973) na wycenę opcji. Założenie, że cena instrumentu bazowego podlega temu procesowi ze stałą zmiennością, pozwala wyprowadzić cenę opcji jako rozwiązanie równania, w którym przyszłe scenariusze uśrednia się w świecie neutralnym względem ryzyka. Dryf rzeczywisty znika z wyceny, a zostaje zmienność, co tłumaczy, dlaczego to ona jest głównym parametrem, o który toczy się gra na rynku opcji. Rachunek, który to spina, czyli lemat Ito i całka stochastyczna, jest treścią wspomnianego podręcznika Shreve'a.

## Gdzie model się kończy

Cała ta konstrukcja jest rusztowaniem, a nie fotografią rynku. Rzeczywiste ceny odchylają się od geometrycznego ruchu Browna w sposób udokumentowany i systematyczny. Rozkłady zwrotów mają grubsze ogony, niż przewiduje rozkład normalny. Zmienność nie jest stała, tylko skupia się w klastry okresów spokojnych i burzliwych. Bywają też nieciągłe skoki, których ciągła ścieżka Browna z definicji nie ma. Reguła pierwiastka czasu staje się wtedy przybliżeniem, a nie prawem. Podobnie hipoteza rynku efektywnego jest modelem granicznym, bo opisuje rynek, w którym łatwe regularności są już wymazane, a nie stan faktyczny w każdej chwili.

Wartość tych pojęć jest inna. Błądzenie losowe, martyngał i ruch Browna wyznaczają punkt odniesienia, wobec którego mierzy się każdą rzekomą regularność. Zanim uzna się jakąś regularność za realną, trzeba pokazać, że jest czymś więcej niż artefaktem błądzenia, ponieważ błądzenie samo z siebie produkuje trendy, serie i wzory, które kuszą oko. Właśnie dlatego czysta losowość jest hipotezą zerową, a nie ozdobnikiem.

Materiał czysto edukacyjny, nie porada inwestycyjna ani sygnał. Modele opisane wyżej to idealizacje: prawdziwe ceny mają grube ogony, zmienną zmienność i skoki, więc błądzenie losowe oraz ruch Browna są punktem odniesienia, a nie wiernym obrazem rynku. Pewna jest tu wyłącznie matematyka procesów: liniowy wzrost wariancji, wynikająca z niego skala pierwiastka czasu i własność martyngału. Źródła: Bachelier (1900, teoria spekulacji), Einstein (1905, ruch Browna), Samuelson (1965, geometryczny ruch Browna oraz losowość poprawnie antycypowanych cen), Fama (1970, hipoteza rynku efektywnego) i Shreve ("Stochastic Calculus for Finance").

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
