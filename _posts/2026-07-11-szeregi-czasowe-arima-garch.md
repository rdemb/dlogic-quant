---
title: "Szeregi czasowe: AR, MA, ARIMA i GARCH"
description: "Szereg czasowy to obserwacje uporządkowane w czasie, a autokorelacja mierzy, na ile dzisiejsza wartość zależy od przeszłych. Model AR wiąże dzisiaj z wczoraj, model MA z wczorajszym szokiem, ARIMA łączy oba i dokłada różnicowanie, które sprowadza szereg do stacjonarności. Zwroty cen są prawie nieautoskorelowane, ale ich kwadraty już nie: to grupowanie zmienności, opisane przez modele ARCH (Engle 1982) i GARCH (Bollerslev 1986). Całość służy prognozie zmienności, czyli amplitudy ruchu, a nie jego kierunku. Koncepcje ze wzorami, jako kontekst ryzyka."
date: 2026-07-11 19:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Autokorelacja mówi, na ile przeszłość szeregu tłumaczy jego teraźniejszość. AR i MA to dwa sposoby zapisania tej pamięci, ARIMA je łączy i dokłada różnicowanie. Zwroty są prawie nieautoskorelowane, lecz ich kwadraty już nie, i właśnie to grupowanie zmienności modeluje GARCH. Narzędzie do prognozy zmienności, nie kierunku."
readingTime: 9
tags: [matematyka, "szeregi czasowe", ARIMA, GARCH, ARCH, zmienność, autokorelacja, stacjonarność, "Engle Bollerslev", "Box Jenkins", "Tsay", edukacja]
category: edukacja
---

> **W skrócie**
>
> - Szereg czasowy to dane uporządkowane w czasie, a autokorelacja mierzy, na ile wartość dzisiejsza jest powiązana z wcześniejszymi. Modelowanie tej zależności wymaga stacjonarności, czyli stałych w czasie własności statystycznych; szereg niestacjonarny zwykle najpierw się różnicuje. Pokrewnym pojęciem jest kointegracja: dwa niestacjonarne szeregi mogą mieć stacjonarną kombinację.
> - AR (autoregresja) zakłada, że dzisiejsza wartość zależy od poprzednich wartości, a MA (średnia ruchoma), że zależy od poprzednich losowych szoków. ARIMA łączy oba mechanizmy i dokłada różnicowanie, a całą metodykę spopularyzowali Box i Jenkins (1970).
> - Zwroty cen są w praktyce prawie nieautoskorelowane, ale ich kwadraty i wartości bezwzględne już nie. Duże ruchy sąsiadują z dużymi, małe z małymi: to grupowanie zmienności (volatility clustering).
> - Ten wzorzec opisują modele ARCH (Engle 1982) i GARCH (Bollerslev 1986), traktujące wariancję jako zmienną w czasie. Prognozują poziom zmienności, czyli jak duży będzie ruch, a nie w którą stronę. Parametry bywają niestabilne, więc model jest opisem struktury, nie wyrocznią.

**Teza w jednym zdaniu:** Modele szeregów czasowych, od AR i MA przez ARIMA po GARCH, opisują strukturę autokorelacji i zmiennej w czasie zmienności, co daje prognozę amplitudy ruchu i kontekst ryzyka, ale nie przewagę kierunkową.

## Szereg czasowy i autokorelacja

Szereg czasowy to ciąg obserwacji uporządkowanych w czasie: kursy zamknięcia, dzienne zwroty, dzienna zmienność. Cechą, która odróżnia go od zwykłej próbki liczb, jest kolejność. Sąsiedztwo w czasie niesie informację, a narzędziem, które ją mierzy, jest autokorelacja: korelacja szeregu z jego własną, przesuniętą w czasie kopią.

Autokorelacja rzędu k odpowiada na pytanie, na ile wartość sprzed k okresów pomaga przewidzieć wartość dzisiejszą. Zestaw tych współczynników dla kolejnych opóźnień tworzy funkcję autokorelacji (ACF), podstawowy obraz diagnostyczny każdego szeregu.

```
ρ_k = Cov(x_t, x_{t−k}) / Var(x_t)      # autokorelacja rzędu k

ρ_k ≈ 0 dla każdego k  →  brak liniowej pamięci
ρ_k ≠ 0                →  przeszłość niesie informację o teraźniejszości
```

Jeśli wszystkie współczynniki są bliskie zeru, szereg nie ma liniowej pamięci i jego przeszłe wartości nie pomagają liniowo przewidzieć przyszłych. Jeśli któreś odstają od zera, istnieje struktura, którą model może próbować opisać.

## Stacjonarność: warunek modelowania

Zanim jakikolwiek model autoregresyjny ma sens, szereg musi być stacjonarny. W wersji słabej oznacza to, że średnia i wariancja są stałe w czasie, a autokowariancja zależy tylko od odstępu między obserwacjami, nie od momentu pomiaru. Intuicja jest prosta: jeżeli reguły gry zmieniają się w czasie, to parametr oszacowany na przeszłości nie opisuje przyszłości.

Poziom kursu zwykle nie jest stacjonarny: ma trend, błądzi, nie wraca do stałej średniej. Dlatego modeluje się nie poziom, lecz jego zmiany. Operacja różnicowania, czyli przejście od ceny do zmiany ceny (a po logarytmie do zwrotu), zwykle usuwa trend i sprowadza szereg do postaci stacjonarnej.

```
Δx_t = x_t − x_{t−1}          # różnicowanie pierwszego rzędu
r_t  = ln(P_t) − ln(P_{t−1})  # log-zwrot: różnica logarytmu ceny
```

Z tym wiąże się kointegracja. Dwa szeregi mogą być z osobna niestacjonarne, a mimo to istnieje ich stacjonarna kombinacja liniowa; wtedy poruszają się razem, a odchylenie między nimi wraca do średniej. To fundament analizy par i koszyków, ale kierunek osobnego kursu pozostaje poza zasięgiem tej analizy. Kointegracja mówi o wspólnym ruchu, nie o tym, dokąd zmierza pojedynczy instrument.

## AR i MA: dwie postaci pamięci

Na stacjonarnym szeregu klasyczna analiza oferuje dwa elementarne mechanizmy pamięci. Model autoregresyjny AR zakłada, że dzisiejsza wartość jest ważoną sumą wartości poprzednich plus nowy losowy składnik. Krótko: dzisiaj zależy od wczoraj. Model średniej ruchomej MA zakłada co innego: dzisiejsza wartość zależy nie od poprzednich wartości, lecz od poprzednich losowych szoków, czyli od niespodzianek, które już się pojawiły. Krótko: dzisiaj zależy od wczorajszego zaskoczenia.

```
AR(1):  x_t = φ·x_{t−1} + ε_t        # dzisiaj zależy od wczorajszej wartości
MA(1):  x_t = ε_t + θ·ε_{t−1}        # dzisiaj zależy od wczorajszego szoku

ε_t = biały szum (niezależne losowe zakłócenia o średniej 0)
|φ| < 1  →  warunek stacjonarności AR(1)
```

Oba mechanizmy można połączyć w model ARMA, który jednocześnie pamięta poprzednie wartości i poprzednie szoki. Dobór rzędów, czyli ile opóźnień wziąć po każdej stronie, opiera się na kształcie funkcji autokorelacji i jej częściowego odpowiednika, co szczegółowo opisuje Tsay w Analysis of Financial Time Series.

## ARIMA: różnicowanie plus pamięć

ARIMA to ARMA rozszerzone o człon całkowania, oznaczany literą I (od integrated). W praktyce oznacza on wbudowane w model różnicowanie: zamiast opisywać surowy, niestacjonarny szereg, model najpierw różnicuje go tyle razy, ile trzeba, by stał się stacjonarny, a dopiero potem nakłada strukturę AR i MA.

Zapis ARIMA(p, d, q) streszcza trzy decyzje: p to liczba członów autoregresyjnych, d to liczba różnicowań, q to liczba członów średniej ruchomej. Metodyczny sposób doboru tych trzech liczb, od identyfikacji przez estymację po diagnostykę reszt, usystematyzowali Box i Jenkins (1970), i to ich nazwiska do dziś towarzyszą całej rodzinie.

```
ARIMA(p, d, q):
  p = człony AR (pamięć wartości)
  d = liczba różnicowań (droga do stacjonarności)
  q = człony MA (pamięć szoków)

d = 0  →  szereg już stacjonarny (czyste ARMA)
d = 1  →  różnicowanie raz: zmiany zamiast poziomu (typowe dla cen)
```

## Zwroty prawie nieautoskorelowane, kwadraty już nie

Zastosowanie tej maszynerii do zwrotów rynkowych prowadzi do wyniku powtarzanego w niezliczonych badaniach. Same zwroty są w praktyce prawie nieautoskorelowane: współczynniki ACF dla kolejnych opóźnień są bliskie zeru. Znak jutrzejszego zwrotu jest liniowo prawie niezależny od dzisiejszego, co jest zgodne z hipotezą o trudnej do pobicia efektywności rynku i jest głównym powodem, dla którego czysty model ARIMA rzadko daje użyteczną prognozę kierunku ceny.

Sytuacja zmienia się radykalnie, gdy zamiast zwrotów wziąć ich kwadraty albo wartości bezwzględne. Te szeregi są wyraźnie autoskorelowane: duży ruch dziś zapowiada podwyższone prawdopodobieństwo dużego ruchu jutro, niezależnie od jego znaku. Innymi słowy, nieprzewidywalny jest kierunek, ale nie skala. To zjawisko nazywa się grupowaniem zmienności (volatility clustering): okresy wzburzenia skupiają się razem, okresy spokoju również.

<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Grupowanie zmienności: naprzemienne pasma spokoju i burzy w szeregu zwrotów" style="width:100%;height:auto;display:block;margin:1.5rem auto">
  <rect x="180" y="30" width="150" height="240" fill="#e5484d" opacity="0.12"/>
  <rect x="518" y="30" width="124" height="240" fill="#e5484d" opacity="0.12"/>
  <line x1="40" y1="150" x2="730" y2="150" stroke="currentColor" stroke-opacity="0.45" stroke-width="1"/>
  <text x="32" y="154" font-size="12" fill="currentColor" fill-opacity="0.55" text-anchor="end">0</text>
  <g fill="#0b66c3">
    <rect x="48" y="142" width="8" height="8"/>
    <rect x="62" y="150" width="8" height="6"/>
    <rect x="76" y="138" width="8" height="12"/>
    <rect x="90" y="150" width="8" height="9"/>
    <rect x="104" y="143" width="8" height="7"/>
    <rect x="118" y="150" width="8" height="13"/>
    <rect x="132" y="140" width="8" height="10"/>
    <rect x="146" y="150" width="8" height="8"/>
    <rect x="160" y="136" width="8" height="14"/>
    <rect x="174" y="150" width="8" height="7"/>
    <rect x="188" y="120" width="8" height="30"/>
    <rect x="202" y="150" width="8" height="42"/>
    <rect x="216" y="98" width="8" height="52"/>
    <rect x="230" y="150" width="8" height="35"/>
    <rect x="244" y="102" width="8" height="48"/>
    <rect x="258" y="150" width="8" height="58"/>
    <rect x="272" y="110" width="8" height="40"/>
    <rect x="286" y="150" width="8" height="50"/>
    <rect x="300" y="117" width="8" height="33"/>
    <rect x="314" y="150" width="8" height="44"/>
    <rect x="328" y="141" width="8" height="9"/>
    <rect x="342" y="150" width="8" height="7"/>
    <rect x="356" y="138" width="8" height="12"/>
    <rect x="370" y="150" width="8" height="6"/>
    <rect x="384" y="139" width="8" height="11"/>
    <rect x="398" y="150" width="8" height="14"/>
    <rect x="412" y="142" width="8" height="8"/>
    <rect x="426" y="150" width="8" height="10"/>
    <rect x="440" y="137" width="8" height="13"/>
    <rect x="454" y="150" width="8" height="6"/>
    <rect x="468" y="141" width="8" height="9"/>
    <rect x="482" y="150" width="8" height="12"/>
    <rect x="496" y="143" width="8" height="7"/>
    <rect x="510" y="150" width="8" height="11"/>
    <rect x="524" y="114" width="8" height="36"/>
    <rect x="538" y="150" width="8" height="48"/>
    <rect x="552" y="96" width="8" height="54"/>
    <rect x="566" y="150" width="8" height="38"/>
    <rect x="580" y="104" width="8" height="46"/>
    <rect x="594" y="150" width="8" height="56"/>
    <rect x="608" y="108" width="8" height="42"/>
    <rect x="622" y="150" width="8" height="34"/>
    <rect x="636" y="142" width="8" height="8"/>
    <rect x="650" y="150" width="8" height="11"/>
    <rect x="664" y="143" width="8" height="7"/>
    <rect x="678" y="150" width="8" height="13"/>
    <rect x="692" y="141" width="8" height="9"/>
    <rect x="706" y="150" width="8" height="6"/>
  </g>
  <text x="115" y="288" font-size="12" fill="currentColor" fill-opacity="0.6" text-anchor="middle">spokój</text>
  <text x="255" y="288" font-size="12" fill="currentColor" fill-opacity="0.6" text-anchor="middle">burza</text>
  <text x="423" y="288" font-size="12" fill="currentColor" fill-opacity="0.6" text-anchor="middle">spokój</text>
  <text x="580" y="288" font-size="12" fill="currentColor" fill-opacity="0.6" text-anchor="middle">burza</text>
</svg>

Wykres pokazuje ten wzorzec: pasma dużych słupków (burza) przeplatają się z pasmami małych (spokój), zamiast być równomiernie rozrzucone. Gdyby kolejne zwroty były niezależne w czasie, duże i małe wahania mieszałyby się bez takich skupisk. Podświetlone tło zaznacza okresy podwyższonej zmienności, które w danych rynkowych trzymają się razem.

## ARCH i GARCH: wariancja zmienna w czasie

Klasyczne modele ARIMA zakładają, że wariancja składnika losowego jest stała. Grupowanie zmienności temu wprost przeczy. Odpowiedzią była nowa klasa modeli, w których wariancja sama jest zmienna w czasie i zależy od przeszłości.

Robert Engle (1982) zaproponował model ARCH (autoregressive conditional heteroskedasticity), w którym dzisiejsza wariancja zależy od kwadratów poprzednich szoków: po dużym zaskoczeniu rośnie, po serii małych opada. Tim Bollerslev (1986) uogólnił go do GARCH, dokładając zależność od poprzedniej wariancji, co pozwoliło opisać tę samą, uporczywą trwałość zmienności znacznie oszczędniejszą liczbą parametrów. Wkład Engle'a w modelowanie zmiennej w czasie wariancji został wyróżniony Nagrodą Nobla z ekonomii w 2003 roku.

```
GARCH(1,1):  σ²_t = ω + α·ε²_{t−1} + β·σ²_{t−1}

ω = kotwica (poziom długookresowy)
α = siła reakcji na ostatni szok
β = trwałość (pamięć) zmienności
warunek stabilności:   α + β < 1
poziom długookresowy:  σ²_∞ = ω / (1 − α − β)
```

Czyta się to jak opis bezwładności zmienności. Duży wczorajszy szok podbija dzisiejszą wariancję przez człon alfa, wysoka wczorajsza wariancja ciągnie się dalej przez człon beta, a ponieważ ich suma jest mniejsza od jedności, prognoza z czasem wraca do poziomu długookresowego. Po burzy rynek stopniowo się uspokaja, po nienaturalnym spokoju zmienność wraca do normy. Ta sama logika, którą widać na wykresie grupowania, jest tu zapisana jednym równaniem.

## Po co to inwestorowi: prognoza zmienności, nie kierunku

Wartość tej rodziny modeli jest konkretna, ale wąska. GARCH i pokrewne konstrukcje prognozują poziom zmienności, czyli jak duży będzie ruch, a nie w którą stronę. To model amplitudy, nie kierunku. Prognoza zmienności bywa użyteczna do skalowania wielkości pozycji, do wyznaczania szerokości poziomów obronnych czy do oceny, czy najbliższe sesje zapowiadają się spokojnie czy burzliwie, ale nie mówi, czy kurs pójdzie w górę czy w dół.

Ograniczenia trzeba wymienić wprost. Parametry ARIMA i GARCH szacuje się na danych historycznych i bywają niestabilne: to, co pasowało do zeszłego reżimu, potrafi rozjechać się w następnym. Model zakłada określoną postać zależności, a jeśli rzeczywistość od niej odbiega, prognoza się myli. Żaden z tych modeli nie jest wyrocznią; jest zwięzłym opisem struktury, która w danych była, przy założeniu, że jutro przypomni wczoraj. Tsay w Analysis of Financial Time Series traktuje je konsekwentnie jako narzędzia opisu i prognozy momentów drugiego rzędu, nie jako generatory sygnału kierunkowego.

Stąd jedno zdanie warte zapamiętania: modele szeregów czasowych opisują strukturę autokorelacji i zmienności, a nie przewagę kierunkową. Mówią, jak szeroko rynek może się ruszyć i jak ta szerokość zmienia się w czasie, a nie dokąd zmierza cena.

To materiał edukacyjny, nie porada inwestycyjna. Wzory podano w formie poglądowej, dla uporządkowania pojęć. Prognoza zmienności z modelu klasy GARCH opisuje możliwą amplitudę ruchu i jest kontekstem ryzyka, nie sygnałem kierunku ani obietnicą przewagi.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
