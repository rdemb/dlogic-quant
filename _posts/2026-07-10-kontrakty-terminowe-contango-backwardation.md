---
title: "Kontrakty terminowe. Contango, backwardation, roll yield"
description: "Kontrakt terminowy to zobowiązanie obu stron, nie prawo jak w opcji: kupujący musi kupić, sprzedający sprzedać instrument po ustalonej cenie w ustalonym terminie. Instrument jest wystandaryzowany, zabezpieczony depozytem i codziennie rozliczany do rynku (marking to market), a jego cena wynika z kosztu utrzymania: cena spot skorygowana o finansowanie i magazynowanie, pomniejszone o premię za posiadanie fizyczne. Gdy ten koszt netto jest dodatni, futures są droższe od spot (contango), gdy ujemny, tańsze (backwardation). Rolowanie wygasających kontraktów daje roll yield, ujemny w contango, przez co długie trzymanie ETF-ów surowcowych traci na rolowaniu. Do tego normalna backwardation Keynesa i Hicksa oraz ostrzeżenie: dźwignia futures działa w obie strony i grozi wezwaniem do uzupełnienia depozytu. Podstawy według Hulla, kontekst empiryczny z Gortona i Rouwenhorsta."
date: 2026-07-10 15:00:00 +0200
eyebrow: "Edukacja · instrumenty"
dek: "Future to lustrzane odbicie opcji: nie prawo, lecz zobowiązanie obu stron, bez premii, za to z depozytem i codziennym rozliczeniem, które lewarują pozycję w obie strony. Do tego wycena kosztem utrzymania, dwa kształty krzywej terminowej (contango i backwardation), roll yield przy rolowaniu kontraktów oraz klasyczna hipoteza normalnej backwardation Keynesa i Hicksa. Na koniec ostrzeżenie o dźwigni i wezwaniu do uzupełnienia depozytu."
readingTime: 8
tags: ["kontrakty terminowe", futures, instrumenty, contango, backwardation, "roll yield", "cost of carry", "koszt utrzymania", "depozyt zabezpieczający", "marking to market", dźwignia, "normalna backwardation", Keynes, Hicks, Hull, "Gorton Rouwenhorst", surowce, edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Kontrakt terminowy (future) to zobowiązanie, nie prawo: obie strony muszą wykonać umowę. Kupujący (pozycja długa) ma obowiązek kupić, sprzedający (pozycja krótka) sprzedać instrument bazowy po ustalonej cenie w ustalonym terminie. To odwrotność opcji, gdzie kupujący ma prawo, nie obowiązek, i płaci za nie premię z góry. W futures premii nie ma, a wartość kontraktu na starcie wynosi zero.
> - Futures giełdowe są wystandaryzowane, a bezpieczeństwo rozliczenia zapewniają depozyt zabezpieczający (margin) i codzienne rozliczenie do rynku (marking to market): zyski i straty księgowane są każdego dnia. Ponieważ depozyt to ułamek wartości nominalnej, kontrakt niesie dźwignię działającą w obie strony.
> - Wycena wynika z kosztu utrzymania (cost of carry): cena terminowa to cena spot skorygowana o koszt finansowania i magazynowania, pomniejszony o premię za posiadanie fizyczne. Gdy ten koszt netto jest dodatni, futures są droższe od spot (contango), gdy ujemny, tańsze (backwardation).
> - Przy długim trzymaniu pozycji wygasające kontrakty trzeba rolować. W contango rolowanie oznacza sprzedaż taniej i kupno drożej (ujemny roll yield), dlatego fundusze ETF na surowce trzymające futures potrafią tracić względem ceny spot mimo płaskiego rynku. W backwardation jest odwrotnie.
> - Normalna backwardation Keynesa (1930) i Hicksa (1939) to hipoteza, że zabezpieczający się producenci płacą premię spekulantom za przejęcie ryzyka, więc cena futures bywa poniżej oczekiwanej przyszłej ceny spot. Sednem ryzyka pozostaje dźwignia: grozi wezwaniem do uzupełnienia depozytu i stratą przekraczającą wpłaconą kaucję.

**Teza w jednym zdaniu:** Kontrakt terminowy to wystandaryzowane zobowiązanie obu stron do transakcji w przyszłości, rozliczane codziennie i lewarowane depozytem, a jego cena wynika z kosztu utrzymania, przy czym nachylenie krzywej terminowej (contango albo backwardation) decyduje, czy rolowanie pozycji dodaje czy odejmuje od wyniku.

## Zobowiązanie, nie prawo: czym future różni się od opcji

Poprzedni tekst o opcjach opierał się na jednym słowie: prawo. Kontrakt terminowy stoi na słowie przeciwnym: zobowiązanie. W ujęciu podręcznika referencyjnego rynków pochodnych, „Options, Futures, and Other Derivatives" Johna Hulla, future to umowa zobowiązująca obie strony do kupna i sprzedaży instrumentu bazowego po ustalonej dziś cenie, w ustalonym terminie w przyszłości. Nie ma tu premii płaconej z góry ani strony, która może się wycofać. Kupujący, czyli pozycja długa, ma obowiązek odebrać instrument i zapłacić; sprzedający, pozycja krótka, ma obowiązek dostarczyć.

Różnicę wobec opcji widać w jednym zdaniu: posiadacz opcji może pozwolić jej wygasnąć, posiadacz futures nie może. Za asymetrię prawa opcji kupujący płaci premię z góry; w kontrakcie terminowym symetria zobowiązań sprawia, że na starcie żadna strona nie płaci drugiej, bo cena jest ustawiona tak, że wartość kontraktu wynosi zero.

```
opcja  = prawo (kupujący) kontra obowiązek (wystawca), premia z góry
future = obowiązek po obu stronach, brak premii, wartość na starcie ok. 0

pozycja długa  (long)  = obowiązek KUPNA po cenie F w terminie T
pozycja krótka (short) = obowiązek SPRZEDAŻY po cenie F w terminie T
```

## Standaryzacja i codzienne rozliczenie

Future giełdowy jest wystandaryzowany: giełda z góry ustala wielkość kontraktu, jakość i rodzaj instrumentu bazowego oraz termin i sposób dostawy. Dzięki temu kontrakty są wymienne i płynne, a kupujący nie negocjuje warunków, wybiera tylko cenę i liczbę kontraktów. To odróżnia futures od kontraktów forward, które zawiera się poza giełdą, dopasowując warunki do stron, ale bez gwarancji izby rozliczeniowej.

Bezpieczeństwo transakcji opiera się na dwóch mechanizmach. Pierwszy to depozyt zabezpieczający (margin): aby otworzyć pozycję, wpłaca się ułamek wartości nominalnej kontraktu jako kaucję, która ma pokryć ewentualną stratę, a nie zaliczkę na zakup. Drugi to codzienne rozliczenie do rynku, po angielsku marking to market: na koniec każdej sesji izba rozliczeniowa księguje zysk lub stratę pozycji w gotówce, obciążając rachunki tracących i uznając rachunki zyskujących. Strata nie czeka do terminu, materializuje się każdego dnia.

Jeżeli po serii niekorzystnych rozliczeń stan depozytu spadnie poniżej progu podtrzymania (maintenance margin), broker wysyła wezwanie do uzupełnienia depozytu (margin call). Brak reakcji oznacza przymusowe zamknięcie pozycji.

## Dźwignia działa w obie strony

Ponieważ depozyt to ułamek wartości nominalnej, kontrakt niesie wbudowaną dźwignię. Ekspozycja pracuje na pełnej wartości nominalnej, a angażuje się tylko depozyt, więc procentowy wynik liczony od wpłaconego kapitału jest wielokrotnością ruchu instrumentu. Działa to symetrycznie, tak samo powiększa zysk jak stratę.

```
PRZYKŁAD ILUSTRACYJNY (liczby umowne)
wartość nominalna kontraktu:  100 000
depozyt wstępny (5%):           5 000

ruch instrumentu  +2%  →  +2 000  →  +40% depozytu
ruch instrumentu  −2%  →  −2 000  →  −40% depozytu
ruch instrumentu −10%  →  −10 000 →  strata dwukrotności depozytu
```

Ostatni wiersz pokazuje, dlaczego dźwignia futures bywa niebezpieczna: ruch większy niż depozyt oznacza stratę przekraczającą wpłaconą kaucję, a codzienne rozliczenie wymusi jej pokrycie, zanim kontrakt dojdzie do terminu.

## Wycena: koszt utrzymania (cost of carry)

Skąd bierze się dzisiejsza cena dostawy w przyszłości? Z arbitrażu. Kto chce mieć instrument w terminie T, ma dwie drogi: kupić future albo kupić instrument dziś za pożyczone pieniądze i przetrzymać go. Obie muszą kosztować tyle samo, inaczej powstałby zysk bez ryzyka. Stąd wzór na koszt utrzymania, wyprowadzony u Hulla:

```
F = S · e^{(r + u − y)·T}

F = cena futures (dziś, dostawa w chwili T)
S = cena spot (dziś)
r = stopa wolna od ryzyka (koszt finansowania zakupu)
u = koszt magazynowania (proporcjonalny, dla surowców)
y = premia za posiadanie fizyczne (convenience yield)
T = czas do wygaśnięcia w latach

aktywo finansowe z dochodem q:  F = S · e^{(r − q)·T}
waluta (parytet stóp):          F = S · e^{(r_kraj − r_zagr)·T}
```

Każdy składnik ma sens ekonomiczny. Stopa r to koszt finansowania zakupu; podnosi cenę terminową. Koszt magazynowania u, istotny przy surowcach, też ją podnosi, bo trzymanie fizycznego towaru kosztuje. Convenience yield y to korzyść z posiadania zapasu pod ręką, na przykład możliwość zaspokojenia nagłego popytu; obniża cenę terminową, bo trzymający spot dostaje coś, czego posiadacz kontraktu nie ma. Dla walut rolę u i y przejmują stopy procentowe obu krajów, a wzór staje się parytetem stóp procentowych.

Jedna własność jest pewna niezależnie od parametrów: w miarę zbliżania się terminu cena futures zbiega do ceny spot, aż w dniu wygaśnięcia obie są praktycznie równe.

## Contango i backwardation: kształt krzywej

Znak wyrażenia w wykładniku decyduje o kształcie krzywej terminowej i o dwóch nazwach, które ten kształt opisują.

```
r + u − y > 0  →  F > S  →  CONTANGO       (futures drożej niż spot)
r + u − y < 0  →  F < S  →  BACKWARDATION   (futures taniej niż spot)
```

Contango to sytuacja, w której kontrakty terminowe są droższe od ceny spot, a im dalszy termin, tym drożej; krzywa rośnie. Dominuje tam, gdzie koszt finansowania i magazynowania przeważa, a więc dla wielu surowców w spokojnych warunkach podaży. Backwardation to odwrotność: futures tańsze od spot, krzywa opada. Pojawia się, gdy premia za posiadanie fizyczne jest wysoka, typowo przy napięciu podażowym, gdy rynek płaci za natychmiastowy dostęp do towaru.

Obie nazwy opisują wyłącznie kształt krzywej dziś, a nie prognozę ceny. To ważne rozróżnienie: słowo backwardation wraca w węższym znaczeniu Keynesa.

## Roll yield: dlaczego rolowanie kosztuje albo płaci

Kontrakt terminowy wygasa. Kto chce utrzymać ekspozycję dłużej niż jeden termin, musi rolować pozycję: zamknąć wygasający kontrakt i otworzyć kolejny, dalszy. Sam akt rolowania ma cenę, która zależy od kształtu krzywej i nosi nazwę roll yield.

```
CONTANGO: krzywa rosnąca (przykład ilustracyjny, spot = 100 niezmienny)
kontrakt bliski (wygasa):   100
kontrakt daleki (następny): 104
rolowanie: sprzedaj bliski po 100, kup daleki po 104
przy stałym spot daleki dąży 104 → 100, roll yield UJEMNY (ok. −4)

BACKWARDATION: krzywa opadająca (spot = 100 niezmienny)
kontrakt bliski (wygasa):   100
kontrakt daleki (następny):  96
rolowanie: sprzedaj bliski po 100, kup daleki po 96
przy stałym spot daleki dąży 96 → 100, roll yield DODATNI (ok. +4)
```

W contango rolowanie oznacza z zasady sprzedaż taniej i kupno drożej, więc każde przejście na kolejny kontrakt odejmuje od wyniku, nawet jeśli cena spot ani drgnie. To wyjaśnia zjawisko mylące inwestorów detalicznych: fundusze ETF na surowce, które nie trzymają fizycznego towaru, tylko rolują kontrakty futures, potrafią systematycznie tracić względem ceny spot surowca, gdy rynek długo tkwi w contango. Notowana cena surowca może przez rok wrócić w to samo miejsce, a taki ETF i tak zanotować stratę zjedzoną przez kolejne ujemne roll yield. W backwardation mechanizm działa na korzyść posiadacza kontraktu, bo rolowanie kupuje taniej, niż sprzedaje.

## Normalna backwardation: hipoteza Keynesa i Hicksa

Słowo backwardation ma drugie, węższe znaczenie, starsze od dzisiejszego żargonu rynkowego. John Maynard Keynes w „A Treatise on Money" (1930) postawił hipotezę nazwaną normalną backwardation. Dotyczy ona nie relacji między futures a dzisiejszym spot, lecz między futures a oczekiwaną przyszłą ceną spot.

Rozumowanie opiera się na tym, kto naturalnie potrzebuje zabezpieczenia. Producent surowca, rolnik, kopalnia czy wytwórca, jest z natury długi w fizycznym towarze i chce zamknąć cenę sprzedaży z wyprzedzeniem, więc sprzedaje futures. Zabezpieczający się są zatem po stronie krótkiej i jest ich w nadmiarze. Żeby ktoś przejął drugą, długą stronę i wziął na siebie ryzyko ceny, musi mieć w tym oczekiwany zysk. Tym kimś jest spekulant, a jego wynagrodzeniem jest cena futures ustawiona poniżej oczekiwanej przyszłej ceny spot: w miarę zbliżania się terminu cena kontraktu ma tendencję do wzrostu ku spotowi, co daje długiemu spekulantowi dodatni oczekiwany zwrot. John Hicks w „Value and Capital" (1939) rozwinął ten argument, wiążąc go z przewagą liczebną zabezpieczających nad spekulantami.

```
UWAGA na dwa znaczenia tego samego słowa:
backwardation (rynkowa)  = F < S       (dziś, kształt krzywej)
normalna backwardation   = F < E[S_T]  (Keynes: futures < oczekiwany spot)
                                         premia za ryzyko dla spekulanta
```

W skrócie: zabezpieczający płacą spekulantom za przejęcie ryzyka, a ta zapłata ma postać ceny terminowej z wbudowaną premią. Hipoteza jest wpływowa i sporna; opisuje mechanizm, a nie gwarancję, bo w praktyce strona zabezpieczająca bywa też długa, na przykład linie lotnicze zabezpieczające koszt paliwa, co może odwracać znak premii.

## Gdzie to działa: surowce, indeksy, waluty

Kontrakty terminowe obejmują trzy główne klasy instrumentu bazowego. Surowce: ropa, gaz, metale, produkty rolne, gdzie futures narodziły się jako narzędzie producentów i odbiorców do zamykania cen. Indeksy giełdowe: kontrakty na S&P 500 czy DAX służą do zabezpieczania portfela akcji i do szybkiej ekspozycji na cały rynek bez kupowania setek spółek. Waluty: futures i forwardy walutowe, wyceniane parytetem stóp procentowych, zabezpieczają ryzyko kursowe lub dają pozycję na różnicy stóp.

Co historia mówi o surowcach jako klasie? Gary Gorton i Geert Rouwenhorst w pracy „Facts and Fantasies about Commodity Futures" (2006) zbadali równoważony koszyk kontraktów surowcowych za okres 1959-2004. Ich obserwacje: zwroty z w pełni zabezpieczonego koszyka były porównywalne z akcjami pod względem relacji zysku do ryzyka, ujemnie skorelowane z akcjami i obligacjami oraz dodatnio z inflacją. To argument za surowcami jako dywersyfikatorem, a nie za samodzielną przewagą: badanie opisuje przeszłość jednego okresu i jednej metody konstrukcji koszyka, nie obietnicę na przyszłość.

## Ryzyko: dźwignia i wezwanie do uzupełnienia depozytu

Cała konstrukcja opiera się na dźwigni, a dźwignia jest symetryczna: powiększa zysk i stratę w tej samej proporcji. W przeciwieństwie do kupionej opcji, gdzie strata jest z góry ścięta do premii, pozycja w futures nie ma wbudowanego dna. Codzienne rozliczenie ściąga stratę z depozytu każdego dnia, a jej narastanie prowadzi do wezwania do uzupełnienia depozytu i, przy braku reakcji, do przymusowego zamknięcia pozycji w najgorszym momencie. Strata może przekroczyć wpłaconą kaucję. To nie scenariusz skrajny, tylko wpisana w instrument mechanika, którą trzeba rozumieć przed zajęciem pozycji, a nie po.

Materiał czysto edukacyjny, nie porada inwestycyjna ani zachęta do zajmowania pozycji. Porządkuje mechanikę kontraktów terminowych według podręcznika Hulla (wycena, koszt utrzymania) oraz klasycznych hipotez Keynesa (1930) i Hicksa (1939) o normalnej backwardation, z kontekstem empirycznym z pracy Gortona i Rouwenhorsta (2006). Wszystkie przykłady liczbowe są ilustracyjne i umowne, a jedyne, co pewne, to arytmetyka i tożsamości wyceny, nie kierunek jakiejkolwiek ceny.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
