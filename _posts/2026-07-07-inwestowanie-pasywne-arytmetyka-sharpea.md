---
title: "Inwestowanie pasywne. Arytmetyka, której nie da się oszukać"
description: "Arytmetyka Sharpe'a (1991): przed kosztami średni aktywnie zarządzany dolar zarabia tyle co pasywny, po kosztach musi zarabiać mniej i to jest tożsamość arytmetyczna, nie opinia. SPIVA US Year-End 2025 pokazuje skalę: 79% funduszy large-cap przegrało z S&P 500 w horyzoncie roku, około 93% w horyzoncie 20 lat. Carhart (1997) oraz Fama i French (2010) dokładają brak persystencji, a jedynym pewnym prognostykiem wyniku pozostają koszty."
date: 2026-07-07 13:00:00 +0200
eyebrow: "Edukacja · długi termin"
dek: "Jedna strona arytmetyki z 1991 roku ustawia oczekiwania wobec całej branży aktywnego zarządzania: po kosztach średni aktywny dolar musi przegrać z pasywnym. Dalej dane SPIVA z korektą na survivorship bias, dwa klasyczne badania persystencji, rachunek kosztów na 30 lat i uczciwy kontrapunkt, bo pasywne nie znaczy bezpieczne. Na start wystarczy 16 stron darmowego PDF."
readingTime: 8
tags: ["inwestowanie pasywne", "fundusze indeksowe", ETF, SPIVA, Sharpe, "arytmetyka aktywnego zarządzania", koszty, "S&P 500", Carhart, "Fama i French", Bogle, Malkiel, Bernstein, "długi termin", "survivorship bias"]
category: edukacja
---

> **W skrócie**
>
> - Sharpe (1991): przed kosztami średni aktywnie zarządzany dolar zarabia dokładnie tyle, ile średni pasywny, a po kosztach musi zarabiać mniej. To tożsamość arytmetyczna, wynika z dodawania, odejmowania, mnożenia i dzielenia, więc nie da się jej obalić lepszym researchem.
> - SPIVA US Year-End 2025: w samym 2025 roku 79% aktywnych funduszy large-cap przegrało z S&P 500, a w horyzoncie 20 lat przegrywa około 93%. Wynik jednoroczny waha się między edycjami od około 55 do 80%, dlatego cytat bez edycji i horyzontu jest bezwartościowy.
> - Zwycięzcy nie wracają: Carhart (1997) pokazuje, że powtarzalność wyników funduszy wyjaśniają wspólne czynniki i koszty, a trwale powtarzalni są tylko najgorsi. Fama i French (2010) szacują, że agregat aktywnych funduszy to w przybliżeniu rynek minus koszty i tylko garstka zarządzających zarabia na pokrycie własnych opłat.
> - Koszty to jedyny składnik przyszłego wyniku znany z góry: przy 7% brutto rocznie 30 lat kapitalizacji daje 7.6-krotność kapitału, a po zdjęciu 2 punktów procentowych opłat zostaje 4.3-krotność, czyli opłaty zjadają około 43% wyniku końcowego. Kontrapunkt: fundusz pasywny spada dokładnie tyle, ile rynek.

**Teza w jednym zdaniu:** Po kosztach średni aktywnie zarządzany dolar musi zarobić mniej niż średni pasywny, bo tak działa arytmetyka, a cztery dekady danych o funduszach pokazują, że prawie nikomu nie udaje się trwale stanąć po lepszej stronie tej średniej.

## Tożsamość arytmetyczna, nie pogląd

William Sharpe opublikował w 1991 roku w Financial Analysts Journal (rocznik 47, numer 1) tekst The Arithmetic of Active Management. Krótki, darmowo dostępny na stronie Stanforda i zbudowany tak, że nie zostawia miejsca na spory o próbkę, okres ani metodologię. Najpierw definicje: inwestor pasywny trzyma wszystkie papiery z danego rynku w proporcjach ich kapitalizacji. Inwestor aktywny to każdy, kto trzyma cokolwiek innego albo próbuje wyprzedzać rynek transakcjami. Dalej wystarczą cztery działania.

```
rynek = wszystkie dolary pasywne + wszystkie dolary aktywne

1. pasywny dolar trzyma portfel rynkowy,
   więc przed kosztami zarabia dokładnie zwrot rynku
2. zwrot rynku to średnia ważona zwrotów wszystkich dolarów,
   a skoro pasywne = rynek, to średni aktywny dolar = rynek (przed kosztami)
3. aktywne zarządzanie kosztuje więcej (opłaty, obrót, spready),
   więc po kosztach średni aktywny dolar MUSI zarobić mniej niż pasywny
```

Nie ma tu hipotezy do przetestowania. Jeśli jakiś aktywny dolar wygrywa z rynkiem przed kosztami, inny aktywny dolar musi o dokładnie tyle przegrać, bo średnia wszystkich jest z góry ustalona i równa zwrotowi rynku. Aktywni grają między sobą w grę o sumie zerowej przed kosztami i o sumie ujemnej po kosztach. Sharpe zaznacza, że wynik trzyma się w każdym okresie i na każdym rynku, bo wymaga wyłącznie praw dodawania, odejmowania, mnożenia i dzielenia, a badania empiryczne, które zdają się mu przeczyć, po prostu mierzą coś niepoprawnie.

## SPIVA: arytmetyka spotyka dane

Tożsamość mówi o średniej. Skalę w praktyce mierzy SPIVA (S&P Indices Versus Active), scorecard publikowany przez S&P Dow Jones Indices od 2002 roku. Metodologicznie SPIVA robi dwie rzeczy, o które rozbija się większość domowych porównań: liczy wyniki funduszy po kosztach i koryguje survivorship bias, czyli trzyma w mianowniku fundusze zlikwidowane i wchłonięte po drodze. Bez tej korekty długie horyzonty wyglądają dużo ładniej, bo najsłabsze fundusze znikają z próby, zanim ktokolwiek zdąży je policzyć.

Edycja US Year-End 2025 daje dwa punkty, które warto zapamiętać razem, nigdy osobno. W samym 2025 roku z S&P 500 przegrało 79% aktywnych funduszy large-cap. W horyzoncie 20 lat przegrywa około 93%. Horyzont jest częścią wyniku: pojedynczy rok bywa łaskawy i między edycjami wynik jednoroczny waha się od około 55 do 80%, ale im dłuższe okno, tym odsetek przegranych rośnie, bo przewaga kosztowa indeksu kumuluje się rok po roku, a fundusz musi ją odrabiać w każdym kolejnym rozdaniu. Stąd żelazna zasada higieny: każdy cytat z SPIVA nosi edycję i horyzont, inaczej nic nie znaczy.

<figure>
<svg viewBox="0 0 640 240" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="26" font-size="13" fill="currentColor">Odsetek aktywnych funduszy large-cap USA przegrywających z S&amp;P 500</text><text x="34" y="44" font-size="10.5" fill="currentColor" opacity="0.6">SPIVA US Year-End 2025, wyniki po kosztach, z korektą na survivorship bias</text><line x1="400" y1="58" x2="400" y2="186" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-dasharray="4 4"/><text x="406" y="68" font-size="10" fill="currentColor" opacity="0.6">50% = rzut monetą</text><rect x="210" y="78" width="300" height="30" fill="#0b66c3" opacity="0.55"/><rect x="210" y="134" width="353" height="30" fill="#0b66c3"/><text x="200" y="97" font-size="11" fill="currentColor" text-anchor="end">1 rok</text><text x="200" y="153" font-size="11" fill="currentColor" text-anchor="end">20 lat</text><text x="518" y="97" font-size="12" font-weight="600" fill="#0b66c3">79%</text><text x="571" y="153" font-size="12" font-weight="600" fill="#0b66c3">≈93%</text><line x1="210" y1="186" x2="590" y2="186" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="210" y1="186" x2="210" y2="191" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="400" y1="186" x2="400" y2="191" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="590" y1="186" x2="590" y2="191" stroke="currentColor" stroke-width="1" opacity="0.6"/><text x="210" y="206" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">0%</text><text x="400" y="206" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">50%</text><text x="590" y="206" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">100%</text></svg>
<figcaption>Dwa horyzonty z tej samej edycji SPIVA US Year-End 2025: w skali jednego roku z S&amp;P 500 przegrało 79% aktywnych funduszy large-cap, w skali 20 lat około 93%. Przerywana linia to poziom rzutu monetą. Wynik jednoroczny potrafi wahać się między edycjami od około 55 do 80%, dwudziestoletni siedzi stabilnie powyżej 90%, dlatego cytat z SPIVA bez edycji i horyzontu nic nie znaczy.</figcaption>
</figure>

## Zwycięzcy nie wracają: Carhart oraz Fama i French

Naturalna linia obrony brzmi: średnia mnie nie dotyczy, wystarczy wybrać zarządzającego z najlepszą historią. Dwa klasyczne badania rozbierają tę nadzieję na częściach.

Carhart (On Persistence in Mutual Fund Performance, Journal of Finance 52(1), 1997) sprawdził na bazie wolnej od survivorship bias, czy zwycięzcy powtarzają wynik. Odpowiedź: to, co wygląda na gorącą rękę, niemal w całości wyjaśniają wspólne czynniki (rynek, wielkość spółek, wycena, momentum) oraz koszty. Opłaty i obroty portfela przekładają się na gorszy wynik netto co najmniej jeden do jednego. Jedyna trwała persystencja, jaka zostaje po korektach, dotyczy najgorszych funduszy: one przegrywają uporczywie, w dużej mierze dlatego, że dużo kosztują.

Fama i French (Luck versus Skill in the Cross-Section of Mutual Fund Returns, Journal of Finance 65(5), 2010) zadali pytanie z drugiej strony: czy w przekroju tysięcy funduszy jest więcej wybitnych wyników, niż wyprodukowałby czysty przypadek? Agregat aktywnych funduszy zachowuje się jak rynek minus koszty, dokładnie tak, jak każe arytmetyka Sharpe'a. A funduszy z alfą na tyle dużą, żeby pokryć własne opłaty, jest tak niewiele, że ex post trudno je odróżnić od szczęściarzy. Tabela wyników z zeszłego roku to w przeważającej części tabela szumu, nie tabela umiejętności.

## Koszty: jedyna zmienna znana z góry

Przyszłego zwrotu rynku nie zna nikt. Opłatę zna każdy, co do punktu bazowego, zanim wpłaci pierwszą złotówkę. To jedyny składnik przyszłego wyniku znany z góry i z gwarancją, tyle że ze znakiem minus. Bogle w The Little Book of Common Sense Investing (2007) nazywa ten efekt tyranią składanych kosztów i streszcza filozofię indeksowania w jednym zdaniu: dostajesz to, za co nie płacisz.

```
30 lat kapitalizacji, czysta arytmetyka:
7% brutto rocznie:               1.07^30 ≈ 7.6x kapitału
po opłatach 2 p.p. (5% netto):   1.05^30 ≈ 4.3x kapitału
opłaty zjadły około 43% wyniku końcowego
```

Dwa punkty procentowe rocznie brzmią niewinnie. W kapitalizacji przez trzy dekady zabierają niemal połowę końcowego kapitału, mimo że w żadnym pojedynczym roku nie bolały. Ta sama mechanika działa w drugą stronę: przewaga funduszu indeksowego za 0.1-0.2% rocznie nad aktywnym za 1-2% nie jest kosmetyką, tylko jedyną w pełni przewidywalną siłą w całym równaniu.

## Czym jest fundusz indeksowy i czym jest ETF

Fundusz indeksowy nie wybiera spółek. Kupuje wszystkie papiery z indeksu w proporcjach kapitalizacji, utrzymuje je przy minimalnym obrocie i dzięki temu kosztuje o rząd wielkości mniej niż fundusz aktywny. Pomysł jest starszy niż produkt: Malkiel w A Random Walk Down Wall Street (1973) postulował taki fundusz dla zwykłego inwestora, kiedy jeszcze nie istniał, a Bogle uruchomił pierwszy detaliczny fundusz indeksowy w 1976 roku i przez lata zbierał za niego kpiny branży.

ETF to ten sam pomysł w giełdowym opakowaniu: fundusz notowany jak akcja, kupowany i sprzedawany w trakcie sesji. Jedno rozróżnienie oszczędza wielu nieporozumień: ETF opisuje opakowanie, nie strategię. Istnieją ETF-y aktywne, tematyczne i lewarowane. Pasywność to cecha zawartości, czyli replikacji szerokiego indeksu przy niskim koszcie, a nie trzech liter w nazwie.

## Czego ta arytmetyka nie obiecuje

Po pierwsze, pasywne nie znaczy bezpieczne. Fundusz indeksowy z definicji spada dokładnie tyle, ile rynek: w bessach z lat 2000-2002 i 2007-2009 szeroki rynek akcji USA tracił rzędu połowy wartości i portfel indeksowy szedł z nim krok w krok, bo do tego został zbudowany. Arytmetyka Sharpe'a rozstrzyga pojedynek aktywne kontra pasywne po kosztach; nie mówi ani słowa o tym, ile akcji w ogóle trzymać. Decyzja o wielkości ekspozycji i o zachowaniu w obsunięciu pozostaje przy inwestorze i żaden indeks jej nie podejmie.

Po drugie, tożsamość dotyczy średniego dolara, nie każdego zarządzającego z osobna. Fundusze bijące rynek po kosztach przez długie okresy istnieją i arytmetyka tego nie zabrania. Problem jest praktyczny i pokazany w danych: Fama i French nie umieją odróżnić większości takich przypadków od szczęścia, a Carhart pokazuje, że wczorajsza pozycja w rankingu prawie nic nie mówi o jutrzejszej. Zakład o wskazanie zwycięzcy z góry ma niską trafność i pewny, coroczny koszt.

Po trzecie, drobna uczciwość techniczna: SPIVA porównuje fundusze z indeksem, a indeks nie ma kosztów. Realny fundusz indeksowy zostaje za swoim indeksem o własną opłatę i różnicę odwzorowania. Przy 0.1-0.2% rocznie to mało na tle 1-2% w funduszach aktywnych, ale zero nie jest.

## Od czego zacząć

Najkrótsza sensowna ścieżka wygląda tak. Na początek Bernstein, If You Can (2014): 16 stron, darmowy PDF na efficientfrontier.com, w środku cała mechanika oszczędzania przez indeks plus pięć przeszkód, głównie behawioralnych, które trzeba po drodze pokonać. Potem oryginalny Sharpe (1991), bo warto raz zobaczyć cały argument u źródła. Na dłuższe wieczory dwie książki: Bogle, The Little Book of Common Sense Investing (2007), czyli arytmetyka kosztów rozpisana na przykładach, oraz Malkiel, A Random Walk Down Wall Street (1973, regularnie wznawiany), czyli szersze tło, dlaczego wybieranie spółek i timing rynku są takie trudne.

To nie jest porada inwestycyjna. To edukacyjne omówienie jednej tożsamości arytmetycznej i czterech dekad danych o funduszach, żeby oczekiwania wobec aktywnego i pasywnego inwestowania ustawiać na liczbach, a nie na marketingu.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
