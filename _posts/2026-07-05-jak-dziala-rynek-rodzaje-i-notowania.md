---
title: "Jak działa rynek. Giełda, OTC i dwa modele handlu"
description: "Dwa podstawowe modele handlu: rynek kierowany cenami, na którym dealer podaje bid i ask i bierze drugą stronę każdej transakcji, oraz rynek kierowany zleceniami z centralną księgą, w której uczestnicy handlują między sobą. Tekst wyjaśnia różnicę między giełdą a OTC, rolę izby rozliczeniowej i nowacji, kontrakt animatora rynku, fragmentację płynności z dark pools oraz to, gdzie w tej układance stoi detaliczny trader na FX i na akcjach. Na źródłach: Harris, Hasbrouck, BIS."
date: 2026-07-05 10:00:00 +0200
eyebrow: "Edukacja · mikrostruktura"
dek: "Zanim na wykresie pojawi się jakakolwiek cena, ktoś musi skojarzyć kupującego ze sprzedającym. Tekst rozkłada na części dwa mechanizmy, które to robią: dealera kwotującego ceny i centralną księgę zleceń, a dalej różnicę między giełdą a rynkiem OTC, nowację w izbie rozliczeniowej, umowę animatora rynku i fragmentację płynności z dark pools. Na końcu: co z tej architektury widzi i za co płaci detalista na FX i na akcjach. Po polsku, na mechanice, bez obietnic."
readingTime: 8
tags: ["struktura rynku", mikrostruktura, giełda, OTC, "quote-driven", "order-driven", dealer, "księga zleceń", "izba rozliczeniowa", CCP, nowacja, "animator rynku", "market maker", "dark pools", "fragmentacja płynności", Forex, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Są dwa podstawowe modele handlu. Na rynku kierowanym cenami (quote-driven) dealer podaje jednocześnie bid i ask, bierze drugą stronę każdej transakcji na własny rachunek i zarabia spread; tak działa rynek walutowy i większość obligacji. Na rynku kierowanym zleceniami (order-driven) uczestnicy wysyłają oferty do wspólnej księgi zleceń i handlują między sobą; tak działają giełdy akcji.
> - Giełda i rynek pozagiełdowy (OTC) różnią się na trzech osiach: standaryzacji instrumentu, przejrzystości kwotowań i transakcji oraz sposobie rozliczenia. OTC nie znaczy niszowy: rynek walutowy, największy rynek finansowy świata, jest pozagiełdowy w całości.
> - Na rynkach giełdowych między strony transakcji wchodzi izba rozliczeniowa (CCP). Przez nowację staje się kupującym dla każdego sprzedającego i sprzedającym dla każdego kupującego, więc nikt nie musi oceniać wypłacalności anonimowego kontrahenta. Na detalicznym FX takiej izby nie ma: kontrahentem jest broker.
> - Płynność tego samego instrumentu bywa rozproszona po wielu miejscach handlu, w tym po dark pools, które nie pokazują ofert przed transakcją. Zlecenie detalisty na akcjach trafia do jawnej księgi albo jest internalizowane przez market makera; na FX zawsze wykonuje się przeciw dealerowi.

**Teza w jednym zdaniu:** Nie istnieje jeden uniwersalny „rynek": każdy instrument handluje się w konkretnym mechanizmie, dealerskim albo zleceniowym, giełdowym albo pozagiełdowym, a ten mechanizm przesądza, kto stoi po drugiej stronie transakcji, ile płynności widać i kto gwarantuje rozliczenie.

## Handel to problem znalezienia drugiej strony

Zanim na wykresie pojawi się jakakolwiek cena, ktoś musi rozwiązać prozaiczny problem: skojarzyć kogoś, kto chce kupić, z kimś, kto chce sprzedać, i to tak, żeby obaj zaakceptowali warunki. Rynek jest mechanizmem rozwiązywania tego problemu, a struktura rynku, jak ujmuje ją Larry Harris w podręczniku „Trading and Exchanges" (2003), to zestaw reguł określających, kto może handlować, czym, kiedy i w jaki sposób. Te reguły nie są dekoracją. Przesądzają, jak powstaje cena, kto dostarcza płynność i kto za nią płaci.

Problem „gdzie jest druga strona" ma dwa czyste rozwiązania. Pierwsze: wyspecjalizowany pośrednik trzyma zapas instrumentu i deklaruje, że zawsze odkupi i zawsze sprzeda, za odpowiednią cenę. To model dealerski. Drugie: wspólna tablica, na której wszyscy zainteresowani wywieszają swoje oferty i czekają, aż ktoś je przyjmie. To model księgi zleceń. Praktycznie każda konstrukcja rynkowa na świecie jest jednym z tych dwóch modeli albo ich hybrydą.

## Model pierwszy: dealer kwotuje i bierze drugą stronę

Na rynku kierowanym cenami (quote-driven) centralną postacią jest dealer. Podaje jednocześnie dwie ceny: bid, po której gotów jest kupić, i ask, po której gotów jest sprzedać. Klient, który chce handlować, nie szuka drugiego klienta. Zawiera transakcję z dealerem, a dealer bierze jej drugą stronę na własny rachunek: sprzedając klientowi, wchodzi w pozycję krótką, kupując od niego, w długą. Wynagrodzeniem dealera jest spread, różnica między ask a bid: kupuje taniej, sprzedaje drożej, a różnica zostaje u niego, o ile zdąży obrócić pozycję, zanim rynek ruszy przeciwko niej.

To „o ile" jest istotą zawodu. Dealer nie musi mieć poglądu na kierunek; ma za to zapas, którego nie chce. Po każdej transakcji zarządza pozycją: odsprzedaje ją innym dealerom, kompensuje przepływem kolejnych klientów, przesuwa kwotowania tak, żeby zachęcić rynek do zdjęcia z niego ryzyka. Harris opisuje dealerów jako sprzedawców natychmiastowości: klient płaci spread nie za prognozę, tylko za to, że może zawrzeć transakcję od ręki, bez czekania i bez szukania kontrahenta.

W czystym modelu dealerskim nie ma jednej publicznej tablicy ofert. Kwotowanie bywa odpowiedzią na pytanie konkretnego klienta (request for quote), ważną kilka sekund, i może zależeć od tego, kto pyta. Tak zorganizowany jest rynek walutowy, rynek większości obligacji skarbowych i korporacyjnych oraz duża część instrumentów pochodnych. Cena rynkowa w takim świecie nie jest wpisem w centralnym rejestrze, tylko wypadkową kwotowań konkurujących ze sobą dealerów.

## Model drugi: wspólna księga zleceń

Na rynku kierowanym zleceniami (order-driven) nie ma wyznaczonego pośrednika, z którym wszyscy handlują. Jest wspólna księga zleceń: uporządkowana lista ofert kupna i sprzedaży z limitem ceny, wystawianych przez samych uczestników. Zlecenia przeciwstawne kojarzą się według jawnego algorytmu, najczęściej priorytetu cena-czas: pierwszeństwo ma lepsza cena, a przy równych cenach zlecenie złożone wcześniej. Kontrahentem jest inny uczestnik rynku, a operator giełdy pozostaje poza transakcją: dostarcza reguły, technologię i nadzór, ale sam nie kupuje i nie sprzedaje.

Płynność w tym modelu nie pochodzi z obowiązku, tylko z decyzji: dostarcza ją każdy, kto wystawi zlecenie z limitem i poczeka, a bierze ten, kto wykona się natychmiast po cudzej ofercie. Obok notowań ciągłych rynki zleceniowe używają aukcji (call auction), zwykle na otwarcie i zamknięcie sesji: zlecenia zbierają się przez pewien czas bez wykonywania, po czym system wyznacza jedną cenę maksymalizującą skojarzony wolumen i po niej wykonuje wszystkie pasujące zlecenia. Tak działają giełdy akcji i kontraktów terminowych.

Podział nie biegnie jednak wzdłuż klas aktywów, tylko wzdłuż mechanizmu. Współczesne giełdy akcji zapraszają do swoich ksiąg kontraktowych animatorów, czyli dealerów osadzonych w strukturze zleceniowej. A rdzeń hurtowego rynku walutowego, międzydealerskie platformy elektroniczne, to technicznie klasyczne księgi zleceń, tyle że dostępne dla wąskiego grona. Modele się przenikają, dlatego produktywne pytanie brzmi zawsze tak samo: kto jest kontrahentem i skąd pochodzi kwotowanie.

<figure>
<svg viewBox="0 0 680 330" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="mArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 2L8 5L2 8" fill="none" stroke="currentColor" stroke-width="1.4"/></marker></defs><text x="20" y="26" font-size="13" fill="currentColor">Rynek kierowany cenami</text><text x="20" y="43" font-size="10.5" fill="currentColor" opacity="0.55">quote-driven: klient handluje z dealerem</text><rect x="24" y="72" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="63" y="89" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">klient</text><rect x="238" y="72" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="277" y="89" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">klient</text><rect x="24" y="248" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="63" y="265" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">klient</text><rect x="238" y="248" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="277" y="265" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">klient</text><rect x="110" y="146" width="120" height="54" rx="8" fill="#0b66c3" fill-opacity="0.14" stroke="#0b66c3" stroke-width="1.5"/><text x="170" y="167" font-size="12" font-weight="600" fill="#0b66c3" text-anchor="middle">DEALER</text><text x="170" y="185" font-size="9.5" fill="currentColor" opacity="0.75" text-anchor="middle">kwotuje bid i ask</text><line x1="70" y1="98" x2="128" y2="144" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-start="url(#mArr)" marker-end="url(#mArr)"/><line x1="270" y1="98" x2="212" y2="144" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-start="url(#mArr)" marker-end="url(#mArr)"/><line x1="70" y1="246" x2="128" y2="202" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-start="url(#mArr)" marker-end="url(#mArr)"/><line x1="270" y1="246" x2="212" y2="202" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-start="url(#mArr)" marker-end="url(#mArr)"/><text x="20" y="316" font-size="10.5" fill="currentColor" opacity="0.6">dealer jest stroną każdej transakcji i zarabia spread</text><line x1="340" y1="52" x2="340" y2="300" stroke="currentColor" stroke-width="1" opacity="0.14"/><text x="360" y="26" font-size="13" fill="currentColor">Rynek kierowany zleceniami</text><text x="360" y="43" font-size="10.5" fill="currentColor" opacity="0.55">order-driven: uczestnicy handlują między sobą</text><rect x="364" y="72" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="403" y="89" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">uczestnik</text><rect x="578" y="72" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="617" y="89" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">uczestnik</text><rect x="364" y="248" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="403" y="265" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">uczestnik</text><rect x="578" y="248" width="78" height="26" rx="6" fill="none" stroke="currentColor" stroke-opacity="0.4"/><text x="617" y="265" font-size="10" fill="currentColor" opacity="0.8" text-anchor="middle">uczestnik</text><rect x="450" y="138" width="120" height="70" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.5"/><text x="510" y="156" font-size="10.5" font-weight="600" fill="currentColor" text-anchor="middle">KSIĘGA ZLECEŃ</text><rect x="464" y="166" width="52" height="9" rx="2" fill="#e5484d" opacity="0.9"/><text x="524" y="174" font-size="9" fill="#e5484d">ASK</text><rect x="464" y="182" width="64" height="9" rx="2" fill="#1a9e6a" opacity="0.9"/><text x="536" y="190" font-size="9" fill="#1a9e6a">BID</text><text x="510" y="224" font-size="9.5" fill="currentColor" opacity="0.6" text-anchor="middle">priorytet cena-czas</text><line x1="410" y1="98" x2="456" y2="136" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-end="url(#mArr)"/><line x1="610" y1="98" x2="564" y2="136" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-end="url(#mArr)"/><line x1="410" y1="246" x2="456" y2="212" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-end="url(#mArr)"/><line x1="610" y1="246" x2="564" y2="212" stroke="currentColor" stroke-width="1.2" opacity="0.5" marker-end="url(#mArr)"/><text x="408" y="118" font-size="9" fill="currentColor" opacity="0.6">zlecenia</text><text x="360" y="316" font-size="10.5" fill="currentColor" opacity="0.6">operator kojarzy zlecenia, sam nie jest stroną transakcji</text></svg>
<figcaption>Dwa modele handlu obok siebie. Po lewej rynek kierowany cenami: klienci handlują z dealerem, który kwotuje bid i ask i bierze każdą transakcję na własny rachunek. Po prawej rynek kierowany zleceniami: uczestnicy wysyłają zlecenia do wspólnej księgi, gdzie kojarzą się według priorytetu cena-czas, a operator rynku nie jest stroną żadnej transakcji.</figcaption>
</figure>

## Giełda kontra OTC: standaryzacja, przejrzystość, rozliczenie

Drugi wielki podział, giełda kontra rynek pozagiełdowy (OTC, over the counter), często myli się z pierwszym, ale dotyczy czego innego: nie tego, jak kojarzone są zlecenia, tylko tego, w jakich ramach prawnych i operacyjnych żyje transakcja. Różnice układają się na trzech osiach.

Standaryzacja. Na giełdzie handluje się instrumentem zdefiniowanym przez giełdę: ta sama akcja, ten sam kontrakt terminowy o identycznych parametrach dla wszystkich. Na OTC transakcja jest umową dwustronną i może być szyta na miarę, jak forward walutowy na dowolną kwotę i dowolną datę. Standaryzacja koncentruje płynność w jednym punkcie; krawiectwo na miarę ją rozprasza, ale pozwala dopasować instrument do konkretnej potrzeby.

Przejrzystość. Giełda publikuje kwotowania (przejrzystość przed transakcją) i zawarte transakcje (przejrzystość po transakcji); wspólna taśma jest częścią produktu. Na OTC widzi się głównie to, o co się samemu zapyta: kwotowania są bilateralne, a informacja o cudzych transakcjach bywa ograniczona albo opóźniona. Joel Hasbrouck w „Securities Trading: Principles and Procedures" podkreśla, że to raczej kontinuum niż ostra granica: elektroniczne platformy wielodealerskie i obowiązki raportowania transakcji przesuwają część rynków OTC w stronę półprzejrzystości.

Rozliczenie. Transakcja giełdowa trafia do izby rozliczeniowej i jest gwarantowana systemowo. Transakcja OTC pozostaje zobowiązaniem dwóch podmiotów i jej wykonanie zależy od ich wypłacalności. Po kryzysie 2008 roku regulatorzy przenieśli znaczną część standaryzowanych derywatów OTC do rozliczania centralnego właśnie dlatego, że sieć bilateralnych ekspozycji okazała się nieprzejrzysta i krucha.

Jedno zastrzeżenie do intuicji: OTC nie znaczy marginalny ani gorszy. Rynek walutowy, największy rynek finansowy świata, jest pozagiełdowy w całości, podobnie jak lwia część rynku długu.

## Izba rozliczeniowa: nowacja zamiast ryzyka kontrahenta

Zawarcie transakcji to dopiero obietnica: jedna strona ma dostarczyć instrument, druga zapłacić. Między tymi momentami żyje ryzyko kontrahenta, czyli ryzyko, że druga strona nie wykona zobowiązania. Rynki giełdowe rozwiązują je izbą rozliczeniową działającą jako centralny kontrpartner (CCP), a kluczowy mechanizm nazywa się nowacją. Brzmi prawniczo, ale jest prosty: w chwili zawarcia transakcji pierwotna umowa między kupującym a sprzedającym przestaje istnieć i zostaje zastąpiona dwiema nowymi, w których stroną jest izba.

```
NOWACJA W IZBIE ROZLICZENIOWEJ (CCP)

przed nowacją:

  KUPUJĄCY <------------------------------> SPRZEDAJĄCY
             jedna umowa dwustronna: każda strona ponosi
             ryzyko, że druga nie wykona zobowiązania

po nowacji:

  KUPUJĄCY <-------> CCP <-------> SPRZEDAJĄCY

  dwie umowy w miejsce jednej: izba jest sprzedającym
  dla kupującego i kupującym dla sprzedającego
```

Konsekwencje są trzy. Po pierwsze, anonimowość przestaje być problemem: nie trzeba oceniać wypłacalności przypadkowego kontrahenta z księgi, bo prawnie kontrahentem jest zawsze izba. Po drugie, pozycje się kompensują (netting): kupno i sprzedaż tego samego instrumentu znoszą się w rozliczeniu do pozycji netto, co radykalnie zmniejsza liczbę i wartość przepływów. Po trzecie, izba nie jest naiwna: własne ryzyko obudowuje depozytami zabezpieczającymi pobieranymi od uczestników przy otwarciu pozycji i uzupełnianymi w miarę ruchu cen oraz wspólnym funduszem gwarancyjnym na wypadek upadłości uczestnika. Hasbrouck opisuje ten łańcuch, od zawarcia do rozrachunku, jako cichą infrastrukturę rynku: widać ją dopiero wtedy, gdy coś w niej pęka.

Warto to od razu odnieść do FX: na detalicznym rynku walutowym CCP nie ma. Transakcja z brokerem jest zobowiązaniem brokera i niczyim więcej, dlatego jego regulacja, segregacja środków klientów i wypłacalność to nie biurokratyczne detale, tylko jedyna warstwa ochrony.

## Animator rynku: obowiązki w zamian za przywileje

Skoro w księdze zleceń płynność jest dobrowolna, giełda ma problem: w mniej popularnych instrumentach księga potrafi świecić pustkami. Rozwiązaniem jest animator rynku (market maker, na części giełd designated market maker): dealer, który podpisuje z giełdą lub emitentem umowę o dostarczanie płynności. Umowa jest wymianą obowiązków za przywileje i to jest cała jej treść.

Obowiązki: kwotować dwustronnie, czyli utrzymywać w księdze jednocześnie ofertę kupna i sprzedaży, nie szerzej niż umowny maksymalny spread, na co najmniej umowną wielkość i przez określoną część czasu sesji. Także wtedy, gdy nikt inny kwotować nie chce, bo dokładnie po to animator istnieje. Przywileje: obniżone opłaty transakcyjne lub rabaty za dodawanie płynności, czasem wynagrodzenie od emitenta albo giełdy. Historycznie bywały mocniejsze: dawny specjalista na NYSE, opisany szeroko u Harrisa, miał wyłączny wgląd w księgę zleceń swojego papieru i uczestniczył w kojarzeniu każdej transakcji. Rynki elektroniczne zredukowały te przywileje głównie do ekonomii opłat, ale konstrukcja przetrwała: giełda kupuje ciągłość kwotowań, animator sprzedaje gotowość do handlu.

Widać tu, że czysty podział z początku tekstu jest w praktyce hybrydą: rynek zleceniowy z wbudowanymi, kontraktowymi dealerami. Zasadnicza różnica względem rynku dealerskiego pozostaje: animator konkuruje w jawnej księdze na tych samych prawach cenowych co każde inne zlecenie.

## Fragmentacja płynności i dark pools

Nic nie zmusza całego handlu jednym instrumentem do spotkania w jednym miejscu. Ta sama akcja bywa notowana na giełdzie macierzystej i równolegle handlowana na giełdach konkurencyjnych, platformach alternatywnych i u internalizatorów. To fragmentacja płynności: zamiast jednej księgi istnieje wiele równoległych, a najlepsza dostępna cena jest rozczłonkowana między nie. Z powrotem skleja ją arbitraż oraz technologia kierowania zleceń (smart order routing), a na amerykańskim rynku akcji dodatkowo regulacja: zlecenia nie wolno wykonać po cenie gorszej niż najlepsza widoczna kwota w skonsolidowanych notowaniach (NBBO).

Osobną kategorią miejsc handlu są dark pools: systemy, które nie publikują ofert przed transakcją. Zlecenia w nich są niewidoczne, a kojarzenie odbywa się zwykle po cenie środkowej zaczerpniętej z rynków jawnych. Sens ekonomiczny jest konkretny: instytucja, która musi kupić duży pakiet, nie chce wywieszać zamiaru w jawnej księdze, bo sama informacja o dużym kupującym przesuwa cenę, zanim cokolwiek zostanie kupione. Ciemne miejsce handlu pozwala szukać drugiej strony bez ujawniania się. Koszt jest systemowy: ciemny obrót korzysta z cen ustalanych w jawnych księgach, ale sam się do ich ustalania nie dokłada, więc im większa jego część, tym mniej informacji niesie widoczny rynek. Hasbrouck omawia tę architekturę na przykładzie rynku amerykańskiego, ale mechanizm jest uniwersalny.

## FX z bliska: sieć dealerów bez centralnej giełdy

Rynek walutowy składa te klocki w konfigurację, którą warto znać, bo na niej handluje każdy detaliczny trader FX. Według analizy BIS (Rime i Schrimpf, „The anatomy of the global FX market", BIS Quarterly Review 2013) średni dzienny obrót na rynku walutowym wynosił w kwietniu 2013 około 5.3 biliona dolarów, z czego na rynek kasowy (spot) przypadało około 2 bilionów. Nie ma centralnej giełdy ani wspólnej taśmy transakcji; jest zdecentralizowana sieć, od dziesięcioleci zorganizowana w dwa poziomy. Rdzeń to handel między dealerami, w tym przez międzydealerskie platformy elektroniczne będące technicznie księgami zleceń. Wokół rdzenia handlują klienci, od korporacji po fundusze, na zasadach kwotowań dealerskich.

Rime i Schrimpf pokazują przy tym, że elektronizacja rozmyła dwupoziomowy porządek: handel dealerów z instytucjami finansowymi niebędącymi dealerami przewyższył handel międzydealerski, prime brokerage wpuścił do rdzenia fundusze i agregatorów detalicznych, a kwotowania płyną przez platformy jednodealerskie i wielodealerskie. Dla detalisty łańcuch wygląda tak: broker pobiera kwotowania od swoich dostawców płynności, składa z nich własną cenę, dokłada narzut i wystawia ją klientowi. Transakcja klienta wykonuje się przeciw brokerowi albo jest przez niego przekazywana dalej, ale w żadnym wariancie nie trafia do centralnej księgi, bo taka księga dla detalicznego FX nie istnieje.

## Co z tego wynika dla detalisty

Z całej tej architektury wynikają rzeczy bardzo praktyczne, choć żadna nie jest sygnałem transakcyjnym.

Na FX handluje się w modelu dealerskim: kontrahentem jest broker lub jego dostawca płynności, kwotowanie jest prywatną kompozycją brokera, a nie ceną z centralnego rejestru, i nie istnieje jedna „prawdziwa" cena, z którą można by je porównać; dwóch brokerów może w tej samej sekundzie uczciwie pokazywać różne kwoty. Nie ma izby rozliczeniowej, więc ryzyko kontrahenta to ryzyko brokera. Spread nie jest opłatą z cennika, tylko ceną natychmiastowości u dealera, i rozszerza się dokładnie wtedy, gdy dealerzy widzą podwyższone ryzyko: wokół publikacji danych i w płytkich godzinach.

Na akcjach zlecenie żyje w świecie zleceniowo-giełdowym: trafia do jawnej księgi, gdzie kontrahentem jest anonimowy uczestnik, a rozliczenie gwarantuje CCP, albo zostaje internalizowane, czyli wykonane przez market makera na jego własny rachunek zanim dotrze na giełdę, z obowiązkiem ceny nie gorszej niż najlepsza widoczna. Fragmentacja i dark pools sprawiają, że jawna księga pokazuje część obrazu, nie całość.

Trzy pytania porządkują każdy rynek, na którym przychodzi handlować: kto jest kontrahentem transakcji, skąd pochodzi kwotowanie i kto gwarantuje rozliczenie. Odpowiedzi nie dają przewagi, ale mówią, które ryzyka są strukturalne, a które negocjowalne, i za co dokładnie płaci się w spreadzie.

To nie jest porada inwestycyjna. To opis architektury rynków, podany z definicjami i źródłami, żeby dało się rozumieć, z kim naprawdę zawiera się transakcję, skąd bierze się cena na ekranie i kto gwarantuje rozliczenie, zanim postawi się na tym pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
