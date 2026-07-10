---
title: "Formacje, wsparcia i opory. Realne czy pareidolia"
description: "Dwa spojrzenia na formacje cenowe: mistyczne, w którym wzór przewiduje ruch, i mechaniczne, w którym wzór to zapis zachowania zleceń. Wsparcie i opór jako skupiska take-profitów i stop-lossów (Osler, NY Fed 2002), granice samospełniającej się przepowiedni oraz werdykt Lo, Mamaysky'ego i Wanga (Journal of Finance 2000): kilka formacji niesie istotną statystycznie informację, ale informatywność to nie zyskowność po kosztach."
date: 2026-07-04 13:00:00 +0200
eyebrow: "Edukacja · analiza techniczna"
category: edukacja
dek: "Głowa z ramionami, trójkąt, wsparcie na okrągłej cenie. Jedni wierzą, że wzór na wykresie przewiduje przyszłość, drudzy widzą w nim tylko twarze w chmurach. Rzetelna odpowiedź leży pośrodku: poziomy to realna mapa skupisk zleceń, a nie wyrocznia, a formacja rozpoznana po fakcie to nie to samo co reguła testowalna z góry."
readingTime: 8
tags: ["analiza techniczna", "formacje cenowe", "wsparcie i opór", "pareidolia", "samospełniająca się przepowiednia", "order flow", "Lo Mamaysky Wang", "Osler", "Edwards Magee", "głowa z ramionami", "okrągłe poziomy", "stop loss", "EUR/USD", "Forex", "quant"]
---

> **W skrócie**
>
> - Formacje można czytać dwojako: mistycznie, gdzie wzór sam „przewiduje" ruch, i mechanicznie, gdzie wzór jest zapisem tego, gdzie leżały i jak wykonały się zlecenia. Tylko drugi odczyt da się sprawdzić danymi.
> - Wsparcie i opór działają nie dlatego, że są magiczne, tylko dlatego, że wielu uczestników umieściło tam zlecenia: take-profity, stop-lossy i zlecenia ustawione z pamięci poprzednich reakcji. Osler (NY Fed, 2002) pokazała ten układ na około 9700 rzeczywistych zleceniach dealera FX.
> - Samospełniająca się przepowiednia wzmacnia poziom, dopóki patrzą na niego wszyscy naraz, ale pęka, gdy napłynie realna informacja albo duży kapitał. Koordynacja bez fundamentu jest krucha.
> - Lo, Mamaysky i Wang (Journal of Finance, 2000) zautomatyzowali rozpoznawanie formacji regresją jądrową: kilka niesie realną, istotną statystycznie informację, ale autorzy wprost zastrzegli, że informatywność to nie zyskowność po kosztach.

**Teza w jednym zdaniu:** formacje, wsparcia i opory są realne o tyle, o ile są zapisem zachowania zleceń, a nie wróżbą z kształtu, więc traktuj je jak mapę skupisk i prawdopodobieństw, testuj reguły z góry i pamiętaj, że mózg widzi wzory także w czystym szumie.

## Dwa spojrzenia na ten sam wykres

Kiedy trader rysuje na wykresie trójkąt albo linię wsparcia, robi jedną z dwóch bardzo różnych rzeczy, choć wygląda to identycznie. W pierwszym ujęciu, nazwijmy je mistycznym, wzór ma moc sprawczą: sam kształt „przewiduje" ruch, jakby rynek pamiętał geometrię i chciał ją dokończyć. Głowa z ramionami „zapowiada" spadek, bo tak głosi katalog formacji. Figura jest tu przyczyną.

W drugim ujęciu, mechanicznym, wzór niczego nie przewiduje. Wzór jest zapisem. Kształt na wykresie to ślad po tym, gdzie uczestnicy składali zlecenia, po jakich cenach je realizowali i gdzie ustawiali ochronę. Poziom, który „trzyma", trzyma dlatego, że siedzi na nim ściana zleceń przeciwnych do ruchu, a nie dlatego, że liczba jest okrągła czy ładna. Różnica między tymi spojrzeniami jest fundamentalna: pierwsze traktuje wykres jak wyrocznię, drugie jak mapę pozycjonowania. Tylko drugie da się sprawdzić danymi i tylko drugie broni się w rzetelnych badaniach.

<figure>
<svg viewBox="0 0 640 210" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ten sam wykres w dwóch odczytach: mistycznym, gdzie wzór przewiduje ruch, i mechanicznym, gdzie wzór zapisuje zlecenia">
<text x="320" y="24" font-size="13" fill="currentColor" text-anchor="middle">Ten sam wykres, dwa odczyty</text>
<g transform="translate(276,44)">
<rect x="0" y="0" width="88" height="60" rx="5" fill="none" stroke="currentColor" stroke-opacity="0.35"/>
<polyline points="8,44 20,30 30,38 42,18 54,40 66,22 80,34" fill="none" stroke="currentColor" stroke-width="1.6" stroke-opacity="0.7"/>
</g>
<text x="320" y="122" font-size="10.5" fill="currentColor" text-anchor="middle" opacity="0.6">ten sam szereg cen</text>
<line x1="270" y1="74" x2="212" y2="74" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.4"/>
<polygon points="210,74 219,70 219,78" fill="currentColor" opacity="0.5"/>
<line x1="370" y1="74" x2="428" y2="74" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.4"/>
<polygon points="430,74 421,70 421,78" fill="currentColor" opacity="0.5"/>
<rect x="20" y="44" width="188" height="120" rx="6" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-opacity="0.25"/>
<text x="34" y="66" font-size="12" fill="#0b66c3">Spojrzenie mistyczne</text>
<text x="34" y="90" font-size="11" fill="currentColor" opacity="0.8">wzór PRZEWIDUJE ruch</text>
<text x="34" y="110" font-size="11" fill="currentColor" opacity="0.8">figura jako przyczyna</text>
<text x="34" y="130" font-size="11" fill="currentColor" opacity="0.8">rozpoznana po fakcie</text>
<text x="34" y="150" font-size="10.5" fill="currentColor" opacity="0.55">ex post, nietestowalne</text>
<rect x="432" y="44" width="188" height="120" rx="6" fill="#0b66c3" fill-opacity="0.08" stroke="#0b66c3" stroke-opacity="0.4"/>
<text x="446" y="66" font-size="12" fill="#0b66c3">Spojrzenie mechaniczne</text>
<text x="446" y="90" font-size="11" fill="currentColor" opacity="0.8">wzór ZAPISUJE zlecenia</text>
<text x="446" y="110" font-size="11" fill="currentColor" opacity="0.8">figura jako skutek</text>
<text x="446" y="130" font-size="11" fill="currentColor" opacity="0.8">definicja z góry</text>
<text x="446" y="150" font-size="10.5" fill="currentColor" opacity="0.55">ex ante, testowalne</text>
<text x="320" y="196" font-size="10.5" fill="currentColor" text-anchor="middle" opacity="0.6">tylko prawy odczyt da się sprawdzić i broni się w badaniach</text>
</svg>
<figcaption>Ten sam szereg cen można odczytać dwojako. W ujęciu mistycznym figura sama „przewiduje" ruch i jest rozpoznawana po fakcie, więc nie da się jej sprawdzić. W ujęciu mechanicznym figura jest zapisem zachowania zleceń, take-profitów i stop-lossów, a regułę można zdefiniować z góry i przetestować na danych, których się wcześniej nie widziało.</figcaption>
</figure>

## Wsparcie i opór to skupiska zleceń, nie magia liczby

Zacznijmy od najprostszego pojęcia technika: poziomu wsparcia i oporu. Dlaczego cena tak często zatrzymuje się w tych samych miejscach? Odpowiedź mistyczna mówi o „pamięci rynku". Odpowiedź mechaniczna jest mniej efektowna i znacznie lepiej udokumentowana: bo w tych miejscach wielu uczestników jednocześnie umieściło zlecenia. Take-profity, którymi zamykają zysk. Stop-lossy, którymi tną stratę. Zlecenia ustawione z pamięci poprzednich reakcji, bo skoro poziom raz odbił, to następnym razem ktoś postawi tam zlecenie na wszelki wypadek. Gęstość zleceń w jednym punkcie robi z niego barierę.

To nie jest spekulacja, tylko rzecz policzona przez bank centralny na rzeczywistych danych, co rozkłada osobny tekst o [polowaniu na stopy u Osler](/dlogic-quant/2026/07/09/polowanie-na-stopy-istnieje-osler-ny-fed/). Carol Osler w raporcie NY Fed z 2002 roku przebadała około 9700 rzeczywistych zleceń dużego dealera FX i pokazała, że take-profity gromadzą się na okrągłych cenach, stąd odbicia, a stop-lossy leżą tuż za nimi, stąd wystrzały i kaskady po przebiciu. Poziom działa więc nie magią liczby, tylko geometrią zleceń wokół niej. To jest cała tajemnica wsparcia i oporu: nie prorokują, tylko pokazują, gdzie tłum coś położył.

## Samospełniająca się przepowiednia i jej granice

Skoro poziom działa przez zlecenia, pojawia się mechanizm, który wzmacnia sam siebie. Jeśli wszyscy patrzą na tę samą okrągłą cenę i wszyscy oczekują tam reakcji, to ich własne zlecenia tę reakcję tworzą. Trader widzi opór na 1.1000, więc stawia tam sprzedaż. Dość wielu robi to samo, więc cena faktycznie się cofa, co utwierdza kolejnych w przekonaniu, że poziom działa. To jest klasyczna samospełniająca się przepowiednia: przekonanie produkuje zachowanie, które potwierdza przekonanie.

I tu jest granica, o której mistyczna wersja milczy. Koordynacja oczekiwań działa tylko do momentu, w którym napłynie coś, czego oczekiwania nie obejmują: realna informacja albo duży kapitał. Odczyt makro, decyzja banku centralnego, wielki flow jednego uczestnika, wszystko to przechodzi przez poziom jak przez papier, bo po drugiej stronie stoi popyt lub podaż silniejszy niż ściana take-profitów. Samospełniająca się przepowiednia jest krucha, bo opiera się wyłącznie na koordynacji, a nie na wartości. Poziom trzyma, dopóki nikt dostatecznie duży nie zdecyduje inaczej. Dlatego zdanie „poziom działał, aż przestał" to nie porażka techniki, tylko dokładny opis jej natury: to statystyczna tendencja podtrzymywana zbiorowym zachowaniem, a nie prawo fizyki.

## Formacja to narracja, dopóki nie stanie się regułą

Z pojedynczym poziomem jest jeszcze w miarę prosto. Problem robi się poważny przy formacjach: głowie z ramionami, trójkątach, flagach, klinach. Tu wchodzi cecha ludzkiego mózgu, która na wykresie działa przeciwko nam. Mózg jest maszyną do wykrywania wzorów i wykrywa je wszędzie, także tam, gdzie ich nie ma. To pareidolia, ten sam mechanizm, który każe nam widzieć twarze w chmurach albo króliki w plamach na ścianie. Na wykresie cen, który w dużej części jest szumem, pareidolia gwarantuje, że zawsze znajdziemy jakąś formację, jeśli tylko dostatecznie mocno się wpatrzymy.

Stąd bierze się najważniejsze rozróżnienie całego tematu. Formacja rozpoznana z prawej strony wykresu, po fakcie, kiedy ruch już się wydarzył, to nie jest to samo co reguła testowalna z góry. Ex post łatwo pokazać idealną głowę z ramionami tuż przed spadkiem, bo wybieramy ją spośród setek układów, wiedząc już, który zadziałał. To jest wybieranie zwycięzcy po wyścigu. Reguła testowalna jest odwrotna: definiujesz kształt precyzyjnie z góry, potem sprawdzasz go na danych, których nie widziałeś, licząc wszystkie przypadki, także te, w których formacja zawiodła. Dopiero wtedy narracja zamienia się w hipotezę, którą da się potwierdzić albo obalić. Dopóki opowiadasz historię do gotowego wykresu, opowiadasz historię.

## Co pokazały rzetelne badania: informacja tak, obietnica nie

Czy po odrzuceniu subiektywnego oka z formacji zostaje cokolwiek? Najpoważniejszą próbę odpowiedzi dali Lo, Mamaysky i Wang w Journal of Finance w 2000 roku. Zamiast rysować formacje ręcznie, zautomatyzowali ich rozpoznawanie: wygładzili wykresy akcji amerykańskich z lat 1962-1996 regresją jądrową i kazali algorytmowi wykrywać klasyczne kształty, w tym głowę z ramionami. W ten sposób z testu zniknął najsłabszy element analizy technicznej, czyli oko analityka, które widzi to, co chce zobaczyć. Potem porównali rozkład zwrotów po wystąpieniu formacji z rozkładem bezwarunkowym.

Wynik był niewygodny dla obu obozów. Kilka formacji rzeczywiście niesie informację: rozkłady warunkowe różnią się od bezwarunkowych w sposób istotny statystycznie, więc po pewnych kształtach rynek zachowuje się mierzalnie inaczej niż przeciętnie. Wykres nie jest więc czystym szumem. Ale, i to jest zastrzeżenie samych autorów, informatywność to nie zyskowność. Rozkład może różnić się na tyle, żeby zobaczył to test statystyczny, i jednocześnie za mało, żeby zobaczył to rachunek maklerski po spreadzie i prowizjach. Praca celowo nie twierdzi, że na formacjach da się zarabiać. Ta granica między „niesie informację" a „daje zysk po kosztach" to oś całej debaty o technice, którą rozkłada osobny tekst [czy analiza techniczna działa](/dlogic-quant/2026/07/07/czy-analiza-techniczna-dziala-badania/).

Warto dodać kontekst historyczny. Katalog formacji, z którego korzysta cała branża, spisali Edwards i Magee w klasycznej „Technical Analysis of Stock Trends" z 1948 roku. To dzieło opisowe: porządkuje i nazywa kształty, ale nie testuje ich statystycznie, bo w 1948 roku nie było do tego ani danych, ani narzędzi. Wartość pracy Lo, Mamaysky'ego i Wanga polega właśnie na tym, że wzięli opisową tradycję i po raz pierwszy przepuścili ją przez rygor. Odpowiedź nie brzmi „formacje to bzdura" ani „formacje działają", tylko „kilka niesie mierzalną informację, ale to nie to samo co przewaga do wypłaty".

## Jak to ustawić w głowie

Z tego wszystkiego płynie kilka konkretnych zasad, które nie obiecują zysku, tylko chronią przed najczęstszymi błędami.

Po pierwsze, traktuj poziomy jak mapę skupisk zleceń i prawdopodobieństw, a nie jak wyrocznię. Wsparcie nie gwarantuje odbicia, tylko podnosi szansę zatrzymania, bo tam jest gęsto od zleceń przeciwnych. To zmienia sposób myślenia: nie „poziom mnie obroni", tylko „w tym miejscu jest strukturalnie większa szansa reakcji, a także większa szansa gwałtownego przebicia, gdy reakcji zabraknie".

Po drugie, testuj reguły, nie dopasowuj opowieści do wykresu po fakcie. Zanim uwierzysz, że jakiś kształt działa, zdefiniuj go precyzyjnie i policz, jak wypadał również wtedy, gdy zawiódł. Jeśli liczysz tylko trafienia, a pomijasz nietrafienia, mierzysz własną pamięć, a nie rynek.

Po trzecie, i to najbardziej konkretne, nie kładź stop-lossa tuż za oczywistym poziomem. Skoro wszyscy widzą tę samą okrągłą cenę i wszyscy chowają stopy w tym samym miejscu, to tam czeka klaster, po który rynek strukturalnie sięga, jak pokazała Osler. Stop schowany dwa pipsy za pełną setką stoi dokładnie tam, gdzie jest najgęściej. Lepiej oprzeć go o realną strukturę, poprzedni dołek czy szczyt, niż o ładną liczbę, którą widzi cały tłum.

Wspólny mianownik tych zasad jest jeden. Formacje, wsparcia i opory są realne dokładnie w tym stopniu, w jakim są zapisem zachowania zleceń, i przestają być realne dokładnie w tym momencie, w którym zamieniasz je we wróżbę z kształtu. Cała technika mieści się między tymi dwoma zdaniami.

To nie jest porada inwestycyjna. To wykład o tym, czym są formacje i poziomy w świetle mikrostruktury oraz recenzowanych badań, żeby oddzielić realną mechanikę zleceń od widzenia twarzy w chmurach, zanim oprzesz na wykresie decyzję.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
