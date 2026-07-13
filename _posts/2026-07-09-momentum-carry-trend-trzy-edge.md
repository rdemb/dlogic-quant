---
title: "Momentum, carry, trend. Trzy klasyczne przewagi i ich ukryte ogony"
description: "Momentum, carry i trend to trzy najlepiej udokumentowane akademicko źródła przewagi w tradingu systematycznym. Tekst tłumaczy, czym każde z nich jest, skąd się bierze (premia za ryzyko albo błąd poznawczy) i dlaczego każde ma swój ogon: momentum crash, carry unwind, whipsaw trendu. Z odniesieniami do prac AQR, Menkhoffa i in., prac roboczych BIS oraz katalogu 151 strategii Kakushadzego i Serura."
date: 2026-07-09 18:00:00 +0200
eyebrow: "Edukacja · strategie"
dek: "Trzy klasyczne przewagi tradingu systematycznego wyglądają jak darmowy obiad, dopóki nie policzy się rachunku. Momentum, carry i trend: skąd biorą się zyski, dlaczego to premia za ryzyko lub efekt behawioralny, a nie magia, i gdzie każde z nich chowa swój ukryty ogon. Rzetelnie, na mechanizmach, bez obiecywania liczb."
readingTime: 8
tags: [momentum, carry, "trend following", "carry trade", "momentum crash", "time-series momentum", "premia za ryzyko", "finanse behawioralne", AQR, Menkhoff, BIS, Kakushadze, walidacja, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Trzy klasyczne, akademicko udokumentowane źródła przewagi to momentum (aktywa, które rosły, przeciętnie rosną dalej w średnim terminie), carry (inkasowanie różnicy stóp procentowych, na przykład kupno waluty wysokoprocentowej za niskoprocentową) oraz trend following (podążanie za długimi ruchami, które wygrywa rzadko, ale grubo). Każde opiera się na innym mechanizmie i ma inny profil wypłaty.
> - Wszystkie trzy tłumaczy się na dwa niewykluczające się sposoby: jako premię za ryzyko (zwrot jest zapłatą za straty w najgorszym momencie) albo jako efekt behawioralny (systematyczny błąd poznawczy, którego arbitraż nie usuwa). W żadnym ujęciu nie jest to darmowy obiad.
> - Dokładnie to, co daje przewagę, produkuje jej ogon. Momentum ma rzadkie, brutalne krachy (momentum crash), carry ma ujemny skos i gwałtowne odwroty (carry unwind), a trend, choć dodatnio skośny, płaci długim krwawieniem w rynku bez kierunku (whipsaw).
> - Realność efektu brutto nie przesądza opłacalności netto. Wysoki obrót topi zwroty w kosztach, a wybór najlepszej parametryzacji z siatki to problem wielokrotnego testowania, ten sam, który koryguje Deflated Sharpe. Katalog w rodzaju 151 strategii to słownik mechanizmów, nie lista zakupów.

**Teza w jednym zdaniu:** Momentum, carry i trend to trzy najlepiej udokumentowane źródła przewagi w tradingu systematycznym, ale żaden nie jest darmowym obiadem, bo każdy płaci się ogonem ryzyka albo znika po kosztach, dlatego liczy się nie samo istnienie efektu, lecz to, czy przetrwa walidację i tarcie.

## Kręgosłup systematycznego tradingu

Trzy nazwy wracają w niemal każdym poważnym katalogu strategii ilościowych: momentum, carry i trend. To nie są chwyty marketingowe ani wskaźniki z pojedynczego backtestu, tylko efekty udokumentowane w recenzowanej literaturze, na wielu rynkach i przez wiele dekad. Zbudowano na nich znaczną część branży zarządzania systematycznego, od funduszy CTA po strategie faktorowe dużych domów badawczych takich jak AQR. Każdy z tych trzech efektów opiera się na innym mechanizmie i każdy ma inny kształt rozkładu zysków. Łączy je jedno: żaden nie jest darmowym obiadem, a cena zwykle bywa ukryta w ogonie rozkładu albo w kosztach transakcyjnych.

<figure>
<svg viewBox="0 0 720 310" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif" role="img" aria-label="Trzy klasyczne źródła przewagi: momentum, carry i trend jako trzy panele pojęciowe">
  <defs>
    <marker id="mct-ah-mom" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="8.5" refY="5.5" orient="auto"><path d="M1,1 L9.5,5.5 L1,10 Z" fill="#0b66c3"/></marker>
    <marker id="mct-ah-tr" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="8.5" refY="5.5" orient="auto"><path d="M1,1 L9.5,5.5 L1,10 Z" fill="#e5484d"/></marker>
  </defs>

  <!-- Panel 1: Momentum -->
  <rect x="15" y="24" width="210" height="272" rx="14" fill="none" stroke="currentColor" stroke-opacity="0.2"/>
  <text x="120" y="52" text-anchor="middle" font-size="17" font-weight="600" fill="#0b66c3">Momentum</text>
  <line x1="90" y1="64" x2="150" y2="64" stroke="#0b66c3" stroke-width="2" stroke-linecap="round" opacity="0.85"/>
  <line x1="40" y1="210" x2="200" y2="210" stroke="currentColor" stroke-opacity="0.28"/>
  <line x1="40" y1="150" x2="200" y2="150" stroke="currentColor" stroke-opacity="0.15"/>
  <polyline points="48,198 70,186 92,192 114,160 136,150" fill="none" stroke="#0b66c3" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="136" cy="150" r="3.6" fill="#0b66c3"/>
  <line x1="136" y1="150" x2="192" y2="110" stroke="#0b66c3" stroke-width="2.6" stroke-dasharray="5 5" stroke-linecap="round" marker-end="url(#mct-ah-mom)"/>
  <text x="120" y="250" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">Cena, która rosła,</text>
  <text x="120" y="270" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">częściej rośnie dalej</text>

  <!-- Panel 2: Carry -->
  <rect x="255" y="24" width="210" height="272" rx="14" fill="none" stroke="currentColor" stroke-opacity="0.2"/>
  <text x="360" y="52" text-anchor="middle" font-size="17" font-weight="600" fill="#1a9e6a">Carry</text>
  <line x1="330" y1="64" x2="390" y2="64" stroke="#1a9e6a" stroke-width="2" stroke-linecap="round" opacity="0.85"/>
  <line x1="300" y1="210" x2="422" y2="210" stroke="currentColor" stroke-opacity="0.28"/>
  <rect x="318" y="168" width="36" height="42" fill="#1a9e6a" fill-opacity="0.2"/>
  <rect x="318" y="112" width="36" height="56" fill="#1a9e6a" fill-opacity="0.85"/>
  <rect x="318" y="112" width="36" height="98" fill="none" stroke="#1a9e6a" stroke-opacity="0.65"/>
  <rect x="372" y="168" width="36" height="42" fill="#1a9e6a" fill-opacity="0.2" stroke="#1a9e6a" stroke-opacity="0.65"/>
  <line x1="318" y1="168" x2="408" y2="168" stroke="currentColor" stroke-opacity="0.3" stroke-dasharray="4 4"/>
  <text x="336" y="104" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.62">różnica</text>
  <text x="336" y="226" text-anchor="middle" font-size="10" fill="currentColor" fill-opacity="0.55">wysoka</text>
  <text x="390" y="226" text-anchor="middle" font-size="10" fill="currentColor" fill-opacity="0.55">niska</text>
  <text x="360" y="250" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">Zbieranie różnicy</text>
  <text x="360" y="270" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">stóp procentowych</text>

  <!-- Panel 3: Trend -->
  <rect x="495" y="24" width="210" height="272" rx="14" fill="none" stroke="currentColor" stroke-opacity="0.2"/>
  <text x="600" y="52" text-anchor="middle" font-size="17" font-weight="600" fill="#e5484d">Trend</text>
  <line x1="572" y1="64" x2="628" y2="64" stroke="#e5484d" stroke-width="2" stroke-linecap="round" opacity="0.85"/>
  <line x1="520" y1="210" x2="690" y2="210" stroke="currentColor" stroke-opacity="0.28"/>
  <line x1="520" y1="150" x2="690" y2="150" stroke="currentColor" stroke-opacity="0.15"/>
  <polyline points="526,198 544,184 560,192 578,168 596,176 614,152 632,160 650,134 668,142 686,120" fill="none" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.8" stroke-linejoin="round"/>
  <line x1="526" y1="200" x2="686" y2="112" stroke="#e5484d" stroke-width="3" stroke-linecap="round" marker-end="url(#mct-ah-tr)"/>
  <text x="600" y="250" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">Podążanie za</text>
  <text x="600" y="270" text-anchor="middle" font-size="12.5" fill="currentColor" fill-opacity="0.72">dłuższym kierunkiem</text>
</svg>
<figcaption>Schemat pojęciowy trzech klasycznych źródeł przewagi: momentum stawia na kontynuację ruchu, carry inkasuje różnicę stóp procentowych, a trend podąża za dłuższym kierunkiem mimo szumu. To ilustracja mechanizmów, nie realne dane.</figcaption>
</figure>

## Momentum: to, co rosło, zwykle rośnie dalej

Momentum w wersji przekrojowej (cross-sectional) polega na rankingu aktywów według stopy zwrotu z ostatnich kilku miesięcy, zwykle od trzech do dwunastu, kupowaniu zwycięzców i sprzedawaniu maruderów. Klasyczna praca Jegadeesha i Titmana z 1993 roku pokazała, że akcje najlepsze w horyzoncie od trzech do dwunastu miesięcy przeciętnie dają wyższe zwroty także w kolejnych miesiącach. Efekt nie ogranicza się do amerykańskich akcji. Asness, Moskowitz i Pedersen w pracy "Value and Momentum Everywhere" (2013) udokumentowali go równolegle w akcjach różnych krajów, obligacjach, surowcach i walutach. Na rynku walutowym momentum opisali między innymi Menkhoff, Sarno, Schmeling i Schrimpf, a wątek podejmowały też prace robocze BIS.

Skąd się bierze? Dominujące wyjaśnienie jest behawioralne: rynek reaguje na informacje zbyt wolno. Inwestorzy kotwiczą się przy starych cenach, zwlekają z realizacją zysków i strat (efekt dyspozycji), a informacja rozchodzi się stopniowo, więc cena dochodzi do nowej równowagi z opóźnieniem, tworząc kontynuację ruchu. Część badaczy dokłada do tego komponent ryzyka. Ważny niuans: momentum jest zjawiskiem średnioterminowym, wciśniętym między krótkoterminową rewersję (horyzont około miesiąca, gdzie ruch często się odwraca) a długoterminową rewersję (trzy do pięciu lat, gdzie przewartościowani zwycięzcy wracają do średniej). Sama etykieta "momentum" bez podanego okresu formowania niewiele znaczy.

## Carry: inkasowanie różnicy stóp procentowych

Carry to zarabianie na różnicy oprocentowania. W wersji walutowej: kupujesz walutę o wysokiej stopie procentowej, finansując to walutą o niskiej stopie, i inkasujesz różnicę, która na rynku FX realizuje się przez punkty swapowe. Teoria w podręcznikowej postaci mówi, że nie powinno to działać. Niepokryty parytet stóp procentowych (UIP) zakłada, że waluta o wyższej stopie osłabi się dokładnie o tyle, ile wynosi przewaga oprocentowania, więc na koniec wyjdzie zero. Empiria uparcie temu przeczy. To słynna zagadka premii terminowej (forward premium puzzle, opisana między innymi przez Famę w 1984 roku): waluty wysokoprocentowe przeciętnie nie osłabiają się dostatecznie, a bywa, że się umacniają, więc carry przynosi dodatni średni zwrot.

Za co płaci ten zwrot? Menkhoff, Sarno, Schmeling i Schrimpf w pracy "Carry Trades and Global Foreign Exchange Volatility" (2012) pokazali, że zyski z carry to w dużej mierze wynagrodzenie za ryzyko globalnej zmienności walutowej: strategia zarabia spokojnie, dopóki rynek jest spokojny, i obrywa dokładnie wtedy, gdy globalna zmienność skacze. Koijen, Moskowitz, Pedersen i Vrugt w pracy "Carry" (2018) uogólnili to pojęcie na obligacje, surowce i akcje, pokazując, że carry jest ogólną zasadą wyceny, a nie ciekawostką z rynku FX. Cena za tę premię jest specyficzna i wraca w dalszej części: rozkład zysków z carry ma gruby, ujemny ogon.

## Trend following: rzadko, ale grubo

Trend following to wersja szeregowo-czasowa (time-series) tej samej rodziny co momentum, tyle że patrzy na własną historię instrumentu, a nie na ranking względem innych. Zasada jest prosta: jeśli instrument rósł w ostatnich miesiącach, zajmij pozycję długą, jeśli spadał, krótką, i rób to jednocześnie na wielu słabo skorelowanych rynkach kontraktów terminowych. Moskowitz, Ooi i Pedersen w pracy "Time Series Momentum" (2012) udokumentowali ten efekt na dziesiątkach rynków. Zespół AQR w opracowaniu "A Century of Evidence on Trend-Following Investing" pokazał, że podejście działało w przybliżeniu przez stulecie i w bardzo różnych reżimach.

Najważniejsza jest tu geometria wypłaty, odwrotna niż w carry. Trend following ma dodatni skos: dużo małych strat i garść dużych zysków, przy niskiej trafności pojedynczej transakcji. Wygrywa się rzadko, ale kiedy już trend się złapie, jeden zysk potrafi pokryć długą serię drobnych wpadek. Ten profil bywa nazywany "długą opcjonalnością" albo długą pozycją w zmienności: strategia zachowuje się jak kupione ubezpieczenie, które najwięcej płaci w przedłużonych kryzysach, stąd popularne określenie "crisis alpha". To fundament branży CTA i funduszy managed futures. Ogon również tu istnieje, tylko przybiera inny kształt.

## Wspólny mianownik: premia za ryzyko albo błąd poznawczy

Mimo różnych mechanizmów wszystkie trzy efekty tłumaczy się na dwa sposoby, które się nie wykluczają. Pierwszy to premia za ryzyko: zwrot jest zapłatą za to, że strategia traci właśnie wtedy, gdy boli najmocniej, czyli w kryzysie, przy skoku zmienności, w recesji. Inwestor dostaje z góry premię za gotowość do trzymania czegoś, co zawiedzie w najgorszym momencie. Drugi to efekt behawioralny: systematyczny błąd poznawczy (niedoreagowanie, przereagowanie, stadność), którego arbitraż nie usuwa, bo napotyka granice w postaci kosztów, ryzyka i ograniczonego kapitału cierpliwych graczy.

Kluczowy wniosek jest taki, że w żadnym z tych ujęć nie ma darmowego obiadu. Jeśli coś płaci jako premia za ryzyko, to z definicji musi czasem boleć, inaczej premia zostałaby wyarbitrażowana do zera. Jeśli płaci jako efekt behawioralny, to jego trwałość zależy od tego, że większość graczy nie wytrzyma dyskomfortu albo cierpliwości potrzebnej do jego zbierania. Najmocniejszym argumentem za realnością tych trzech efektów, podnoszonym konsekwentnie przez AQR, jest ich wszechobecność i trwałość: ten sam mechanizm widać w akcjach, obligacjach, surowcach i walutach, przez dekady. Powtarzalność na wielu niezależnych rynkach jest znacznie trudniejsza do zbycia jako przypadek niż pojedynczy ładny backtest.

## Każda przewaga ma swój ogon

Tu robi się niewygodnie, bo dokładnie to, co daje przewagę, produkuje jej ogon.

Momentum crash. Momentum kupuje ostatnich zwycięzców i shortuje ostatnich maruderów. Po głębokiej bessie, gdy rynek gwałtownie odbija, najmocniej odbijają właśnie najbardziej przecenione spółki, czyli te, które strategia trzyma na krótko. Efektem jest rzadka, ale brutalna strata. Daniel i Moskowitz w pracy "Momentum Crashes" (2016) pokazali, że rozkład zysków z momentum ma ujemny skos, a jego wypłata w stresie przypomina wystawioną, czyli krótką, opcję na rynek: spokojny dochód przez długi czas, po czym nagłe, duże cięcie przy odwrocie.

Carry unwind. Carry ma ten sam ujemny skos, tylko z innego powodu. Waluty wysokoprocentowe to zwykle waluty ryzykowne. Kiedy nastaje risk-off, wszyscy zamykają te same pozycje w tym samym momencie, płynność wysycha i uruchamia się spirala, którą opisali Brunnermeier, Nagel i Pedersen w "Carry Trades and Currency Crashes" (2008). Stąd popularne, bezlitosne porównanie: carry to zbieranie drobniaków przed nadjeżdżającym walcem. Rośnie schodami, spada windą.

Whipsaw trendu. Trend following ma skos dodatni, więc jego ogon nie jest pojedynczym wybuchem, lecz przewlekłym krwawieniem. W rynku bez kierunku, piłującym w wąskim zakresie i szarpanym newsami, strategia wchodzi za późno, wychodzi za późno i zbiera serię drobnych strat, jedna po drugiej. Ceną nie jest tu jeden dramatyczny dzień, tylko długie, męczące obsunięcia, które testują dyscyplinę, zanim pojawi się trend spłacający rachunek. Innymi słowy: carry i momentum sprzedają spokój i płacą katastrofą, trend kupuje katastrofę i płaci nudą.

## Koszty, tarcie i dyscyplina walidacji

Do tego dochodzi warstwa, która w praktyce topi wiele z tych przewag: koszty. Momentum i szybszy trend mają wysoki obrót portfela, a każde przetasowanie to spread, poślizg i wpływ na rynek. Zwroty brutto z prac akademickich potrafią być wielokrotnie wyższe niż to, co realnie zostaje po odjęciu kosztów, zwłaszcza na detalicznych spreadach FX. To stały motyw każdego uczciwego researchu: efekt bywa prawdziwy brutto i jednocześnie nieopłacalny netto.

Druga pułapka jest statystyczna. To, że momentum, carry i trend istnieją w literaturze, nie znaczy, że akurat twoja parametryzacja, czyli konkretny okres formowania, konkretny próg i konkretna para, jest istotna. Wybierając najlepszy wariant z siatki kilkudziesięciu konfiguracji, wracasz do problemu wielokrotnego testowania: najlepszy z wielu losowych wyników prawie zawsze wygląda nieźle. To dokładnie ten sam mechanizm, który koryguje Deflated Sharpe Ratio, opisany w osobnym tekście na tym blogu: Sharpe trzeba zdeflatować o liczbę wypróbowanych prób, zanim uzna się go za dowód. Trwałość efektu na wielu rynkach broni samego mechanizmu, ale nie broni pojedynczego dopasowania.

Na koniec katalogi. Praca "151 Trading Strategies" Kakushadzego i Serura (2018) to użyteczna mapa mechanizmów, encyklopedia pomysłów wraz z formułami. Ale sama jej objętość jest ostrzeżeniem: przy stu pięćdziesięciu jeden kandydatach kilka będzie wyglądać świetnie czysto z przypadku. Katalog jest cenny jako słownik mechanizmów i groźny jako lista zakupów. Różnica między jednym a drugim to właśnie dyscyplina walidacji: znajomość źródła przewagi, jej ogona i jej kosztu.

## Co z tego wynika przy stole

Momentum, carry i trend są kręgosłupem tradingu systematycznego nie dlatego, że są darmowe, lecz dlatego, że mają nazwany mechanizm oraz są wszechobecne i trwałe. Uczciwa forma myślenia o każdej przewadze brzmi tak: da się podać jej źródło (dlaczego w ogóle płaci, premia za ryzyko czy błąd poznawczy), jej ogon (kiedy i jak boli) oraz jej koszt (ile zabiera tarcie). Jeśli tych trzech rubryk nie da się wypełnić, to nie jest przewaga, tylko krzywa dopasowana do przeszłości.

To nie jest porada inwestycyjna. To szkic mechanizmów, pokazany po to, żeby odróżnić udokumentowane źródło przewagi od ładnie wyglądającego backtestu, i żeby pamiętać, że nawet realny efekt ma swój ogon i swój rachunek za tarcie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
