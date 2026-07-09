---
title: "Drawdown. Dlaczego strata 50 procent wymaga zysku 100"
description: "Obsunięcie kapitału to spadek wartości konta od szczytu do dołka. Dlaczego głębokie obsunięcie jest groźne nieliniowo, jaka jest matematyka odrabiania strat, czemu drawdown jest bliższy doświadczeniu inwestora niż zmienność i jak Conditional Drawdown at Risk formalizuje ogon obsunięć."
date: 2026-07-08 12:00:00 +0200
eyebrow: "Edukacja · ryzyko"
category: edukacja
dek: "Zmienność mierzy rozproszenie, obsunięcie mierzy ból. Kompendium: definicja drawdown, nieliniowa arytmetyka odrabiania strat, obsunięcie jako miara ryzyka wierniejsza doświadczeniu niż odchylenie standardowe, CDaR jako formalna miara ogona i związek z wielkością pozycji."
readingTime: 7
tags: ["drawdown", "obsunięcie kapitału", "ryzyko", "maximum drawdown", "CDaR", "zarządzanie ryzykiem", "zmienność", "quant"]
---

> **W skrócie**
>
> - **Obsunięcie to spadek kapitału od szczytu do dołka**, liczony od high-water mark. Maksymalne obsunięcie (MDD) to najgłębszy taki zjazd, a czas pod wodą to jak długo kapitał wraca do rekordu. Drawdown mierzy ból ścieżki, nie rozproszenie wokół średniej.
> - **Arytmetyka odrabiania jest nieliniowa i bezlitosna:** strata d wymaga zysku d/(1−d). 10% straty to 11% zysku, 50% straty to już 100%, a 90% straty to aż 900%. Wymagany zwrot przyspiesza, im głębiej schodzisz, bo ta funkcja jest wypukła.
> - **Drawdown jest bliższy doświadczeniu inwestora niż zmienność,** bo jest zależny od ścieżki i wyłapuje seryjną korelację strat, czyli ich zbijanie się w serie, której odchylenie standardowe nie widzi (Goldberg, Mahmoud).
> - **CDaR (Chekhlov, Uryasev, Zabarankin)** formalizuje ogon obsunięć jako średnią z najgorszych zjazdów i płynnie łączy średnie obsunięcie z maksymalnym. Przez Kelly z limitem obsunięcia (Busseti, Boyd) ten ogon wprost wyznacza dopuszczalną wielkość pozycji.

**Teza w jednym zdaniu:** głębokie obsunięcie jest groźne nieliniowo, bo zysk potrzebny do odrobienia rośnie szybciej niż sama strata, a ponieważ drawdown wierniej niż zmienność mierzy realny ból ścieżki, to on, a nie odchylenie standardowe, powinien wyznaczać limit ryzyka i wielkość pozycji.

## Czym jest obsunięcie kapitału

Drawdown to nie to samo co strata na pojedynczej transakcji. To spadek wartości konta liczony od jego dotychczasowego szczytu, czyli od tak zwanego high-water mark. Dopóki kapitał rośnie i bije rekordy, obsunięcie wynosi zero. W chwili, gdy konto cofa się poniżej ostatniego szczytu, zaczyna się obsunięcie i trwa aż do momentu, w którym wartość wróci na ten sam poziom.

```
M(t)  = max_{s ≤ t} V(s)              wartość szczytowa (high-water mark) do chwili t
DD(t) = ( M(t) − V(t) ) / M(t)        obsunięcie względne w chwili t  (0, gdy jesteś na szczycie)
MDD   = max_t DD(t)                    maksymalne obsunięcie na całej ścieżce

V(t) = wartość kapitału w chwili t
czas pod wodą = długość okresu od szczytu do powrotu na ten szczyt
```

Trzy liczby opisują obsunięcie. Głębokość, czyli jak daleko jest od szczytu do dołka. Maksymalne obsunięcie (maximum drawdown, MDD), czyli najgłębszy taki zjazd na całej badanej ścieżce. I czas pod wodą, czyli jak długo kapitał pozostaje poniżej poprzedniego rekordu, zanim go odzyska. Ta trzecia liczba bywa niedoceniana, a potrafi boleć najbardziej: nawet umiarkowane obsunięcie, które odrabia się latami, zjada cierpliwość i kapitał psychiczny szybciej, niż zrobiłaby to sama głębokość.

## Brutalna arytmetyka odrabiania

Kluczowa własność obsunięcia jest czysto arytmetyczna i nie podlega dyskusji: strata i zysk potrzebny do jej odrobienia nie są symetryczne. Jeśli tracisz frakcję d kapitału, zostaje Ci (1 − d). Żeby wrócić na szczyt, musisz tę resztę pomnożyć przez odwrotność tego, co zostało.

```
zostaje po stracie:   1 − d
mnożnik do szczytu:   1 / (1 − d)
wymagany zysk:        g(d) = 1 / (1 − d) − 1 = d / (1 − d)

d = głębokość obsunięcia  (np. 0,50 to utrata połowy kapitału)
g = zysk potrzebny, żeby wrócić na szczyt
```

Sama strata i wymagany zysk rozjeżdżają się coraz bardziej, im głębiej schodzisz.

```
strata (d)        wymagany zysk  g(d) = d/(1−d)
    5%                   5,3%
   10%                  11,1%
   20%                  25,0%
   25%                  33,3%
   33,3%                50,0%
   50%                 100,0%
   60%                 150,0%
   70%                 233,3%
   80%                 400,0%
   90%                 900,0%
```

Przeczytaj tę tabelę powoli. Strata 10% wymaga skromnych 11% zysku, więc różnica jest prawie niewidoczna. Ale strata 50% wymaga już zysku 100%, czyli podwojenia tego, co zostało. A strata 90% wymaga zysku 900%, czyli dziesięciokrotności ocalałego kapitału. Te same procenty straty kupują radykalnie różny rachunek do zapłaty.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><line x1="150" y1="60" x2="150" y2="243" stroke="currentColor" stroke-opacity="0.28"/><line x1="296.67" y1="60" x2="296.67" y2="243" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><line x1="443.33" y1="60" x2="443.33" y2="243" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><line x1="590" y1="60" x2="590" y2="243" stroke="currentColor" stroke-opacity="0.12" stroke-dasharray="3 4"/><text x="150" y="256" font-size="9" fill="currentColor" fill-opacity="0.5" text-anchor="middle">0%</text><text x="296.67" y="256" font-size="9" fill="currentColor" fill-opacity="0.5" text-anchor="middle">300%</text><text x="443.33" y="256" font-size="9" fill="currentColor" fill-opacity="0.5" text-anchor="middle">600%</text><text x="590" y="256" font-size="9" fill="currentColor" fill-opacity="0.5" text-anchor="middle">900%</text><text x="10" y="20" font-size="13" fill="currentColor">Odrabianie straty: wymagany zysk rośnie eksplozyjnie</text><rect x="10" y="32" width="12" height="10" rx="2" fill="#e5484d"/><text x="27" y="41" font-size="10.5" fill="currentColor" fill-opacity="0.85">strata kapitału</text><rect x="112" y="32" width="12" height="10" rx="2" fill="#0b66c3"/><text x="129" y="41" font-size="10.5" fill="currentColor" fill-opacity="0.85">wymagany zysk do powrotu na szczyt</text><text x="142" y="81" font-size="11" fill="currentColor" fill-opacity="0.8" text-anchor="end">strata 10%</text><rect x="150" y="66" width="4.89" height="10" rx="1.5" fill="#e5484d"/><rect x="150" y="79" width="5.38" height="10" rx="1.5" fill="#0b66c3"/><text x="160" y="88" font-size="11" fill="#0b66c3" font-family="monospace">11%</text><text x="142" y="119" font-size="11" fill="currentColor" fill-opacity="0.8" text-anchor="end">strata 25%</text><rect x="150" y="104" width="12.22" height="10" rx="1.5" fill="#e5484d"/><rect x="150" y="117" width="16.13" height="10" rx="1.5" fill="#0b66c3"/><text x="171" y="126" font-size="11" fill="#0b66c3" font-family="monospace">33%</text><text x="142" y="157" font-size="11" fill="currentColor" fill-opacity="0.8" text-anchor="end">strata 50%</text><rect x="150" y="142" width="24.44" height="10" rx="1.5" fill="#e5484d"/><rect x="150" y="155" width="48.89" height="10" rx="1.5" fill="#0b66c3"/><text x="204" y="164" font-size="11" fill="#0b66c3" font-family="monospace">100%</text><text x="142" y="195" font-size="11" fill="currentColor" fill-opacity="0.8" text-anchor="end">strata 75%</text><rect x="150" y="180" width="36.67" height="10" rx="1.5" fill="#e5484d"/><rect x="150" y="193" width="146.67" height="10" rx="1.5" fill="#0b66c3"/><text x="302" y="202" font-size="11" fill="#0b66c3" font-family="monospace">300%</text><text x="142" y="233" font-size="11" fill="currentColor" fill-opacity="0.8" text-anchor="end">strata 90%</text><rect x="150" y="218" width="44" height="10" rx="1.5" fill="#e5484d"/><rect x="150" y="231" width="440" height="10" rx="1.5" fill="#0b66c3"/><text x="595" y="240" font-size="11" fill="#0b66c3" font-family="monospace">900%</text><text x="10" y="280" font-size="10.5" fill="currentColor" fill-opacity="0.6">Strata 50% wymaga 100% zysku, strata 90% wymaga 900%. Ten sam ubytek w procentach kosztuje coraz więcej.</text></svg>
<figcaption>Asymetria odrabiania straty. Czerwone słupki to strata kapitału, niebieskie to zysk potrzebny, aby wrócić na szczyt, w tej samej skali. Przy stracie 10% oba słupki są niemal równe (zysk 11%), lecz przy stracie 50% wymagany zysk to już 100%, przy 75% aż 300%, a przy 90% aż 900%. Strata rośnie liniowo, wymagany zysk eksplozyjnie.</figcaption>
</figure>

## Dlaczego głębokość jest groźna nieliniowo

Ta asymetria nie rośnie liniowo, tylko przyspiesza. Wymagany zysk jest funkcją wypukłą: każdy kolejny punkt procentowy obsunięcia kosztuje więcej niż poprzedni. Tempo tego wzrostu opisuje pochodna, która sama rośnie bez ograniczeń, gdy zbliżasz się do utraty całości.

```
tempo wzrostu wymaganego zysku:  g'(d) = 1 / (1 − d)²     (dąży do nieskończoności, gdy d → 1)

z 10% na 20% obsunięcia:  wymagany zysk rośnie z 11,1% do 25,0%    (+13,9 pkt proc.)
z 70% na 80% obsunięcia:  wymagany zysk rośnie z 233,3% do 400,0%  (+166,7 pkt proc.)
```

Porównaj oba odcinki. W obu przypadkach obsunięcie pogłębia się o dokładnie te same 10 punktów procentowych, a jednak drugi z nich kosztuje ponad dziesięć razy więcej dodatkowego zysku. To jest sedno, dlaczego głębokie obsunięcie jest groźne w sposób, którego liniowa intuicja nie łapie. Pierwsze punkty obsunięcia są tanie w odrobieniu i mieszczą się w normalnym koszcie prowadzenia strategii. Ostatnie punkty są rujnujące, bo wymagany zysk eksploduje do nieskończoności, gdy kapitał zbliża się do zera.

Do tego dochodzi efekt, o którym czysta arytmetyka milczy, a który jeszcze pogarsza sprawę. Po głębokim obsunięciu handluje się zwykle mniejszym kapitałem i z mniejszą pewnością, więc realnie osiągany zwrot na odbiciu bywa niższy, a to wydłuża czas pod wodą. Głęboki zjazd zabiera więc dwa razy: raz przez wykładniczo rosnący wymagany zysk, drugi raz przez czas potrzebny, żeby ten zysk w ogóle uzbierać.

## Obsunięcie a zmienność: co naprawdę boli

Standardową miarą ryzyka jest zmienność, czyli odchylenie standardowe zwrotów. Ma jednak wadę, która dla praktyka jest zasadnicza: jest symetryczna i ślepa na ścieżkę. Zmienność traktuje ruch o +3% i o −3% identycznie i w ogóle nie patrzy na kolejność zwrotów. Tymczasem inwestor nie odczuwa rozproszenia wokół średniej. Odczuwa odległość od szczytu i długość okresu pod wodą. A to jest właśnie obsunięcie, wielkość zależna od ścieżki, a nie od samego rozrzutu.

Różnicę widać najlepiej na prostym eksperymencie myślowym. Weź dwie strategie o identycznej zmienności. Jedna rozkłada straty równomiernie i przypadkowo w czasie. Druga ma tendencję do zbijania strat w serie, jedna zła transakcja pociąga następną pod ten sam reżim rynku. Odchylenie standardowe obu może być takie samo co do grosza, a mimo to druga strategia zaliczy znacznie głębsze maksymalne obsunięcie, bo jej straty się kumulują. To jest dokładnie obserwacja Goldberga i Mahmoud: drawdown wyłapuje seryjną korelację zwrotów i ich układ w czasie, których zmienność liczona w standardowy sposób nie widzi. Dlatego obsunięcie jest miarą ryzyka bliższą temu, co inwestor faktycznie przeżywa.

## CDaR: formalna miara ogona obsunięć

Samo maksymalne obsunięcie ma słabość: to jedna liczba, najgorszy pojedynczy punkt na całej ścieżce. Jest przez to wrażliwe na przypadek i niewygodne w optymalizacji. Odpowiedzią jest miara, która patrzy nie na jeden punkt, tylko na cały ogon najgorszych obsunięć. To Conditional Drawdown at Risk (CDaR), zaproponowana przez Chekhlova, Uryaseva i Zabarankina. Jest zbudowana wobec procesu obsunięć tak samo, jak Conditional Value at Risk (CVaR) jest zbudowana wobec rozkładu strat.

```
proces obsunięcia:  DD(t) = ( M(t) − V(t) ) / M(t)
DaR_α  (kwantyl):   próg, który obsunięcie przekracza tylko w (1 − α) najgorszych przypadkach
CDaR_α:             średnia z tych (1 − α) najgłębszych obsunięć  (średnia ogona)

α → 1:   CDaR dąży do maksymalnego obsunięcia (MDD)
α = 0:   CDaR równa się średniemu obsunięciu (AvDD)
```

Piękno tej konstrukcji polega na tym, że jednym parametrem α reguluje się, jak dużą część ogona bierze się pod uwagę. Przy α blisko jedynki CDaR zbliża się do maksymalnego obsunięcia, czyli do najczarniejszego scenariusza. Przy α równym zero staje się po prostu średnim obsunięciem. Cała rodzina miar między średnim a maksymalnym zjazdem mieści się na jednej pokrętce. Co równie ważne, CDaR jest funkcją wypukłą i porządną miarą ryzyka, więc daje się wstawić jako ograniczenie do optymalizacji portfela metodami programowania liniowego, w przeciwieństwie do surowego maksymalnego obsunięcia, które jest w rachunku niewygodne.

Goldberg i Mahmoud postawili drawdown na formalnym fundamencie od strony teoretycznej. Ich Conditional Expected Drawdown (CED) to średnia ogona rozkładu maksymalnych obsunięć. Pokazali, że jest to miara odchylenia, że jest wypukła i, co kluczowe, że jest czuła na seryjną korelację zwrotów, której zmienność nie widzi. Innymi słowy ogon obsunięć to nie tylko liczba do raportu. To matematycznie dobrze zachowująca się wielkość, którą można świadomie ograniczać.

## Obsunięcie, wielkość pozycji i Kelly

Tu obsunięcie spina się z wielkością pozycji, bo drawdown to nie tylko miara opisowa po fakcie. To zmienna, którą można ograniczać z góry, dobierając lot. Punkt wyjścia jest niewygodny: pełny Kelly, czyli frakcja maksymalizująca długoterminowe tempo wzrostu, ma około 50% szans, że po drodze obsunie kapitał o połowę. Gra ułamkiem pełnego Kelly'ego tnie to ryzyko bardzo szybko.

```
idealizacja ciągła, gra ułamkiem λ pełnego Kelly'ego:
P(kapitał kiedykolwiek spadnie do frakcji c swojej wartości) = c^(2/λ − 1)

λ = ułamek pełnego Kelly'ego  (λ = 1 to pełny Kelly)
c = docelowy poziom           (c = 0,5 to utrata połowy)

pełny Kelly (λ = 1):    P(spadek o połowę) = 0,5^1 = 50%
pół Kelly   (λ = 0,5):  P(spadek o połowę) = 0,5^3 = 12,5%
```

Formalizuje to Kelly z limitem obsunięcia w ujęciu Bussetiego i Boyda. Zamiast maksymalizować samo tempo wzrostu, szuka się największej frakcji spełniającej twardy warunek na prawdopodobieństwo głębokiego zjazdu.

```
maksymalizuj   E[ log(1 + f · r) ]
przy warunku   P( obsunięcie > próg ) ≤ α

przykład:  próg = 30% kapitału,   α = 10%
```

To zamyka klamrę. Arytmetyka odrabiania mówi, że głębokie obsunięcie jest nieliniowo drogie. CDaR mówi, że tym, co warto mierzyć, jest cały ogon obsunięć, a nie jeden punkt. Kelly z limitem obsunięcia mówi, jak ograniczyć prawdopodobieństwo, że ten ogon się zrealizuje, i wprost zamienia zadany limit obsunięcia na dopuszczalną frakcję kapitału, czyli na wielkość pozycji. Trzy warstwy, jedna zmienna: obsunięcie.

## Jak myśleć o obsunięciu

Z całej tej matematyki płynie jedna zasada. Obsunięcie, a nie zmienność, jest miarą ryzyka najbliższą temu, co inwestor faktycznie przeżywa, bo mierzy odległość od szczytu i czas pod wodą, a nie abstrakcyjny rozrzut. Głębokie obsunięcie jest przy tym groźne w sposób nieliniowy: zysk potrzebny do jego odrobienia rośnie szybciej niż sama strata i przy dużej głębokości staje się praktycznie nieosiągalny. Dlatego twardym limitem ryzyka warto uczynić dopuszczalne obsunięcie, a nie dopuszczalną zmienność. Nie chodzi o to, żeby unikać każdego zjazdu, bo płytkie obsunięcia to normalny koszt gry. Chodzi o to, żeby nigdy nie wejść w strefę, z której arytmetyka odrabiania już nie pozwala wrócić.

To nie jest porada inwestycyjna. To wykład matematyki obsunięcia kapitału i tego, dlaczego głębokość zjazdu, a nie odchylenie standardowe, jest właściwą miarą ryzyka. Źródła: Chekhlov, Uryasev, Zabarankin (Conditional Drawdown at Risk, miara obsunięcia w optymalizacji portfela), Goldberg i Mahmoud (teoria drawdown i Conditional Expected Drawdown, 2017), w tle Busseti i Boyd (risk-constrained Kelly, 2016). Fakty o odrabianiu strat, wzór g(d) = d/(1−d), są algebraiczne i pewne; liczby w tabeli to jego bezpośrednie przeliczenia, nie dane rynkowe.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
