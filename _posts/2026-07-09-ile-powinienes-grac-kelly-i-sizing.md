---
title: "Ile naprawdę powinieneś grać. Kelly, ogon i wielkość pozycji"
description: "Kryterium Kelly'ego liczy optymalną frakcję kapitału na pozycję, ale pełny Kelly prowadzi do głębokich obsunięć. Ile teoria każe stawiać, dlaczego racjonalnie gra się ułamkiem, jak działa Kelly z limitem ryzyka obsunięcia i czemu lewy ogon rozkładu jest ważniejszy niż średni zysk."
date: 2026-07-09 14:00:00 +0200
eyebrow: "Edukacja · zarządzanie ryzykiem"
category: edukacja
dek: "Edge nie jest licencją na większy lot. Kompendium: ile mówi kryterium Kelly'ego, ile pozwala ograniczenie ryzyka obsunięcia i dlaczego prawdziwa dźwignia siedzi w ucinaniu ogona rozkładu, a nie w wielkości pozycji."
readingTime: 7
tags: ["Kelly", "sizing", "zarządzanie ryzykiem", "drawdown", "dźwignia", "money management", "quant"]
---

> **W skrócie**
>
> - **Kelly maksymalizuje długoterminowy log-wzrost**, wzór to f* = μ/σ². Pełny Kelly ma jednak około 50% szans, że po drodze obsunie kapitał o połowę. Dlatego racjonalnie gra się ułamkiem: połową frakcji albo mniej.
> - **Risk-constrained Kelly (Busseti, Boyd)** dokłada twardy warunek: bierzemy największą frakcję, przy której P(obsunięcie > próg) ≤ α. Im grubszy lewy ogon rozkładu, tym mocniej ten warunek ścina bezpieczną frakcję poniżej surowego Kelly'ego.
> - **Kelly zakłada, że znasz rozkład.** W praktyce estymujesz μ i σ² z próbki, więc prawdziwy Kelly jest niższy niż policzony. Niepewność edge'u to niezależny, dodatkowy powód, żeby grać ułamkiem, a nie z ostrożności.
> - **Prawdziwa dźwignia to nie większy lot, tylko krótszy ogon.** Twardy stop loss ucinający rzadką brzydką stratę podnosi jakość edge'u i dopiero on legalnie odblokowuje większą frakcję. Martingale, czyli dokładanie po stracie, to anty-Kelly.

**Teza w jednym zdaniu:** edge nie jest licencją na większy lot, bo o dopuszczalnej wielkości pozycji decyduje lewy ogon rozkładu, a nie sam średni zysk, więc racjonalny gracz zawsze schodzi do ułamka Kelly'ego.

## Kelly: co ten wzór właściwie maksymalizuje

Kryterium sformułował John Kelly w 1956 roku, a dla rynków i gier spopularyzował je Edward Thorp. Wzór nie liczy zysku na jednej transakcji, tylko frakcję kapitału, która maksymalizuje tempo wzrostu w długim biegu, gdy zyski reinwestujesz.

```
f* = μ / σ²                              (przybliżenie Gaussowskie)
f* : maksymalizuje  E[ log(1 + f · r) ]  (pełny rozkład, po wszystkich f)

μ   = średni zwrot na trade
σ²  = wariancja zwrotów
r   = zwrot pojedynczej pozycji (zmienna losowa)
f   = frakcja kapitału wystawiona na jeden trade
```

Konkret na klasycznym przykładzie Thorpa. Weź monetę z przewagą, wypłata jeden do jednego: wygrywasz z prawdopodobieństwem 0,60, przegrywasz z 0,40. Ile stawiać?

```
p = 0,60   (szansa wygranej),   q = 0,40   (szansa przegranej),   kurs 1:1
f* = p − q = 0,60 − 0,40 = 0,20        → pełny Kelly stawia 20% kapitału
pół Kelly                              → 10% kapitału
```

Kluczowe jest to, co siedzi pod logarytmem. Kelly maksymalizuje wartość oczekiwaną z log(kapitału), czyli średnie tempo geometryczne, a nie średni zysk arytmetyczny. Logarytm karze straty niesymetrycznie. Gdy wystawiona frakcja razy zwrot dąży do minus jeden, czyli tracisz cały postawiony kapitał, log leci do minus nieskończoności.

```
gdy  f · r → −1   (tracisz cały wystawiony kapitał),   log(1 + f · r) → −∞
```

To jeden akapit, ale zawiera całą intuicję sizingu. Pojedynczy gruby lewy ogon, jedna wyjątkowo brzydka strata, ściąga optymalne f w dół dużo mocniej, niż taki sam co do wielkości zysk je podnosi. Dlatego w przybliżeniu Gaussowskim f* to po prostu stosunek średniej do wariancji: im grubszy rozkład, tym mniejsza frakcja. Ten wzór nie nagradza za odwagę, on wycenia zmienność.

## Dlaczego pełny Kelly to za dużo

Pełny Kelly optymalizuje wzrost, ale nie mówi ani słowa o komforcie drogi. A ta droga jest brutalna: pełny Kelly ma około 50% szans, że w którymś momencie ścieżka kapitału obsunie się o połowę od swojego szczytu. To nie jest odległy ogon, to rzut monetą o głęboki zjazd.

Ten wynik da się zapisać wzorem. W idealizacji ciągłej, gdy grasz ułamkiem λ pełnego Kelly'ego, prawdopodobieństwo, że kapitał kiedykolwiek spadnie do frakcji α swojej wartości, wynosi:

```
P(kapitał kiedykolwiek spadnie do frakcji α)  =  α^(2/λ − 1)      (idealizacja ciągła)

λ = ułamek pełnego Kelly'ego, którym grasz  (λ = 1 to pełny Kelly)
α = docelowy poziom obsunięcia  (α = 0,5 oznacza utratę połowy kapitału)

pełny Kelly  (λ = 1):     P(spadek do połowy) = 0,5^1 = 50%
pół Kelly    (λ = 0,5):   P(spadek do połowy) = 0,5^3 = 12,5%
ćwierć Kelly (λ = 0,25):  P(spadek do połowy) = 0,5^7 ≈ 0,8%
```

Zwróć uwagę, jak ostro spada ryzyko przy schodzeniu z frakcji. Zejście z pełnego do połowy Kelly'ego tnie szansę głębokiego obsunięcia z 50% do około 12%, a do ćwierci Kelly'ego już poniżej jednego procenta. Człowiek, który gra pełnym Kelly, statystycznie prędzej złamie się psychicznie i zejdzie z pozycji na dnie, niż doczeka obiecanego tempa wzrostu.

Kontrargument narzuca się sam: skoro pełny Kelly ma najwyższe tempo wzrostu, to czy ułamek nie zostawia pieniędzy na stole? Zostawia, ale niewiele, a kupuje bardzo dużo spokoju. Krzywa tempa wzrostu wokół optimum jest płaska, więc zejście do połowy frakcji kosztuje niewielki ułamek wzrostu, a wyraźnie ścina ryzyko głębokiego obsunięcia. To jedna z najlepszych wymian w całym zarządzaniu ryzykiem, dlatego żelazna praktyka mówi: gra się połową Kelly'ego albo mniej.

## Kelly z limitem obsunięcia: Busseti i Boyd

Sam Kelly nie zna słowa „obsunięcie". Lukę tę domykają Busseti i Boyd w pracy o risk-constrained Kelly (2016). Pomysł jest prosty i praktyczny: nie maksymalizuj samego wzrostu, tylko znajdź największą frakcję, która nie przekracza zadanego ryzyka głębokiego zjazdu.

```
maksymalizuj   E[ log(1 + f · r) ]
przy warunku   P( obsunięcie > próg )  ≤  α

przykład:  próg = 30% kapitału,   α = 10%
```

Zamiast pytać „ile da się wycisnąć", pytasz „ile wolno, żeby prawdopodobieństwo obsunięcia ponad 30% nie przekroczyło 10%". Odpowiedzią jest bezpieczna frakcja f, zwykle dużo mniejsza od surowego Kelly'ego, a im grubszy lewy ogon, tym większa ta przepaść.

Warto zobaczyć to na kierunku, bo tu jest cała lekcja. Tę samą strategię można policzyć na trzy sposoby, coraz uczciwsze wobec ogona:

```
Kelly Gaussowski     największa frakcja   (udaje rozkład symetryczny)
Kelly empiryczny     mniejsza frakcja     (skośny, realny rozkład już go ścina)
Kelly z limitem DD   najmniejsza frakcja  (dokłada twardy warunek na obsunięcie)
```

Gaussowski wzór udaje, że rozkład jest ładny i symetryczny, więc mówi najwięcej. Ten sam wzór policzony na prawdziwym, skośnym rozkładzie spada, bo ogon już go trochę ściął. A gdy dołożysz twardy warunek na obsunięcie, bezpieczna frakcja leci najniżej ze wszystkich. Trzy odpowiedzi na to samo pytanie, a jedyne, co się zmienia, to ile uczciwości wobec lewego ogona wpuszczasz do rachunku. Dobrze policzona bezpieczna frakcja potrafi wyjść poniżej tego, czym gracz już intuicyjnie gra.

## Niepewny edge: dlaczego ułamek jest obowiązkowy

Jest jeszcze jeden haczyk, o którym Kelly milczy, a który dla realnego gracza jest najważniejszy. Wzór zakłada, że ZNASZ rozkład. Że μ i σ² są dane, prawdziwe, pewne. W praktyce nikt ich nie zna, tylko estymuje z garści historii, a estymacja bywa optymistyczna.

Przydatną miarą jest tu PSR (Probabilistic Sharpe Ratio): prawdopodobieństwo, że prawdziwy Sharpe jest dodatni, przy danej długości próby, skośności i grubości ogonów. Dopóki PSR nie przekroczy typowego progu 0,95, edge nie jest jeszcze dowiedziony statystycznie. A jeśli prawdziwe μ jest niższe, niż wygląda z próbki, to prawdziwy Kelly jest niższy niż policzony. Skoro nie wiesz dokładnie, ile masz edge'u, musisz grać frakcją, i to nie z ostrożności, tylko z rachunku: niepewność co do rozkładu to kolejny, niezależny powód, żeby zejść poniżej pełnego Kelly'ego. Gra ułamkiem przy niedowiedzionym edge nie jest opcją, jest obowiązkiem.

Uczciwie trzeba też dodać, że symulacje ryzyka obsunięcia bywają optymistyczne z innego powodu. Typowy bootstrap losuje trady z powtórzeniami i miesza ich kolejność, zakładając, że są niezależne. W realnym torze bywają skorelowane w czasie: seria strat pod jeden reżim rynku potrafi ustawić się jedna za drugą, a wtedy prawdziwe obsunięcie jest gorsze niż w wymieszanej symulacji. Innymi słowy, rachunek bezpiecznej frakcji jest raczej optymistyczny niż pesymistyczny. Kolejny argument, żeby nie zaokrąglać w górę.

## Prawdziwa dźwignia to ucięty ogon

Skoro to lewy ogon rządzi bezpieczną frakcją, to najsilniejszą dźwignią nie jest większy lot, tylko krótszy ogon. Weź strategię, której najgorszy pojedynczy trade to minus 20 jednostek na tle rozkładu skupionego wokół małych wartości. Dołóż twardy stop loss, który ucina tę stratę do minus 8:

```
najgorszy trade:   −20   →   −8      (twardy SL)
skośność rozkładu:  spada
PSR:                rośnie
efekt:              wyższa bezpieczna frakcja Kelly'ego
```

To jest kontrintuicyjne i dlatego warte podkreślenia. Ucięcie jednej brzydkiej straty nie tylko ratuje kapitał na tym konkretnym tradzie. Ono podnosi jakość całego edge'u: rozkład robi się mniej skośny, PSR rośnie, a to z kolei pozwala bezpiecznie grać większą frakcją niż wcześniej. Kolejność jest sztywna: najpierw utnij ogon, dopiero potem masz prawo myśleć o większym locie. Odwrotnie to hazard.

Innymi słowy, stop loss to nie koszt, to mnożnik. Nie dlatego, że ładnie wygląda w statystykach, tylko dlatego, że matematycznie odblokowuje frakcję, której bez niego nie wolno Ci tknąć.

## Czego Kelly nie jest: martingale to anty-Kelly

Warto dopowiedzieć, czym ten sposób myślenia NIE jest. Martingale, czyli dokładanie lota po stracie, żeby się odkuć, to dokładne przeciwieństwo Kelly'ego. Kelly skaluje pozycję według edge'u i zmienności, a nie według tego, jak bardzo chcesz odzyskać stratę. Zwiększanie ryzyka po serii strat to anty-Kelly i najkrótsza znana droga do zera, bo dokłada wielkość pozycji dokładnie tam, gdzie lewy ogon właśnie się realizuje.

## Jak myśleć o wielkości pozycji

Z całej tej matematyki wychodzi jedna prosta zasada operacyjna: wielkość pozycji liczysz z bezpiecznej frakcji, a nie z tego, jak bardzo w danym momencie wierzysz w setup. Frakcja, nie pełny Kelly. Ustawiony sufit lota jako twardy górny limit, niższy tryb ochrony po serii strat albo w nieczytelnym reżimie, i czerwona linia na wysokości pełnego Kelly'ego, której nie przekraczasz nigdy.

Bo tak trzeba to ustawić w głowie. Edge nie jest licencją na większy lot. Wysoka skuteczność nie jest licencją na większy lot, bo o obsunięciu decyduje wielkość rzadkiej straty, a nie częstość wygranych. Jedyne, co ustala dopuszczalną wielkość pozycji, to jak głęboko potrafi Cię ściąć rzadka strata, a na to najlepszą odpowiedzią jest krótszy ogon i frakcja Kelly'ego, nie cały Kelly. Ogon jest ważniejszy niż wielkość. Kto to odwróci, ten prędzej czy później odda konto normalnej zmienności, nie żadnemu spektakularnemu błędowi.

To nie jest porada inwestycyjna. To wykład matematyki sizingu i tego, dlaczego racjonalna wielkość pozycji jest niższa, niż podpowiada apetyt, zanim ustawisz swój lot. Źródła: Kelly (1956), Thorp (kryterium Kelly'ego w blackjacku i na rynkach), Busseti i Boyd (risk-constrained Kelly, 2016).

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
