---
title: "Ile naprawdę kosztuje twój trade. Implementation shortfall po ludzku"
description: "Twój realny koszt to nie spread z reklamy, tylko implementation shortfall: różnica między ceną w chwili decyzji a ceną realnego fillu. Jak rozłożyć koszt na spread, poślizg i timing, jak policzyć TCA względem ceny odniesienia i czemu mediana jest odporniejsza od średniej. Wszystko po ludzku."
date: 2026-07-09 14:30:00 +0200
eyebrow: "Edukacja · koszty egzekucji"
category: edukacja
dek: "Broker pokazuje ci spread i mówi, że to twój koszt. To połowa prawdy. Prawdziwy koszt to implementation shortfall, różnica między ceną, którą widziałeś klikając, a ceną, po której naprawdę wszedłeś. Jak się go liczy i jak zmierzyć własny, krok po kroku."
readingTime: 7
tags: [TCA, "koszty transakcyjne", "implementation shortfall", spread, egzekucja, slippage, Forex, quant]
---

> **W skrócie**
>
> - **Spread to nie cały koszt, tylko jego kawałek.** Realny koszt to implementation shortfall, czyli różnica między ceną w chwili decyzji a ceną realnego fillu.
> - **Koszt ma warstwy.** Pół spreadu na każdą nogę, poślizg między kliknięciem a fillem oraz timing. Płacisz wszystkie trzy, a spread pokazuje tylko pierwszą.
> - **TCA mierzy to porównaniem.** Transaction cost analysis stawia obok siebie cenę realizacji i cenę odniesienia z chwili decyzji, a nie liczbę z cennika brokera.
> - **Patrz na medianę, nie na średnią.** Rozkład kosztów ma gruby ogon, więc mediana lepiej opisuje typowy fill. Precyzyjny pomiar wymaga danych tickowych bid/ask.

**Teza w jednym zdaniu:** twój realny koszt to nie spread z reklamy, tylko implementation shortfall, różnica między ceną w chwili decyzji a ceną realnego fillu, a żeby go poznać, trzeba zmierzyć go na własnych transakcjach względem ceny odniesienia, zamiast wierzyć w jedną liczbę z platformy.

## Mit: „spread to twój koszt"

Otwierasz platformę, widzisz EURUSD ze spreadem, powiedzmy dziesiątych części pipsa, i myślisz, że to jest cała cena wstępu. To wygodne, bo broker sam to pokazuje, i błędne, bo pomija resztę.

Spread to tylko jedna warstwa. Do niej dochodzi poślizg (cena rusza się między kliknięciem a fillem), opóźnienie zlecenia i to, że kwotowanie, które widziałeś, oraz cena, po której naprawdę wszedłeś, to dwa różne momenty. Suma tych rzeczy to prawdziwy koszt egzekucji i prawie zawsze jest większa niż sam spread. Pytanie brzmi: o ile większa. Bez pomiaru to zgadywanka.

## Implementation shortfall, po ludzku

Nazwa brzmi korporacyjnie, idea jest prosta. Implementation shortfall to różnica między ceną, którą „powinieneś" był dostać w chwili podjęcia decyzji, a ceną, po której transakcja naprawdę się wykonała. Nie spread. Nie prowizja. Cała luka między planem a rzeczywistością, wyrażona w pipsach.

```
Cena decyzji  = mid rynku w chwili, gdy klikasz (ile teoretycznie powinieneś dostać)
Cena fillu    = po ile broker naprawdę cię wpuścił
Implementation shortfall = |cena fillu - cena decyzji|, liczone w pipsach

round-trip (RT) = shortfall na wejściu + shortfall na wyjściu
```

Dlaczego to lepsza miara niż spread? Bo łapie wszystko naraz: pół spreadu na każdą nogę, poślizg, timing. Jeśli wchodzisz w spokojny rynek limitem, shortfall bywa mniejszy niż nominalny spread. Jeśli walisz marketem w gorącą świecę na newsie, potrafi być wielokrotnością spreadu. Spread ci tego nie powie, bo jest liczbą z cennika, a shortfall jest liczbą z twojego rachunku.

## Z czego składa się koszt

Rozbijmy koszt egzekucji na warstwy, bo każda ma inne źródło i inną dźwignię kontroli.

```
Warstwa 1: pół spreadu na każdą nogę
  Kupujesz po ask, sprzedajesz po bid. Round-trip płacisz cały spread,
  po połowie na wejściu i na wyjściu.

Warstwa 2: poślizg (slippage)
  Cena rusza się między momentem kliknięcia a momentem fillu.
  Rośnie na newsach, w niskiej płynności, przy zleceniach rynkowych.

Warstwa 3: timing
  Kwotowanie, które widziałeś, i cena realizacji to dwa różne momenty.
  Opóźnienie zlecenia i tempo rynku decydują, ile tu tracisz.
```

Implementation shortfall to suma tych trzech warstw wyrażona jedną liczbą. Dlatego jest lepszą miarą niż sam spread: spread pokazuje tylko warstwę pierwszą, a płacisz wszystkie trzy.

## Jak liczy się TCA

TCA, czyli transaction cost analysis, to standardowa metoda pomiaru realnego kosztu. Sedno jest jedno: porównujesz cenę realizacji z ceną odniesienia z chwili decyzji i patrzysz, ile ci uciekło.

Jako cenę odniesienia zwykle przyjmuje się mid rynku, czyli środek między bid a ask w momencie podjęcia decyzji. W wersji przybliżonej, gdy nie masz ticku, można użyć środka bara na niskim interwale, na przykład (High + Low) / 2 bara M1 w chwili wejścia. Potem to samo dla wyjścia, a suma daje round-trip w pipsach.

To jest dokładnie ten pomiar, który zaleca literatura wykonawcza: porównaj cenę realizacji z ceną odniesienia z chwili decyzji, nie z liczbą z cennika. Reszta to już tylko arytmetyka na fillach.

## Czemu mediana jest odporniejsza od średniej

Kiedy zbierzesz koszty z wielu transakcji, kusi, żeby policzyć średnią. To błąd, i to systematyczny.

Rozkład kosztów egzekucji ma gruby prawy ogon. Większość filli kosztuje tyle, ile powinna, ale pojedyncze wejścia w gorący, zmienny bar potrafią kosztować wielokrotność normy. Średnia jest wrażliwa na te pojedyncze rozdmuchane odczyty: kilka ekstremów wciąga ją w górę i przestaje opisywać typową transakcję.

Mediana bierze wartość środkową, więc jeden odczyt dziesięć razy większy od reszty przesuwa ją minimalnie. Dlatego typowy koszt lepiej opisać medianą: mówi, ile kosztuje przeciętny fill, a nie ile kosztuje book po doliczeniu kilku katastrof. Ogon też jest ważny, ale mierzy się go osobno (na przykład percentylem), a nie chowa w średniej.

## Dlaczego precyzyjny TCA wymaga danych tickowych

Przybliżenie mid jako (High + Low) / 2 bara M1 to proxy, nie prawda. To środek zakresu z jednej minuty, a nie realny mid z ticku bid/ask w milisekundzie decyzji. Na spokojnych barach ten proxy jest bliski prawdy. Na barach zmiennych, gdzie minuta ma duży zakres, potrafi być zawyżony i sam wciąga prawy ogon pomiaru w górę.

Precyzyjny TCA wymaga danych tickowych bid/ask (na przykład z komercyjnych dostawców historii ticków) i liczenia shortfallu względem realnego mid w momencie zlecenia. Tak robi się to w pracach o mikrostrukturze rynku FX. Do nauki metody proxy z bara M1 wystarczy, ale trzeba pamiętać o jego ograniczeniu i właśnie dlatego patrzeć na medianę, nie na średnią.

Ważne też: mała próba nie jest dowodem. Kilka obserwacji na parze to ciekawostka, nie wniosek. Solidne liczby wymagają dziesiątek, a najlepiej setek filli na danym instrumencie.

## Jak policzyć to u siebie

Metoda jest standardowa i powtarzalna. Krok po kroku:

```
1. Wyeksportuj własne fille z platformy (historia zleceń: cena i czas).
2. Do każdego fillu dołóż cenę odniesienia z chwili decyzji
   (mid rynku, albo proxy (High + Low) / 2 bara M1 z tej minuty).
3. Policz różnicę w pipsach: |cena fillu - cena odniesienia|.
4. Zsumuj wejście i wyjście, żeby dostać round-trip.
5. Patrz na medianę zestawu, nie na średnią. Ogon oglądaj osobno.
```

Twoje liczby będą zależeć od brokera, par i godzin, w których grasz, więc nie ma sensu porównywać ich z cudzymi. O to właśnie chodzi: żeby to były twoje liczby, a nie reklama z cennika. Kiedy je masz, wiesz, ile naprawdę kosztuje wejście, i możesz oddzielić koszt egzekucji od tego, co tracisz gdzie indziej.

## Co przeczytać

Metoda nie jest niczyją prywatną sztuczką, tylko standardem rynku. Dwa źródła wystarczą na start:

- **FX Global Code**, kodeks dobrych praktyk rynku walutowego. Tłumaczy, czym jest uczciwa cena odniesienia i jak myśleć o kosztach wykonania, zamiast wierzyć w jedną liczbę z platformy.
- **LMAX FX TCA**, materiały o transaction cost analysis na FX. Pokazują, jak rozbić koszt na spread, poślizg i timing i dlaczego cena odniesienia z chwili decyzji jest właściwym punktem porównania.

To nie jest porada inwestycyjna. Tekst pokazuje metodę pomiaru realnego kosztu egzekucji, żebyś umiał policzyć własny implementation shortfall zamiast ufać spreadowi z cennika. Nie ma tu obietnicy zysku, jest tylko narzędzie do tego, żeby przestać mylić się co do tego, gdzie naprawdę uciekają pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
