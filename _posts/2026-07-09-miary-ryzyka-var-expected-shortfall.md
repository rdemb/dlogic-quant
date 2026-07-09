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
