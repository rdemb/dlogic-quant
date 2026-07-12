---
title: "Łańcuchy Markowa i ukryte modele Markowa: matematyka reżimów"
description: "Własność Markowa mówi, że przyszłość zależy od stanu obecnego, a nie od całej historii. Na tym stoi macierz przejść i rozkład stacjonarny: w przykładzie stanu spokojnego i burzliwego długoterminowy udział czasu wychodzi dwie trzecie do jednej trzeciej. Ukryty model Markowa dokłada obserwacje i macierz emisji, a Rabiner (1989) porządkuje go w trzy problemy: forward, Viterbi i Baum-Welch. Kontekst reżimów, nie prognoza kierunku. Źródła: Rabiner (1989), Hamilton (1989), Baum i Welch (1970)."
date: 2026-07-11 16:00:00 +0200
eyebrow: "Edukacja · matematyka"
dek: "Reżim rynku, opisany wcześniej jako filtr nadrzędny, ma pod spodem konkretną matematykę: łańcuch Markowa, macierz przejść i rozkład stacjonarny, a nad nim ukryty model Markowa z macierzą emisji. Ten tekst otwiera tę skrzynkę pojęciowo, od własności Markowa po trzy algorytmy i granice metody."
readingTime: 7
tags: [matematyka, "łańcuchy Markowa", HMM, "ukryte modele Markowa", reżimy, Viterbi, "Baum-Welch", Rabiner, Hamilton, "macierz przejść", "rozkład stacjonarny", zmienność, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Własność Markowa to skrócona pamięć: rozkład następnego stanu zależy wyłącznie od stanu obecnego, a nie od całej wcześniejszej trasy. To założenie modelujące, nie prawo natury, i właśnie ono czyni cały aparat obliczalnym.
> - Skończony łańcuch Markowa streszcza się macierzą przejść (prawdopodobieństwa zmiany stanu) i rozkładem stacjonarnym (długoterminowy udział czasu w każdym stanie). W przykładzie dwóch stanów, spokojnego i burzliwego, przy prawdopodobieństwach pozostania 0,90 i 0,80 rozkład stacjonarny wychodzi dwie trzecie do jednej trzeciej, a stan spokojny trwa średnio dziesięć kroków wobec pięciu dla burzliwego. To formalny odpowiednik lepkości reżimu.
> - Ukryty model Markowa dokłada warstwę: stanu nie widać wprost, widać tylko obserwacje (zwroty, zmienność), a łączy je macierz emisji, czyli rozkład obserwacji przypisany każdemu stanowi. Pojedynczy duży ruch nie dowodzi burzy, jest w niej tylko bardziej prawdopodobny, więc stan trzeba wywnioskować z zaszumionego strumienia.
> - Rabiner (1989) porządkuje HMM w trzy problemy: ocenę prawdopodobieństwa danych (algorytm forward), znalezienie najlepszej ścieżki stanów (Viterbi) i uczenie parametrów z danych (Baum-Welch, odmiana EM). Do ekonomii wniósł tę konstrukcję Hamilton (1989) jako przełączanie reżimów Markowa. To narzędzie opisu środowiska i jego trwałości, nie prognoza kierunku ani przewaga.

**Teza w jednym zdaniu:** Łańcuch Markowa opisuje reżim jako stan, w którym przyszłość zależy tylko od teraźniejszości i który da się streścić macierzą przejść oraz rozkładem stacjonarnym, a ukryty model Markowa dokłada do tego obserwacje i macierz emisji, przez co staje się matematycznym zapleczem rozpoznawania reżimu: opisuje strukturę środowiska, nie przewiduje kierunku.

## Własność Markowa: pamięć skrócona do teraźniejszości

Punktem wyjścia jest jedno założenie o pamięci procesu. Proces losowy ma własność Markowa, jeśli rozkład następnego stanu zależy od przeszłości wyłącznie przez stan obecny. Cała wcześniejsza trasa, sposób, w jaki proces doszedł do bieżącego stanu, nie wnosi już nic ponad to, co mówi sam ten stan.

```
własność Markowa:
P(s_{t+1} | s_t, s_{t-1}, ..., s_0) = P(s_{t+1} | s_t)

przyszłość zależy od przeszłości tylko przez stan obecny
```

To jest założenie modelujące, nie prawo natury. Bywa fałszywe, gdy proces ma dłuższą pamięć, ale dla reżimu jest zaskakująco rozsądne: jeśli wiadomo, że rynek jest teraz w stanie spokojnym, dodatkowa wiedza o tym, co działo się pół roku temu, mało zmienia szansę stanu jutro. Ceną za to założenie jest ogromne uproszczenie rachunku, bo cały opis dynamiki mieści się w prawdopodobieństwach przejść między stanami.

## Macierz przejść i rozkład stacjonarny

Gdy stanów jest skończenie wiele, dynamikę łańcucha zapisuje jedna tabela: macierz przejść. Jej element w wierszu i oraz kolumnie j to prawdopodobieństwo, że stan zmieni się z i na j w jednym kroku. Każdy wiersz sumuje się do jedności, bo z danego stanu trzeba gdzieś przejść. Prosty przykład z dwoma stanami, spokojnym i burzliwym, wystarcza do całej intuicji.

```
macierz przejść A   (wiersz = stan dziś, kolumna = stan jutro)

            spokój   burza
spokój       0.90    0.10
burza        0.20    0.80

każdy wiersz sumuje się do 1
```

Wysokie wartości na przekątnej oznaczają lepkość: rynek najczęściej zostaje tam, gdzie jest. Ze stanu spokojnego zostaje w nim z prawdopodobieństwem 0,90, ze stanu burzliwego z prawdopodobieństwem 0,80. Średni czas trwania stanu to odwrotność prawdopodobieństwa wyjścia, więc epizod spokoju trwa średnio dziesięć kroków, a epizod burzy pięć.

Osobne pytanie brzmi, jaka część czasu przypada na każdy stan w długim biegu, niezależnie od tego, gdzie łańcuch wystartował. Odpowiada na nie rozkład stacjonarny: taki rozkład prawdopodobieństwa po stanach, który po przemnożeniu przez macierz przejść nie zmienia się. To klimat łańcucha, a nie jego pogoda z danego dnia.

```
rozkład stacjonarny π:  π = π · A,   suma π = 1

π(spokój) = 2/3 ≈ 0.667
π(burza)  = 1/3 ≈ 0.333

średni czas w stanie = 1 / (prawdopodobieństwo wyjścia)
spokój: 1 / 0.10 = 10 kroków
burza:  1 / 0.20 = 5 kroków
```

W tym przykładzie stan spokojny dominuje w proporcji dwa do jednego i trwa dwa razy dłużej. To jest formalny odpowiednik zdania, że reżimy są lepkie, które w [tekście o rozpoznawaniu reżimu rynku](/dlogic-quant/2026/07/09/jak-rozpoznac-rezim-rynku/) pojawiło się jako warunek użyteczności całej metody. Gdyby przekątna macierzy przejść była niska, stany migotałyby z kroku na krok i ich wykrywanie nie miałoby sensu, bo zanim dałoby się je rozpoznać, już by ich nie było.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="mkA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M1 1.5 L9 5 L1 8.5 z" fill="currentColor" fill-opacity="0.75"/></marker>
</defs>
<text x="320" y="26" text-anchor="middle" font-size="13.5" fill="currentColor" fill-opacity="0.85">Dwustanowy łańcuch Markowa: spokój i burza</text>
<circle cx="168" cy="176" r="64" fill="#1a9e6a" fill-opacity="0.12" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.3"/>
<text x="168" y="172" text-anchor="middle" font-size="16" font-weight="600" fill="currentColor">Spokój</text>
<text x="168" y="192" text-anchor="middle" font-size="9.5" fill="currentColor" fill-opacity="0.6">niska zmienność</text>
<circle cx="472" cy="176" r="64" fill="#e5484d" fill-opacity="0.13" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.3"/>
<text x="472" y="172" text-anchor="middle" font-size="16" font-weight="600" fill="currentColor">Burza</text>
<text x="472" y="192" text-anchor="middle" font-size="9.5" fill="currentColor" fill-opacity="0.6">wysoka zmienność</text>
<path d="M144 116 C 118 58, 218 58, 192 116" fill="none" stroke="currentColor" stroke-opacity="0.75" stroke-width="1.7" marker-end="url(#mkA)"/>
<text x="168" y="50" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.8">0.90</text>
<path d="M448 116 C 422 58, 522 58, 496 116" fill="none" stroke="currentColor" stroke-opacity="0.75" stroke-width="1.7" marker-end="url(#mkA)"/>
<text x="472" y="50" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.8">0.80</text>
<path d="M228 150 C 282 108, 358 108, 412 150" fill="none" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.7" marker-end="url(#mkA)"/>
<text x="320" y="102" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.8">0.10</text>
<path d="M412 202 C 358 248, 282 248, 228 202" fill="none" stroke="currentColor" stroke-opacity="0.7" stroke-width="1.7" marker-end="url(#mkA)"/>
<text x="320" y="260" text-anchor="middle" font-size="11" fill="currentColor" fill-opacity="0.8">0.20</text>
</svg>
<figcaption>Dwustanowy łańcuch Markowa. Pętle zwrotne to prawdopodobieństwa pozostania w stanie (0.90 dla spokoju, 0.80 dla burzy), a łuki między węzłami to prawdopodobieństwa przejść (0.10 i 0.20). Każdy wiersz macierzy przejść sumuje się do jedności. Wysokie wartości na pętlach oznaczają lepkość: stan spokojny trwa średnio dziesięć kroków, burzliwy pięć, a rozkład stacjonarny wychodzi dwie trzecie do jednej trzeciej.</figcaption>
</figure>

## Ukryty model Markowa: stan, którego nie widać

Łańcuch z poprzedniego przykładu zakłada, że stan jest widoczny. Na rynku tak nie jest. Nikt nie wypisuje na taśmie etykiety spokój ani burza, widać tylko zwroty i zmienność zrealizowaną. Ukryty model Markowa (HMM) bierze to na wprost: stan `s_t` jest ukryty i zmienia się jak łańcuch Markowa według macierzy przejść, a każdy stan emituje obserwacje losowane z własnego rozkładu.

```
ukryty model Markowa   λ = (A, B, π₀)

stan ukryty:  s_t ∈ {spokój, burza}      nie jest obserwowany
przejścia:    A[i,j] = P(s_t=j | s_{t-1}=i)     macierz przejść
emisje:       B[i,k] = P(o_t=k | s_t=i)         macierz emisji
start:        π₀ = rozkład stanu na początku
```

Nowym elementem jest macierz emisji: dla każdego stanu rozkład tego, co widać. Jeśli obserwacją jest zgrubny podział ruchu na mały i duży, macierz emisji może wyglądać tak.

```
macierz emisji B     mały ruch   duży ruch
spokój                0.85        0.15
burza                 0.40        0.60

wiersze sumują się do 1
```

Sedno jest w tym, że jeden duży ruch nie dowodzi burzy. Jest w burzy bardziej prawdopodobny (0,60 wobec 0,15), ale zdarza się i w spokoju. Stanu nie da się odczytać wprost, trzeba go wywnioskować z całego zaszumionego strumienia obserwacji. Macierz emisji jest właśnie mostem między tym, co mierzalne (ruchy, zmienność), a tym, co interesujące (reżim). Ta sama konstrukcja stała za opisem HMM w tekście o reżimach, tutaj rozłożona na części: łańcuch pod spodem, obserwacje nad nim i macierz emisji, która je łączy.

## Trzy problemy HMM

Rabiner (1989) w klasycznym wykładzie HMM, pierwotnie dla rozpoznawania mowy, uporządkował całą maszynerię w trzy problemy. Każdy odpowiada na inne pytanie i ma własny algorytm.

```
1. Ocena        P(obserwacje | λ)               algorytm forward
2. Dekodowanie  najlepsza ścieżka stanów        Viterbi
3. Uczenie      estymacja A, B, π₀ z danych      Baum-Welch (EM)
```

Ocena pyta, jak prawdopodobny jest zaobserwowany ciąg przy danym modelu. Liczenie tego wprost wymagałoby zsumowania prawdopodobieństwa po wszystkich możliwych ścieżkach stanów, a tych dla T kroków i K stanów jest K do potęgi T, czyli astronomicznie wiele. Algorytm forward zwija tę sumę do tabeli metodą programowania dynamicznego: przenosi z kroku na krok prawdopodobieństwo obserwacji dotychczasowych wraz z bieżącym stanem i aktualizuje je jedną rekurencją.

```
forward:  α_t(i) = P(o_1..o_t, s_t=i | λ)
α_t(j) = [ Σ_i α_{t-1}(i)·A[i,j] ] · B[j, o_t]
P(obserwacje | λ) = Σ_i α_T(i)

koszt: rzędu K²·T zamiast K^T
```

Ten sam mechanizm, znormalizowany do jedynki w każdej chwili, daje prawdopodobieństwo filtrowane, czyli szansę każdego stanu przy danych dostępnych do tej chwili. To jest wersja używana do odczytu reżimu na żywo, bo korzysta wyłącznie z przeszłości.

Dekodowanie pyta o najbardziej prawdopodobną ścieżkę stanów, która tłumaczy obserwacje. Algorytm Viterbiego ma tę samą postać co forward, tylko zastępuje sumowanie maksimum i zapamiętuje wskaźniki wstecz, żeby po przejściu całego ciągu odtworzyć jedną, najlepszą sekwencję ukrytych stanów. To narzędzie do etykietowania historii: które okresy były spokojne, a które burzliwe.

Uczenie odpowiada na pytanie, skąd biorą się macierze A i B. Baum, Welch i współpracownicy (1970) podali algorytm, który estymuje je z samych obserwacji, bez etykiet stanów. Jest to odmiana EM (expectation-maximization): zgaduje parametry, liczy oczekiwane obłożenie stanów i oczekiwane przejścia, po czym przelicza z nich parametry i powtarza. Każda iteracja nie może zmniejszyć prawdopodobieństwa danych, więc proces zbiega, ale tylko do optimum lokalnego, stąd wrażliwość na punkt startowy.

## Zastosowanie: reżimy zmienności

Do ekonomii i finansów tę konstrukcję wniósł Hamilton (1989) jako przełączanie reżimów Markowa: autoregresja, której parametry, w tym średnia i wariancja, przełączają się wraz z ukrytym stanem Markowa. Pierwotnie posłużyła do modelowania faz wzrostu i recesji w danych o produkcie. Finansowe odczytanie jest bezpośrednie: od dwóch do trzech stanów, na przykład spokój, trend i turbulencja, każdy z własną średnią i wariancją, plus macierz przejść kodująca trwałość.

Grupowanie się zmienności wynika z tej struktury samo. Stan o wysokiej wariancji, który jest lepki, produkuje serie dużych ruchów, dokładnie te stada zmienności, o których była mowa przy okazji reżimów. Odczytem na żywo jest prawdopodobieństwo filtrowane stanu przy danych do bieżącej chwili. Tekst o rozpoznawaniu reżimu rynku porównywał narzędzia na poziomie który wybrać (GARCH, GMM, HMM, wykrywanie punktów zmiany); tutaj otwarta jest maszynownia jednego z nich, żeby widać było, że pod etykietą stanu siedzi zwykły łańcuch Markowa z macierzą emisji.

## Granice metody

Ta sama matematyka, która czyni HMM eleganckim, wyznacza jego granice. Cztery są istotne i żadna nie znika przez staranniejsze dopasowanie.

Liczba stanów jest wyborem, nie odkryciem. K ustala człowiek. Za mało stanów gubi strukturę, za dużo tnie szum na pseudoreżimy bez odpowiednika w rzeczywistości. W praktyce zostaje zwykle od dwóch do czterech, a kryteria informacyjne pomagają wybrać, lecz nie usuwają arbitralności.

Ryzyko dopasowania i podglądanie przyszłości. Dopasowanie modelu na całej próbie, a potem etykietowanie historii estymatą wygładzoną, używa danych z przyszłości do orzekania o przeszłości. Powstaje piękna mapa in-sample, która na żywo się nie powtarza. Do czegokolwiek, co dotyka decyzji, parametry muszą być ustalone na przeszłości, a stan musi być prawdopodobieństwem filtrowanym, liczonym przyczynowo.

Opóźnienie detekcji. Żeby rozpoznać zmianę stanu, model potrzebuje danych, więc estymata jest najbardziej niepewna dokładnie w chwili zwrotu. Potwierdzenie kosztuje pierwszą część ruchu. To koszt strukturalny, nie błąd do naprawienia.

Założenia są uproszczeniem. Własność Markowa (skrócona pamięć), stałe rozkłady emisji w obrębie stanu i niezmienna macierz przejść to idealizacje. Prawdziwe rynki miewają dłuższą pamięć i pełzające parametry, a rozkłady normalne w emisjach zaniżają grube ogony. Model jest użyteczną soczewką, nie prawem.

Dlatego łańcuch Markowa i jego ukryta wersja są przede wszystkim językiem: pozwalają opisać reżim jako stan o określonej trwałości i powiedzieć, w jakiej grze rynek prawdopodobnie się znajduje. Nie mówią, w którą stronę pójdzie cena, i nie są przewagą. To samo rozróżnienie, które niosła całość rozważań o reżimach: opis środowiska, nie prognoza kierunku.

Materiał czysto edukacyjny, nie porada inwestycyjna. Liczby w przykładach (macierze przejść i emisji, rozkład stacjonarny) są ilustracyjne i służą pokazaniu mechaniki, nie opisują żadnego konkretnego rynku. Pewna jest tu wyłącznie matematyka: własność Markowa, rachunek na macierzy przejść i trójka algorytmów forward, Viterbi oraz Baum-Welch.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
