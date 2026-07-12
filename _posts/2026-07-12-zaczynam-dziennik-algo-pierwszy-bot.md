---
title: "Zaczynam dziennik algo. Pierwszy bot i zasady, które go pilnują"
description: "Nowa sekcja: jawny dziennik budowy własnych systemów algorytmicznych. Pierwszy bot działa na rynku krypto z egzekucją przez MetaTrader 5, ale sedno wpisu to nie strategia, tylko bezpieczniki i jedna zasada, która ustawia całą resztę: backtest nie jest dowodem, dowodem jest wyłącznie forward w czasie rzeczywistym, po kosztach."
date: 2026-07-12 16:00:00 +0200
eyebrow: "Moje Algo · dziennik"
dek: "Po co osobna sekcja o botach, dlaczego zaczyna się od bezpieczników, a nie od sygnału, i czemu pierwszy system długo chodzi na papierze zanim dotknie realnego konta. Zapis procesu, nie oferta i nie obietnica wyniku."
readingTime: 5
tags: ["moje algo", bot, automatyzacja, "zarządzanie ryzykiem", walidacja, forward, "kill-switch", dziennik]
category: algo
---

> **W skrócie**
>
> - Ta sekcja to dziennik budowy moich własnych systemów algorytmicznych, pisany na bieżąco. Nie sygnały, nie oferta, nie kurs. Zapis decyzji i błędów.
> - Pierwszy bot działa na rynku krypto, z egzekucją przez MetaTrader 5. Opisuję tu jego szkielet i zasady bezpieczeństwa, a nie strategię wejścia.
> - Najważniejsze w bocie nie jest to, kiedy wchodzi, tylko czego mu nie wolno. Dzienny limit straty, kill-switch od szczytu kapitału i jedna pozycja na instrument są wpisane na twardo.
> - Backtest, choćby najładniejszy, nie jest dowodem przewagi. Jedyny dowód, który uznaję, to forward w czasie rzeczywistym, po realnych kosztach. Dlatego bot najpierw długo liczy na papierze.
> - Bramka wejścia na realne pieniądze jest zapisana z góry i nie zmienia się po fakcie. Przełączenie wymaga dwóch świadomych, ręcznych kroków.

**Teza w jednym zdaniu:** Wartość systemu algorytmicznego mierzy się nie urodą krzywej z przeszłości, tylko tym, jak jest zabezpieczony przed katastrofą i czy przetrwał uczciwy test na danych, których wcześniej nie widział.

## Po co osobna sekcja

Reszta tego portalu jest bezosobowa i edukacyjna, celowo. Ta zakładka jest wyjątkiem: to jawny dziennik tego, co sam buduję. Będę tu zapisywał kolejne systemy, ich założenia, potknięcia i to, co z nich wyszło albo nie wyszło. Piszę to, bo uważam, że proces jest ciekawszy i uczciwszy niż gotowa teza, a publiczny zapis wymusza dyscyplinę. Nie znajdziesz tu sygnałów do kopiowania ani niczego na sprzedaż.

## Dlaczego w ogóle algorytm

Mechaniczna egzekucja usuwa część błędów, które popełnia człowiek przy ekranie: przesuwanie stopa, dokładanie do straty, wchodzenie z zemsty. To realna korzyść i ma pokrycie w tym, co wiadomo o [finansach behawioralnych](/dlogic-quant/2026/07/07/finanse-behawioralne-mozg-inwestora/) i o [psychologii długiego inwestora](/dlogic-quant/2026/07/06/psychologia-dlugiego-inwestora-wrog-w-lustrze/). Ale trzeba powiedzieć to jasno: sama automatyzacja nie tworzy przewagi. Bot wykonuje regułę szybciej i bez emocji, natomiast jeśli reguła jest bezwartościowa, automat po prostu traci sprawniej. Architektura chroni przed katastrofą i pozwala rzetelnie testować, i tyle. To samo rozróżnienie opisałem przy [architekturze automatu](/dlogic-quant/2026/07/12/architektura-automatu-warstwy/).

## Pierwszy bot: co mogę powiedzieć teraz

Pierwszy system działa na rynku krypto i składa zlecenia przez MetaTrader 5. Świadomie nie opisuję tu logiki wejścia, bo jest w trakcie walidacji i wrócę do niej dopiero, gdy będę miał na jej temat coś uczciwego do powiedzenia. To, co mogę pokazać już teraz, to warstwa, która w moim przekonaniu decyduje o przetrwaniu konta, czyli zarządzanie ryzykiem i bezpieczniki.

Bot jest rozłożony na osobne warstwy: dane, sygnał, ryzyko, egzekucja i log. Warstwa sygnału jest czystą funkcją, którą da się testować w oderwaniu od reszty. Warstwa ryzyka to osobna bramka, przez którą musi przejść każda decyzja, zanim dotrze do brokera.

## Czego botowi nie wolno

To jest sedno, a nie dodatek. Zasady są wpisane na twardo i nieodłączalne:

```
Dzienny limit straty: po -10% kapitalu dnia bot pauzuje wejscia do polnocy UTC.
Kill-switch: po -30% od szczytu kapitalu bot zamyka wszystko i staje.
                Reset tylko reczny, nigdy automatyczny.
Jedna pozycja na instrument. Bez usredniania w strate, bez martingale.
Guard wielkosci: jesli minimalny lot przekracza budzet ryzyka, bot pomija sygnal.
Tryb domyslny: papierowy. Realne pieniadze wymagaja dwoch recznych krokow.
```

Zakaz dokładania do straty jest tu nie z ostrożności, tylko z arytmetyki. Podwajanie pozycji, która idzie przeciw tobie, to znany, najszybszy sposób na wyzerowanie konta. Widziałem, jak taki mechanizm kasuje realny depozyt, i ta zasada nie podlega negocjacji.

## Dlaczego papier, skoro backtest wygląda dobrze

Bo backtest, który wygląda dobrze, jest stanem domyślnym, a nie osiągnięciem. Jeśli przeszuka się dość kombinacji parametrów, świetny wynik na przeszłych danych jest gwarantowany, nawet gdy w danych nie ma żadnej struktury. To nie moja opinia, tylko własność statystyki, którą opisałem przy [walk-forward](/dlogic-quant/2026/07/12/optymalizacja-walk-forward-w-kodzie/), przy [look-ahead w kodzie](/dlogic-quant/2026/07/12/look-ahead-w-kodzie-realizm/) i przy [zawyżonym Sharpe](/dlogic-quant/2026/07/09/dlaczego-twoj-sharpe-klamie-deflated-sharpe/).

Dlatego traktuję backtest wyłącznie jako filtr negatywny: jeśli reguła nie przechodzi go nawet w wersji naiwnej, odpada. Jeśli przechodzi, nie znaczy to jeszcze nic. Jedyny dowód, który uznaję, to forward w czasie rzeczywistym, na realnych kwotowaniach i po pełnych kosztach. Bramka przejścia z papieru na realne konto jest zapisana z góry, obejmuje minimalny czas testu, minimalną liczbę zamkniętych transakcji, dodatni wynik netto i limit obsunięcia. Tej bramki nie wolno przesuwać po fakcie, bo wtedy przestaje cokolwiek znaczyć.

## Co dalej

Będę tu wracał z kolejnymi wpisami: co przeszło walidację, co poległo, jakie błędy wyszły dopiero na żywo. Bez obietnic wyniku i bez podawania parametrów, dopóki nie będę pewien, że jest o czym mówić. Jeśli ktoś szuka gotowego zarabiającego bota, to nie tutaj. Tu jest zapis pracy.

Materiał ma charakter dziennika i edukacji, nie jest poradą inwestycyjną ani ofertą. Opisane zasady bezpieczeństwa dotyczą mojego systemu i nie stanowią rekomendacji. Handel z dźwignią, a zwłaszcza automatyczny, grozi utratą całego kapitału.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
