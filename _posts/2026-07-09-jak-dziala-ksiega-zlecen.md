---
title: "Jak działa księga zleceń. Bid, ask i skąd bierze się spread"
description: "Księga zleceń (limit order book) to dwie listy ofert, kupna i sprzedaży, uporządkowane według ceny i czasu. Tekst rozkłada jej mechanikę na części: bid, ask, spread, głębokość, różnicę między zleceniem limit a market oraz priorytet cena-czas. Dalej pokazuje, skąd naprawdę bierze się spread: koszty operacyjne, ryzyko zapasu i adverse selection, aż po intuicję modelu Glostena-Milgroma i market making Avellanedy-Stoikova. Bez żargonu, na samej mechanice."
date: 2026-07-09 21:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
dek: "Za każdą ceną na wykresie stoi lista ofert kupna i sprzedaży. Tekst rozkłada tę listę na części: najlepszy bid i ask, spread, głębokość, zlecenia limit kontra market, priorytet cena-czas, wpływ dużego zlecenia na cenę oraz to, dlaczego spread w ogóle istnieje. Od budowy księgi po adverse selection i modele market makerów. Po polsku, na mechanice, bez obietnic."
readingTime: 8
tags: ["księga zleceń", "limit order book", LOB, bid, ask, spread, głębokość, "market impact", "adverse selection", "Glosten-Milgrom", "Avellaneda-Stoikov", "market making", mikrostruktura, płynność, edukacja, Forex]
category: edukacja
---

> **W skrócie**
>
> - Księga zleceń to dwie listy: oferty kupna (bid) i oferty sprzedaży (ask), każda opisana ceną i wolumenem, ułożone od najlepszej. Najlepszy bid to najwyższa cena, po której ktoś gotów jest kupić; najlepszy ask to najniższa cena, po której ktoś gotów jest sprzedać; spread to po prostu różnica między tymi dwiema liczbami.
> - Zlecenie limit czeka w księdze na swojej cenie i dostarcza płynność; zlecenie market wykonuje się natychmiast po przeciwnej stronie księgi, bierze płynność i płaci spread. O kolejności wykonania decyduje priorytet cena-czas: najpierw lepsza cena, a przy równej cenie zlecenie złożone wcześniej.
> - Duże zlecenie market nie realizuje się po jednej cenie. Zjada kolejne poziomy księgi, więc jego średnia cena wykonania jest gorsza od najlepszej kwoty, a ta różnica to wpływ na cenę (market impact). To, ile poziomów trzeba zjeść, żeby wypełnić zlecenie, mierzy głębokość.
> - Spread nie jest przypadkowy. Pokrywa koszty operacyjne dostarczyciela płynności, ryzyko trzymania zapasu oraz ryzyko handlu z lepiej poinformowanym (adverse selection). Model Glostena-Milgroma (1985) pokazuje, że sam ten ostatni składnik wystarcza, żeby spread był dodatni, nawet przy zerowych kosztach i konkurencji doskonałej.

**Teza w jednym zdaniu:** Spread to nie opłata cennikowa, tylko cena natychmiastowości i rekompensata dla dostarczyciela płynności za ryzyko, że po drugiej stronie transakcji siedzi ktoś lepiej poinformowany, a księga zleceń to mechanizm, który tę cenę na bieżąco ustala.

## Księga zleceń: dwie kolumny ofert

Za każdą pojedynczą ceną, którą widać na wykresie, stoi struktura znacznie bogatsza: księga zleceń, po angielsku limit order book. To zbiór wszystkich aktualnych, niezrealizowanych zleceń z limitem ceny, posortowany na dwie strony. Strona kupna (bid) grupuje oferty kupienia, uporządkowane od najwyższej ceny w dół. Strona sprzedaży (ask, czasem offer) grupuje oferty sprzedaży, uporządkowane od najniższej ceny w górę. Każdy poziom ma dwie liczby: cenę oraz wolumen, czyli ile jednostki da się na tej cenie kupić lub sprzedać.

Dwie liczby są ważniejsze od reszty. Najlepszy bid to najwyższa cena, po której ktoś w tej chwili chce kupić. Najlepszy ask to najniższa cena, po której ktoś w tej chwili chce sprzedać. Para tych dwóch nazywa się szczytem księgi (top of book) albo dotknięciem (the touch). Ich różnica to spread, a punkt w połowie między nimi to cena środkowa (mid). Poniższy schemat pokazuje to na jednym obrazku.

```
KSIĘGA ZLECEŃ EUR/USD   (przykład ilustracyjny, nie dane rzeczywiste)

  ASK  oferty sprzedaży, od najniższej ceny w górę
  cena       wolumen
  1.08125    4.0 mln
  1.08124    3.0 mln
  1.08123    2.5 mln
  1.08122    1.0 mln    <-- najlepszy ASK
  ....................    spread = 1.08122 - 1.08120 = 0.00002 = 0.2 pip
  1.08120    1.5 mln    <-- najlepszy BID
  1.08119    3.0 mln
  1.08118    2.0 mln
  1.08117    5.0 mln
  BID  oferty kupna, od najwyższej ceny w dół

  mid = (1.08122 + 1.08120) / 2 = 1.08121
```

Kilka rzeczy widać od razu. Między najlepszym bidem a najlepszym askiem jest pusta przestrzeń: nikt nie oferuje sprzedaży taniej niż 1.08122 ani kupna drożej niż 1.08120, bo gdyby oferty się nakładały, natychmiast doszłoby do transakcji i przestałyby wisieć w księdze. Wolumeny na kolejnych poziomach bywają nierówne, co odzwierciedla rozkład zainteresowania po obu stronach. A cała ta struktura zmienia się wiele razy na sekundę, bo zlecenia napływają, są anulowane i realizowane. Porządny przegląd definicji i własności ksiąg zleceń dają Gould i współautorzy (2013).

<figure>
<svg viewBox="0 0 640 320" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="lobArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 2L8 5L2 8" fill="none" stroke="currentColor" stroke-width="1.4"/></marker></defs><text x="12" y="22" font-size="13" fill="currentColor">Księga zleceń EUR/USD (przykład ilustracyjny)</text><line x1="100" y1="54" x2="100" y2="278" stroke="currentColor" stroke-width="1" opacity="0.14"/><text x="12" y="48" font-size="10" fill="currentColor" opacity="0.5">cena</text><text x="100" y="48" font-size="11" fill="#e5484d">ASK oferty sprzedaży</text><text x="628" y="48" font-size="10" fill="currentColor" opacity="0.5" text-anchor="end">wolumen, mln EUR</text><rect x="100" y="58" width="248" height="15" rx="2" fill="#e5484d" opacity="0.82"/><text x="12" y="69" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08125</text><text x="356" y="69" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">4.0</text><rect x="100" y="82" width="186" height="15" rx="2" fill="#e5484d" opacity="0.82"/><text x="12" y="93" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08124</text><text x="294" y="93" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">3.0</text><rect x="100" y="106" width="155" height="15" rx="2" fill="#e5484d" opacity="0.82"/><text x="12" y="117" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08123</text><text x="263" y="117" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">2.5</text><rect x="100" y="130" width="62" height="15" rx="2" fill="#e5484d"/><text x="12" y="141" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08122</text><text x="170" y="141" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">1.0</text><text x="205" y="141" font-size="10.5" fill="#e5484d">najlepszy ASK</text><line x1="100" y1="150" x2="430" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.4"/><line x1="100" y1="182" x2="430" y2="182" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.4"/><g opacity="0.6"><line x1="470" y1="151" x2="470" y2="181" stroke="currentColor" stroke-width="1.3" marker-start="url(#lobArr)" marker-end="url(#lobArr)"/></g><text x="484" y="162" font-size="11" fill="currentColor">SPREAD</text><text x="484" y="176" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">0.2 pip</text><text x="12" y="170" font-size="10" fill="currentColor" opacity="0.6" font-family="monospace">mid 1.08121</text><rect x="100" y="188" width="93" height="15" rx="2" fill="#1a9e6a"/><text x="12" y="199" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08120</text><text x="201" y="199" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">1.5</text><text x="236" y="199" font-size="10.5" fill="#1a9e6a">najlepszy BID</text><rect x="100" y="212" width="186" height="15" rx="2" fill="#1a9e6a" opacity="0.82"/><text x="12" y="223" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08119</text><text x="294" y="223" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">3.0</text><rect x="100" y="236" width="124" height="15" rx="2" fill="#1a9e6a" opacity="0.82"/><text x="12" y="247" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08118</text><text x="232" y="247" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">2.0</text><rect x="100" y="260" width="310" height="15" rx="2" fill="#1a9e6a" opacity="0.82"/><text x="12" y="271" font-size="11" fill="currentColor" opacity="0.85" font-family="monospace">1.08117</text><text x="418" y="271" font-size="10.5" fill="currentColor" opacity="0.7" font-family="monospace">5.0</text><text x="100" y="296" font-size="11" fill="#1a9e6a">BID oferty kupna</text></svg>
<figcaption>Schemat księgi zleceń (przykład ilustracyjny, nie dane rzeczywiste). U góry oferty sprzedaży (ask, czerwony), u dołu oferty kupna (bid, zielony), a między najlepszym askiem a najlepszym bidem leży spread. Długość słupka to wolumen na danym poziomie ceny, najmniejszy tuż przy szczycie księgi. Mid to punkt w połowie spreadu.</figcaption>
</figure>

## Zlecenie limit kontra market: kto dostarcza, kto bierze płynność

Są dwa podstawowe typy zleceń i różnica między nimi jest kluczem do zrozumienia całej reszty. Zlecenie z limitem (limit order) mówi: „kup, ale nie drożej niż X" albo „sprzedaj, ale nie taniej niż Y". Jeśli nie da się go od razu wykonać po żądanej cenie, ląduje w księdze i czeka. Przez sam fakt czekania takie zlecenie dostarcza płynności: to ono buduje poziomy, które widać na schemacie, i to na nim wykona się ktoś inny. W zamian za cierpliwość dostawca płynności nie płaci spreadu, a często dostaje od giełdy rabat.

Zlecenie po cenie rynkowej (market order) mówi: „kup teraz, po jakiejkolwiek cenie jest dostępna". Nie czeka, tylko od razu wykonuje się po przeciwnej stronie księgi, zjadając wiszące tam zlecenia limit. Takie zlecenie bierze płynność i płaci za nią spreadem. W księdze z przykładu kupno market wykona się po najlepszym asku 1.08122, choć mid wynosi 1.08121. Ten pół spreadu ponad mid to koszt natychmiastowości: cena, jaką płaci się za to, że nie chce się czekać.

O kolejności realizacji decyduje priorytet cena-czas (price-time priority). Pierwsze pierwszeństwo ma cena: zlecenie z lepszą ceną wykona się przed gorszym. Przy równej cenie o kolejce decyduje czas: zlecenie złożone wcześniej stoi z przodu i zostanie wypełnione jako pierwsze. Dlatego umieszczenie zlecenia limit to nie tylko wybór ceny, ale też miejsca w kolejce, a przesunięcie się o jeden poziom bliżej rynku potrafi oznaczać dużą różnicę w tym, czy i kiedy zlecenie w ogóle się wykona.

## Głębokość i wpływ na cenę: jak duże zlecenie zjada poziomy

Najlepsza kwota pokazuje tylko czubek. Głębokość (depth) to pytanie, ile płynności czeka za nim: jaki łączny wolumen jest dostępny na kolejnych poziomach po obu stronach. Ma to bezpośrednie przełożenie na to, co się stanie, gdy ktoś złoży zlecenie większe niż wolumen na szczycie księgi.

Weźmy księgę z przykładu i kupno market na 3.5 mln. Na najlepszym asku 1.08122 czeka tylko 1.0 mln, więc zlecenie bierze cały ten poziom, a resztę, 2.5 mln, dobija z następnego poziomu po 1.08123. W efekcie średnia cena wykonania to około 1.08123, czyli powyżej najlepszego asku, od którego wszystko się zaczęło. Ta różnica między najlepszą kwotą a rzeczywistą średnią ceną wypełnienia to wpływ na cenę (market impact). Skutek uboczny jest widoczny natychmiast: dwa dolne poziomy asku zniknęły, nowym najlepszym askiem staje się 1.08124, a spread chwilowo rozszerza się z 0.2 do 0.4 pip, dopóki nowe zlecenia limit go nie uzupełnią.

Stąd prosta zasada: im płytsza księga, tym drożej kosztuje ruszenie ceną, i tym mocniej pojedyncze duże zlecenie potrafi nią szarpnąć. Dlatego wielkie zlecenia zwykle tnie się na porcje rozłożone w czasie (metaorder), zamiast wrzucać je hurtem. Empiryczna prawidłowość, potwierdzona na wielu rynkach, jest taka, że skumulowany wpływ na cenę rośnie z rozmiarem wolniej niż liniowo, w przybliżeniu jak pierwiastek: podwojenie wolumenu nie podwaja kosztu wpływu (Bouchaud, Farmer i Lillo, 2009). Głębokość jest więc drugim wymiarem płynności obok spreadu: spread mówi, ile kosztuje mała transakcja tu i teraz, a głębokość mówi, jak szybko ten koszt rośnie wraz z rozmiarem.

## Skąd bierze się spread: trzy koszty dostarczyciela płynności

Skoro dostarczyciel płynności zarabia na spreadzie, to dlaczego konkurencja nie zbije go do zera? Bo spread pokrywa trzy realne koszty, i literatura mikrostruktury (dobry przegląd: Biais, Glosten i Spatt, 2005) rozkłada go zwykle na te same trzy składniki.

Pierwszy to koszty operacyjne (order processing): technologia, łącza, opłaty giełdowe, rozliczenie. To najprostszy, w miarę stały narzut na każdą transakcję. Drugi to ryzyko zapasu (inventory risk). Market maker, który sprzedał komuś walutę, zostaje z krótką pozycją, a kupując, z długą. Dopóki jej nie zamknie, jest wystawiony na ruch ceny. Im większy niechciany zapas i im większa zmienność, tym bardziej market maker przesuwa swoje kwotowania, żeby zachęcić rynek do odciążenia go po właściwej stronie. To wątek modeli zapasowych, od Stolla oraz Ho i Stolla po Amihuda i Mendelsona.

Trzeci składnik jest najciekawszy i najważniejszy: adverse selection, czyli ryzyko negatywnej selekcji. Dostarczyciel płynności wystawia oferty w ciemno, nie wiedząc, kto je weźmie. Część kontrahentów handluje z powodów niezwiązanych z wartością (potrzeba płynności, hedging, przepływy), ale część wie coś, czego market maker jeszcze nie wie. Kłopot w tym, że poinformowany kupuje właśnie wtedy, gdy cena ma pójść w górę, i sprzedaje, gdy ma spaść. Wystawiając kwotowania, market maker systematycznie przegrywa z tą grupą: sprzedaje im tuż przed wzrostem, odkupuje tuż przed spadkiem. Spread jest po to, żeby to, co market maker zarabia na nieinformowanych, pokryło to, co traci na poinformowanych.

## Glosten i Milgrom: spread jako cena ryzyka informacyjnego

Najczystszą intuicję na adverse selection dają Glosten i Milgrom (1985). Ich model odziera problem ze wszystkiego zbędnego: market maker jest neutralny wobec ryzyka, działa w konkurencji doskonałej (zerowy oczekiwany zysk) i nie ponosi żadnych kosztów operacyjnych ani zapasowych. Zostaje sama informacja. Na rynku miesza się dwa typy graczy: poinformowani, którzy znają prawdziwą wartość, oraz nieinformowani, którzy handlują losowo względem wartości.

W tym świecie market maker ustawia kwotowania jak wartości warunkowe. Ask to oczekiwana wartość pod warunkiem, że napłynęło zlecenie kupna; bid to oczekiwana wartość pod warunkiem, że napłynęło zlecenie sprzedaży. Ponieważ kupno jest sygnałem, że nadawca może wiedzieć o wyższej wartości, ask ląduje powyżej bieżącego oczekiwania, a bid, symetrycznie, poniżej. Powstaje dodatni spread wokół wartości, choć nikt nie doliczał żadnej marży ani kosztu. Spread jest tu w całości ceną za ryzyko informacyjne.

Płyną z tego dwa wnioski, które warto zapamiętać. Po pierwsze, każda transakcja niesie informację, więc po każdej market maker aktualizuje przekonania w duchu reguły Bayesa, a cena stopniowo dryfuje ku prawdziwej wartości. To jest właśnie proces odkrywania ceny (price discovery): rynek uczy się z przepływu zleceń. Po drugie, szerokość spreadu skaluje się z udziałem poinformowanych i z niepewnością. Gdy rośnie prawdopodobieństwo, że po drugiej stronie siedzi ktoś, kto wie więcej (na przykład tuż przed publikacją danych), spread się rozszerza. Gdyby poinformowani zniknęli, w tym czystym modelu spread spadłby do zera. To dlatego płynność potrafi wyparować w sekundę przed odczytem makro: nie z powodu awarii, lecz dlatego, że ryzyko adverse selection skacze.

## Avellaneda i Stoikov: kwotowanie z ryzykiem zapasu

Model Glostena-Milgroma tłumaczy, dlaczego spread istnieje; Avellaneda i Stoikov (2008) pokazują, jak market maker powinien go praktycznie ustawiać, gdy jednocześnie martwi się o swój zapas. Ich rozwiązanie kręci się wokół ceny rezerwacji: to cena środkowa przesunięta w bok proporcjonalnie do aktualnej pozycji, zmienności i pozostałego czasu. Gdy market maker nabiera długiej pozycji, jego cena rezerwacji spada poniżej mid, więc kwotuje agresywniej po stronie sprzedaży i mniej chętnie kupuje, żeby zrzucić nadmiar zapasu; przy krótkiej pozycji dzieje się odwrotnie. Sam spread wokół ceny rezerwacji rozszerza się wraz ze zmiennością, awersją do ryzyka i horyzontem, a zwęża, gdy zleceń napływa gęściej. Cała konstrukcja to problem sterowania stochastycznego (równanie Hamiltona-Jacobiego-Bellmana), który godzi dwie siły z poprzednich akapitów: chęć zarobienia większego spreadu na transakcję z ryzykiem, że szersze kwotowanie rzadziej się wypełnia i dłużej trzyma niebezpieczny zapas. To do dziś kanoniczny punkt wyjścia dla algorytmicznego market makingu.

## Statystyka prawdziwych ksiąg

Modele są schludne, prawdziwe księgi mniej, a ich empiryczna statystyka to osobny, dojrzały dział (Bouchaud, Mezard i Potters, 2002; przeglądowo Gould i współautorzy, 2013). Kilka regularności warto znać, bo korygują naiwne wyobrażenia. Uśredniony kształt księgi nie jest gęsty tuż przy szczycie: gęstość zleceń zaczyna się nisko przy dotknięciu, rośnie do maksimum kilka poziomów dalej, po czym opada, więc realna płynność bywa cofnięta od najlepszej kwoty. Znaki transakcji mają długą pamięć: po kupnie częściej idzie kolejne kupno, a autokorelacja kierunku przepływu opada powoli, jak funkcja potęgowa, nie wykładniczo. Mimo to ceny pozostają blisko efektywne, bez silnej autokorelacji zwrotów, bo dostarczyciele płynności na bieżąco absorbują ten uporządkowany przepływ. I wreszcie płynność widoczna w księdze to często ułamek prawdziwej: duża jej część jest utajona i pojawia się dopiero, gdy cena po nią sięgnie. Te fakty są tłem dla wcześniejszej zasady o pierwiastkowym wpływie na cenę i tłumaczą, czemu ocena głębokości po samym szczycie księgi bywa myląca.

## Co z tego wynika przy ekranie

Dla kogoś, kto handluje na EUR/USD przez MT5, jedno zastrzeżenie jest istotne: rynek spot FX nie ma jednej, wspólnej księgi zleceń. Jest zdecentralizowany, a płynność rozsiana po platformach międzybankowych (jak EBS czy Refinitiv Matching, które akurat są klasycznymi księgami zleceń), dealerach i agregatorach. Detaliczny broker pobiera kwoty od dostawców płynności, dokłada narzut i pokazuje najczęściej sam szczyt: jeden bid i jeden ask. Głębokość rynku (DOM) w terminalu, jeśli w ogóle jest, to częściowa księga jednego dostawcy, a nie globalny obraz. Praktyczny skutek jest taki, że detaliczny trader prawie zawsze bierze płynność zleceniem market i płaci spread, rzadko ją dostarczając.

To nie zmienia jednak mechaniki, tylko to, ile z niej widać. Kwotowanie, które broker podaje, jest wypadkową dokładnie tych samych sił: kosztów operacyjnych, ryzyka zapasu i adverse selection u dostawcy płynności. Dlatego spread na EUR/USD nie jest stały. Rozszerza się przy niskiej płynności (przełom sesji, święta) i tuż przed odczytami makro, gdy ryzyko handlu z lepiej poinformowanym skacze, dokładnie tak, jak przewiduje intuicja Glostena-Milgroma. Rozumienie księgi zleceń nie daje przewagi samo w sobie, ale pozwala czytać koszt transakcyjny jako sensowną wielkość, a nie przypadkowy podatek: wiadomo, za co się płaci, i kiedy ta cena rośnie.

To nie jest porada inwestycyjna. To opis mechaniki mikrostruktury rynku, podany z definicjami i intuicją modeli, żeby dało się rozumieć, skąd bierze się cena, którą płaci się za każdą transakcję, zanim postawi się na niej pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
