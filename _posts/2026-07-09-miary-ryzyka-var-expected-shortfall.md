---
title: "VaR i Expected Shortfall. Dlaczego jedna liczba ryzyka kłamie"
description: "Value at Risk kusi prostotą i milczy o najważniejszym: jak głęboka jest strata, gdy już przekroczy próg. VaR ignoruje kształt ogona i potrafi karać dywersyfikację, bo nie jest subaddytywny. Expected Shortfall, czyli średnia strata w najgorszych przypadkach, patrzy w ogon i spełnia aksjomaty spójnej miary ryzyka Artznera. Definicje, cztery własności i źródła, bez zmyślonych liczb."
date: 2026-07-09 23:00:00 +0200
eyebrow: "Edukacja · ryzyko"
dek: "VaR sprowadza ryzyko do jednej liczby i właśnie dlatego bywa mylący: nie mówi nic o tym, jak głęboka jest strata za progiem, a czasem karze dywersyfikację. Expected Shortfall patrzy w ogon i spełnia warunki spójnej miary ryzyka. Definicje, cztery aksjomaty Artznera i różnica, która rośnie przy grubych ogonach."
readingTime: 8
tags: ["VaR", "Value at Risk", "Expected Shortfall", "CVaR", "coherent risk measure", "spójna miara ryzyka", ryzyko, "grube ogony", subaddytywność, Artzner, "Acerbi & Tasche", "Rockafellar & Uryasev", RiskMetrics, "zarządzanie ryzykiem", statystyka, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - VaR na poziomie ufności X% to kwantyl straty: z prawdopodobieństwem X% strata w danym horyzoncie nie przekroczy VaR. Kusi, bo to jedna liczba, którą łatwo wpisać do raportu i porównać między dniami.
> - VaR kłamie w dwóch miejscach. Nie mówi nic o tym, jak zła jest strata, GDY już przebije próg, bo ignoruje wszystko, co leży w ogonie. Do tego bywa niesubaddytywny, czyli potrafi pokazać wyższe ryzyko dla połączonego portfela niż suma ryzyk osobnych pozycji, a to karze dywersyfikację.
> - Expected Shortfall (ES), zwany też CVaR, to średnia strata w najgorszych X% przypadków. Nie pyta „gdzie zaczyna się ogon", tylko „jak ciężki jest średnio ogon". Spełnia wszystkie cztery aksjomaty spójnej miary ryzyka Artznera, a VaR jednego z nich, subaddytywności, nie spełnia.
> - Przy zwrotach dalekich od normalnych, ze skosem i grubymi ogonami, różnica między VaR a ES rośnie, bo cała informacja o katastrofie siedzi właśnie w ogonie, który VaR pomija z definicji.

**Teza w jednym zdaniu:** VaR mówi, gdzie zaczyna się zły scenariusz, ale milczy, jak bardzo zły on jest, i potrafi ukarać dywersyfikację, podczas gdy Expected Shortfall odpowiada na oba pytania i jako jedyny z tej pary jest spójną miarą ryzyka.

## VaR: jedna liczba, która kusi

Value at Risk odpowiada na proste pytanie: jaka jest strata, której z zadanym prawdopodobieństwem nie przekroczysz w ustalonym oknie czasu. Formalnie to kwantyl rozkładu straty na wybranym poziomie ufności.

```
VaR_α = najmniejsza strata L, dla której  P(strata ≤ L) ≥ α

α        = poziom ufności (np. 0.99 albo 0.975)
horyzont = ustalone okno (1 dzień, 10 dni)

Czyta się tak: z prawdopodobieństwem α strata w tym oknie nie przekroczy VaR_α,
a w pozostałych (1 − α) przypadkach przekroczy, ale o ile, tego VaR nie mówi.
```

Cała siła VaR to jedna liczba. Zamiast opisywać rozkład, mówisz „dzienny VaR 99% wynosi tyle" i każdy wie, gdzie postawiono płot. Właśnie ta zwięzłość zrobiła z VaR standard branżowy, spopularyzowany przez dokument RiskMetrics banku JP Morgan z połowy lat dziewięćdziesiątych. Problem w tym, że jedna liczba, która ma zastąpić cały ogon rozkładu, musi coś przemilczeć. VaR przemilcza dokładnie to, co najważniejsze w sytuacji kryzysowej.

## Gdzie VaR kłamie: milczy o głębi ogona

Pierwsza wada jest wbudowana w definicję. VaR to próg, a nie średnia za progiem. Wskazuje granicę „złych" scenariuszy, ale kompletnie nie rozróżnia, co się za tą granicą dzieje.

Wyobraź sobie dwie strategie o identycznym dziennym VaR 99%. W pierwszej te najgorsze 1% dni to straty tylko odrobinę większe od progu. W drugiej te same 1% dni to katastrofy wielokrotnie głębsze, bo rozkład ma gruby lewy ogon. VaR obu strategii jest taki sam, a ich realne ryzyko ruiny jest przepaścią. VaR z definicji nie zagląda za próg, więc nie widzi tej różnicy. Mówi, kiedy zaczyna się zły dzień, ale nie mówi, jak zły on będzie.

To nie jest subtelność akademicka. Miara, która jest ślepa na głębokość ogona, zachęca wprost do sprzedawania ryzyka ogonowego: strategie typu „zbieraj drobne, raz na jakiś czas oberwij dużym ciosem" potrafią mieć bardzo ładny VaR aż do dnia, w którym ogon się realizuje. VaR nie ostrzeże, bo katastrofa mieści się w tym 1%, którego on nie opisuje.

## Druga wada: VaR potrafi karać dywersyfikację

Druga wada jest głębsza i mniej oczywista. Dobra miara ryzyka powinna nagradzać dywersyfikację, albo przynajmniej jej nie karać: połączenie dwóch pozycji nie może mieć ryzyka większego niż suma ryzyk osobnych. Ta własność nazywa się subaddytywnością. VaR w ogólności jej nie spełnia.

Klasyczny kontrprzykład to dwie niezależne obligacje, każda z małym prawdopodobieństwem bankructwa. Weź poziom ufności tak dobrany, że pojedyncze bankructwo jest rzadsze niż próg ogona. Wtedy VaR każdej obligacji z osobna potrafi wynosić zero, bo scenariusz bankructwa nie mieści się w mierzonym ogonie. Ale portfel dwóch obligacji ma już zauważalną szansę, że zbankrutuje przynajmniej jedna, i ten scenariusz wchodzi do ogona. W efekcie VaR portfela jest dodatni, czyli większy niż suma dwóch zer.

```
Subaddytywność wymaga:   VaR(A + B) ≤ VaR(A) + VaR(B)

Kontrprzykład (dwie rzadkie porażki):
   VaR(A) = 0,  VaR(B) = 0,  ale  VaR(A + B) > 0
   czyli  VaR(A + B) > VaR(A) + VaR(B)   ← złamana subaddytywność
```

Wniosek jest paradoksalny: według VaR rozłożenie ryzyka na dwie niezależne pozycje wygląda groźniej niż trzymanie każdej osobno. Miara, która ma pilnować ryzyka, karze tu dokładnie to, co ryzyko realnie zmniejsza. Dla portfela złożonego z wielu pozycji oznacza to, że sumowanie VaR-ów po biurkach czy instrumentach może dawać wynik oderwany od prawdy, w którą stronę, zależy od kształtu rozkładów.

## Expected Shortfall: średnia z ogona, nie jego próg

Lekarstwem jest miara, która zamiast wskazywać próg, uśrednia to, co za nim leży. Expected Shortfall, znany też jako Conditional VaR (CVaR) lub Expected Tail Loss, to średnia strata w najgorszych (1 − α) przypadkach.

```
ES_α = średnia strata w najgorszych (1 − α) przypadkach
     = E[ strata | strata ≥ VaR_α ]                (dla rozkładów ciągłych)
     = (1 / (1 − α)) · ∫ VaR_u du,   u przebiega od α do 1

Czyta się tak: nie „gdzie zaczyna się ogon", tylko „jak ciężki jest średnio ogon".
```

Różnica wobec VaR jest jednym zdaniem: VaR to próg wejścia w ogon, ES to średnia z całego ogona za tym progiem. Dlatego ES zawsze jest co najmniej tak duży jak VaR na tym samym poziomie, a zwykle większy. Dwie strategie z rozdziału o głębi ogona, nierozróżnialne przez VaR, dostają wyraźnie różne ES: ta z grubszym ogonem ma wyższe Expected Shortfall, bo uśrednia głębsze straty. ES widzi to, na co VaR jest ślepy z konstrukcji.

Trzecia postać definicji, całka z VaR po poziomach ufności, jest wygodna obliczeniowo. Rockafellar i Uryasev pokazali, że CVaR daje się zapisać jako zadanie optymalizacji wypukłej, a przy danych historycznych sprowadza się do programowania liniowego. To praktyczna przewaga: portfel minimalizujący ES można policzyć wprost, czego o minimalizacji VaR (funkcji niewypukłej, z wieloma minimami lokalnymi) w ogólności powiedzieć się nie da.

<figure>
<svg viewBox="0 0 640 324" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><defs><marker id="esarr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#e5484d" stroke-width="1.6"/></marker></defs><text x="20" y="26" font-size="14" fill="currentColor">Rozkład zwrotów: VaR i Expected Shortfall</text><text x="20" y="44" font-size="11" fill="currentColor" opacity="0.55">Strata rośnie w lewo, zysk w prawo. Lewy ogon jest gruby.</text><path d="M 60,250 L 60,230.1 L 64,229.1 L 68,227.9 L 72,226.8 L 76,225.6 L 80,224.3 L 84,223.0 L 88,221.7 L 92,220.3 L 96,218.8 L 100,217.3 L 104,215.8 L 108,214.2 L 112,212.6 L 116,210.9 L 120,209.1 L 124,207.3 L 128,205.5 L 132,203.6 L 136,201.7 L 140,199.7 L 144,197.6 L 148,195.5 L 152,193.4 L 156,191.2 L 160,189.0 L 164,186.7 L 168,184.4 L 172,182.1 L 176,179.7 L 180,177.2 L 184,174.8 L 188,172.3 L 192,169.7 L 196,167.2 L 200,164.6 L 200,250 Z" fill="#e5484d" fill-opacity="0.35"/><line x1="60" y1="250" x2="600" y2="250" stroke="currentColor" stroke-width="1" opacity="0.4"/><path d="M 60,230.1 L 64,229.1 L 68,227.9 L 72,226.8 L 76,225.6 L 80,224.3 L 84,223.0 L 88,221.7 L 92,220.3 L 96,218.8 L 100,217.3 L 104,215.8 L 108,214.2 L 112,212.6 L 116,210.9 L 120,209.1 L 124,207.3 L 128,205.5 L 132,203.6 L 136,201.7 L 140,199.7 L 144,197.6 L 148,195.5 L 152,193.4 L 156,191.2 L 160,189.0 L 164,186.7 L 168,184.4 L 172,182.1 L 176,179.7 L 180,177.2 L 184,174.8 L 188,172.3 L 192,169.7 L 196,167.2 L 200,164.6 L 204,162.0 L 208,159.3 L 212,156.7 L 216,154.0 L 220,151.3 L 224,148.7 L 228,146.0 L 232,143.3 L 236,140.5 L 240,137.9 L 244,135.2 L 248,132.5 L 252,129.8 L 256,127.2 L 260,124.5 L 264,121.9 L 268,119.4 L 272,116.8 L 276,114.3 L 280,111.9 L 284,109.5 L 288,107.1 L 292,104.8 L 296,102.5 L 300,100.4 L 304,98.2 L 308,96.2 L 312,94.2 L 316,92.3 L 320,90.5 L 324,88.7 L 328,87.0 L 332,85.5 L 336,84.0 L 340,82.6 L 344,81.3 L 348,80.1 L 352,79.0 L 356,78.0 L 360,77.1 L 364,76.4 L 368,75.7 L 372,75.1 L 376,74.7 L 380,74.4 L 384,74.1 L 388,74.0 L 392,74.0 L 396,74.4 L 400,75.0 L 404,76.0 L 408,77.3 L 412,79.0 L 416,80.9 L 420,83.1 L 424,85.6 L 428,88.4 L 432,91.4 L 436,94.7 L 440,98.2 L 444,101.9 L 448,105.7 L 452,109.8 L 456,113.9 L 460,118.2 L 464,122.6 L 468,127.1 L 472,131.7 L 476,136.3 L 480,140.9 L 484,145.6 L 488,150.2 L 492,154.8 L 496,159.4 L 500,163.9 L 504,168.3 L 508,172.7 L 512,176.9 L 516,181.1 L 520,185.1 L 524,189.1 L 528,192.9 L 532,196.5 L 536,200.0 L 540,203.4 L 544,206.6 L 548,209.7 L 552,212.7 L 556,215.4 L 560,218.1 L 564,220.6 L 568,222.9 L 572,225.1 L 576,227.2 L 580,229.1 L 584,230.9 L 588,232.6 L 592,234.2 L 596,235.7 L 600,237.0" fill="none" stroke="currentColor" stroke-width="1.7"/><line x1="200" y1="250" x2="200" y2="90" stroke="#0b66c3" stroke-width="1.8"/><text x="200" y="84" font-size="13" fill="#0b66c3" text-anchor="middle">VaR</text><text x="200" y="100" font-size="9.5" fill="#0b66c3" opacity="0.85" text-anchor="middle">próg (np. 5%)</text><line x1="146" y1="250" x2="146" y2="150" stroke="#e5484d" stroke-width="1.8" stroke-dasharray="5 3"/><text x="146" y="142" font-size="13" fill="#e5484d" text-anchor="middle">ES</text><text x="146" y="158" font-size="9.5" fill="#e5484d" opacity="0.9" text-anchor="middle">średnia ogona</text><path d="M200 226 H152" fill="none" stroke="#e5484d" stroke-width="1.4" marker-end="url(#esarr)"/><text x="176" y="219" font-size="9.5" fill="#e5484d" opacity="0.9" text-anchor="middle">głębiej</text><text x="130" y="284" font-size="10.5" fill="#e5484d" opacity="0.95" text-anchor="middle">5% najgorszych przypadków</text><rect x="20" y="292" width="11" height="11" rx="2" fill="#0b66c3"/><text x="38" y="301" font-size="11" fill="currentColor" opacity="0.8">VaR mówi, gdzie zaczyna się zły przypadek.</text><rect x="20" y="309" width="11" height="11" rx="2" fill="#e5484d"/><text x="38" y="318" font-size="11" fill="currentColor" opacity="0.8">ES mówi, jak zły jest średnio, gdy już nastąpi.</text></svg>
<figcaption>Schemat rozkładu zwrotów z grubym lewym ogonem. Pionowa niebieska linia to VaR, czyli próg: kwantyl, poniżej którego leży ustalony procent najgorszych przypadków, tu przykładowo 5%. Czerwony obszar to ten ogon. Expected Shortfall to średnia strata w całym zacienionym ogonie, dlatego leży głębiej niż VaR. VaR mówi, gdzie zaczyna się zły przypadek, a ES jak zły jest on średnio, gdy już nastąpi.</figcaption>
</figure>

## Spójna miara ryzyka: cztery aksjomaty Artznera

Skąd wiadomo, że ES jest „lepszy", a nie tylko inny? Artzner, Delbaen, Eber i Heath w pracy z 1999 roku postawili pytanie odwrotnie niż zwykle: nie „jaki wzór", tylko „jakie własności powinna mieć KAŻDA rozsądna miara ryzyka". Wyszły z tego cztery aksjomaty. Miarę, która spełnia wszystkie, nazwali spójną (coherent).

```
Miara ryzyka ρ jest SPÓJNA (Artzner i wsp., 1999), gdy dla dowolnych pozycji X, Y:

1. Monotoniczność
   jeśli X zawsze daje gorszy wynik niż Y  ⇒  ρ(X) ≥ ρ(Y)
   (gorsza pozycja nie może mieć niższego ryzyka)

2. Subaddytywność
   ρ(X + Y) ≤ ρ(X) + ρ(Y)
   (łączenie pozycji nie zwiększa ryzyka, dywersyfikacja nie szkodzi)

3. Jednorodność dodatnia
   ρ(λ · X) = λ · ρ(X)   dla λ ≥ 0
   (podwojenie pozycji podwaja ryzyko)

4. Niezmienniczość na translację
   ρ(X + gotówka a) = ρ(X) − a
   (dołożenie pewnej gotówki a obniża ryzyko dokładnie o a)
```

Te aksjomaty to nie estetyka, tylko warunki zdrowego rozsądku. Monotoniczność mówi, że gorsze pozycje nie mogą wyglądać na bezpieczniejsze. Jednorodność, że skala pozycji przekłada się liniowo na ryzyko. Niezmienniczość na translację, że dołożenie bufora gotówki obniża ryzyko o wartość tego bufora. A subaddytywność to matematyczny zapis tego, że dywersyfikacja pomaga.

Puenta Artznera jest ostra: Expected Shortfall spełnia wszystkie cztery. VaR spełnia trzy, ale łamie subaddytywność, co pokazał przykład z obligacjami. Dlatego VaR nie jest spójną miarą ryzyka, a ES jest. Acerbi i Tasche uściślili później samą definicję Expected Shortfall (rozprawiając się z niejednoznacznościami przy rozkładach nieciągłych) i dowiedli formalnie, że tak zdefiniowany ES jest spójny. To zamknęło sprawę teoretyczną: z dwóch popularnych miar tylko jedna przechodzi test aksjomatów.

## Grube ogony: dlaczego różnica VaR i ES rośnie

Kiedy różnica między VaR a ES jest mała, a kiedy przepastna? Odpowiedź brzmi: zależy od ogona. Przy rozkładzie normalnym obie miary są znanymi wielokrotnościami odchylenia standardowego i sztywno powiązane.

```
Rozkład normalny (strata ~ Normal(μ, σ)):

VaR_α = μ + σ · z_α                    z_α = kwantyl normalny (z_0.99 ≈ 2.33)
ES_α  = μ + σ · φ(z_α) / (1 − α)       φ = gęstość rozkładu normalnego

Przy normalności ES to VaR przemnożony przez znany, stały czynnik.
Cały ogon jest „lekki" i przewidywalny, więc próg i średnia z ogona idą w parze.
```

Kłopot w tym, że zwroty rynkowe rzadko są normalne. Mają grube ogony i często ujemny skos, czyli duże straty zdarzają się częściej i są głębsze, niż przewiduje krzywa dzwonowa. Gdy podłożysz rozkład z grubym ogonem, na przykład t-Studenta o niskiej liczbie stopni swobody, VaR rośnie umiarkowanie, bo próg przesuwa się tylko trochę, natomiast ES rośnie znacznie mocniej, bo uśrednia teraz naprawdę głębokie straty zza progu. Iloraz ES do VaR, prawie stały przy normalności, zaczyna puchnąć.

To jest sedno praktyczne całej dyskusji. Im bardziej rynek odbiega od normalności, tym więcej informacji o ryzyku ucieka VaR-owi, bo cała różnica między „nieprzyjemnym" a „katastrofalnym" scenariuszem siedzi w kształcie ogona, którego VaR nie mierzy. Na spokojnym, quasi-normalnym rynku obie liczby mówią prawie to samo. Dokładnie w kryzysie, gdy ogon tyje, rozjeżdżają się najbardziej, a VaR uspokaja najmocniej wtedy, kiedy najmniej powinien.

## Skąd to się wzięło i dokąd poszło

Warto znać kolejność zdarzeń, bo tłumaczy, dlaczego VaR wciąż jest wszędzie, mimo znanych wad. Najpierw był RiskMetrics, dokument techniczny JP Morgan z lat 1994 i 1996, który dał VaR gotową metodologię (podejście wariancja-kowariancja przy założeniu normalności) i rozpowszechnił go jako wspólny język ryzyka. To był ogromny krok, jedna liczba, którą dało się raportować i porównywać.

Potem przyszła krytyka od strony teorii. Artzner i współautorzy (1999) zdefiniowali spójne miary ryzyka i wskazali, że VaR łamie subaddytywność. Rockafellar i Uryasev (2000 i 2002) pokazali, że CVaR jest nie tylko spójny, ale też wygodny obliczeniowo, bo optymalizowalny metodami wypukłymi. Acerbi i Tasche (2002) domknęli definicję Expected Shortfall i udowodnili jej spójność także dla rozkładów, które nie są ciągłe. Trzy nurty, teoria aksjomatyczna, optymalizacja i statystyka, zeszły się w tym samym wniosku: ES bije VaR tam, gdzie to się liczy, czyli w ogonie i w traktowaniu dywersyfikacji.

Regulator poszedł tą drogą. W ramach przeglądu wymogów kapitałowych dla portfeli handlowych (Fundamental Review of the Trading Book) Komitet Bazylejski zastąpił dawny VaR 99% przez Expected Shortfall na poziomie 97.5% jako podstawę kapitału na ryzyko rynkowe. Dobór poziomu 97.5% nie jest przypadkowy: przy rozkładzie normalnym ES 97.5% wypada blisko VaR 99%, więc zmiana miary nie oznacza automatycznie skokowo innej liczby na spokojnym rynku, za to daje właściwą wrażliwość na ogon, gdy rynek przestaje być normalny.

## Co z tego wynika przy stole

Praktyczny wniosek jest prosty. VaR to dobry pierwszy komunikat, „gdzie stoi płot", i zła miara ryzyka ogonowego, bo z definicji nie zagląda za płot. Jeśli raportujesz tylko VaR, opowiadasz, kiedy zaczyna się zły scenariusz, i przemilczasz, jak bardzo zły on jest. Expected Shortfall dopowiada brakujące zdanie: średnią głębokość ogona. Uczciwy opis ryzyka pojedynczej pozycji czy całego portfela podaje obie liczby, a nie jedną.

Dwie rzeczy warto zapamiętać poza wzorami. Po pierwsze, przy sumowaniu ryzyka po wielu pozycjach VaR potrafi wprowadzić w błąd co do korzyści z dywersyfikacji, bo nie jest subaddytywny; ES tego błędu nie popełnia. Po drugie, im dalej rynek od rozkładu normalnego, tym większa różnica między tymi miarami, i tym bardziej sam VaR usypia czujność, im grubszy jest ogon, który pomija. Dla operatora, który świadomie handluje strategiami zbierającymi drobne z ryzykiem rzadkiego dużego ciosu, ta różnica nie jest akademicka, to jest różnica między liczbą, która widzi katastrofę, a liczbą, która jej nie widzi.

To nie jest porada inwestycyjna. To rozłożone na czynniki definicje dwóch miar ryzyka wraz z ich własnościami i źródłami, żebyś umiał odróżnić „gdzie zaczyna się strata" od „jak głęboka ona jest", zanim postawisz na tej różnicy pieniądze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
