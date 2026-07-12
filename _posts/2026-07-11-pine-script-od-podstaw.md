---
title: "Pine Script od podstaw: struktura i rysowanie"
description: "Jak zbudowany jest wskaźnik na TradingView, warstwa po warstwie. Model wykonania raz na bar, seria czasowa i historia przez operator [1], szkielet skryptu w Pine Script v6 z indicator() i plot(), wbudowane ta.sma oraz ta.crossover, a na koniec request.security i mechanizm repaintu przy zaglądaniu w przyszłość. Całość domyka kompletny, minimalny skrypt rysujący dwie średnie i znacznik ich przecięcia, opisany jako przykład rysowania, nie sygnał do handlu."
date: 2026-07-11 12:00:00 +0200
eyebrow: "Programowanie · Pine Script"
dek: "Wskaźnik na TradingView to nie obrazek, tylko program liczony osobno na każdej świecy. Ten tekst rozkłada jego budowę na czynniki pierwsze: od pojedynczej serii wartości, przez szkielet w Pine Script v6, po pułapkę repaintu przy danych z wyższego interwału. Wszystkie fakty o działaniu funkcji oparto na dokumentacji Pine Script (TradingView)."
readingTime: 8
tags: [programowanie, "Pine Script", TradingView, wskaźniki, repaint, "seria czasowa", "request.security", overlay, "analiza techniczna", edukacja]
category: edukacja
---

> **W skrócie**
>
> - Model wykonania: skrypt Pine liczy się raz na każdym barze, od najstarszego dostępnego do najnowszego. Na barze bieżącym w czasie rzeczywistym przelicza się na każdym ticku, co jest źródłem części zmian wartości w trakcie świecy.
> - Każda zmienna to seria: ciąg wartości, po jednej na bar. Operator [1] sięga o jeden bar wstecz, close[1] to zamknięcie poprzedniej świecy, a close[0] to bar bieżący.
> - Szkielet v6: linia //@version=6, wywołanie indicator(title, overlay), potem deklaracje i wywołania plot(). overlay = true rysuje na wykresie ceny, false w osobnym panelu.
> - Wbudowane funkcje żyją w przestrzeniach nazw: ta.sma, ta.ema, ta.crossover do obliczeń, input.int do parametrów, plot i plotshape do rysowania.
> - Największa pułapka to repaint. request.security z wyższego interwału z barmerge.lookahead_on i bez przesunięcia [1] wciąga do historii wartości, których na żywo jeszcze by nie było, przez co test wygląda lepiej niż rzeczywistość.

**Teza w jednym zdaniu:** Wskaźnik na TradingView to program wykonywany raz na każdej świecy na serii wartości, a jego rzetelność zależy od jednego pytania, czy w danym momencie korzysta wyłącznie z informacji, która byłaby wtedy dostępna.

## Model wykonania: raz na każdym barze

Zgodnie z dokumentacją Pine Script (TradingView) skrypt nie liczy się raz dla całego wykresu. Wykonuje się osobno na każdym barze, od najstarszego dostępnego do najnowszego, przesuwając się w prawo świeca po świecy. Na każdym barze historycznym przebiega dokładnie raz, korzystając z jego wartości otwarcia, maksimum, minimum, zamknięcia i wolumenu.

Wyjątkiem jest bar bieżący. Gdy wykonanie dojdzie do prawej krawędzi wykresu, a ten bar jest barem czasu rzeczywistego, skrypt przelicza się ponownie przy każdej aktualizacji ceny, czyli na każdym ticku. Wartości zmiennych są przed każdym takim przeliczeniem cofane do stanu z otwarcia bara, a zatwierdzane dopiero na jego zamknięciu. To jest powód, dla którego wskaźnik potrafi pokazywać jedną wartość w trakcie świecy, a inną po jej zamknięciu. Ta sama mechanika stoi za większością nieporozumień z repaintem opisanym niżej.

## Seria i historia przez operator [1]

Podstawową strukturą danych w Pine jest seria czasowa (series): ciąg wartości, po jednej na każdy bar. Nazwy takie jak close, high czy volume nie są pojedynczymi liczbami, tylko właśnie seriami. Gdy skrypt liczy się na danym barze, close oznacza zamknięcie tego bara, ale cała wcześniejsza historia pozostaje dostępna.

Sięga się po nią operatorem historii, czyli nawiasem kwadratowym z indeksem. Indeks 0 to bar bieżący, a liczby dodatnie cofają w przeszłość.

```
close       // zamkniecie bara biezacego (to samo co close[0])
close[1]    // zamkniecie poprzedniego bara
close[10]   // zamkniecie sprzed dziesieciu barow
high[1] - low[1]   // zasieg poprzedniej swiecy
```

Ten sam operator działa na dowolnej serii, także na wyniku własnych obliczeń. Dzięki temu skrypt może porównywać stan bieżący ze stanem sprzed jednego bara, co jest fundamentem wykrywania przecięć, do którego wrócimy przy funkcji ta.crossover.

## Szkielet skryptu w Pine Script v6

Każdy skrypt zaczyna się od komentarza z numerem wersji kompilatora. Dla najnowszej odsłony jest to //@version=6. Zaraz po nim pada deklaracja typu skryptu. Dla wskaźnika jest to funkcja indicator(), która ustawia jego nazwę i sposób wyświetlania.

```
//@version=6
indicator(title = "Moj pierwszy wskaznik", overlay = true)

// deklaracje zmiennych i obliczenia
srednia = ta.sma(close, 20)

// rysowanie
plot(srednia)
```

Parametr overlay decyduje o miejscu rysowania. Zgodnie z dokumentacją overlay = true nakłada wynik na wykres ceny, a overlay = false umieszcza go w osobnym panelu pod wykresem. Wskaźniki cenowe, jak średnie, zwykle idą na overlay, a oscylatory do osobnego panelu. Po deklaracji następują obliczenia i wywołania funkcji rysujących. Kolejność ma znaczenie o tyle, że zmiennej trzeba użyć po jej zdefiniowaniu.

## Wbudowane funkcje i parametry wejściowe

Biblioteka Pine grupuje funkcje w przestrzeniach nazw. Analiza techniczna mieszka w przestrzeni ta. Trzy funkcje wystarczą, by zbudować przykład z końca tekstu:

- ta.sma(source, length): prosta średnia ruchoma z length ostatnich wartości serii source.
- ta.ema(source, length): średnia wykładnicza, nadająca świeższym wartościom większą wagę.
- ta.crossover(source1, source2): wykrywa przecięcie pierwszej serii nad drugą.

Zgodnie z dokumentacją Pine Script (TradingView) ta.crossover(a, b) jest prawdziwe na tym barze, na którym a jest większe od b, a na barze poprzednim a było mniejsze lub równe b. Funkcja lustrzana ta.crossunder wykrywa przecięcie w dół. Obie w środku korzystają z operatora [1], bo porównują wartość bieżącą z wartością sprzed jednego bara.

```
sredniaSzybka = ta.sma(close, 20)
sredniaWolna  = ta.ema(close, 50)
wGore = ta.crossover(sredniaSzybka, sredniaWolna)   // prawda na barze przeciecia
```

Parametry oddaje się użytkownikowi przez funkcje z przestrzeni input. input.int() tworzy pole liczby całkowitej w oknie ustawień wskaźnika.

```
okres = input.int(defval = 20, title = "Okres sredniej", minval = 1)
srednia = ta.sma(close, okres)
```

Argument defval to wartość domyślna, title to etykieta pola, a minval ogranicza dół zakresu. Dzięki temu okresy średnich zmienia się jednym kliknięciem, bez ruszania kodu.

## Rysowanie: plot, plotshape, kolor i overlay

Samo obliczenie niczego jeszcze nie pokazuje. Za obraz odpowiadają funkcje rysujące. Najczęstsza to plot(), która kreśli serię jako ciągłą linię.

```
plot(srednia, title = "SMA 20", color = color.orange, linewidth = 2)
```

plotshape() nakłada znaczniki, na przykład trójkąty albo kółka, w miejscach, gdzie podana seria jest prawdziwa lub różna od na, czyli od wartości pustej. Kształt wybiera parametr style, a położenie względem świecy parametr location.

```
plotshape(wGore, title = "Sygnal", style = shape.triangleup,
     location = location.belowbar, color = color.green)
```

Kolory podaje się przez wbudowane stałe z przestrzeni color, jak color.green czy color.red, albo buduje funkcją color.new(kolor, przezroczystosc). Jedna zasada z dokumentacji bywa zaskoczeniem: funkcje plot() i plotshape() wywołuje się w głównym zasięgu skryptu, a nie wewnątrz bloków warunkowych if. Widocznością znacznika steruje się wartością serii, na przykład podając na tam, gdzie nic nie ma się pojawić.

## Wielointerwałowość: request.security, lookahead i repaint

Skrypt może sięgnąć po dane z innego symbolu lub innego interwału funkcją request.security(). Typowe zastosowanie to odczyt wartości z wyższej ramy czasowej, na przykład dziennej, na wykresie godzinowym.

I tu pojawia się najczęstsze źródło błędu, czyli repaint. Dokumentacja Pine Script (TradingView) definiuje repaint jako sytuację, w której skrypt zachowuje się inaczej na barach historycznych niż na barach czasu rzeczywistego, albo w której wartości historyczne zmieniają się po fakcie. Dane z wyższego interwału są klasycznym źródłem tego zjawiska, bo bar dzienny w trakcie dnia nie jest jeszcze zamknięty, a jego wartość dopiero się kształtuje.

Za sposób łączenia danych odpowiada parametr lookahead. Domyślnie ma wartość barmerge.lookahead_off. Ustawienie barmerge.lookahead_on sprawia, że funkcja pobiera wartość okresu z jego początku. Na barach historycznych oznacza to sięganie po liczbę, która w rzeczywistości jest znana dopiero na zamknięciu tego okresu, czyli zaglądanie w przyszłość. Test na danych historycznych wygląda wtedy lepiej, niż wypadłby na żywo, bo skrypt korzysta z informacji, której w danym momencie jeszcze by nie było. To nie jest przewaga, to artefakt.

Dokumentacja podaje bezpieczny wzorzec pobierania potwierdzonych wartości z wyższego interwału. Łączy on przesunięcie serii o jeden bar z włączonym lookahead:

```
// Ostatnia ZAMKNIETA wartosc dzienna, taka sama na historii i na zywo.
dzienne = request.security(syminfo.tickerid, "D", close[1], lookahead = barmerge.lookahead_on)
```

close[1] cofa odczyt do poprzedniego, już zamkniętego bara dziennego, a lookahead_on wyrównuje go spójnie na całej historii. Efekt to wartość potwierdzona, bez repaintu. Wersja odwrotna, z lookahead_on i bez przesunięcia [1], robi dokładnie to, przed czym ostrzega dokumentacja, czyli wciąga do przeszłości cenę z przyszłości:

```
// UWAGA: ta wersja zaglada w przyszlosc na barach historycznych.
zle = request.security(syminfo.tickerid, "D", close, lookahead = barmerge.lookahead_on)
```

Prosta reguła na koniec tego wątku: jeśli decyzja na danym barze zależy od wartości z wyższego interwału, ta wartość musi pochodzić z okresu już zamkniętego. Inaczej wynik testu opisuje świat, w którym znało się przyszłość.

## Kompletny przykład: dwie średnie i znacznik przecięcia

Poniższy skrypt składa wszystkie elementy w całość. Liczy dwie średnie, rysuje je na wykresie ceny i stawia znacznik tam, gdzie się przecinają. Jest to wyłącznie przykład rysowania i wykrywania zdarzenia na serii. Przecięcie średnich nie jest tu sygnałem do handlu ani rekomendacją wejścia czy wyjścia, a jedynie ilustracją tego, jak plotshape reaguje na warunek logiczny.

```
//@version=6
// Wskaznik edukacyjny: dwie srednie i znacznik ich przeciecia.
// Cel: pokazac budowe i rysowanie, nie generowac sygnal transakcyjny.
indicator(title = "Dwie srednie i znacznik przeciecia", shorttitle = "2 SMA edu", overlay = true)

// Parametry wejsciowe (uzytkownik zmienia je w oknie ustawien).
okresSzybki = input.int(defval = 20, title = "Okres sredniej szybkiej", minval = 1)
okresWolny  = input.int(defval = 50, title = "Okres sredniej wolnej",  minval = 1)

// Obliczenia. Kazda z tych zmiennych to seria: jedna wartosc na bar.
sredniaSzybka = ta.sma(close, okresSzybki)
sredniaWolna  = ta.sma(close, okresWolny)

// Wykrycie przeciecia. crossover korzysta wewnetrznie z operatora [1],
// porownujac stan biezacy ze stanem poprzedniego bara.
wGore = ta.crossover(sredniaSzybka, sredniaWolna)
wDol  = ta.crossunder(sredniaSzybka, sredniaWolna)

// Rysowanie obu srednich na wykresie ceny (overlay = true).
plot(sredniaSzybka, title = "SMA szybka", color = color.aqua,   linewidth = 2)
plot(sredniaWolna,  title = "SMA wolna",  color = color.orange, linewidth = 2)

// Znaczniki w miejscach przeciec. Ilustracja rysowania,
// nie rekomendacja wejscia ani wyjscia z rynku.
plotshape(wGore, title = "Przeciecie w gore", style = shape.triangleup,
     location = location.belowbar, color = color.green, size = size.small)
plotshape(wDol, title = "Przeciecie w dol", style = shape.triangledown,
     location = location.abovebar, color = color.red, size = size.small)
```

Warto prześledzić, jak przez ten skrypt przechodzi wszystko z wcześniejszych sekcji. input.int oddaje okresy użytkownikowi. ta.sma zwraca dwie serie, po jednej wartości na bar. ta.crossover i ta.crossunder porównują stan bieżący z poprzednim, więc pod spodem żyje operator [1]. plot kreśli linie na wykresie ceny, bo overlay jest ustawione na true, a plotshape stawia trójkąty tam, gdzie warunek jest prawdziwy. Żadna z tych funkcji nie ocenia rynku, one tylko liczą i rysują to, co wynika z danych.

Materiał czysto edukacyjny o strukturze skryptu, nie porada inwestycyjna. Opisane zachowanie funkcji oparto na dokumentacji Pine Script (TradingView), sekcje o modelu wykonania, serii czasowej, funkcjach wbudowanych, request.security i repaincie. Przykładowy kod służy pokazaniu, jak zbudowany jest wskaźnik, a nie generowaniu decyzji rynkowych. Rysowanie znacznika w miejscu przecięcia średnich jest tu wyłącznie ilustracją mechaniki plotshape.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
