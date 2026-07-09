---
title: "Dlaczego twój Sharpe kłamie. Deflated Sharpe Ratio i test na overfitting"
description: "Sam Sharpe ratio przemilcza dwie rzeczy: ile konfiguracji wypróbowano, zanim wypadł tak wysoko, i jak gruby jest lewy ogon rozkładu. Deflated Sharpe (Bailey i López de Prado, 2014) koryguje oba naraz. Wzory po ludzku, przykład z oryginalnej pracy: roczny Sharpe 1.59 z dwóch lat miesięcznych spada do DSR 0.9505 po uwzględnieniu 88 wypróbowanych prób."
date: 2026-07-09 13:30:00 +0200
eyebrow: "Edukacja · walidacja"
dek: "Każdy chwali się Sharpe'em, prawie nikt nie pyta, ile strategii przetestowano, zanim ten Sharpe wyszedł. Rozkładam metodę, która to karze: Deflated Sharpe i PBO. Trochę statystyki, ale po ludzku, z wzorami i przykładem z oryginalnej pracy. Po polsku pisze o tym prawie nikt."
readingTime: 8
tags: ["Deflated Sharpe", PBO, PSR, walidacja, overfitting, Sharpe, "Sharpe ratio", backtest, "López de Prado", "Harvey & Liu", "istotność statystyczna", statystyka, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Sharpe kłamie z dwóch niezależnych powodów. Pierwszy to selection bias: im więcej konfiguracji wypróbujesz, tym wyższy będzie „najlepszy" Sharpe czysto z przypadku. Drugi to nienormalność zwrotów, bo ujemny skos i grube ogony rozdmuchują niepewność samego Sharpe'a. Deflated Sharpe (Bailey i López de Prado, 2014) koryguje oba naraz.
> - Przykład wprost z pracy: roczny Sharpe 1.59, policzony z dwóch lat miesięcznych zwrotów, po uwzględnieniu 88 wypróbowanych konfiguracji spada do DSR równego 0.9505, czyli ledwo ociera się o próg 0.95. Sam fakt, że szukano wśród 88 wariantów, prawie zjada cały wynik.
> - Probabilistyczny Sharpe (PSR) zamienia punktową liczbę na prawdopodobieństwo, że prawdziwy Sharpe jest powyżej progu, i uwzględnia długość próby, skos oraz kurtozę. Przy ujemnym skosie ten sam Sharpe daje niższe PSR, bo lewy ogon powiększa niepewność estymatora.
> - Lekarstwo ma dwie części: Deflated Sharpe karze za liczbę prób i kształt ogona, a PBO (metoda CSCV, Bailey i López de Prado, 2013) szacuje, jaki odsetek zwycięzców in-sample wypada poniżej mediany out-of-sample. Po polsku o obu narzędziach pisze prawie nikt.

**Teza w jednym zdaniu:** Sharpe ratio nie jest dowodem edge'u, dopóki nie zdeflatujesz go o liczbę wypróbowanych prób i nie skorygujesz o kształt ogona, a kiedy zrobisz to uczciwie, większość „istotnych" wyników przestaje być istotna.

## Sharpe to nie dowód, tylko punkt startu

Sharpe ratio to najpopularniejsza miara jakości strategii: średni zwrot podzielony przez jego odchylenie standardowe, zwykle przeskalowany na rok. Im wyższy, tym rzekomo lepiej. Problem w tym, że sama liczba nie mówi, ile kosztowało jej wyprodukowanie ani z jakiego rozkładu pochodzi.

```
Sharpe = średnia(zwroty) / odchylenie_std(zwroty)
```

Są dwie dziury, które ta formuła przemilcza. Pierwsza: jeśli przetestowałeś sto wariantów strategii i pokazujesz najlepszy, to jego Sharpe jest zawyżony przez samo przeszukiwanie, bo maksimum ze stu losowych prób prawie zawsze wygląda nieźle. Druga: Sharpe zakłada po cichu, że zwroty są w miarę normalne, a jeśli masz ujemny skos i grube ogony (typowe dla strategii, które zbierają po trochu i czasem obrywają dużym ciosem), to niepewność samego Sharpe'a jest większa, niż sądzisz. Bailey i López de Prado zaproponowali w 2013 i 2014 roku dwa narzędzia, które łatają dokładnie te dwie dziury: Deflated Sharpe Ratio oraz Probability of Backtest Overfitting. W polskim internecie praktycznie nikt o tym nie pisze, choć to jeden z najważniejszych filtrów anty-overfitting ostatniej dekady.

## Pierwszy powód: im więcej prób, tym wyższy Sharpe z przypadku

Intuicja jest prosta i nieprzyjemna. Rzuć monetą wystarczająco wiele razy, a znajdziesz serię, która wygląda jak system. Jeśli przepuścisz przez grid 88 konfiguracji wskaźnika, to nawet gdyby żadna nie miała realnego edge'u, najlepsza z nich wyjdzie z dodatnim Sharpe'em tylko dlatego, że wybierasz maksimum z 88 losowych wyników. To nie jest edge, to jest statystyka porządkowa.

López de Prado formalizuje tę poprzeczkę wzorem na oczekiwaną wartość maksymalnego Sharpe'a pod hipotezą zerową, czyli przy założeniu, że żadna próba nie ma prawdziwego edge'u.

```
E[max SR] = √(V[SRₙ]) · [ (1−γ) · Z⁻¹(1 − 1/N) + γ · Z⁻¹(1 − 1/(N·e)) ]

V[SRₙ] = wariancja Sharpe'ów między próbami (dyspersja gridu)
N      = liczba wypróbowanych konfiguracji
γ      = stała Eulera-Mascheroniego ≈ 0.5772
Z⁻¹    = kwantyl rozkładu normalnego (odwrotna dystrybuanta)
e      = liczba Eulera ≈ 2.718
```

Czyta się to tak: im więcej prób N, tym wyżej wędruje poprzeczka, a im bardziej rozstrzelone są Sharpe'y w gridzie (większe V[SRₙ]), tym mocniej rośnie oczekiwane maksimum. Ta poprzeczka, oznaczana dalej jako SR0, to poziom, który musisz przebić, żeby w ogóle mówić o czymkolwiek ponad szum. Ćwiczenie z monetą, tylko z liczbami.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Poprzeczka rośnie z liczbą wypróbowanych prób</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">wymagany Sharpe, by przebić szum</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">liczba wypróbowanych prób N</text><text x="98" y="250" font-size="10" fill="currentColor" opacity="0.6">mało prób</text><text x="598" y="250" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end">dużo prób</text><text x="104" y="224" font-size="10" fill="currentColor" opacity="0.6">niższa poprzeczka</text><path d="M92 210 C165 132 320 96 600 84" fill="none" stroke="#0b66c3" stroke-width="2"/><circle cx="92" cy="210" r="3.4" fill="#0b66c3"/><circle cx="146" cy="168" r="3.4" fill="#0b66c3"/><circle cx="222" cy="135" r="3.4" fill="#0b66c3"/><circle cx="321" cy="111" r="3.4" fill="#0b66c3"/><circle cx="447" cy="94" r="3.4" fill="#0b66c3"/><circle cx="600" cy="84" r="4.4" fill="#0b66c3"/><text x="596" y="74" font-size="10.5" fill="#0b66c3" text-anchor="end">wyższa poprzeczka</text></svg>
<figcaption>Im więcej wypróbowanych konfiguracji N, tym wyżej wędruje poprzeczka SR0, czyli oczekiwany maksymalny Sharpe z samego przeszukiwania. Krzywa jest wklęsła, więc rośnie coraz wolniej: każda kolejna próba podnosi wymóg mniej niż poprzednia. Im więcej prób, tym wyższą poprzeczkę musi przebić strategia, żeby jej Sharpe znaczył coś ponad szum.</figcaption>
</figure>

## Drugi powód: skos i grube ogony zawyżają pewność

Druga poprawka dotyczy kształtu rozkładu. Probabilistyczny Sharpe, czyli PSR, nie zwraca punktowej wartości, tylko prawdopodobieństwo, że prawdziwy Sharpe jest powyżej wybranego progu, biorąc pod uwagę długość próby oraz skos i kurtozę.

```
PSR(SR*) = Z[ (SR − SR*) · √(T−1) / √(1 − γ₃·SR + (γ₄−1)/4 · SR²) ]

Z    = dystrybuanta rozkładu normalnego
SR   = obserwowany Sharpe,  SR* = próg odniesienia
T    = liczba obserwacji (liczba tradów lub okresów)
γ₃   = skos,  γ₄ = kurtoza surowa (dla rozkładu normalnego = 3)
```

Kluczowy jest mianownik. Przy zwrotach normalnych (γ₃ = 0, γ₄ = 3) redukuje się on prawie do jedynki i PSR zależy głównie od tego, jak SR odstaje od progu oraz ile masz obserwacji. Ale gdy skos jest ujemny, składnik −γ₃·SR robi się dodatni i powiększa mianownik, czyli powiększa wariancję estymatora Sharpe'a. Po ludzku: strategia, która regularnie zgarnia drobne, a od czasu do czasu dostaje dużą stratą, ma Sharpe'a obarczonego większą niepewnością niż taka sama liczba przy zwrotach symetrycznych. PSR to widzi, zwykły Sharpe nie.

## Deflated Sharpe: obie poprawki w jednej liczbie

Deflated Sharpe składa oba mechanizmy w jedną liczbę. To po prostu PSR policzony nie względem zera, tylko względem poprzeczki SR0 wyznaczonej z liczby prób.

```
SR0 = E[max SR]     poprzeczka z samego przeszukiwania N prób
DSR = PSR(SR0)      PSR liczony względem tej poprzeczki, nie względem zera
```

Zobaczmy to na przykładzie wprost z pracy Baileya i López de Prado. Roczny Sharpe 1.59, policzony z dwóch lat miesięcznych zwrotów, przy założeniu normalności rozkładu, wygląda na solidny wynik. Ale kiedy uwzględnisz, że powstał w wyniku przeszukania 88 konfiguracji, poprzeczka E[max SR] podnosi się do 0.0973 w jednostkach per okres, a deflowany Sharpe spada do 0.9505. To ledwo powyżej umownego progu 0.95, przy którym dopiero mówimy o istotności. Sam fakt, że szukano wśród 88 wariantów, zjadł prawie całą przewagę pozornie mocnego Sharpe'a. To jest cała lekcja tego przykładu: dwa lata ładnych miesięcznych zwrotów po zderzeniu z liczbą prób zostają na granicy szumu.

## PSR na własnym torze: ile obserwacji naprawdę potrzeba

Metoda najłatwiej sprzedaje się na cudzych danych, a najwięcej uczy, kiedy przyłożysz ją do własnego dziennika. Schemat jest prosty: policz PSR wobec progu zerowego (SR* = 0), żeby sprawdzić, czy masz istotnie dodatni edge, a nie tylko dodatnią średnią z małej próby.

Często wychodzi, że Sharpe jest dodatni, a PSR i tak nie dobija do 0.95. Luka bierze się z ogona, nie z kierunku. Bailey i López de Prado podają na to gotowy wzór na minimalną długość toru, czyli liczbę obserwacji, przy której PSR przekroczy żądaną pewność.

```
MinTRL = 1 + [ 1 − γ₃·SR + (γ₄−1)/4 · SR² ] · ( Z_α / (SR − SR*) )²

Z_α = kwantyl normalny dla żądanej pewności (dla 0.95 to około 1.645)
SR  = obserwowany Sharpe na obserwację,  SR* = próg (zwykle 0)
γ₃  = skos,  γ₄ = kurtoza surowa (dla rozkładu normalnego = 3)
```

Wzór czyta się jak rachunek sumienia. Im mniejsza przewaga SR nad progiem, tym gwałtowniej rośnie wymóg, bo (SR − SR*) siedzi w mianowniku podniesionym do kwadratu. Im bardziej ujemny skos, tym większy nawias w liczniku, bo składnik −γ₃·SR robi się dodatni. Im grubszy ogon (wyższa kurtoza), tym znowu więcej obserwacji. Strategia, która zbiera po trochu i raz na jakiś czas obrywa dużym ciosem, potrafi wymagać kilkuset tradów, żeby jej Sharpe stał się statystycznie wiarygodny, nawet jeśli goła krzywa kapitału wygląda ładnie.

Najlepiej widać to na jednym eksperymencie, który każdy może zrobić na swoich danych: policz PSR, potem usuń pojedynczy najgorszy trade i policz PSR jeszcze raz. Przy ujemnym skosie ta jedna obserwacja potrafi podnieść PSR o kilka punktów procentowych. To dowód wprost, że wrogiem nie jest trafność, tylko lewy ogon. Stąd dwie drogi do domknięcia dowodu: albo uzbierasz tyle obserwacji, ile każe MinTRL, albo założysz twardy stop loss, który przytnie ogon, zmniejszy skos i kurtozę, a przez to obniży sam wymóg.

## PBO: prawdopodobieństwo, że najlepszy backtest to overfit

DSR ma jedno założenie: że próby są niezależne. Gdy konfiguracje w gridzie są silnie skorelowane, efektywne N jest mniejsze niż nominalne i trzeba je szacować. Dlatego drugim, komplementarnym narzędziem jest PBO, czyli prawdopodobieństwo overfittingu, liczone metodą CSCV (Combinatorially Symmetric Cross-Validation). Pomysł: tniesz macierz zwrotów na wiele kombinacji części in-sample i out-of-sample, w każdej wybierasz konfigurację najlepszą in-sample i sprawdzasz, gdzie ląduje ona out-of-sample. PBO to odsetek podziałów, w których twój in-sample zwycięzca wypada poniżej mediany na danych, których nie widział. Wysokie PBO oznacza, że twój „najlepszy" wynik to w dużej mierze dopasowanie do szumu.

Narzędzie łatwo sprawdzić na dwóch skrajnościach. Na czystym szumie PBO siada blisko 0.5, czyli in-sample zwycięzca wypada out-of-sample nie lepiej niż rzut monetą, dokładnie tak, jak powinno być przy braku jakiegokolwiek edge'u. Na danych ze sztucznie wszczepioną prawdziwą przewagą PBO spada w okolice zera. Ta separacja pokazuje, że metoda faktycznie odróżnia strukturę od przypadku, a nie tylko produkuje ładnie wyglądającą liczbę. Dlatego DSR i PBO warto trzymać jako stały wiersz protokołu walidacji, uruchamiany po każdym przeszukiwaniu gridu.

## Co z tego wynika przy stole

Praktyczny wniosek jest niewygodny, ale prosty. Jeśli chwalisz się Sharpe'em bez podania, ile strategii przetestowałeś, żeby go znaleźć, to podajesz liczbę bez jednostki. Ta sama wartość 1.59 znaczy co innego po jednej próbie, a co innego po 88. Kolejny stopień tej samej dyscypliny to haircut Harveya i Liu (2015), którzy dla nowych „odkryć" podnoszą wymaganą istotność do statystyki t większej niż 3, właśnie dlatego, że literatura testuje tysiące strategii i mnożą się fałszywe odkrycia.

Zamienia to też sposób mówienia o wynikach. Zamiast „mam działającą strategię" uczciwsza forma brzmi „PSR wynosi tyle a tyle, przy tylu próbach i takim skosie". To nie musi być werdykt sukcesu albo porażki. Najczęściej jest to po prostu uczciwy stan wiedzy: poszlaka mocna, dowodu brak, a warunek, który go domknie, da się podać liczbą (tyle a tyle obserwacji albo ucięty ogon). Taki komunikat da się później rozliczyć, podkolorowanej krzywej kapitału rozliczyć się nie da.

To nie jest porada inwestycyjna. To metoda walidacji, pokazana z wzorami i przykładem z literatury, żebyś umiał odróżnić realny edge od artefaktu przeszukiwania, zanim postawisz na nim pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
