---
title: "Order flow. Co naprawdę rusza kursem, gdy nie ma newsa"
description: "Tradycyjny model makro tłumaczy kurs fundamentami, ale stopy i inflacja wyjaśniają zaskakująco mało krótkoterminowych ruchów, co nazwano zagadką rozłączenia. Znakowany, skumulowany przepływ zleceń tłumaczy znacznie więcej, bo agreguje rozproszoną informację i potrzeby portfelowe uczestników w cenę, której dealer musi bronić kwotowaniem. Mechanizm modelu portfolio shifts Evansa i Lyonsa, różnica między order flow a wolumenem i praktyczna intuicja, dlaczego cena rusza się bez newsa."
date: 2026-07-09 22:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
dek: "Stopy i inflacja tłumaczą zaskakująco mało tego, co kurs robi w ciągu dnia. Robotę wykonuje niezrównoważony przepływ zleceń: kupujący inicjujący minus sprzedający inicjujący. Skąd w przepływie bierze się informacja, dlaczego to nie to samo co wolumen i dlaczego cena rusza się, gdy w kalendarzu pusto. Model portfolio shifts Evansa i Lyonsa po ludzku."
readingTime: 8
tags: ["order flow", "przepływ zleceń", mikrostruktura, "Evans & Lyons", "portfolio shifts", "prywatna informacja", "disconnect puzzle", "Meese-Rogoff", "kurs walutowy", dealer, wolumen, BIS, Lyons, edukacja, Forex]
category: edukacja
---

> **W skrócie**
>
> - Tradycyjny model makro wywodzi kurs z fundamentów: różnic stóp, inflacji, podaży pieniądza. Kłopot w tym, że te zmienne wyjaśniają zaskakująco mało dziennych ruchów, a modele strukturalne nie biją zwykłego błądzenia losowego w prognozie na horyzoncie do roku (Meese i Rogoff, 1983). Obstfeld i Rogoff nazwali ten rozjazd zagadką rozłączenia kursu od fundamentów.
> - Znacznie więcej dziennej zmienności tłumaczy order flow, czyli skumulowany, znakowany przepływ zleceń: liczba transakcji zainicjowanych przez kupującego minus zainicjowanych przez sprzedającego. Evans i Lyons pokazali ten związek modelem portfolio shifts (2002).
> - Order flow to nie wolumen. Wolumen jest bezznakowy, bo każda transakcja ma kupującego i sprzedającego, więc łączny obrót jest z definicji symetryczny. Przepływ pyta, kto był stroną agresywną, kto zażądał płynności i przycisnął cenę.
> - Mechanizm: przepływ agreguje rozproszoną, prywatną informację i potrzeby portfelowe uczestników, których nikt nie ogłasza. Dealer widzi imbalance, uczy się z niego i przesuwa kwotowanie. Dlatego cena potrafi ruszyć bez żadnego newsa. Po polsku o mikrostrukturze FX pisze prawie nikt.

**Teza w jednym zdaniu:** Kursem walutowym w krótkim terminie rusza nie sam strumień wiadomości, tylko niezrównoważony przepływ zleceń, bo to on scala rozproszoną informację i potrzeby uczestników w cenę, której dealer musi bronić kwotowaniem.

## Zagadka rozłączenia: fundamenty tłumaczą zaskakująco mało

Podręcznikowy obraz kursu jest prosty. Kurs to cena jednego pieniądza wyrażona w drugim, więc powinny go napędzać fundamenty: różnica stóp procentowych, inflacja, podaż pieniądza, bilans obrotów bieżących. Napływa news o którejś z tych wielkości, rynek go dyskontuje i kurs się przesuwa. Tyle teoria.

Dane od dekad opowiadają coś innego. Meese i Rogoff w 1983 roku sprawdzili modele makro kursu na danych z lat siedemdziesiątych i pokazali, że poza próbą nie biją naiwnego błądzenia losowego, czyli prognozy mówiącej po prostu, że jutro będzie mniej więcej tyle co dziś. Na horyzoncie od miesiąca do roku fundamenty nie pomagały. Obstfeld i Rogoff w przeglądzie zagadek makroekonomii międzynarodowej nazwali ten rozjazd zagadką rozłączenia: w krótkim i średnim terminie kurs wygląda, jakby był odłączony od fundamentów, które rzekomo go napędzają. Coś inne wykonuje tę robotę, a fundamenty domykają obraz dopiero na dłuższych horyzontach.

To jest punkt wyjścia całej mikrostruktury walutowej. Skoro publiczne wiadomości nie tłumaczą dziennych ruchów, to trzeba zejść piętro niżej, do samego mechanizmu handlu, i zapytać, kto z kim zawiera transakcje i w którą stronę.

## Order flow to nie wolumen

Order flow, czyli przepływ zleceń, to skumulowana suma transakcji z przypisanym znakiem. Każdej transakcji nadajesz kierunek: plus, gdy inicjuje ją kupujący, to znaczy sięga po ofertę i płaci ask, oraz minus, gdy inicjuje ją sprzedający, czyli uderza w bid. Order flow w danym okresie to różnica: transakcje zainicjowane przez kupujących minus zainicjowane przez sprzedających. To jest netto presji, a nie suma obrotu.

I tu pada kluczowe rozróżnienie, które myli większość ludzi. Order flow to nie wolumen. Wolumen jest bezznakowy, bo każda transakcja ma jednocześnie kupującego i sprzedającego, więc łączny obrót jest z definicji symetryczny i nie ma kierunku. Dwa dni mogą mieć identyczny wolumen i przeciwny order flow. Wolumen mówi, ile się wydarzyło. Order flow mówi, w którą stronę szła presja, bo pyta, kto był stroną agresywną i kto zażądał płynności. Ta jedna informacja, znak i inicjator, jest tym, czego goły wolumen nigdy nie poda.

Dlatego popularne na platformach detalicznych pojęcie wolumenu tickowego nie jest order flow. To liczba zmian ceny w jednostce czasu z feedu jednego brokera, bez znaku i bez inicjatora. Bywa zgrubnym przybliżeniem aktywności, ale nie mówi, kto naciskał.

## Model portfolio shifts: skąd w przepływie bierze się informacja

Przełomem była praca Evansa i Lyonsa Order Flow and Exchange Rate Dynamics z 2002 roku. Zbudowali model nazwany portfolio shifts i skonfrontowali go z rzeczywistymi danymi z rynku międzydealerskiego. Sam mechanizm da się opisać bez jednej liczby.

Dzień handlu dzieli się na rundy. Dealerzy kwotują dwustronne ceny. Najpierw napływa publiczny news makro, który wszyscy widzą w tej samej chwili. Potem klienci, czyli fundusze i korporacje, składają u dealerów zlecenia wynikające z chęci przestawienia portfeli, na przykład trzymać więcej aktywów w euro, a mniej w dolarze. I tu jest sedno: te zlecenia są rozproszone. Każdy dealer widzi tylko swój wycinek napływu, nikt nie widzi agregatu. Następnie dealerzy handlują między sobą. Przepływ zleceń w tej rundzie międzydealerskiej jest sygnałem, bo scala rozproszony popyt klientów w jeden obserwowalny imbalance. Dealerzy odczytują tę nierównowagę i przesuwają kwotowania tak długo, aż rynek zechce dobrowolnie utrzymać nową pozycję netto. Cena ląduje przesunięta nie przez sam news, tylko przez przepływ, który ujawnił zagregowane przesunięcie portfeli.

To dlatego przepływ niesie informację, której nie ma w żadnym komunikacie. On jest miejscem, w którym rozproszony popyt staje się widoczny.

## Prywatna informacja nie znaczy insider

Słowo prywatna informacja brzmi jak poufna wiedza o niepublikowanym komunikacie. W mikrostrukturze walutowej znaczy co innego: informację rozproszoną, potłuczoną na kawałki trzymane przez wielu uczestników, z których żaden nie widzi całości.

Te kawałki są trojakiego rodzaju. Pierwszy to potrzeby płynnościowe i portfelowe, których nikt nie ogłasza: fundusz robiący rebalancing, korporacja zabezpieczająca płatność za przejęcie, bank centralny wygładzający rezerwy. Drugi to prywatna interpretacja publicznego newsa. Dwa biura czytają ten sam odczyt inflacji inaczej, a dopiero netto ich transakcji ujawnia, jak rynek zbiorczo odczytał liczbę. Trzeci to strzępy wiedzy o fundamentach, które poszczególni gracze zbierają na własną rękę. Żaden z tych kawałków nie jest publiczny i żaden nie wypływa inaczej niż jako zlecenie. Order flow jest mechanizmem, który je agreguje.

Jest jeszcze subtelność, która domyka obraz. Nawet przesunięcie portfela o zerowej treści fundamentalnej rusza cenę, bo dealer musi dostać rekompensatę za wchłonięcie niechcianego zapasu. Przepływ przesuwa więc kurs dwoma kanałami naraz: niesie informację i zżera płynność. To drugie działa również wtedy, gdy za flow nie stoi żadna wiedza, tylko sama potrzeba.

## Dlaczego dealer uczy się z przepływu

Popatrz na to oczami dealera. Ma kwotować dwustronną cenę, nie wiedząc, czy następne zlecenie pochodzi od kogoś poinformowanego, czy od funduszu, który po prostu potrzebuje gotówki. Kiedy przepływ jest uporczywie jednostronny, dealer wnioskuje, że za nim stoi informacja albo duży popyt, i przesuwa kwotowanie, żeby nie dać się przejechać. To jest ochrona przed negatywną selekcją, czyli przed handlem z kimś, kto wie więcej.

Do tego dochodzi zarządzanie zapasem. Dealer, który nazbierał niechcianych euro, podszywa kwotowania tak, by je zrzucić, i przekazuje nierównowagę kolejnym dealerom. To wielokrotne przerzucanie zapasu między biurami, opisane przez Lyonsa jako efekt gorącego ziemniaka, pompuje przepływ międzydealerski ponad pierwotne zlecenie klienta i czyni go tak informacyjnym. Wniosek jest jeden: cena to bieżące, najlepsze przypuszczenie dealera przy danym przepływie, i przesuwa się w rytm napływających zleceń, tik po tiku, często bez żadnego nagłówka nad głową.

## Dlaczego cena rusza się bez newsa

Teraz zapłata za ten wywód. Jeśli to przepływ jest bezpośrednim motorem kursu, to ruch bez wiadomości przestaje być paradoksem. Jest śladem flow, którego nie widać. Pojedynczy duży rebalancing w cichej godzinie, program zabezpieczający, bank centralny, fundusz przekładający alokację, każde z tych zdarzeń tworzy przepływ netto, który dealerzy wchłaniają przesunięciem ceny. Żaden publiczny katalizator nie jest potrzebny, bo informacja i popyt siedziały w samym przepływie.

To przestawia też myślenie o newsie. Liczba jest publiczna, ale jej implikacja dla ceny publiczna nie jest. Rynek odkrywa ją dopiero przez handel, i właśnie dlatego kurs potrafi ruszyć wbrew oczywistej lekturze odczytu. Nie interpretacja pojedynczego analityka przesuwa cenę, tylko netto transakcji, które tę interpretację zamieniają w zlecenia.

## Co z tego ma trader detaliczny

Część niewygodna: detal nie widzi prawdziwego order flow rynku walutowego. Rynek jest zdecentralizowany i pozagiełdowy, co pokazują cykliczne badania obrotu BIS, nie ma jednej skonsolidowanej taśmy transakcji, a przepływ międzydealerski pozostaje prywatny. To, co platforma pokazuje jako wolumen, to zwykle wolumen tickowy z jednego feedu, bezznakowy i cząstkowy. Istnieją przybliżenia, na przykład order flow z kontraktów terminowych na giełdzie w Chicago albo tygodniowe raporty pozycjonowania typu COT, ale są niepełne, opóźnione i pokazują raczej stan niż strumień.

Praktyczna wartość nie jest więc gotowym sygnałem do klikania, tylko modelem mentalnym. Świadomość, że bezpośrednim motorem jest przepływ, a nie nagłówek, robi trzy rzeczy. Oducza przypisywania każdej świecy do jakiejś wiadomości. Każe traktować ruch bez newsa jako prawdziwy, bo ktoś robi wielkość, której nie widzisz. I nastraja na to, że pozycjonowanie oraz zabezpieczenia potrafią przez długie odcinki dominować nad fundamentalną historią. To jest kontekst do czytania rynku, a nie spust do wejścia.

To nie jest porada inwestycyjna. To wyłożenie mechanizmu z literatury mikrostruktury, od zagadki rozłączenia u Meese i Rogoffa, przez model portfolio shifts Evansa i Lyonsa, po obraz rynku z badań BIS, żebyś rozumiał, dlaczego cena rusza się, gdy w kalendarzu pusto, i nie mylił flow z wolumenem.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
