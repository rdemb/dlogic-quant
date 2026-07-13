---
title: "Opcje od zera. Prawo, nie obowiązek"
description: "Opcja daje prawo, nie obowiązek: call to prawo kupna, put to prawo sprzedaży instrumentu po ustalonej cenie do ustalonego terminu. Kupujący ryzykuje tylko premię, wystawca przyjmuje obowiązek, a niepokryty wystawca call ma stratę bez górnego ograniczenia. Cena opcji dzieli się na wartość wewnętrzną i czasową, której paliwem są czas i zmienność, spójności cen pilnuje parytet put-call, a praktyczne zastosowania to ubezpieczenie portfela, dochód z pokrytych calli i spekulacja ze z góry znanym ryzykiem. Podstawy według Hulla, Natenberga i OIC."
date: 2026-07-05 13:00:00 +0200
eyebrow: "Edukacja · instrumenty"
dek: "Call daje prawo kupna, put prawo sprzedaży, a kupujący ryzykuje najwyżej premię, podczas gdy wystawca przyjmuje obowiązek. Do tego wartość wewnętrzna i czasowa, moneyness po ludzku, parytet put-call jako fundament spójności cen oraz trzy uczciwe zastosowania opcji: ubezpieczenie, dochód i spekulacja z ograniczonym ryzykiem. Podstawy, bez wyceny i greckich, które przyjdą osobno."
readingTime: 8
tags: ["opcje", call, put, "premia opcyjna", "wartość wewnętrzna", "wartość czasowa", moneyness, ITM, ATM, OTM, "parytet put-call", "profil wypłaty", hedging, "protective put", "covered call", Hull, Natenberg, OIC, edukacja, quant]
category: edukacja
---

> **W skrócie**
>
> - Opcja to prawo, nie obowiązek. Call daje prawo kupna, put daje prawo sprzedaży instrumentu po ustalonej cenie wykonania, najpóźniej do ustalonego terminu. Kupujący płaci premię i tylko premią ryzykuje. Wystawca inkasuje premię i w zamian przyjmuje obowiązek.
> - Tę asymetrię widać w profilach wypłat: strata kupującego jest ścięta na poziomie premii, zysk wystawcy jest ścięty na poziomie premii, a strata wystawcy niepokrytego call jest teoretycznie nieograniczona, bo cena instrumentu nie ma sufitu.
> - Cena opcji składa się z wartości wewnętrznej i czasowej. Opcja poza pieniądzem ma wyłącznie wartość czasową, a jej paliwem są czas do wygaśnięcia i zmienność. Spójności cen call i put pilnuje parytet put-call: C − P = S − K·e^(−rT).
> - W praktyce opcje służą do trzech rzeczy: ubezpieczenia portfela (put ochronny), generowania dochodu (pokryty call) i spekulacji ze z góry znanym ryzykiem. Kupowanie groszowych opcji głęboko poza pieniądzem działa jak los na loterię: niska cena jest wyceną niskiego prawdopodobieństwa, nie okazją.

**Teza w jednym zdaniu:** Opcja rozdziela ryzyko asymetrycznie, bo kupujący nabywa prawo i może stracić najwyżej premię, a wystawca przyjmuje obowiązek i za tę premię bierze na siebie resztę rozkładu, przy czym cena prawa to wartość wewnętrzna plus czasowa, którą karmią czas i zmienność, a wzajemną spójność cen call i put wymusza parytet put-call.

## Prawo, nie obowiązek: co właściwie kupuje posiadacz opcji

W ujęciu z podręcznika referencyjnego rynków pochodnych, czyli „Options, Futures, and Other Derivatives" Johna Hulla, opcja daje posiadaczowi prawo, ale nie obowiązek, kupna lub sprzedaży instrumentu bazowego po ustalonej z góry cenie wykonania, najpóźniej do ustalonego terminu wygaśnięcia. Za to prawo płaci się z góry cenę zwaną premią. Instrumentem bazowym może być akcja, indeks, waluta, surowiec albo kontrakt terminowy; mechanika jest ta sama.

```
call   = prawo KUPNA instrumentu po cenie wykonania K, do terminu T
put    = prawo SPRZEDAŻY instrumentu po cenie wykonania K, do terminu T
premia = cena tego prawa, płacona z góry wystawcy opcji

opcja europejska  = wykonanie możliwe tylko w dniu wygaśnięcia
opcja amerykańska = wykonanie możliwe w każdej chwili do wygaśnięcia
```

Sednem konstrukcji jest asymetria. Kupujący może z prawa skorzystać, jeżeli mu się to opłaca, albo pozwolić opcji wygasnąć, jeżeli się nie opłaca. Jego najgorszy scenariusz jest znany w chwili zakupu: strata całej premii i ani grosza więcej. Wystawca opcji stoi po drugiej stronie tej samej umowy. Premię dostaje od razu, ale w zamian przyjmuje obowiązek: jeżeli posiadacz call zażąda kupna, wystawca musi sprzedać po K; jeżeli posiadacz put zażąda sprzedaży, wystawca musi kupić po K. Prawo i obowiązek to dwie strony tej samej monety, a premia jest ceną, po której obowiązek przechodzi z jednej kieszeni do drugiej.

## Cztery pozycje podstawowe i ich profile wypłat

Z dwóch typów opcji i dwóch stron transakcji powstają cztery pozycje elementarne. Poniżej ich wyniki w dniu wygaśnięcia: pionowo wynik pozycji, poziomo cena instrumentu S, K to cena wykonania, p to zapłacona lub otrzymana premia. Wykresy są poglądowe.

```
LONG CALL (kupiony call)             wynik = max(S − K, 0) − p
   |                  /
   |                 /
 0 +-------------K--/----------->  S
   |               /
−p |______________/
    strata: najwyżej p, zysk: bez górnego ograniczenia
    próg rentowności: K + p

LONG PUT (kupiony put)               wynik = max(K − S, 0) − p
   |        \
   |         \
 0 +----------\--K------------->  S
   |           \
−p |            \_______________
    strata: najwyżej p, zysk: duży, maksimum K − p przy S = 0
    próg rentowności: K − p

SHORT CALL (wystawiony call)         wynik = p − max(S − K, 0)
+p |______________\
   |               \
 0 +-------------K--\----------->  S
   |                 \
   |                  \
    zysk: najwyżej p, strata: BEZ OGRANICZEŃ przy niepokrytym call
    (cena instrumentu nie ma sufitu)

SHORT PUT (wystawiony put)           wynik = p − max(K − S, 0)
+p |            /_______________
   |           /
 0 +----------/--K------------->  S
   |         /
   |        /
    zysk: najwyżej p, strata: duża, maksimum K − p przy S = 0
```

Z tych profili trzeba zapamiętać dwie rzeczy. Po pierwsze, kupujący ma stratę ściętą do premii, a zysk otwarty (call) albo bardzo duży (put); wystawca odwrotnie: zysk ścięty do premii, strata otwarta lub bardzo duża. Po drugie, niepokryty short call jest jedyną z czterech pozycji o teoretycznie nieograniczonej stracie, bo instrument może rosnąć bez końca, a wystawca ma obowiązek sprzedać po K niezależnie od tego, jak wysoko cena zaszła. Short put ma stratę wielką, ale ograniczoną, bo cena nie spada poniżej zera. Dlatego materiały edukacyjne OIC i podręcznik Hulla traktują wystawianie gołych calli jako pozycję o najbardziej niewygodnym profilu ryzyka, u brokerów zwykle obwarowaną najwyższymi wymogami depozytowymi.

Przykład ilustracyjny, liczby umowne. Call z ceną wykonania K = 100 kupiony za premię p = 3: przy cenie 105 w dniu wygaśnięcia wynik to 105 − 100 − 3 = +2. Przy cenie 99 opcja wygasa bezwartościowo i strata wynosi całe 3, mimo że do ceny wykonania zabrakło niewiele. Próg rentowności leży na K + p = 103: sam wzrost ceny nie wystarczy, ruch musi jeszcze pokryć premię.

<figure>
<svg viewBox="0 0 660 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Profil wypłaty długiej opcji CALL i długiej opcji PUT w terminie wygaśnięcia" font-family="-apple-system,Segoe UI,Roboto,sans-serif">
<title>Profil wypłaty opcji w terminie wygaśnięcia</title>
<g font-size="13" fill="currentColor">
<rect x="70" y="13" width="22" height="3.5" rx="1.5" fill="#1a9e6a"/>
<text x="99" y="21">długi CALL (prawo kupna)</text>
<rect x="300" y="13" width="22" height="3.5" rx="1.5" fill="#e5484d"/>
<text x="329" y="21">długi PUT (prawo sprzedaży)</text>
</g>
<line x1="66" y1="180" x2="636" y2="180" stroke="currentColor" stroke-width="1.5" opacity="0.5"/>
<path d="M636 180 l-9 -4.5 v9 z" fill="currentColor" opacity="0.5"/>
<line x1="70" y1="272" x2="70" y2="44" stroke="currentColor" stroke-width="1.5" opacity="0.5"/>
<path d="M70 44 l-4.5 9 h9 z" fill="currentColor" opacity="0.5"/>
<line x1="330" y1="58" x2="330" y2="254" stroke="currentColor" stroke-width="1.25" stroke-dasharray="5 4" opacity="0.7"/>
<g fill="currentColor" opacity="0.75" font-size="12.5">
<text x="60" y="184" text-anchor="end">0</text>
<text x="60" y="245" text-anchor="end">&#8722;p</text>
<text x="324" y="200" text-anchor="end">K</text>
<text x="352" y="300" text-anchor="middle">cena instrumentu bazowego S  &#8594;</text>
</g>
<text transform="translate(26 205) rotate(-90)" text-anchor="middle" fill="currentColor" opacity="0.75" font-size="12.5">wynik pozycji</text>
<g opacity="0.6">
<circle cx="270" cy="180" r="3" fill="none" stroke="currentColor" stroke-width="1.25"/>
<circle cx="390" cy="180" r="3" fill="none" stroke="currentColor" stroke-width="1.25"/>
<text x="262" y="197" text-anchor="end" fill="currentColor" font-size="11">K&#8722;p</text>
<text x="398" y="197" text-anchor="start" fill="currentColor" font-size="11">K+p</text>
</g>
<path d="M70 240 H330 L520 50" fill="none" stroke="#1a9e6a" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M140 50 L330 240 H620" fill="none" stroke="#e5484d" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="120" y1="240" x2="120" y2="258" stroke="currentColor" stroke-dasharray="2 3" stroke-width="1" opacity="0.45"/>
<text x="96" y="270" fill="currentColor" opacity="0.85" font-size="12">premia p = maksymalna strata kupującego</text>
</svg>
<figcaption>Profil wypłaty w terminie wygaśnięcia dla długiej pozycji CALL i długiej pozycji PUT. Zysk kupującego otwiera się po właściwej stronie ceny wykonania K, a strata jest ścięta do zapłaconej premii p niezależnie od skali niekorzystnego ruchu.</figcaption>
</figure>

## Wartość wewnętrzna i czasowa: z czego składa się premia

Cena opcji rozkłada się na dwa składniki, które warto umieć rozdzielić w pamięci za każdym razem, gdy patrzy się na kwotowanie.

```
wartość wewnętrzna call = max(S − K, 0)
wartość wewnętrzna put  = max(K − S, 0)

premia = wartość wewnętrzna + wartość czasowa
```

Wartość wewnętrzna to część premii, którą dałoby się zrealizować od ręki, gdyby opcję wykonać natychmiast: call z prawem kupna po 100 przy cenie rynkowej 105 ma pięć jednostek wartości wewnętrznej. Wartość czasowa to cała reszta premii: zapłata za możliwość, że do terminu wygaśnięcia sytuacja zrobi się jeszcze lepsza. Opcja poza pieniądzem ma wartość wewnętrzną równą zeru, więc cała jej cena to wartość czasowa, czyli czysty zakład o przyszłość.

Paliwem wartości czasowej są dwie rzeczy: czas i zmienność. To centralny wątek książki Sheldona Natenberga „Option Volatility and Pricing": im więcej czasu do wygaśnięcia i im bardziej rozedrgany instrument, tym większa szansa, że opcja wskoczy w pieniądz, więc tym więcej to prawo jest warte. Z upływem czasu wartość czasowa topnieje, coraz szybciej w miarę zbliżania się terminu, aż w dniu wygaśnięcia zostaje sama wartość wewnętrzna. Największą wartość czasową mają opcje przy pieniądzu, bo tam niepewność rozstrzygnięcia jest największa; głęboko w pieniądzu i głęboko poza pieniądzem finał jest w dużej mierze przesądzony, więc za niepewność płaci się mniej.

## Moneyness po ludzku: ITM, ATM, OTM

Moneyness opisuje, gdzie cena wykonania leży względem bieżącej ceny instrumentu. Terminologia jest angielska i warto ją znać, bo występuje w każdym łańcuchu opcyjnym.

```
                          call (prawo kupna)    put (prawo sprzedaży)
ITM  (in the money,       S > K                 S < K
     w pieniądzu)
ATM  (at the money,       S ≈ K                 S ≈ K
     przy pieniądzu)
OTM  (out of the money,   S < K                 S > K
     poza pieniądzem)
```

Po ludzku: opcja ITM to taka, której wykonanie już dziś miałoby sens, więc ma dodatnią wartość wewnętrzną i jest relatywnie droga. Opcja ATM ma cenę wykonania mniej więcej równą bieżącej cenie rynkowej i jest polem największej niepewności. Opcja OTM to prawo, z którego dziś nikt by nie skorzystał: jej cała cena to wartość czasowa, nadzieja na ruch. Im głębiej poza pieniądzem, tym opcja tańsza i tym mniejsze prawdopodobieństwo, że kiedykolwiek nabierze wartości wewnętrznej.

## Parytet put-call: fundament spójności cen

Ceny call i put o tej samej cenie wykonania i tym samym terminie nie żyją osobno. Dla opcji europejskich na aktywo niepłacące dywidendy wiąże je relacja znana jako parytet put-call, wyprowadzona u Hulla z czystego argumentu arbitrażowego.

```
C − P = S − K·e^(−rT)

C = cena call, P = cena put (ta sama cena wykonania K i termin T)
S = bieżąca cena instrumentu
r = stopa wolna od ryzyka, T = czas do wygaśnięcia
K·e^(−rT) = wartość bieżąca ceny wykonania (K zdyskontowane na dziś)
```

Intuicja jest następująca. Portfel złożony z kupionego call i wystawionego put (K i T identyczne) kończy się w terminie zawsze kupnem instrumentu po K. Jeżeli cena jest powyżej K, wykonuje się call i kupuje po K; jeżeli poniżej, put zostaje wykonany przeciwko portfelowi i też kupuje się po K. Skoro pakiet call minus put w każdym scenariuszu daje to samo co umowa kupna po K w przyszłości, to replikuje kontrakt forward, a jego dzisiejsza cena musi być równa różnicy między bieżącą ceną instrumentu a wartością bieżącą K. Gdyby rynek kwotował call i put niezgodnie z tą relacją, dałoby się złożyć pakiet bez ryzyka i z zyskiem, a arbitrażyści domknęliby lukę. Dla aktywów płacących dywidendę i dla walut wzór dostaje odpowiednie korekty, ale sens pozostaje ten sam: cena call, cena put i cena instrumentu bazowego są sztywno spięte. Nie istnieje osobna „drożyzna w callach" i osobna „tanizna w putach" na tym samym strike'u; wycena jednej nogi determinuje drugą.

## Po co komu opcje: ubezpieczenie, dochód i ryzyko znane z góry

Trzy klasyczne zastosowania, wszystkie opisane w darmowych materiałach edukacyjnych OIC (Options Industry Council) i w podręczniku Hulla.

Ubezpieczenie portfela, czyli put ochronny. Kupno put na posiadane aktywo działa jak polisa: premia jest składką, a cena wykonania poziomem, od którego szkody pokrywa druga strona. Wartość pozycji w terminie nie spadnie poniżej K pomniejszonego o zapłaconą premię, niezależnie od tego, jak głęboko rynek zanurkuje. Różnica między bieżącą ceną a K pełni rolę udziału własnego: im niższy strike, tym tańsza polisa i tym większa część pierwszej straty zostaje po stronie ubezpieczonego.

Dochód, czyli pokryty call (covered call). Posiadając instrument, wystawia się call z ceną wykonania powyżej bieżącej ceny: premia wpada od razu, a w zamian oddaje się zyski powyżej K. To zamiana części potencjału wzrostu na gotówkę tu i teraz. Pozycja jest pokryta, bo w razie wykonania opcji instrument jest pod ręką i scenariusz nieograniczonej straty wystawcy znika; zostaje koszt utraconych korzyści, gdy rynek ucieknie wysoko ponad strike.

Spekulacja z ograniczonym ryzykiem. Kupno call lub put zamiast pozycji z dźwignią daje ekspozycję kierunkową, w której najgorszy scenariusz jest znany co do grosza w momencie wejścia: to zapłacona premia. Pozycja liniowa z dźwignią może wyrzucić z rynku w połowie ruchu; kupiona opcja nie ma wezwania do uzupełnienia depozytu. Cena tej wygody jest jednak realna: premia zawiera wartość czasową, więc ruch musi być odpowiednio duży i przyjść odpowiednio szybko, inaczej racja co do kierunku nie wystarczy.

## Los na loterię: pułapka tanich opcji OTM

Najczęstsze nieporozumienie początkującego wygląda tak: opcja głęboko poza pieniądzem kosztuje grosze, a potrafi urosnąć wielokrotnie, więc wygląda na tanią okazję o ogromnym potencjale. Sęk w tym, że niska cena nie jest rabatem, tylko wyceną prawdopodobieństwa. Rynek kwotuje takie opcje tanio dokładnie dlatego, że rzadko kończą w pieniądzu. Rozkład wyników kupującego przypomina rozkład losu na loterię: bardzo częste straty całej premii i rzadkie, spektakularne wygrane, które napędzają anegdoty i przyciągają następnych kupujących. Do tego dochodzi arytmetyka progu rentowności: żeby call OTM zarobił w terminie, cena musi najpierw dojść do K, a potem jeszcze pokryć premię. Można mieć rację co do kierunku i mimo to stracić wszystko, bo ruch był za mały albo przyszedł za późno, a wartość czasowa przez cały ten czas topniała. Natenberg formułuje właściwe pytanie wprost: nie „czy opcja jest tania", tylko „czy jest tania względem prawdopodobieństw, które wycenia". Groszowa cena opcji głęboko OTM jest zwykle po prostu adekwatna do groszowej szansy.

## Co dalej: wycena i greckie

Skąd dokładnie bierze się wartość czasowa, jak przeliczyć zmienność na cenę opcji i dlaczego opcja przy pieniądzu traci na czasie najszybciej, to już temat modelu Blacka-Scholesa i tak zwanych greckich: delty, gammy, thety i vegi, czyli miar wrażliwości ceny opcji na ruch instrumentu, upływ czasu i zmiany zmienności. To materiał na osobny artykuł. Ten kończy się na fundamencie, bez którego tamten nie ma sensu: opcja to prawo, nie obowiązek, kupujący ryzykuje premię, a wystawca przyjmuje obowiązek, cena opcji to wartość wewnętrzna plus czasowa, a spójności całego układu pilnuje parytet put-call.

To nie jest porada inwestycyjna. To materiał edukacyjny porządkujący podstawy opcji według podręczników Hulla i Natenberga oraz materiałów edukacyjnych OIC; wszystkie przykłady liczbowe są ilustracyjne i umowne.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
