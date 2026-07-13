---
title: "Jak naprawdę działa bank. Bilans, marża i wbudowana kruchość"
description: "Bank to nie skarbiec, tylko bilans: po jednej stronie kredyty, obligacje i rezerwy, po drugiej depozyty, finansowanie hurtowe i cienka warstwa kapitału własnego. Zysk bierze się z marży odsetkowej netto i prowizji, a istotą modelu jest transformacja terminów: krótkie pasywa płatne na żądanie finansują długie, niepłynne aktywa. Ta sama konstrukcja, która czyni bank użytecznym, czyni go kruchym: wypłacalny bank może paść z braku płynności, a run jest samospełniający się. Tekst rozkłada bilans, dźwignię i mechanikę paniki według modelu Diamonda i Dybviga (Nobel 2022), z Bank of England (2014), kursem Mehrlinga i podręcznikiem Freixasa i Rocheta w tle."
date: 2026-07-07 16:00:00 +0200
eyebrow: "Edukacja · pieniądz"
dek: "Bank nie jest skarbcem, w którym leżą twoje pieniądze. Jest bilansem: depozyty płatne od ręki finansują kredyty zamrożone na lata, a całość stoi na cienkiej warstwie kapitału. Ta konstrukcja zarabia na różnicy stóp i dokładnie z tego samego powodu jest krucha. Rozłożone na części: bilans, marża, dźwignia, run i wyłączniki paniki."
readingTime: 8
tags: [bank, bilans, "marża odsetkowa", depozyty, kredyty, "transformacja terminów", płynność, wypłacalność, dźwignia, "kapitał własny", "run na bank", "Diamond i Dybvig", "ubezpieczenie depozytów", "pożyczkodawca ostatniej instancji", "Bank of England", Mehrling, makroekonomia, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Bank to bilans, nie skarbiec. Po stronie aktywów: kredyty, obligacje, rezerwy w banku centralnym. Po stronie pasywów: depozyty klientów, finansowanie hurtowe od innych instytucji i kapitał własny, czyli cienka warstwa będąca różnicą między majątkiem a zobowiązaniami, która jako pierwsza pochłania straty.
> - Zysk banku to głównie marża odsetkowa netto: odsetki z długich aktywów minus koszt krótkich pasywów, plus prowizje i opłaty. Żeby ta różnica istniała, bank musi robić transformację terminów: od deponentów pożycza na żądanie, kredytobiorcom pożycza na lata. To społecznie użyteczne i to samo jest źródłem kruchości.
> - Płynność i wypłacalność to dwie różne rzeczy. Bank wypłacalny (majątek wart więcej niż zobowiązania) może upaść, bo nie ma z czego wypłacać dzisiaj. Do tego dochodzi dźwignia: skoro kapitał to mały ułamek bilansu, niewielka procentowo strata na aktywach zjada dużą część kapitału.
> - Diamond i Dybvig (1983, Nobel 2022) pokazali formalnie, że run na bank jest samospełniający się: istnieją dwie równowagi, spokój i panika, a sam strach przełącza system w tę gorszą, w której pada nawet zdrowy bank. Ubezpieczenie depozytów działa jak wyłącznik paniki, a resztę siatki bezpieczeństwa domyka pożyczkodawca ostatniej instancji.

**Teza w jednym zdaniu:** Bank zarabia na tym, że krótkim, płatnym na żądanie pieniądzem finansuje długie i niepłynne aktywa, więc kruchość nie jest usterką tego modelu, tylko jego ceną, a ubezpieczenie depozytów i pożyczkodawca ostatniej instancji istnieją po to, żeby tę wbudowaną kruchość trzymać w ryzach.

## Bilans banku: dwie strony jednej kartki

Potoczny obraz banku to skarbiec: wpłacasz pieniądze, one gdzieś leżą, czasem bank pożycza je dalej. Rzeczywisty bank to bilans, czyli kartka z dwiema stronami, które zawsze się równają. Po lewej aktywa: to, co bank ma i co przynosi mu dochód. Po prawej pasywa: to, skąd wziął środki i co jest winien innym.

Po stronie aktywów dominują kredyty: hipoteki, kredyty dla firm, kredyty konsumpcyjne. To pozycje rozpisane na lata, trudne do szybkiej sprzedaży bez straty. Obok nich obligacje, zwykle łatwiejsze do upłynnienia, oraz rezerwy w banku centralnym i gotówka, czyli to, czym bank rozlicza płatności i obsługuje wypłaty. Po stronie pasywów największą pozycją są depozyty klientów, w dużej części płatne na żądanie. Dalej finansowanie hurtowe: krótkoterminowe pożyczki od innych banków i instytucji, nieobjęte żadną gwarancją. Na końcu kapitał własny. To nie jest worek z pieniędzmi, tylko różnica między aktywami a zobowiązaniami: część bilansu należąca do właścicieli, która jako pierwsza pochłania straty.

```
BILANS BANKU (schemat ilustracyjny, liczby przykladowe):

  AKTYWA                           PASYWA
  kredyty                65        depozyty klientow         70
  obligacje              20        finansowanie hurtowe      20
  rezerwy i gotowka      10        kapital wlasny            10
  inne                    5
  ───────────────────────────      ───────────────────────────
  razem                 100        razem                    100

  kapital wlasny = aktywa minus zobowiazania (bufor na straty)
```

Jedno sprostowanie na starcie, za Bank of England (2014, „Money creation in the modern economy"): depozyty po prawej stronie w większości nie są oszczędnościami przyniesionymi do okienka. Powstają, gdy banki udzielają kredytów, bo kredyt tworzy depozyt. Mechanika kreacji pieniądza to osobna historia; tutaj wystarczy zapamiętać, że obie strony bilansu żyją. Aktywa rodzą dochód i ryzyko, pasywa rodzą koszt i mogą odpłynąć.

<figure>
<svg viewBox="0 0 640 470" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bilansTitle">
<title id="bilansTitle">Uproszczony bilans banku: aktywa po lewej, pasywa i kapitał po prawej</title>
<g font-family="system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif">
<text x="320" y="28" text-anchor="middle" font-size="12" font-weight="600" letter-spacing="1.2" fill="currentColor" opacity="0.6">BILANS BANKU (SCHEMAT ILUSTRACYJNY)</text>
<text x="160" y="74" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor" opacity="0.85">AKTYWA</text>
<text x="480" y="74" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor" opacity="0.85">PASYWA I KAPITAŁ</text>
<rect x="60" y="90" width="200" height="188.5" fill="currentColor" fill-opacity="0.30" stroke="currentColor" stroke-opacity="0.28"/>
<rect x="60" y="278.5" width="200" height="58" fill="currentColor" fill-opacity="0.20" stroke="currentColor" stroke-opacity="0.28"/>
<rect x="60" y="336.5" width="200" height="43.5" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-opacity="0.28"/>
<text x="72" y="188" font-size="13" fill="currentColor" opacity="0.8">kredyty</text>
<text x="248" y="188" text-anchor="end" font-size="13" font-weight="600" fill="currentColor" opacity="0.85">65</text>
<text x="72" y="311" font-size="13" fill="currentColor" opacity="0.8">obligacje</text>
<text x="248" y="311" text-anchor="end" font-size="13" font-weight="600" fill="currentColor" opacity="0.85">20</text>
<text x="72" y="362" font-size="12.5" fill="currentColor" opacity="0.8">rezerwy i gotówka</text>
<text x="248" y="362" text-anchor="end" font-size="13" font-weight="600" fill="currentColor" opacity="0.85">15</text>
<rect x="380" y="90" width="200" height="203" fill="currentColor" fill-opacity="0.33" stroke="currentColor" stroke-opacity="0.28"/>
<rect x="380" y="293" width="200" height="58" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-opacity="0.28"/>
<rect x="380" y="351" width="200" height="29" fill="#1a9e6a" fill-opacity="0.85" stroke="#1a9e6a" stroke-opacity="0.95" stroke-width="1.3"/>
<text x="392" y="195" font-size="13" fill="currentColor" opacity="0.82">depozyty klientów</text>
<text x="568" y="195" text-anchor="end" font-size="13" font-weight="600" fill="currentColor" opacity="0.85">70</text>
<text x="392" y="326" font-size="13" fill="currentColor" opacity="0.8">inne zobowiązania</text>
<text x="568" y="326" text-anchor="end" font-size="13" font-weight="600" fill="currentColor" opacity="0.85">20</text>
<text x="392" y="370" font-size="12" font-weight="600" fill="currentColor" opacity="0.85">kapitał własny</text>
<text x="568" y="370" text-anchor="end" font-size="12" font-weight="700" fill="currentColor" opacity="0.85">10</text>
<text x="320" y="240" text-anchor="middle" font-size="30" fill="currentColor" opacity="0.5">=</text>
<text x="320" y="260" text-anchor="middle" font-size="10.5" fill="currentColor" opacity="0.5">obie strony</text>
<text x="320" y="273" text-anchor="middle" font-size="10.5" fill="currentColor" opacity="0.5">równe</text>
<text x="376" y="356" text-anchor="end" font-size="9.5" fill="#1a9e6a" opacity="0.95">bufor na straty</text>
<path d="M308 366 L376 366" stroke="#1a9e6a" stroke-opacity="0.9" stroke-width="1.4" fill="none"/>
<path d="M377 366 L370 362.5 L370 369.5 Z" fill="#1a9e6a" fill-opacity="0.95"/>
<line x1="60" y1="404" x2="580" y2="404" stroke="currentColor" stroke-opacity="0.2"/>
<text x="320" y="426" text-anchor="middle" font-size="11.5" fill="currentColor" opacity="0.72">Dźwignia: kapitał to około 10% bilansu, a strata 5% aktywów zjada połowę bufora.</text>
<text x="320" y="447" text-anchor="middle" font-size="11.5" fill="currentColor" opacity="0.72">Krótkie pasywa finansują długie, niepłynne aktywa → stąd wbudowana kruchość.</text>
</g>
</svg>
<figcaption>Uproszczony bilans banku: obie kolumny mają równą wysokość, depozyty dominują po stronie finansowania, a kapitał własny to tylko cienka zielona warstwa na dole, która jako pierwsza pochłania straty. Przy takiej dźwigni już kilkuprocentowa strata na aktywach zjada dużą część tego cienkiego bufora.</figcaption>
</figure>

## Skąd bank ma zysk: marża odsetkowa i prowizje

Model biznesowy banku mieści się w jednej różnicy. Aktywa są oprocentowane wyżej, bo są długie i ryzykowne: kredyt hipoteczny albo firmowy płaci więcej niż rachunek bieżący. Pasywa kosztują mniej, bo są krótkie i wygodne: depozyt na żądanie płaci mało albo nic właśnie dlatego, że możesz go wyjąć w każdej chwili. Różnica między tym, co bank dostaje z aktywów, a tym, co płaci za pasywa, to wynik odsetkowy netto, a w przeliczeniu na aktywa marża odsetkowa netto.

```
ZYSK BANKU (schemat):

  odsetki otrzymywane z aktywow (kredyty, obligacje)
  minus odsetki placone za pasywa (depozyty, finansowanie hurtowe)
  ────────────────────────────────────────────────
  = wynik odsetkowy netto
  + prowizje i oplaty (konta, karty, wymiana walut)
  = z tego bank pokrywa koszty dzialania i straty kredytowe
```

Ta marża nie jest darmowa. Wynagradza trzy rzeczy naraz: ryzyko kredytowe (część kredytów nie wróci), ryzyko płynności (aktywa są zamrożone, pasywa płatne od ręki) i koszty prowadzenia całej maszynerii. Drugim silnikiem są prowizje i opłaty, mniej wrażliwe na poziom stóp. Ale rdzeń jest odsetkowy i ma jedną konsekwencję, wokół której kręci się reszta tego tekstu: żeby zarabiać na różnicy między długim a krótkim, trzeba być długim po stronie aktywów i krótkim po stronie pasywów. Czyli trzeba wziąć na siebie niedopasowanie terminów.

## Transformacja terminów: istota bankowości

To niedopasowanie ma nazwę: transformacja terminów. Bank bierze pasywa krótkie, płatne na żądanie, i zamienia je w aktywa długie, zamrożone na lata. Podręcznik akademicki (Freixas i Rochet, „Microeconomics of Banking") wymienia to jako jedną z definiujących funkcji banku, obok obsługi płatności oraz selekcji i monitorowania kredytobiorców, czego pojedynczy deponent nie umiałby robić sam.

Najpierw o tym, jak bardzo jest to użyteczne, potem o tym, dlaczego bywa groźne. Deponenci chcą mieć pieniądze dostępne od ręki, bo nie wiedzą, kiedy będą ich potrzebować. Kredytobiorcy chcą finansowania stabilnego i długiego, bo dom i fabryka zwracają się latami. Te potrzeby są sprzeczne, a bank je godzi: tysiącom deponentów daje płynność, kredytobiorcom pewność finansowania. Diamond i Dybvig opisali to jako ubezpieczenie płynności. Bank pozwala każdemu z osobna mieć dostęp do gotówki, choć wspólny majątek jest zamrożony, bo w normalnych czasach po pieniądze zgłasza się naraz tylko ułamek klientów.

Cały mechanizm działa więc na jednym założeniu statystycznym: nie wszyscy przyjdą jednocześnie. Prawo wielkich liczb robi za skarbiec. I dokładnie w tym miejscu użyteczność przechodzi w kruchość, bo założenie o rozproszonych wypłatach potrafi się załamać w jeden dzień.

## Płynność to nie wypłacalność

Dwa pojęcia, które potocznie się zlewają, a które trzeba trzymać osobno. Wypłacalność dotyczy całego bilansu: czy aktywa, uczciwie wycenione, są warte więcej niż zobowiązania. Płynność dotyczy przepływów: czy bank jest w stanie zapłacić to, co wymagalne dzisiaj, dzisiejszą gotówką i rezerwami. Perry Mehrling w kursie „Economics of Money and Banking" robi z tego rozróżnienia oś całego wykładu i nazywa dzienny przymus domykania przepływów warunkiem przetrwania (survival constraint). Bank może mieć najpiękniejsze aktywa świata, ale rachunki rozlicza się gotówką i rezerwami, nie pięknem aktywów. Niewypłacalność da się ciągnąć długo, brak płynności zatrzymuje instytucję od razu.

Stąd scenariusz, który na zdrowy rozum wygląda absurdalnie, a jest podręcznikowy: bank wypłacalny pada z braku płynności. Mechanizm jest sekwencją. Deponenci i wierzyciele hurtowi żądają zapłaty szybciej, niż bank ma płynnych środków. Bank zaczyna sprzedawać długie aktywa. Szybka sprzedaż niepłynnych pozycji odbywa się po cenach pożarowych, poniżej uczciwej wartości. Straty z tej wyprzedaży zjadają kapitał. Instytucja, która trzymana do zapadalności byłaby wypłacalna, staje się niewypłacalna przez samą próbę natychmiastowej zamiany majątku na gotówkę. Problem płynności i problem wypłacalności potrafią więc przechodzić jeden w drugi, i to w złą stronę.

## Dźwignia: małe straty, wielkie szkody

Druga wbudowana słabość to proporcje. Kapitał własny finansuje tylko mały ułamek bilansu banku, resztę finansuje cudzy pieniądz: depozyty i finansowanie hurtowe. To jest dźwignia i działa jak każda dźwignia: zwielokrotnia zwrot z kapitału, kiedy aktywa zarabiają, i zwielokrotnia stratę, kiedy tracą.

```
DZWIGNIA (przyklad ilustracyjny, nie realne wymogi kapitalowe):

  aktywa 100 = zobowiazania 92 + kapital wlasny 8

  strata 2% aktywow  → kapital z 8 do 6   (znika 1/4 kapitalu)
  strata 4% aktywow  → kapital z 8 do 4   (znika polowa)
  strata 8% aktywow  → kapital z 8 do 0   (niewyplacalnosc)

  mala procentowo strata na duzym bilansie zjada maly kapital
```

Arytmetyka jest prosta i bezlitosna. Wystarczy, że niewielki procent aktywów straci na wartości, a z kapitału ubywa wielokrotnie większy procent, bo cała strata uderza w cienką warstwę bufora. Dlatego regulacje bankowe kręcą się wokół kapitału, czyli tego, ile go ma być i jak ważyć ryzyko aktywów, a nie wokół zapasu gotówki w skarbcu. I dlatego rynek tak nerwowo reaguje na wieści o stratach banków: przy dźwigni droga od przejściowych strat do braku kapitału jest krótka. Dźwignia sprzęga się też z poprzednim punktem. Im cieńszy bufor, tym szybciej wyprzedaż pożarowa przerabia problem płynnościowy na niewypłacalność.

## Run na bank: model Diamonda i Dybviga

Skoro bank stoi na założeniu, że nie wszyscy przyjdą naraz, to co się dzieje, gdy przyjdą? Odpowiedź formalną daje artykuł „Bank Runs, Deposit Insurance, and Liquidity" (Diamond i Dybvig, Journal of Political Economy, 1983), za który Douglas Diamond i Philip Dybvig dostali w 2022 roku Nagrodę Nobla z ekonomii, wspólnie z Benem Bernanke.

W modelu deponenci nie wiedzą z góry, kiedy będą potrzebować pieniędzy, a majątek banku tkwi w długiej inwestycji, którą przedwczesna likwidacja psuje. Depozyt na żądanie jest świetnym ubezpieczeniem: kto musi, wypłaca wcześniej, kto może czekać, zostawia. Obowiązuje jednak kolejka: bank wypłaca po kolei, póki ma z czego. I tu pojawia się rdzeń wyniku: ten sam bank ma dwie równowagi.

```
DWIE ROWNOWAGI (Diamond i Dybvig 1983):

  SPOKOJ:  wyplacaja tylko ci, ktorzy musza → plynnosci starcza
                                            → bank stoi
  PANIKA:  wyplacaja wszyscy na zapas       → likwidacja dlugich
                                              aktywow ze strata
                                            → bank pada

  te same aktywa, ci sami klienci; wynik wybiera oczekiwanie tlumu
```

Jeśli każdy wierzy, że inni nie pobiegną, nikt nie biegnie i wszystko działa. Jeśli każdy uwierzy, że inni pobiegną, jedyną racjonalną odpowiedzią jest stanąć w kolejce pierwszym, zanim skończy się gotówka. Wtedy biegną wszyscy, także ci, którzy pieniędzy nie potrzebują i uważają bank za zdrowy. Run jest samospełniający się: nie potrzebuje złych aktywów ani oszustwa, wystarczy plotka albo zła wiadomość, cokolwiek, co skoordynuje oczekiwania na panikę. Upaść może bank całkowicie zdrowy, a run z definicji wymusza straty, bo zmusza do przedwczesnej likwidacji tego, co miało pracować latami. Współczesna wersja różni się tylko techniką: kolejkę przed oddziałem zastąpiła aplikacja, więc depozyty potrafią odpływać w tempie, o jakim dawne paniki mogły tylko śnić.

## Wyłączniki paniki: ubezpieczenie depozytów i ostatnia instancja

Diamond i Dybvig nie zatrzymali się na diagnozie, w tym samym artykule wskazali wyłącznik. Skoro panika bierze się z przekonania, że kto przyjdzie za późno, nie dostanie nic, trzeba to przekonanie zabić u źródła. Robi to ubezpieczenie depozytów: wiarygodna gwarancja (w modelu rządowa, bo stoi za nią władza podatkowa), że deponent odzyska pieniądze niezależnie od tego, co zrobią inni. Jeśli nie musisz ścigać się z tłumem, nie biegniesz. Jeśli nikt nie biegnie, gwarancji nie trzeba używać. Dobrze skonstruowane ubezpieczenie depozytów działa głównie przez samo istnienie. Ceną jest pokusa nadużycia: bank z ubezpieczonymi pasywami jest słabiej pilnowany przez deponentów, dlatego gwarancja chodzi w parze z limitami, nadzorem i wymogami kapitałowymi.

Tyle depozyty detaliczne. Ale spora część pasywów, całe finansowanie hurtowe, nie jest objęta żadną gwarancją, a run instytucji na instytucję bywa szybszy niż run klientów indywidualnych. Na to jest drugi wyłącznik: bank centralny jako pożyczkodawca ostatniej instancji, który w panice pożycza płynność pod dobry zastaw, żeby wypłacalny bank nie musiał wyprzedawać majątku po cenach pożarowych. Ta zasada jest o sto dziesięć lat starsza niż model Diamonda i Dybviga i ma na tym blogu osobny tekst o [regule Bagehota](/dlogic-quant/2026/07/08/lender-of-last-resort-bagehot/). Tutaj wystarczy domknąć logikę: ubezpieczenie depozytów gasi panikę deponentów, pożyczkodawca ostatniej instancji gasi panikę finansowania hurtowego, a wymogi kapitałowe pilnują, żeby pod spodem było czym pokrywać straty.

## Co z tego wynika

Najważniejsza zmiana w patrzeniu jest taka: kruchość banku nie jest anomalią, którą dałoby się doregulować do zera, tylko drugą stroną usługi, z której korzysta każdy posiadacz konta. Ten sam mechanizm, który daje deponentom płynność, a gospodarce długi kredyt, tworzy możliwość runu. Dlatego nowoczesna bankowość zawsze występuje w pakiecie: transformacja terminów plus siatka bezpieczeństwa, czyli gwarancje depozytów, ostatnia instancja i kapitał. Spory o regulacje to w gruncie rzeczy spory o to, ile kruchości tolerować w zamian za ile kredytu i marży.

Druga zmiana dotyczy czytania kryzysów. Pytanie, czy bank ma dobre aktywa, to pytanie o wypłacalność. Pytanie, czy dotrwa do piątku, to pytanie o płynność. Przy dźwigni odpowiedzi potrafią zamienić się miejscami w tydzień. Kto rozumie bilans, marżę i dwie równowagi Diamonda i Dybviga, ten w nagłówkach o kłopotach banków szuka trzech rzeczy: jak krótkie są pasywa, jak niepłynne aktywa i ile kapitału stoi pomiędzy. Reszta jest komentarzem.

To nie jest porada inwestycyjna. To wykład mechaniki bankowości, oparty na klasycznym artykule Diamonda i Dybviga (1983), materiałach Bank of England (2014), kursie Perry'ego Mehrlinga „Economics of Money and Banking" oraz podręczniku Freixasa i Rocheta „Microeconomics of Banking", żebyś rozumiał, na czym stoi bank, zanim zaczniesz oceniać, czy stoi pewnie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
