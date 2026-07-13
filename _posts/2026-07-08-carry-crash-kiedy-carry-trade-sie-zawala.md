---
title: "Carry crash. Czemu carry trade zarabia latami i pada w tydzień"
description: "Carry trade, czyli zarabianie na różnicy stóp procentowych między walutami, to jedna z najlepiej udokumentowanych przewag na rynku FX. Tekst tłumaczy jej mechanikę, wyjaśnia, dlaczego działa mimo że podręcznikowa teoria (niepokryty parytet stóp) tego zabrania, i pokazuje ukrytą cenę: ujemny skos rozkładu zwrotów oraz gwałtowne krachy w momentach paniki. Z odniesieniami do prac Brunnermeiera, Nagla i Pedersena oraz Menkhoffa, Sarna, Schmelinga i Schrimpfa."
date: 2026-07-08 18:00:00 +0200
eyebrow: "Edukacja · strategie"
dek: "Carry trade zbiera drobne zyski przez lata, a potem oddaje je w kilka dni. Skąd bierze się przewaga na różnicy stóp, dlaczego działa mimo teorii, która jej zabrania, i czemu jej rozkład zwrotów ma gruby, ujemny ogon. Rzetelnie, na mechanizmach, bez obiecywania liczb."
readingTime: 8
tags: [carry, "carry trade", "carry unwind", "carry crash", "forward premium puzzle", "parytet stóp procentowych", UIP, "premia za ryzyko", "ryzyko ogona", "ujemny skos", "risk-off", Brunnermeier, Menkhoff, zmienność, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Carry trade to inkasowanie różnicy stóp procentowych: pożyczasz walutę nisko oprocentowaną, kupujesz wysoko oprocentowaną, a różnicę zgarniasz przez punkty swapowe. Działa, mimo że podręcznikowa teoria (niepokryty parytet stóp) mówi, że nie powinno, bo waluty wysokoprocentowe przeciętnie nie osłabiają się tak, jak zakłada model. To zagadka premii terminowej.
> - Dodatni średni zwrot nie jest darmowy. To wynagrodzenie za ryzyko globalnej zmienności: carry zarabia spokojnie, dopóki rynek jest spokojny, i obrywa dokładnie wtedy, gdy zmienność skacze, a apetyt na ryzyko znika.
> - Rozkład zysków carry ma ujemny skos: długie pasma drobnych zysków przerywane rzadkimi, brutalnymi stratami. Kiedy nastaje risk-off, wszyscy zamykają te same, zatłoczone pozycje naraz, płynność wysycha i uruchamia się spirala. Rośnie schodami, spada windą.
> - To premia za ryzyko krachu, nie darmowy obiad. Wniosek praktyczny dotyczy ogona: pozycjonowanie i dźwignia muszą zakładać, że rzadka katastrofa przyjdzie, bo Sharpe i zwykła zmienność zaniżają realne ryzyko strategii o ujemnym skosie.

**Teza w jednym zdaniu:** Carry trade zarabia przez lata, bo pobiera premię za gotowość do trzymania pozycji, która załamie się w najgorszym możliwym momencie, więc jego istotą nie jest przewaga bez ryzyka, lecz sprzedawanie ubezpieczenia od paniki, i dlatego rośnie schodami, a spada windą.

## Co to jest carry i skąd bierze się zysk

Carry to najstarsza i najprostsza idea na rynku walutowym: zarabianie na samej różnicy oprocentowania między dwiema walutami. Mechanika jest bezpośrednia. Finansujesz się walutą o niskiej stopie procentowej, zamieniasz ją na walutę o wysokiej stopie i tę wyżej oprocentowaną trzymasz. Dopóki kurs stoi w miejscu, samo utrzymywanie pozycji przynosi różnicę stóp. Na rynku FX ta różnica realizuje się dzień po dniu przez punkty swapowe doliczane lub odejmowane od pozycji trzymanej przez noc. Klasyczne waluty finansujące to te z historycznie najniższymi stopami, na przykład jen japoński czy frank szwajcarski, a po stronie kupowanej stają waluty o wyraźnie wyższym oprocentowaniu.

Atrakcyjność bierze się z tego, że zysk nie wymaga, żeby kurs w ogóle drgnął we właściwą stronę. Wystarczy, że nie ruszy się mocno przeciw pozycji. To sprawia, że przez długie okresy spokoju carry wygląda jak strumień dochodu niemal oderwany od ryzyka kierunkowego. Wrażenie jest jednak mylące i cały ten tekst jest o tym, dlaczego.

## Teoria mówi, że to nie ma prawa działać

W podręczniku carry nie powinno przynosić zysku. Odpowiada za to niepokryty parytet stóp procentowych (UIP). Zakłada on, że rynek walutowy jest efektywny w prosty sposób: skoro wszyscy widzą wyższą stopę w jednej walucie, to jej kurs musi już zawierać oczekiwanie osłabienia o dokładnie tyle, ile wynosi przewaga oprocentowania. Innymi słowy, korzyść z wyższej stopy ma zostać zjedzona przez spodziewany spadek kursu, a oczekiwany zwrot z carry powinien wynosić zero.

Empiria od dekad temu przeczy. Zjawisko nosi nazwę zagadki premii terminowej (forward premium puzzle) i zostało sformalizowane w klasycznej regresji Famy z 1984 roku. Zamiast osłabiać się zgodnie z różnicą stóp, waluty wysokoprocentowe przeciętnie nie osłabiają się dostatecznie, a w wielu okresach wręcz się umacniają. Znak zależności bywa dokładnie odwrotny do tego, co przewiduje UIP. Skutek jest taki, że carry przez długie odcinki historii przynosi dodatni średni zwrot, i to na wielu parach jednocześnie. To nie jest anomalia jednego rynku ani jednej dekady, lecz jeden z najlepiej udokumentowanych faktów empirycznych w finansach międzynarodowych.

Wagę tego wyniku trzeba dobrze zrozumieć. Uporczywe łamanie UIP nie znaczy, że rynek jest głupi. Znaczy, że w kursie walutowym siedzi coś więcej niż tylko oczekiwana zmiana notowania: siedzi tam premia, którą ktoś płaci, a ktoś inny pobiera. Pytanie brzmi, za co.

## Za co naprawdę płaci ta premia

Najmocniejsza odpowiedź jest taka, że zysk z carry to wynagrodzenie za ekspozycję na globalne ryzyko. Menkhoff, Sarno, Schmeling i Schrimpf w pracy "Carry Trades and Global Foreign Exchange Volatility" (2012) pokazali, że zwroty z carry porządkuje jeden czynnik: globalna zmienność walutowa. Waluty wysokoprocentowe, te kupowane w carry, radzą sobie źle dokładnie wtedy, gdy zmienność na świecie rośnie. Waluty finansujące, nisko oprocentowane, zachowują się wtedy odwrotnie, jak bezpieczna przystań. Innymi słowy, carry płaci premię za to, że ładuje na siebie ryzyko złych czasów.

To wpisuje carry w tę samą logikę co inne premie za ryzyko: dostajesz dodatni zwrot w zamian za to, że strategia zawiedzie w najgorszym momencie. Koijen, Moskowitz, Pedersen i Vrugt w pracy "Carry" (2018) uogólnili to pojęcie poza rynek walutowy, na obligacje, surowce i akcje, pokazując, że carry jest ogólną zasadą wyceny, a nie ciekawostką FX. Wspólny mianownik pozostaje ten sam: carry lubi spokój i umiera w panice. Jego zwrot jest sprzężony z globalnym apetytem na ryzyko, więc kiedy rynek przechodzi w tryb risk-off, premia zamienia się w stratę.

## Schodami w górę, windą w dół

Tu jest sedno sprawy, czyli kształt rozkładu zwrotów. Carry nie oddaje ryzyka równomiernie. Jego rozkład ma silnie ujemny skos: bardzo długie pasma małych, regularnych zysków przerywane rzadkimi, ale bardzo dużymi stratami. Krzywa kapitału rośnie łagodnie i spokojnie miesiącami, a potem w kilka dni potrafi zawrócić o wielkość, której zbieranie zajęło lata. Stąd bezlitosne, ale celne porównanie: carry to zbieranie drobniaków przed nadjeżdżającym walcem. I stąd tytułowe: rośnie schodami, spada windą.

Ta asymetria nie jest pechem ani wadą konkretnej pary. Jest wpisana w naturę strategii. Skoro carry pobiera premię za ryzyko krachu, to rozkład jego zwrotów musi wyglądać właśnie tak: dużo małych wygranych za sprzedawanie spokoju i rzadka, potężna wypłata w drugą stronę, kiedy spokój się kończy. Profil ten przypomina pozycję kogoś, kto wystawił opcję albo sprzedał ubezpieczenie: inkasuje regularną składkę, dopóki nie zdarzy się szkoda, a wtedy płaci naraz i dużo.

To ma bezpośrednią konsekwencję dla pomiaru. Wskaźnik Sharpe'a, policzony na spokojnym odcinku, pokaże carry jako znakomitą strategię o gładkiej krzywej. Problem w tym, że Sharpe premiuje niską zmienność i jest ślepy na skos. Strategia, która zarabia gładko, a traci skokowo, będzie miała imponujący Sharpe aż do dnia, w którym go nie ma. Dlatego ocena carry po samej zmienności i po Sharpie jest myląca: ukrywa dokładnie to ryzyko, za które płacona jest premia.

## Anatomia carry unwind

Dlaczego straty przychodzą tak nagle i tak skoncentrowane w czasie? Odpowiedź leży w tym, że carry jest z natury pozycją zatłoczoną i lewarowaną. Skoro premia jest znana i udokumentowana, to bardzo wielu graczy trzyma bardzo podobne pozycje: długo waluty wysokoprocentowe, krótko finansujące. Dopóki jest spokojnie, wszystko działa. Kiedy pojawia się szok i zmienność skacze, zaczyna się to, co rynek nazywa carry unwind.

Mechanizm jest samonapędzający. Wzrost zmienności podnosi wymagania co do zabezpieczeń i uruchamia wezwania do uzupełnienia depozytu. Część graczy musi zamknąć pozycje, co pcha kursy przeciwko wszystkim pozostałym trzymającym to samo. To generuje kolejne straty, kolejne wezwania i kolejne przymusowe zamknięcia. Płynność, obfita w spokoju, wysycha dokładnie wtedy, gdy jest najbardziej potrzebna. Brunnermeier, Nagel i Pedersen w pracy "Carry Trades and Currency Crashes" (2008, NBER w14473) opisali ten związek wprost: waluty o wysokiej różnicy stóp są narażone na ryzyko krachu, a odwroty carry są sprzężone z warunkami płynności finansowania oraz ze skokami zmienności. Samą spiralę płynności, w której straty i topniejąca płynność napędzają się nawzajem, opisali szerzej Brunnermeier i Pedersen.

Kluczowe jest słowo "naraz". Krach carry to nie jest suma niezależnych, drobnych pechów. To jedno zdarzenie, w którym korelacje między parami, w spokojnych czasach umiarkowane, skaczą do jedności. Wszystkie pozycje carry, na różnych walutach, zaczynają spadać razem, bo wszystkie reagują na ten sam czynnik: ucieczkę od ryzyka. Dywersyfikacja po wielu parach carry, która wyglądała solidnie na spokojnym wykresie, w krachu okazuje się iluzją, bo w ogonie wszystko jest ze sobą splecione.

<figure>
<svg viewBox="0 0 720 384" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Profil skumulowanego wyniku carry trade: powolny wzrost premii i nagły krach"><defs><linearGradient id="carryGain" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a9e6a" stop-opacity="0.30"/><stop offset="1" stop-color="#1a9e6a" stop-opacity="0.02"/></linearGradient><linearGradient id="carryLoss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e5484d" stop-opacity="0.06"/><stop offset="1" stop-color="#e5484d" stop-opacity="0.32"/></linearGradient></defs><g stroke="currentColor" stroke-opacity="0.18" stroke-width="1"><line x1="196" y1="48" x2="196" y2="336"/><line x1="328" y1="48" x2="328" y2="336"/><line x1="460" y1="48" x2="460" y2="336"/><line x1="592" y1="48" x2="592" y2="336"/><line x1="64" y1="95" x2="696" y2="95"/><line x1="64" y1="160" x2="696" y2="160"/><line x1="64" y1="225" x2="696" y2="225"/></g><path d="M78,290 H108 V277 H138 V264 H168 V251 H198 V238 H228 V225 H258 V212 H288 V199 H318 V186 H348 V173 H378 V160 H408 V147 H438 V134 H468 V121 H498 V108 H528 V95 L528,290 Z" fill="url(#carryGain)"/><path d="M566,290 L572,322 L620,316 L696,318 L696,290 Z" fill="url(#carryLoss)"/><line x1="64" y1="290" x2="696" y2="290" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.25"/><line x1="64" y1="48" x2="64" y2="336" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.25"/><path d="M78,290 H108 V277 H138 V264 H168 V251 H198 V238 H228 V225 H258 V212 H288 V199 H318 V186 H348 V173 H378 V160 H408 V147 H438 V134 H468 V121 H498 V108 H528 V95" fill="none" stroke="#1a9e6a" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/><path d="M528,95 L572,322 L620,316 L696,318" fill="none" stroke="#e5484d" stroke-width="2.75" stroke-linejoin="round" stroke-linecap="round"/><circle cx="528" cy="95" r="4.5" fill="#1a9e6a"/><circle cx="528" cy="95" r="4.5" fill="none" stroke="currentColor" stroke-opacity="0.3"/><line x1="612" y1="150" x2="612" y2="238" stroke="#e5484d" stroke-width="2.4" stroke-linecap="round"/><path d="M612,247 L604.5,233 L619.5,233 Z" fill="#e5484d"/><text x="96" y="166" fill="#1a9e6a" font-size="13" font-weight="600">lata drobnych premii</text><text x="612" y="138" text-anchor="middle" fill="#e5484d" font-size="13" font-weight="600">krach w kilka dni</text><text x="56" y="294" text-anchor="end" fill="currentColor" fill-opacity="0.6" font-size="12">0</text><text x="690" y="283" text-anchor="end" fill="currentColor" fill-opacity="0.7" font-size="12.5">czas →</text><text transform="rotate(-90 22 192)" x="22" y="192" text-anchor="middle" fill="currentColor" fill-opacity="0.7" font-size="12.5">skumulowany wynik</text></svg>
<figcaption>Profil skumulowanego wyniku carry trade w czasie. Zielona linia to lata drobnych premii narastających schodami, czerwona to gwałtowny krach, który w kilka dni oddaje zyski zbierane latami.</figcaption>
</figure>

## Premia za ryzyko krachu, nie darmowy obiad

Sprowadza się to do jednego zdania: dodatni zwrot z carry jest zapłatą za gotowość do poniesienia rzadkiej katastrofy. To nie jest błąd rynku do wykorzystania w nieskończoność ani darmowy obiad. To transakcja, w której z góry inkasujesz składkę, a w zamian bierzesz na siebie ryzyko, które przez długi czas się nie materializuje, aż w końcu się materializuje.

Statystyka ma na tę pułapkę nazwę: problem peso. Jeśli rzadkie, ale ogromne zdarzenie nie wypadło jeszcze w próbce, to historyczne zwroty wyglądają lepiej, niż wynosi prawdziwa, oczekiwana wypłata z uwzględnieniem tej katastrofy. Krótka, spokojna historia carry systematycznie zawyża jego atrakcyjność, bo najgorszy scenariusz z definicji zdarza się rzadko i po prostu może jeszcze nie trafić do danych. To odwrotność darmowego obiadu: rachunek istnieje, tylko przychodzi z opóźnieniem i w całości.

To także tłumaczy, dlaczego premia nie znika, mimo że jest znana od dekad. Gdyby była błędem, arbitraż wyzerowałby ją dawno temu. Skoro trwa, to znaczy, że jest zapłatą za realne, niechciane przez większość ryzyko. Ktoś musi trzymać ekspozycję na globalną panikę i dostaje za to premię. Nagroda i ból to dwie strony tej samej monety i nie da się wziąć jednej bez drugiej.

## Nauka o zarządzaniu ryzykiem ogona

Praktyczny wniosek z carry jest właściwie wnioskiem o zarządzaniu ryzykiem ogona i przydaje się daleko poza samym carry. Po pierwsze, pozycjonowanie musi zakładać krach, a nie spokojny dzień. Rozmiar pozycji ustawiony pod typową, cichą zmienność będzie o wiele za duży w dniu, w którym zmienność się potroi. Ryzyko strategii o ujemnym skosie mierzy się nie średnią zmiennością, lecz wielkością możliwego obsunięcia w scenariuszu stresowym.

Po drugie, dźwignia jest tu wrogiem szczególnym. To właśnie ona zamienia bolesny, ale przeżywalny ruch w wezwanie do uzupełnienia depozytu i przymusowe zamknięcie w najgorszym momencie. Krach carry zabija nie samą stratą, lecz tym, że lewarowany gracz zostaje zmuszony do wyjścia po najgorszej cenie, zanim rynek zdąży się uspokoić. Awersja do dźwigni nie jest tu przesadną ostrożnością, tylko bezpośrednim wnioskiem z kształtu rozkładu.

Po trzecie, ostrożność wobec pozornej dywersyfikacji. Skoro w krachu korelacje idą do jedności, to trzymanie wielu pozycji carry naraz daje dużo mniej ochrony, niż sugeruje spokojny okres. Prawdziwa dywersyfikacja to ekspozycja na inny czynnik ryzyka, a nie kilka wariantów tej samej ekspozycji na globalny apetyt na ryzyko. I po czwarte, właściwe narzędzia oceny: zamiast samego Sharpe'a warto patrzeć na skos, na najgłębsze obsunięcia oraz na zachowanie strategii w historycznych epizodach paniki, bo to one, a nie spokojna średnia, decydują o przeżyciu.

## Co z tego wynika przy stole

Carry trade jest jednym z najlepiej udokumentowanych źródeł przewagi na rynku walutowym i zarazem najczystszym przykładem tego, że udokumentowana przewaga nie znaczy darmowy zysk. Mechanizm jest realny: parytet stóp empirycznie zawodzi, więc różnica oprocentowania przynosi dodatni średni zwrot. Ale ten sam mechanizm, który za to płaci, wystawia rachunek w postaci ujemnego skosu i gwałtownego krachu w chwili paniki.

Uczciwa forma myślenia o carry, jak o każdej przewadze, mieści się w trzech rubrykach: skąd bierze się zysk (premia za ryzyko globalnej zmienności), gdzie jest ogon (rzadki, brutalny carry unwind przy skoku zmienności i risk-off) oraz jaki płynie z niego wniosek dla ryzyka (pozycjonowanie i dźwignia liczone pod krach, nie pod spokój). Kto potrafi wypełnić te trzy rubryki, ten rozumie, że carry nie jest maszynką do drukowania pieniędzy, tylko sprzedawaniem ubezpieczenia od paniki. Rośnie schodami, spada windą, a cała sztuka polega na tym, żeby przeżyć jazdę windą.

To nie jest porada inwestycyjna. To szkic mechanizmów, pokazany po to, żeby odróżnić udokumentowane źródło przewagi od darmowego obiadu, i żeby pamiętać, że premia za ryzyko krachu bywa realna dokładnie dlatego, że kiedyś każe za siebie zapłacić.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
