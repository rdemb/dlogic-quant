---
title: "Aukcje otwarcia, zamknięcia i fixing. Najważniejsze minuty sesji"
description: "Aukcja jednej ceny zbiera zlecenia i kojarzy je po jednym kursie, który maksymalizuje obrót. Tekst tłumaczy, dlaczego giełdy otwierają i zamykają dzień aukcją, czemu udział aukcji zamknięcia w wolumenie akcji w USA wzrósł z 3,1% w 2010 do 7,5% w 2018 roku, jak działa fixing walutowy WM/Reuters z okna 16:00 czasu londyńskiego i jak wyglądał skandal manipulacji z lat 2008-2013, zakończony karami ponad 5,7 mld dolarów. Na koniec częste aukcje wsadowe jako odpowiedź na wyścig zbrojeń HFT."
date: 2026-07-05 11:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
dek: "Przez większość dnia rynek handluje ciągle, transakcja po transakcji, ale najważniejsze ceny dnia powstają inaczej. Otwarcie i zamknięcie giełd wyznacza aukcja jednej ceny, a kursy referencyjne na rynku walutowym ustala fixing z krótkiego okna pomiarowego. Tekst rozkłada oba mechanizmy na części: od tego, jak aukcja kojarzy zlecenia po kursie maksymalizującym obrót, przez rosnącą siłę aukcji zamknięcia w epoce ETF, po skandal fixingowy na FX i pomysł częstych aukcji wsadowych. Po polsku, na mechanice, bez obietnic."
readingTime: 8
tags: ["aukcja otwarcia", "aukcja zamknięcia", "call auction", fixing, "WM/Reuters", benchmark, "cena zamknięcia", indeksowanie, ETF, "skandal FX", FCA, CFTC, DOJ, "batch auctions", HFT, mikrostruktura, edukacja, Forex]
category: edukacja
---

> **W skrócie**
>
> - Aukcja jednej ceny (call auction) najpierw przez pewien czas zbiera zlecenia kupna i sprzedaży bez zawierania transakcji, a potem kojarzy je po jednym kursie, przy którym da się wymienić największy wolumen. Wszyscy handlują po tej samej cenie, przewaga ułamka sekundy niemal znika, a rozproszona płynność skupia się w jednym punkcie.
> - Giełdy akcji otwierają i zamykają dzień aukcją, bo potrzebują wiarygodnej ceny odniesienia po nocnej przerwie i na koniec dnia. Aukcja zamknięcia rośnie w siłę: jej udział w wolumenie obrotu akcjami w USA wzrósł z 3,1% w 2010 do 7,5% w 2018 roku, a napędza to indeksowanie i ETF, bo fundusze indeksowe chcą handlować dokładnie po cenie zamknięcia (Bogousslavsky i Muravyev, 2023).
> - Rynek walutowy nie ma zamknięcia, więc rolę ceny referencyjnej pełni fixing WM/Reuters z krótkiego okna wokół 16:00 czasu londyńskiego. W latach 2008-2013 traderzy kilku banków zmawiali się w chatroomach i grali na wyprzedzenie zleceń klientów wokół tego okna. Kary: 1,1 mld funtów od FCA i 1,4 mld dolarów od CFTC w listopadzie 2014, a w maju 2015 ugody z amerykańskim Departamentem Sprawiedliwości i łącznie ponad 5,7 mld dolarów.
> - Budish, Cramton i Shim (2015) pokazali, że handel w czasie ciągłym strukturalnie premiuje szybkość, i zaproponowali częste aukcje wsadowe: rynek rozstrzygany aukcją w krótkich odstępach likwiduje wyścig o nanosekundy, bo o wykonaniu decyduje cena, a nie kolejność dobiegnięcia.

**Teza w jednym zdaniu:** Otwarcie, zamknięcie i okno fixingu to minuty, w których cena nie powstaje z ciągłego strumienia pojedynczych transakcji, tylko z celowo skupionego wolumenu, i właśnie dlatego te momenty są jednocześnie najbardziej wiarygodne jako punkt odniesienia i najbardziej kuszące dla tych, którzy chcieliby je przesunąć.

## Dwa tryby handlu: notowania ciągłe i aukcja jednej ceny

Przez większość sesji nowoczesna giełda działa w trybie notowań ciągłych. Zlecenia napływają do księgi, a transakcja zawiera się w chwili, gdy oferta kupna spotka ofertę sprzedaży, w kolejności wyznaczonej priorytetem cena-czas. Cena rynkowa jest wtedy sekwencją pojedynczych transakcji: każda może mieć inny kurs, a między kolejnymi kurs potrafi skakać. Ten tryb daje natychmiastowość, ale ma cechę, o której rzadko się pamięta: każda pojedyncza cena powstaje z jednego skojarzenia dwóch zleceń, czasem drobnych i przypadkowych.

Aukcja jednej ceny (po angielsku call auction) działa inaczej, a klasyczny opis obu trybów i ich własności daje Harris (2003). Najpierw przez ustalony czas system zbiera zlecenia kupna i sprzedaży, ale żadnej transakcji nie zawiera. Potem wyznacza jeden kurs rozliczenia: taki, przy którym skojarzyć można największy wolumen. Wszystkie transakcje aukcji wykonują się po tym jednym kursie, więc kupujący z limitem powyżej niego i sprzedający z limitem poniżej niego dostają cenę lepszą, niż żądali. Na warszawskiej GPW ten mechanizm nosi zresztą swojską nazwę: fazy fixingu otwarcia i zamknięcia.

```
AUKCJA JEDNEJ CENY   (przykład ilustracyjny, nie dane rzeczywiste)

zlecenia kupna               zlecenia sprzedaży
limit     wolumen            limit     wolumen
10.04     2 000              9.96      1 000
10.02     3 000              9.98      2 000
10.00     4 000              10.00     5 000
9.98      3 000              10.02     4 000

szukanie ceny rozliczenia:
cena     popyt (limity >= ceny)   podaż (limity <= ceny)   obrót = minimum
9.98     12 000                    3 000                    3 000
10.00     9 000                    8 000                    8 000   <-- maksimum
10.02     5 000                   12 000                    5 000

cena aukcji = 10.00
wszystkie transakcje wykonują się po 10.00, skojarzony wolumen 8 000
```

Sposób wyznaczenia kursu widać w przykładzie. Przy cenie 10.00 kupić chcą wszyscy z limitem 10.00 lub wyższym, łącznie 9 000 sztuk, a sprzedać wszyscy z limitem 10.00 lub niższym, łącznie 8 000 sztuk. Skojarzyć da się mniejszą z tych liczb, czyli 8 000, i to jest najwięcej ze wszystkich możliwych kursów, więc aukcja rozlicza się po 10.00. Popyt przy tej cenie przewyższa podaż, więc zlecenia kupna z limitem równym dokładnie 10.00 zostaną wykonane tylko częściowo, według reguły kolejności przyjętej przez daną giełdę, a niewykonane resztki mogą przejść do notowań ciągłych.

<figure>
<svg viewBox="0 0 640 340" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="12" y="22" font-size="13" fill="currentColor">Aukcja jednej ceny: gdzie popyt spotyka podaż (przykład ilustracyjny)</text><line x1="120" y1="38" x2="150" y2="38" stroke="#1a9e6a" stroke-width="2.5"/><text x="156" y="42" font-size="10.5" fill="currentColor" opacity="0.75">skumulowany popyt (kupno)</text><line x1="330" y1="38" x2="360" y2="38" stroke="#e5484d" stroke-width="2.5"/><text x="366" y="42" font-size="10.5" fill="currentColor" opacity="0.75">skumulowana podaż (sprzedaż)</text><text x="96" y="56" font-size="10" fill="currentColor" opacity="0.5" text-anchor="end">wolumen</text><line x1="100" y1="213" x2="570" y2="213" stroke="currentColor" stroke-width="1" opacity="0.08"/><line x1="100" y1="60" x2="570" y2="60" stroke="currentColor" stroke-width="1" opacity="0.08"/><line x1="100" y1="60" x2="100" y2="290" stroke="currentColor" stroke-width="1" opacity="0.35"/><line x1="100" y1="290" x2="570" y2="290" stroke="currentColor" stroke-width="1" opacity="0.35"/><text x="92" y="293" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end" font-family="monospace">0</text><text x="92" y="217" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end" font-family="monospace">4 000</text><text x="92" y="141" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end" font-family="monospace">8 000</text><text x="92" y="64" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end" font-family="monospace">12 000</text><line x1="120" y1="290" x2="120" y2="295" stroke="currentColor" opacity="0.35"/><line x1="220" y1="290" x2="220" y2="295" stroke="currentColor" opacity="0.35"/><line x1="320" y1="290" x2="320" y2="295" stroke="currentColor" opacity="0.35"/><line x1="420" y1="290" x2="420" y2="295" stroke="currentColor" opacity="0.35"/><line x1="520" y1="290" x2="520" y2="295" stroke="currentColor" opacity="0.35"/><text x="120" y="310" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle" font-family="monospace">9.96</text><text x="220" y="310" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle" font-family="monospace">9.98</text><text x="320" y="310" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle" font-family="monospace">10.00</text><text x="420" y="310" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle" font-family="monospace">10.02</text><text x="520" y="310" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle" font-family="monospace">10.04</text><text x="575" y="294" font-size="10" fill="currentColor" opacity="0.5">cena</text><path d="M123 271 H223 V233 H323 V137 H423 V60 H523" stroke="#e5484d" stroke-width="2.5" fill="none"/><path d="M120 60 H220 V118 H320 V194 H420 V252 H520" stroke="#1a9e6a" stroke-width="2.5" fill="none"/><line x1="320" y1="137" x2="320" y2="290" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.45"/><line x1="100" y1="137" x2="320" y2="137" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.45"/><circle cx="320" cy="137" r="4.5" fill="currentColor"/><text x="340" y="118" font-size="11" fill="currentColor">cena aukcji = 10.00</text><text x="340" y="132" font-size="10.5" fill="currentColor" opacity="0.75">skojarzony obrót = 8 000</text></svg>
<figcaption>Aukcja jednej ceny z przykładu powyżej. Zielona schodkowa linia to skumulowany popyt (wolumen zleceń kupna z limitem nie niższym niż dana cena), czerwona to skumulowana podaż (limity nie wyższe niż dana cena). Możliwy do skojarzenia obrót przy każdej cenie to mniejsza z dwóch wartości. Największy, 8 000, wypada przy kursie 10.00 i to on zostaje ceną aukcji dla wszystkich transakcji.</figcaption>
</figure>

Z tej konstrukcji wynikają dwie własności, dla których giełdy w ogóle sięgają po aukcje. Po pierwsze, płynność się skupia: zamiast strumienia rozproszonych transakcji wszyscy zainteresowani spotykają się w jednym punkcie czasu, więc cena aukcji powstaje ze znacznie większego wolumenu niż jakakolwiek pojedyncza transakcja w handlu ciągłym. Po drugie, przewaga szybkości niemal znika: skoro zlecenia i tak czekają do końca zbiórki i wykonują się po wspólnym kursie, bycie o milisekundę wcześniej praktycznie nic nie zmienia. W notowaniach ciągłych szybkość bywa decydująca, w aukcji liczy się cena.

## Po co giełdom aukcja na otwarciu i zamknięciu

Otwarcie rozwiązuje problem nocy. Od zamknięcia poprzedniej sesji nagromadziły się informacje: raporty spółek, dane makro, ruchy na rynkach w innych strefach czasowych, a handlu nie było. Pierwsza cena dnia musi to wszystko zagregować naraz. Gdyby sesja zaczynała się od razu notowaniami ciągłymi, pierwszą cenę ustaliłoby jedno zlecenie trafiające w płytką, dopiero budującą się księgę, i mogłoby to być zlecenie zupełnie przypadkowe. Aukcja otwarcia najpierw zbiera zlecenia wszystkich, którzy nocne wiadomości przetrawili, i dopiero z tej zbiorczej podaży i popytu wyznacza kurs.

Zamknięcie rozwiązuje problem odniesienia. Cena zamknięcia to najważniejsza pojedyncza liczba dnia: po niej wycenia się jednostki funduszy, rozlicza instrumenty pochodne, liczy wartości indeksów i depozyty zabezpieczające. Jest zbyt ważna, żeby zostawić ją ostatniej przypadkowej transakcji. W czystych notowaniach ciągłych jedno niewielkie, agresywne zlecenie w ostatniej sekundzie mogłoby ustawić oficjalne zamknięcie, a więc i wycenę tysięcy portfeli. W aukcji cena zamknięcia powstaje z całego zebranego wolumenu skojarzonego po jednym kursie: żeby ją przesunąć, trzeba przeważyć zagregowany popyt lub podaż, a nie zjeść na moment szczyt księgi. Manipulacja nie staje się niemożliwa, ale jej koszt rośnie o rzędy wielkości i zostawia wyraźniejszy ślad.

## Aukcja zamknięcia rośnie w siłę: indeksowanie i ETF

Przez lata aukcja zamknięcia była dodatkiem do sesji, ale ostatnia dekada zmieniła proporcje. Bogousslavsky i Muravyev (2023) policzyli w pracy „Who Trades at the Close?", że udział aukcji zamknięcia w całkowitym wolumenie obrotu akcjami w USA wzrósł z 3,1% w 2010 do 7,5% w 2018 roku, czyli ponad dwukrotnie. Mechanizm jest strukturalny: rośnie inwestowanie indeksowe i ETF, a fundusz indeksowy rozliczany jest z ceny zamknięcia. Jeśli chce odwzorować indeks bez błędu odwzorowania, powinien kupować i sprzedawać dokładnie po tej cenie, więc kieruje zlecenia typu market-on-close prosto do aukcji. Im więcej pieniędzy w strategiach pasywnych, tym więcej wolumenu spływa do ostatnich minut dnia.

Warto zauważyć, czym ten wolumen jest, a czym nie jest. To w przeważającej mierze przepływ płynnościowy, nie informacyjny: fundusz indeksowy kupuje na zamknięciu nie dlatego, że coś wie o spółce, tylko dlatego, że dostał napływy i potrzebuje ceny zamknięcia. Końcówka sesji to przez to inny tłum niż środek dnia: mniej zakładów o wartość, więcej mechanicznego rebalansowania, skupionego w jednym, z góry znanym momencie.

## FX nie ma zamknięcia, więc ma fixing

Rynek walutowy tego mechanizmu nie ma. Jest zdecentralizowany, handluje całą dobę przez pięć dni w tygodniu i nie istnieje giełda, która mogłaby ogłosić aukcję zamknięcia dla EUR/USD. Potrzeba ceny referencyjnej jest jednak identyczna jak na akcjach: globalne portfele trzeba na koniec dnia wyceny przeliczyć do wspólnej waluty, indeksy wielowalutowe potrzebują kursów, firmy rozliczają zabezpieczenia. Tę rolę pełni fixing, a najważniejszy jest benchmark WM/Reuters, wyznaczany z krótkiego okna pomiarowego wokół 16:00 czasu londyńskiego, czyli 17:00 czasu polskiego. Kurs liczony jest mechanicznie z rzeczywistych transakcji i kwotowań zebranych w tym oknie i publikowany jako oficjalna stawka dnia, do której odnoszą się wyceny portfeli i indeksów.

Z punktu widzenia klienta wygląda to wygodnie: fundusz składa bankowi zlecenie „na fixing", czyli do wykonania po kursie benchmarku, jakikolwiek on będzie, i ma gwarancję wyceny spójnej z indeksem. Z punktu widzenia konstrukcji rynku jest jednak zasadnicza różnica wobec aukcji: fixing nie zbiera zleceń w jednym miejscu i nie wyznacza kursu czyszczącego rynek. Jest migawką, pomiarem tego, co i tak dzieje się w handlu ciągłym w krótkim oknie. A bank, który przyjął zlecenia na fixing, zna z wyprzedzeniem kierunek i przybliżoną skalę przepływu, który sam będzie musiał w tym oknie wykonać. Ta kombinacja, przewidywalny przepływ plus krótkie okno pomiaru, okazała się zapalna.

## Skandal fixingowy: chatroomy i miliardowe kary

Między 2008 a 2013 rokiem traderzy kilku wielkich banków dilerskich zamienili tę kombinację w maszynkę do zarabiania na klientach. W zamkniętych chatroomach, z których jeden nosił nazwę „The Cartel", wymieniali się poufnymi informacjami o zleceniach klientów na fixing i koordynowali strategie. Schemat był prosty: jeśli wiadomo, że w oknie trzeba będzie kupić dla klientów dużo danej waluty, można najpierw kupić ją na własny rachunek, a potem handlować w oknie agresywnie tak, żeby pchnąć kurs wyżej (w żargonie „banging the close"). Klient dostaje gorszy kurs referencyjny, bank zarabia na pozycji zajętej przed oknem, a w zapisach wszystko wygląda jak zwykły handel.

Precyzja jest tu ważna, bo skrót „zmanipulowali benchmark WM/Reuters" bywa mylący. Sama metodologia benchmarku działała tak, jak ją zaprojektowano: mierzyła rynek w oknie. Manipulacja dotyczyła handlu wokół okna, bo skoordynowane zlecenia przesuwały rynek, który benchmark potem uczciwie mierzył. To rozróżnienie nie jest kosmetyczne. Pokazuje, że słabym punktem nie był wzór matematyczny, tylko konstrukcja: krótkie okno pomiaru w połączeniu z uczestnikami, którzy znają cudze przepływy i mogą je wyprzedzać.

Rachunek przyszedł w dwóch ratach. W listopadzie 2014 brytyjska FCA nałożyła łącznie 1,1 mld funtów kar na pięć banków, ówcześnie rekordowe, a równolegle amerykańska CFTC wymierzyła 1,4 mld dolarów. W maju 2015 sprawę domknęły ugody z amerykańskim Departamentem Sprawiedliwości (DOJ): banki przyznały się do winy, a łączna kwota kar przekroczyła 5,7 mld dolarów. Zmieniła się też sama konstrukcja benchmarku: okno pomiarowe wydłużono z jednej minuty do pięciu, żeby trudniej było je przepchnąć skoordynowanym przepływem, wzmocniono nadzór nad benchmarkami i kontrole wewnątrz banków, a rynek walutowy dostał globalny kodeks dobrych praktyk (FX Global Code).

## Częste aukcje wsadowe: propozycja na wyścig zbrojeń

Skandal fixingowy obnażył słabość pomiaru z krótkiego okna. Budish, Cramton i Shim (2015) obnażyli słabość samego handlu ciągłego, i to na najbardziej rozwiniętych rynkach świata. Ich diagnoza: jeśli rynek działa w czasie ciągłym, to na horyzoncie milisekund korelacje między blisko powiązanymi instrumentami załamują się i nieustannie powstają mechaniczne okazje arbitrażowe, które zgarnia ten, kto pierwszy dobiegnie. Wyścig o szybkość nie jest patologią uczestników, tylko cechą konstrukcji: nagroda za bycie pierwszym odnawia się bez końca, więc opłaca się wydawać kolejne miliardy na szybsze łącza i kolokację, a koszt tych zbrojeń wraca do inwestorów w cenie płynności.

Ich propozycja to częste aukcje wsadowe (frequent batch auctions): podzielić dzień na bardzo krótkie odstępy, rzędu ułamków sekundy, w każdym zbierać zlecenia i rozstrzygać je aukcją jednej ceny. W obrębie odstępu kolejność przybycia zleceń przestaje mieć znaczenie, konkuruje się ceną, nie szybkością, a przewaga nanosekundowa traci wartość, bo nie zmienia wyniku aukcji. Obraz się domyka: aukcja, mechanizm starszy niż handel elektroniczny, wraca jako propozycja naprawy jego najnowszego problemu. Rynki na dużą skalę tej reformy nie wdrożyły, ale praca przesunęła debatę o tym, co w strukturze rynku jest daną naturalną, a co wyborem projektowym.

## Co z tego wynika przy ekranie

Praktyczna nauka jest jedna, ale ma kilka twarzy: otwarcie, zamknięcie i okna fixingów to momenty o innej mechanice niż reszta sesji. Wolumen jest skupiony, duża jego część to przepływy mechaniczne i z góry przewidywalne (indeksowe na zamknięciu giełd akcji, fixingowe na FX wokół 17:00 czasu polskiego, szczególnie na przełomie miesiąca, gdy portfele się rebalansują), a skład uczestników różni się od środka dnia. Ten sam ruch ceny znaczy więc co innego w oknie fixingu, a co innego o 14:30: w oknie może odzwierciedlać mechaniczny przepływ, nie zmianę przekonań rynku.

Druga twarz dotyczy danych. Na giełdach akcji ceny otwarcia i zamknięcia świec dziennych to zwykle wydruki z aukcji, czyli kursy o szczególnym statusie, powstałe ze skupionego wolumenu. Na rynku walutowym doba nie ma naturalnego końca, więc „zamknięcie" świecy dziennej to umowna migawka handlu ciągłego, zależna od konwencji dostawcy danych i strefy czasowej platformy. Traktowanie obu rodzajów zamknięć jak tej samej wielkości to prosta droga do błędów w analizie.

I trzecia twarz, ta od skandalu: tam, gdzie skupia się przewidywalny przepływ, skupia się też pokusa. O tym, ile kosztuje przesunięcie ceny referencyjnej, decyduje konstrukcja mechanizmu. Aukcja z jedną ceną agreguje cały zebrany popyt i podaż, a pomiar krótkiego okna w handlu ciągłym agreguje tylko to, co ktoś zdążył w tym oknie zrobić. Historia kar za fixing to w gruncie rzeczy lekcja z projektowania rynków, wyceniona na ponad 5,7 mld dolarów.

To nie jest porada inwestycyjna. To opis mechanizmów rynkowych, podany z definicjami i udokumentowanymi liczbami, żeby było wiadomo, jak powstają najważniejsze ceny dnia i dlaczego wokół nich obowiązują inne reguły niż przez resztę sesji.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
