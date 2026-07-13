---
title: "Inflacja, realne stopy i równanie Fishera"
description: "Równanie Fishera łączy stopę nominalną, realną i oczekiwaną inflację. Wersja przybliżona: stopa nominalna ≈ stopa realna + oczekiwana inflacja, obok dokładnej multiplikatywnej. Dlaczego dla kapitału liczy się siła nabywcza, czym różni się inflacja oczekiwana od nieoczekiwanej, jak rynek obligacji indeksowanych (breakeven, TIPS) wycenia oczekiwania oraz jak realna stopa działa jako stopa dyskontowa w wycenach aktywów i przez realne różnice stóp na kurs walutowy."
date: 2026-07-10 10:00:00 +0200
eyebrow: "Edukacja · makro"
dek: "Jedno równanie porządkuje makro dla inwestora: nominał to realna stopa plus oczekiwana inflacja. Stąd wynika, dlaczego rosnący nominalnie rachunek może tracić siłę nabywczą, dlaczego rynek czyta oczekiwania inflacyjne z obligacji indeksowanych i dlaczego realna stopa siedzi w każdej wycenie jako stopa dyskontowa oraz w każdej różnicy stóp między walutami."
readingTime: 8
tags: [makro, inflacja, "realne stopy", Fisher, TIPS, breakeven, "iluzja pieniądza", "stopa dyskontowa", "kurs walutowy", Modigliani, Siegel, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Równanie Fishera (Fisher, 1930): stopa nominalna ≈ stopa realna + oczekiwana inflacja. Postać dokładna jest multiplikatywna, (1 + nominalna) = (1 + realna) · (1 + oczekiwana inflacja), a pominięty w przybliżeniu iloczyn realna · inflacja zaczyna ważyć dopiero przy wysokiej inflacji.
> - Dla kapitału liczy się stopa realna, czyli po inflacji. Nominalne 5% przy inflacji 5% to realnie okolica zera: siła nabywcza stoi w miejscu, choć liczba na rachunku rośnie. To jest iluzja pieniądza, którą Irving Fisher opisał już w 1928 roku.
> - Oczekiwana inflacja jest wliczona w stopy nominalne, a majątek przesuwa dopiero inflacja nieoczekiwana. Zaskoczenie w górę przenosi wartość od wierzyciela do dłużnika, bo dług spłacany jest tańszym pieniądzem.
> - Rynek obligacji indeksowanych wycenia oczekiwaną inflację: breakeven to różnica między rentownością obligacji nominalnej a realną rentownością obligacji indeksowanej (TIPS). To miara zaszumiona premią za ryzyko inflacji i za płynność, nie czysty pomiar oczekiwań.

**Teza w jednym zdaniu:** Wartość kapitału mierzy się stopą realną, nie nominalną, a równanie Fishera pokazuje, że każda stopa nominalna rozkłada się na realny koszt pieniądza w czasie i oczekiwaną inflację; to ten rozkład, a nie sam nominał, rządzi stopą dyskontową w wycenach aktywów i różnicami stóp między walutami.

## Iluzja pieniądza: liczba rośnie, siła nabywcza niekoniecznie

Pensja w górę o 5%, a rachunek w sklepie o 6%. Nominalnie przybyło, realnie ubyło. Skłonność do myślenia liczbą na rachunku zamiast jej siłą nabywczą Irving Fisher nazwał iluzją pieniądza i poświęcił jej osobną książkę „The Money Illusion" (1928). Reszta tego tekstu to jedno równanie, które tę iluzję rozkłada na części i pokazuje, gdzie w wycenach aktywów oraz w kursach walut siedzi jej rachunek.

Punktem wyjścia jest rozróżnienie, które w codziennym języku znika: wielkość nominalna to liczba jednostek pieniądza, wielkość realna to ilość dóbr, którą za nie można kupić. Inflacja jest kursem wymiany między jednym a drugim i zmienia się w czasie. Dopóki liczy się tylko nominał, ten kurs pozostaje niewidoczny, a razem z nim znika prawdziwy wynik.

## Równanie Fishera: nominał to realna stopa plus oczekiwana inflacja

Irving Fisher w „The Theory of Interest" (1930) sformalizował związek, który spina te trzy wielkości. Stopa nominalna, ta zapisana w umowie kredytu czy obligacji, zawiera w sobie dwie rzeczy: realny koszt pieniądza w czasie oraz rekompensatę za spodziewany spadek jego wartości.

```
Równanie Fishera (postać dokładna, multiplikatywna):
(1 + i) = (1 + r) · (1 + πe)

i  = stopa nominalna
r  = stopa realna
πe = oczekiwana inflacja

rozwinięcie:   i = r + πe + r · πe
przybliżenie:  i ≈ r + πe        (pomija iloczyn r · πe)

PRZYKŁAD ILUSTRACYJNY (liczby służą arytmetyce, nie prognozie):
i = 5%, πe = 3%:
  dokładnie:    r = 1.05 / 1.03 − 1 ≈ 1,94%
  przybliżenie: r ≈ 5% − 3% = 2%       (błąd 0,06 p.p.)

i = 20%, πe = 15%:
  dokładnie:    r = 1.20 / 1.15 − 1 ≈ 4,35%
  przybliżenie: r ≈ 20% − 15% = 5%     (błąd 0,65 p.p.)
```

Przybliżenie stopa nominalna ≈ stopa realna + oczekiwana inflacja wystarcza przy niskiej inflacji, bo pominięty iloczyn dwóch małych liczb jest wtedy zaniedbywalny. Przy wysokiej inflacji ten sam iloczyn rośnie i wersja przybliżona zaczyna zawyżać stopę realną, dlatego w warunkach wysokiej inflacji poprawna jest postać multiplikatywna. Samo równanie jest tożsamością: przy danych trzech wielkościach zawsze się domyka. Osobną, mocniejszą tezą jest tak zwany efekt Fishera, zgodnie z którym stopa nominalna dostosowuje się do zmian oczekiwanej inflacji, pozostawiając stopę realną kształtowaną przez czynniki realne. To już hipoteza o zachowaniu rynku, nie sama arytmetyka.

<figure>
<svg viewBox="0 0 720 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Równanie Fishera jako składany słupek: stopa nominalna równa się stopa realna plus oczekiwana inflacja" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
  <title>Równanie Fishera jako składany słupek</title>
  <desc>Stopa nominalna podzielona na dwa segmenty: stopa realna i oczekiwana inflacja.</desc>
  <defs>
    <clipPath id="fisherBarClip"><rect x="60" y="100" width="600" height="58" rx="8"/></clipPath>
  </defs>
  <text x="360" y="30" text-anchor="middle" fill="currentColor" fill-opacity="0.85" font-size="18" font-weight="600">Równanie Fishera</text>
  <text x="360" y="70" text-anchor="middle" fill="currentColor" fill-opacity="0.8" font-size="15">stopa nominalna (i) ≈ 5%</text>
  <path d="M60 96 V88 H660 V96 M360 88 V78" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  <g clip-path="url(#fisherBarClip)">
    <rect x="60" y="100" width="240" height="58" fill="#0b66c3"/>
    <rect x="300" y="100" width="360" height="58" fill="#1a9e6a"/>
  </g>
  <line x1="300" y1="100" x2="300" y2="158" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5"/>
  <rect x="60" y="100" width="600" height="58" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5"/>
  <line x1="180" y1="158" x2="180" y2="186" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5"/>
  <line x1="480" y1="158" x2="480" y2="186" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5"/>
  <text x="180" y="204" text-anchor="middle" fill="currentColor" fill-opacity="0.8" font-size="13.5">stopa realna (r)</text>
  <text x="180" y="226" text-anchor="middle" fill="currentColor" fill-opacity="0.75" font-size="18" font-weight="600">2%</text>
  <text x="330" y="225" text-anchor="middle" fill="currentColor" fill-opacity="0.55" font-size="22">+</text>
  <text x="480" y="204" text-anchor="middle" fill="currentColor" fill-opacity="0.8" font-size="13.5">oczekiwana inflacja (πe)</text>
  <text x="480" y="226" text-anchor="middle" fill="currentColor" fill-opacity="0.75" font-size="18" font-weight="600">3%</text>
  <text x="360" y="256" text-anchor="middle" fill="currentColor" fill-opacity="0.5" font-size="12">przykład ilustracyjny, wersja przybliżona</text>
</svg>
<figcaption>Równanie Fishera jako składany słupek: stopa nominalna to suma stopy realnej i oczekiwanej inflacji. Liczby (2%, 3%, 5%) są przykładem ilustracyjnym w wersji przybliżonej, nie prognozą.</figcaption>
</figure>

## Nominalna kontra realna: dlaczego kapitał liczy się w sile nabywczej

Skoro nominał zawiera rekompensatę za inflację, to o przyroście majątku decyduje dopiero to, co zostaje po jej odjęciu.

```
PRZYKŁAD ILUSTRACYJNY: 100 jednostek, i = 5% nominalnie, 10 lat
inflacja π = 3% rocznie

wartość nominalna:            100 · 1.05^10        ≈ 162,9
w dzisiejszej sile nabywczej: 100 · (1.05/1.03)^10 ≈ 121,2

przypadek i = π = 5%:
  nominalnie: 100 · 1.05^10 ≈ 162,9
  realnie:    100 · (1.05/1.05)^10 = 100   (zero realnego wzrostu)
```

Nominalne 162,9 wygląda na sukces, realne 121,2 to prawda o sile nabywczej. Gdy stopa nominalna równa się inflacji, realny przyrost wynosi zero, mimo że liczba na rachunku urosła o ponad 60%. Gdy inflacja przewyższa stopę nominalną, przyrost realny jest ujemny: kapitał traci siłę nabywczą, choć jego nominalny zapis rośnie. To sedno iluzji pieniądza w wersji dla inwestora, a zarazem powód, dla którego najdłuższe zestawienia zwrotów podaje się realnie. Jeremy Siegel w „Stocks for the Long Run" (pierwsze wydanie 1994) raportuje zwroty amerykańskich akcji po inflacji właśnie dlatego, że tylko liczba realna mówi, ile dóbr przybyło.

## Inflacja oczekiwana kontra nieoczekiwana

Równanie Fishera zawiera inflację oczekiwaną, nie zrealizowaną, i to rozróżnienie ma konkretne konsekwencje. Oczekiwana inflacja jest już wliczona w stopy nominalne w chwili zawierania umowy: pożyczkodawca żąda jej rekompensaty z góry. Dopóki inflacja wypada zgodnie z oczekiwaniem, nikt nie jest zaskoczony, a podział korzyści przebiega tak, jak założono.

Majątek przesuwa dopiero inflacja nieoczekiwana. Jeśli zrealizowana inflacja przewyższy tę wliczoną w stopę, dłużnik spłaca zobowiązanie pieniądzem o niższej sile nabywczej i zyskuje kosztem wierzyciela; zaskoczenie w drugą stronę odwraca kierunek transferu. Wszystkie kontrakty ustalone nominalnie, obligacje o stałym kuponie, kredyty, pensje zapisane w umowie, są wyceniane na inflację oczekiwaną, a rozliczane w inflacji zrealizowanej. Różnica między jedną a drugą jest tym, co faktycznie redystrybuuje wartość, i dlatego oczekiwania inflacyjne są tak uważnie obserwowane, a ich nagłe rewizje potrafią gwałtownie przecenić obligacje.

## Breakeven z obligacji indeksowanych: rynkowa miara oczekiwań

Skoro oczekiwana inflacja siedzi w stopach nominalnych, można ją z nich wydobyć, o ile istnieje instrument pozbawiony inflacyjnej rekompensaty. Takim instrumentem są obligacje indeksowane inflacją, w wersji amerykańskiej TIPS: ich kapitał podąża za wskaźnikiem cen, więc płacą rentowność realną. Zestawienie ich z obligacją nominalną o tym samym terminie daje rynkową miarę oczekiwań.

```
breakeven = rentowność nominalna − rentowność realna (obligacja indeksowana)

to średnia inflacja, przy której trzymanie obligacji nominalnej
i indeksowanej daje ten sam wynik

składniki breakeven:
  oczekiwana inflacja
  + premia za ryzyko inflacji
  − premia za niższą płynność obligacji indeksowanej
```

Breakeven inflation jest więc różnicą rentowności nominalnej i realnej i można go czytać jako średnią inflację oczekiwaną przez rynek na dany horyzont. Z zastrzeżeniem: to miara zaszumiona. Zawiera premię za ryzyko inflacji, której inwestor żąda za niepewność co do przyszłych cen, oraz efekt niższej płynności obligacji indeksowanych, zwykle mniej chętnie handlowanych niż zwykłe obligacje skarbowe. Z tych powodów breakeven jest przybliżeniem oczekiwań, a nie ich czystym pomiarem. Mimo to pozostaje jednym z niewielu odczytów oczekiwań inflacyjnych dostępnych w czasie rzeczywistym i z rynkową, a nie ankietową, dyscypliną.

## Realna stopa jako koszt pieniądza i stopa dyskontowa

Stopa realna to cena czasu: ile realnie kosztuje przesunięcie konsumpcji z przyszłości do teraz. Ta sama liczba jest fundamentem każdej wyceny, bo wartość aktywa to zdyskontowana suma jego przyszłych przepływów.

```
wartość bieżąca przepływu C za n lat:
PV = C / (1 + r)^n        (r realne dla przepływów realnych)

im wyższa realna stopa r, tym niższe PV
efekt rośnie z n: aktywa o długim horyzoncie reagują najsilniej
```

Wyższa stopa realna podnosi mianownik i obniża wartość bieżącą, a im dalej w przyszłość sięgają przepływy, tym mocniej. Dlatego aktywa o długim horyzoncie, obligacje o długim terminie i spółki, których zyski są odległe, reagują na zmiany realnych stóp najsilniej. Tu wchodzi klasyczna obserwacja Modiglianiego i Cohna (1979): inwestorzy giełdowi ulegają iluzji inflacji, dyskontując realne zyski spółek stopą nominalną zamiast realną i nie doceniając, że inflacja obniża realny ciężar nominalnego zadłużenia firm. Skutkiem, zdaniem autorów, jest systematyczne zaniżanie wyceny akcji w okresach wysokiej inflacji. To iluzja pieniądza przeniesiona z pojedynczego rachunku na cały rynek.

## Realne różnice stóp a kurs walutowy

To samo rozłożenie stopy nominalnej na część realną i inflacyjną porządkuje myślenie o kursach walut. W długim okresie parytet siły nabywczej wiąże kurs nominalny z różnicą inflacji: waluta kraju o trwale wyższej inflacji ma tendencję do nominalnej deprecjacji, która tę różnicę cen kompensuje. Osobno definiuje się kurs realny, czyli nominalny skorygowany o relację poziomów cen, i to on jest właściwą miarą konkurencyjności.

Przez równanie Fishera różnica stóp nominalnych między dwiema walutami rozkłada się na różnicę stóp realnych i różnicę oczekiwanej inflacji. Wysoka stopa nominalna napędzana wyłącznie wysoką oczekiwaną inflacją to nie to samo, co wysoka stopa realna: pierwsza sygnalizuje presję na deprecjację, druga w teorii przyciąga kapitał szukający wyższego realnego zwrotu. Rozdzielenie tych dwóch składników jest sednem makro spojrzenia na waluty. Zastrzeżenie jest tu jednak mocne: powyższe zależności to długookresowe, teoretyczne mechanizmy, a nie reguły dające się przełożyć na krótkoterminowy sygnał. Empirycznie kursy potrafią latami odchylać się od parytetu siły nabywczej, a relacja między różnicami stóp a zmianami kursów jest notorycznie zaszumiona. To rama do rozumienia, nie recepta na prognozę.

Materiał czysto edukacyjny, nie porada inwestycyjna. Liczby w przykładach służą arytmetyce, nie prognozie, i są jawnie oznaczone jako ilustracyjne. Pewny jest tu wyłącznie rozkład stopy nominalnej na realny koszt pieniądza i oczekiwaną inflację (Fisher, 1930) oraz płynące z niego wnioski o sile nabywczej, dyskontowaniu i kursie realnym; wszystko, co dotyczy przyszłej inflacji, przyszłych stóp i przyszłych kursów, pozostaje niepewne.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
