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

<figure>
<svg viewBox="0 0 640 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Wykres schodkowy: koszt egzekucji narasta od połowy spreadu, przez prowizję i wpływ na rynek, po poślizg, a ostatni słupek to koszt całkowity">
  <title>Dekompozycja pełnego kosztu transakcji</title>
  <g font-family="system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
    <text x="60" y="26" font-size="16" font-weight="600" fill="currentColor" opacity="0.85">Dekompozycja pełnego kosztu transakcji</text>

    <g stroke="currentColor" stroke-width="1" opacity="0.18">
      <line x1="60" y1="330" x2="620" y2="330"/>
      <line x1="60" y1="260" x2="620" y2="260"/>
      <line x1="60" y1="190" x2="620" y2="190"/>
      <line x1="60" y1="120" x2="620" y2="120"/>
      <line x1="60" y1="50" x2="620" y2="50"/>
    </g>

    <g stroke="currentColor" stroke-width="1.5" opacity="0.5">
      <line x1="60" y1="50" x2="60" y2="330"/>
      <line x1="60" y1="330" x2="620" y2="330"/>
    </g>

    <g font-size="12" fill="currentColor" opacity="0.6" text-anchor="end">
      <text x="52" y="334">0,0</text>
      <text x="52" y="264">0,5</text>
      <text x="52" y="194">1,0</text>
      <text x="52" y="124">1,5</text>
      <text x="52" y="54">2,0</text>
    </g>

    <text transform="translate(20 190) rotate(-90)" text-anchor="middle" font-size="12.5" fill="currentColor" opacity="0.6">koszt egzekucji (pip)</text>

    <g stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.35">
      <line x1="147" y1="274" x2="197" y2="274"/>
      <line x1="259" y1="232" x2="309" y2="232"/>
      <line x1="371" y1="190" x2="421" y2="190"/>
      <line x1="483" y1="106" x2="533" y2="106"/>
    </g>

    <rect x="85"  y="274" width="62" height="56"  fill="currentColor" opacity="0.30"/>
    <rect x="197" y="232" width="62" height="42"  fill="currentColor" opacity="0.45"/>
    <rect x="309" y="190" width="62" height="42"  fill="currentColor" opacity="0.62"/>
    <rect x="421" y="106" width="62" height="84"  fill="currentColor" opacity="0.80"/>
    <rect x="533" y="106" width="62" height="224" fill="#0b66c3"/>

    <g font-size="12.5" fill="currentColor" opacity="0.7" text-anchor="middle">
      <text x="116" y="266">0,4</text>
      <text x="228" y="224">0,3</text>
      <text x="340" y="182">0,3</text>
      <text x="452" y="98">0,6</text>
    </g>
    <text x="564" y="98" font-size="13" font-weight="600" text-anchor="middle" fill="currentColor" opacity="0.85">1,6 pip</text>

    <g font-size="13" fill="currentColor" opacity="0.75" text-anchor="middle">
      <text x="116" y="350">Połowa<tspan x="116" dy="16">spreadu</tspan></text>
      <text x="228" y="350">Prowizja</text>
      <text x="340" y="350">Wpływ na<tspan x="340" dy="16">rynek</tspan></text>
      <text x="452" y="350">Poślizg</text>
      <text x="564" y="350">Koszt<tspan x="564" dy="16">całkowity</tspan></text>
    </g>
  </g>
</svg>
<figcaption>Koszt egzekucji narasta warstwami, od połowy spreadu, przez prowizję i wpływ na rynek, aż po poślizg. Ostatni słupek to suma wszystkich warstw, czyli pełny implementation shortfall dla wejścia i wyjścia.</figcaption>
</figure>

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
