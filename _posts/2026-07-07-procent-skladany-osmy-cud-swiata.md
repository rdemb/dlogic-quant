---
title: "Procent składany. Ósmy cud świata policzony"
description: "Wzrost wykładniczy kontra liniowa intuicja: 1000 na ilustracyjnych 7% rocznie to po 40 latach 14 974, nie 3800. Reguła 72, cena startu o dekadę później, 1,5 p.p. opłat zjadające około jednej trzeciej kapitału po 30 latach, variance drain oraz kontekst z najdłuższych szeregów danych: około 200 lat Siegela i 126 lat rocznika UBS."
date: 2026-07-07 15:00:00 +0200
eyebrow: "Edukacja · długi termin"
dek: "Cztery rachunki, które ustawiają myślenie o długim terminie: czas podwojenia z reguły 72, koszt spóźnionego startu, opłaty jako cichy pożeracz kapitału i zmienność, która obniża tempo składania. Do tego dwa najdłuższe zbiory danych o zwrotach, jakie istnieją: Siegel oraz rocznik Dimsona, Marsha i Stauntona. Wszystko policzalne na serwetce."
readingTime: 7
tags: ["procent składany", "reguła 72", compounding, "variance drain", opłaty, koszty, horyzont, "długi termin", Siegel, Bogle, "Dimson Marsh Staunton", Housel, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Mózg ekstrapoluje liniowo, kapitał rośnie wykładniczo. 1000 na ilustracyjnych 7% rocznie to po 40 latach 14 974, a nie 3800 z liniowego szacunku. Połowa końcowej kwoty powstaje w ostatnich 10 z 40 lat.
> - Reguła 72: czas podwojenia ≈ 72 / stopa. Przy 7% kapitał podwaja się co około 10,3 roku, przy 2% co 36 lat. Kilka punktów procentowych stopy to na długim horyzoncie różnica liczby podwojeń, nie „trochę więcej".
> - Start o dekadę później kosztuje ponad dwukrotność rocznej wpłaty: żeby dogonić 40 lat odkładania po 1000 rocznie (przykład na 7%), trzeba przez 30 lat odkładać po około 2113. A 1,5 p.p. opłat rocznie zjada po 30 latach około jedną trzecią kapitału końcowego: 1.07^30 ≈ 7.61 wobec 1.055^30 ≈ 4.98. Ta arytmetyka jest pewna, niezależna od prognoz.
> - Zmienność obniża tempo składania: +50% i potem −50% to nie zero, tylko −25%. Kontekst historyczny: realny zwrot akcji USA to około 6,5-7% rocznie za blisko 200 lat (Siegel), a rocznik UBS za lata 1900-2025 daje realnie 6,6% rocznie dla akcji wobec 1,6% dla obligacji. To średnie z bardzo długich okresów, po drodze bywały dekady posuchy.

**Teza w jednym zdaniu:** O wyniku składania decydują trzy dźwignie: czas, stopa po kosztach i stabilność tej stopy; czas jest z nich najsilniejszy, a cała potrzebna matematyka mieści się w czterech krótkich rachunkach.

## Mózg liczy liniowo, kapitał rośnie wykładniczo

Cytat o procencie składanym jako ósmym cudzie świata bywa przypisywany Einsteinowi i jest najpewniej apokryficzny. Liczby bronią się jednak bez autorytetu. Pierwszy rok inwestycji 1000 przy stopie 7% dodaje 70. Liniowa intuicja mnoży: 40 lat razy 70 to 2800 zysku, razem około 3800. Rzeczywistość: 14 974, prawie cztery razy więcej. Błąd nie bierze się z niewiedzy, tylko z konstrukcji intuicji. Mózg dobrze ekstrapoluje proste, a wzrost wykładniczy przez większość trasy wygląda jak prosta i dopiero pod koniec odsłania krzywiznę.

```
Stopa 7% rocznie jest ilustracyjna (służy arytmetyce, nie prognozie).

1000 · 1.07^10 ≈  1 967
1000 · 1.07^20 ≈  3 870
1000 · 1.07^30 ≈  7 612
1000 · 1.07^40 ≈ 14 974

liniowy szacunek: 1000 + 40 · 70 = 3 800
zysk w 1. roku:   70
zysk w 40. roku:  ~980 (14 razy więcej, przy tej samej stopie)
ostatnie 10 lat:  7 612 → 14 974, czyli połowa końcowej kwoty
```

Stąd najbardziej niedoceniana własność składania: efekt kumuluje się na końcu. Morgan Housel w „The Psychology of Money" (2020) podaje skrajny przykład: z 84,5 mld USD majątku Warrena Buffetta (w chwili pisania książki) 81,5 mld przyszło po jego 65. urodzinach. Nie dlatego, że stopa wzrosła na starość, tylko dlatego, że składanie działało nieprzerwanie od czasów, gdy Buffett był dzieckiem. Sekret nie tkwi w wyjątkowej stopie, tylko w wyjątkowo długim, nieprzerwanym horyzoncie.

<figure style="margin:2rem 0">
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Porównanie wzrostu liniowego i wykładniczego kapitału w ciągu 40 lat przy stopie 7% rocznie" style="width:100%;height:auto;max-width:720px;display:block;margin:0 auto;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif">
  <rect x="540" y="30" width="160" height="340" fill="#1a9e6a" opacity="0.06"/>
  <path d="M60,348.8 L140,340.2 L220,328.2 L300,311.4 L380,287.8 L460,254.7 L540,208.2 L620,143.1 L700,51.8 L700,289.2 L60,348.8 Z" fill="#1a9e6a" opacity="0.10"/>
  <g stroke="currentColor" stroke-opacity="0.18" stroke-width="1">
    <line x1="60" y1="285" x2="700" y2="285"/>
    <line x1="60" y1="200" x2="700" y2="200"/>
    <line x1="60" y1="115" x2="700" y2="115"/>
    <line x1="220" y1="30" x2="220" y2="370"/>
    <line x1="380" y1="30" x2="380" y2="370"/>
  </g>
  <g stroke="currentColor" stroke-opacity="0.45" stroke-width="1.2">
    <line x1="60" y1="30" x2="60" y2="370"/>
    <line x1="60" y1="370" x2="700" y2="370"/>
  </g>
  <line x1="540" y1="30" x2="540" y2="370" stroke="#1a9e6a" stroke-opacity="0.45" stroke-width="1.3" stroke-dasharray="4 4"/>
  <line x1="60" y1="348.8" x2="700" y2="289.2" stroke="currentColor" stroke-opacity="0.6" stroke-width="2" stroke-dasharray="5 4"/>
  <polyline points="60,348.8 140,340.2 220,328.2 300,311.4 380,287.8 460,254.7 540,208.2 620,143.1 700,51.8" fill="none" stroke="#1a9e6a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <g fill="#1a9e6a" stroke="currentColor" stroke-opacity="0.25" stroke-width="1">
    <circle cx="220" cy="328.2" r="4.2"/>
    <circle cx="380" cy="287.8" r="4.2"/>
    <circle cx="540" cy="208.2" r="4.2"/>
    <circle cx="700" cy="51.8" r="4.2"/>
  </g>
  <g>
    <line x1="78" y1="52" x2="108" y2="52" stroke="#1a9e6a" stroke-width="3"/>
    <text x="114" y="56" fill="currentColor" opacity="0.8" font-size="12.5">wzrost wykładniczy (7%/rok)</text>
    <line x1="78" y1="74" x2="108" y2="74" stroke="currentColor" stroke-opacity="0.6" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="114" y="78" fill="currentColor" opacity="0.7" font-size="12.5">intuicja liniowa (prosta)</text>
  </g>
  <text x="692" y="46" text-anchor="end" fill="#1a9e6a" font-weight="700" font-size="13">≈ 14 974</text>
  <text x="692" y="283" text-anchor="end" fill="currentColor" opacity="0.7" font-size="13">≈ 3 800</text>
  <text x="548" y="250" fill="#1a9e6a" opacity="0.8" font-size="12">ostatnie 10 lat:</text>
  <text x="548" y="266" fill="#1a9e6a" opacity="0.8" font-size="12">połowa końcowej kwoty</text>
  <text x="60" y="22" fill="currentColor" opacity="0.7" font-size="12.5">kapitał</text>
  <text x="380" y="408" text-anchor="middle" fill="currentColor" opacity="0.7" font-size="12.5">lata</text>
  <g fill="currentColor" opacity="0.65" font-size="11" text-anchor="middle">
    <text x="60" y="388">0</text>
    <text x="220" y="388">10</text>
    <text x="380" y="388">20</text>
    <text x="540" y="388">30</text>
    <text x="700" y="388">40</text>
  </g>
  <g fill="currentColor" opacity="0.65" font-size="11" text-anchor="end">
    <text x="53" y="374">0</text>
    <text x="53" y="289">4 000</text>
    <text x="53" y="204">8 000</text>
    <text x="53" y="119">12 000</text>
    <text x="53" y="34">16 000</text>
  </g>
</svg>
<figcaption>Ta sama kwota startowa i ta sama stopa 7% rocznie: liniowa intuicja (przerywana prosta) i realny wzrost wykładniczy pokrywają się na starcie, a rozjeżdżają dopiero pod koniec. Po 40 latach to 3 800 wobec 14 974, przy czym połowa końcowej kwoty powstaje w podświetlonych ostatnich 10 latach.</figcaption>
</figure>

## Reguła 72: podwojenia liczone w pamięci

Zamiast potęgować, wystarczy zapamiętać jedną liczbę. Czas podwojenia kapitału to w przybliżeniu 72 podzielone przez stopę w procentach. Przybliżenie bierze się z tego, że ln 2 ≈ 0,693, a 72 wygrywa z 69, bo dzieli się wygodnie przez 2, 3, 4, 6, 8, 9 i 12 oraz lekko koryguje błąd przybliżenia dla typowych stóp jednocyfrowych.

```
czas podwojenia ≈ 72 / stopa (w % rocznie)

 2%  → 36 lat     (dokładnie 35,0)
 4%  → 18 lat     (17,7)
 7%  → 10,3 roku  (10,2)
10%  → 7,2 roku   (7,3)
```

Reguła zamienia stopy na podwojenia i nagle widać skalę. 40 lat przy 7% to niemal cztery podwojenia, a 2^4 = 16, stąd piętnastokrotność z poprzedniego bloku. Przy 2% ten sam horyzont to nieco ponad jedno podwojenie (1.02^40 ≈ 2.21). Różnica „5 punktów procentowych" brzmi niegroźnie, a na 40 latach oznacza różnicę między piętnastokrotnością a okolicą 2,2 raza.

## Cena spóźnionego startu

Skoro efekt kumuluje się na końcu, to opóźnienie startu obcina właśnie najcenniejsze lata, te ostatnie. Kto zaczyna dekadę później, nie traci dekady „z początku", traci dekadę podwojeń z końca. Rachunek na stopie ilustracyjnej:

```
PRZYKŁAD ILUSTRACYJNY: stopa 7% rocznie, wpłata na koniec roku
FV = wpłata · (1.07^n − 1) / 0.07

40 lat po 1000 rocznie: ≈ 199 600   (suma wpłat: 40 000)
30 lat po 1000 rocznie: ≈  94 500   (suma wpłat: 30 000)

ten sam cel ~199 600 w 30 lat wymaga wpłat po ≈ 2 113 rocznie,
czyli 2,1 raza więcej co rok i 63 400 wpłat łącznie zamiast 40 000
```

Wersja ostrzejsza, znana z podręczników finansów osobistych, na tym samym horyzoncie 40 lat:

```
A: wpłaca 1000 rocznie tylko przez pierwsze 10 lat, potem nic
   po 10 latach ≈ 13 816, dalej 30 lat samego składania:
   13 816 · 1.07^30 ≈ 105 000     (suma wpłat: 10 000)

B: zaczyna w 11. roku, wpłaca 1000 rocznie przez 30 lat
   wynik ≈ 94 500                 (suma wpłat: 30 000)

A kończy wyżej, wpłaciwszy trzy razy mniej.
```

Dziesięć wczesnych lat wpłat pobija trzydzieści późniejszych. To nie magia, to geometria: każda wpłata A pracowała od 30 do 39 lat, wpłaty B średnio przez połowę tego czasu.

## Opłaty: 1,5 punktu procentowego to jedna trzecia kapitału

Opłaty wyglądają niewinnie, bo są podawane w skali roku, a działają w skali dekad. Mechanizm jest lustrzany wobec zysków: koszty też się składają, tylko przeciwko rachunkowi. Ten rachunek nie wymaga żadnej prognozy, wystarczy potęgowanie:

```
7,0% rocznie:  1.07^30  ≈ 7.61    (100 000 → ok. 761 000)
5,5% rocznie:  1.055^30 ≈ 4.98    (100 000 → ok. 498 000)

różnica to tylko 1,5 p.p. rocznych opłat,
ubytek kapitału końcowego: 1 − 4.98/7.61 ≈ 34,5%, około jedna trzecia

po 40 latach: 1.055^40 / 1.07^40 ≈ 8.51 / 14.97, ubytek ≈ 43%
```

Im dłuższy horyzont, tym większy udział opłat w wyniku, dokładnie z tego samego powodu, dla którego składanie w ogóle działa. John Bogle nazywał to tyranią składanych kosztów i sprowadzał rzecz do jednego zdania: w inwestowaniu dostaje się to, za co się nie zapłaciło. Dokładny procent ubytku zależy od stopy bazowej, ale mechanizm jest pewny matematycznie: każdy punkt bazowy opłat pracuje przeciw kapitałowi przez wszystkie lata i wszystkie podwojenia.

## Średnia arytmetyczna kłamie, składa się geometryczna

Ostatnia dźwignia jest najmniej intuicyjna: sama zmienność obniża tempo składania, nawet przy tej samej „średniej". Klasyczny przykład: plus 50%, potem minus 50%. Średnia arytmetyczna wynosi zero, a kapitał stopniał o jedną czwartą.

```
+50%, potem −50%:   1.5 · 0.5 = 0.75  →  −25%, nie 0%
średnia arytmetyczna: (+50% − 50%) / 2 = 0%
średnia geometryczna: √0.75 − 1 ≈ −13,4% na okres

dwa aktywa o tej samej średniej arytmetycznej 7%:
stabilne:   +7% co roku            → 1.07^30 ≈ 7.61
huśtawka:   +27%, −13%, na zmianę  → (1.27 · 0.87)^15 ≈ 4.47

przybliżenie: tempo geometryczne ≈ arytmetyczne − σ²/2
tutaj: 7% − (20%)²/2 = 7% − 2 p.p. ≈ 5% rocznie
```

To zjawisko nosi nazwę variance drain. Kapitał składa się po średniej geometrycznej, a ta jest niższa od arytmetycznej o mniej więcej połowę wariancji. Dlatego dwie strategie o identycznej „średniej stopie" mogą po 30 latach dzielić dziesiątki procent kapitału i dlatego głębokie obsunięcia są tak drogie: strata 50% wymaga zysku 100%, żeby wrócić do zera.

## Co mówią najdłuższe szeregi danych, jakie istnieją

Ile naprawdę wynosiła stopa, którą dało się składać? Dwa źródła mają najdłuższe szeregi. Jeremy Siegel w „Stocks for the Long Run" (pierwsze wydanie 1994, szóste 2022) zebrał dane amerykańskie od 1802 roku: realny, czyli po inflacji, łączny zwrot z akcji USA wynosił około 6,5-7% rocznie i pozostawał zaskakująco stabilny między stuleciami. Drugie źródło to „Global Investment Returns Yearbook" Dimsona, Marsha i Stauntona, od 2024 wydawany przez UBS, wcześniej przez Credit Suisse: 126 lat danych z 35 rynków. Za okres 1900-2025 akcje dały realnie około 6,6% rocznie wobec 1,6% dla obligacji.

Regułą 72 widać, co ta różnica znaczy: przy 6,6% realna wartość podwaja się co około 11 lat, przy 1,6% co około 45 lat. Na horyzoncie pokolenia to przepaść między kilkoma podwojeniami a jednym.

I tu obowiązkowe zastrzeżenie, bez którego ten rozdział byłby marketingiem: to są średnie z bardzo długich okresów, nie obietnica na najbliższą dekadę. Po drodze zdarzały się długie posuchy: lata 1966-1982 w USA były dla akcji realnie stracone, dekada 2000-2009 również wypadła realnie pod kreską, a japoński rynek po szczycie z 1989 roku potrzebował ponad trzech dekad, by wrócić w okolice szczytu. Średnia 6,6% zawiera te epizody w cenie. Kto ma horyzont pięcioletni, nie ma horyzontu, na którym te średnie pracują. Kto ma trzydziestoletni, spotyka po drodze wszystkie cztery rachunki z tego tekstu naraz: podwojenia, koszt opóźnienia, opłaty i variance drain.

Materiał czysto edukacyjny, nie porada inwestycyjna. Stopa 7% w przykładach służy arytmetyce, nie prognozie; historyczne średnie opisują przeszłość i niczego nie gwarantują. Pewna jest tu wyłącznie matematyka składania: potęgowanie, reguła 72 i różnica między średnią arytmetyczną a geometryczną.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
