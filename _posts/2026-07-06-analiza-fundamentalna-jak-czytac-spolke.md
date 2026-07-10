---
title: "Analiza fundamentalna. Jak czytać spółkę"
description: "Spółkę opisują trzy sprawozdania: bilans mówi, co firma ma i komu jest winna, rachunek wyników pokazuje zysk za okres według reguł księgowych, a rachunek przepływów pieniężnych liczy gotówkę, która naprawdę weszła i wyszła. Zysk to opinia, gotówka to fakt. Tekst przechodzi przez wskaźniki P/E, P/B i ROE z dekompozycją DuPonta i pułapką dźwigni, przez marże i dług, aż do wartości wewnętrznej liczonej metodą DCF, jej wrażliwości na założenia i marginesu bezpieczeństwa Grahama. Na klasyce gatunku: Graham i Dodd (Security Analysis, 1934; siódme wydanie 2023), Graham (The Intelligent Investor, 1949), darmowe materiały Aswatha Damodarana z NYU Stern oraz podręcznik McKinsey Valuation."
date: 2026-07-06 12:00:00 +0200
eyebrow: "Edukacja · długi termin"
dek: "Cena akcji to jedna liczba. Spółka pod spodem to trzy sprawozdania, kilka wskaźników i strumień gotówki, który albo jest, albo go nie ma. Jak czytać bilans, rachunek wyników i przepływy, czemu zysk bywa opinią, skąd naprawdę bierze się ROE i dlaczego wycena DCF trzęsie się od jednego punktu procentowego. Na końcu margines bezpieczeństwa, czyli co Graham każe robić z niepewnością."
readingTime: 9
tags: [analiza fundamentalna, bilans, "rachunek wyników", "przepływy pieniężne", "zysk a gotówka", "P/E", "P/B", "ROE", "dekompozycja DuPonta", dźwignia, marże, DCF, "wartość wewnętrzna", "stopa dyskontowa", "margines bezpieczeństwa", "Mr. Market", Graham, "Graham i Dodd", Damodaran, "McKinsey Valuation", wycena, akcje, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Spółkę opisują trzy sprawozdania i każde odpowiada na inne pytanie. Bilans: co firma ma i komu jest winna (migawka na jeden dzień). Rachunek wyników: ile zarobiła w okresie, według reguł księgowych, które zostawiają zarządowi sporo swobody. Rachunek przepływów pieniężnych: ile gotówki naprawdę weszło i wyszło. Stąd stara zasada: zysk to opinia, gotówka to fakt.
> - Wskaźniki to skróty myślowe z pułapkami. P/E mówi, ile płacisz za złotówkę rocznego zysku, ale zysk bywa cykliczny i księgowo podrasowany. P/B porównuje cenę z majątkiem księgowym, który słabo łapie marki i technologię. Wysokie ROE potrafi pochodzić z długu, nie z jakości biznesu, i dokładnie to obnaża dekompozycja DuPonta.
> - Wartość wewnętrzna to zdyskontowane przyszłe przepływy gotówki (DCF). Problem w tym, że wynik jest bardzo wrażliwy na założenia: przesunięcie stopy dyskontowej albo tempa wzrostu o jeden punkt procentowy potrafi zmienić wycenę o kilkanaście do kilkudziesięciu procent.
> - Odpowiedzią Grahama na tę niepewność jest margines bezpieczeństwa: kupować tylko wyraźnie poniżej szacowanej wartości, żeby błąd w założeniach nie musiał oznaczać straty. I cierpliwość, bo rynek może latami nie uznawać wartości, którą policzyłeś.

**Teza w jednym zdaniu:** Analiza fundamentalna to odtwarzanie biznesu z trzech sprawozdań po to, żeby oszacować, ile spółka jest naprawdę warta, a ponieważ każdy taki szacunek ma szeroki przedział błędu, kupuje się tylko z marginesem bezpieczeństwa: na tyle poniżej wyliczonej wartości, żeby pomyłka w założeniach nie zamieniała się automatycznie w stratę.

## Trzy sprawozdania: trzy pytania do tej samej spółki

Cena akcji na ekranie to jedna liczba. Spółka pod spodem to zestaw dokumentów publikowanych co kwartał i co rok, z których trzy są rdzeniem: bilans, rachunek wyników i rachunek przepływów pieniężnych. Każdy odpowiada na inne pytanie i żaden nie wystarcza w pojedynkę.

Bilans jest migawką: pokazuje stan na jeden konkretny dzień, co spółka ma i komu jest winna. Rachunek wyników jest filmem: opowiada, ile firma zarobiła przez kwartał albo rok, tyle że film zmontowano według reguł księgowych, a montaż zostawia swobodę. Rachunek przepływów pieniężnych to zapis z kasy: ile gotówki fizycznie wpłynęło i wypłynęło, niezależnie od tego, co twierdzą pozostałe dwa dokumenty.

```
TRZY SPRAWOZDANIA I ICH POWIAZANIA:

  BILANS (stan na dzien)        co spolka MA i komu jest WINNA
  RACHUNEK WYNIKOW (okres)      ile ZAROBILA wedlug regul ksiegowych
  PRZEPLYWY PIENIEZNE (okres)   ile GOTOWKI weszlo i wyszlo

  jak sie spinaja:
    zysk netto z rachunku wynikow → powieksza kapital wlasny w bilansie
    saldo przeplywow pienieznych  → zmienia pozycje "gotowka" w bilansie
    bilans otwarcia + caly okres  → bilans zamkniecia
```

Te trzy dokumenty są ze sobą zszyte. Zysk netto z rachunku wyników zasila kapitał własny w bilansie. Saldo przepływów zmienia stan gotówki w bilansie. Bilans na koniec okresu jest bilansem otwarcia następnego. Kto czyta tylko jedno sprawozdanie, ogląda jedną ścianę budynku i wyciąga wnioski o całej konstrukcji. Graham i Dodd w „Security Analysis" (1934, siódme wydanie 2023) ustawili ten nawyk jako fundament zawodu: analiza zaczyna się od sprawozdań, ale nie polega na ich przepisaniu, tylko na odtworzeniu z liczb rzeczywistego biznesu.

## Bilans: migawka majątku i długów

Bilans ma dwie strony, które zawsze się równają. Po lewej aktywa: wszystko, co spółka kontroluje i co ma przynosić korzyści, od gotówki, przez należności od klientów i zapasy w magazynie, po fabryki, maszyny i wartości niematerialne. Po prawej źródła finansowania: zobowiązania wobec dostawców, banków i obligatariuszy oraz kapitał własny, czyli to, co zostaje właścicielom po spłacie wszystkich długów.

```
BILANS (schemat ilustracyjny, liczby przykladowe):

  AKTYWA (co spolka ma)          PASYWA (skad to sfinansowala)
  gotowka             10         zobowiazania krotkie      25
  naleznosci          15         dlug dlugoterminowy       30
  zapasy              15         ────────────────────────────
  fabryki, maszyny    40         zobowiazania razem        55
  wartosci niemat.    20         kapital wlasny            45
  ─────────────────────          ────────────────────────────
  razem              100         razem                    100

  kapital wlasny = aktywa minus zobowiazania (bufor na straty)
```

Dwie rzeczy warto widzieć od razu. Pierwsza to płynność pozycji: gotówka jest gotówką, ale fabryka wyceniona na 40 nie zamieni się w 40 gotówki na zawołanie, a zapasy niemodnego towaru potrafią być warte ułamek tego, co mówi księga. Druga to charakter wyceny: bilans w dużej mierze zapisuje koszty historyczne i księgowe konwencje, nie cennik z dzisiejszego rynku. Nieruchomość kupiona dwadzieścia lat temu może być warta wielokrotność zapisu, a wartość firmy z przejęcia (goodwill) może wisieć w aktywach do dnia bolesnego odpisu. Kapitał własny pełni tu tę samą rolę, co w każdym bilansie: jest buforem, który jako pierwszy pochłania straty, i mianownikiem, do którego za chwilę wrócimy przy ROE.

## Rachunek wyników: zysk jako opinia

Rachunek wyników schodzi kaskadą: przychody ze sprzedaży, minus koszty wytworzenia, minus koszty sprzedaży i zarządu, minus amortyzacja, minus odsetki, minus podatek, równa się zysk netto. Wygląda jak arytmetyka, ale kluczowe słowo brzmi: memoriał. Księgowość memoriałowa ujmuje przychód wtedy, gdy został zarobiony, a nie wtedy, gdy klient zapłacił, i rozkłada koszty w czasie według przyjętych reguł, a nie według ruchów na koncie.

```
MEMORIAL KONTRA KASA (przyklad ilustracyjny):

  Spolka sprzedaje towar za 1000, faktura platna za 90 dni.

  RACHUNEK WYNIKOW (memorial):   przychod +1000, zysk rosnie DZIS
  PRZEPLYWY PIENIEZNE (kasa):    gotowka +0, wplynie za 90 dni
                                 (albo nigdy, jesli klient padnie)

  zysk mozna zaksiegowac; gotowke trzeba dostac
```

Memoriał nie jest oszustwem, jest sensowną konwencją: pozwala przypisać wynik do okresu, w którym powstał. Ale otwiera przestrzeń uznaniowości. Amortyzacja zależy od tego, ile lat życia przypiszesz maszynie. Rezerwy i odpisy to szacunki zarządu. Moment ujęcia przychodu przy kontraktach wieloletnich to decyzja, nie fakt. Do tego dochodzą zdarzenia jednorazowe: sprzedaż nieruchomości albo odwrócenie odpisu potrafi podbić zysk netto kwartału, mówiąc dokładnie nic o sile biznesu. Wszystko legalne, wszystko opisane w notach, ale suma tych decyzji sprawia, że zysk netto jest wypadkową ocen, a nie odczytem z licznika. Stąd powiedzenie, które organizuje całą resztę tego tekstu: zysk to opinia.

## Przepływy pieniężne: gotówka jako fakt

Rachunek przepływów pieniężnych rozbija ruch gotówki na trzy strumienie. Operacyjny: ile gotówki wygenerował podstawowy biznes. Inwestycyjny: ile poszło na maszyny, fabryki i przejęcia, a ile wróciło ze sprzedaży aktywów. Finansowy: ile dopłynęło z emisji akcji i nowego długu, a ile wypłynęło na spłaty, dywidendy i skup akcji. U dojrzałej, zdrowej spółki typowy obraz to dodatni strumień operacyjny, ujemny inwestycyjny (firma inwestuje) i finansowy zależny od etapu życia: młode spółki zasysają kapitał, dojrzałe go oddają.

To sprawozdanie jest najtrudniejsze do podrasowania, bo gotówka na rachunku albo jest, albo jej nie ma. Najtrudniejsze nie znaczy niemożliwe: można na kwartał wstrzymać płatności dostawcom, sprzedać należności, przesunąć inwestycje. Dlatego czyta się je w dłuższym oknie i zawsze razem z rachunkiem wyników. Klasyczny sygnał ostrzegawczy wygląda tak: zysk netto rośnie kwartał po kwartale, a gotówka operacyjna za nim nie nadąża, bo puchną należności i zapasy. Papierowy zysk już jest, pieniędzy jeszcze nie ma, i czasem nigdy nie będzie. Podręcznik McKinsey „Valuation" stawia sprawę wprost: o wartości firmy decyduje jej zdolność do generowania gotówki w długim okresie, a księgowe miary zysku mają znaczenie o tyle, o ile o tej zdolności informują. Miarą roboczą jest tu wolna gotówka (free cash flow): w uproszczeniu strumień operacyjny minus nakłady inwestycyjne potrzebne do utrzymania i rozwoju biznesu. To właśnie ona zasili za chwilę wycenę DCF.

## Wskaźniki wyceny: ile płacisz za złotówkę

Wskaźniki nie są wiedzą, są skrótami: pozwalają szybko porównać cenę z fundamentem, zanim zacznie się właściwa robota. Dwa najstarsze dotyczą wyceny.

P/E, cena do zysku, odpowiada na pytanie: ile płacisz za złotówkę rocznego zysku netto. Przykład ilustracyjny: spółka zarabia 5 zł na akcję, akcja kosztuje 75 zł, więc P/E wynosi 15, a odwrotność, około 6,7 procent, to rentowność zysku, którą można porównywać z oprocentowaniem obligacji. Intuicja jest prosta, pułapki dwie. Po pierwsze zysk bywa cykliczny: producent surowców na szczycie koniunktury pokazuje rekordowe zyski i śmiesznie niskie P/E dokładnie wtedy, gdy tych zysków nie da się utrzymać; tani wskaźnik na szczycie cyklu to często najdroższy zakup. Po drugie zysk bywa księgowy: jednorazowe pozycje i uznaniowe odpisy z poprzedniej sekcji siedzą w mianowniku, a przy stratach wskaźnik w ogóle traci sens.

P/B, cena do wartości księgowej, porównuje wycenę rynkową z kapitałem własnym z bilansu. To było podstawowe narzędzie Grahama w epoce, w której wartość spółki siedziała w fabrykach i zapasach. Dziś działa słabiej, bo księgowość w większości nie kapitalizuje tego, co tworzy wartość współczesnych firm: marki, oprogramowania, badań, relacji z klientami. Niskie P/B może oznaczać okazję, ale równie dobrze biznes, który trwale zarabia mniej, niż kosztuje jego kapitał. W obu przypadkach wskaźnik jest początkiem pytania, nie odpowiedzią. Do porównań sektorowych warto sięgać po systematyczne dane zamiast pojedynczych przykładów: Aswath Damodaran (NYU Stern) publikuje na stronie uczelni (pages.stern.nyu.edu/~adamodar) darmowe, aktualizowane co roku zestawienia mnożników, marż i kosztu kapitału po branżach, obok kompletnych materiałów kursowych z wyceny.

## Wskaźniki jakości: skąd naprawdę bierze się ROE

ROE, zwrot z kapitału własnego, to zysk netto podzielony przez kapitał własny: ile biznes wyciska ze złotówki należącej do właścicieli. Wysokie, stabilne ROE uchodzi za znak dobrego biznesu i często nim jest. Ale ROE ma wbudowaną pułapkę: można je podnieść nie poprawiając biznesu ani o milimetr, wystarczy dołożyć długu. Mniej kapitału własnego w mianowniku, ten sam zysk w liczniku, wskaźnik rośnie. Dekompozycja DuPonta rozkłada ROE na trzy silniki i pokazuje, który faktycznie pracuje.

```
DEKOMPOZYCJA DUPONTA (ROE rozlozone na trzy silniki):

  ROE = zysk netto / kapital wlasny

      = (zysk netto / przychody)     marza netto
      x (przychody / aktywa)         rotacja aktywow
      x (aktywa / kapital wlasny)    dzwignia finansowa

  Przyklad ilustracyjny: dwie spolki, obie ROE 15%
    A: marza 10% x rotacja 0.75 x dzwignia 2.0  = 15%
    B: marza  3% x rotacja 1.00 x dzwignia 5.0  = 15%

  to samo ROE, inna jakosc: A zarabia biznesem,
  B stoi na dlugu i jest krucha przy kazdym zakrecie
```

Ta sama liczba na górze, zupełnie inne ryzyko pod spodem. Spółka A ma zwrot z marży i efektywności, spółka B z dźwigni, a dźwignia działa w obie strony: odsetki są stałe, przychody nie, więc niewielki spadek sprzedaży u mocno zadłużonej firmy zjada zysk i kapitał w tempie, którego niezadłużony konkurent w ogóle nie zna. Dlatego obok ROE patrzy się na dług do kapitału własnego: nie po to, żeby dług potępiać, tylko żeby wiedzieć, ile kruchości kupujesz razem ze zwrotem. Ostatni element tej układanki to marże czytane osobno: marża brutto mówi o sile cenowej produktu, operacyjna o dyscyplinie kosztów, netto o tym, co zostaje właścicielom. Trwale wysoka marża to zwykle ślad jakiejś przewagi konkurencyjnej i jednocześnie magnes na konkurencję, więc właściwe pytanie brzmi: co tę marżę chroni i jak długo jeszcze.

## Wartość wewnętrzna: DCF w pigułce

Wszystko powyżej opisuje spółkę. Wycena zadaje następne pytanie: ile to jest warte. Rama, na której stoi i podręcznik McKinsey, i materiały Damodarana, jest jedna: aktywo jest warte tyle, ile gotówki odda właścicielowi w przyszłości, po przeliczeniu tej przyszłej gotówki na dzisiejsze pieniądze. Przeliczanie nazywa się dyskontowaniem i jest [procentem składanym](/dlogic-quant/2026/07/07/procent-skladany-osmy-cud-swiata/) puszczonym wstecz: złotówka za dziesięć lat jest warta mniej niż złotówka dziś, bo dzisiejszą można ulokować i czekać. Model zbudowany na tej idei to DCF, discounted cash flow.

```
DCF W PIGULCE (idea; liczby ilustracyjne):

  wartosc = suma [ CF_t / (1+r)^t ]   dla t = 1, 2, 3, ...

  CF_t = wolna gotowka w roku t
  r    = stopa dyskontowa (wymagany zwrot)

  Najprostsza wersja (staly wzrost g, wzor Gordona):
    wartosc = CF / (r - g)

  Wrazliwosc przy CF = 100 rocznie:
    r = 8%, g = 2%   →  100 / 0.06 = 1667
    r = 9%, g = 2%   →  100 / 0.07 = 1429    (-14%)
    r = 8%, g = 3%   →  100 / 0.05 = 2000    (+20%)

  jeden punkt procentowy w zalozeniach przesuwa wycene
  o kilkanascie do kilkudziesieciu procent
```

Na tym schemacie widać jednocześnie siłę i słabość metody. Siła: DCF zmusza do jawnych założeń. Zamiast „ta spółka mi się podoba" trzeba powiedzieć, ile gotówki, w jakim tempie wzrostu i przy jakim wymaganym zwrocie, a potem można się o każde z tych założeń uczciwie spierać. McKinsey dokłada do tego rdzeń całego podręcznika: wartość tworzą tylko dwie rzeczy, wzrost i zwrot z zainwestowanego kapitału powyżej kosztu tego kapitału, a wzrost bez odpowiedniego zwrotu wartości nie dodaje, potrafi ją niszczyć. Słabość: wynik trzęsie się od założeń. Jak pokazuje blok wyżej, przesunięcie stopy dyskontowej albo tempa wzrostu o jeden punkt procentowy zmienia wycenę o kilkanaście do kilkudziesięciu procent, a przecież nikt nie zna przyszłych przepływów ani właściwej stopy z taką precyzją. Damodaran powtarza to w swoich materiałach na wiele sposobów: wycena nie jest wyrocznią, jest uporządkowaną opowieścią o biznesie przetłumaczoną na liczby, i lepiej być z grubsza w porządku niż precyzyjnie w błędzie.

## Margines bezpieczeństwa: odpowiedź Grahama na niepewność

Skoro najlepszy dostępny szacunek wartości ma przedział błędu liczony w dziesiątkach procent, co z nim właściwie zrobić? Odpowiedź Grahama z „The Intelligent Investor" (1949) jest jedną z najsłynniejszych w historii inwestowania: poproszony o streszczenie sekretu zdrowego inwestowania w trzech słowach, odpowiada: margines bezpieczeństwa. Zasada jest prosta. Nie kupuje się za cenę równą oszacowanej wartości, tylko wyraźnie poniżej niej. Różnica jest poduszką: jeśli założenia były zbyt optymistyczne, jeśli biznes potknie się o coś nieprzewidzianego, jeśli po prostu policzyłeś źle, strata nie jest automatyczna, bo zapłaciłeś na tyle mało, że spory błąd wciąż mieści się w cenie.

Margines bezpieczeństwa nie jest hurraoptymizmem ubranym w regułę, jest dokładnie odwrotnie: instytucjonalizacją pokory. Zakłada z góry, że wycena jest niepewna, prognozy zawodne, a przyszłość złośliwa, i zamienia to założenie na wymóg cenowy. Im bardziej krucha i nieprzewidywalna spółka, tym większego marginesu żąda rozsądek; im stabilniejszy biznes, tym mniejszy wystarcza. Do pary Graham daje drugą figurę, Mr. Market: rynek jako chimeryczny wspólnik, który codziennie podaje ci cenę, raz w euforii, raz w depresji. Z jego ofert wolno korzystać, kiedy są absurdalne, ale nie trzeba go słuchać, kiedy się z tobą nie zgadza. Margines bezpieczeństwa mówi, ile płacić; Mr. Market przypomina, że cena i wartość to dwie różne wielkości, które schodzą się bez rozkładu jazdy.

## Czego analiza fundamentalna nie obiecuje

Uczciwy wykład musi domknąć trzy ograniczenia. Pierwsze: księgowość to nie ekonomia. Sprawozdania mierzą to, co mierzalne według przyjętych reguł, a nie wartość ekonomiczną: marka, kapitał ludzki, efekty sieciowe i opcje rozwoju są w bilansie niewidzialne albo widzialne dopiero po fakcie, więc dwie spółki o identycznych księgach mogą być zupełnie różnymi biznesami. Drugie: prognozy są kruche. DCF na dziesięć lat to dziesięć lat założeń o przychodach, marżach i inwestycjach, a wrażliwość pokazana wyżej działa bezlitośnie na każde z nich; dlatego wynik wyceny traktuje się jako przedział, nie punkt, i dlatego margines bezpieczeństwa nie jest ozdobą metody, tylko jej warunkiem koniecznym. Trzecie: rynek może latami nie uznawać wartości. Graham i Dodd opisali rynek jako maszynę do głosowania, nie wagę: w krótkim okresie ceny zapisują nastroje i przepływy, nie wyceny. Niedowartościowanie potrafi trwać dłużej niż cierpliwość i kapitał tego, kto je znalazł, a spór o to, czy w cenach w ogóle zostaje coś systematycznie do zebrania, ma na tym blogu [osobny tekst o hipotezie rynku efektywnego](/dlogic-quant/2026/07/07/hipoteza-rynku-efektywnego-najwiekszy-spor/).

Co zostaje po tych zastrzeżeniach? Rama, która porządkuje myślenie. Trzy sprawozdania mówią, czym spółka jest; wskaźniki pozwalają szybko porównać cenę i jakość, o ile pamięta się o ich pułapkach; DCF zmusza do jawnych założeń o przyszłości; margines bezpieczeństwa zamienia niepewność wyceny na dyscyplinę cenową. Analiza fundamentalna nie jest maszynką do sygnałów i nie obiecuje, że rynek szybko przyzna ci rację. Obiecuje coś skromniejszego i cenniejszego: że wiesz, co kupujesz, ile to może być warte i ile błędu jesteś w stanie przeżyć.

To nie jest porada inwestycyjna. To wykład podstaw analizy fundamentalnej według klasyki gatunku: Graham i Dodd („Security Analysis", 1934; siódme wydanie 2023), Benjamin Graham („The Intelligent Investor", 1949), darmowe materiały i dane o wycenie Aswatha Damodarana (NYU Stern, pages.stern.nyu.edu/~adamodar) oraz podręcznik McKinsey „Valuation". Wszystkie liczby w przykładach są ilustracyjne i służą wyłącznie pokazaniu mechaniki.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
