---
title: "Black-Scholes i greckie. Jak wycenia się niepewność"
description: "Model Blacka, Scholesa i Mertona z 1973 roku wycenia opcję jako koszt jej replikacji: dealer może dynamicznie równoważyć opcję akcjami i gotówką, więc cena wynika z braku arbitrażu, a nie z przewidywania kierunku. Dlatego we wzorze nie ma oczekiwanego zwrotu, jest za to zmienność. Do tego greckie jako język ryzyka opcji (delta, gamma, vega, theta), delta hedging w praktyce oraz zmienność implikowana jako cena ubezpieczenia, a nie prognoza. Koncepcje po ludzku, ze wzorem i tabelą intuicji."
date: 2026-07-05 14:00:00 +0200
eyebrow: "Edukacja · instrumenty"
dek: "Cenę opcji wyznacza koszt jej odtworzenia, a nie czyjaś prognoza kierunku. Dlatego we wzorze Blacka i Scholesa nie ma oczekiwanego zwrotu akcji, jest za to zmienność. Greckie (delta, gamma, vega, theta) to język, w którym rynek opcji opisuje swoje ryzyko, a zmienność implikowana to cena ubezpieczenia, nie przepowiednia."
readingTime: 9
tags: ["Black-Scholes", BSM, opcje, "wycena opcji", greckie, delta, gamma, vega, theta, "delta hedging", "zmienność implikowana", replikacja, "brak arbitrażu", smile, Black, Scholes, Merton, Hull, Natenberg, "Nobel 1997", edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Przełom Blacka, Scholesa i Mertona z 1973 roku nie polegał na lepszym prognozowaniu rynku, lecz na zmianie pytania. Zamiast zgadywać, ile opcja będzie warta, policzyli, ile kosztuje jej odtworzenie: dealer może dynamicznie równoważyć opcję akcjami i gotówką, więc cena wynika z braku arbitrażu, a nie z czyjejś prognozy kierunku.
> - Najbardziej zaskakująca konsekwencja: we wzorze nie ma oczekiwanego zwrotu akcji. Zabezpieczony dealer nie zarabia i nie traci na kierunku, więc kierunek nie może wpływać na cenę. Zostaje zmienność, jedyna wielkość we wzorze, której nie widać na ekranie.
> - Greckie to język ryzyka opcji. Delta mierzy wrażliwość na ruch ceny i z grubsza przybliża szansę wygaśnięcia w pieniądzu, gamma tempo zmiany delty, vega wrażliwość na zmienność, theta upływ czasu. Posiadacz opcji płaci thetę za dodatnią gammę, wystawca inkasuje thetę i nosi ryzyko gwałtownego ruchu.
> - Zmienność implikowana to cena, nie prognoza: wynika z rynkowej ceny opcji odwróconej przez wzór, a uśmiech zmienności mówi, za które scenariusze rynek płaci więcej. Za ten aparat Scholes i Merton odebrali w 1997 roku Nagrodę Nobla; Black nie dożył.

**Teza w jednym zdaniu:** Model Blacka-Scholesa wycenia opcję jako koszt jej dynamicznej replikacji akcjami i gotówką, przez co ze wzoru znika oczekiwany zwrot, a zostaje zmienność, greckie zaś (delta, gamma, vega, theta) opisują, jak ta wycena reaguje na cenę, zmienność i czas, i dlatego rynek opcji jest w istocie rynkiem zmienności, a nie kierunku.

## Problem, który przez dekady wydawał się nierozwiązywalny

Opcja kupna (call) daje prawo, ale nie obowiązek, kupienia instrumentu po ustalonym kursie wykonania w ustalonym terminie; opcja sprzedaży (put) analogicznie daje prawo sprzedaży. Wypłata zależy od tego, gdzie wyląduje cena, więc naturalny odruch podpowiada, że do wyceny takiej warunkowej obietnicy trzeba najpierw przewidzieć, dokąd pójdzie rynek. Tu tkwił kłopot: każdy uczestnik ma inną prognozę i inny apetyt na ryzyko, więc każdy dostawałby inną „słuszną" cenę. Wcześniejsze próby wyceny utykały dokładnie na tym, bo we wzorach zawsze zostawał oczekiwany zwrot akcji albo parametr czyjejś awersji do ryzyka, wielkości nieobserwowalne i z natury sporne.

## Kluczowa idea: cena opcji to koszt jej replikacji

Black i Scholes w pracy „The Pricing of Options and Corporate Liabilities" (Journal of Political Economy, 1973) oraz Merton w „Theory of Rational Option Pricing" (Bell Journal, 1973) odwrócili pytanie. Zamiast „ile ta opcja będzie warta" zapytali: ile kosztuje portfel, który zachowuje się dokładnie jak ta opcja. Okazuje się, że odpowiednio dobrany i stale dostosowywany koszyk akcji i gotówki naśladuje wypłatę opcji. Skoro tak, cena opcji musi być równa kosztowi prowadzenia tej strategii. Gdyby była wyższa, można by opcję sprzedać, taniej ją zreplikować i zgarnąć różnicę bez ryzyka; gdyby była niższa, wystarczy operacja odwrotna. Cena wynika z braku arbitrażu, a nie z przewidywania przyszłości. Merton pokazał przy tym, że do wyniku wystarczy sama możliwość ciągłej replikacji i brak okazji arbitrażowych, i rozszerzył model na ogólniejsze warunki.

Z tej konstrukcji płynie najgłębszy i najbardziej antyintuicyjny wniosek. Dealer, który na bieżąco równoważy pozycję, nie ma ekspozycji na kierunek rynku, więc jego koszt replikacji nie zależy od tego, czy akcja „powinna" rosnąć czy spadać. A skoro cena opcji równa się temu kosztowi, prognoza kierunku nie ma prawa się w niej pojawić. Optymista i pesymista, jeśli tylko zgadzają się co do skali przyszłych wahań, muszą podać tę samą cenę opcji. Dlatego we wzorze nie występuje oczekiwany zwrot akcji, występuje za to zmienność. Wycena niepewności bez prognozowania kierunku: to była rewolucja roku 1973, tego samego, w którym ruszyła pierwsza giełda opcji CBOE.

## Wzór, czyli mniej strasznie, niż wygląda

```
C = S·N(d1) − K·e^(−r·T)·N(d2)        # europejski call (bez dywidend)
P = K·e^(−r·T)·N(−d2) − S·N(−d1)      # europejski put

d1 = [ln(S/K) + (r + σ²/2)·T] / (σ·√T)
d2 = d1 − σ·√T

S = bieżąca cena instrumentu          K = kurs wykonania (strike)
T = czas do wygaśnięcia (w latach)    r = stopa wolna od ryzyka
σ = zmienność, jedyna wielkość niewidoczna na ekranie
N(·) = dystrybuanta rozkładu normalnego, liczba od 0 do 1
```

Czyta się to prościej, niż wygląda. Cena call to „wartość tego, co dostanę" minus „wartość tego, co zapłacę", a oba składniki są zdyskontowane i zważone szansami wykonania. N(d2) pełni rolę prawdopodobieństwa, że opcja wygaśnie w pieniądzu, więc K·e^(−r·T)·N(d2) to dzisiejsza wartość kursu wykonania płaconego tylko wtedy, gdy do wykonania dojdzie. S·N(d1) to odpowiadająca temu dzisiejsza wartość odbieranych akcji. Jedno zastrzeżenie jest kluczowe: te prawdopodobieństwa są policzone w tak zwanym świecie wolnym od ryzyka, sztucznej konstrukcji wynikającej z wyceny przez replikację, w której wszystko dryfuje w tempie stopy procentowej. Nie są prognozą rzeczywistych szans, są jednostkami rozliczeniowymi wyceny. Hull w klasycznym podręczniku o instrumentach pochodnych prowadzi przez tę konstrukcję krok po kroku; na rynku walutowym ta sama logika działa w wersji z dwiema stopami procentowymi, krajową i zagraniczną (model Garmana-Kohlhagena).

Warto zatrzymać wzrok na liście składników. Cena instrumentu, kurs wykonania, czas, stopa procentowa: wszystko to widać na ekranie. Jedyną wielkością, którą trzeba skądś wziąć, jest zmienność. Cały spór o wartość opcji sprowadza się więc do jednej liczby: jak bardzo rynek będzie się ruszał do wygaśnięcia.

<figure>
<svg viewBox="0 0 640 380" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Wartość opcji call przed wygaśnięciem jako gładka krzywa leżąca nad łamaną wypłatą w terminie równą max(S minus K, 0); pionowy odstęp między nimi to wartość czasowa."><defs><marker id="bsax" markerWidth="10" markerHeight="10" refX="7.5" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="currentColor" fill-opacity="0.5"/></marker><marker id="bstv" markerWidth="9" markerHeight="9" refX="6" refY="3.5" orient="auto-start-reverse"><path d="M0,0 L7,3.5 L0,7 Z" fill="currentColor" fill-opacity="0.85"/></marker></defs><line x1="56" y1="256" x2="610" y2="256" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><line x1="56" y1="186" x2="610" y2="186" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><line x1="56" y1="116" x2="610" y2="116" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><line x1="250" y1="326" x2="250" y2="52" stroke="currentColor" stroke-opacity="0.4" stroke-dasharray="5 5"/><line x1="56" y1="326" x2="626" y2="326" stroke="currentColor" stroke-opacity="0.5" marker-end="url(#bsax)"/><line x1="56" y1="326" x2="56" y2="42" stroke="currentColor" stroke-opacity="0.5" marker-end="url(#bsax)"/><path d="M56,326 L250,326 L610,76" fill="none" stroke="currentColor" stroke-opacity="0.85" stroke-width="2" stroke-linejoin="round"/><path d="M56,320 C92,318 128,312 160,304 C190,296 224,282 250,266 C282,250 318,236 350,222 C392,206 432,182 470,156 C520,138 566,104 610,70" fill="none" stroke="#0b66c3" stroke-width="2.4" stroke-linecap="round"/><line x1="300" y1="291" x2="300" y2="243" stroke="currentColor" stroke-opacity="0.85" stroke-width="1.4" marker-start="url(#bstv)" marker-end="url(#bstv)"/><line x1="300" y1="291" x2="325" y2="306" stroke="currentColor" stroke-opacity="0.5" stroke-width="1"/><text x="330" y="310" font-size="12" fill="currentColor" fill-opacity="0.85">wartość czasowa</text><text x="250" y="342" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.65">K (kurs wykonania)</text><text x="336" y="360" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.65">cena instrumentu bazowego (S)</text><text transform="translate(18,192) rotate(-90)" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.65">wartość opcji</text><text x="10" y="20" font-size="13" fill="currentColor">Wartość opcji call: wartość bieżąca kontra wypłata w terminie</text><line x1="14" y1="34" x2="40" y2="34" stroke="#0b66c3" stroke-width="2.4" stroke-linecap="round"/><text x="46" y="38" font-size="10.5" fill="currentColor" fill-opacity="0.85">wartość przed wygaśnięciem</text><line x1="212" y1="34" x2="238" y2="34" stroke="currentColor" stroke-opacity="0.85" stroke-width="2" stroke-linecap="round"/><text x="244" y="38" font-size="10.5" fill="currentColor" fill-opacity="0.85">wypłata w terminie: max(S − K, 0)</text></svg>
<figcaption>Gładka niebieska krzywa to wartość opcji call przed wygaśnięciem, a łamana poniżej to jej wypłata w dniu wygaśnięcia. Pionowy odstęp między liniami to wartość czasowa, która topnieje do zera, gdy zbliża się termin.</figcaption>
</figure>

## Założenia i to, jak rzeczywistość je łamie

Model kupuje swoją elegancję za cenę mocnych założeń: zmienność jest stała przez całe życie opcji, cena porusza się ciągłymi, drobnymi krokami bez skoków (rozkład logarytmiczno-normalny), handel jest ciągły, bez kosztów transakcyjnych i ograniczeń, a stopa procentowa się nie zmienia. Rzeczywistość łamie każde z nich. Zmienność sama się zmienia i przychodzi seriami. Rynki skaczą: luka weekendowa, decyzja banku centralnego czy zaskakujący odczyt danych potrafią przenieść cenę bez żadnego handlu po drodze. Hedging odbywa się skokowo i kosztuje spread.

Rynek doskonale o tym wie i wycenia poprawkę. W świecie modelu wszystkie opcje na ten sam instrument i termin powinny mieć jedną wspólną zmienność; w praktyce opcje o różnych kursach wykonania mają różne zmienności implikowane, a ich wykres układa się w uśmiech albo skos. To zapis tego, że rynek płaci więcej za ochronę przed scenariuszami skrajnymi, niż wynikałoby z rozkładu normalnego. Mechanika uśmiechu, risk reversal i premia za ryzyko zmienności mają na tym blogu [osobny artykuł o zmienności](/dlogic-quant/2026/07/09/zmiennosc-prognoza-premia-ryzyka/). Natenberg, autor praktycznego kanonu o zmienności i wycenie opcji, ujmuje to trzeźwo: model jest mapą, nie terytorium, a zawodowi traderzy używają go jako wspólnego języka kwotowań, znając jego słabości na pamięć.

## Greckie: język, w którym opcje opisują swoje ryzyko

Wzór podaje jedną cenę, ale praktyk potrzebuje wiedzieć, jak ta cena zareaguje, gdy świat drgnie. Temu służą greckie, czyli wrażliwości ceny opcji na poszczególne parametry. Cztery z nich tworzą podstawowy słownik.

Delta mówi, o ile zmieni się cena opcji przy małym ruchu instrumentu bazowego. Dla call mieści się między zerem a jedynką, dla put między minus jedynką a zerem, przy pieniądzu wynosi około 0.5. Delta jest jednocześnie przelicznikiem na pozycję: opcja o delcie 0.4 zachowuje się chwilowo jak 40 procent pozycji w instrumencie i dokładnie tyle trzeba mieć po przeciwnej stronie, żeby ryzyko kierunku znieść do zera. Praktycy używają delty także jako szybkiego przybliżenia szansy, że opcja wygaśnie w pieniądzu; formalnie tę rolę pełni N(d2), a delta ją nieco zawyża, ale heurystyka „opcja 25-delta ma z grubsza jedną czwartą szans skończyć w pieniądzu" jest na deskach codziennym skrótem myślowym.

Gamma mówi, jak szybko delta się zmienia, gdy rynek się rusza. To miara wypukłości i zarazem ryzyka dużego ruchu. Kupujący opcję ma gammę dodatnią: gdy rynek idzie w jego stronę, delta rośnie i pozycja sama się rozpędza, a gdy zawraca, delta maleje i pozycja sama hamuje. Wystawca ma gammę ujemną i dokładnie odwrotny problem: duży ruch w którąkolwiek stronę obraca się przeciw niemu coraz szybciej. Gamma jest największa przy pieniądzu i narasta, gdy zbliża się wygaśnięcie, dlatego ostatnie dni życia opcji ATM to najbardziej nerwowy okres dla wystawcy.

Vega mówi, o ile zmieni się cena opcji, gdy zmienność implikowana wzrośnie o punkt procentowy. Kupiona opcja to pozycja długa w zmienności: drożeje, gdy rynek zaczyna płacić więcej za niepewność, nawet jeśli kurs stoi w miejscu. Vega jest największa przy pieniądzu i przy dłuższych terminach.

Theta mówi, ile wartości opcji wyparowuje z każdym dniem przy pozostałych parametrach bez zmian. Posiadacz opcji płaci thetę, wystawca ją inkasuje. To nie jest wada konstrukcyjna, tylko druga strona gammy: kto ma prawo do wypukłości, płaci za nie czynsz; kto wypukłość sprzedał, pobiera czynsz i nosi ryzyko.

```
# cztery podstawowe greckie: kto co ma i kto komu płaci

grecka   co mierzy                      posiadacz opcji              wystawca opcji
delta    reakcję na ruch ceny           ekspozycja na kierunek       ekspozycja odwrotna
gamma    tempo zmiany delty             dodatnia: duży ruch pomaga   ujemna: duży ruch boli
vega     reakcję na zmienność (IV)      zyskuje, gdy IV rośnie       traci, gdy IV rośnie
theta    upływ czasu                    płaci dzień po dniu          inkasuje dzień po dniu
```

## Delta hedging w praktyce: dlaczego rynek opcji gra o zmienność

Dealer, który sprzedał klientowi opcję, zwykle nie chce grać z nim o kierunek. Pierwszym ruchem neutralizuje więc deltę: kupuje tyle instrumentu bazowego, ile wynosi delta pozycji. Od tej chwili drobne ruchy rynku przestają go obchodzić. Zostaje z gammą, vegą i thetą, i tu zaczyna się właściwa gra. Jego gamma jest ujemna, więc gdy rynek rośnie, delta wystawionej opcji rośnie i dealer musi dokupować coraz drożej, a gdy rynek spada, musi sprzedawać coraz taniej. Systematycznie kupuje wysoko i sprzedaje nisko, a straty z tego dostrajania pokrywa inkasowana dzień po dniu theta. Posiadacz opcji jest w lustrzanej pozycji: jego hedging mechanicznie sprzedaje po wzrostach i odkupuje po spadkach, ale za ten komfort codziennie płaci thetę.

Bilans obu stron rozstrzyga jedna rzecz: czy zmienność, która faktycznie się zrealizuje, okaże się większa, czy mniejsza od tej zapłaconej w cenie opcji. Pozycja opcyjna z wyzerowaną deltą jest zakładem o zmienność, nie o kierunek. Dlatego zawodowy rynek opcji kwotuje w punktach zmienności i myśli w kategoriach kupowania oraz sprzedawania zmienności, a nie wzrostów i spadków. Natenberg poświęca tej mechanice dużą część książki: opcje to rynek ubezpieczeń od ruchu, na którym kierunek jest neutralizowany pierwszą transakcją.

## Zmienność implikowana: cena, nie prognoza

Skoro zmienność jest jedyną niewiadomą we wzorze, można spojrzeć od drugiej strony: wziąć rynkową cenę opcji i zapytać, jaka zmienność musiałaby obowiązywać, żeby wzór tę cenę odtworzył. Wynik to zmienność implikowana. I tu łatwo o nieporozumienie: IV nie jest niezależną prognozą przyszłych wahań, jest przeliczeniem ceny opcji na wygodniejsze jednostki. Gdy przed posiedzeniem banku centralnego IV rośnie, nie znaczy to, że „model przewiduje duży ruch"; znaczy to, że ubezpieczenie od ruchu podrożało, bo wzrósł popyt na ochronę. IV jest ceną niepewności, dokładnie tak jak składka polisy jest ceną, a nie przepowiednią pożaru.

Uśmiech dopowiada resztę. Skoro każda opcja ma własną IV, kształt całej krzywej mówi, za które scenariusze rynek płaci więcej: uniesione skrzydła to droższa ochrona przed ogonami, przechył na jedną stronę to asymetria obaw. Czytana w ten sposób powierzchnia zmienności jest jedną z uczciwszych ankiet rynkowych, bo respondenci odpowiadają w niej pieniędzmi, a nie deklaracjami.

## Nobel 1997 i przestroga w tle

W 1997 roku Scholes i Merton otrzymali Nagrodę Nobla w dziedzinie ekonomii za nową metodę wyznaczania wartości instrumentów pochodnych. Black zmarł dwa lata wcześniej, a nagrody nie przyznaje się pośmiertnie, więc swojej części uznania nie dożył; Akademia wprost podkreśliła jego rolę w uzasadnieniu. Historia dopisała gorzki epilog: rok później fundusz LTCM, wśród którego partnerów byli obaj nobliści, poniósł spektakularne straty i wymagał zorganizowanego ratunku. To dobra puenta całego tematu: wzór zmienił finanse, ale jego założenia łamią się najmocniej dokładnie wtedy, gdy najbardziej potrzeba, żeby działały.

## Po co to inwestorowi, który opcji nie tyka

Z tego aparatu płyną trzy przenośne lekcje, użyteczne także poza rynkiem opcji. Po pierwsze, rozdzielenie kierunku od skali: Black-Scholes pokazuje, że można rzetelnie wycenić niepewność, nie mając żadnego zdania o kierunku, bo to są dwie osobne osie analizy. Po drugie, IV jako barometr: rynkowa cena ubezpieczenia mówi, ile niepokoju jest w cenie przed wydarzeniem, co stanowi kontekst ryzyka również dla tradera działającego na rynku kasowym. Po trzecie, rachunek thety i gammy uczy, że każda ochrona ma swój czynsz, a każdy pozornie darmowy dochód z wystawiania ma ogon ryzyka po drugiej stronie. Wszystko to jest kontekst, nie sygnał: wiedza o tym, jak rynek wycenia niepewność, nie mówi, w którą stronę pójdzie kurs.

To nie jest porada inwestycyjna. To materiał edukacyjny, który tłumaczy logikę wyceny opcji przez replikację i język greckich na podstawie prac Blacka, Scholesa i Mertona oraz podręczników Hulla i Natenberga, żeby czytać rynek opcji jako rynek zmienności i kontekst ryzyka, a nie maszynę do przewidywania kierunku.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
