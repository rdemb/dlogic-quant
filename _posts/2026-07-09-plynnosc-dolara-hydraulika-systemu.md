---
title: "Płynność dolara. Hydraulika, której nie widać, a która rządzi tłem"
description: "Płynność dolara na poziomie systemu to rezerwy banków w Fed. Sterują nią trzy pozycje z cotygodniowego raportu H.4.1: bilans Fedu (WALCL), konto rządu (TGA) i reverse repo (RRP), a przybliżenie płynności netto to bilans minus TGA minus RRP. Mechanika QE i QT, rynek eurodolara jako dolar poza bilansem oraz powód, dla którego to tło reżimu ryzyka, a nie sygnał wejścia. Źródła: Pozsar, CGFS, Bank of England, Mehrling."
date: 2026-07-09 17:00:00 +0200
eyebrow: "Edukacja · makro"
dek: "Rezerwy banków w Fed, konto rządu i reverse repo to trzy krany, które sterują ilością dolara w systemie. Rozłożona na części hydraulika bilansu Fedu: co robi QE, co robi QT, dlaczego płynność netto to z grubsza bilans minus TGA minus RRP, skąd wziąć publiczne dane i po co to inwestorowi jako tło, a nie sygnał."
readingTime: 8
tags: ["płynność dolara", "bilans Fedu", QE, QT, TGA, RRP, "reverse repo", eurodolar, "H.4.1", Pozsar, Mehrling, "money market plumbing", makro, Fed]
category: edukacja
---

> **W skrócie**
>
> - Płynność dolara na poziomie systemu to nie gotówka w portfelach ani nawet depozyt w banku. To rezerwy: zobowiązanie Fedu, którym banki rozliczają się między sobą. Publiczność nigdy ich nie dotyka, a banki nie „pożyczają rezerw" klientom (Bank of England, 2014).
> - Ilością rezerw rządzą trzy pozycje z bilansu Fedu: sam bilans (WALCL), konto rządu USA w Fed (TGA) i reverse repo (RRP). Przybliżenie płynności netto to bilans minus TGA minus RRP. TGA i RRP to krany, które potrafią wyssać rezerwy nawet wtedy, gdy bilans stoi w miejscu.
> - QE dodaje rezerwy (Fed kupuje obligacje i zapisuje bankom rezerwy), QT je odejmuje (obligacje zapadają bez rolowania). Ale wzrost TGA albo RRP drenuje rezerwy równie skutecznie co QT, tylko szybciej i mniej widocznie.
> - To jest tło reżimu ryzyka, nie sygnał wejścia. Zależność jest luźna, opóźniona i zależna od reżimu; działa jak pogoda, nie jak spust. Dane są publiczne i darmowe: raport H.4.1 Fedu, w każdy czwartek.

**Teza w jednym zdaniu:** Ilością dolara w systemie nie rządzi mityczna drukarka, tylko trzy pozycje w bilansie Fedu (sam bilans, konto rządu i reverse repo), a ich wypadkowa to wolno płynący przypływ, który jest tłem dla apetytu na ryzyko, a nie sygnałem wejścia.

## Płynność, o której mowa, to rezerwy w Fed

Kiedy pada zdanie „płynność dolara rośnie" albo „drukują", pod spodem najczęściej kryje się jedna, konkretna wielkość: rezerwy banków trzymane w Rezerwie Federalnej. Rezerwy to nie banknoty i nie salda, które widzisz na wyciągu. To zobowiązanie banku centralnego wobec banków komercyjnych, rodzaj depozytu, który banki trzymają w Fed i którym rozliczają się między sobą oraz z państwem. Dostęp do tego pieniądza mają wyłącznie instytucje depozytowe. Zwykły uczestnik rynku nigdy nie dotyka rezerw, tak samo jak nigdy nie dotyka wnętrza izby rozliczeniowej.

To rozróżnienie nie jest pedantyczne, bo od niego zależy cała reszta rozumowania. Bank of England w pracy „Money creation in the modern economy" (McLeay, Radia, Thomas, 2014) pokazał czarno na białym, że pieniądz, którym płaci gospodarka, powstaje głównie wtedy, gdy bank komercyjny udziela kredytu i dopisuje depozyt. Banki nie „wypożyczają" rezerw klientom i nie mnożą ich przez prosty mnożnik. Rezerwy służą do rozliczeń w warstwie międzybankowej, a depozyty publiczności żyją warstwę wyżej. Płynność systemowa (rezerwy) i szeroki pieniądz (depozyty w rękach ludzi i firm) to dwa różne piętra. Fed steruje bezpośrednio tylko dolnym.

## Bilans Fedu: aktywa równają się zobowiązaniom

Bilans banku centralnego, jak każdy bilans, musi się domykać. Po stronie aktywów Fed trzyma głównie obligacje skarbowe i papiery hipoteczne (MBS) kupione na rynku, a doraźnie także pożyczki i operacje repo. Po stronie zobowiązań są cztery duże pozycje: gotówka w obiegu, rezerwy banków, konto rządu (TGA), reverse repo (RRP), plus kapitał i drobiazgi. Suma aktywów zawsze równa się sumie zobowiązań i kapitału. To banalna tożsamość księgowa, ale to z niej wynika cała mechanika płynności.

QE, czyli luzowanie ilościowe, działa tak: Fed kupuje obligację od banku, a zapłatę księguje jako nowe rezerwy na koncie tego banku w Fed. Aktywa rosną o wartość obligacji, zobowiązania rosną o tyle samo rezerw. System dostaje zastrzyk płynności bazowej. QT, czyli zacieśnianie ilościowe, jest odwrotnością: zapadające obligacje nie są rolowane, Skarb Państwa spłaca je do Fedu, pieniądz wychodzi z systemu, aktywa Fedu się kurczą, a rezerwy maleją. Warto zapamiętać jedną rzecz, którą upraszczają hasła o drukarce. QE to zamiana obligacji na rezerwy, a nie rozdawanie pieniędzy z helikoptera. Zmienia strukturę aktywów sektora prywatnego, a to, czy przełoży się na szeroki pieniądz i akcję kredytową, jest osobnym pytaniem, na które odpowiedź daje warstwa banków komercyjnych, nie sam Fed. Sumę aktywów Fedu śledzi się w danych publicznych pod nazwą WALCL.

## Trzy pozycje, które przesuwają rezerwy

Skoro aktywa równają się zobowiązaniom, to rezerwy można zapisać jako resztę po odjęciu pozostałych zobowiązań. Gotówka w obiegu i kapitał pełzają wolno, więc z tygodnia na tydzień prawie się nie zmieniają. Dwie pozycje, które potrafią skoczyć szybko i o dużo, to konto rządu (TGA) oraz reverse repo (RRP). Dlatego zmiany rezerw są w praktyce napędzane przez trójkę: bilans, TGA i RRP.

```
Bilans Fedu (aktywa) = gotówka w obiegu + rezerwy + TGA + RRP + kapitał i reszta

rezerwy = aktywa − gotówka w obiegu − TGA − RRP − kapitał i reszta

przybliżenie płynności netto:
płynność netto ≈ WALCL − TGA − RRP

WALCL = suma aktywów Fedu (raport H.4.1, poziom środowy)
TGA   = konto rządu USA w Fed (Treasury General Account)
RRP   = overnight reverse repo, gotówka zaparkowana w Fed
```

Uczciwie: to przybliżenie, nie tożsamość. Formuła pomija gotówkę w obiegu i kapitał, więc nie daje dokładnego poziomu rezerw. Ale jej zmiany dobrze śledzą zmiany rezerw, bo pominięte pozycje poruszają się ślamazarnie. Kierunek czyta się prosto. WALCL w górę to płynność w górę (QE), WALCL w dół to płynność w dół (QT). TGA w górę drenuje rezerwy, TGA w dół je dolewa. RRP w górę drenuje, RRP w dół dolewa. Wypadkowa tych trzech to przypływ, na którym unosi się cała reszta.

## TGA i RRP: dwa krany, które potrafią wysuszyć rynek

TGA to rachunek bieżący amerykańskiego Skarbu Państwa prowadzony w Fed. Kiedy rząd inkasuje podatki albo sprzedaje obligacje, pieniądz płynie z banków (rezerwy) na to konto, więc rezerwy spadają. Kiedy rząd wydaje, pieniądz wraca do systemu, więc rezerwy rosną. Najciekawiej robi się przy limicie długu. Gdy Skarb nie może emitować nowego długu, finansuje wydatki, spuszczając TGA, co po cichu dolewa rezerw do systemu. Po podniesieniu limitu Skarb odbudowuje konto zalewem emisji bonów, co po cichu wysysa rezerwy z powrotem. Ten sam mechanizm działa wokół kwartalnych dat podatkowych. Dlatego obserwatorzy płynności pilnują TGA równie uważnie jak samego bilansu: potrafi ono zafundować zacieśnienie albo rozluźnienie bez jednego ruchu stopy procentowej.

RRP, a dokładnie overnight reverse repo, to okienko, w którym fundusze rynku pieniężnego parkują nadmiar gotówki na noc w Fed, dostając w zamian oprocentowanie i zabezpieczenie. Pieniądz siedzący w RRP jest sterylizowany, to znaczy nie jest rezerwą krążącą w systemie bankowym. RRP w górę drenuje, RRP w dół dolewa. Między 2021 a 2023 rokiem widać było ten mechanizm jak na dłoni: nadmiar gotówki, mało bonów skarbowych i atrakcyjna stawka RRP wypchnęły to okienko do rekordowych rozmiarów. Kiedy potem Skarb ruszył z podażą bonów, fundusze zaczęły przekładać pieniądz z RRP do bonów, RRP zaczęło opadać, a ten odpływ amortyzował ubytek rezerw wynikający z QT i odbudowy TGA. Mechanika, nie prognoza.

Warto pamiętać, że liczy się nie tylko kierunek, ale i poziom rezerw względem potrzeb systemu. We wrześniu 2019 roku, po serii QT, rezerwy zrobiły się rzadsze niż wynosił popyt na nie. Zbiegła się z tym data podatkowa i duże rozliczenie emisji skarbowej, a stawki repo overnight wystrzeliły śródsesyjnie w okolice kilkunastu procent, zanim Fed zdążył dolać płynności operacjami repo. Lekcja jest twarda: „obfite rezerwy" mają dno. Kiedy zejdzie się poniżej niego, hydraulika zgrzyta i ceny pieniądza skaczą, nawet gdy stopa docelowa się nie rusza.

## Skąd brać dane: raport H.4.1 w czwartki

Cała ta trójka jest jawna i darmowa. Podstawowe źródło to cotygodniowy raport Fedu H.4.1, „Factors Affecting Reserve Balances", publikowany zwykle w czwartki około 16:30 czasu Nowego Jorku, z danymi na zamknięcie poprzedniej środy. To surowy, pierwotny dokument banku centralnego, w którym rozpisane są rezerwy, konto Skarbu, reverse repo, gotówka w obiegu i pozycje aktywów. Baza FRED prowadzona przez oddział Fedu w St. Louis udostępnia te same szeregi w wygodnej formie: WALCL dla sumy aktywów oraz odpowiedniki dla TGA i RRP. Dane dzienne dla TGA znajdziesz w Daily Treasury Statement, a dzienne RRP w komunikatach operacyjnych oddziału Fedu w Nowym Jorku. Żaden płatny dostawca nie jest potrzebny. To dokładnie ten typ źródła, który wypada traktować poważnie: dokumentacja instytucji, nie wpis z forum.

## Eurodolar: dolar poza bilansem Fedu

Bilans Fedu to tylko warstwa bazowa. Większość systemu dolarowego żyje poza jego księgami i dzieje się to dwoma kanałami. Pierwszy opisała już przywołana praca Bank of England: banki komercyjne tworzą dolarowe depozyty, udzielając kredytu, a Fed ustawia cenę i reguły, nie zaś bezpośrednio ilość szerokiego pieniądza. Drugi to eurodolar, czyli dolarowe depozyty i zobowiązania tworzone przez banki poza Stanami Zjednoczonymi oraz przez zagraniczne oddziały banków. Te „dolary z zagranicy" powstają poza bilansem Fedu i nie podlegają jego bezpośredniej kontroli, a rynek jest ogromny. To jest cień dolara, w którym rozgrywa się duża część realnej hydrauliki.

Najpełniej opisał ten świat Zoltan Pozsar, który system dolarowy czyta jak instalację wodno-kanalizacyjną: repo, zabezpieczenia (collateral) i dealerzy pośredniczący w przepływach, a nad tym warstwa bankowości cienia i rynku eurodolarowego. Kiedy ta hydraulika się zatyka, w rolę „dealera ostatniej instancji" wchodzi bank centralny. Skalę międzynarodowego finansowania w dolarze udokumentował raport CGFS, komitetu przy Banku Rozrachunków Międzynarodowych, „US dollar funding: an international perspective" (CGFS Papers nr 65, 2020): banki spoza USA prowadzą wielkie księgi dolarowe finansowane na rynkach hurtowych i przez swapy walutowe, co tworzy transgraniczną kruchość finansowania. Ramę pojęciową dla tego wszystkiego dał wcześniej Perry Mehrling w „The New Lombard Street" (2011) i w swoim „money view": pieniądz jest hierarchiczny, a to, co w dobrych czasach uchodzi za pieniądz (zobowiązania cienia, eurodolary), w kryzysie potrafi przestać być „money-good". Wtedy bije tak zwane ograniczenie przetrwania, czyli twardy obowiązek rozliczenia własnych płatności. Dlatego hydraulika ma znaczenie, choć w spokojnych czasach jest niewidoczna.

## Po co to inwestorowi: tło reżimu, nie sygnał

Płynność netto to wolny przypływ. Historycznie, gdy rosła (QE, spuszczanie TGA, odpływ z RRP), stanowiła wspierające tło dla aktywów ryzykownych, a gdy opadała (QT, odbudowa TGA, wyczerpane już RRP), działała jak wiatr w twarz. Trzeba jednak od razu dopowiedzieć to, co najważniejsze: to korelacja, nie mechanizm sterujący ceną z tygodnia na tydzień, a związek jest luźny, opóźniony i zależny od reżimu. To kontekst dla apetytu na ryzyko, a nie spust wejścia. Nikt rozsądny nie klika dlatego, że „płynność netto wzrosła w tym tygodniu".

Dla rynku walutowego wątek jest jeszcze bliższy. Warunki finansowania w dolarze przekładają się na premię za dolarowe finansowanie i na tak zwaną bazę cross-currency. Gdy dolara zaczyna brakować, na przykład w marcu 2020 roku podczas globalnej ucieczki do gotówki, dolar zwykle się umacnia, a baza cross-currency gwałtownie się rozjeżdża. Właśnie po to istnieją linie swapowe Fedu z innymi bankami centralnymi: żeby rozładować niedobór dolara poza granicami USA. Hydraulika jest więc tłem dla zachowania par dolarowych w stresie, zwłaszcza wtedy, gdy zwykłe modele przestają działać.

Praktyczny wniosek jest skromny i właśnie dlatego użyteczny. To mapa pogody, a nie zegar. Mówi, w jakim reżimie się stoi i dlaczego jakiś ruch może mieć paliwo albo je tracić, a nie kiedy nacisnąć przycisk. Do tego się nadaje: do ważenia przekonania i rozumienia tła, nie do wyznaczania momentu wejścia.

To nie jest porada inwestycyjna. To opis mechaniki systemu monetarnego, pokazany po to, żeby rozumieć tło reżimu ryzyka, a nie po to, żeby na nim ustawiać wejścia.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
