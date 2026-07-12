---
title: "Walidacja modeli ML w finansach: dlaczego zwykły cross-validation przecieka"
description: "Walidacja krzyżowa dzieli dane na foldy i ocenia model na częściach, których nie widział podczas treningu. W finansach standardowy k-fold zawodzi, bo obserwacje nakładają się w czasie: etykiety z okien czasowych łączą trening z testem, więc oba dzielą tę samą informację i wynik wychodzi zawyżony. Tekst tłumaczy purging i embargo, kombinatoryczną walidację CPCV oraz związek z prawdopodobieństwem przeuczenia backtestu i deflated Sharpe według López de Prado (2018) oraz Baileya i López de Prado."
date: 2026-07-13 11:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
dek: "Dlaczego tasowanie danych finansowych przed walidacją krzyżową zawyża wynik, jak purging i embargo odcinają przeciek między treningiem a testem, i czym kombinatoryczna purged cross-validation różni się od pojedynczego przebiegu: rozkładem wyników zamiast jednej liczby, którą łatwo dobrać pod z góry znany rezultat."
readingTime: 9
tags: ["uczenie maszynowe", walidacja, "cross-validation", "purged k-fold", embargo, CPCV, overfitting, "López de Prado", PBO, "deflated Sharpe", edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Walidacja krzyżowa, k-fold, dzieli dane na k równych części, trenuje model na k minus jednej i ocenia na tej odłożonej, po czym obraca role i uśrednia. Każda obserwacja raz trafia do testu, więc estymata jakości opiera się na wielu podziałach, a nie na jednym arbitralnym cięciu.
> - Cała procedura zakłada, że obserwacje są niezależne. Dane rynkowe tego nie spełniają: etykieta powstaje z okna czasowego, a zmienność i trend przelewają się z próbki na próbkę, więc sąsiednie obserwacje dzielą informację. Po przetasowaniu prawie identyczna obserwacja trafia raz do treningu, raz do testu, i model ocenia się na tym, co już widział.
> - Efekt to przeciek, który zawyża wynik. Lekarstwo López de Prado (2018) ma dwie części. Purging usuwa z treningu obserwacje, których okna czasowe nachodzą na okno testowe. Embargo dokłada bufor tuż po tescie, bo autokorelacja przenosi informację także w przód.
> - CPCV, kombinatoryczna purged cross-validation z tej samej książki, testuje wiele układów treningu i testu naraz i zwraca rozkład wyników zamiast jednej liczby. Rozrzut ścieżek mówi więcej niż pojedynczy przebieg, który łatwo dobrać pod z góry znany rezultat.
> - Rozkład ścieżek zasila miary uczciwości: Probability of Backtest Overfitting oraz Deflated Sharpe (Bailey i López de Prado). Wniosek jest jeden: wynik walidacji jest wart tyle, ile poprawność procedury, a nie tyle, ile wynosi liczba na końcu.

**Teza w jednym zdaniu:** Walidacja krzyżowa w finansach mierzy przede wszystkim szczelność własnej procedury, bo jeśli trening i test dzielą informację z nakładających się okien czasowych, wynik wyjdzie wysoki niezależnie od tego, czy model czegokolwiek się nauczył.

## Po co dzieli się dane na foldy

Model oceniony na tych samych danych, na których się uczył, zawsze wygląda dobrze, bo potrafi je po prostu zapamiętać. Sens ma wyłącznie ocena na danych, których procedura nie widziała podczas treningu. Najprostszy podział to jedno cięcie historii na część treningową i testową. Ma dwie wady: marnuje dane, bo testu nie wolno użyć do nauki, a sama ocena wisi na jednym, arbitralnym punkcie podziału, który mógł akurat wypaść łaskawie albo surowo.

Walidacja krzyżowa, k-fold, rozwiązuje oba problemy. Dane dzieli się na k równych części. Model trenuje się na k minus jednej z nich i ocenia na tej odłożonej. Potem role się obracają, aż każda część raz posłuży za test, a wyniki z k przebiegów się uśrednia. Dzięki temu każda obserwacja raz trafia do oceny, cała historia pracuje, a estymata jakości opiera się na wielu podziałach zamiast jednego. W klasycznym uczeniu maszynowym, na zdjęciach czy tekstach, to złoty standard i działa, bo tam kolejność próbek nie niesie informacji, więc wolno je tasować.

## Gdzie pęka założenie w danych finansowych

k-fold w domyślnej postaci stoi na jednym założeniu: obserwacje są niezależne, więc potasowanie ich i rozrzucenie po foldach niczego nie psuje. Dane rynkowe łamią to założenie na dwa sposoby, oba opisane u López de Prado (2018).

Pierwszy to sposób budowania etykiet. W uczeniu maszynowym dla rynków etykieta rzadko dotyczy pojedynczej chwili. Zwykle opisuje, co stało się w oknie po zdarzeniu: czy w ciągu najbliższych barów cena dobiła do bariery zysku, czy do bariery straty, jaki był zwrot na horyzoncie. Dwie obserwacje, których okna się nakładają, opisują częściowo to samo przyszłe zdarzenie, więc dzielą wynik. Drugi to autokorelacja cech. Zmienność, trend i płynność zmieniają się wolno, więc próbki blisko siebie w czasie są do siebie podobne z samej natury rynku.

Efekt jest zawsze ten sam. Kiedy tasujesz i dzielisz na foldy, obserwacja z testu ląduje tuż obok prawie identycznej obserwacji, która została w treningu. Model rozpoznaje ją nie dlatego, że nauczył się reguły, tylko dlatego, że widział jej bliźniaka. Ocena wychodzi zawyżona, a im silniejsza autokorelacja i im dłuższe okna etykiet, tym większy przeciek. To jest sedno problemu: w finansach zwykły cross-validation nie mierzy jakości modelu, tylko to, jak bardzo trening i test się przenikają.

## Purging i embargo

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Purged k-fold na osi czasu: trening, test, purge, embargo</text><rect x="64" y="116" width="172" height="52" rx="3" fill="#0b66c3" opacity="0.16"/><rect x="64" y="116" width="172" height="52" rx="3" fill="none" stroke="#0b66c3" stroke-width="1.5"/><text x="150" y="147" font-size="11.5" fill="#0b66c3" text-anchor="middle">trening</text><rect x="236" y="116" width="22" height="52" fill="#e5484d" opacity="0.16"/><rect x="258" y="116" width="100" height="52" rx="3" fill="#1a9e6a" opacity="0.18"/><rect x="258" y="116" width="100" height="52" rx="3" fill="none" stroke="#1a9e6a" stroke-width="1.5"/><text x="308" y="147" font-size="11.5" fill="#1a9e6a" text-anchor="middle">test</text><rect x="358" y="116" width="22" height="52" fill="#e5484d" opacity="0.16"/><rect x="380" y="116" width="34" height="52" fill="#e5484d" opacity="0.09"/><rect x="414" y="116" width="162" height="52" rx="3" fill="#0b66c3" opacity="0.16"/><rect x="414" y="116" width="162" height="52" rx="3" fill="none" stroke="#0b66c3" stroke-width="1.5"/><text x="495" y="147" font-size="11.5" fill="#0b66c3" text-anchor="middle">trening</text><text x="308" y="104" font-size="10" fill="currentColor" opacity="0.7" text-anchor="middle">fold oceniany out-of-sample</text><line x1="397" y1="116" x2="397" y2="92" stroke="#e5484d" stroke-width="1" opacity="0.75"/><text x="397" y="86" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">embargo</text><line x1="247" y1="168" x2="247" y2="192" stroke="#e5484d" stroke-width="1" opacity="0.75"/><text x="247" y="206" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">purge</text><line x1="369" y1="168" x2="369" y2="192" stroke="#e5484d" stroke-width="1" opacity="0.75"/><text x="369" y="206" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">purge</text><line x1="64" y1="248" x2="580" y2="248" stroke="currentColor" stroke-width="1" opacity="0.55"/><path d="M572 244 L580 248 L572 252" fill="none" stroke="currentColor" stroke-width="1" opacity="0.55"/><text x="576" y="268" font-size="10.5" fill="currentColor" opacity="0.6" text-anchor="end">czas</text><text x="64" y="268" font-size="10" fill="currentColor" opacity="0.6">purge wycina trening nachodzący na test, embargo dokłada bufor po tescie</text></svg>
<figcaption>Trening otacza pojedynczy fold testowy z obu stron. Purging, czerwone pasy przy granicach testu, usuwa z treningu obserwacje, których okna czasowe nachodzą na okno testowe. Embargo, jaśniejszy pas po prawej, dokłada bufor tuż za testem, bo autokorelacja przenosi informację także w przód. Bez obu tych cięć sąsiadujące obserwacje przeciekają między treningiem a testem i zawyżają wynik.</figcaption>
</figure>

Naprawa nie polega na porzuceniu walidacji krzyżowej, tylko na uszczelnieniu jej granic. López de Prado (2018) proponuje dwie operacje, obie widoczne na osi czasu powyżej.

Purging to oczyszczenie treningu. Z każdego przebiegu usuwa się te obserwacje treningowe, których okna czasowe nachodzą na okno testu. Skoro etykieta rozciąga się na horyzont, obserwacja tuż przed testem albo tuż za nim może opisywać ten sam fragment przyszłości co obserwacja testowa. Wycięcie tych nakładek zamyka kanał, którym informacja z testu wyciekała do treningu. Na rysunku to czerwone pasy przy obu granicach bloku testowego.

Embargo to dodatkowy bufor. Nawet po purgingu obserwacje treningowe tuż po tescie mogą przeciekać, bo autokorelacja cech sięga dalej niż formalna długość okna etykiety. Embargo wycina niewielki pas treningu bezpośrednio za oknem testowym, tworząc martwą strefę, przez którą korelacja nie przenosi już informacji. Na rysunku to jaśniejszy czerwony pas po prawej stronie testu. Obie operacje mają jeden cel: sprawić, żeby ocena naprawdę dotyczyła danych, których model nie mógł podejrzeć.

## Kombinatoryczna walidacja: rozkład zamiast jednej liczby

Purged k-fold i walk-forward mają wspólne ograniczenie: dają jedną ścieżkę wyników out-of-sample, czyli jedną liczbę na końcu. Jedna liczba kusi, żeby ją poprawiać. Wystarczy dobrać taki podział na okna albo taki fragment historii, który akurat schlebia strategii, i pojedynczy przebieg zaczyna kłamać, nawet bez złej woli.

CPCV, combinatorial purged cross-validation, opisana przez López de Prado (2018), rozbija tę pojedynczość. Zamiast jednego podziału na trening i test bierze się N bloków czasu i rozważa wszystkie kombinacje wyboru k z nich jako test, a reszty jako trening. Każdy taki układ przechodzi normalne purging i embargo. Ponieważ kombinacji jest wiele, powstaje wiele ścieżek out-of-sample, a więc cały rozkład wyników, a nie jeden punkt.

```
# CPCV: N blokow czasu, k jako test, reszta jako trening.
# Zamiast jednej sciezki OOS powstaje ich wiele.
sciezki = []
for combo in kombinacje(bloki_1..N, wybierz=k):
    test  = polacz(combo)                    # k blokow jako zbior testowy
    train = pozostale_bloki
    train = purge(train, wzgledem=test)      # usun nakladajace sie okna
    train = embargo(train, po=test)          # martwa strefa za testem
    sciezki.append(ocena(model(train), test))

rozklad = zbierz(sciezki)   # patrzysz na mediane i rozrzut, nie na jedna liczbe
```

Rozkład mówi to, czego pojedynczy przebieg nie powie. Wąski rozrzut wokół przyzwoitej wartości to inna sytuacja niż szeroki rozrzut, w którym ta sama strategia raz wygląda świetnie, raz fatalnie. Trudniej też oszukać samego siebie, bo nie widać jednego wyniku do wypolerowania, tylko całą chmurę, w której skrajny przypadek nie ma już siły dowodu.

## Od rozkładu wyników do PBO i deflated Sharpe

Rozkład ścieżek to nie ozdoba, tylko wsad do miar, które wprost karzą za przeszukiwanie. Probability of Backtest Overfitting, przedstawione przez Baileya, Borweina, López de Prado i Zhu (2016), pyta o rzecz prostą: jak często konfiguracja, która wypadła najlepiej in-sample, ląduje poniżej mediany out-of-sample. Gdy strategia to czysty szum, odpowiedź siada blisko połowy, bo zwycięstwo in-sample nie niesie wtedy żadnej informacji o przyszłości. Im bliżej połowy, tym mocniejszy sygnał, że wybór najlepszego wariantu był losowaniem, nie odkryciem.

Druga miara to Deflated Sharpe Ratio, Bailey i López de Prado (2014). Koryguje ona zwykły współczynnik Sharpe o dwie rzeczy, które zawyżają go w praktyce: liczbę wypróbowanych konfiguracji oraz kształt rozkładu zwrotów, czyli skośność i grube ogony. Sens jest ten sam co przy PBO: im więcej prób stało za wynikiem, tym wyższa poprzeczka, którą musi przebić, żeby znaczył więcej niż szczęśliwe losowanie. Obie miary rozłożone są na części w osobnych materiałach o tym, [dlaczego twój Sharpe kłamie](/dlogic-quant/2026/07/09/dlaczego-twoj-sharpe-klamie-deflated-sharpe/), oraz o [optymalizacji i walk-forward](/dlogic-quant/2026/07/12/optymalizacja-walk-forward-w-kodzie/).

## Puenta: wynik jest wart tyle, ile procedura

Cała ta maszyneria nie tworzy przewagi. Purging, embargo i CPCV nie sprawią, że model zacznie zarabiać. Robią coś skromniejszego i ważniejszego: pilnują, żeby liczba na końcu walidacji znaczyła to, co ma znaczyć, a nie była echem przecieku między treningiem a testem. Wynik z walidacji, która przecieka, jest gorszy niż brak wyniku, bo niesie fałszywą pewność i pcha kapitał tam, gdzie stoi tylko złudzenie.

Stąd jedno pytanie, które warto zadać wobec każdego wyniku modelu, cudzego i własnego: jak wyglądała procedura walidacji. Czy etykiety miały okna, a jeśli tak, czy trening był z tych okien oczyszczony. Czy był embargo. Czy wynik to jedna ścieżka, czy rozkład. Ile konfiguracji wypróbowano, zanim padła ta jedna. Bez tych odpowiedzi Sharpe z walidacji krzyżowej jest liczbą bez mianownika, dokładnie jak pojedynczy backtest bez licznika prób. Ta sama myśl wraca w materiale o [data snoopingu](/dlogic-quant/2026/07/05/data-snooping-jak-finanse-sie-oszukuja/): nie liczy się sam wynik, tylko wynik w kontekście tego, ile i jak go szukano.

To nie jest porada inwestycyjna ani zachęta do jakiejkolwiek strategii. To materiał o metodyce: dlaczego standardowa walidacja krzyżowa zawodzi na danych finansowych i jak purging, embargo oraz kombinatoryczna purged cross-validation przywracają jej sens. Normalnym produktem uczciwej walidacji jest częściej odrzucenie modelu niż jego potwierdzenie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
