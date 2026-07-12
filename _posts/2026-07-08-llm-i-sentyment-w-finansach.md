---
title: "LLM i sentyment w finansach. Co potrafią, a gdzie zaczyna się hype"
description: "Analiza sentymentu tekstu finansowego to realne, dobrze postawione zadanie klasyfikacji, w którym modele dostrojone do języka finansów (FinBERT) biją modele ogólne. Ale przewidywanie ceny przez ChatGPT to inna liga: głośne prace typu „Can ChatGPT Forecast Stock Price Movements” trzeba czytać przez ryzyko look-ahead, przeciek danych z treningu i publikacyjny bias. Uczciwy wniosek: LLM to narzędzie do tekstu i kontekstu, nie wyrocznia cenowa. Źródła: FinBERT, FinGPT, BloombergGPT, Lopez-Lira i Tang, przeglądy Financial LLMs."
date: 2026-07-08 19:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
category: edukacja
dek: "Duże modele językowe świetnie streszczają i klasyfikują ton tekstu finansowego, ale to nie to samo co przewidywanie ceny. Kompendium bez hype'u: gdzie sentyment realnie pomaga jako kontekst, dlaczego modele finansowe biją ogólne i czemu prace „ChatGPT przewiduje akcje” trzeba czytać przez ryzyko look-ahead."
readingTime: 8
tags: ["LLM", "duże modele językowe", "analiza sentymentu", "FinBERT", "FinGPT", "BloombergGPT", "ChatGPT", "NLP", "przetwarzanie języka naturalnego", "look-ahead", "data leakage", "sentyment", "quant", "Forex"]
---

> **W skrócie**
>
> - **LLM przetwarza tekst, nie wróży ceny.** Duże modele językowe realnie potrafią streszczać, wyciągać fakty i klasyfikować ton (sentyment) newsów oraz raportów. To jest dobrze postawione zadanie z etykietami, które da się sprawdzić. Przewidywanie kierunku ceny to zupełnie inne, znacznie słabiej postawione zadanie i to właśnie tam obietnice rozjeżdżają się z dowodami.
> - **Model dostrojony do finansów bije model ogólny.** W klasyfikacji tonu tekstu finansowego wyspecjalizowany FinBERT (BERT dostrojony na korpusie finansowym, na przykład Financial PhraseBank) czyta branżowy język lepiej niż model ogólnego przeznaczenia, bo w finansach „zobowiązanie" czy „niższe koszty" znaczą co innego niż w języku codziennym (Araci, 2019).
> - **„Can ChatGPT Forecast Stocks" trzeba czytać krytycznie.** Głośny wynik, że sentyment z ChatGPT przewiduje zwroty (Lopez-Lira i Tang, 2023), obciążają realne ryzyka: look-ahead przez datę odcięcia treningu, przeciek danych, koncentracja efektu w małych i trudnych do arbitrażu spółkach oraz publikacyjny bias. Ciekawe, ale to nie wyrocznia.
> - **Sentyment to jedna cecha, nie strategia.** Ton tekstu jest słabym, szybko wygasającym predyktorem i dokłada wartość tylko jako jeden kontekstowy wkład obok innych, nigdy jako samodzielny generator wejść.

**Teza w jednym zdaniu:** duże modele językowe to narzędzia do przetwarzania tekstu i kontekstu (streszczanie, ekstrakcja faktów, klasyfikacja sentymentu), a nie wyrocznie cenowe, więc sentyment należy traktować jak jedną słabą cechę pod rygorem walidacji, nie jak samodzielną strategię.

## Punkt wyjścia: przetwarzanie tekstu kontra przewidywanie ceny

Hype wokół LLM w finansach żywi się jednym pomieszaniem pojęć. Model, który potrafi napisać poprawne streszczenie raportu kwartalnego, zostaje w narracji awansowany na model, który potrafi powiedzieć, dokąd pójdzie kurs. To są dwa różne zadania o dwóch różnych poziomach trudności, a różnicy nie widać, dopóki nie nazwie się jej wprost.

```
Przetwarzanie tekstu (dobrze postawione)  ->  etykiety istnieją, ton da się sprawdzić
   streszczenie, ekstrakcja faktów, klasyfikacja sentymentu
Przewidywanie ceny (źle postawione)       ->  niski sygnał, cel ucieka, przeciwnik gra
   „w którą stronę pójdzie kurs jutro"
```

Zadanie z górnego wiersza jest dla modelu językowego naturalne. Istnieje poprawna odpowiedź (streszczenie da się porównać ze źródłem, ton zdania da się oznaczyć przez człowieka), a danych tekstowych jest ogrom. Zadanie z dolnego wiersza ma wszystkie patologie rynku naraz: przewidywalna część zwrotu to ułamek szumu, cel jest niestacjonarny, a jeśli wzorzec naprawdę zarabia i zostanie odkryty, kapitał go zamyka. Uczciwe pytanie nie brzmi więc „czy LLM działa w finansach", tylko „na którym z tych dwóch zadań". Na pierwszym pomaga realnie. Na drugim głównie dostarcza dobrze brzmiących uzasadnień.

## Analiza sentymentu: co to realnie jest

Analiza sentymentu to klasyfikacja tonu tekstu wobec aktywa: pozytywny, negatywny albo neutralny. Materiałem są newsy, komunikaty spółek, transkrypcje calli wynikowych, raporty analityków i media społecznościowe. Kluczowe jest to, że jest to problem nadzorowany z etykietami. Istnieje zbiór zdań oznaczonych ręcznie przez ludzi, model uczy się je odtwarzać, a jakość mierzy się na trzymanym z boku zbiorze testowym. Klasycznym benchmarkiem jest Financial PhraseBank (Malo i wsp., 2014): zdania z newsów finansowych oznaczone wydźwiękiem przez anotatorów z wykształceniem finansowym.

To rozróżnienie decyduje o wszystkim. Sentyment jest dobrze postawiony właśnie dlatego, że istnieje prawda podstawowa (ground truth), z którą można się porównać. Wynik takiej klasyfikacji to cecha kontekstowa: przybliżony „nastrój" wokół instrumentu w danym momencie. To nie jest cel cenowy ani sygnał wejścia. To liczba opisująca ton tekstu, którą dopiero trzeba uczciwie sprawdzić jako ewentualny predyktor, i która, jak zobaczymy niżej, okazuje się predyktorem słabym.

## Dlaczego modele finansowe biją ogólne

Język finansów to dialekt, nie ten sam język, którego model nauczył się z recenzji produktów i wpisów w sieci. Słowa niosą w nim inny ładunek. „Zobowiązanie" (liability) to neutralny termin bilansowy, nie groźba. „Niższe koszty" to sygnał pozytywny, choć samo słowo „niższe" w potocznym sentymencie ciągnie w dół. Do tego dochodzi asekuracyjny styl komunikatów, podwójne przeczenia i żargon. Model ogólnego przeznaczenia regularnie się na tym potyka.

```
„Spółka obniżyła koszty i zredukowała zobowiązania."
Model ogólny:    „obniżyła", „zredukowała", „zobowiązania"  ->  wydźwięk raczej negatywny
Model finansowy: niższe koszty i mniejszy dług              ->  wydźwięk pozytywny
```

Stąd bierze się FinBERT (Araci, 2019; pokrewna linia: Yang i wsp., 2020): model BERT dostrojony na korpusie tekstów finansowych. Na benchmarkach klasyfikacji sentymentu finansowego konsekwentnie bije modele ogólne, bo dostrojenie do dziedziny uczy go tego branżowego znaczenia słów. To jest solidny, wielokrotnie potwierdzony wynik i zarazem najlepiej udokumentowana rzecz, jaką LLM wnoszą do finansów: nie prognoza, tylko lepsze czytanie tonu specjalistycznego tekstu. Warto przy tym pamiętać o skromnej naturze tej przewagi. Chodzi o dokładniejszą klasyfikację tekstu, a nie o to, że model rozumie rynek.

## FinGPT, BloombergGPT i agenci: obietnica i realne zastosowania

Generatywne LLM podniosły stawkę, bo potrafią nie tylko klasyfikować, ale i pisać. Powstały dwa bieguny. BloombergGPT (Wu i wsp., 2023) to duży, zamknięty model wytrenowany na wielkim korpusie finansowym, kosztowny i niepubliczny. FinGPT (Yang i wsp., 2023) to odpowiedź otwartoźródłowa, z naciskiem na tani pipeline danych i lekkie dostrajanie, tak by wyspecjalizowanie modelu pod zadanie finansowe było dostępne bez budżetu instytucji. Do tego doszła moda na „agentów", czyli łączenie modelu z narzędziami w wieloetapowe procesy.

Realne zwycięstwa tej rodziny są konkretne i wszystkie leżą po stronie przetwarzania tekstu. Streszczanie długich dokumentów i transkrypcji. Ekstrakcja ustrukturyzowanych faktów (liczby, podmioty, zdarzenia) z nieustrukturyzowanego tekstu. Klasyfikacja sentymentu i tematu. Wstępne szkice i przeszukiwanie dużych zbiorów dokumentów pod pytanie. To są wymierne usprawnienia pracy analitycznej. Problem zaczyna się dokładnie tam, gdzie narracja przeskakuje od „model dobrze czyta tekst" do „model dlatego przewidzi cenę". Ten przeskok nie jest podparty tak, jak podparta jest sama klasyfikacja tekstu, i to jego trzeba prześwietlić osobno.

## „Can ChatGPT Forecast Stocks": gdzie hype wyprzedza dowody

Najczęściej cytowanym dowodem na „przewidywanie" jest praca Lopez-Lira i Tang (2023), „Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models". Metoda jest prosta: model ocenia, czy nagłówek jest dobry, zły czy neutralny dla spółki, z tego powstaje liczbowy wynik sentymentu, a autorzy pokazują dodatnią korelację tego wyniku z następnym dziennym zwrotem. Portfel long-short zbudowany na tym sygnale wyglądał w próbie mocno, a starsze, prostsze modele nie dawały tego samego efektu. To realny wynik badawczy i warto go potraktować poważnie. Trzeba go jednak czytać przez standardowy zestaw ryzyk, zanim zamieni się w opowieść o wyroczni.

Pierwsze i najważniejsze ryzyko to look-ahead przez datę odcięcia treningu. LLM wytrenowany na tekście do pewnego momentu mógł wchłonąć wiedzę o tym, co stało się po danym nagłówku: późniejsze ruchy kursu, kolejne newsy, rewizje. Podanie mu historycznego nagłówka może więc zwrócić „sentyment" podszyty wiedzą z przyszłości, co zawyża przewidywalność w backteście, a na żywo znika.

```
Nagłówek z przeszłości  ->  LLM trenowany na tekście do późniejszej daty
                            (zna już, co stało się PO tym nagłówku)
                        ->  „sentyment" podszyty wiedzą z przyszłości
                        ->  backtest zawyżony, edge słabnie lub znika na żywo
```

Autorzy próbowali to ograniczyć, testując na okresie po dacie odcięcia modelu, i to uczciwe posunięcie. Problem w ogólności pozostaje jednak subtelny: przeciek nie dotyczy tylko cen, a każde użycie wytrenowanego wcześniej LLM do historycznego backtestu wymaga tej samej ostrożności. Do tego dochodzą trzy zwykłe podejrzenia. Koncentracja efektu w małych, mało płynnych i trudnych do krótkiej sprzedaży spółkach, gdzie papierowy edge topnieje po realnych kosztach i ograniczeniach egzekucji. Publikacyjny bias, bo wynik pozytywny się publikuje, a szuflada z „nie przewidział" zostaje zamknięta. I krucha replikowalność między okresami. Najuczciwsza interpretacja tej pracy jest taka: pokazuje ona, że analiza sentymentu ma wartość i że LLM robią ją dobrze, a nie że ChatGPT jest maszyną do prognozy ceny. Sygnałem jest tu sentyment, słaby i kosztowny w zebraniu, nie magiczna prognoza.

## Sentyment to jedna cecha, nie strategia

Nawet gdy sentyment realnie coś przewiduje, jest to predyktor słaby i szybko wygasający. Rynek wycenia jawne informacje szybko, więc ton newsa, który każdy może odczytać, traci moc w kolejnych godzinach lub dniach. To nie dyskwalifikuje sentymentu, ale wyznacza mu właściwe miejsce: jest jednym wkładem kontekstowym obok innych, a nie samodzielnym generatorem wejść. Traktowanie go jak strategii to ta sama pomyłka co w naiwnym uczeniu maszynowym na surowej cenie, tylko z tekstem zamiast świec.

Skoro sentyment jest cechą, obowiązują go te same rygory walidacji co każdą inną. Podział na trening i test musi respektować przyczynowość (trening na przeszłości, test na przyszłości, bez mieszania obserwacji), trzeba wykluczyć przeciek informacji z przyszłości (zwłaszcza ten wbudowany w LLM), a wynik trzeba deflować o liczbę wypróbowanych konfiguracji. Cecha sentymentu, która przeżyje ten filtr, bywa użyteczna jako kontekst. Cecha, która żyje wyłącznie w efektownym backteście, jest artefaktem procedury, a nie przewagą.

## Co z tego wynika przy stole

Uczciwa mapa jest wąska i spójna. LLM to narzędzie do tekstu: streszczą raport, wyciągną fakty, sklasyfikują ton, a model dostrojony do finansów zrobi to lepiej niż ogólny. To realna wartość, ale wartość po stronie przetwarzania języka, nie prognozy. Wyrocznia cenowa, która z newsa wyprodukuje pewny kierunek, jest produktem marketingu, bo dobrze się sprzedaje, a nie dowodu.

Zanim liczba sentymentu wpłynie na decyzję, warto zadać pięć pytań. Czy to jest klasyfikacja tekstu (dobrze postawiona) czy przebrane za nią przewidywanie ceny. Czy model jest dostrojony do dziedziny, czy ogólny. Czy w oknie testowym nie ma look-ahead wynikającego z daty treningu użytego LLM. Czy efekt przeżywa koszty i wychodzi poza małe, niepłynne spółki. I czy sentyment jest jedną cechą pod uczciwą walidacją, czy całą strategią. Sygnał, który przechodzi ten filtr, jest skromniejszy, niż obiecuje hype, ale za to jest prawdziwym kontekstem, a nie wróżbą.

To nie jest porada inwestycyjna. To uczciwa ocena narzędzia: gdzie LLM i analiza sentymentu w finansach realnie pomagają (czytanie i porządkowanie tekstu), gdzie zaczyna się hype (przewidywanie ceny) i jaką dyscypliną odróżnić jedno od drugiego, zanim zaufasz liczbie na wykresie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
