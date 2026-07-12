---
title: "Architektura automatu. Sygnał, ryzyko, egzekucja, log"
description: "Bot to nie jeden magiczny skrypt, tylko pięć warstw o rozłącznych odpowiedzialnościach: dane, sygnał, ryzyko, egzekucja, log. Sygnał ma być czystą, deterministyczną funkcją (te same dane, ta sama decyzja), bo tylko taką da się testować. Ryzyko to osobna bramka z dziennym limitem straty, kill-switchem i limitem pozycji, zwykle ważniejsza od samego sygnału. Do tego idempotencja i stan czytany z konta brokera jako źródło prawdy, pełny log każdej decyzji i twarda uwaga: architektura nie tworzy przewagi, tylko chroni przed katastrofą i ułatwia test."
date: 2026-07-12 11:00:00 +0200
eyebrow: "Programowanie · architektura"
dek: "Słowo bot sugeruje jeden magiczny skrypt. W praktyce bezpieczny automat to pięć warstw o jasnych granicach: czysty sygnał, który da się testować, osobna bramka ryzyka, która pilnuje konta, egzekucja odporna na poślizg i restart oraz log, z którego da się odtworzyć każdą decyzję. Tekst pokazuje ten szkielet w pseudokodzie i mówi wprost, czego architektura nie robi: nie tworzy edge."
readingTime: 8
tags: [programowanie, architektura, "zarządzanie ryzykiem", egzekucja, "kill-switch", bot, "separacja warstw", idempotencja, sygnał, log, "Ernest Chan", "López de Prado", quant]
category: edukacja
---

> **W skrócie**
>
> - **Pięć warstw, pięć odpowiedzialności:** dane, sygnał, ryzyko, egzekucja, log. Każda robi jedno. Granica między nimi to warunek testu, a nie ozdoba architektoniczna.
> - **Sygnał to czysta, deterministyczna funkcja** dane w decyzję, zero efektów ubocznych. Tylko taką da się przetestować i odtworzyć bit w bit. Chan (2013) całe rozdziały poświęca temu, jak look-ahead i inne wycieki przyszłości psują backtest.
> - **Ryzyko to osobna bramka, nie dodatek do sygnału:** dzienny limit straty, kill-switch, maksymalna liczba pozycji i pułap ekspozycji. Zwykle ważniejsza niż sam sygnał. López de Prado (2018) traktuje wielkość zakładu jako problem osobny od tego, w którą stronę grać.
> - **Idempotencja i stan:** bot musi przetrwać restart i nie zdublować zlecenia. Źródłem prawdy jest konto u brokera, nie zmienna w pamięci procesu.
> - **Architektura nie tworzy przewagi.** Chroni przed katastrofą i pozwala testować. Reguła bez źródła zarobku po zautomatyzowaniu zostaje tą samą regułą, tylko wykonywaną szybciej, również w traceniu.

**Teza w jednym zdaniu:** bezpieczny automat rozkłada się na pięć warstw o rozłącznych odpowiedzialnościach, z których sygnał ma być czystą funkcją, a ryzyko osobną bramką ważniejszą od sygnału, bo architektura nie tworzy przewagi, tylko decyduje o tym, czy system da się testować i czy jeden błąd nie wysadzi konta.

## Warstwa to nie ozdoba, tylko warunek testu

Początkujący pisze bota jako jeden skrypt: pobiera cenę, liczy wskaźnik, składa zlecenie, wszystko w jednej pętli, wszystko splecione. Taki kod bywa krótki i przez chwilę działa, ale ma jedną nieuleczalną wadę: nie da się go przetestować po kawałku ani odtworzyć, gdy coś pójdzie nie tak. Dlaczego bot kupił akurat tu? Pytanie zostaje bez odpowiedzi, bo decyzja, ryzyko i wysłanie zlecenia są zlepione w jedno zdarzenie.

Lekarstwem jest stara zasada inżynierii, separacja odpowiedzialności: każdy fragment robi dokładnie jedną rzecz i ma jedną granicę. W automacie transakcyjnym te granice są naturalne i jest ich pięć. To nie estetyka. To warunek, żeby dało się osobno przetestować logikę wejścia, osobno limity ryzyka i osobno składanie zleceń, oraz żeby po fakcie odtworzyć, co system widział i co z tym zrobił.

## Pięć warstw, pięć odpowiedzialności

```
warstwa      odpowiedzialność                          efekt uboczny
dane         pobierz i uporządkuj wejście              odczyt (wejście)
sygnał       dane → decyzja: kup / sprzedaj / nic      żaden (czysta funkcja)
ryzyko       decyzja + stan → zezwól albo odrzuć       żaden (czysta bramka)
egzekucja    zlecenie → fill u brokera                 zapis: zlecenia, sieć
log          zapisz każdą decyzję i zlecenie           zapis: dysk / baza
```

Klucz jest w prawej kolumnie. Efekty uboczne, czyli sięganie do sieci, zegara, dysku i konta brokera, mają być spchnięte na brzegi: do warstwy danych na wejściu oraz do egzekucji i logu na wyjściu. Środek łańcucha, sygnał i ryzyko, ma być czystym rachunkiem, który nic nie dotyka i niczego nie zmienia. To jedna decyzja projektowa, a odblokowuje testowalność całego systemu.

## Sygnał: czysta funkcja, dane wchodzą, decyzja wychodzi

Sygnał to serce, o którym wszyscy myślą, i zarazem warstwa, która ma być najgłupsza w sensie inżynierskim: czysta funkcja. Czysta znaczy dwie rzeczy. Po pierwsze deterministyczna: te same dane na wejściu zawsze dają tę samą decyzję na wyjściu. Po drugie bez efektów ubocznych: w środku nie ma sięgania do zegara, sieci, pliku ani losowania. Wynik zależy wyłącznie od argumentu.

```
# CZYSTA: te same 'dane' zawsze dają tę samą 'decyzję', zero I/O w środku
def signal(dane) -> Decyzja:
    # tylko rachunek na 'dane': bez zegara, bez sieci, bez pliku, bez losowania
    if warunek_wejscia(dane):
        return Decyzja(kierunek="kup", sila=1.0)
    return Decyzja(kierunek="nic")

# ANTYWZORZEC: decyzja zależy od ukrytego stanu i wejścia z sieci
def signal_zle():
    cena = broker.pobierz_cene()        # I/O w środku: wynik nie do powtórzenia
    if zegar.teraz().sekunda % 2: ...   # niedeterministyczne: testu brak
```

Po co ten rygor? Bo tylko czystą funkcję da się przetestować w izolacji: podajesz przygotowany kawałek historii, sprawdzasz, czy decyzja jest ta, której oczekujesz, i powtarzasz to tysiąc razy w sekundę bez rynku, bez brokera, bez czekania. Backtest takiej funkcji jest po prostu jej wywołaniem na danych z przeszłości. Chan (2013) pokazuje, że najgroźniejsze błędy backtestu, look-ahead bias i survivorship bias, biorą się właśnie z przecieku: gdy logika sygnału podejrzy dane z przyszłości albo stan, którego w danej chwili nie mogła znać. Czysta funkcja, która dostaje tylko jawnie podany wycinek danych, domyka tę furtkę z definicji.

## Ryzyko to osobna bramka, nie dodatek do sygnału

Tu jest najczęstszy błąd konstrukcyjny: wpleść zarządzanie ryzykiem w sygnał. Wtedy jedno i drugie testuje się razem, jedno i drugie psuje się razem. Ryzyko ma być osobną warstwą, bramką, przez którą przechodzi każda decyzja, zanim stanie się zleceniem. Bramka odpowiada na dwa pytania w kolejności: czy w ogóle wolno teraz zagrać, a jeśli tak, to jak dużą pozycją.

```
def risk_filter(decyzja, stan) -> Zlecenie:
    # najpierw twarde bramki, wielkość pozycji dopiero na końcu
    if stan.strata_dnia <= -DZIENNY_LIMIT:      # dzienny limit straty
        return STOP                             # kill-switch: koniec na dziś
    if stan.liczba_pozycji >= MAX_POZYCJI:      # limit liczby otwartych pozycji
        return STOP
    if stan.ekspozycja >= MAX_EKSPOZYCJI:       # limit łącznej ekspozycji
        return STOP
    if decyzja.kierunek == "nic":
        return STOP

    wielkosc = min(rozmiar_z_ryzyka(stan), MAX_LOT)   # sizing: ile postawić
    return Zlecenie(decyzja.kierunek, wielkosc)
```

Ta warstwa jest zwykle ważniejsza niż sam sygnał, bo decyduje o przetrwaniu, a nie o pojedynczym wejściu. López de Prado (2018) rozdziela wprost dwa problemy: w którą stronę grać oraz ile postawić, i pokazuje, że wielkość zakładu jest osobnym modelem, nie doklejką do prognozy. Powód jest arytmetyczny i bezlitosny: strata 50 procent kapitału wymaga potem zysku 100 procent, żeby wrócić do punktu wyjścia. Dlatego dzienny limit straty i kill-switch, który po jego przekroczeniu wygasza handel do końca dnia, chronią przed scenariuszem, w którym seria wpadek albo jeden zepsuty dzień zabiera konto, zanim sygnał w ogóle dostanie szansę się sprawdzić. Sygnał, który się myli, kosztuje jeden trade. Brak bramki ryzyka kosztuje całość.

## Idempotencja i stan: broker jest źródłem prawdy

Bot działa tygodniami, więc prędzej czy później padnie: restart procesu, zerwana sieć, reset maszyny. Pytanie nie brzmi, czy, tylko kiedy, i architektura ma to przewidywać. Śmiertelny błąd to trzymać stan pozycji w zmiennej w pamięci. Po restarcie ta zmienna jest pusta albo nieaktualna, a bot, który jej wierzy, złoży drugie zlecenie na pozycję, którą już ma, albo zapomni o otwartej ekspozycji.

```
# Źródłem prawdy jest konto u brokera, nie zmienna w pamięci procesu
stan = broker.pobierz_stan()             # pozycje, zlecenia, saldo od brokera

# Każde zlecenie ma powtarzalny identyfikator (idempotency key)
klucz = klucz_zlecenia(sygnal, czas_bara)   # ten sam sygnał → ten sam klucz
if not broker.zlecenie_istnieje(klucz):     # sprawdź u brokera, zanim wyślesz
    broker.zloz(zlecenie, klucz)            # po restarcie nie zdubluje pozycji
```

Dwie zasady załatwiają większość problemu. Pierwsza: źródłem prawdy jest konto u brokera, nie pamięć procesu. Stan czytamy od brokera na starcie każdej pętli, bo to on wie, co naprawdę jest otwarte. Druga: idempotencja. Każde zlecenie dostaje powtarzalny identyfikator wyliczony z sygnału i czasu bara, a przed wysłaniem bot sprawdza, czy zlecenie o tym kluczu już istnieje. Dzięki temu ta sama decyzja wykonana dwa razy, po restarcie albo po ponowieniu, tworzy jedną pozycję, nie dwie. To ten sam wzorzec, którego systemy płatnicze używają, żeby jedno kliknięcie nie obciążyło karty dwukrotnie.

## Egzekucja: poślizg, retry, potwierdzenie

Egzekucja to warstwa, która styka się z brutalnym światem, więc musi zakładać, że świat zawodzi. Zlecenie rynkowe nie wykona się po cenie z ekranu: między kliknięciem a fillem cena zdąży się ruszyć, i ten poślizg jest realnym kosztem, nie usterką. Zlecenie może też nie dojść, dojść z opóźnieniem albo zostać odrzucone. Dlatego egzekucja potrzebuje rozsądnego ponawiania z limitem prób oraz potwierdzenia: nie zakładaj, że zlecenie weszło, dopóki broker tego nie potwierdzi. Ponawianie musi współgrać z idempotencją z poprzedniej warstwy, w przeciwnym razie retry po cichym sukcesie zdubluje pozycję. Chan (2013) każe wyceniać koszty egzekucji pesymistycznie, zanim policzy się cokolwiek innego, bo cienką przewagę sygnału najłatwiej oddać właśnie tutaj, w spreadzie i poślizgu.

## Log: żeby dało się odtworzyć, co się stało

Log to nie dodatek na koniec, to warunek, żeby system dało się w ogóle debugować i sobie ufać. Zasada jest prosta: zapisz każdą decyzję i każde zlecenie, razem z wejściem, które je wywołało. Co widziała warstwa danych, co zwrócił sygnał, jak zadecydowała bramka ryzyka, co odpowiedział broker. Gdy po tygodniu pojawi się pytanie, dlaczego bot zrobił coś dziwnego, log pozwala odtworzyć tamtą chwilę zamiast zgadywać. Bez niego rozjazd między testem a produkcją, pierwszy sygnał, że coś pękło w feedzie albo w płynności, jest niewykrywalny, bo nie ma śladu, z czym porównać.

## Pętla: jak to się składa w całość

```
# Pętla: jedna odpowiedzialność na krok, stan zawsze świeży od brokera
while rynek_otwarty():
    dane     = pobierz_dane()               # 1. DANE
    stan     = broker.pobierz_stan()        # źródło prawdy, nie pamięć
    decyzja  = signal(dane)                 # 2. SYGNAŁ  (czysty, testowalny)
    zlecenie = risk_filter(decyzja, stan)   # 3. RYZYKO  (bramka + sizing)
    wynik    = execute(zlecenie, stan)      # 4. EGZEKUCJA (poślizg, retry)
    log(dane, decyzja, zlecenie, wynik)     # 5. LOG (pełny ślad decyzji)
    czekaj_na_kolejny_bar()
```

Cała architektura mieści się w tej pętli. Każdy krok to osobna funkcja z jedną odpowiedzialnością, a dane płyną w jedną stronę: od danych, przez sygnał i ryzyko, do egzekucji i logu. Taki układ testuje się warstwami: sygnał na historii bez brokera, bramkę ryzyka na wymyślonych stanach konta, egzekucję na atrapie brokera. Nie trzeba uruchamiać całości, żeby sprawdzić kawałek, i to jest praktyczny zysk z separacji.

## Minimalizm i granica autonomii

Pokusa idzie w dwie strony i obie są kosztowne. Pierwsza to przeinżynierowanie: warstwa abstrakcji na warstwie abstrakcji, konfigurowalne wszystko, framework, którego po miesiącu nikt nie rozumie. Im więcej kodu, tym więcej miejsc na cichy błąd i tym trudniej odpowiedzieć na proste pytanie, dlaczego bot złożył to zlecenie. Zasada odwrotna sprawdza się lepiej: jeden skrypt na jeden cel, granice widoczne gołym okiem, mało zależności. Pięć jasnych funkcji bije elegancki framework, bo mniej kodu to mniej powierzchni na katastrofę.

Druga pokusa jest groźniejsza: autonomia bez nadzoru. Automat, który sam składa zlecenia bez człowieka w pętli, jest bezpieczny tylko na tyle, na ile bezpieczne są jego bramki ryzyka, a te nigdy nie przewidzą wszystkiego: dziury w płynności, błędu feedu, rozjazdu między testem a produkcją. Dlatego kill-switch, dzienny limit i twardy pułap ekspozycji nie są opcją, tylko warunkiem wpuszczenia bota na żywo, a rozsądny start prowadzi przez tryb wyłącznie obserwacyjny i mikroskopijne wielkości, zanim cokolwiek urośnie. Nadzór człowieka nie jest oznaką słabości architektury, tylko ostatnią bramką, której żaden kod nie zastąpi.

To nie jest porada inwestycyjna ani gotowy system. To szkielet inżynierski: pokazuje, jak rozłożyć automat na warstwy, które da się testować osobno, i gdzie postawić bramki, żeby jeden błąd nie zabrał konta. Architektura nie tworzy przewagi. Reguła bez źródła zarobku, nawet idealnie oprogramowana, zostaje regułą bez źródła zarobku, tylko wykonywaną szybciej i bardziej konsekwentnie, również w traceniu. Bezpieczna struktura jest warunkiem koniecznym, nie wystarczającym: chroni przed katastrofą i pozwala uczciwie sprawdzić, czy edge w ogóle istnieje.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
