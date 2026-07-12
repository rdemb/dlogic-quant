---
title: "Regulacja banków. Po co Basel, kapitał i bufory"
description: "Banki reguluje się ostrożnościowo, bo upadek jednego banku wywołuje efekt domina, a rachunek za ratunek płaci podatnik. Tekst rozkłada mechanikę: po co jest kapitał (poduszka na straty i struktura finansowania, nie zapas gotówki), jak działa adekwatność kapitałowa od Basel I przez Basel II po Basel III, na czym polega pułapka aktywów ważonych ryzykiem (waga zero dla obligacji skarbowych, gry modelami wewnętrznymi), dlaczego wskaźnik dźwigni jest prostym bezpiecznikiem i skąd po 2008 wzięły się normy płynności LCR i NSFR. Na koniec procykliczność, pokusa nadużycia i krytyka Admati oraz Hellwig. Źródła: dokumenty Komitetu Bazylejskiego (BIS) i „The Bankers' New Clothes”."
date: 2026-07-04 11:00:00 +0200
eyebrow: "Edukacja · pieniądz"
dek: "Bank to nie zwykła firma, bo jego upadek przewraca kolejne instytucje, a rachunek płaci podatnik. Dlatego państwo narzuca reguły ostrożnościowe, których osią jest kapitał: poduszka pochłaniająca straty i sposób finansowania banku, a nie zapas gotówki w skarbcu. Bazylea, aktywa ważone ryzykiem, wskaźnik dźwigni i normy płynności rozłożone na mechanikę, plus lekcje, których udzielił rok 2008."
readingTime: 8
tags: [bank, "regulacja banków", Bazylea, "Basel III", "adekwatność kapitałowa", "kapitał własny", "aktywa ważone ryzykiem", RWA, "wskaźnik dźwigni", płynność, LCR, NSFR, procykliczność, "too big to fail", "pokusa nadużycia", "Komitet Bazylejski", BIS, "Admati i Hellwig", "kryzys 2008", makroekonomia, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Banki reguluje się inaczej niż piekarnie, bo upadek jednego banku zaraża kolejne (efekt domina przez wzajemne ekspozycje i przez panikę), a kiedy pada bank systemowy, koszt ratunku spada na podatnika. Reguły ostrożnościowe mają obniżyć i prawdopodobieństwo upadku, i jego cenę dla reszty gospodarki.
> - Osią regulacji jest kapitał własny, czyli poduszka pochłaniająca straty, zanim stracą deponenci i wierzyciele. To nie jest zapas gotówki leżący w skarbcu, tylko struktura finansowania: bank z grubszym kapitałem finansuje ten sam majątek mniejszym długiem, a większym udziałem właścicieli, więc wchłania większą stratę, zanim padnie.
> - Ile kapitału ma być, liczy się od aktywów ważonych ryzykiem (RWA), a nie od surowej sumy bilansu. To sedno umów bazylejskich (Basel I z 1988, Basel II, Basel III po 2008), a zarazem źródło słabości: obligacje skarbowe z wagą zero oraz modele wewnętrzne dały pole do zaniżania mierzonego ryzyka. Dlatego dołożono prosty wskaźnik dźwigni (kapitał do sumy aktywów bez wag) i normy płynności (LCR, NSFR).
> - Regulacja bywa procykliczna (w hossie mierzone ryzyko spada i wymogi luzują, w bessie zaciskają), a domniemana gwarancja państwa dla największych (too big to fail) zachęca je do ryzyka. Admati i Hellwig dowodzą, że banki mają wciąż za mało kapitału, a popularne argumenty przeciw wyższym wymogom są mylące.

**Teza w jednym zdaniu:** Banki reguluje się dlatego, że ich upadek jest zaraźliwy i drogi dla podatnika, a rdzeniem tych reguł jest kapitał własny jako poduszka na straty; cała reszta, czyli aktywa ważone ryzykiem, wskaźnik dźwigni, bufory antycykliczne i normy płynności, to kolejne próby odpowiedzi na jedno pytanie: ile kapitału i płynności bank musi mieć, żeby jego wbudowana kruchość nie stała się problemem całej gospodarki.

## Dlaczego bank to nie zwykła piekarnia

Kiedy pada piekarnia, tracą jej właściciele i dostawcy, a rynek chleba ledwie to zauważa. Kiedy pada bank, jest inaczej, z trzech powodów naraz. Po pierwsze, banki są splecione: pożyczają sobie nawzajem, rozliczają płatności i trzymają wobec siebie ekspozycje, więc upadek jednego wyrywa dziury w bilansach kolejnych. Po drugie, panika jest zaraźliwa: gdy jeden bank się chwieje, deponenci i wierzyciele innych zaczynają się zastanawiać, czy nie są następni, a od takiego pytania blisko do runu. Po trzecie, banki dostarczają całej gospodarce płatności i kredytu, więc ich zawał zamraża realną aktywność, nie tylko finanse.

Do tego dochodzi rzecz, która zmienia całą kalkulację. Rządu zwykle nie stać na to, żeby pozwolić dużemu bankowi po prostu upaść, bo koszt domina byłby wyższy niż koszt ratunku. Więc w krytycznym momencie państwo ratuje, publicznym pieniądzem. Oznacza to, że podatnik jest cichym współsygnatariuszem ryzyka, które bank bierze na siebie w dobrych czasach. Regulacja ostrożnościowa istnieje po to, żeby zmniejszyć jedno i drugie: prawdopodobieństwo, że bank padnie, oraz wysokość rachunku, gdy jednak padnie. Skąd bierze się sama kruchość, rozkłada [osobny tekst o tym, jak działa bank](/dlogic-quant/2026/07/07/jak-dziala-bank-bilans-i-kruchosc/); tutaj chodzi o to, co z tą kruchością robi regulator.

## Kapitał: poduszka na straty, nie skarbiec

Najczęstsze nieporozumienie dotyczy słowa kapitał. Wymóg kapitałowy nie oznacza sterty banknotów leżącej bezczynnie w skarbcu na czarną godzinę. Kapitał własny to pozycja po stronie pasywów: część majątku banku sfinansowana pieniędzmi właścicieli (akcjami i zatrzymanymi zyskami), a nie pożyczona od deponentów i wierzycieli. Innymi słowy kapitał odpowiada na pytanie nie „ile bank trzyma gotówki", tylko „czyimi pieniędzmi bank sfinansował swoje aktywa".

To rozróżnienie ma twarde konsekwencje. Kapitał własny jest tą warstwą bilansu, która pochłania straty jako pierwsza. Jeśli aktywa tracą na wartości, ubytek idzie najpierw w kapitał właścicieli, a dopiero gdy on się wyczerpie, zagrożone są pieniądze deponentów i wierzycieli. Więcej kapitału to po prostu grubsza poduszka, czyli większa strata wchłonięta, zanim bank stanie się niewypłacalny.

```
KAPITAL TO STRUKTURA FINANSOWANIA, NIE ZAPAS GOTOWKI:

  ten sam majatek 100, dwa sposoby sfinansowania

  BANK A (cienki kapital)          BANK B (gruby kapital)
  aktywa            100            aktywa            100
  dlug (depozyty,                  dlug (depozyty,
  finansowanie)      95            finansowanie)      85
  kapital wlasny      5            kapital wlasny     15
  ──────────────────────────       ──────────────────────────
  strata 5 na aktywach:
  kapital 5 → 0                    kapital 15 → 10
  bank na krawedzi                 bank spokojnie stoi

  wiecej kapitalu = wieksza strata wchlonieta przed upadkiem
```

Widać tu też, dlaczego zdanie „bank musi trzymać więcej kapitału, więc będzie mniej pożyczał" jest mylące. Wymóg kapitałowy dotyczy prawej strony bilansu (sposobu finansowania), a nie lewej (aktywów). Bank B ma dokładnie ten sam majątek co bank A, te same kredyty w portfelu. Różni się tylko tym, że mniejszą jego część sfinansował długiem, a większą pieniędzmi właścicieli. Grubszy kapitał nie zabiera pieniędzy z akcji kredytowej, tylko zmienia to, kto poniesie stratę, gdy coś pójdzie nie tak. Do tej pomyłki wrócą jeszcze Admati i Hellwig.

## Bazylea: od prostych wag do buforów

Skoro kapitał jest osią bezpieczeństwa, pojawia się pytanie praktyczne: ile go wymagać i jak to mierzyć porównywalnie między krajami. Odpowiadają na nie umowy Komitetu Bazylejskiego, ciała skupiającego głównych nadzorców przy Banku Rozrachunków Międzynarodowych (BIS). Dokumenty są jawne i darmowe, a ich ewolucja to opowieść o kolejnych łatanych dziurach.

Basel I z 1988 roku był pierwszym wspólnym standardem. Prosty do bólu: aktywa wrzucano do kilku koszyków ryzyka, każdemu przypisywano wagę, a minimalny kapitał wiązano z sumą tak zważonych aktywów. Zaleta to przejrzystość i porównywalność. Wada to zgrubność: kredyty bardzo różnej jakości trafiały do jednego koszyka, co zachęcało do upychania w nim tego, co najbardziej ryzykowne, bo dawało najwyższą marżę przy tym samym wymogu.

Basel II (uzgadniany w pierwszej dekadzie XXI wieku) miał być mądrzejszy: bardziej wrażliwy na rzeczywiste ryzyko, między innymi dzięki pozwoleniu dużym bankom na szacowanie wag własnymi modelami wewnętrznymi. W teorii lepiej, w praktyce dwa nowe problemy. Po pierwsze, procykliczność, o której niżej. Po drugie, pole do gry: jeśli bank sam szacuje ryzyko, ma interes w tym, żeby wyszło niskie, bo niższe ryzyko to niższy wymóg kapitałowy przy tym samym portfelu. Kryzys 2008 zastał system dokładnie w tym miejscu.

Basel III to odpowiedź po 2008. Kierunek jest jasny, nawet bez podawania konkretnych progów, które i tak z czasem się zmieniają. Więcej kapitału i, co ważniejsze, kapitału lepszej jakości: nacisk na najbardziej wartościową, naprawdę pochłaniającą straty część (zwykłe akcje i zatrzymane zyski), a nie na hybrydy, które w kryzysie okazały się miękkie. Do tego bufory: bufor zabezpieczający, który przy nadszarpnięciu ogranicza wypłaty dywidend i premii, oraz bufor antycykliczny, budowany w hossie i uwalniany w bessie. Wreszcie dwa nowe filary, których wcześniej nie było: prosty wskaźnik dźwigni i normy płynności. Obie te nowości biorą się z konkretnych lekcji, więc zasługują na osobne akapity.

## Aktywa ważone ryzykiem i ich pułapka

Sercem całej konstrukcji, od Basel I po dziś, jest jeden pomysł: nie wszystkie aktywa są tak samo ryzykowne, więc żądanie identycznego kapitału pod obligację skarbową i pod ryzykowny kredyt firmowy byłoby prymitywne. Dlatego każdej ekspozycji przypisuje się wagę ryzyka, a wymagany kapitał liczy się od sumy tak zważonych aktywów, czyli od RWA (risk-weighted assets), a nie od surowej sumy bilansu.

```
AKTYWA WAZONE RYZYKIEM (RWA), schemat ilustracyjny:

  ekspozycja  ×  waga ryzyka  =  aktywo wazone ryzykiem
  ───────────────────────────────────────────────────────
  obligacja skarbowa  100  ×    0%  =    0
  kredyt hipoteczny   100  ×   35%  =   35
  kredyt firmowy      100  ×  100%  =  100
  ───────────────────────────────────────────────────────
  wymog kapitalowy liczy sie od sumy RWA, nie od sumy aktywow

  pulapka: waga 0% zachecala do gromadzenia obligacji panstwa,
           modele wewnetrzne pozwalaly zanizac wlasne wagi
```

Sam pomysł jest rozsądny. Pułapka tkwi w szczegółach i to ona jest jedną z ważniejszych lekcji ostatnich kryzysów. Pierwsza rysa: obligacje skarbowe własnego państwa dostawały wagę zero, więc ich trzymanie nie wymagało w ogóle kapitału. To wyglądało bezpiecznie i przez lata bezpieczne bywało, ale sam mechanizm zachęcał banki do ładowania bilansów długiem rządowym, aż do dnia, w którym „bezpieczny" dług przestawał być bezpieczny, jak w europejskim kryzysie zadłużeniowym. Regulacja, która miała mierzyć ryzyko, po cichu premiowała koncentrację w jednej klasie aktywów.

Druga rysa jest subtelniejsza i groźniejsza. Modele wewnętrzne z Basel II pozwalały bankom szacować własne wagi ryzyka. Kierunek pokusy jest oczywisty: im niżej model wyceni ryzyko, tym niższy wymóg kapitałowy przy niezmienionym portfelu. Efekt to bank, który wygląda dobrze skapitalizowany według swojego wskaźnika opartego na RWA, a pod spodem ma cienką realną poduszkę, bo mianownik został wymodelowany w dół. Wskaźnik pokazujący zdrowie może więc maskować chudy bufor. Stąd potrzeba drugiego, prostszego pomiaru, którego nie da się tak łatwo podrasować.

## Wskaźnik dźwigni: prosty bezpiecznik

Odpowiedzią jest wskaźnik dźwigni: kapitał odniesiony do sumy aktywów, bez żadnego ważenia ryzykiem. Jest tępy, bo traktuje obligację skarbową i ryzykowny kredyt tak samo. Ale właśnie w tej tępocie tkwi jego siła: skoro nie ma wag, nie ma czego podkręcać modelem. Cokolwiek bank zrobi ze swoimi szacunkami ryzyka, wskaźnik dźwigni i tak zmierzy, ile realnego majątku przypada na jednostkę kapitału.

```
DWA OBIEKTYWY NA TEN SAM BANK:

  wskaznik oparty na RWA:  kapital / aktywa wazone ryzykiem
     czuly na ryzyko, ale podatny na gry wagami i modelami

  wskaznik dzwigni:        kapital / suma aktywow (bez wag)
     tepy, ale odporny na manipulacje wagami

  Basel III trzyma oba naraz:
  jeden lapie to, co drugi przepuszcza
```

Dlatego Basel III nie zastąpił wskaźnika opartego na RWA wskaźnikiem dźwigni, tylko dołożył ten drugi jako zabezpieczenie awaryjne. Filozofia jest taka jak przy dwóch niezależnych obiektywach patrzących na ten sam obiekt: wskaźnik oparty na ryzyku jest inteligentny, ale manipulowalny, wskaźnik dźwigni jest prosty, ale trudny do oszukania. Bank musi spełnić oba naraz, więc jeden łapie to, co drugi przepuszcza. To zresztą wraca do arytmetyki dźwigni: skoro kapitał jest cienkim ułamkiem bilansu, niewielka procentowo strata na aktywach zjada nieproporcjonalnie dużą część kapitału, a wskaźnik dźwigni pilnuje, żeby ten ułamek nie zrobił się niebezpiecznie cienki niezależnie od tego, co twierdzą modele.

## Płynność: bo 2008 był kryzysem płynności

Do 2008 roku Bazylea skupiała się na wypłacalności, czyli na kapitale. Kryzys pokazał, że to za mało. Wiele instytucji nie padło dlatego, że ich aktywa z dnia na dzień stały się bezwartościowe, tylko dlatego, że krótkoterminowe finansowanie wyparowało szybciej, niż dało się cokolwiek upłynnić. To była lekcja, że można być (przynajmniej papierowo) wypłacalnym i mimo to umrzeć z braku płynności, bo rachunki rozlicza się gotówką i rezerwami dzisiaj, a nie wartością aktywów kiedyś. Rozróżnienie płynności i wypłacalności rozkłada [tekst o mechanice banku](/dlogic-quant/2026/07/07/jak-dziala-bank-bilans-i-kruchosc/); Basel III wyciągnął z niego wniosek regulacyjny.

Wniosek przyjął postać dwóch nowych norm płynności. Pierwsza, LCR (wskaźnik pokrycia płynności), wymaga, żeby bank trzymał dość aktywów wysokiej jakości, łatwych do szybkiej sprzedaży, aby przetrwać zdefiniowany okres stresu, w którym pieniądz odpływa. Idea: przetrwać burzę własnym zapasem, bez natychmiastowego biegu po ratunek. Druga, NSFR (wskaźnik stabilnego finansowania netto), pilnuje struktury finansowania w dłuższym horyzoncie: długie i niepłynne aktywa mają być finansowane stabilnym, dłuższym pieniądzem, a nie finansowaniem, które może zniknąć jutro. W skrócie: nie finansuj trzydziestoletniego kredytu pieniądzem pożyczonym na jedną noc. Konkretne progi z czasem się zmieniają, ale mechanika jest trwała: kapitał odpowiada za pochłanianie strat, płynność za przetrwanie okna, w którym finansowanie ucieka.

## Procykliczność i pokusa nadużycia

Zostają dwie słabości, których nie usuwa żaden pojedynczy wskaźnik, bo tkwią w samej naturze regulacji i bodźców. Pierwsza to procykliczność. Reguły wrażliwe na ryzyko poruszają się razem z cyklem, i to w złą stronę. W hossie mierzone ryzyko jest niskie: ceny aktywów rosną, upadłości są rzadkie, modele widzą spokój, więc RWA spada, a wymogi się rozluźniają, co pozwala pożyczać więcej i jeszcze bardziej rozgrzewa boom. W bessie dzieje się odwrotnie: mierzone ryzyko skacze, wymogi się zaciskają, banki tną kredyt i wyprzedają aktywa, żeby podnieść wskaźniki, co pogłębia wyprzedaż i zapaść kredytową. Regulacja pomyślana jako hamulec potrafi więc dolewać oliwy do cyklu, który miała tłumić. Bufor antycykliczny z Basel III jest właśnie próbą odwrócenia tego odruchu: każe budować dodatkowy kapitał, gdy jest dobrze, żeby było co uwolnić, gdy jest źle.

Druga słabość to pokusa nadużycia wokół too big to fail. Jeśli wszyscy wierzą, że państwo nie pozwoli upaść gigantowi, to jego wierzyciele czują się chronieni i pożyczają mu taniej. Tania pożyczka premiuje dokładnie to, co niebezpieczne: większą dźwignię, większy rozmiar i większe ryzyko, bo zyski zostają prywatne, a straty w razie czego przejdą na publiczny rachunek. To domniemana gwarancja, za którą nikt formalnie nie płaci składki. Regulacja walczy z tym z kilku stron: wyższymi wymogami i dopłatami kapitałowymi dla banków systemowych oraz reżimami uporządkowanej likwidacji, które mają uczynić upadek dużego banku możliwym bez pociągania za sobą całego systemu.

Najostrzejszą krytykę całości formułują Anat Admati i Martin Hellwig w książce „The Bankers' New Clothes" (Princeton University Press, 2013). Tytuł nawiązuje do baśni o nowych szatach cesarza: argumenty branży przeciw wyższemu kapitałowi brzmią uczenie, ale pod spodem są puste. Ich diagnoza jest prosta i niewygodna. Banki działają na skrajnie cienkim kapitale, z dźwignią, jakiej żadna zwykła firma by nie tknęła. Popularne kontrargumenty są mylące: „kapitał jest drogi" myli prywatny koszt (napędzany podatkową premią dla długu i oczekiwaniem ratunku) ze społecznym, a „więcej kapitału to mniej kredytu" i „kapitał leży bezczynnie" mylą sposób finansowania z zapasem gotówki, ten sam błąd, który pojawił się na początku tego tekstu. Wniosek autorów: bezpieczniejszy system wymaga wielokrotnie wyższego kapitału, niż przewidują dzisiejsze wymogi, a opór wobec tego bierze się głównie z prywatnych bodźców, nie z troski o gospodarkę.

## Co z tego wynika

Regulacja bankowa nie jest nudnym dodatkiem do finansów, tylko instrukcją obsługi, która tłumaczy, dlaczego banki zachowują się tak, jak się zachowują. Dlaczego lubią obligacje skarbowe (kiedyś waga zero). Dlaczego trzymają się blisko minimum kapitałowego (kapitał właścicieli jest z ich punktu widzenia droższy niż tani, subsydiowany dług). Dlaczego tak zaciekle bronią się przed wyższymi wymogami. I dlaczego w kryzysie wszystkie naraz tną kredyt i wyprzedają aktywa, zamiast działać wbrew stadu.

Głębsza lekcja 2008 jest jednak inna i warto ją zapamiętać ponad szczegółami. System, który wygląda bezpiecznie według własnych mierników, potrafi hodować ukryte ryzyko właśnie dlatego, że te mierniki dają się podrasować, a bodźce są przekrzywione. Wskaźnik oparty na RWA da się wymodelować w dół, waga zero potrafi zachęcić do koncentracji, procykliczność każe luzować dokładnie wtedy, gdy narasta bańka, a domniemana gwarancja nagradza rozrost i dźwignię. Kto rozumie tę mechanikę, ten czyta doniesienia o bankach z właściwymi pytaniami: jak cienki jest realny kapitał, ile deklarowanego bezpieczeństwa pochodzi z modelu, jak płochliwe jest finansowanie i czy poduszka pod spodem naprawdę udźwignie stratę, zanim zapłaci ją ktoś inny.

To nie jest porada inwestycyjna. To wykład mechaniki regulacji bankowej, oparty na jawnych dokumentach Komitetu Bazylejskiego przy BIS (Basel I z 1988, Basel II, Basel III) oraz na książce Anat Admati i Martina Hellwiga „The Bankers' New Clothes" (Princeton University Press, 2013), z nawiązaniem do modelu runu Diamonda i Dybviga (1983) i do [tekstu o tym, jak działa bank](/dlogic-quant/2026/07/07/jak-dziala-bank-bilans-i-kruchosc/). Konkretnych progów kapitałowych świadomie tu nie podano, bo się zmieniają; trwała jest mechanika, nie liczba.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
