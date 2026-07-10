---
title: "CAPM i faktory. Skąd bierze się zwrot ponad rynek"
description: "CAPM Sharpe'a (1964, Nobel 1990) obiecywał, że jedynym wynagradzanym ryzykiem jest beta względem rynku. Przekrój zwrotów akcji tej obietnicy nie potwierdził: Fama i French pokazali niemal płaską zależność zwrotu od bety i zbudowali model trójczynnikowy, Carhart dodał momentum, a wersja z 2015 roku rentowność i inwestycje. Do tego przestroga o zoo faktorów: setki ogłoszonych odkryć, w większości artefakty wielokrotnego testowania, próg t powyżej 3 według Harveya, Liu i Zhu oraz spadek zwrotów predyktorów o 58% po publikacji według McLeana i Pontiffa."
date: 2026-07-06 11:00:00 +0200
eyebrow: "Edukacja · portfel"
dek: "Po Markowitzu wiadomo, jak składać portfel. Zostaje pytanie, ile powinno zarabiać pojedyncze aktywo. CAPM odpowiedział jedną grecką literą: tyle, ile wynika z bety względem rynku. Dane odpowiedziały inaczej i z gruzów pięknego modelu wyrosły faktory, a potem ich patologia: zoo setek odkryć, z których większość nie przeżywa ani rygoru statystycznego, ani własnej publikacji."
readingTime: 8
tags: [CAPM, beta, Sharpe, "Fama i French", SMB, HML, momentum, Carhart, "model trójczynnikowy", "model pięcioczynnikowy", "zoo faktorów", "wielokrotne testowanie", "data mining", "premia za ryzyko", quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - CAPM (Sharpe 1964, Nobel 1990) wyprowadza z równowagi rynkowej jedną mocną obietnicę: jedynym wynagradzanym ryzykiem jest ryzyko systematyczne mierzone betą względem portfela rynkowego. Ryzyko specyficzne da się zdywersyfikować, więc rynek za nie nie płaci, a oczekiwany zwrot każdego aktywa to stopa wolna od ryzyka plus beta razy premia rynkowa.
> - Empiria tej obietnicy nie potwierdziła. Fama i French (1992) pokazali, że po kontroli wielkości spółki związek między betą a średnim zwrotem jest niemal płaski, a przekrój zwrotów lepiej opisują wielkość i wskaźnik wartości księgowej do ceny. Model trójczynnikowy (1993) dodał do rynku faktory SMB i HML, Carhart (1997) dołożył momentum, a model pięcioczynnikowy (2015) rentowność i inwestycje.
> - Interpretacja premii pozostaje sporna: wynagrodzenie za ryzyko złych czasów (wtedy premia może trwać, bo trzeba ją odpracować w krachu) albo anomalia behawioralna z błędów wyceny (wtedy nagłośnienie i napływ kapitału powinny ją dławić). Od rozstrzygnięcia zależy trwałość każdej premii.
> - Zoo faktorów to przestroga: literatura wyprodukowała setki kandydatów, w większości artefakty wielokrotnego testowania. Harvey, Liu i Zhu (2016): przy tej skali przeszukiwania nowy faktor powinien przekraczać próg t powyżej 3, nie klasyczne 2. McLean i Pontiff (2016): zwroty opublikowanych predyktorów są średnio o 26% niższe poza próbą i o 58% niższe po publikacji. Rygor przeżyło niewiele: rynek, wartość, momentum, jakość.

**Teza w jednym zdaniu:** CAPM dał finansom język (beta, alfa, premia za ryzyko), faktory Famy, Frencha i Carharta opisały to, czego ten język nie tłumaczył, a zoo faktorów nauczyło, że dane torturowane dostatecznie długo wyznają wszystko, więc zaufanie należy się tylko tym premiom, które przeżyły podniesiony próg istotności, test poza próbą i własną publikację.

## CAPM: jedna beta ma wycenić wszystko

Markowitz pokazał, jak racjonalny inwestor powinien składać portfel. Sharpe poszedł o krok dalej i zapytał, co stanie się z cenami aktywów, jeżeli tak zachowają się wszyscy naraz. Odpowiedź, opublikowana w 1964 roku jako "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk" (Journal of Finance), przyniosła mu Nagrodę Nobla (1990, wspólnie z Markowitzem i Millerem) i zdefiniowała język finansów na dekady. W równowadze CAPM każdy inwestor trzyma kombinację dwóch składników: instrumentu wolnego od ryzyka i portfela rynkowego. A skoro wszyscy trzymają rynek, ryzyko specyficzne pojedynczej spółki nie ma prawa być wynagradzane, bo w portfelu rynkowym jest rozpuszczone, dokładnie tak, jak opisuje to teoria portfela. Wyceniane może być tylko to, czego zdywersyfikować się nie da: wkład aktywa w ryzyko całego rynku. Ten wkład mierzy beta.

```
E[Rᵢ] = Rf + βᵢ · (E[Rm] − Rf)

βᵢ = Cov(Rᵢ, Rm) / Var(Rm)

Rf           = stopa wolna od ryzyka
E[Rm] − Rf   = premia rynkowa (zapłata za ryzyko systematyczne)
βᵢ           = beta: wrażliwość zwrotów aktywa i na zwroty rynku
```

Wnioski są mocne i przyjemnie testowalne. Istnieje dokładnie jedno wynagradzane ryzyko: ekspozycja na rynek. Zmienność sama w sobie nie jest wynagradzana, więc aktywo o dużych wahaniach, ale zerowej korelacji z rynkiem, powinno zarabiać tyle co instrument wolny od ryzyka (beta zero zeruje cały drugi składnik wzoru). Średnie zwroty rosną liniowo z betą: portfel o becie dwa powinien mieć dwa razy większą nadwyżkę nad stopę wolną od ryzyka niż rynek. I wreszcie alfa, czyli zwrot ponad to, co wynika z bety, powinna w równowadze wynosić zero dla każdego aktywa. Jedna linia na wykresie, wszystkie aktywa na niej. Trudno o piękniejszą hipotezę do obalenia.

## Zderzenie z danymi: beta nie tłumaczy przekroju

Wątpliwości empiryczne narastały latami, ale symboliczny cios przyszedł w 1992 roku. Fama i French w "The Cross-Section of Expected Stock Returns" (Journal of Finance) sprawdzili na przekroju amerykańskich akcji, czy beta rzeczywiście tłumaczy, dlaczego jedne spółki zarabiają średnio więcej od innych. Wynik: po kontroli wielkości spółki zależność między betą a średnim zwrotem jest niemal płaska. Portfele o wysokiej becie nie zarabiały wyraźnie więcej niż portfele o niskiej, czyli jedyna zmienna, która według CAPM ma się liczyć, nie działała. Działały za to dwie charakterystyki, które w modelu nie miały prawa istnieć: kapitalizacja (małe spółki zarabiały średnio więcej niż duże) i stosunek wartości księgowej do ceny (spółki tanie względem księgi biły drogie spółki wzrostowe).

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">CAPM kontra dane: średni zwrot względem bety</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">średni zwrot portfela</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">beta względem rynku</text><circle cx="92" cy="205" r="3" fill="currentColor" opacity="0.5"/><text x="84" y="209" font-size="10" fill="currentColor" opacity="0.7" text-anchor="end">Rf</text><line x1="92" y1="205" x2="566" y2="78" stroke="#0b66c3" stroke-width="2.2"/><text x="380" y="98" font-size="10.5" fill="#0b66c3">CAPM: nachylenie = premia rynkowa</text><circle cx="150" cy="184" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="210" cy="190" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="270" cy="180" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="330" cy="186" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="390" cy="173" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="450" cy="180" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="510" cy="168" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="545" cy="176" r="2.6" fill="currentColor" opacity="0.3"/><line x1="92" y1="188" x2="566" y2="170" stroke="#e5484d" stroke-width="2.2" stroke-dasharray="6 5"/><text x="330" y="212" font-size="10.5" fill="#e5484d">empiria: związek bety ze zwrotem niemal płaski</text></svg>
<figcaption>Każdy punkt to portfel akcji sortowany po becie. CAPM przewiduje, że średnie zwroty leżą na rosnącej linii o nachyleniu równym premii rynkowej (niebieska). Fama i French (1992) pokazali obraz bliższy czerwonej przerywanej: po kontroli wielkości spółki zależność jest niemal płaska, niska beta zarabia za dużo względem teorii, a wysoka za mało.</figcaption>
</figure>

Dla teorii to było trzęsienie ziemi: model przewidywał jedną rosnącą linię, a dane pokazały poziomą kreskę i dwie zmienne spoza modelu, które robiły całą robotę.

## Od jednego czynnika do pięciu

Rok później Fama i French zamienili charakterystyki w czynniki. W "Common Risk Factors in the Returns on Stocks and Bonds" (Journal of Financial Economics, 1993) obok rynku pojawiły się dwa portfele long-short: SMB, długi w małych spółkach i krótki w dużych, oraz HML, długi w spółkach o wysokim stosunku wartości księgowej do ceny i krótki w tych o niskim.

```
E[Rᵢ] − Rf = bᵢ·(E[Rm] − Rf) + sᵢ·E[SMB] + hᵢ·E[HML]

SMB = Small Minus Big    czynnik wielkości (małe minus duże)
HML = High Minus Low     czynnik wartości (wysokie B/M minus niskie)
```

Filozofia pozostała CAPM-owa, zmieniła się tylko liczba wynagradzanych ryzyk: oczekiwany zwrot to suma ekspozycji na czynniki systematyczne pomnożonych przez ich premie, a alfa to reszta, której czynniki nie tłumaczą. W 1997 roku Carhart w "On Persistence in Mutual Fund Performance" (Journal of Finance 52(1)) dołożył czwarty czynnik, momentum: portfel długi w akcjach o najwyższych zwrotach z ostatniego roku i krótki w najsłabszych. Powód był praktyczny. Carhart badał, czy fundusze z dobrą historią dalej wygrywają, i pokazał, że utrzymywanie się wyników w dużej mierze tłumaczą mechaniczna ekspozycja na momentum oraz koszty, a nie powtarzalny talent zarządzających. Model czteroczynnikowy na lata stał się standardowym benchmarkiem oceny funduszy: zanim komuś przypisze się alfę, trzeba najpierw odjąć wszystko, co da się kupić tanio i mechanicznie.

W 2015 roku Fama i French rozszerzyli model do pięciu czynników ("A Five-Factor Asset Pricing Model", Journal of Financial Economics), dodając rentowność (RMW, spółki o solidnej rentowności operacyjnej minus słabe) i inwestycje (CMA, spółki inwestujące konserwatywnie minus agresywnie powiększające aktywa). Motywacja przyszła z algebry wyceny: przy ustalonej cenie względem wartości księgowej wyższa oczekiwana rentowność i niższe inwestycje implikują wyższy oczekiwany zwrot. Ciekawostka z samej pracy: po dodaniu tych dwóch czynników klasyczny HML robi się w dużej mierze zbędny, bo jego premię przejmują pozostałe. A momentum, jedna z najsilniejszych regularności w danych, do modelu Famy i Frencha nie weszło nigdy.

```
1964  CAPM       rynek (beta)
1992  diagnoza   beta nie tłumaczy przekroju zwrotów
1993  FF3        rynek + SMB (wielkość) + HML (wartość)
1997  Carhart    FF3 + momentum (zwycięzcy minus przegrani)
2015  FF5        rynek + SMB + HML + RMW (rentowność) + CMA (inwestycje)
```

## Premia za ryzyko czy błąd wyceny

To, że małe, tanie i rozpędzone spółki zarabiały historycznie więcej, jest faktem statystycznym. Spór dotyczy tego, dlaczego, i ma dwie strony o zupełnie różnych konsekwencjach.

Interpretacja racjonalna mówi: premie faktorowe to zapłata za ryzyko. Strategia value boli dokładnie wtedy, gdy boli wszystko inne, bo tanie spółki to często firmy zadłużone i cykliczne, podatne na kłopoty w recesji. Kto trzyma taki portfel, nosi ryzyko złych czasów, a rynek za noszenie ryzyka płaci średnią premią, podobnie jak ubezpieczyciel każe sobie płacić za przejęcie cudzego ryzyka. Konsekwencja: premia może trwać długo po odkryciu, bo nie jest darmowym obiadem, tylko wynagrodzeniem, które trzeba odpracować w krachu.

Interpretacja behawioralna mówi: premie to ślady systematycznych błędów wyceny. Inwestorzy ekstrapolują wzrost i przepłacają za spółki z efektowną historią, a nudne i tanie zostawiają w tyle; nadreakcja, moda i niechęć do przyznawania się do błędu robią resztę. Konsekwencja jest odwrotna: skoro premia bierze się z cudzych pomyłek, nagłośnienie jej w literaturze i napływ kapitału powinny ją systematycznie dławić.

Ten spór nie jest rozstrzygnięty i obie historie potrafią wyjaśnić te same historyczne średnie. Różnią się jednak jedną przewidywalną konsekwencją: tym, co powinno stać się ze zwrotami po publikacji odkrycia. A to akurat da się zmierzyć.

## Zoo faktorów: kiedy odkryć jest za dużo

Model trójczynnikowy otworzył złotą żyłę. Skoro rynek nie jest jedynym wycenianym czynnikiem, każda zmienna, która w regresji przekrojowej "działa", może zostać ogłoszona nowym faktorem. Literatura dostarczyła setki takich kandydatów i w pewnym momencie przestało to być przyrostem wiedzy, a stało się problemem, który doczekał się własnej nazwy: zoo faktorów.

Harvey, Liu i Zhu w "... and the Cross-Section of Expected Returns" (2016) skatalogowali czynniki ogłoszone w literaturze i policzyli, co z tej skali wynika dla statystyki. Sedno jest proste: klasyczny próg istotności t powyżej 2, odpowiadający około 5% szans na fałszywy alarm, jest skalibrowany na jeden test. Gdy testów są setki, fałszywe odkrycia przestają być ryzykiem, a stają się arytmetyczną pewnością.

```
pojedynczy test, próg t > 2:
P(fałszywy alarm) ≈ 5%

100 niezależnych testów przy tym samym progu:
P(co najmniej jeden fałszywy alarm) = 1 − 0.95¹⁰⁰ ≈ 99.4%
```

Do tego dochodzi selekcja publikacyjna: wynik "działa" znacznie łatwiej opublikować niż "nie działa", więc literatura pokazuje wierzchołek góry przeszukiwań, a nieudane warianty (inne okno, inna definicja, inny rynek) zostają w szufladach i nie wchodzą do rachunku. Rekomendacja Harveya, Liu i Zhu: nowo ogłaszany faktor powinien przekraczać próg t powyżej 3, nie klasyczne 2, i to jako minimum, bo poprzeczka rośnie z każdym kolejnym przeszukaniem tych samych danych. Ich wniosek, postawiony wprost, brzmi niewygodnie dla całej dziedziny: większość ogłoszonych odkryć jest przy takim rachunku prawdopodobnie fałszywa.

## Test czasu: publikacja zjada premię

McLean i Pontiff w "Does Academic Research Destroy Stock Return Predictability?" (Journal of Finance 71(1), 2016) zmierzyli dokładnie to, co różni obie interpretacje premii. Zebrali predyktory przekroju zwrotów udokumentowane w opublikowanych badaniach i porównali ich wyniki w trzech oknach: w oryginalnej próbie badania, po końcu próby ale jeszcze przed publikacją, oraz po publikacji.

Wyniki układają się w schody w dół. Poza próbą, zanim ktokolwiek przeczytał pracę, zwroty predyktorów są średnio o 26% niższe niż w próbie. To czysty pomiar przeszacowania statystycznego: świat się nie zmienił, zmieniła się tylko próba, więc ta część "odkrycia" była szczęściem konkretnego okresu. Po publikacji spadek pogłębia się do 58%. Ta druga część to ślad uczącego się rynku: kapitał czyta literaturę, wchodzi w nagłośnione strategie i zjada premię.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Co zostaje z odkrycia: zwroty predyktorów w trzech oknach</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">średni zwrot (okres próby = 100)</text><line x1="92" y1="82" x2="604" y2="82" stroke="currentColor" opacity="0.15" stroke-dasharray="3 4"/><rect x="150" y="82" width="100" height="150" fill="#0b66c3" rx="3"/><rect x="298" y="121" width="100" height="111" fill="#1a9e6a" rx="3"/><rect x="446" y="169" width="100" height="63" fill="#e5484d" rx="3"/><text x="200" y="72" font-size="12" fill="currentColor" opacity="0.85" text-anchor="middle">100</text><text x="348" y="111" font-size="12" fill="currentColor" opacity="0.85" text-anchor="middle">74</text><text x="348" y="97" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">o 26% mniej</text><text x="496" y="159" font-size="12" fill="currentColor" opacity="0.85" text-anchor="middle">42</text><text x="496" y="145" font-size="10" fill="currentColor" opacity="0.65" text-anchor="middle">o 58% mniej</text><text x="200" y="252" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle">w próbie badania</text><text x="348" y="252" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle">po próbie, przed publikacją</text><text x="496" y="252" font-size="10.5" fill="currentColor" opacity="0.7" text-anchor="middle">po publikacji</text></svg>
<figcaption>Zwroty przeskalowane tak, że średnia z okresu oryginalnej próby badania wynosi 100 (McLean i Pontiff 2016). Poza próbą, jeszcze przed publikacją, zostaje około 74: spadek o 26% mierzy statystyczne przeszacowanie. Po publikacji zostaje około 42: dodatkowy spadek to rynek, który przeczytał pracę. Do zera jednak nie spada.</figcaption>
</figure>

Równie ważne jest to, czego w danych nie ma: zwroty nie spadają do zera, a zanikanie jest silniejsze tam, gdzie arbitraż jest tani i łatwy. Obraz końcowy jest pośredni i uczciwy. Część premii z literatury to złudzenie próby, dokładnie to, przed czym ostrzega zoo faktorów. Część to błąd wyceny, który po nagłośnieniu dławi kapitał. A reszta może być autentyczną zapłatą za ryzyko, które ktoś musi nosić, żeby ją dostawać.

## Co z tego zostaje

CAPM przegrał jako opis danych, ale wygrał jako język. Beta, alfa, premia za ryzyko, benchmark: cały słownik nowoczesnych finansów pochodzi z tego modelu i nadal pracuje, tyle że w roli układu odniesienia, a nie prawa natury. Gdy ktoś dziś mówi "alfa", mówi "zwrot ponad model czynnikowy", czyli używa konstrukcji Sharpe'a z dłuższą listą czynników.

Z zoo po latach selekcji zostaje krótka lista premii o najmocniejszej reputacji: rynek, wartość, momentum i jakość (rentowność). Każda ma za sobą dekady danych i przetrwała podniesione progi istotności. Cała reszta katalogu jest domyślnie wątpliwa, dopóki nie udowodni, że jest inaczej: poza próbą, po kosztach i po poprawce na liczbę wykonanych testów.

Najszersza lekcja wykracza poza akcje i faktory. Dane torturowane dostatecznie długo wyznają wszystko, więc każde przeszukanie setek kandydatów wyprodukuje odkrycia, które wyglądają jak przewaga, a są szumem. Różnica między wynikiem a artefaktem sprowadza się do progu dowodu: t powyżej 3 zamiast 2, obowiązkowy test poza próbą i założenie, że po nagłośnieniu będzie gorzej. Premie, które przeżyją takie traktowanie, można traktować poważnie. Reszta zostaje w zoo.

To nie jest porada inwestycyjna. To edukacyjne omówienie CAPM, modeli czynnikowych i literatury o wielokrotnym testowaniu: wzory i wyniki badań są zreferowane wiernie, a najważniejsza liczba mówi, że po publikacji z przeciętnej premii zostaje mniej niż połowa.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
