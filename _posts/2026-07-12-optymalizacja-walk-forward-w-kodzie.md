---
title: "Optymalizacja i walk-forward. Jak nie dopasować się do szumu"
description: "Optymalizacja parametrów na całej historii to najprostszy sposób na piękny i bezwartościowy backtest. Tekst tłumaczy, dlaczego pojedynczy wysoki pik na siatce jest podejrzany, a szerokie plateau wiarygodne, i pokazuje minimalny szkielet pętli walk-forward w Pythonie: strojenie na oknie, test na kolejnym, sklejenie wyników out-of-sample. Do tego purged i embargoed cross-validation według López de Prado (2018) oraz uczciwe miary: deflated Sharpe i Probability of Backtest Overfitting (Bailey, Borwein, López de Prado, Zhu, 2016)."
date: 2026-07-12 12:00:00 +0200
eyebrow: "Programowanie · walidacja"
dek: "Stroić parametry, nie oszukując samego siebie: różnica między pojedynczym pikiem a szerokim plateau, podział na in-sample i out-of-sample, walk-forward rolling kontra anchored oraz purged cross-validation dla danych z autokorelacją. Z minimalnym, poprawnym szkieletem pętli w Pythonie."
readingTime: 8
tags: [programowanie, "walk-forward", optymalizacja, overfitting, "cross-validation", "out-of-sample", "purged CV", "grid search", "López de Prado", Pardo, walidacja, backtest, PBO, quant]
category: edukacja
---

> **W skrócie**
>
> - Optymalizacja na całej historii nie tworzy przewagi, tylko dopasowuje parametry do szumu. Przy dostatecznie szerokiej siatce najlepszy wynik in-sample jest wysoki z samej konstrukcji, nawet gdy żadna konfiguracja nie ma edge'u (White, 2000; Bailey i López de Prado, 2014).
> - Pojedynczy wysoki pik na siatce parametrów jest podejrzany: sąsiednie ustawienia wypadają słabo, więc wynik wisi na jednej wartości i najpewniej jest przypadkiem. Szerokie plateau, gdzie sąsiedzi też działają, jest bardziej wiarygodne (Pardo, 2008).
> - Walk-forward: stroisz na oknie treningowym, oceniasz na kolejnym, przylegającym oknie testowym, przesuwasz się w przód, a jedynym uczciwym backtestem jest sklejona krzywa out-of-sample. Anchored trzyma stały początek, rolling przesuwa całe okno.
> - Zwykły k-fold przecieka informację przy danych finansowych, bo autokorelacja łączy sąsiadujące obserwacje. Lekarstwo to purged i embargoed cross-validation (López de Prado, 2018): wycięcie obserwacji na styku okien i luka bezpieczeństwa po teście.
> - Liczba prób podnosi poprzeczkę. Deflated Sharpe i Probability of Backtest Overfitting (Bailey, Borwein, López de Prado i Zhu, 2016) karzą za przeszukiwanie. Większość wyników znika out-of-sample i po kosztach.

**Teza w jednym zdaniu:** Optymalizacja nie tworzy przewagi, tylko ją rozpoznaje albo udaje, więc cały sens strojenia parametrów polega na tym, żeby oceniać je wyłącznie na danych, których procedura nie widziała podczas strojenia.

## Piękny backtest, który nic nie znaczy

Najprostszy sposób na wykres kapitału wyglądający jak marzenie jest zarazem najbardziej zwodniczy: wziąć całą dostępną historię, przepuścić przez nią siatkę kombinacji parametrów i wybrać tę, która wypadła najlepiej. Taka procedura nie szuka przewagi, tylko dopasowuje parametry do konkretnego przebiegu szumu w tych danych. Każda seria cenowa zawiera przypadkowe wzory: lokalne trendy, serie wygranych, układy świec, które nigdy się nie powtórzą. Optymalizacja na całej historii bierze te przypadki za regułę i stroi się pod nie.

Skala problemu rośnie z liczbą prób. Bailey i López de Prado pokazali w pracy o pseudomatematyce finansowej (2014), że przy dostatecznie wielu wypróbowanych konfiguracjach znalezienie strategii z imponującym wynikiem in-sample jest gwarantowane, nawet gdy wszystkie konfiguracje to czysty szum. Nie jest to ryzyko, tylko własność statystyki porządkowej: maksimum z wielu losowych wyników prawie zawsze leży daleko w prawym ogonie rozkładu. Dlatego pojedynczy backtest bez informacji o tym, ile wariantów odrzucono po drodze, jest liczbą bez mianownika. Więcej o samej arytmetyce przeszukiwania w osobnym materiale o [data snoopingu](/dlogic-quant/2026/07/05/data-snooping-jak-finanse-sie-oszukuja/).

## Krajobraz parametrów: pik kontra plateau

Optymalizacja daje nie jedną liczbę, ale całą powierzchnię: dla każdej kombinacji parametrów jakiś wynik. Ten krajobraz mówi więcej niż samo maksimum. Jeśli najlepszy rezultat to wąski, samotny pik, otoczony ustawieniami, które wypadają słabo, to znaczy, że całość wisi na jednej konkretnej wartości parametru. Przesunięcie o krok w bok psuje wszystko. Taki pik jest niemal na pewno artefaktem: dopasowaniem do przypadkowego układu w danych, a nie odbiciem trwałej struktury rynku.

Odwrotnie wygląda szerokie plateau: obszar, w którym cała grupa sąsiadujących ustawień daje podobnie przyzwoite wyniki. Wtedy rezultat nie zależy od zgadnięcia jednej magicznej liczby, a strategia znosi drobne zmiany parametrów bez rozpadu. Plateau nie gwarantuje przewagi, ale jest warunkiem koniecznym wiarygodności: mechanizm, który działa tylko przy jednym ustawieniu na tysiąc, prawie na pewno nie działa wcale. Pardo w "The Evaluation and Optimization of Trading Strategies" (2008) formułuje tę zasadę wprost: parametry wybiera się ze środka stabilnego regionu, nie z izolowanego szczytu.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Krajobraz parametrów: pik kontra plateau</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 150)" x="30" y="150" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">wynik in-sample (np. Sharpe)</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">wartość parametru</text><path d="M112 206 L140 150 L172 126 L215 122 L262 124 L302 121 L334 150 L366 200 L470 198 L500 150 L512 78 L524 150 L552 198 L600 201 L600 232 L112 232 Z" fill="#0b66c3" opacity="0.14" stroke="none"/><path d="M112 206 L140 150 L172 126 L215 122 L262 124 L302 121 L334 150 L366 200 L470 198 L500 150 L512 78 L524 150 L552 198 L600 201" fill="none" stroke="#0b66c3" stroke-width="2"/><text x="238" y="96" font-size="10.5" fill="#0b66c3" text-anchor="middle">szerokie plateau</text><text x="238" y="110" font-size="9.5" fill="currentColor" opacity="0.6" text-anchor="middle">sąsiednie ustawienia też działają</text><circle cx="512" cy="78" r="4.4" fill="#0b66c3"/><text x="512" y="66" font-size="10.5" fill="#0b66c3" text-anchor="middle">pojedynczy pik</text><text x="600" y="120" font-size="9.5" fill="currentColor" opacity="0.6" text-anchor="end">sąsiedzi słabi, wynik z przypadku</text></svg>
<figcaption>Optymalizacja daje całą powierzchnię wyników, nie jedną liczbę. Wąski, samotny pik zwykle jest dopasowaniem do szumu: sąsiednie ustawienia wypadają słabo, więc rezultat zależy od jednej wartości. Szerokie plateau, gdzie cała grupa sąsiadujących parametrów działa podobnie, jest bardziej wiarygodne, choć samo w sobie nie dowodzi przewagi.</figcaption>
</figure>

## In-sample, out-of-sample i walk-forward

Sam kształt krajobrazu nie wystarczy. Potrzebny jest podział danych, w którym strojenie i ocena nie dotykają tych samych obserwacji. Najprostsza wersja to rozcięcie historii na dwie części: in-sample, na której wolno stroić i przeszukiwać do woli, oraz out-of-sample, której nie wolno tknąć aż do jednej, ostatecznej oceny. Wynik na danych, których procedura nigdy nie widziała podczas strojenia, jest jedynym, który cokolwiek znaczy.

Walk-forward rozwija ten pomysł w ruchomą procedurę, bliższą temu, jak strategia działałaby na żywo. Bierzesz okno treningowe, stroisz na nim parametry, testujesz wybrane ustawienie na kolejnym, przylegającym oknie, zapisujesz wynik, po czym przesuwasz oba okna w przód i powtarzasz. Sklejone odcinki out-of-sample tworzą jedną krzywą, która symuluje coś prawdziwego: strateg co jakiś czas przestraja model na świeżych danych i handluje tym, co właśnie wyszło, a nie tym, co dopiero wyjdzie w przyszłości. Pardo (2008) nazywa relację między jakością in-sample a out-of-sample walk-forward efficiency i traktuje jej załamanie jako sygnał przeoptymalizowania.

Dwa warianty różnią się traktowaniem początku historii. Anchored, czyli kotwiczony, trzyma stały punkt startowy okna treningowego i pozwala mu tylko rosnąć, więc model widzi coraz więcej przeszłości. Rolling przesuwa całe okno o stałej długości, więc model zapomina najstarsze dane i uczy się głównie z niedawnej przeszłości. Anchored daje więcej danych i stabilniejsze estymaty, rolling szybciej reaguje na zmianę reżimu. Wybór zależy od tego, czy odległą historię uznaje się za wciąż informatywną, czy za nieaktualny, inny rynek.

## Dlaczego zwykły k-fold przecieka

Kusi, żeby zamiast walk-forward użyć klasycznej walidacji krzyżowej: potasować obserwacje, podzielić na k części, trenować na k minus jednej, testować na pozostałej i uśrednić. Na danych niezależnych to działa. Na danych finansowych przecieka informację. Powód to autokorelacja: sąsiadujące w czasie obserwacje są powiązane, bo etykieta zdarzenia często obejmuje okno kilku barów, a zmienność i trend przelewają się z jednej próbki na kolejną. Kiedy tasujesz, obserwacja z testu ląduje tuż obok niemal identycznej obserwacji w treningu, więc model ocenia się częściowo na tym, co już widział. Wynik wychodzi zawyżony.

López de Prado w "Advances in Financial Machine Learning" (2018) proponuje na to dwie poprawki. Purging: usunięcie z treningu wszystkich obserwacji, których okna czasowe nachodzą na okno testowe, żeby żadna informacja z testu nie wyciekła przez wspólny przedział. Embargo: dodatkowa luka bezpieczeństwa tuż po zbiorze testowym, wycinająca kolejne obserwacje, bo autokorelacja sięga też w przód. Ta sama książka uogólnia walk-forward do CPCV, kombinatorycznej wersji purged cross-validation, która testuje wiele różnych układów train i test naraz, dając rozkład wyników zamiast jednej ścieżki. W kodzie poniżej embargo pojawia się jako prosta luka między oknem treningowym a testowym.

## Ile prób, taka poprzeczka

Nawet uczciwy walk-forward można zepsuć, jeśli powtarza się go w kółko, zmieniając za każdym razem coś w strategii. Każda taka iteracja to kolejna próba, a liczba prób podnosi poprzeczkę, którą musi przebić wynik, żeby znaczył więcej niż szum. Dwa narzędzia karzą za to wprost. Deflated Sharpe Ratio koryguje Sharpe o liczbę wypróbowanych konfiguracji i kształt ogona, rozłożone na części w materiale o tym, [dlaczego twój Sharpe kłamie](/dlogic-quant/2026/07/09/dlaczego-twoj-sharpe-klamie-deflated-sharpe/). Probability of Backtest Overfitting, przedstawione przez Baileya, Borweina, López de Prado i Zhu (2016), szacuje odsetek podziałów, w których zwycięzca in-sample wypada poniżej mediany out-of-sample. Na czystym szumie wartość ta siada blisko połowy, dokładnie tak, jak powinno być przy braku jakiejkolwiek przewagi.

Historyczny fundament tej dyscypliny to Reality Check White'a (2000): bootstrapowy test, który porównuje najlepszą regułę nie z zerem, ale z rozkładem najlepszych wyników całego przeszukiwanego uniwersum. Wspólny wniosek tej literatury jest trzeźwiący: po uczciwej korekcie na liczbę prób i poza oknem, w którym dokonano wyboru, większość pozornych przewag znika.

## Szkielet pętli walk-forward

W kodzie cała procedura sprowadza się do kilkunastu linii. Kluczowe są cztery reguły: nie tasuj, bo kolejność czasu jest święta; stroją się parametry wyłącznie na trainie; ocena idzie tylko na niewidzianym tescie; sklejasz jedynie wyniki out-of-sample.

```
# Szkielet walk-forward (wersja rolling).
# Cel: nastroić parametry na oknie treningowym, ocenić je na
# kolejnym oknie testowym, przesunąć się w przód i skleić
# WYŁĄCZNIE wyniki out-of-sample.

def walk_forward(dane, siatka, len_train, len_test, embargo=0):
    oceny_oos = []                       # zbieramy tylko oceny OOS
    start = 0
    while start + len_train + embargo + len_test <= len(dane):

        # 1. podział na okna, bez tasowania: kolejność czasu jest święta
        train = dane[start : start + len_train]
        t0    = start + len_train + embargo   # embargo = luka po trainie
        test  = dane[t0 : t0 + len_test]

        # 2. strojenie tylko na trainie (grid search po siatce)
        best_p, best_is = None, float("-inf")
        for p in siatka:
            score = ocena(strategia(train, p))    # np. Sharpe in-sample
            if score > best_is:
                best_is, best_p = score, p

        # 3. ocena wybranych parametrów na NIEWIDZIANYM tescie
        oceny_oos.append(ocena(strategia(test, best_p)))

        # 4. przesunięcie okna o długość testu i powtórka
        start += len_test

    # 5. sklejona krzywa OOS to jedyny uczciwy backtest
    return sklej(oceny_oos)
```

Zmiana na wariant anchored to jedna linia: początek okna zostaje w miejscu, a rośnie tylko jego prawy koniec.

```
# Wariant anchored (kotwiczony): trening zawsze od początku historii.
train = dane[0 : start + len_train]      # zamiast dane[start : ...]
```

Pętla nie zawiera kosztów transakcyjnych ani poślizgu, a te potrafią zamienić dodatni wynik brutto w ujemny netto. W realnej walidacji funkcja ocena musi liczyć wynik po spreadzie, prowizji i realistycznym wypełnieniu, bo backtest bez kosztów mierzy fantazję, nie strategię.

## Puenta

Optymalizacja nie tworzy przewagi. W najlepszym razie ją rozpoznaje: wydobywa z danych strukturę, która istniała niezależnie od tego, że ktoś jej szukał. W najgorszym ją udaje: lepi z szumu kształt, który rozpada się przy pierwszym zetknięciu ze świeżymi danymi. Cała technika z tego tekstu, podział na in-sample i out-of-sample, walk-forward, purging, embargo, deflacja Sharpe'a, służy jednemu: odróżnieniu tych dwóch przypadków, zanim zaryzykuje się kapitał.

I trzeba być gotowym na najczęstszy wynik uczciwej walidacji, którym jest brak. Większość parametrów, które świeciły in-sample, gaśnie out-of-sample, a to, co przetrwa, często dobija koszt transakcyjny. To nie jest porażka metody, tylko jej działanie: uczciwa optymalizacja odsiewa złudzenia, a jej normalnym produktem jest odrzucenie, nie zielona krzywa kapitału.

To nie jest porada inwestycyjna ani zachęta do jakiejkolwiek strategii. To materiał o metodyce walidacji: jak stroić parametry, nie oszukując samego siebie, i dlaczego większość wyników nie przeżywa zderzenia z danymi out-of-sample i z kosztami.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
