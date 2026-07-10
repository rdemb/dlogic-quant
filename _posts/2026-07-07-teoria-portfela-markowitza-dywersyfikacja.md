---
title: "Teoria portfela Markowitza. Jedyny darmowy obiad w finansach"
description: "Markowitz w 1952 roku odwrócił sposób myślenia o inwestowaniu: ocenia się portfel jako całość, a ryzyko aktywa mierzy się jego wkładem do ryzyka portfela. Wzór na wariancję portfela, korelacja jako serce dywersyfikacji, granica efektywna oraz uczciwa lista ograniczeń: error maximization, korelacje rosnące w kryzysie, grube ogony. Na koniec nowoczesna odpowiedź na kruchość optymalizacji: Hierarchical Risk Parity Lópeza de Prado."
date: 2026-07-07 14:00:00 +0200
eyebrow: "Edukacja · portfel"
dek: "Dywersyfikację nazywa się jedynym darmowym obiadem w finansach i to hasło ma twarde matematyczne jądro: przy korelacji poniżej jedności ryzyko portfela spada, a oczekiwany zwrot nie. Jest też drobny druk, o którym mówi się rzadziej: optymalizator Markowitza wzmacnia błędy estymacji, a korelacje rosną dokładnie wtedy, gdy dywersyfikacja jest najbardziej potrzebna."
readingTime: 8
tags: [Markowitz, "teoria portfela", dywersyfikacja, korelacja, "wariancja portfela", "granica efektywna", "mean-variance", "Hierarchical Risk Parity", "López de Prado", Ilmanen, "zarządzanie ryzykiem", "błąd estymacji", quant, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Do 1952 roku analiza inwestycji sprowadzała się do pytania, które aktywo jest najlepsze. Markowitz w "Portfolio Selection" (Journal of Finance, 1952) odwrócił perspektywę: ocenia się portfel jako całość, a ryzyko pojedynczego aktywa liczy się przez jego wkład do ryzyka portfela, nie przez samotną zmienność. Ta zmiana punktu widzenia przyniosła mu w 1990 roku Nagrodę Nobla z ekonomii.
> - Oczekiwany zwrot portfela to zwykła średnia ważona zwrotów składników. Ryzyko już nie: dopóki korelacja składników jest niższa od jedności, zmienność portfela jest mniejsza niż średnia ważona ich zmienności. Ta asymetria to całe matematyczne jądro darmowego obiadu: część ryzyka znika, a oczekiwany zwrot zostaje.
> - Granica efektywna to zbiór portfeli, których nie da się poprawić: żaden inny portfel nie daje wyższego oczekiwanego zwrotu przy tym samym ryzyku ani niższego ryzyka przy tym samym zwrocie. Cała reszta chmury możliwych portfeli jest zdominowana.
> - Uczciwe zastrzeżenia: optymalizacja mean-variance jest krucha, bo wejścia trzeba estymować, a małe błędy estymacji produkują skrajne wagi (error maximization). Korelacje rosną w kryzysach dokładnie wtedy, gdy dywersyfikacja jest najbardziej potrzebna, a wariancja nie widzi grubych ogonów. Nowoczesną odpowiedzią są podejścia hierarchiczne jak HRP (López de Prado, 2016), budujące portfel z klastrów zamiast z odwracanej macierzy kowariancji.

**Teza w jednym zdaniu:** Dywersyfikacja to jedyny mechanizm w finansach, który obniża ryzyko bez proporcjonalnej utraty oczekiwanego zwrotu, ale klasyczna maszyneria Markowitza, czyli optymalizacja mean-variance, jest krucha na błędy estymacji i wymaga pokory dokładnie tam, gdzie obiecuje precyzję.

## Rewolucja 1952: patrz na portfel, nie na aktywo

W marcu 1952 roku w Journal of Finance ukazał się artykuł "Portfolio Selection". Autor, Harry Markowitz, był wtedy doktorantem z Chicago, a niemal cztery dekady później dostał za tę pracę Nagrodę Nobla z ekonomii (1990, wspólnie z Millerem i Sharpe'em). Punkt wyjścia jest zaskakująco prosty. Gdyby inwestorowi chodziło wyłącznie o maksymalizację oczekiwanego zwrotu, powinien włożyć cały kapitał w jedno aktywo, to z najwyższą oczekiwaną stopą. Żadna reguła oparta na samym oczekiwanym zwrocie nigdy nie zaleci dywersyfikacji. Tymczasem inwestorzy dywersyfikują i mają rację. Markowitz stawia sprawę ostro: dywersyfikacja jest zarówno obserwowana, jak i sensowna, więc reguła postępowania, z której nie wynika jej wyższość, musi zostać odrzucona i jako hipoteza, i jako maksyma.

Skoro liczy się nie tylko zwrot, potrzebna jest druga współrzędna. Markowitz proponuje wariancję zwrotów i każe oceniać każdy portfel parą liczb: oczekiwany zwrot oraz wariancja (w pracy nazywa to regułą E-V). Brzmi technicznie, ale niesie zmianę filozoficzną. Ryzyko przestaje być cechą pojedynczego aktywa, a staje się cechą całości. O tym, czy aktywo jest ryzykowne w portfelu, decyduje nie jego samotna zmienność, tylko to, jak porusza się względem reszty. Aktywo o dużej zmienności, które chodzi w kontrze do pozostałych, może ryzyko portfela obniżać.

Z tego samego powodu Markowitz odróżnia dywersyfikację właściwą od naiwnej. Portfel sześćdziesięciu spółek kolejowych nie jest dobrze zdywersyfikowany, bo wszystkie zależą od tej samej koniunktury. Ten sam kapitał rozłożony między kolej, energetykę, górnictwo i przetwórstwo jest zdywersyfikowany lepiej, choć pozycji może być mniej. Liczy się współporuszanie, nie liczba wierszy w portfelu.

## Dwa wzory, które robią całą robotę

Oczekiwany zwrot portfela dwóch aktywów to średnia ważona:

```
E[Rp] = w₁·E[R₁] + w₂·E[R₂]
```

Wariancja portfela średnią ważoną nie jest i w tym miejscu zaczyna się cała teoria:

```
σp² = w₁²·σ₁² + w₂²·σ₂² + 2·w₁·w₂·ρ₁₂·σ₁·σ₂

wᵢ   = waga aktywa i (udział w kapitale)
σᵢ   = odchylenie standardowe zwrotów aktywa i
ρ₁₂  = korelacja zwrotów obu aktywów (od −1 do +1)
```

Dwa pierwsze składniki to indywidualne ryzyka, stłumione kwadratami wag. Trzeci składnik jest sercem wzoru, bo to w nim siedzi korelacja. Zauważ, że w formule na zwrot korelacji nie ma wcale: oczekiwany zwrot portfela jest taki sam niezależnie od tego, czy składniki chodzą razem, osobno czy przeciwnie. Ryzyko natomiast zależy od korelacji wprost. Cała korzyść z dywersyfikacji mieszka w jednym parametrze trzeciego składnika.

Dla większej liczby aktywów wzór uogólnia się na sumę po wszystkich parach:

```
σp² = Σᵢ Σⱼ wᵢ·wⱼ·σᵢ·σⱼ·ρᵢⱼ        (ρᵢᵢ = 1)
```

## Korelacja: serce dywersyfikacji

Podstaw liczby, a intuicja robi się namacalna. Dwa aktywa o zmienności 10% każde, kapitał podzielony po połowie:

```
ρ = +1.0  →  σp = 10.0%    zero korzyści: ryzyko to średnia ważona
ρ = +0.5  →  σp ≈ 8.7%
ρ =  0.0  →  σp ≈ 7.1%
ρ = −0.5  →  σp = 5.0%
ρ = −1.0  →  σp = 0.0%     ryzyko można zredukować do zera
```

W każdym wierszu oczekiwany zwrot portfela jest identyczny, bo wagi i składniki się nie zmieniły. Zmienia się wyłącznie ryzyko. Im niższa korelacja, tym większa redukcja ryzyka bez oddania choćby punktu bazowego oczekiwanego zwrotu. To jest dokładnie ta własność, przez którą dywersyfikację nazywa się darmowym obiadem (powiedzenie przypisuje się samemu Markowitzowi): na rynku prawie za wszystko płaci się zwrotem, tu wyjątkowo nie.

Skala korzyści rośnie z liczbą składników. Dla aktywów nieskorelowanych i równych wag:

```
σp = σ / √N

N = 4   →  ryzyko spada o połowę
N = 16  →  ryzyko spada czterokrotnie
```

W praktyce aktywa nieskorelowane prawie nie istnieją, więc działa wersja słabsza: dywersyfikacja wygasza ryzyko specyficzne składników, ale nie zejdzie poniżej podłogi, którą wyznacza średnia kowariancja, czyli wspólny czynnik, na którym wszystko jedzie. Warto też zobaczyć, jak szybko rośnie liczba parametrów, bo ta obserwacja wróci w sekcji o ograniczeniach:

```
liczba wariancji      = N
liczba par korelacji  = N·(N−1)/2

N = 10  →  45 par
N = 50  →  1225 par
```

Przy pięćdziesięciu aktywach o ryzyku portfela decyduje głównie 1225 par, a nie 50 indywidualnych zmienności. Ryzyko dużego portfela to prawie w całości współporuszanie.

## Granica efektywna: menu, nie rekomendacja

Weź teraz wszystkie możliwe podziały kapitału między dostępne aktywa i nanieś każdy z nich na płaszczyznę: ryzyko na osi poziomej, oczekiwany zwrot na pionowej. Powstaje chmura punktów. Większość jest zdominowana: istnieje inny portfel o tym samym zwrocie i mniejszym ryzyku albo o tym samym ryzyku i wyższym zwrocie. Lewa górna krawędź chmury, tam gdzie dalsza poprawa przestaje być możliwa, to granica efektywna. Jej skrajnie lewy punkt to portfel minimalnej wariancji, najspokojniejsza kombinacja, jaką da się z tych aktywów skleić.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">Granica efektywna: górna krawędź zbioru możliwych portfeli</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">oczekiwany zwrot portfela</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">ryzyko portfela (odchylenie standardowe)</text><circle cx="250" cy="150" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="300" cy="171" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="350" cy="158" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="390" cy="110" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="400" cy="185" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="440" cy="160" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="470" cy="125" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="500" cy="190" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="520" cy="150" r="2.6" fill="currentColor" opacity="0.3"/><circle cx="545" cy="105" r="2.6" fill="currentColor" opacity="0.3"/><path d="M200 160 C200 195 330 212 560 218" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.45" stroke-dasharray="4 4"/><path d="M200 160 C200 120 320 88 560 75" fill="none" stroke="#0b66c3" stroke-width="2.2"/><line x1="218" y1="137" x2="424" y2="137" stroke="currentColor" stroke-width="1" opacity="0.5" stroke-dasharray="2 4"/><circle cx="214" cy="137" r="4" fill="#0b66c3"/><circle cx="430" cy="137" r="4" fill="currentColor" opacity="0.75"/><circle cx="200" cy="160" r="4.4" fill="#0b66c3"/><text x="320" y="128" font-size="10" fill="currentColor" opacity="0.7" text-anchor="middle">ten sam zwrot, mniej ryzyka</text><text x="438" y="149" font-size="10" fill="currentColor" opacity="0.7">portfel zdominowany</text><text x="188" y="172" font-size="10" fill="currentColor" opacity="0.7" text-anchor="end">min. wariancja</text><text x="392" y="70" font-size="10.5" fill="#0b66c3">granica efektywna</text><text x="352" y="224" font-size="10" fill="currentColor" opacity="0.6">dolna gałąź: zdominowana</text></svg>
<figcaption>Każdy punkt chmury to portfel, czyli inny podział kapitału między te same aktywa. Granica efektywna (niebieska) to lewa górna krawędź zbioru: dla każdego poziomu ryzyka najwyższy osiągalny oczekiwany zwrot. Portfel zdominowany ma na granicy odpowiednik o tym samym zwrocie i mniejszym ryzyku (linia przerywana). Skrajnie lewy punkt to portfel minimalnej wariancji, a dolna gałąź jest zdominowana: to samo ryzyko co wyżej, niższy zwrot.</figcaption>
</figure>

Granica efektywna nie wskazuje jednego właściwego portfela. Jest menu: przesuwanie się w prawo po granicy kupuje wyższy oczekiwany zwrot za wyższe ryzyko i żadna matematyka nie rozstrzygnie, ile ryzyka wypada chcieć. To rozstrzyga preferencja inwestora. Teoria gwarantuje tylko tyle, że portfele spoza granicy nie mają racji bytu, bo za to samo ryzyko można było dostać więcej zwrotu.

## Uczciwe ograniczenia: gdzie ta maszyna się łamie

Wszystko powyżej jest matematycznie pewne, pod warunkiem że znasz prawdziwe oczekiwane zwroty, zmienności i korelacje. Nie znasz. I tu zaczyna się drobny druk.

Po pierwsze, wejścia są estymatami. Najbardziej niepewny element to oczekiwane zwroty: historyczna średnia jest głośnym i chwiejnym prognostykiem przyszłej stopy, a rozstrzał między metodami szacowania bywa większy niż same szacowane wielkości. Przekrojowo rozbiera to Ilmanen w "Expected Returns" (2011), książce w całości poświęconej temu, skąd w ogóle biorą się oczekiwane zwroty i czemu tak trudno je przyszpilić.

Po drugie, optymalizator działa jak wzmacniacz błędów. Procedura mean-variance traktuje estymaty jak prawdę objawioną: aktywo z zawyżonym w próbce zwrotem albo zaniżoną korelacją dostaje ogromną wagę, a małe przesunięcie wejść potrafi kompletnie przemeblować wynikowe wagi. W literaturze ukuto na to termin error maximization: optymalizator maksymalizuje nie tyle jakość portfela, ile błąd estymacji. López de Prado dokłada do tego obserwację, którą nazywa klątwą Markowitza: im silniej skorelowane są aktywa, tym bardziej dywersyfikacja jest potrzebna, ale tym gorzej uwarunkowana jest macierz korelacji i tym mniej stabilne są wagi wychodzące z jej odwracania. Maszyna psuje się najmocniej dokładnie tam, gdzie jest najbardziej potrzebna.

Po trzecie, korelacje nie są stałymi natury. Szacuje się je na danych ze spokojnych rynków, a w kryzysie rosną, bo w panice aktywa ryzykowne zaczynają chodzić razem. Dywersyfikacja zmierzona na spokojnej próbce obiecuje więc więcej ochrony, niż dostarczy w stresie. To najbardziej złośliwe ograniczenie całej ramy: darmowy obiad częściowo znika w momencie, w którym najbardziej chce się go zjeść.

Po czwarte, wariancja jako miara ryzyka jest w pełni adekwatna, gdy zwroty są mniej więcej normalne albo gdy inwestorowi naprawdę zależy wyłącznie na średniej i wariancji. Realne zwroty mają grube ogony i skosy. Dwa aktywa o identycznej wariancji mogą mieć zupełnie różne ogony, a rama mean-variance ich nie rozróżni: kara za łagodne wahania w obie strony jest taka sama jak za rzadkie, głębokie obsunięcia.

## Nowoczesna odpowiedź: portfel budowany z klastrów

Skoro najbardziej kruchym elementem jest odwracanie pełnej macierzy kowariancji, naturalny kierunek naprawy brzmi: nie odwracaj jej. Tak działa Hierarchical Risk Parity (HRP) z pracy Lópeza de Prado "Building Diversified Portfolios that Outperform Out-of-Sample" (2016). Zamiast szukać wag w jednym wielkim układzie równań, HRP buduje portfel tak, jak człowiek myśli o rynkach: najpierw grupy podobnych aktywów, potem podział kapitału między grupy, na końcu wewnątrz grup.

Technicznie to trzy kroki. Krok pierwszy: klasteryzacja hierarchiczna. Korelacje zamienia się na odległości i skleja aktywa w drzewo podobieństwa:

```
dᵢⱼ = √( (1 − ρᵢⱼ) / 2 )

ρ = +1  →  d = 0        zachowują się identycznie
ρ =  0  →  d ≈ 0.707
ρ = −1  →  d = 1        maksymalnie różne
```

Krok drugi: quasi-diagonalizacja, czyli takie poprzestawianie wierszy i kolumn macierzy, żeby podobne aktywa sąsiadowały ze sobą. Krok trzeci: rekurencyjna bisekcja. Kapitał dzieli się z góry na dół wzdłuż drzewa, na każdym rozgałęzieniu odwrotnie proporcjonalnie do wariancji gałęzi, aż do pojedynczych aktywów.

W żadnym kroku nie odwraca się pełnej macierzy. Dzięki temu HRP działa także wtedy, gdy macierz jest źle uwarunkowana albo wręcz osobliwa, na przykład gdy aktywów jest więcej niż obserwacji, czyli dokładnie tam, gdzie klasyczny optymalizator wybucha. W eksperymentach Monte Carlo z tej samej pracy portfele HRP miały niższą wariancję out-of-sample niż portfele z klasycznej optymalizacji minimalnej wariancji. Wynik jest złośliwie ironiczny: optymalizator przegrał we własnej konkurencji, bo minimalizował wariancję na estymatach, a HRP, mniej dopasowane do próbki, okazało się odporniejsze na jej błędy. To ta sama lekcja co wszędzie w quant: mniej dopasowania in-sample, więcej przeżywalności out-of-sample.

## Co z tego zostaje

Trwałe jądro Markowitza ma się dobrze po ponad siedemdziesięciu latach: myśl portfelowo, oceniaj każdą pozycję przez wkład do całości, szanuj korelacje bardziej niż indywidualne zmienności. Darmowy obiad jest prawdziwy w jedynym sensie, w jakim matematyka umie coś obiecać: przy korelacji poniżej jedności redukcja ryzyka bez utraty oczekiwanego zwrotu wynika z wzoru, nie z opinii.

Krucha jest natomiast skorupa, czyli przekonanie, że z historycznych estymat da się wycisnąć optymalne wagi z czterema miejscami po przecinku. Praktyczna hierarchia wygląda więc tak. Najpierw być zdywersyfikowanym w ogóle, między rzeczy, które naprawdę jeżdżą na różnych czynnikach. Potem ważyć prosto i stabilnie, na przykład klastrami, zamiast ufać wagom z odwracanej macierzy. I zawsze zakładać, że korelacje w stresie będą wyższe niż w próbce, na której je policzono. Wtedy z teorii portfela zostaje dokładnie to, co w niej najlepsze: rama do myślenia o ryzyku, a nie automat do produkowania pewności.

To nie jest porada inwestycyjna. To edukacyjne omówienie teorii portfela: wzory są pewne, estymaty wejść nigdy, i właśnie o tej różnicy jest sekcja o ograniczeniach.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
