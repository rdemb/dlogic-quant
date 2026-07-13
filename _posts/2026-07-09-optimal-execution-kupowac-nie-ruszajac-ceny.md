---
title: "Optimal execution. Jak kupić dużo, nie ruszając ceny"
description: "Jak zrealizować duże zlecenie, nie rujnując sobie ceny. Market impact dzieli się na część chwilową, zależną od tempa realizacji, i trwałą, zależną od całkowitej ilości. Model Almgrena i Chrissa formalizuje kompromis między wpływem na cenę a ryzykiem czasu jako minimalizację oczekiwanego kosztu plus lambda razy jego wariancja. TWAP rozkłada zlecenie równo w czasie, VWAP proporcjonalnie do wolumenu. Źródła: Almgren i Chriss, Lehalle, Bouchaud, Farmer i Lillo."
date: 2026-07-09 21:30:00 +0200
eyebrow: "Edukacja · egzekucja"
dek: "Duże zlecenie ma własny cień: rzucone naraz rusza cenę przeciw sobie, rozłożone w czasie wystawia się na to, że cena ucieknie. Tekst rozkłada kompromis między pośpiechem a wpływem na cenę: dwa koszty egzekucji, model Almgrena i Chrissa jako formalny rozjazd między nimi oraz TWAP i VWAP jako proste harmonogramy. Mechanizm i wzór, nie konkretne liczby."
readingTime: 8
tags: ["optimal execution", "market impact", "Almgren-Chriss", TWAP, VWAP, egzekucja, mikrostruktura, "implementation shortfall", slippage, Lehalle, "Bouchaud-Farmer-Lillo", "prawo pierwiastka", quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Realizacja dużego zlecenia to gra między dwoma kosztami, które ciągną w przeciwne strony. Pośpiech płaci market impactem: bierzesz płynność szybciej, niż rynek ją odbudowuje, i ruszasz cenę przeciw sobie. Cierpliwość płaci ryzykiem czasu: im dłużej się realizujesz, tym większa szansa, że zmienność odsunie cenę, zanim skończysz. Zmniejszenie jednego kosztu zwiększa drugi.
> - Sam impact ma dwie warstwy. Część chwilowa zależy od tempa i znika, gdy przestajesz naciskać, bo arkusz się odbudowuje. Część trwała zależy od całkowitej ilości i zostaje, bo rynek czyta twój przepływ jako informację i przesuwa poziom równowagi. Harmonogram realizacji walczy głównie z częścią chwilową i z ryzykiem czasu.
> - Model Almgrena i Chrissa (2000) zamienia ten kompromis w liczbę: wybierz harmonogram, który minimalizuje oczekiwany koszt plus λ razy jego wariancja, gdzie λ to awersja do ryzyka. Małe λ daje realizację wolną i równą, duże λ realizację szybką i załadowaną z przodu. Każdy sensowny plan leży na tej granicy między impactem a ryzykiem czasu.
> - TWAP rozkłada zlecenie równo w czasie, VWAP proporcjonalnie do spodziewanego wolumenu, grubo na otwarciu i zamknięciu, chudo w środku dnia. To problem instytucji, ale nauka jest dla każdego: koszt zależy od rozmiaru zlecenia względem płynności, więc nie wchodzi się całością w cienki rynek.

**Teza w jednym zdaniu:** Realizacja dużego zlecenia to nie problem kierunku, tylko problem tempa, bo każda jednostka pośpiechu kupowana jest wpływem na cenę, a każda jednostka cierpliwości ryzykiem, że cena ucieknie, i cała sztuka polega na świadomym wyborze punktu między tymi dwoma kosztami.

## Problem: duże zlecenie ma własny cień

Kiedy chcesz kupić lub sprzedać ilość małą względem płynności rynku, cena praktycznie się nie rusza. Wchodzisz po tym, co widzisz, i tyle. Problem zaczyna się, gdy zlecenie jest duże względem tego, co rynek jest w stanie wchłonąć w danej chwili. Wtedy pojawia się zjawisko, które w mikrostrukturze nazywa się market impact: samo twoje kupowanie podbija cenę, a sprzedawanie ją dociska. Handlujesz przeciw sobie.

Rynek nie trzyma nieograniczonej liczby ofert po najlepszej cenie. Arkusz zleceń ma skończoną głębokość: kilka ofert blisko, potem coraz dalej. Jeśli walniesz cały wolumen naraz, zjadasz kolejne poziomy arkusza i realizujesz się po coraz gorszych cenach. Twoja średnia cena realizacji jest gorsza od ceny, którą widziałeś w momencie decyzji. Ta różnica to koszt egzekucji, w literaturze nazywany implementation shortfall.

Naturalny odruch jest taki: skoro walnięcie wszystkiego naraz jest drogie, to rozłóżmy zlecenie na kawałki i sączmy je powoli. To działa na impact, ale otwiera drugi front. Przez cały czas, gdy realizujesz zlecenie po kawałku, cena żyje własnym życiem. Może pójść w twoją stronę, ale równie dobrze może uciec. Im dłużej się realizujesz, tym większe ryzyko, że zanim skończysz, rynek będzie zupełnie gdzie indziej.

To jest sedno problemu optimal execution: pośpiech kosztuje wpływem na cenę, cierpliwość kosztuje ryzykiem czasu, i nie da się mieć obu naraz.

## Dwa koszty, które ciągną w przeciwne strony

Warto rozpisać oba koszty osobno, bo cała reszta to już tylko ich ważenie.

Pierwszy koszt to market impact. Rośnie z tempem realizacji. Im więcej chcesz zrealizować w jednostce czasu, tym głębiej wchodzisz w arkusz i tym mocniej ruszasz cenę przeciw sobie. Impact jest w dużej mierze pod twoją kontrolą, bo to twoje własne zlecenie go generuje. Zwalniasz, płacisz mniej impactu.

Drugi koszt to ryzyko czasu, czyli niepewność związana ze zmiennością rynku w trakcie realizacji. Rośnie z długością okna realizacji. Im dłużej trzymasz niezrealizowaną część pozycji, tym dłużej jesteś wystawiony na to, że cena odjedzie. Tego kosztu nie kontrolujesz, bo bierze się ze zmienności rynku, nie z twojego zlecenia. Możesz go tylko skrócić, realizując się szybciej.

I tu jest zgrzyt. Jedyny sposób na zmniejszenie impactu to zwolnić. Jedyny sposób na zmniejszenie ryzyka czasu to przyspieszyć. Te dwie dźwignie są tą samą dźwignią, przesuwaną w przeciwne strony. Nie istnieje harmonogram, który minimalizuje oba koszty jednocześnie. Istnieje tylko rodzina kompromisów.

<figure>
<svg viewBox="0 0 680 380" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><title>Kompromis egzekucji Almgrena i Chrissa</title><text x="34" y="28" font-size="13" fill="currentColor" opacity="0.85">Kompromis egzekucji: koszt łączny ma minimum w optymalnym tempie</text><g stroke="currentColor" opacity="0.15"><line x1="186.4" y1="52" x2="186.4" y2="300"/><line x1="298.8" y1="52" x2="298.8" y2="300"/><line x1="411.2" y1="52" x2="411.2" y2="300"/><line x1="523.6" y1="52" x2="523.6" y2="300"/><line x1="74" y1="238" x2="636" y2="238"/><line x1="74" y1="176" x2="636" y2="176"/><line x1="74" y1="114" x2="636" y2="114"/></g><line x1="74" y1="52" x2="74" y2="300" stroke="currentColor" stroke-width="1.2" opacity="0.6"/><line x1="74" y1="300" x2="636" y2="300" stroke="currentColor" stroke-width="1.2" opacity="0.6"/><path d="M70 60 L74 52 L78 60" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.6"/><path d="M628 296 L636 300 L628 304" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.6"/><text transform="rotate(-90 28 176)" x="28" y="176" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">koszt egzekucji</text><text x="80" y="317" font-size="10.5" fill="currentColor" opacity="0.6">wolno</text><text x="630" y="317" font-size="10.5" fill="currentColor" opacity="0.6" text-anchor="end">szybko</text><text x="355" y="333" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">tempo realizacji zlecenia</text><polyline points="74,171.9 130.2,196.2 186.4,218 242.6,237.2 270.7,245.9 298.8,253.9 355,268 411.2,279.5 467.4,288.5 523.6,294.9 579.8,298.7 636,300" fill="none" stroke="#e5484d" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><polyline points="74,300 130.2,297.6 186.4,290.5 242.6,278.6 270.7,270.9 298.8,262 355,240.6 411.2,214.4 467.4,183.5 523.6,147.9 579.8,107.5 636,62.3" fill="none" stroke="#0b66c3" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/><polyline points="74,171.9 130.2,193.8 186.4,208.5 242.6,215.8 270.7,216.7 298.8,215.8 355,208.6 411.2,193.9 467.4,172 523.6,142.8 579.8,106.2 636,62.3" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round" opacity="0.9"/><line x1="270.7" y1="216.7" x2="270.7" y2="300" stroke="#1a9e6a" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.75"/><circle cx="270.7" cy="216.7" r="5.5" fill="#1a9e6a"/><circle cx="270.7" cy="216.7" r="5.5" fill="none" stroke="currentColor" stroke-width="1.4" opacity="0.2"/><text x="270.7" y="200" font-size="11.5" fill="#1a9e6a" font-weight="600" text-anchor="middle">optymalne tempo</text><g><line x1="120" y1="356" x2="146" y2="356" stroke="#0b66c3" stroke-width="2.6"/><text x="152" y="360" font-size="11.5" fill="currentColor" opacity="0.78">wpływ na rynek</text><line x1="300" y1="356" x2="326" y2="356" stroke="#e5484d" stroke-width="2.6"/><text x="332" y="360" font-size="11.5" fill="currentColor" opacity="0.78">ryzyko czasu</text><line x1="452" y1="356" x2="478" y2="356" stroke="currentColor" stroke-width="3.2" opacity="0.9"/><text x="484" y="360" font-size="11.5" fill="currentColor" opacity="0.78">koszt łączny</text></g></svg>
<figcaption>Niebieska krzywa to wpływ na rynek, rosnący z tempem realizacji, a czerwona to ryzyko czasu, malejące z tempem. Ich suma, pogrubiona krzywa U, ma wyraźne minimum, które wyznacza optymalne tempo egzekucji w duchu modelu Almgrena i Chrissa.</figcaption>
</figure>

## Impact ma dwie warstwy: chwilową i trwałą

Zanim zbudujemy harmonogram, trzeba rozłożyć sam impact na dwie części, bo zachowują się zupełnie inaczej.

Część chwilowa to natychmiastowy koszt tego, że w tej konkretnej chwili bierzesz płynność szybciej, niż rynek ją odbudowuje. Zależy od tempa: im agresywniej realizujesz dany kawałek, tym gorszą cenę dostajesz na tym kawałku. Ale to znika. Gdy przestajesz naciskać, arkusz się odbudowuje, a cena wraca do poprzedniego poziomu. Ten koszt płacisz tylko za transakcję, która go wywołała.

Część trwała to przesunięcie ceny, które zostaje po tym, jak już przestałeś handlować. Rynek interpretuje twój przepływ jako informację (ktoś kupuje, może coś wie) i przesuwa poziom równowagi. Ta część zależy nie od tempa, tylko od całkowitej ilości, którą przeprowadziłeś przez rynek. Zostaje z tobą i z każdym, kto handluje po tobie.

```
impact chwilowy   =  zależy od TEMPA realizacji;      znika, gdy przestajesz naciskać (arkusz się odbudowuje)
impact trwały     =  zależy od CAŁKOWITEJ ilości;     zostaje po zakończeniu handlu (rynek przesuwa poziom równowagi)
```

To rozróżnienie jest praktyczne, nie akademickie. Częścią chwilową sterujesz tempem: realizuj wolniej, a arkusz nadąży się odbudować między kawałkami. Część trwała zależy od tego, ile w sumie chcesz przełożyć, więc jedyny sposób na jej zmniejszenie to zmniejszyć zlecenie. Harmonogram realizacji walczy głównie z częścią chwilową i z ryzykiem czasu, bo tylko na to ma realny wpływ.

## Almgren i Chriss: harmonogram jako policzalny kompromis

W 2000 roku Robert Almgren i Neil Chriss w pracy "Optimal Execution of Portfolio Transactions" zamienili ten kompromis w problem, który da się rozwiązać liczbami. Ich pomysł: potraktuj harmonogram realizacji jako ciąg decyzji, ile zrealizować w każdym kolejnym oknie czasu, i wybierz ten ciąg, który minimalizuje oczekiwany koszt plus karę za ryzyko.

```
minimalizuj:   E[koszt] + λ · Var[koszt]

E[koszt]     rośnie, gdy realizujesz SZYBCIEJ   (impact: własny nacisk na cenę)
Var[koszt]   rośnie, gdy realizujesz WOLNIEJ    (ryzyko czasu: zmienność σ na niezrealizowanej pozycji)
λ            awersja do ryzyka: ile oczekiwanego kosztu godzisz się zapłacić za jednostkę mniej ryzyka
```

Serce tego wzoru to jedna litera: λ. To współczynnik awersji do ryzyka, twój świadomy wybór, jak bardzo boisz się zmienności w trakcie realizacji.

W modelu z liniowym impactem oczekiwany koszt składa się z części trwałej (proporcjonalnej do całości zlecenia) i chwilowej (proporcjonalnej do tempa realizacji), a wariancja jest proporcjonalna do zmienności rynku razy suma kwadratów niezrealizowanej pozycji w kolejnych oknach. Im dłużej trzymasz duży niezrealizowany kawałek, tym większy jego wkład do wariancji.

Rozwiązanie ma elegancki kształt: optymalny harmonogram to malejąca krzywa niezrealizowanej pozycji, opadająca wykładniczo, o tempie opadania rosnącym z λ.

```
xⱼ  ∝  sinh( κ · (T − tⱼ) )      niezrealizowana pozycja: krzywa opadająca do zera w czasie T
κ   ∝  √( λ · σ² / η )           tempo opadania krzywej

λ = awersja do ryzyka,   σ = zmienność rynku,   η = koszt impactu chwilowego (cieńszy rynek to większe η)
```

Większe κ oznacza realizację bardziej załadowaną z przodu, czyli szybszą. Mniejsze κ oznacza realizację równiejszą, czyli wolniejszą. Innymi słowy, im bardziej boisz się ryzyka czasu (duże λ) albo im bardziej zmienny jest rynek (duże σ), tym szybciej domykasz zlecenie. Im droższy jest impact chwilowy (duże η), tym bardziej rozciągasz realizację w czasie, żeby na nim oszczędzić.

## Efektywna granica: od realizacji wolnej do szybkiej

Almgren i Chriss zauważyli, że różne wartości λ dają rodzinę harmonogramów, którą można narysować jak granicę efektywną z teorii portfela Markowitza, tylko osiami są tu oczekiwany koszt i jego wariancja.

Na jednym końcu jest λ równe zero, czyli obojętność na ryzyko. Wtedy liczy się jedynie minimalizacja oczekiwanego kosztu, więc realizujesz najwolniej, jak się da, równo rozkładając zlecenie, żeby maksymalnie oszczędzić na impakcie. Płacisz najmniej oczekiwanego kosztu, ale bierzesz na siebie najwięcej ryzyka czasu.

Na drugim końcu jest λ bardzo duże, czyli silna awersja. Wtedy najważniejsze jest jak najszybsze pozbycie się ekspozycji, więc ładujesz realizację z przodu, płacąc wysoki impact w zamian za krótkie okno wystawienia na zmienność.

Żaden z tych punktów nie jest obiektywnie najlepszy. To nie jest wybór między dobrą a złą strategią, tylko między dwoma rodzajami kosztu. Wybór λ to deklaracja, ile impactu godzisz się zapłacić, żeby skrócić ryzyko czasu. Model nie mówi, gdzie stanąć na tej granicy. Mówi tylko, że każdy sensowny harmonogram leży właśnie na niej, a nie w środku, gdzie płaci się i za jedno, i za drugie naraz.

## TWAP i VWAP: dwa proste harmonogramy

Pełny model Almgrena i Chrissa wymaga oszacowania parametrów impactu i zmienności. W praktyce większość realizacji chodzi po dwóch prostych heurystykach, które są szczególnymi przypadkami tej samej idei.

TWAP (Time-Weighted Average Price) rozkłada zlecenie równo w czasie. Dzielisz je na równe kawałki i realizujesz jeden co stały interwał, aż do końca okna. To dokładnie ten harmonogram, który wypada z modelu przy zerowej awersji do ryzyka i stałej płynności: prosta, opadająca liniowo linia niezrealizowanej pozycji. Zaleta to prostota i przewidywalność. Wada to ignorowanie faktu, że płynność nie jest stała w ciągu dnia.

VWAP (Volume-Weighted Average Price) rozkłada zlecenie proporcjonalnie do spodziewanego wolumenu. Realizujesz więcej wtedy, gdy rynek jest grubszy, a mniej, gdy jest cienki. Wolumen intraday ma zwykle kształt litery U: gruby na otwarciu i przy zamknięciu, chudy w środku dnia. VWAP jedzie po tym profilu, żeby każdy kawałek trafiał w moment największej płynności i tym samym generował najmniejszy impact. Cel praktyczny: zrealizować się blisko średniej ceny ważonej wolumenem, czyli nie odstawać od tego, co i tak działo się na rynku.

Różnica w jednym zdaniu: TWAP pyta tylko o zegar, VWAP pyta o zegar i o to, gdzie akurat jest płynność. Oba mają ten sam cel co model Almgrena i Chrissa, czyli rozłożyć zlecenie tak, żeby nie ruszać własnej ceny, tylko robią to prostszymi regułami, bez jawnego parametru awersji do ryzyka.

## Rynek trawi powoli

Skąd w ogóle wiadomo, że rozkładanie zlecenia w czasie działa? Odpowiedź daje nurt badań mikrostruktury, który najlepiej streszcza tytuł pracy Bouchauda, Farmera i Lillo: "How Markets Slowly Digest Changes in Supply and Demand". Rynki trawią zmiany podaży i popytu powoli.

Ich obserwacja jest z pozoru paradoksalna. Przepływ zleceń jest silnie autoskorelowany: jeśli ktoś teraz kupuje, to prawdopodobnie za chwilę też będzie kupował, bo duże zlecenia są cięte na kawałki i sączone godzinami. A mimo to ceny pozostają w przybliżeniu nieprzewidywalne. Gdyby impact każdego kawałka był trwały i natychmiastowy, ta autokorelacja przepływu przekładałaby się na przewidywalny trend cen, który dałoby się łatwo wykorzystać. Tak się nie dzieje.

Rozwiązaniem tej zagadki jest impact przejściowy: wpływ pojedynczego zlecenia nie jest ani czysto chwilowy, ani czysto trwały, tylko zanika w czasie. Rynek stopniowo wchłania każdy kawałek, cena częściowo się cofa, i dlatego seria skorelowanych zleceń nie buduje przewidywalnego trendu. To empiryczne uzasadnienie, dlaczego cierpliwa realizacja jest tańsza: dając rynkowi czas między kawałkami, pozwalasz mu odbudować płynność i pochłonąć twój przepływ, zamiast spychać cenę kaskadą.

Z tego nurtu pochodzi też jedna z najbardziej odpornych regularności empirycznych w całym tradingu: prawo pierwiastka. Wpływ dużego zlecenia na cenę rośnie mniej więcej jak pierwiastek z jego rozmiaru mierzonego względem dziennego wolumenu, przeskalowany zmiennością. Podwojenie rozmiaru zlecenia nie podwaja impactu, tylko mnoży go mniej więcej przez pierwiastek z dwóch. Koszt rośnie więc wolniej niż zlecenie, ale rośnie nieubłaganie i robi się dotkliwy dokładnie wtedy, gdy zlecenie staje się liczącym się ułamkiem dziennego wolumenu. Nie podaję tu współczynników, bo zależą od rynku i estymacji, ale sam kształt, pierwiastek zamiast linii prostej, jest zadziwiająco uniwersalny w różnych klasach aktywów.

## Co z tego przy małym rachunku

Optimal execution brzmi jak problem wyłącznie instytucji, które przepychają przez rynek pozycje warte tyle, co ułamek dziennego obrotu. I owszem, cała maszyneria TWAP, VWAP i harmonogramów Almgrena i Chrissa powstała dla takich graczy, a praktyczną stronę tych algorytmów szczegółowo opisuje Lehalle w literaturze o mikrostrukturze i tradingu intraday. Ale mechanizm, który za nią stoi, jest skalowalny w dół i dotyczy każdego, kto handluje na rynku o skończonej płynności.

Lekcja pierwsza: rozmiar zlecenia liczy się względem płynności, nie w wartościach bezwzględnych. Ten sam wolumen, który jest niezauważalny na EURUSD w środku sesji londyńskiej, potrafi ruszyć cenę na egzotyku albo na tym samym EURUSD w cienkim oknie w niedzielny wieczór. Prawo pierwiastka mówi wprost, że kosztem rządzi stosunek twojego zlecenia do dziennego wolumenu.

Lekcja druga: nie wchodź całością w cienki rynek. Jeśli twoje zlecenie jest duże względem tego, co akurat stoi w arkuszu, walnięcie go naraz to dobrowolne zjadanie kolejnych poziomów i realizacja po gorszej średniej. To ta sama część chwilowa impactu, tylko na twoją skalę.

Lekcja trzecia jest najgłębsza i wykracza poza samą egzekucję: pośpiech i cierpliwość mają ceny, które ciągną w przeciwne strony, a świadomy trader wybiera punkt między nimi zamiast udawać, że wybór nie istnieje. Wejście po rynku natychmiast płaci impactem i spreadem, wejście zleceniem z limitem oszczędza na tym, ale ryzykuje, że cena ucieknie bez ciebie. To dokładnie ten sam kompromis co u Almgrena i Chrissa, tylko na jedno kliknięcie.

To nie jest porada inwestycyjna. To wykład mechanizmu egzekucji: dwóch kosztów, które ciągną w przeciwne strony, oraz formalnego sposobu ich ważenia, żeby było jasne, dlaczego rozmiar zlecenia względem płynności jest osobną decyzją, obok kierunku i momentu wejścia.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
