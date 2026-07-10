---
title: "Czy analiza techniczna działa. 30 lat badań w jednym tekście"
description: "Sześć prac z czołowych czasopism finansowych, od Brocka, Lakonishoka i LeBarona (1992) po Bajgrowicza i Scailleta (2012), układa się w jedną odpowiedź: informacja w cenach istnieje, ale po kosztach transakcyjnych i po korekcie na data snooping praktycznie żadna prosta reguła nie przeżywa, a realne przewagi wygasają wraz z adaptacją rynku."
date: 2026-07-07 12:00:00 +0200
eyebrow: "Edukacja · paradygmaty"
dek: "Na YouTube analiza techniczna albo gwarantuje zyski, albo jest szarlatanerią. Recenzowana literatura ma odpowiedź ciekawszą od obu skrajności: od pracy, która dała średnim kroczącym akademicką wiarygodność, przez rachunek za przeszukanie 7846 reguł, po dowód, że dawne przewagi na FX były realne i wygasły. Trzy dekady badań w jednym tekście."
readingTime: 9
tags: ["analiza techniczna", "data snooping", "koszty transakcyjne", "Reality Check", "False Discovery Rate", "Brock Lakonishok LeBaron", "Sullivan Timmermann White", "Lo Mamaysky Wang", "Park Irwin", "Neely Weller Ulrich", "Bajgrowicz Scaillet", "hipoteza rynków adaptacyjnych", "teoria Dowa", "głowa z ramionami", backtest, Forex, quant]
category: edukacja
---

> **W skrócie**
>
> - Brock, Lakonishok i LeBaron (Journal of Finance, 1992) pokazali na indeksie DJIA z lat 1897-1986, że proste średnie kroczące i przebicia zakresu dają sygnały istotne statystycznie i niespójne z błądzeniem losowym. Jedno ale: test pomijał koszty transakcyjne.
> - Sullivan, Timmermann i White (1999) policzyli rachunek za przeszukiwanie: w uniwersum 7846 reguł, po korekcie metodą Reality Check na 100 latach DJIA, wyniki BLL przetrwały w próbie, ale najlepsza reguła nie działała out-of-sample w dekadzie 1987-1996.
> - Park i Irwin (2007) przejrzeli około 95 badań: 56 pozytywnych, 20 negatywnych, 19 mieszanych, przy czym większość pozytywnych obciążają data snooping, selekcja reguł ex post i pominięcie kosztów. Neely, Weller i Ulrich (2009) pokazali na FX, że przewagi z lat 70. i 80. były realne, ale wygasły do połowy lat 90.
> - Bajgrowicz i Scaillet (2012) domknęli temat na DJIA 1897-2011 metodą False Discovery Rate: przyszłych zwycięskich reguł nie dało się wskazać ex ante (zero persystencji), a już niskie koszty transakcyjne kasują całą in-sample przewagę.

**Teza w jednym zdaniu:** Surowa informacja w cenach istnieje, ale po kosztach transakcyjnych i po uczciwej korekcie na przeszukiwanie tysięcy reguł praktycznie nic nie przeżywa, a przewagi, które kiedyś były realne, wygasły wraz z adaptacją rynku.

## Sto lat tego samego pytania

Spór o analizę techniczną nie zaczął się od YouTube. William Hamilton porządkował teorię Dowa w książce „The Stock Market Barometer" już w 1922 roku: pogląd, że rynek porusza się w trendach, a sama historia notowań mówi coś o przyszłości. Od tamtej pory pytanie brzmi identycznie, zmieniły się tylko narzędzia do jego rozstrzygania. I to jest dobra wiadomość, bo przez ostatnie trzydzieści lat rozstrzygali je ludzie z dostępem do stuletnich szeregów danych, mocnej statystyki i recenzentów, którzy nie przepuszczają chciejstwa.

Ten tekst przechodzi chronologicznie przez sześć prac, które wyznaczyły trajektorię tego sporu w najlepszych czasopismach finansowych. Bez obietnic i bez taniego dyskredytowania, bo uczciwa odpowiedź nie leży w żadnej ze skrajności.

## 1992: praca, która dała technice akademicką wiarygodność

Brock, Lakonishok i LeBaron (Journal of Finance, 1992) wzięli indeks Dow Jones z lat 1897-1986 i przetestowali na nim najprostsze reguły z podręczników: przecięcia średnich kroczących oraz przebicia zakresu, czyli wybicia ponad lokalne maksima i pod lokalne minima. Zamiast porównywać wyniki z zerem, porównali je z symulowanymi szeregami cen, w których z konstrukcji nie ma żadnej struktury do wykorzystania. Wynik był niewygodny dla akademickiej ortodoksji: zwroty po sygnałach kupna różniły się od zwrotów po sygnałach sprzedaży w sposób istotny statystycznie i niespójny z hipotezą błądzenia losowego. Jeśli historia cen nie niesie żadnej informacji, taka regularność nie powinna istnieć.

To ta praca dała analizie technicznej akademicką wiarygodność. Ukazała się w czołowym czasopiśmie finansowym świata i na lata stała się koronnym cytatem zwolenników AT. Miała jednak zastrzeżenie, o którym cytujący chętnie zapominali: test w ogóle nie uwzględniał kosztów transakcyjnych. Sygnał statystyczny to nie to samo co strategia, którą da się grać po spreadzie i prowizjach. Ta luka stanie się osią całej dalszej historii.

## 1999: rachunek za przeszukanie 7846 reguł

Sullivan, Timmermann i White (Journal of Finance, 1999) zadali pytanie, które dziś powinno poprzedzać każdy backtest: ile reguł trzeba było przetestować, żeby znaleźć te, które wyglądają dobrze? Problem nazywa się data snooping i ma prostą intuicję. W turnieju rzutu monetą z tysiącami uczestników ktoś musi trafić długą serię orłów. Seria zwycięzcy nie jest dowodem umiejętności, jest statystyką porządkową: tak po prostu wygląda maksimum z tysięcy losowych prób.

Autorzy zbudowali uniwersum 7846 reguł technicznych i przepuścili je przez metodę Reality Check na 100 latach danych DJIA. Metoda odpowiada na pytanie, czy najlepsza znaleziona reguła jest lepsza od najlepszej reguły, jakiej należałoby oczekiwać w czystym szumie. Dwa wyniki. Pierwszy: rezultaty Brocka, Lakonishoka i LeBarona przetrwały korektę w badanej próbie, więc nie były prostym artefaktem selekcji. Drugi, ważniejszy: reguła najlepsza w próbie nie działała out-of-sample w dekadzie 1987-1996. Pojedyncza „działająca" reguła okazała się dokładnie tym, czego uczy turniej monet: oczekiwanym artefaktem przeszukiwania tysięcy wariantów.

## 2000: formacje niosą informację, nie obietnicę zysku

Lo, Mamaysky i Wang (Journal of Finance, 2000) podeszli do tematu od strony, którą traderzy znają najlepiej: formacji cenowych. Zautomatyzowali ich rozpoznawanie, wygładzając wykresy akcji amerykańskich z lat 1962-1996 regresją jądrową i każąc algorytmowi wykrywać klasyczne kształty, między innymi głowę z ramionami. Dzięki temu z testu zniknął najsłabszy element tradycyjnej AT, czyli subiektywne oko analityka. Potem porównali rozkłady zwrotów po wystąpieniu formacji z rozkładami bezwarunkowymi.

Wynik zaskoczył obie strony sporu: kilka formacji rzeczywiście niesie informację. Rozkłady warunkowe różnią się od bezwarunkowych w sposób istotny statystycznie, czyli po wystąpieniu formacji rynek zachowuje się mierzalnie inaczej niż przeciętnie. To do dziś najmocniejszy akademicki argument za tym, że wykresy nie są czystym szumem. Autorzy dopisali jednak zastrzeżenie, które jest sercem całej debaty: informatywność to nie to samo co zyskowność. Rozkład może różnić się na tyle, żeby zobaczył to test statystyczny, i jednocześnie za mało, żeby zobaczył to rachunek maklerski po kosztach. Praca celowo nie twierdzi, że na formacjach da się zarabiać.

## 2007: dwa przeglądy i jedna rysa

Park i Irwin (Journal of Economic Surveys, 2007) zrobili to, co w dojrzewającej dziedzinie robi się raz na dekadę: przegląd wszystkiego. Zebrali około 95 nowoczesnych badań nad zyskownością analizy technicznej i policzyli werdykty: 56 pozytywnych, 20 negatywnych, 19 mieszanych. Na pierwszy rzut oka wygląda to jak wygrana AT. Czytane w całości, wygląda inaczej: większość pozytywnych wyników obciąża co najmniej jeden z trzech grzechów, czyli data snooping, selekcja reguł ex post albo pominięcie kosztów transakcyjnych. Do tego pozytywne dowody koncentrują się na rynkach walutowych i futures oraz we wczesnych okresach próbek, a nie tam, gdzie szuka ich dzisiejszy trader detaliczny.

<figure>
<svg viewBox="0 0 640 180" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Werdykty około 95 badań: 56 pozytywnych, 20 negatywnych, 19 mieszanych">
<text x="34" y="28" font-size="13" fill="currentColor">56 z około 95 badań raportuje zyski, ale sama liczba zwycięstw myli</text>
<text x="34" y="46" font-size="11" fill="currentColor" opacity="0.6">werdykty przeglądu Parka i Irwina (Journal of Economic Surveys, 2007)</text>
<rect x="34" y="67" width="9" height="9" fill="#0b66c3"/>
<text x="48" y="75" font-size="11" fill="currentColor" opacity="0.75">pozytywne: 56</text>
<rect x="371" y="67" width="9" height="9" fill="currentColor" opacity="0.5"/>
<text x="385" y="75" font-size="11" fill="currentColor" opacity="0.75">negatywne: 20</text>
<rect x="492" y="67" width="9" height="9" fill="currentColor" opacity="0.18"/>
<text x="506" y="75" font-size="11" fill="currentColor" opacity="0.75">mieszane: 19</text>
<clipPath id="at-bar-clip"><rect x="34" y="86" width="572" height="52" rx="5"/></clipPath>
<g clip-path="url(#at-bar-clip)">
<rect x="34" y="86" width="335" height="52" fill="#0b66c3"/>
<rect x="371" y="86" width="119" height="52" fill="currentColor" opacity="0.5"/>
<rect x="492" y="86" width="114" height="52" fill="currentColor" opacity="0.18"/>
</g>
<rect x="34" y="156" width="9" height="9" fill="#0b66c3"/>
<text x="49" y="164" font-size="11" fill="currentColor" opacity="0.75">większość pozytywnych prac: data snooping, selekcja reguł ex post lub brak kosztów transakcyjnych</text>
</svg>
<figcaption>Park i Irwin (2007) zebrali około 95 nowoczesnych badań nad zyskownością analizy technicznej: 56 pozytywnych, 20 negatywnych, 19 mieszanych. Sam licznik zwycięstw myli, bo większość pozytywnych wyników jest obciążona data snoopingiem, selekcją reguł ex post lub pominięciem kosztów transakcyjnych, a pozytywne dowody koncentrują się na rynkach walutowych, futures i wczesnych okresach próbek.</figcaption>
</figure>

Ten sam rok przyniósł drugi przegląd, tym razem od strony praktyki. Menkhoff i Taylor (Journal of Economic Literature, 2007) udokumentowali, że niemal wszyscy profesjonalni uczestnicy rynku walutowego używają analizy technicznej na krótkich horyzontach, przeważnie jako uzupełnienia innych narzędzi. Zestawienie obu przeglądów tworzy paradoks: narzędzie, którego zyskowność literatura podważa, jest jednocześnie standardowym wyposażeniem zawodowców. To napięcie rozładuje dopiero następna praca.

## 2009: przewagi były realne i wygasły

Neely, Weller i Ulrich (Journal of Financial and Quantitative Analysis, 2009) sięgnęli po najczystszy możliwy test na rynku walutowym: wzięli reguły techniczne dokładnie w takiej postaci, w jakiej opisano je w dawnej literaturze, i sprawdzili, co robiły na danych, które napłynęły dopiero po ich publikacji. Taki test nie może być dotknięty data snoopingiem, bo reguł nikt nie dobierał pod nowe dane.

Werdykt ma dwie części i obie są ważne. Po pierwsze: zyski reguł z lat siedemdziesiątych i osiemdziesiątych były realne. Nie były artefaktem przeszukiwania, były prawdziwą nieefektywnością rynku. Po drugie: te same reguły wygasły do połowy lat dziewięćdziesiątych. Dokładnie tak wygląda świat opisywany przez hipotezę rynków adaptacyjnych: przewaga istnieje, przyciąga kapitał, który ją eksploatuje, i przez to znika. Pytanie „czy analiza techniczna działa" zakłada odpowiedź stałą w czasie, a dane pokazują cykl życia przewagi. Obie strony sporu miały rację, tylko każda w innej dekadzie.

## 2012: zero persystencji i koszty, które dobijają resztę

Bajgrowicz i Scaillet (Journal of Financial Economics, 2012) domknęli klamrę na tym samym indeksie, na którym wszystko się zaczęło: DJIA, tym razem na danych 1897-2011. Do kontroli fałszywych odkryć użyli metody False Discovery Rate, która szacuje, jaki odsetek reguł uznanych za działające to pomyłki wynikające z masowego testowania. Wnioski są dwa i oba bolą. Pierwszy: inwestor w żadnym momencie tej długiej historii nie byłby w stanie wskazać ex ante reguł, które okażą się najlepsze w kolejnym okresie. Zwycięzcy się nie powtarzają, persystencja jest zerowa. Drugi: już niskie koszty transakcyjne kasują całą in-sample przewagę. Nawet trafienie w przyszłego zwycięzcę, na które według pierwszego wniosku nie ma co liczyć, po kosztach nie zostawiłoby nic do wypłaty.

## Uczciwa odpowiedź po trzydziestu latach

Odpowiedź nie brzmi ani „działa", ani „nie działa". Brzmi tak: surowa informacja w cenach istnieje, co pokazali Lo, Mamaysky i Wang. Po kosztach transakcyjnych i po uczciwej korekcie na przeszukiwanie reguł praktycznie nic z niej nie zostaje, co pokazali Sullivan, Timmermann i White oraz Bajgrowicz i Scaillet. Przewagi, które istniały naprawdę, wygasły wraz z adaptacją rynku, co pokazali Neely, Weller i Ulrich. Analiza techniczna ma dwóch zabójców i żaden nie jest tajemnicą: koszty transakcyjne i data snooping.

Z tego wynika praktyczna checklista na każdy materiał o „działającej" strategii. Pytanie pierwsze: czy wynik podano po realnych kosztach? Pytanie drugie: ile wariantów przetestowano, zanim pokazano ten jeden? Pytanie trzecie: czy reguła działała także na danych, których autor nie znał, kiedy ją wybierał? Sześć prac z tego tekstu to w praktyce historia tego, jak każdy z tych filtrów po kolei odsiewał to, co bez niego wyglądało na przewagę.

Dla tradera detalicznego jest jeszcze jedna warstwa, zwykle pomijana: detal płaci spready wyższe niż koszty zakładane w badaniach. Jeśli reguła nie przeżywa kosztów przyjętych w recenzowanej pracy, to na rachunku detalicznym nie przeżyje ich tym bardziej. To najkrótsze wyjaśnienie, dlaczego strategia z materiału wideo wygląda świetnie na wykresie historycznym i gorzej na wyciągu z konta.

Uczciwość wymaga dopisania także drugiej strony. Literatura testuje reguły proste, mechaniczne i publicznie znane, bo tylko takie da się testować masowo, więc nie rozstrzyga o każdym możliwym użyciu wykresu. Przegląd Menkhoffa i Taylora pokazuje zresztą, że zawodowcy traktują AT jako uzupełnienie i język opisu rynku na krótkich horyzontach, nie jako samodzielną maszynkę do sygnałów. Między „AT jako kontekst" a „AT jako system, który sam zarabia" biegnie granica, którą literatura rysuje konsekwentnie od trzydziestu lat. Po pierwszej stronie jest narzędzie, którego używają prawie wszyscy. Po drugiej jest obietnica, której w danych po kosztach prawie nie widać.

To nie jest porada inwestycyjna. To przegląd recenzowanej literatury z liczbami z prac źródłowych, po to, żeby ocena dowolnej reguły technicznej zaczynała się od pytań o koszty i o liczbę prób, a nie od koloru świeczek na cudzym zrzucie ekranu.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
