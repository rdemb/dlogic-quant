---
title: "Teoria aukcji. Vickrey, Milgrom i klątwa zwycięzcy"
description: "Vickrey (1961) pokazał, że w aukcji drugiej ceny opłaca się licytować dokładnie własną wycenę, a cztery klasyczne formaty dają sprzedawcy ten sam oczekiwany przychód. Myerson (1981) uogólnił ten wynik na całe klasy mechanizmów. Capen, Clapp i Campbell (1971) odkryli na przetargach naftowych klątwę zwycięzcy: wygrywa ten, kto najbardziej przeszacował. Nobel 2020 dla Milgroma i Wilsona domyka historię, która dotyczy aukcji skarbowych, IPO, fixingu na giełdzie i reklam w internecie."
date: 2026-07-05 12:00:00 +0200
eyebrow: "Edukacja · rynki"
dek: "Ta sama licencja 3G poszła w 2000 roku po około 650 euro od mieszkańca w Wielkiej Brytanii i po około 20 euro w Szwajcarii, bo różniły się reguły licytacji. Cztery klasyczne formaty aukcji, mechanizm Vickreya, w którym kłamstwo przestaje się opłacać, twierdzenie o równoważności przychodów i klątwa zwycięzcy: mapa teorii, za którą przyznano Nobla i w którą inwestor gra częściej, niż mu się wydaje."
readingTime: 8
tags: [aukcje, "teoria aukcji", Vickrey, Milgrom, Wilson, Myerson, Klemperer, "klątwa zwycięzcy", "winner's curse", "równoważność przychodów", "wartość wspólna", "aukcje skarbowe", IPO, fixing, "Nobel 2020", edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Cztery klasyczne formaty aukcji to angielska (cena rośnie, wygrywa ostatni przy stole), holenderska (cena spada, wygrywa pierwszy, kto się zgłosi), pierwszej ceny w zamkniętej kopercie (zwycięzca płaci własną ofertę) i drugiej ceny, czyli Vickreya (zwycięzca płaci drugą najwyższą ofertę). Holenderska jest strategicznie tożsama z pierwszą ceną, a angielska, przy wycenach prywatnych, prowadzi do tego samego wyniku co Vickreya.
> - W aukcji Vickreya (1961) opłaca się licytować dokładnie tyle, ile przedmiot jest dla ciebie wart: prawdomówność jest strategią dominującą, niezależnie od tego, co robią rywale. Przy standardowych założeniach wszystkie cztery formaty dają sprzedawcy ten sam oczekiwany przychód, co Myerson (1981) uogólnił na całe klasy mechanizmów.
> - Gdy licytowana jest wartość wspólna (pole naftowe jest warte dla wszystkich tyle samo, tylko nikt nie wie ile), wygrywa ten, kto najbardziej przeszacował. Klątwę zwycięzcy opisali w 1971 roku Capen, Clapp i Campbell, trzej inżynierowie naftowi, po analizie przetargów na koncesje. Racjonalna odpowiedź: licytuj poniżej własnego oszacowania, tym niżej, im więcej masz konkurentów.
> - Nagrodę Nobla 2020 Milgrom i Wilson dostali „za ulepszenia teorii aukcji i wynalezienie nowych formatów aukcyjnych": ich aukcja SMRA sprzedaje częstotliwości radiowe od 1994 roku, a według materiałów noblowskich same amerykańskie aukcje widma przyniosły przez dwie dekady ponad 120 mld dolarów. Inwestor gra w aukcje częściej, niż myśli: przetargi obligacji, IPO, fixing otwarcia i zamknięcia, reklamy w internecie.

**Teza w jednym zdaniu:** O cenie w licytacji decyduje nie tylko przedmiot, ale sam format gry, a tam, gdzie licytowana jest wspólna, nieznana wartość, wygrana bywa złą wiadomością, bo przeciw wielu konkurentom wygrywa najbardziej optymistyczne oszacowanie, więc racjonalny gracz licytuje poniżej tego, co sam wyliczył, tym ostrożniej, im większy tłok.

## Dwie aukcje, ta sama technologia i wynik różny o rząd wielkości

Wiosną 2000 roku Wielka Brytania sprzedała na aukcji pięć licencji na telefonię 3G za około 22,5 mld funtów, blisko 2,5 procent ówczesnego produktu narodowego, czyli mniej więcej 650 euro od mieszkańca. Do licytacji stanęło trzynastu chętnych, a jedną licencję z góry zarezerwowano dla nowego gracza, żeby zasiedziali operatorzy nie mogli spokojnie podzielić rynku między siebie. Pod koniec tego samego roku identyczną technologię licytowała Szwajcaria: reguły pozwoliły kandydatom połączyć się w konsorcja tuż przed startem, chętnych zostało dokładnie tylu, ile licencji, i częstotliwości poszły po cenie minimalnej, około 20 euro od mieszkańca. Paul Klemperer, współprojektant brytyjskiej aukcji, zestawia oba wyniki w książce „Auctions: Theory and Practice" (Princeton University Press, 2004; darmowy draft wisi na jego stronie w Nuffield College w Oksfordzie) z prostą diagnozą: trzydziestokrotnej różnicy nie zrobiła technologia ani koniunktura, tylko reguły gry.

Teoria aukcji to dział teorii gier, który takie historie wyjaśnia: bada, jak format licytacji kształtuje strategie graczy, a przez strategie ceny. Na dobre zaczęła się od jednego artykułu: William Vickrey, „Counterspeculation, Auctions, and Competitive Sealed Tenders" (Journal of Finance 16(1), 1961). Vickrey dostał za tę linię badań Nobla w 1996 roku i zmarł trzy dni po ogłoszeniu werdyktu, w drodze na konferencję naukową. Jego artykuł zawiera dwa pomysły, które do dziś niosą całą konstrukcję: aukcję drugiej ceny i twierdzenie o równoważności przychodów.

## Cztery klasyczne formaty i dwie ukryte pary

Klasyczna czwórka wygląda tak. Aukcja angielska: cena rośnie, licytujący kolejno odpadają, wygrywa ostatni przy stole i płaci mniej więcej poziom, przy którym odpadł przedostatni. Aukcja holenderska: zegar startuje z ceny zaporowo wysokiej i schodzi w dół, wygrywa pierwszy, kto krzyknie „biorę", i płaci cenę z zegara; tak od ponad wieku sprzedaje się kwiaty w Aalsmeer, bo format jest błyskawiczny. Aukcja pierwszej ceny: każdy składa jedną ofertę w zamkniętej kopercie, wygrywa najwyższa i płaci dokładnie to, co napisała. Aukcja drugiej ceny, czyli Vickreya: koperty jak wyżej, wygrywa najwyższa oferta, ale rachunek wystawia się według drugiej najwyższej.

Na pierwszy rzut oka to cztery różne gry. Naprawdę są dwie pary bliźniaków:

```
format otwarty                     bliźniak w zamkniętej kopercie
holenderska (cena spada)      →    pierwsza cena
angielska (cena rośnie)       →    druga cena (Vickreya)
```

Holenderska i pierwsza cena to strategicznie ta sama gra: w obu wybierasz jedną liczbę, niczego nie dowiadując się po drodze o rywalach, i jeśli twoja liczba okaże się najodważniejsza, płacisz właśnie ją. Angielska i Vickreya schodzą się przy wycenach prywatnych: w aukcji angielskiej opłaca się stać przy stole dokładnie dopóty, dopóki cena nie przebije twojej wyceny, więc zwycięzca płaci poziom wyjścia drugiego w kolejności, czyli drugą najwyższą wycenę. Podział na cztery formaty ma jednak sens, bo pary rozjeżdżają się z powrotem, gdy w grę wchodzi wspólna wartość i informacja płynąca z cudzych zachowań. O tym za chwilę.

Dla licytującego różnica między rodzinami jest fundamentalna. W rodzinie pierwszej ceny oferta równa własnej wycenie gwarantuje zysk zero, więc trzeba licytować poniżej wyceny i balansować: wyższa oferta to częstsze wygrane, niższa to grubszy zysk z każdej wygranej. Optimum zależy od tego, ilu jest rywali i jak grają, czyli trzeba ich prognozować. W rodzinie drugiej ceny prognozowanie rywali jest zbędne, i to jest właśnie odkrycie Vickreya.

## Aukcja Vickreya: mechanizm, w którym opłaca się mówić prawdę

Sztuczka polega na rozdzieleniu dwóch ról oferty. W aukcji pierwszej ceny twoja koperta decyduje jednocześnie o tym, czy wygrasz, i o tym, ile zapłacisz, więc masz motyw, żeby kłamać w dół. U Vickreya koperta decyduje wyłącznie o tym, czy wygrasz; wysokość rachunku ustala druga najwyższa oferta, na którą nie masz wpływu. Sprawdź, co daje odejście od prawdy. Zawyżysz ofertę ponad własną wycenę: dokładasz sobie wyłącznie te wygrane, w których rachunek przekracza wartość przedmiotu, czyli dopłacasz do interesu. Zaniżysz: rachunku i tak nie obniżysz, za to wypadasz z licytacji, które były dla ciebie zyskowne. Licytowanie dokładnie własnej wyceny jest więc strategią dominującą: najlepszą niezależnie od tego, co zrobi reszta stołu. Prawdomówność przestaje być cnotą, a staje się chłodną kalkulacją.

To nie jest ciekawostka z tablicy. Licytacja przez pełnomocnika w serwisie eBay działa na pokrewnej zasadzie: podajesz swoje maksimum, system licytuje za ciebie, a zwycięzca płaci drugą najwyższą ofertę powiększoną o minimalne postąpienie. Skrót VCG, opisujący mechanizmy używane w aukcjach reklamy internetowej, rozwija się w Vickrey, Clarke, Groves: pomysł z 1961 roku dorobił się uogólnień na sprzedaż wielu przedmiotów naraz.

## Równoważność przychodów: różne reguły, średnio ten sam utarg

Sprzedawca zapyta: skoro formaty tak różnie ustawiają zachowanie, to który daje najwyższy przychód? Pierwsza odpowiedź Vickreya jest zaskakująca: żaden. Przy standardowych założeniach (gracze neutralni wobec ryzyka, wyceny prywatne, niezależne i losowane z tego samego rozkładu) wszystkie cztery klasyczne formaty dają sprzedawcy identyczny oczekiwany przychód. Intuicja: w aukcji drugiej ceny licytujesz prawdę i płacisz drugą najwyższą wycenę; w aukcji pierwszej ceny wszyscy ścinają oferty mniej więcej do poziomu, jakiego spodziewają się po drugiej najwyższej wycenie pod warunkiem własnej wygranej. Ścięta oferta i rachunek z drugiej koperty uśredniają się do tego samego.

Roger Myerson („Optimal Auction Design", Mathematics of Operations Research 6(1), 1981) podniósł tę obserwację do rangi twierdzenia o całych klasach mechanizmów: jeśli dwa mechanizmy sprzedaży tak samo przydzielają przedmiot (na przykład zawsze najwyższej wycenie) i tak samo traktują najsłabszego uczestnika, dają ten sam oczekiwany przychód niezależnie od całej reszty konstrukcji. Przy okazji wyznaczył aukcję optymalną: dla symetrycznych kupujących to zwykła aukcja z dobrze dobraną ceną minimalną, ustawioną powyżej wartości przedmiotu dla sprzedawcy. Optymalny sprzedawca czasem woli nie sprzedać wcale, niż sprzedać tanio, i sama ta groźba podnosi utarg. Myerson dostał w 2007 roku Nobla za fundamenty projektowania mechanizmów.

Równoważność przychodów bywa odczytywana jako „format nie ma znaczenia", co jest odczytaniem na opak. Twierdzenie mówi, że format nie ma znaczenia dokładnie wtedy, gdy trzymają założenia, i przez to wskazuje palcem, gdzie szukać różnic: awersja do ryzyka (gracze bojący się przegranej licytują w pierwszej cenie agresywniej, więc ten format daje wtedy więcej), skorelowane oszacowania, asymetrie między graczami, zmowa i bariery wejścia. Klemperer po doświadczeniach z aukcjami 3G twierdzi wręcz, że w praktyce projektowania aukcji subtelności teorii ustępują dwóm przyziemnym pytaniom: czy reguły ściągną nowych graczy i czy utrudnią zmowę.

## Obraz na ścianę kontra pole naftowe

Do klątwy zwycięzcy potrzebne jest jeszcze jedno rozróżnienie. Wartość prywatna: licytujesz obraz na własną ścianę, wart jest dla ciebie tyle, ile przyjemności z patrzenia, a opinia rywali nie zmienia tej liczby w niczym. Wartość wspólna: licytujesz pole naftowe, w którym siedzi jedna, obiektywna ilość ropy, taka sama niezależnie od tego, kto wygra; różnią się tylko oszacowania geologów. Większość realnych aukcji miesza oba składniki, ale aktywa finansowe leżą blisko bieguna wspólnego: przyszłe przepływy z obligacji czy akcji są jedne dla wszystkich posiadaczy.

Przy wartościach prywatnych cudze oferty nie mówią ci nic o twojej wycenie. Przy wspólnej mówią bardzo dużo: skoro rywal licytuje nisko, jego geolodzy zobaczyli coś, czego twoi nie zobaczyli. I tu zaczyna się kłopot.

## Klątwa zwycięzcy: trzej inżynierowie liczą, dlaczego wygrana boli

Ed Capen, Robert Clapp i William Campbell byli inżynierami koncernu naftowego Atlantic Richfield, nie ekonomistami. W artykule „Competitive Bidding in High-Risk Situations" (Journal of Petroleum Technology 23(6), 1971) zapisali obserwację, która od lat gryzła branżę: na przetargach koncesji w Zatoce Meksykańskiej ropy było pod dostatkiem, a mimo to zwycięzcy licytacji rok po roku zarabiali mniej, niż planowali. Oferty różnych firm na tę samą działkę, składane przez zawodowców z badaniami sejsmicznymi w ręku, potrafiły różnić się kilkukrotnie, a zdarzało się, że o rząd wielkości. Na słynnej aukcji koncesji na North Slope na Alasce we wrześniu 1969 roku zwycięskie oferty opiewały łącznie na około 900 mln dolarów.

Mechanizm, który za tym stoi, jest czysto statystyczny i dlatego nieubłagany:

```
każda firma szacuje wartość działki bez systematycznego błędu
→ oferty podążają za oszacowaniami
→ wygrywa najwyższa oferta, czyli najwyższe oszacowanie
→ zwycięzca to z konstrukcji największy optymista
→ średnio: zwycięzca przepłaca, choć nikt nie mylił się „średnio"
```

Pojedyncze oszacowanie może być nieobciążone, ale aukcja nie wybiera losowego oszacowania, tylko maksimum z wielu. A maksimum z nieobciążonych oszacowań jest obciążone w górę, tym mocniej, im więcej firm szacuje i im większa niepewność. Stąd rada Capena, Clappa i Campbella, która do dziś brzmi jak herezja: licytuj poniżej własnego oszacowania, i to tym niżej, im więcej masz konkurentów. Zdrowy rozsądek podpowiada, że duża konkurencja wymusza agresję; rachunek mówi odwrotnie, bo wygrana przeciw pięćdziesięciu rywalom znaczy, że twoje oszacowanie było najbardziej optymistyczne z pięćdziesięciu jeden, a to jest zła wiadomość o oszacowaniu, nie dobra o działce. Autorzy ujęli to obrazowo: kto wygrywa z dwoma czy trzema rywalami, może się cieszyć; kto wygrał z pięćdziesięcioma, powinien się martwić. I dopisali puentę: kto uparcie licytuje tyle, ile jego zdaniem działka jest warta, w długim okresie zostanie oskubany.

W ścisłej teorii klątwa zwycięzcy nie jest błędem rynku, tylko błędem gracza: w pełni racjonalny licytujący wycenia przedmiot warunkowo, „ile to jest warte, jeżeli okaże się, że wygrałem", i odpowiednio ścina ofertę, więc w równowadze nikt nie przepłaca. Sęk w tym, że dane polowe i dekady eksperymentów pokazują to samo, co Zatoka Meksykańska: realni gracze ścinają za słabo. Klątwa jest pojęciem z pogranicza teorii i psychologii, i właśnie dlatego jest taka praktyczna.

<figure>
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rozkład prywatnych wycen uczestników aukcji wokół wartości prawdziwej. Zwycięzca to najwyższa wycena, leży na prawo od prawdy i przepłaca." style="width:100%;height:auto;max-width:720px;display:block;margin:0 auto;font-family:-apple-system,Segoe UI,Roboto,sans-serif">
<g stroke="currentColor" stroke-width="1" opacity="0.18">
<line x1="210" y1="115" x2="210" y2="320"/>
<line x1="295" y1="115" x2="295" y2="320"/>
<line x1="465" y1="115" x2="465" y2="320"/>
<line x1="550" y1="115" x2="550" y2="320"/>
</g>
<line x1="90" y1="320" x2="660" y2="320" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
<polygon points="660,320 650,316 650,324" fill="currentColor" opacity="0.4"/>
<text x="628" y="338" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.55">wycena</text>
<path d="M125,317.7 L146.2,315.2 L167.5,310.8 L188.8,303.3 L210,291.6 L231.2,274.6 L252.5,251.8 L273.8,223.9 L295,192.6 L316.2,161.5 L337.5,134.7 L358.8,116.5 L380,110 L401.2,116.5 L422.5,134.7 L443.8,161.5 L465,192.6 L486.2,223.9 L507.5,251.8 L528.8,274.6 L550,291.6 L571.2,303.3 L592.5,310.8 L613.8,315.2 L635,317.7 L635,320 L125,320 Z" fill="#0b66c3" opacity="0.12"/>
<path d="M125,317.7 L146.2,315.2 L167.5,310.8 L188.8,303.3 L210,291.6 L231.2,274.6 L252.5,251.8 L273.8,223.9 L295,192.6 L316.2,161.5 L337.5,134.7 L358.8,116.5 L380,110 L401.2,116.5 L422.5,134.7 L443.8,161.5 L465,192.6 L486.2,223.9 L507.5,251.8 L528.8,274.6 L550,291.6 L571.2,303.3 L592.5,310.8 L613.8,315.2 L635,317.7" fill="none" stroke="#0b66c3" stroke-width="2" opacity="0.75" stroke-linejoin="round"/>
<g fill="#0b66c3" opacity="0.8">
<circle cx="285" cy="306" r="5"/>
<circle cx="312" cy="300" r="5"/>
<circle cx="330" cy="308" r="5"/>
<circle cx="345" cy="298" r="5"/>
<circle cx="356" cy="304" r="5"/>
<circle cx="365" cy="300" r="5"/>
<circle cx="373" cy="307" r="5"/>
<circle cx="380" cy="301" r="5"/>
<circle cx="388" cy="305" r="5"/>
<circle cx="396" cy="299" r="5"/>
<circle cx="405" cy="306" r="5"/>
<circle cx="416" cy="300" r="5"/>
<circle cx="430" cy="307" r="5"/>
<circle cx="451" cy="302" r="5"/>
<circle cx="485" cy="303" r="5"/>
</g>
<line x1="380" y1="92" x2="380" y2="358" stroke="currentColor" stroke-width="1.5" opacity="0.6" stroke-dasharray="5,4"/>
<text x="380" y="64" text-anchor="middle" font-size="15" fill="currentColor" opacity="0.85">wartość prawdziwa</text>
<text x="380" y="82" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.6">= średnia wycen</text>
<circle cx="545" cy="302" r="12" fill="#e5484d" opacity="0.15"/>
<circle cx="545" cy="302" r="7" fill="#e5484d"/>
<line x1="545" y1="278" x2="545" y2="295" stroke="currentColor" stroke-width="1" opacity="0.4"/>
<text x="545" y="255" text-anchor="middle" font-size="15" fill="currentColor" opacity="0.85">zwycięzca</text>
<text x="545" y="272" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.6">najwyższa wycena</text>
<line x1="380" y1="352" x2="545" y2="352" stroke="currentColor" stroke-width="1.5" opacity="0.75"/>
<polygon points="545,352 535,347 535,357" fill="currentColor" opacity="0.75"/>
<line x1="545" y1="311" x2="545" y2="350" stroke="#e5484d" stroke-width="1.5" opacity="0.5" stroke-dasharray="4,3"/>
<text x="462" y="372" text-anchor="middle" font-size="13" fill="currentColor" opacity="0.85">przepłata zwycięzcy</text>
<circle cx="98" cy="54" r="5" fill="#0b66c3" opacity="0.8"/>
<text x="112" y="58" font-size="13" fill="currentColor" opacity="0.75">wyceny uczestników</text>
<circle cx="98" cy="76" r="5" fill="#e5484d"/>
<text x="112" y="80" font-size="13" fill="currentColor" opacity="0.75">zwycięzca (maksimum)</text>
</svg>
<figcaption>Prywatne wyceny uczestników (niebieskie) rozkładają się wokół wartości prawdziwej i średnio jej nie zawyżają. Aukcja wybiera jednak maksimum, więc zwycięzca (czerwony) prawie zawsze leży na prawo od prawdy i przepłaca, a im więcej licytujących, tym głębsze to obciążenie.</figcaption>
</figure>

## Nobel 2020: od twierdzeń do projektowania rynków

Teorię licytacji przy wartości wspólnej ujął w równowagi Robert Wilson w latach 60. i 70.: pokazał, jak racjonalni gracze powinni ścinać oferty, żeby klątwa ich nie zjadła. Jego doktorant Paul Milgrom domknął obraz, łącząc wartości prywatne i wspólne w jednym modelu, z wnioskiem znanym jako zasada powiązania: formaty otwarte, które w trakcie licytacji ujawniają zachowanie rywali, zmniejszają niepewność i łagodzą klątwę, więc gracze licytują śmielej, a sprzedawca przeciętnie zarabia więcej niż przy zamkniętych kopertach. To jeden z powodów, dla których drogie i niepewne aktywa świat woli sprzedawać w formatach rosnących. Wykład tej teorii Milgrom zebrał w książce „Putting Auction Theory to Work" (Cambridge University Press, 2004).

W 2020 roku Milgrom i Wilson dostali Nobla „za ulepszenia teorii aukcji i wynalezienie nowych formatów aukcyjnych". Nagrodzono nie tylko twierdzenia, ale i inżynierię. Gdy w 1994 roku amerykański regulator FCC pierwszy raz sprzedawał częstotliwości radiowe na aukcji, problemem były zależności między licencjami: wartość pasma w jednym regionie zależy od tego, jakie inne pasma się posiada. Milgrom i Wilson zaprojektowali aukcję SMRA, w której wszystkie licencje licytowane są równocześnie, w otwartych rundach, z regułami aktywności, które nie pozwalają czaić się do końca. Format skopiowano na całym świecie, a według materiałów noblowskich same amerykańskie aukcje widma przyniosły przez dwie dekady ponad 120 mld dolarów. Wilson ma przy okazji nietypowy rekord promotora: wypromował doktoraty trzech późniejszych noblistów. Wieść o nagrodzie musiał zresztą Milgromowi przekazać osobiście, dzwoniąc w środku nocy do drzwi sąsiada, bo świeżo upieczony laureat nie odbierał telefonów ze Sztokholmu; nagranie z wideodomofonu obiegło potem świat. Brytyjskie 22,5 mld funtów i szwajcarskie 20 euro od mieszkańca z początku tekstu to dwie strony tej samej monety: dobrze i źle zastosowanej teorii.

## Gdzie inwestor licytuje, nawet jeśli o tym nie wie

Aukcje skarbowe. Rządy sprzedają dług w dwóch rodzinach formatów: po cenach ofert (każdy zwycięzca płaci to, co zaoferował, logika pierwszej ceny, ze ścinaniem ofert i ryzykiem klątwy) albo po jednolitej cenie (wszyscy zwycięzcy płacą cenę odcięcia, logika rodziny Vickreya). Amerykański Departament Skarbu po latach eksperymentów przeszedł w 1998 roku w całości na jednolitą cenę, między innymi po to, żeby złagodzić klątwę zwycięzcy i ośmielić szerszy krąg uczestników. Spór o to, który format daje państwu tańsze finansowanie, ciągnie się w literaturze do dziś, dokładnie wzdłuż linii wytyczonych przez równoważność przychodów i jej pęknięcia.

Fixing na giełdzie. Otwarcie i zamknięcie sesji na większości giełd, w tym na GPW, to aukcje zbiorcze: zlecenia zbierają się w arkuszu, a system wyznacza jedną cenę równowagi, która maksymalizuje obrót. Na zamknięciu koncentrują się przepływy funduszy indeksowych, więc bywa to najpłynniejszy moment dnia. Kto składa zlecenia na fixing, gra w aukcję jednolitej ceny, z innymi regułami niż w notowaniach ciągłych.

IPO. Klasyczna budowa księgi popytu formalną aukcją nie jest, ale bywały debiuty aukcyjne z prawdziwego zdarzenia: Google w 2004 roku sprzedał akcje w zmodyfikowanej aukcji holenderskiej, z jednolitą ceną wyznaczoną z ofert inwestorów. Klątwa zwycięzcy ma w IPO swoją miniaturę po stronie przydziałów: pełny przydział akcji najłatwiej dostać w emisjach, na które popyt był słaby, a w gorących redukcje są największe, więc portfel „wygranych" przydziałów sam z siebie przechyla się ku słabszym debiutom.

Reklamy w internecie. Każde załadowanie strony z reklamą to rozstrzygana w milisekundach aukcja o uwagę użytkownika. Branża przez lata pracowała na wariantach drugiej ceny (GSP i VCG, gdzie V to Vickrey), a po 2019 roku duża część rynku przeszła na pierwszą cenę, co natychmiast przywróciło ścinanie ofert i całą maszynerię szacowania rywali. Te formaty mielą ogromne pieniądze dokładnie według reguł opisanych w 1961 roku.

## Co z tego wynika w praktyce

Format determinuje zachowanie. Przed każdą licytacją, od przetargu po zlecenie na fixing, pierwsze pytanie brzmi: co płacę, jeśli wygram, swoją cenę czy cenę rywala? W rodzinie pierwszej ceny licytuje się poniżej wyceny i prognozuje konkurencję; w rodzinie drugiej ceny, przy wartości prywatnej, mówi się prawdę i śpi spokojnie.

Drugie pytanie: czyja jest wartość. Prywatna (ile to jest warte dla mnie) pozwala licytować własny komfort. Wspólna (ile to jest warte obiektywnie) oznacza, że twoje oszacowanie jest jednym losowaniem z rozkładu, a wygrana selekcjonuje losowanie najwyższe. Aktywa finansowe niemal zawsze leżą po stronie wspólnej.

Im więcej konkurentów, tym ostrożniej. To najbardziej antyintuicyjna lekcja Capena, Clappa i Campbella: przy wspólnej wartości rosnący tłok każe ścinać ofertę głębiej, nie licytować odważniej, bo obciążenie maksimum z oszacowań rośnie z liczbą szacujących.

Wygrana jest informacją. Kto dostał pełny przydział gorącego IPO, kupił spółkę po wygranej wojnie przetargowej albo został natychmiast wypełniony na zleceniu z limitem, powinien odruchowo zapytać: dlaczego wszyscy pozostali chcieli mniej? Czasem odpowiedź jest niewinna. Ale mechanizm selekcji najbardziej optymistycznego oszacowania działa wszędzie tam, gdzie „wygrywa się" wycenę przeciw wielu konkurentom, i nigdy nie wysyła zawiadomień.

A kto sam sprzedaje, od mieszkania po firmę, powinien pamiętać o drugiej stronie lustra: cena minimalna (Myerson), jawność i tempo licytacji (Milgrom), wejście nowych graczy i odporność na zmowę (Klemperer) to parametry warte realne pieniądze. Trzydziestokrotna różnica między brytyjską a szwajcarską aukcją 3G nie wzięła się z jakości pasma.

To nie jest porada inwestycyjna. To mapa klasycznej teorii aukcji, z datami i liczbami z oryginalnych prac, po to, żeby format licytacji rozpoznawać, zanim się w nim zagra, a po każdej wygranej wycenie przeciw tłumowi zadawać sobie pytanie z 1971 roku: co wiedzieli ci, którzy licytowali niżej.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
