---
title: "Prawdopodobieństwo i rozkłady. Język niepewności rynku"
description: "Zmienna losowa, rozkład i gęstość, cztery momenty (wartość oczekiwana, wariancja, skośność, kurtoza) oraz rozkład normalny wraz z centralnym twierdzeniem granicznym i tym, gdzie Gauss zawodzi na rynku. Grube ogony i prawa potęgowe: Mandelbrot (1963) z indeksem ogona poniżej 2 i nieskończoną wariancją, korekta Conta (2001) do indeksu powyżej 2, rozkład t Studenta z grubością ogona sterowaną liczbą stopni swobody. Do tego prawdopodobieństwo warunkowe, twierdzenie Bayesa oraz różnica między prawdopodobieństwem a szansami. Pogłębienie matematyczne tekstu o stylizowanych faktach."
date: 2026-07-11 14:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Słownik, którym rynek mówi o niepewności: zmienna losowa, rozkład, gęstość oraz cztery momenty opisujące kształt. Dlaczego rozkład normalny kusi (centralne twierdzenie graniczne) i gdzie zawodzi (grube ogony, prawa potęgowe, rozkład t Studenta). Do tego prawdopodobieństwo warunkowe, Bayes w skrócie i różnica między prawdopodobieństwem a szansami."
readingTime: 8
tags: [matematyka, prawdopodobieństwo, rozkłady, "zmienna losowa", "wartość oczekiwana", wariancja, "grube ogony", kurtoza, "rozkład normalny", "centralne twierdzenie graniczne", "rozkład t Studenta", Bayes, Mandelbrot, Cont, Taleb, statystyka, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Zmienna losowa przypisuje liczbę wynikowi losowego zdarzenia, a jej rozkład mówi, jak prawdopodobne są poszczególne wartości. Dla wielkości ciągłych opisuje to gęstość: pole pod krzywą na danym przedziale równa się prawdopodobieństwu trafienia w ten przedział, a pole pod całą krzywą wynosi 1. To standardowy słownik z podręcznika Rossa "A First Course in Probability".
> - Kształt rozkładu streszczają cztery momenty: wartość oczekiwana (środek), wariancja (rozrzut), skośność (asymetria) oraz kurtoza (masa w ogonach). Dla rozkładu normalnego kurtoza wynosi dokładnie 3, a dla zwrotów rynkowych jest wyraźnie wyższa, co potwierdza katalog stylizowanych faktów Conta (2001).
> - Rozkład normalny kusi z powodu centralnego twierdzenia granicznego: suma wielu niezależnych składników o skończonej wariancji zmierza do krzywej Gaussa. Haczyk siedzi w założeniach, skończonej wariancji i niezależności, których zwroty finansowe nie spełniają.
> - Grube ogony to świat, w którym duże ruchy są znacznie częstsze, niż dopuszcza Gauss. Mandelbrot (1963), badając ceny bawełny, zaproponował rozkłady o indeksie ogona poniżej 2, czyli o nieskończonej wariancji. Późniejsze prace, w tym Cont (2001), znajdują ogon zwykle grubszy niż normalny, ale z indeksem powyżej 2, więc wariancja przeważnie jednak istnieje. Rozkład t Studenta pozwala sterować grubością ogona jedną liczbą, liczbą stopni swobody.
> - Prawdopodobieństwo warunkowe i twierdzenie Bayesa opisują aktualizację przekonań po nowej informacji. Osobno warto odróżnić prawdopodobieństwo od szans (odds): wartości p równej 0,8 odpowiadają szanse 4 do 1.

**Teza w jednym zdaniu:** Prawdopodobieństwo i rozkłady to precyzyjny język niepewności, a jego najważniejsza lekcja brzmi: wygodny rozkład normalny jest szczególnym przypadkiem, nie domyślnym stanem świata, bo rzeczywiste rozkłady zwrotów mają grubsze ogony, niż podpowiada krzywa Gaussa.

## Zmienna losowa, rozkład, gęstość

Cała matematyka rynku zaczyna się od jednego pojęcia: zmiennej losowej. To reguła, która wynikowi losowego zdarzenia przypisuje liczbę, na przykład jutrzejszej sesji wartość procentowej zmiany kursu. Rozkład tej zmiennej to pełen opis tego, jak prawdopodobne są poszczególne wartości. Dla wielkości skokowej wystarczy lista prawdopodobieństw, dla wielkości ciągłej, a taką jest zwrot, potrzebna jest gęstość. Gęstość nie podaje prawdopodobieństwa pojedynczej wartości (ono jest zerowe), lecz gęstość szansy wokół niej. Praktyczny sens ma dopiero pole pod krzywą: prawdopodobieństwo, że zwrot wpadnie w dany przedział, to pole pod gęstością nad tym przedziałem, a pole pod całą krzywą z definicji wynosi 1. Ten słownik, zmienna losowa, dystrybuanta, gęstość, jest punktem wyjścia każdego podręcznika rachunku prawdopodobieństwa, w tym klasycznego Rossa "A First Course in Probability".

```
Zmienna losowa X              reguła: wynik losowy → liczba
Dystrybuanta  F(x) = P(X ≤ x)  rośnie od 0 do 1
Gęstość       f(x) = F'(x)     P(a ≤ X ≤ b) = pole pod f na [a, b]
Normalizacja  ∫ f(x) dx = 1    pole pod całą krzywą równe 1
```

## Cztery momenty: środek, rozrzut, asymetria, ogony

Skoro rozkład to cała krzywa, potrzebne są liczby, które streszczają jej kształt. Służą do tego momenty. Wartość oczekiwana to środek ciężkości rozkładu, przeciętny wynik w długiej serii losowań. Wariancja mierzy rozrzut wokół tego środka, a jej pierwiastek, odchylenie standardowe, wraca do jednostek oryginalnej wielkości. Dwie kolejne liczby opisują kształt subtelniej. Skośność mówi o asymetrii: rozkład symetryczny ma skośność zero, dodatnia oznacza dłuższy ogon w prawo, ujemna w lewo. Kurtoza mierzy, ile masy siedzi w ogonach w porównaniu ze środkiem. Dla rozkładu normalnego kurtoza wynosi dokładnie 3 i to jest punkt odniesienia, a wartość powyżej 3 (leptokurtoza) oznacza grubsze ogony oraz wyższy, węższy szczyt. Warto zapamiętać jeden warunek: każdy z tych momentów istnieje tylko wtedy, gdy odpowiednia całka jest skończona. To pozornie techniczne zastrzeżenie okaże się kluczowe za dwie sekcje.

```
Wartość oczekiwana  μ  = E[X]                środek ciężkości rozkładu
Wariancja           σ² = E[(X − μ)²]         przeciętny kwadrat odchylenia
Skośność               = E[(X − μ)³] / σ³    asymetria (0 dla rozkładu symetrycznego)
Kurtoza                = E[(X − μ)⁴] / σ⁴    masa w ogonach (3 dla rozkładu normalnego)
```

## Rozkład normalny i dlaczego kusi

Wśród wszystkich rozkładów normalny zajmuje miejsce uprzywilejowane i nie bez powodu. Opisują go tylko dwie liczby, średnia i odchylenie standardowe, jest symetryczny, a rachunki z nim są wyjątkowo wygodne. Najgłębszy powód jego popularności to jednak centralne twierdzenie graniczne. Mówi ono, że suma wielu niezależnych, drobnych i porównywalnych składników o skończonej wariancji zmierza do rozkładu normalnego niezależnie od tego, jak wyglądał każdy pojedynczy składnik. Skoro cenę popycha mnóstwo drobnych, niezależnych bodźców, kuszący wniosek brzmi: zwrot powinien być w przybliżeniu normalny. To rozumowanie ma dokładnie dwa słabe punkty i oba są założeniami twierdzenia. Pierwsze to skończona wariancja każdego składnika. Drugie to niezależność. Rynek łamie jedno i drugie, dlatego most między pięknym twierdzeniem a rzeczywistością zwrotów okazuje się kruchy właśnie w tych dwóch miejscach.

```
Gęstość normalna
  f(x) = 1 / (σ√(2π)) · exp( −(x − μ)² / (2σ²) )
  opisana dwiema liczbami: μ (środek) oraz σ (szerokość)

Centralne twierdzenie graniczne (CTG)
  suma wielu niezależnych składników o skończonej wariancji
  → rozkład normalny, niezależnie od kształtu składników
```

## Gdzie Gauss zawodzi: grube ogony i prawa potęgowe

Gdy porówna się krzywą Gaussa z prawdziwym rozkładem zwrotów, rozjazd jest systematyczny i dotyczy ogonów. Ogon rozkładu normalnego opada wykładniczo, czyli zamiera błyskawicznie: ruch o kilka odchyleń standardowych jest pod nim zdarzeniem raz na wiele ludzkich żywotów. W danych takie ruchy wracają co kilka lat. Pierwszy pokazał to Mandelbrot (1963), analizując ceny bawełny: rozkład zmian cen był na tyle "dziki", że dopasował do niego rodzinę rozkładów stabilnych o ogonie potęgowym i indeksie poniżej 2, a taki indeks oznacza nieskończoną wariancję. Późniejsze prace złagodziły ten wniosek. Przeglądy empiryczne, w tym Cont (2001), znajdują indeks ogona zwykle skończony i większy od 2, więc wariancja przeważnie istnieje, choć ogon i tak jest znacznie grubszy niż u Gaussa. Zwroty siedzą gdzieś pomiędzy wygodnym rozkładem normalnym a dzikim rozkładem o nieskończonej wariancji. Empiryczny katalog tych odstępstw opisuje osobny tekst, [stylizowane fakty rynków](/dlogic-quant/2026/07/09/stylizowane-fakty-rynkow-grube-ogony/), a tutaj chodzi o ich matematyczny fundament. Konsekwencje grubych ogonów dla praktyki wielokrotnie podkreślał Taleb (2007): pod takim rozkładem o wyniku decyduje garść skrajnych zdarzeń, a nie spokojna większość obserwacji.

```
Ogon normalny opada wykładniczo:  P(X > x) ~ exp(−x² / 2σ²)   bardzo szybko
Ogon potęgowy opada wolniej:      P(|X| > x) ~ x^(−α)

α ≤ 2  ⇒  wariancja nieskończona   (Mandelbrot, 1963: ceny bawełny)
α > 2  ⇒  wariancja istnieje, lecz ogon i tak grubszy niż normalny   (Cont, 2001)
```

## Rozkład t Studenta: grubość ogona na jednej gałce

Do opisania grubego ogona bez natychmiastowego wpadania w nieskończoną wariancję dobrze nadaje się rozkład t Studenta. Ma jeden parametr kształtu, liczbę stopni swobody, oznaczaną ν, która działa jak pokrętło grubości ogona. Przy dużym ν rozkład t jest praktycznie nieodróżnialny od normalnego. W miarę zmniejszania ν ogony pęcznieją, a rozkład coraz wyraźniej odstaje od Gaussa. Wygodne jest to, że skrajne własności pojawiają się stopniowo i w policzalnych progach. Wariancja jest skończona dopiero dla ν większego od 2, a kurtoza dopiero dla ν większego od 4. Rozkład t o trzech stopniach swobody ma więc skończoną wariancję, ale nieskończoną kurtozę: średni rozrzut jest dobrze określony, lecz masa ogona formalnie wymyka się opisowi czwartym momentem. To wraca do zastrzeżenia z sekcji o momentach, że moment istnieje tylko wtedy, gdy jego całka jest skończona. Dlatego t Studenta jest w praktyce wygodnym modelem zwrotów i standardowym budulcem miar ryzyka odpornych na grube ogony. Poniższy schemat zestawia obie krzywe przy tej samej wariancji.

```
Rozkład t Studenta, parametr ν (liczba stopni swobody)

ν → ∞    zbiega do rozkładu normalnego (ogon cienki)
ν małe   ogon gruby, potęgowy: P(|X| > x) ~ x^(−ν)

wariancja skończona tylko dla ν > 2
kurtoza  skończona tylko dla ν > 4
przykład: t o ν = 3 ma skończoną wariancję, lecz nieskończoną kurtozę
```

<figure>
<svg viewBox="0 0 640 340" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="tarr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#e5484d" stroke-width="1.6"/></marker></defs><text x="20" y="26" font-size="14" fill="currentColor">Rozkład normalny kontra rozkład grubogonowy</text><text x="20" y="44" font-size="11" fill="currentColor" opacity="0.55">Ta sama wariancja. Grubogonowy ma wyższy szczyt i cięższe ogony.</text><path d="M 60,250 L 60,249.4 L 66,249.3 L 72,249.3 L 78,249.2 L 84,249.1 L 90,249.0 L 96,248.9 L 102,248.8 L 108,248.7 L 114,248.6 L 120,248.4 L 126,248.2 L 132,248.0 L 138,247.8 L 144,247.5 L 150,247.2 L 156,246.9 L 162,246.5 L 168,246.0 L 174,245.5 L 180,244.8 L 186,244.1 L 192,243.2 L 192,250 Z" fill="#e5484d" fill-opacity="0.28"/><path d="M 468,250 L 468,243.2 L 474,244.1 L 480,244.8 L 486,245.5 L 492,246.0 L 498,246.5 L 504,246.9 L 510,247.2 L 516,247.5 L 522,247.8 L 528,248.0 L 534,248.2 L 540,248.4 L 546,248.6 L 552,248.7 L 558,248.8 L 564,248.9 L 570,249.0 L 576,249.1 L 582,249.2 L 588,249.3 L 594,249.3 L 600,249.4 L 600,250 Z" fill="#e5484d" fill-opacity="0.28"/><line x1="60" y1="250" x2="600" y2="250" stroke="currentColor" stroke-width="1" opacity="0.4"/><line x1="330" y1="250" x2="330" y2="255" stroke="currentColor" stroke-width="1" opacity="0.4"/><text x="330" y="266" font-size="9.5" fill="currentColor" opacity="0.5" text-anchor="middle">średnia</text><polyline points="60,250.0 66,249.9 72,249.9 78,249.9 84,249.9 90,249.8 96,249.7 102,249.6 108,249.5 114,249.3 120,249.1 126,248.8 132,248.4 138,248.0 144,247.4 150,246.7 156,245.9 162,244.8 168,243.6 174,242.1 180,240.3 186,238.2 192,235.8 198,233.1 204,229.9 210,226.4 216,222.5 222,218.2 228,213.4 234,208.4 240,202.9 246,197.2 252,191.3 258,185.2 264,179.0 270,172.9 276,166.9 282,161.1 288,155.7 294,150.7 300,146.3 306,142.5 312,139.5 318,137.3 324,136.0 330,135.5 336,136.0 342,137.3 348,139.5 354,142.5 360,146.3 366,150.7 372,155.7 378,161.1 384,166.9 390,172.9 396,179.0 402,185.2 408,191.3 414,197.2 420,202.9 426,208.4 432,213.4 438,218.2 444,222.5 450,226.4 456,229.9 462,233.1 468,235.8 474,238.2 480,240.3 486,242.1 492,243.6 498,244.8 504,245.9 510,246.7 516,247.4 522,248.0 528,248.4 534,248.8 540,249.1 546,249.3 552,249.5 558,249.6 564,249.7 570,249.8 576,249.9 582,249.9 588,249.9 594,249.9 600,250.0" fill="none" stroke="#0b66c3" stroke-width="2"/><polyline points="60,249.4 66,249.3 72,249.3 78,249.2 84,249.1 90,249.0 96,248.9 102,248.8 108,248.7 114,248.6 120,248.4 126,248.2 132,248.0 138,247.8 144,247.5 150,247.2 156,246.9 162,246.5 168,246.0 174,245.5 180,244.8 186,244.1 192,243.2 198,242.1 204,240.9 210,239.4 216,237.7 222,235.6 228,233.1 234,230.0 240,226.3 246,221.9 252,216.5 258,210.0 264,202.2 270,193.0 276,182.1 282,169.4 288,155.0 294,139.3 300,122.6 306,106.0 312,90.7 318,78.3 324,70.1 330,67.3 336,70.1 342,78.3 348,90.7 354,106.0 360,122.6 366,139.3 372,155.0 378,169.4 384,182.1 390,193.0 396,202.2 402,210.0 408,216.5 414,221.9 420,226.3 426,230.0 432,233.1 438,235.6 444,237.7 450,239.4 456,240.9 462,242.1 468,243.2 474,244.1 480,244.8 486,245.5 492,246.0 498,246.5 504,246.9 510,247.2 516,247.5 522,247.8 528,248.0 534,248.2 540,248.4 546,248.6 552,248.7 558,248.8 564,248.9 570,249.0 576,249.1 582,249.2 588,249.3 594,249.3 600,249.4" fill="none" stroke="#e5484d" stroke-width="2"/><text x="330" y="59" font-size="12.5" fill="#e5484d" text-anchor="middle">rozkład grubogonowy</text><text x="410" y="176" font-size="12.5" fill="#0b66c3" text-anchor="middle">rozkład normalny</text><path d="M135 216 V245" fill="none" stroke="#e5484d" stroke-width="1.3" marker-end="url(#tarr)"/><text x="135" y="210" font-size="10.5" fill="#e5484d" text-anchor="middle">grubszy ogon</text><path d="M525 216 V245" fill="none" stroke="#e5484d" stroke-width="1.3" marker-end="url(#tarr)"/><text x="525" y="210" font-size="10.5" fill="#e5484d" text-anchor="middle">grubszy ogon</text><rect x="20" y="300" width="11" height="11" rx="2" fill="#0b66c3"/><text x="38" y="309" font-size="11" fill="currentColor" opacity="0.8">Rozkład normalny (Gauss): ogon opada wykładniczo, bardzo szybko.</text><rect x="20" y="319" width="11" height="11" rx="2" fill="#e5484d"/><text x="38" y="328" font-size="11" fill="currentColor" opacity="0.8">Rozkład grubogonowy (np. t Studenta): ogon potęgowy, opada wolniej.</text></svg>
<figcaption>Porównanie dwóch rozkładów o tej samej wariancji. Krzywa niebieska to rozkład normalny, czerwona to rozkład grubogonowy (schematyczny rozkład t Studenta o małej liczbie stopni swobody). Grubogonowy ma wyższy, węższy szczyt oraz cięższe ogony: skrajne odchylenia od środka są pod nim znacznie częstsze niż pod krzywą Gaussa. Zacieniony obszar przy osi zaznacza te ogony. Kształt schematyczny, dla ilustracji pojęcia, nie z konkretnych danych.</figcaption>
</figure>

## Prawdopodobieństwo warunkowe i Bayes w skrócie

Do tej pory mowa była o rozkładzie bezwarunkowym. Rynek dostarcza jednak informacji, a te zmieniają szanse. Prawdopodobieństwo warunkowe to szansa zdarzenia A przy założeniu, że zaszło zdarzenie B, i liczy się je jako iloraz prawdopodobieństwa obu zdarzeń naraz przez prawdopodobieństwo warunku. Twierdzenie Bayesa odwraca ten rachunek i pokazuje, jak zaktualizować przekonanie po nowej obserwacji: przekonanie sprzed informacji (a priori) mnoży się przez to, jak dobrze informacja pasuje do hipotezy, i normuje przez prawdopodobieństwo samej obserwacji. Jedna pułapka wraca tu regularnie, także przy interpretacji sygnałów rynkowych: wynik zależy nie tylko od trafności samego sygnału, lecz również od tego, jak częste było zdarzenie, zanim sygnał się pojawił (częstość bazowa). Pominięcie częstości bazowej to jeden z najczęściej opisywanych błędów rozumowania probabilistycznego, obecny zarówno w podręcznikach (Ross), jak i w literaturze o osądzie pod niepewnością.

```
Prawdopodobieństwo warunkowe   P(A | B) = P(A ∩ B) / P(B)
Twierdzenie Bayesa             P(A | B) = P(B | A) · P(A) / P(B)

P(A)      przekonanie przed nową informacją (a priori)
P(A | B)  przekonanie po informacji B (a posteriori)
```

## Prawdopodobieństwo a szanse

Na koniec rozróżnienie, które w mowie potocznej zlewa się w jedno, a w rachunku znaczy co innego: prawdopodobieństwo kontra szanse. Prawdopodobieństwo to liczba z przedziału od 0 do 1 (albo procent). Szanse (angielskie odds) to stosunek prawdopodobieństwa zdarzenia do prawdopodobieństwa jego braku, więc opisują to samo, lecz w innej skali. Prawdopodobieństwo 0,5 to szanse 1 do 1, prawdopodobieństwo 0,8 to szanse 4 do 1, a 0,9 to 9 do 1. Przejście w obie strony jest jednoznaczne, co pokazuje ostatni blok. Rozróżnienie nie jest pedanterią: kursy bukmacherskie i wiele intuicji o ryzyku podaje się w szansach, a mylenie ich z prawdopodobieństwem zniekształca ocenę. Szanse rosną nieliniowo: różnica między prawdopodobieństwem 0,90 a 0,99 to skok z 9 do 1 na 99 do 1, choć samo prawdopodobieństwo urosło tylko o dziewięć setnych.

```
Prawdopodobieństwo   p ∈ [0, 1]
Szanse (odds)        o = p / (1 − p)
Powrót do p          p = o / (1 + o)

p = 0,50  →  szanse 1 do 1
p = 0,80  →  szanse 4 do 1
p = 0,90  →  szanse 9 do 1
```

Materiał czysto edukacyjny, nie porada inwestycyjna. Powyższe pojęcia opisują język, w którym da się mówić o niepewności precyzyjnie, i nie zawierają żadnej obietnicy przewagi. Pewne jest tu wyłącznie to, co wynika z definicji i twierdzeń rachunku prawdopodobieństwa: rozkład opisuje kształt niepewności, momenty go streszczają, a rozkład normalny jest jednym z wielu rozkładów, wygodnym, lecz na rynku systematycznie zaniżającym wagę zdarzeń skrajnych.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
