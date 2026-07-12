---
title: "Stacjonarność i kointegracja: fundament pairs tradingu"
description: "Dlaczego ceny są zwykle niestacjonarne, a zwroty bliższe stacjonarnym; jak dwa niezależne błądzenia losowe dają wysokie R² bez żadnego związku (regresja pozorna, Granger i Newbold 1974); czym jest kointegracja (Engle i Granger 1987), gdy kombinacja liniowa dwóch niestacjonarnych szeregów jest stacjonarna i daje powrót spreadu do średniej; test ADF, procedura Engle Grangera, test Johansena (1991) oraz związek z pairs tradingiem (Gatev, Goetzmann, Rouwenhorst 2006). Z twardym zastrzeżeniem: kointegracja bywa niestabilna, pęka w czasie, a wynik często znika po kosztach."
date: 2026-07-10 13:00:00 +0200
eyebrow: "Edukacja · statystyka"
dek: "Fundament statystyczny pairs tradingu w jednym miejscu: różnica między szeregiem stacjonarnym a błądzeniem losowym, pułapka regresji pozornej, definicja kointegracji i testy, które ją sprawdzają. Bez hype, z wzorami i źródłami. Na końcu to, co przemilcza większość poradników: powrót spreadu do średniej to hipoteza do przetestowania, a nie własność rynku."
readingTime: 8
tags: [statystyka, kointegracja, stacjonarność, "pairs trading", "mean reversion", "Engle Granger", "regresja pozorna", "błądzenie losowe", "test ADF", "Granger Newbold", Johansen, "Gatev Goetzmann Rouwenhorst", quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Szereg stacjonarny ma stałą średnią i wariancję i wraca do średniej; błądzenie losowe nie ma żadnej z tych własności, bo szok zostaje w nim na zawsze, a wariancja rośnie z czasem. Ceny walut i akcji zachowują się zwykle jak szeregi niestacjonarne, oznaczane I(1), a ich zwroty są bliższe stacjonarnym, oznaczanym I(0).
> - Regresja jednego niestacjonarnego szeregu na drugim potrafi dać wysokie R² i pozornie istotne t-statystyki, nawet gdy oba szeregi są zupełnie niezależne. Granger i Newbold (1974) pokazali to symulacjami: fałszywe odrzucenia znacznie częstsze niż nominalne 5%, a sygnałem ostrzegawczym jest R² wyższe od statystyki Durbina-Watsona.
> - Kointegracja (Engle i Granger 1987) to sytuacja, w której dwa szeregi są niestacjonarne z osobna, ale pewna ich kombinacja liniowa jest stacjonarna. Ten stacjonarny spread wraca do stałej średniej i to jest teoretyczna podstawa pairs tradingu.
> - Sprawdza się to testami: ADF na pierwiastek jednostkowy (Dickey i Fuller 1979), dwukrokowa procedura Engle Grangera oraz wielorównaniowy test Johansena (1991) dla wielu wektorów kointegrujących naraz.
> - Empiryczny benchmark pairs tradingu to Gatev, Goetzmann i Rouwenhorst (2006). Twarde zastrzeżenie: kointegracja bywa niestabilna, relacja pęka przy zmianie reżimu, a udokumentowane zyski słabły w czasie i kurczą się po kosztach transakcyjnych. Powrót do średniej to hipoteza do przetestowania, nie pewnik.

**Teza w jednym zdaniu:** Pairs trading opiera się na kointegracji, czyli na tym, że stacjonarny spread dwóch niestacjonarnych cen wraca do stałej średniej; jest to jednak hipoteza statystyczna do przetestowania, a nie własność rynku, ponieważ zależność bywa pozorna, pęka przy zmianie reżimu i często nie przeżywa kosztów transakcyjnych.

## Stacjonarność, czyli fundament, o którym się nie mówi

Szereg czasowy jest stacjonarny w sensie słabym, kowariancyjnym, gdy jego średnia i wariancja nie zmieniają się w czasie, a autokowariancja zależy wyłącznie od odstępu między obserwacjami, nie od momentu, w którym się je bierze. Praktyczna konsekwencja jest jedna i ważna: taki szereg ma stałą średnią, wokół której się waha i do której wraca. Szok wytrąca go z równowagi tylko na chwilę.

Przeciwieństwem jest błądzenie losowe, kanoniczny przykład szeregu niestacjonarnego. Kolejna wartość to poprzednia plus losowy szok. Nie ma stałej średniej, wariancja rośnie z czasem, a każdy szok zostaje w szeregu na zawsze, bo wchodzi do poziomu i nigdy nie jest odrabiany. Nazywa się to szeregiem zintegrowanym rzędu pierwszego, w skrócie I(1): dopiero jego pierwsza różnica, czyli przyrost z okresu na okres, jest stacjonarna, czyli I(0).

```
Szereg stacjonarny (I(0)): stała średnia i wariancja w czasie,
    autokowariancja zależy tylko od odstępu, szereg wraca do średniej.

Błądzenie losowe (I(1)):   y_t = y_{t-1} + e_t
    brak stałej średniej, wariancja rośnie z czasem,
    szok e_t zostaje w poziomie na zawsze (brak powrotu do średniej).

Pierwsza różnica:          y_t − y_{t-1} = e_t   → stacjonarna (I(0))
```

## Ceny błądzą, zwroty są bliższe stacjonarności

Ceny instrumentów finansowych, kursy walut i indeksy zachowują się w praktyce jak szeregi niestacjonarne, bardzo blisko błądzenia losowego. To nie jest przypadek, tylko odbicie prostego faktu: gdyby poziom ceny miał przewidywalną, stałą średnią, do której wraca, przewidzenie kierunku byłoby trywialne, a rynek szybko by tę własność usunął. Dlatego surowe ceny zwykle traktuje się jako I(1). Ich logarytmiczne zwroty, czyli różnice logarytmów cen, są znacznie bliższe stacjonarnym, choć nie idealnie: zmienność skupia się w klastry, a ogony są grube. Bliższe stacjonarnym nie znaczy więc idealnie stacjonarne, znaczy tyle, że mają w miarę stałą średnią i wracają do niej, w odróżnieniu od poziomów.

Ten podział ma konkretne konsekwencje dla modelowania. Regresja i większość klasycznej statystyki zakłada stacjonarność zmiennych. Podane na wejściu dwa niestacjonarne poziomy potrafią złamać te założenia w spektakularny sposób, co prowadzi wprost do najstarszej pułapki w ekonometrii szeregów czasowych.

## Regresja pozorna: wysokie R² znikąd

Granger i Newbold (1974) pokazali rzecz, która do dziś jest kubłem zimnej wody. Wzięli dwa całkowicie niezależne błądzenia losowe, bez żadnego wspólnego czynnika, i regresowali jedno na drugim. Zgodnie z intuicją współczynnik powinien być nieistotny, a R² bliskie zeru. Symulacje Monte Carlo dały coś przeciwnego: wysokie R², wysokie, pozornie istotne t-statystyki i fałszywe odrzucenia hipotezy o braku związku znacznie częstsze niż nominalne 5%. Dwa niezależne trendy wyglądały jak silnie powiązana para.

Mechanizm jest prosty. Dwa szeregi, które dryfują, będą się poruszać w jakąś stronę jednocześnie po prostu dlatego, że każdy z nich dryfuje. Regresja odczytuje ten wspólny dryf jako zależność, choć żadnej nie ma. Sygnałem ostrzegawczym, który Granger i Newbold wskazali, jest reszta: reszty takiej regresji są silnie autoskorelowane, co widać po bardzo niskiej statystyce Durbina-Watsona. Stąd ich praktyczna reguła: jeśli R² jest wyższe od statystyki Durbina-Watsona, regresja jest prawdopodobnie pozorna.

```
Dwa NIEZALEŻNE błądzenia losowe x_t, y_t (brak wspólnego czynnika):
    regresja  y_t = a + b·x_t + u_t

Granger, Newbold (1974), symulacje Monte Carlo:
    wysokie R², pozornie istotne t   → fałszywe "odkrycia"
    znacznie częściej niż nominalne 5%
    reszty u_t silnie autoskorelowane → niski Durbin-Watson

Reguła ostrzegawcza:  R² > Durbin-Watson  → podejrzenie regresji pozornej
```

Wniosek jest niewygodny dla każdego, kto koreluje ceny: wysoka korelacja dwóch trendujących poziomów nie jest dowodem żadnego związku. Może być czystym artefaktem tego, że oba szeregi są niestacjonarne.

## Kointegracja: kiedy dwa błądzenia dzielą jeden spread

I tu wchodzi pojęcie, za które Clive Granger otrzymał później Nagrodę Nobla. Engle i Granger (1987) sformalizowali kointegrację: sytuację, w której dwa szeregi są niestacjonarne każdy z osobna, ale istnieje ich kombinacja liniowa, która jest stacjonarna. Innymi słowy oba poziomy błądzą, lecz błądzą razem, powiązane wspólnym trendem stochastycznym, tak że pewna ważona różnica między nimi ma stałą średnią i do niej wraca.

Ta ważona różnica to spread, a wagę nazywa się wektorem kointegrującym. Kluczowa różnica względem zwykłej korelacji jest taka: korelacja mówi o krótkoterminowym współruchu, zwykle zwrotów, i bywa pozorna. Kointegracja mówi o długoterminowym powiązaniu poziomów, które trzyma spread na uwięzi. To właśnie stacjonarność spreadu, a nie korelacja cen, jest teoretyczną podstawą powrotu do średniej.

```
Dwa szeregi I(1):  X_t, Y_t  (każdy z osobna niestacjonarny)

Kointegracja: istnieje β takie, że
    spread_t = Y_t − β·X_t   jest stacjonarny (I(0))

→ spread ma stałą średnią i wraca do niej (mean reversion)
β = wektor kointegrujący;   korelacja ≠ kointegracja
```

<figure>
<svg viewBox="0 0 640 340" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="26" font-size="13" fill="currentColor">Dwie niestacjonarne ceny, jeden stacjonarny spread</text><text x="34" y="48" font-size="11" fill="currentColor" opacity="0.6">poziomy cen (dryfują, każdy z osobna niestacjonarny)</text><line x1="80" y1="58" x2="80" y2="150" stroke="currentColor" stroke-width="1" opacity="0.5"/><line x1="80" y1="150" x2="600" y2="150" stroke="currentColor" stroke-width="1" opacity="0.5"/><path d="M80 138 L150 130 L220 128 L290 116 L360 108 L430 102 L500 96 L570 90 L600 84" fill="none" stroke="#0b66c3" stroke-width="2"/><path d="M80 142 L150 126 L220 132 L290 112 L360 106 L430 108 L500 92 L570 94 L600 80" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4" opacity="0.75"/><text x="610" y="86" font-size="10.5" fill="#0b66c3">Y</text><text x="610" y="74" font-size="10.5" fill="currentColor" opacity="0.75">X</text><text x="34" y="190" font-size="11" fill="currentColor" opacity="0.6">spread (stacjonarny, wraca do średniej)</text><line x1="80" y1="208" x2="80" y2="310" stroke="currentColor" stroke-width="1" opacity="0.5"/><line x1="80" y1="310" x2="600" y2="310" stroke="currentColor" stroke-width="1" opacity="0.5"/><line x1="80" y1="260" x2="600" y2="260" stroke="currentColor" stroke-width="1" opacity="0.55"/><line x1="80" y1="228" x2="600" y2="228" stroke="#0b66c3" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/><line x1="80" y1="292" x2="600" y2="292" stroke="#0b66c3" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/><path d="M80 258 L140 232 L200 262 L260 288 L320 256 L380 228 L440 264 L500 286 L560 256 L600 260" fill="none" stroke="#0b66c3" stroke-width="2"/><text x="598" y="224" font-size="10" fill="#0b66c3" opacity="0.8" text-anchor="end">górne 2σ</text><text x="598" y="256" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end">średnia</text><text x="598" y="306" font-size="10" fill="#0b66c3" opacity="0.8" text-anchor="end">dolne 2σ</text></svg>
<figcaption>Ilustracja poglądowa. Górny panel: dwie ceny, które dryfują w czasie i z osobna są niestacjonarne, bo błądzą i nie mają stałej średniej. Dolny panel: ich spread, czyli odpowiednio zważona różnica, jest stacjonarny i oscyluje wokół stałej średniej. Klasyczny wyzwalacz pairs tradingu to odchylenie spreadu o dwa odchylenia standardowe od średniej, zaznaczone jako pasma górne i dolne, z zakładem na powrót do średniej. Ten powrót jest hipotezą do przetestowania, a nie własnością rynku, i bywa, że relacja pęka.</figcaption>
</figure>

## Jak się to testuje: ADF, Engle Granger, Johansen

Stacjonarność szeregu sprawdza się testem pierwiastka jednostkowego. Najpopularniejszy to test Dickeya i Fullera (1979) oraz jego rozszerzona wersja ADF, która dokłada opóźnione różnice, żeby oczyścić test z autokorelacji. Hipoteza zerowa mówi, że szereg ma pierwiastek jednostkowy, czyli jest niestacjonarny. Odrzucenie tej hipotezy jest przesłanką za stacjonarnością, choć warto pamiętać, że brak odrzucenia nie dowodzi niestacjonarności, a jedynie jej nie wyklucza.

Na tym stoi dwukrokowa procedura Engle-Grangera. Krok pierwszy: regresja jednego poziomu na drugim, z której bierze się reszty będące estymatą spreadu. Krok drugi: test ADF na tych resztach. Jeśli reszty są stacjonarne, para jest kointegrowana. Metoda jest prosta, ale ma wadę: wynik zależy od tego, który szereg wybierze się jako objaśniany, a przy więcej niż dwóch instrumentach się nie skaluje.

Odpowiedzią jest test Johansena (1991), oparty na modelu wektorowej autoregresji i estymacji największej wiarygodności. Traktuje wszystkie szeregi symetrycznie, pozwala wykryć więcej niż jeden wektor kointegrujący naraz i podaje ich liczbę przez statystyki śladu oraz maksymalnej wartości własnej. Dla dwóch instrumentów wystarcza zwykle Engle-Granger, dla całego koszyka potrzebny jest Johansen.

```
Test ADF (Dickey, Fuller 1979 i wersja rozszerzona):
    H0: pierwiastek jednostkowy (szereg niestacjonarny)
    odrzucenie H0 → przesłanka za stacjonarnością

Engle-Granger (1987), dwa kroki:
    1. regresja Y_t na X_t     → reszty = estymata spreadu
    2. ADF na resztach         → stacjonarne reszty = kointegracja

Johansen (1991): model VAR, wiele wektorów kointegrujących naraz,
    statystyki śladu i maks. wartości własnej; symetryczny wobec zmiennych
```

## Od kointegracji do pairs tradingu

Empirycznym punktem odniesienia dla pairs tradingu jest praca Gatev, Goetzmann i Rouwenhorst (2006). Warto od razu zaznaczyć niuans: ich metoda jest dystansowa, nieparametryczna. Pary dobiera się, minimalizując sumę kwadratów odchyleń znormalizowanych cen w oknie formowania, a nie testem kointegracji. Wariant kointegracyjny, w którym spread buduje się wprost z wektora kointegrującego, to pokrewna, ale osobna rodzina. Obie łączy ta sama idea: znaleźć dwa instrumenty, których spread jest stacjonarny, i handlować jego odchyleniami.

Schemat jest mechaniczny. Po oknie formowania następuje okno handlu. Pozycję otwiera się, gdy spread rozjedzie się o umowne dwa odchylenia standardowe od średniej, grając na powrót, i zamyka przy powrocie do średniej. Badanie udokumentowało dodatnie średnie zwroty tej reguły na akcjach amerykańskich w długim okresie, co uczyniło je najczęściej cytowanym dowodem, że w spreadach bywa coś realnego.

```
Pairs trading (schemat dystansowy, Gatev i in. 2006):
    okno formowania → dobór par: min. suma kwadratów
                      odchyleń znormalizowanych cen
    okno handlu:
        spread odchyla się o 2σ od średniej  → otwarcie (zakład na powrót)
        spread wraca do średniej             → zamknięcie

Uwaga: to metoda dystansowa, nie test kointegracji;
wariant kointegracyjny (spread z β) = osobna rodzina.
```

## Dlaczego to pęka i znika po kosztach

Tu kończy się teoria, a zaczyna dyscyplina. Kointegracja nie jest własnością wieczną. Relacja, która trzymała się w próbie historycznej, potrafi pęknąć poza próbą, gdy zmienia się reżim, fundamenty jednej ze stron albo struktura rynku. Wektor kointegrujący sam dryfuje i wymaga ponownej estymacji w oknie kroczącym, a strukturalne złamanie zależności zamienia rzekomo stacjonarny spread w kolejne błądzenie losowe, tyle że odkryte za późno.

Dochodzi problem wielokrotnego testowania, będący echem regresji pozornej. Przeszukanie setek par w poszukiwaniu tej najlepiej kointegrowanej to ta sama statystyka porządkowa, która produkuje fałszywe odkrycia: część znalezionych zależności będzie artefaktem samego przeszukiwania, nie realnym powiązaniem. Bez korekty na liczbę prób łatwo wziąć szum za sygnał, dokładnie tak jak w symulacjach Grangera i Newbolda.

Najtwardszy filtr jest jednak kosztowy. Powrót spreadu do średniej to często kilka albo kilkanaście pipsów, ułamek procenta, a każde wejście i wyjście płaci spread, prowizję i poślizg, w dodatku po obu nogach pary naraz. Udokumentowane w literaturze zyski pairs tradingu słabły w kolejnych podokresach, w miarę jak rynek stawał się bardziej efektywny, a po realistycznych kosztach transakcyjnych przewaga w wielu badaniach zanika. Dlatego stacjonarność spreadu, choćby przeszła test ADF, jest początkiem analizy, nie jej końcem: mówi tylko, że powrót do średniej jest hipotezą wartą przetestowania, a nie że da się na nim zarobić.

Materiał czysto edukacyjny, nie porada inwestycyjna ani sygnał. Kointegracja to model, a nie gwarancja: bywa niestabilna, pęka w czasie, a wynik strategii opartej na powrocie spreadu do średniej często znika po uwzględnieniu kosztów. Pewne jest tu wyłącznie to, że każdą taką zależność trzeba przetestować, i że zwykle łatwiej ją odrzucić, niż potwierdzić.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
