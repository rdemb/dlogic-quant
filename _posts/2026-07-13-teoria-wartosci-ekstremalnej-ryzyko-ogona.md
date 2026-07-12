---
title: "Teoria wartości ekstremalnej. Matematyka ryzyka ogona"
description: "Rozkład normalny opisuje środek danych, a nie ich skrajności, dlatego systematycznie zaniża prawdopodobieństwo oraz głębokość rzadkich, dużych strat. Teoria wartości ekstremalnej (EVT) to aparat skrojony do ogonów: twierdzenie Fishera-Tippetta-Gnedenki mówi, że rozkład unormowanych maksimów zbiega do uogólnionego rozkładu wartości ekstremalnych (GEV), a metoda przekroczeń progu (peaks over threshold) opisuje nadwyżki ponad wysoki próg uogólnionym rozkładem Pareto (GPD). Indeks ogona streszcza grubość ogona jedną liczbą i pozwala szacować VaR oraz Expected Shortfall z realnego kształtu ogona zamiast z krzywej Gaussa. Do tego ograniczenia metody: dobór progu, mała próba w ogonie i zmienność ogona w czasie. Źródła: Embrechts, Klüppelberg i Mikosch (1997) oraz McNeil, Frey i Embrechts (2005)."
date: 2026-07-13 12:00:00 +0200
eyebrow: "Edukacja · ryzyko"
dek: "Dlaczego rozkład normalny zaniża ryzyko rzadkich, dużych strat i czym zastąpić go w ogonie. Teoria wartości ekstremalnej: twierdzenie o rozkładzie maksimów (GEV), metoda przekroczeń progu z uogólnionym rozkładem Pareto (GPD), indeks ogona jako miara grubości oraz szacowanie VaR i Expected Shortfall z ogona, a nie z krzywej Gaussa. Na koniec granice metody: dobór progu, skąpe dane w ogonie i zmienność w czasie."
readingTime: 8
tags: [ryzyko, "teoria wartości ekstremalnej", EVT, "ryzyko ogona", VaR, "Expected Shortfall", "rozkład Pareto", GPD, "indeks ogona", "twierdzenie Fishera-Tippetta", "grube ogony", "zarządzanie ryzykiem", statystyka, quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Rozkład normalny opisuje środek danych, nie ich skrajności. Jego ogon opada wykładniczo, więc ruch o kilka odchyleń standardowych jest pod nim skrajnie rzadki, podczas gdy na rynku takie ruchy wracają co kilka lat. Kto liczy ryzyko dużej straty z krzywej Gaussa, ten je systematycznie zaniża.
> - Teoria wartości ekstremalnej (EVT) to dział statystyki skrojony do ogonów. Zamiast opisywać przeciętną obserwację, opisuje maksimum oraz przekroczenia progu, czyli dokładnie te zdarzenia, które decydują o ryzyku ruiny.
> - Twierdzenie Fishera-Tippetta-Gnedenki mówi, że rozkład unormowanych maksimów, o ile do czegokolwiek zbiega, musi zbiegać do uogólnionego rozkładu wartości ekstremalnych (GEV). Metoda przekroczeń progu (peaks over threshold) opisuje z kolei nadwyżki ponad wysoki próg uogólnionym rozkładem Pareto (GPD). Podają to Embrechts, Klüppelberg i Mikosch (1997).
> - Indeks ogona streszcza grubość ogona jedną liczbą: im większy parametr kształtu ξ, tym cięższy ogon, a moment rzędu p istnieje tylko wtedy, gdy p jest mniejsze od odwrotności ξ. Z dopasowanego ogona szacuje się VaR oraz Expected Shortfall bliżej prawdy niż z rozkładu normalnego (McNeil, Frey i Embrechts, 2005).
> - EVT nie jest wróżką. Jej wynik zależy od doboru progu, jest obarczony dużą niepewnością z powodu małej liczby obserwacji w ogonie i wymaga ostrożności, gdy zmienność zmienia się w czasie.

**Teza w jednym zdaniu:** Rozkład normalny modeluje środek rozkładu i milczy o jego skrajnościach, a teoria wartości ekstremalnej dostarcza aparatu, który opisuje sam ogon, twierdzeniem o rozkładzie maksimów oraz metodą przekroczeń progu, dzięki czemu VaR i Expected Shortfall można oszacować z rzeczywistego kształtu ogona, a nie z wygodnego założenia normalności.

## Dlaczego rozkład normalny zaniża ryzyko ogona

Ryzyko rzadkich, dużych strat mieszka w ogonie rozkładu zwrotów, a rozkład normalny opisuje ogon wyjątkowo źle. Gęstość Gaussa opada wykładniczo, z kwadratem odległości od środka w wykładniku, więc prawdopodobieństwo ruchu o kilka odchyleń standardowych spada astronomicznie szybko. Pod krzywą normalną dzienny spadek o pięć czy sześć sigma jest zdarzeniem rzadszym niż raz na wiele ludzkich żywotów. W danych rynkowych takie sesje wracają co kilka lat. Rozjazd nie jest drobnym błędem kalibracji, tylko różnicą jakościową między ogonem wykładniczym a ogonem potęgowym, znacznie grubszym. Matematyczny fundament tego zjawiska, prawa potęgowe oraz indeks ogona, rozwija osobny tekst o [rozkładach grubogonowych](/dlogic-quant/2026/07/11/prawdopodobienstwo-i-rozklady/). Konsekwencja praktyczna jest prosta: kto szacuje prawdopodobieństwo albo głębokość dużej straty, podkładając rozkład normalny, ten liczbę tę zaniża, i to najmocniej wtedy, gdy stawka jest najwyższa. Potrzebny jest aparat, który modeluje sam ogon, zamiast doklejać go do wygodnej krzywej opisującej środek.

## Teoria wartości ekstremalnej: aparat skrojony do ogonów

Klasyczna statystyka celuje w środek. Prawo wielkich liczb i centralne twierdzenie graniczne opisują średnią oraz sumę wielu obserwacji, czyli masę rozkładu skupioną wokół typowej wartości. Teoria wartości ekstremalnej odwraca pytanie: interesuje ją nie przeciętna, lecz rekord. Jak wygląda rozkład największej straty w długiej serii sesji? Jak zachowują się nieliczne obserwacje przekraczające wysoki próg? To są pytania o ogon, a nie o środek, i mają własne twierdzenia graniczne, niezależne od centralnego twierdzenia granicznego. Kanonicznym wykładem tej teorii jest monografia „Modelling Extremal Events" (Embrechts, Klüppelberg i Mikosch, 1997), a jej przełożenie na język zarządzania ryzykiem podaje „Quantitative Risk Management" (McNeil, Frey i Embrechts, 2005). Aparat stoi na dwóch filarach, które warto poznać po kolei: twierdzeniu o rozkładzie maksimów oraz metodzie przekroczeń progu.

## Twierdzenie Fishera-Tippetta-Gnedenki: prawo maksimów

Pierwszy filar dotyczy maksimów. Weź próbę niezależnych obserwacji o tym samym rozkładzie, podziel ją na bloki i z każdego bloku wybierz wartość największą. Twierdzenie Fishera-Tippetta-Gnedenki mówi coś zaskakująco silnego: jeśli rozkład tak wybranych, odpowiednio przeskalowanych maksimów w ogóle zbiega do jakiegoś nietrywialnego rozkładu granicznego, to tym granicznym rozkładem musi być jeden z trzech typów, a wszystkie trzy łączy jeden wzór, uogólniony rozkład wartości ekstremalnych (GEV). Trzy typy nazwano historycznie od nazwisk: Gumbela, Frécheta oraz Weibulla. Fisher i Tippett (1928) wskazali te trzy możliwości, a pełny dowód, że innych być nie może, podał później Gnedenko. O tym, który typ obowiązuje, decyduje jeden parametr kształtu, oznaczany ξ i zwany indeksem ekstremalnym.

```
Uogólniony rozkład wartości ekstremalnych (GEV)

G(x) = exp( −(1 + ξ·(x−μ)/σ)^(−1/ξ) )     dla ξ ≠ 0
G(x) = exp( −exp(−(x−μ)/σ) )               dla ξ = 0

μ = położenie,  σ = skala,  ξ = kształt (indeks ekstremalny)

ξ = 0   typ Gumbela    ogon lekki, wykładniczy (tu należy rozkład normalny)
ξ > 0   typ Frécheta   ogon ciężki, potęgowy (przypadek rynkowy)
ξ < 0   typ Weibulla   ogon ograniczony, skończony kraniec
```

Kluczowa jest interpretacja ξ. Rozkłady o lekkim, wykładniczym ogonie, w tym rozkład normalny, wpadają do typu Gumbela z ξ równym zero. Rozkłady o ciężkim, potęgowym ogonie, a takie pasują do zwrotów rynkowych, należą do typu Frécheta z ξ dodatnim. Ujemne ξ oznacza ogon urwany na skończonej wartości. Cała różnica między rynkiem spokojnym a groźnym daje się więc zapisać znakiem oraz wielkością jednej liczby.

## Metoda przekroczeń progu: POT i uogólniony rozkład Pareto

Podział na bloki i branie jednego maksimum z bloku marnuje dane, bo odrzuca pozostałe duże obserwacje. Drugi filar EVT jest pod tym względem oszczędniejszy. Metoda przekroczeń progu (peaks over threshold, POT) patrzy na wszystkie obserwacje, które przekraczają pewien wysoki próg u, i bada rozkład nadwyżek ponad ten próg. Twierdzenie Pickandsa oraz Balkemy i de Haana orzeka, że gdy próg rośnie, rozkład tych nadwyżek zbiega do jednej rodziny: uogólnionego rozkładu Pareto (GPD). Co istotne, parametr kształtu GPD to ten sam ξ co w twierdzeniu o maksimach, więc obie drogi mierzą tę samą grubość ogona. POT jest w praktyce podstawowym narzędziem szacowania ryzyka ogonowego w „Quantitative Risk Management" (McNeil, Frey i Embrechts, 2005), bo lepiej wykorzystuje skąpe dane z ogona.

```
Twierdzenie Pickandsa, Balkemy i de Haana (POT)

Dla progu u dostatecznie wysokiego rozkład nadwyżek Y = X − u,
pod warunkiem X > u, dąży do uogólnionego rozkładu Pareto (GPD):

H(y) = 1 − (1 + ξ·y/β)^(−1/ξ)     dla ξ ≠ 0
H(y) = 1 − exp(−y/β)              dla ξ = 0

β > 0 = skala,   ξ = kształt (ten sam indeks ogona co w GEV)
```

<figure>
<svg viewBox="0 0 640 340" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="potarr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#e5484d" stroke-width="1.6"/></marker></defs><text x="20" y="26" font-size="14" fill="currentColor">Ogon normalny kontra ogon gruby powyżej progu</text><text x="20" y="44" font-size="11" fill="currentColor" opacity="0.55">Powyżej progu rozkład normalny zanika wykładniczo, ogon gruby (GPD) opada wolniej i trzyma masę.</text><path d="M 160,213.5 L 171,218.4 L 182,222.5 L 194,226.1 L 205,229.1 L 216,231.7 L 228,234.0 L 239,235.9 L 250,237.6 L 261,239.0 L 272,240.3 L 284,241.4 L 295,242.3 L 306,243.1 L 318,243.9 L 329,244.5 L 340,245.1 L 351,245.5 L 362,246.0 L 374,246.4 L 385,246.7 L 396,247.0 L 408,247.3 L 419,247.5 L 430,247.7 L 441,247.9 L 452,248.1 L 464,248.2 L 475,248.4 L 486,248.5 L 498,248.6 L 509,248.7 L 520,248.8 L 531,248.9 L 542,249.0 L 554,249.1 L 565,249.1 L 576,249.2 L 588,249.2 L 599,249.3 L 610,249.3 L 610,250 L 160,250 Z" fill="#e5484d" fill-opacity="0.30"/><line x1="70" y1="250" x2="610" y2="250" stroke="currentColor" stroke-width="1" opacity="0.4"/><polyline points="70,138.4 81,151.8 92,164.2 104,175.3 115,185.2 126,193.9 138,201.4 149,207.9 160,213.5 171,218.4 182,222.5 194,226.1 205,229.1 216,231.7 228,234.0 239,235.9 250,237.6 261,239.0 272,240.3 284,241.4 295,242.3 306,243.1 318,243.9 329,244.5 340,245.1 351,245.5 362,246.0 374,246.4 385,246.7 396,247.0 408,247.3 419,247.5 430,247.7 441,247.9 452,248.1 464,248.2 475,248.4 486,248.5 498,248.6 509,248.7 520,248.8 531,248.9 542,249.0 554,249.1 565,249.1 576,249.2 588,249.2 599,249.3 610,249.3" fill="none" stroke="#e5484d" stroke-width="2"/><polyline points="70,119.3 81,135.6 92,151.4 104,166.3 115,180.1 126,192.5 138,203.4 149,212.9 160,220.8 171,227.5 182,232.9 194,237.2 205,240.5 216,243.1 228,245.1 239,246.5 250,247.6 261,248.4 272,248.9 284,249.3 295,249.5 306,249.7 318,249.8 329,249.9 340,249.9 351,250.0 362,250.0 374,250.0 385,250.0 396,250.0 408,250.0 419,250.0 430,250.0 441,250.0 452,250.0 464,250.0 475,250.0 486,250.0 498,250.0 509,250.0 520,250.0 531,250.0 542,250.0 554,250.0 565,250.0 576,250.0 588,250.0 599,250.0 610,250.0" fill="none" stroke="#0b66c3" stroke-width="2"/><line x1="160" y1="250" x2="160" y2="150" stroke="currentColor" stroke-width="1.4" stroke-dasharray="5 3" opacity="0.7"/><text x="160" y="143" font-size="12" fill="currentColor" opacity="0.75" text-anchor="middle">próg u</text><text x="160" y="266" font-size="9.5" fill="currentColor" opacity="0.5" text-anchor="middle">u</text><text x="72" y="78" font-size="12.5" fill="#0b66c3">rozkład normalny</text><text x="608" y="78" font-size="12.5" fill="#e5484d" text-anchor="end">ogon gruby (GPD)</text><text x="300" y="182" font-size="11" fill="#e5484d" opacity="0.95" text-anchor="middle">obszar przekroczeń</text><path d="M300 189 L288 244" fill="none" stroke="#e5484d" stroke-width="1.3" marker-end="url(#potarr)"/><rect x="20" y="300" width="11" height="11" rx="2" fill="#0b66c3"/><text x="38" y="309" font-size="11" fill="currentColor" opacity="0.8">Ogon normalny: opada wykładniczo, poza progiem masa znika bardzo szybko.</text><rect x="20" y="319" width="11" height="11" rx="2" fill="#e5484d"/><text x="38" y="328" font-size="11" fill="currentColor" opacity="0.8">Ogon gruby (GPD): opada potęgowo, masa przekroczeń pozostaje istotna.</text></svg>
<figcaption>Schemat prawego ogona rozkładu zwrotów. Pionowa przerywana linia to próg u, od którego liczy się przekroczenia (peaks over threshold). Krzywa niebieska to ogon rozkładu normalnego: opada wykładniczo, więc powyżej progu jego masa znika bardzo szybko. Krzywa czerwona to ogon gruby, opisany uogólnionym rozkładem Pareto: opada potęgowo, więc masa przekroczeń pozostaje istotna daleko w ogonie. Zacieniony obszar to właśnie te przekroczenia, których rozkład normalny niemal nie widzi. Kształt schematyczny, dla ilustracji pojęcia, nie z konkretnych danych.</figcaption>
</figure>

## Indeks ogona: jedna liczba o grubości

Parametr ξ jest sercem całej konstrukcji, bo streszcza grubość ogona jedną liczbą. Wygodnie myśleć o nim przez indeks ogona α, równy odwrotności ξ dla dodatniego ξ: ogon opada wtedy jak potęga, z wykładnikiem α. Im mniejsze α, czyli im większe ξ, tym wolniej gaśnie ogon i tym częstsze są ekstrema. Ta sama liczba rządzi istnieniem momentów. Moment rzędu p jest skończony tylko wtedy, gdy p jest mniejsze od α. Stąd twarde progi: przy α nie większym niż dwa wariancja jest nieskończona, a przy α nie większym niż cztery nieskończona jest kurtoza. Badania empiryczne lokują zwroty rynkowe w obszarze Frécheta, z dodatnim ξ, zwykle na tyle małym, że wariancja istnieje, lecz nie wszystkie wyższe momenty. Innymi słowy ogon jest gruby, ale nie aż tak dziki, by wariancja przestała mieć sens. Tę samą diagnozę, od strony praw potęgowych i indeksu ogona, rozwija przywołany wcześniej tekst o rozkładach grubogonowych.

```
Indeks ogona: parametr kształtu ξ oraz α = 1/ξ (dla ξ > 0)

ogon potęgowy:  P(X > x) ~ x^(−α) = x^(−1/ξ)   dla dużych x

większe ξ (mniejsze α)  ⇒  grubszy ogon
moment rzędu p istnieje tylko gdy  p < α

α ≤ 2  (ξ ≥ 1/2)  ⇒  wariancja nieskończona
α ≤ 4  (ξ ≥ 1/4)  ⇒  kurtoza nieskończona
```

## VaR i Expected Shortfall z EVT, nie z Gaussa

Po co to wszystko przy stole z ryzykiem? Bo z dopasowanego ogona GPD wyprowadza się wprost dwie miary, o których mówi osobny tekst o [miarach ryzyka VaR i Expected Shortfall](/dlogic-quant/2026/07/09/miary-ryzyka-var-expected-shortfall/). Zamiast zakładać normalność i czytać kwantyl z krzywej dzwonowej, metoda POT dopasowuje ogon do rzeczywistych przekroczeń progu, a potem podstawia go do wzorów na wysoki kwantyl (VaR) oraz średnią stratę w ogonie (Expected Shortfall). McNeil, Frey i Embrechts (2005) podają zamknięte estymatory obu miar.

```
Szacowanie ogona metodą POT (McNeil, Frey i Embrechts, 2005)

Nu = liczba przekroczeń progu u,   n = liczebność próby

P(X > x) ≈ (Nu/n)·(1 + ξ·(x−u)/β)^(−1/ξ)          x > u

VaR_α = u + (β/ξ)·[ ((n/Nu)·(1−α))^(−ξ) − 1 ]

ES_α  = VaR_α/(1−ξ) + (β − ξ·u)/(1−ξ)             dla ξ < 1

Stąd iloraz ogona:   ES_α / VaR_α → 1/(1−ξ)   gdy α → 1
o grubości ogona decyduje ξ, nie założenie normalności
```

Najważniejsza jest ostatnia linia. Przy rozkładzie normalnym stosunek Expected Shortfall do VaR jest ściśle ustalony i przy oddalaniu poziomu ufności dąży do jedynki, bo lekki ogon nie kryje głębokich strat za progiem. Przy ogonie modelowanym przez EVT ten sam stosunek dąży do odwrotności różnicy jeden minus ξ, czyli rośnie wraz z grubością ogona. To jest ilościowy zapis tego, co rozkład normalny przemilcza: im cięższy ogon, tym średnia strata w katastrofie bardziej przewyższa próg, od którego katastrofa się zaczyna. EVT wstawia tę różnicę wprost do liczby, zamiast zakładać, że jej nie ma.

## Ograniczenia: próg, mała próba, zmienność w czasie

Aparat jest potężny, lecz ma trzy realne słabości i uczciwy opis musi je wymienić. Pierwsza to dobór progu u. Zbyt niski próg wpuszcza do próby obserwacje ze środka rozkładu i psuje przybliżenie GPD, obciążając wynik. Zbyt wysoki zostawia garść przekroczeń i rozdmuchuje wariancję oszacowania. Kompromisu szuka się narzędziami diagnostycznymi, na przykład wykresem średniej nadwyżki, które opisują Embrechts, Klüppelberg i Mikosch (1997), i pozostaje w nim element osądu. Druga słabość jest wbudowana w naturę problemu: ekstremów jest z definicji mało, więc oszacowanie indeksu ξ opiera się na kilku, kilkunastu obserwacjach i bywa niepewne. Trzecia dotyczy czasu. Klasyczna EVT zakłada obserwacje niezależne i o stałym rozkładzie, tymczasem zmienność rynku skupia się w kłębach, a ogon puchnie i chudnie wraz z reżimem. Odpowiedzią jest EVT warunkowa: McNeil i Frey (2000) proponują najpierw odfiltrować zmienność modelem typu GARCH, a dopiero na resztach zastosować EVT, tak by ogon opisywać na danych pozbawionych grupowania zmienności.

## Co z tego wynika

EVT nie przepowiada, kiedy nadejdzie duża strata, ani nie obiecuje przewagi. Robi coś skromniejszego i pożyteczniejszego: zastępuje ciche założenie, że ogon jest cienki jak u Gaussa, jawnym modelem kształtu ogona, opartym na twierdzeniach granicznych dla ekstremów oraz na danych z samego ogona. Dzięki temu VaR i Expected Shortfall przestają dziedziczyć optymizm rozkładu normalnego, a zaczynają odzwierciedlać rzeczywistą grubość ogona, streszczoną jednym parametrem ξ. Kto rozumie ten parametr, ten wie, że różnica między liczbą ryzyka policzoną z krzywej dzwonowej a policzoną z ogona nie jest niuansem, lecz przepaścią, która ujawnia się dokładnie w dniu, w którym ogon się realizuje.

Materiał ma charakter wyłącznie edukacyjny i nie jest poradą inwestycyjną. Powyższe to definicje oraz twierdzenia teorii wartości ekstremalnej wraz ze źródłami, po to, by odróżnić ryzyko policzone z wygodnego założenia normalności od ryzyka policzonego z rzeczywistego kształtu ogona, zanim na tej różnicy postawi się pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
