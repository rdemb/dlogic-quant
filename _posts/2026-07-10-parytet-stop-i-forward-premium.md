---
title: "Parytet stóp procentowych i zagadka forward premium"
description: "Pokryty parytet stóp (CIP) jako warunek bezarbitrażowy wiążący stopy, kurs spot i forward, w zapisie F/S = (1+i_kraj)/(1+i_zagr); parytet niepokryty (UIP) jako hipoteza o oczekiwaniach; empiryczna porażka UIP i zagadka forward premium z ujemnym nachyleniem w regresji Famy (1984); dlaczego to ekonomiczny fundament carry trade i dlaczego premia jest zapłatą za ryzyko krachu (Brunnermeier, Nagel, Pedersen 2008); pęknięcie samego CIP po 2008 roku i baza cross-currency (Du, Tepper, Verdelhan 2018)."
date: 2026-07-10 09:00:00 +0200
eyebrow: "Edukacja · makro"
dek: "Trzy powiązane relacje FX na jednej stronie: pokryty parytet stóp, który domyka arbitraż, niepokryty parytet stóp, który jest tylko hipotezą o oczekiwaniach, oraz systematyczne odchylenie danych od tej hipotezy, znane jako zagadka forward premium. Do tego kontekst: dlaczego z tej anomalii wyrasta carry, jaka jest jej cena w ogonie rozkładu i co pękło w samym arbitrażu po 2008 roku."
readingTime: 8
tags: ["parytet stóp", makro, FX, "carry trade", UIP, CIP, "forward premium", "Fama 1984", "Engel 1996", "Lustig Verdelhan", "Du Tepper Verdelhan", "cross-currency basis", arbitraż, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Pokryty parytet stóp (CIP) to warunek bezarbitrażowy: kurs terminowy jest zdeterminowany przez kurs spot i różnicę stóp, w zapisie F/S = (1 + stopa krajowa) / (1 + stopa zagraniczna). Waluta o wyższej stopie wychodzi w tym rachunku na terminowym dyskoncie, które dokładnie kasuje jej przewagę odsetkową, więc zabezpieczony zwrot jest wyrównany.
> - Niepokryty parytet stóp (UIP) podstawia w miejsce kursu terminowego oczekiwany przyszły spot i głosi, że różnica stóp równa się oczekiwanej zmianie kursu. To już nie arbitraż, tylko hipoteza wsparta na racjonalnych oczekiwaniach i neutralności wobec ryzyka.
> - Dane łamią UIP. W regresji Famy (1984) nachylenie, które przy prawdziwym UIP wynosiłoby 1, wychodzi zwykle poniżej jedynki, a często ujemne: waluty o wyższej stopie w badanych próbach nie osłabiały się zgodnie z hipotezą, przeciętnie wręcz się umacniały. To zagadka forward premium.
> - Anomalia nie jest darmowym obiadem. Jedno z wyjaśnień wiąże premię z ryzykiem konsumpcyjnym (Lustig, Verdelhan 2007), a rozkład zwrotów carry jest silnie lewoskośny: powolne zyski i gwałtowne krachy (Brunnermeier, Nagel, Pedersen 2008). Carry to osobny temat z własnym ryzykiem ogona.
> - Po 2008 pękł nawet CIP. Utrzymuje się niezerowa baza cross-currency, czyli mierzalny koszt zabezpieczenia jednej waluty w drugą ponad różnicę stóp (Du, Tepper, Verdelhan 2018), rozszerzający się regularnie na koniec kwartałów.

**Teza w jednym zdaniu:** CIP jest twardą tożsamością bezarbitrażową, UIP tylko hipotezą o oczekiwaniach, a systematyczna różnica między nimi, czyli zagadka forward premium, jest zarazem najlepiej udokumentowaną anomalią rynku walutowego i źródłem, z którego wyrasta carry wraz z całym swoim ryzykiem.

## Pokryty parytet stóp: warunek bez arbitrażu

Punktem wyjścia jest jedno pytanie zadane na dwa sposoby. Kapitał można trzymać w walucie krajowej na jej stopie, albo wymienić na walutę zagraniczną, ulokować na tamtejszej stopie i już dziś zakontraktować kurs odwrotnej wymiany za rok. Skoro kurs terminowy, czyli forward, jest umówiony z góry, obie drogi są pozbawione ryzyka kursowego, więc muszą dać identyczny wynik. Gdyby dawały różny, istniałby zysk bez ryzyka, a taki zysk rynek domyka niemal natychmiast. Ten warunek nosi nazwę pokrytego parytetu stóp procentowych.

```
Pokryty parytet stóp (CIP)
S = cena 1 jednostki waluty zagranicznej w walucie krajowej

    F / S = (1 + i_kraj) / (1 + i_zagr)

Przykład ilustracyjny (stopy roczne, umowne):
    S = 1.1000    i_kraj = 5%    i_zagr = 3%
    F = 1.1000 · 1.05 / 1.03 = 1.1214

Dwie drogi na rok, ten sam wynik dla 1 jedn. krajowej:
    A) lokata krajowa:                      1 → 1.0500
    B) wymiana na zagr. + lokata + forward:
       1 / 1.1000        = 0.9091 zagr.
       0.9091 · 1.03     = 0.9364 zagr.
       0.9364 · 1.1214   = 1.0500 krajowej

Wyższa stopa krajowa (5 > 3) → waluta krajowa na
terminowym DYSKONCIE, które kasuje przewagę odsetkową.
```

Równość wyniku B i wyniku A nie jest przypadkiem, to wręcz definicja kursu terminowego przy działającym arbitrażu. Ważniejsze jest, co ten rachunek mówi o kierunku. Waluta krajowa ma tu wyższą stopę, pięć wobec trzech procent, a mimo to kurs terminowy wycenia ją na osłabienie: forward pokazuje więcej jednostek krajowych za walutę zagraniczną niż spot, czyli waluta krajowa stoi na terminowym dyskoncie. To reguła ogólna, nie cecha przykładu. Waluta o wyższej stopie zawsze wychodzi w CIP na terminowym dyskoncie, a to dyskonto dokładnie równoważy przewagę odsetkową. Zabezpieczony zysk z pogoni za wyższą stopą wynosi zero, bo cała różnica siedzi już w cenie forwardu.

## Parytet niepokryty: to już tylko hipoteza

Pokryty parytet domyka arbitraż właśnie dlatego, że forward jest zakontraktowany. Co jednak, gdy kursu na przyszłość nikt nie zabezpiecza kontraktem, tylko po prostu czeka na przyszły spot? W miejsce kursu terminowego wchodzi wtedy kurs oczekiwany, a warunek zmienia naturę: z tożsamości arbitrażowej staje się hipotezą o zachowaniu rynku. To parytet niepokryty.

```
Parytet niepokryty (UIP)
w miejsce forwardu wchodzi oczekiwany przyszły spot:

    E[S_{t+1}] / S = (1 + i_kraj) / (1 + i_zagr)

Forma logarytmiczna (przybliżenie dla małych stóp):

    E[Δs] ≈ i_kraj − i_zagr
    oczekiwana zmiana kursu ≈ różnica stóp

CIP + UIP razem  →  F = E[S_{t+1}]
forward jako nieobciążony prognostyk przyszłego spotu
```

Przesłanie UIP jest mocne. Jeżeli krajowa stopa jest wyższa o dwa punkty procentowe, rynek ma oczekiwać, że waluta krajowa osłabi się średnio o mniej więcej te dwa punkty, przez co oczekiwany zysk z różnicy stóp znika. Cały mechanizm stoi na dwóch założeniach: że oczekiwania są racjonalne i że inwestorzy są neutralni wobec ryzyka, to znaczy nie żądają premii za trzymanie jednej waluty zamiast drugiej. Oba są dyskusyjne. Połączenie CIP i UIP daje przy tym wniosek w pełni testowalny: kurs terminowy powinien być nieobciążonym prognostykiem przyszłego kursu spot. To zdanie da się skonfrontować z danymi, i właśnie tam zaczyna się problem.

## Zagadka forward premium: dane mówią „nie"

Test ma prostą formę. Rzeczywistą zmianę kursu regresuje się na różnicę stóp, równoważnie na premię terminową. Jeżeli UIP jest prawdziwe, nachylenie tej regresji powinno wynosić jeden. Fama w pracy z 1984 roku pokazał, że tak nie jest, i to nie o włos: szacowane nachylenie jest nie tylko mniejsze od jedynki, ale zwykle ujemne.

```
Test UIP, regresja Famy (1984)
Δs = zmiana log-kursu   (Δs > 0 = osłabienie waluty krajowej)

    Δs_{t+1} = α + β · (i_kraj − i_zagr) + ε

    UIP przewiduje:                  β = 1
    Fama (1984) i późniejsze prace:  β < 1,  często β < 0

β < 0  →  waluta o wyższej stopie przeciętnie się UMACNIAŁA,
          zamiast osłabiać zgodnie z hipotezą.
```

Znak ujemny ma dosłowne znaczenie. UIP mówi, że waluta o wyższej stopie powinna się osłabiać. Dane z badanych okresów mówią, że osłabiała się za słabo, a przeciętnie wręcz się umacniała. Rozbieżność między przewidywaniem hipotezy a rzeczywistością nie tylko nie znikała, ona zmieniała znak. Zjawisko nazwano zagadką forward premium, ponieważ forward systematycznie wskazywał zły kierunek. Engel w przeglądzie literatury z 1996 roku zebrał dziesiątki takich badań i pokazał, że anomalia jest odporna: nie znika przy zmianie waluty, okresu ani metody, a próby wyjaśnienia jej samą premią za ryzyko w ówczesnych modelach nie domykały rachunku.

Ta sama liczba, ujemne nachylenie, jest ekonomicznym fundamentem carry trade. Skoro waluta o wyższej stopie nie osłabia się tyle, ile trzeba, by wyrównać różnicę stóp, to trzymanie waluty wysokodochodowej za pożyczoną niskodochodową przynosiło historycznie dodatni średni wynik. Nie dlatego, że ktoś przewidział kurs, tylko dlatego, że składnik oczekiwanego osłabienia okazywał się mniejszy od różnicy stóp.

## Skąd premia: ryzyko, nie darmowy obiad

Dodatni średni wynik nie oznacza, że rynek zostawia pieniądze na stole. Dominujące wyjaśnienie głosi, że to zapłata za ryzyko, którego nie widać w spokojnych czasach. Lustig i Verdelhan w pracy z 2007 roku posortowali waluty w portfele według stopy i pokazali, że zwroty portfeli wysokodochodowych są powiązane z ryzykiem wzrostu konsumpcji w Stanach Zjednoczonych: te waluty tracą właśnie wtedy, gdy gospodarka zwalnia, a konsumpcja się kurczy, czyli w najgorszym możliwym momencie. Premia carry jest w tym ujęciu wynagrodzeniem za to, że aktywo wypłaca marnie w złych stanach świata.

Kształt rozkładu dopowiada resztę. Brunnermeier, Nagel i Pedersen w pracy z 2008 roku pokazali, że zwroty z carry są silnie lewoskośne. Strategia zbiera drobne, regularne zyski przez długie okresy spokoju, a potem gwałtownie je oddaje w krachu, gdy zanik płynności finansującej wymusza jednoczesne zamykanie pozycji i waluty wysokodochodowe zapadają się skokowo. W obrazowym skrócie z tej literatury carry wchodzi po schodach, a spada windą. Dodatnia średnia jest więc ceną za ogon rozkładu: rzadki, lecz dotkliwy.

Stąd twarda granica tego tekstu. Opis anomalii to opis mechanizmu, nie zachęta do jego wykorzystania. Zagadka forward premium tłumaczy, dlaczego carry w ogóle istnieje, lecz nie zdejmuje z niego ryzyka krachu, które jest jego drugą stroną. Wielkość pozycji, moment wejścia i zarządzanie ryzykiem ogona to osobny temat, a sama znajomość anomalii niczego nie gwarantuje.

## Po 2008: pęka nawet pokryty parytet

Na koniec zwrot akcji, który przez dekady wydawał się niemożliwy. Pokryty parytet jest warunkiem bezarbitrażowym, więc powinien trzymać się zawsze, dopóki ktokolwiek może wykonać arbitraż. Do 2008 roku trzymał się bardzo ściśle, odchylenia mieściły się w granicach szumu. Po kryzysie finansowym coś się zacięło. Du, Tepper i Verdelhan udokumentowali w 2018 roku trwałe odchylenia od CIP: pojawiła się niezerowa baza cross-currency, czyli różnica między kosztem pożyczenia dolara wprost a kosztem uzyskania go syntetycznie, przez pożyczkę w innej walucie i swap walutowy.

```
Baza cross-currency (uproszczenie)

    baza = koszt dolara z FX swap  −  bezpośredni koszt dolara

    przed 2008:  baza ≈ 0     (arbitraż domyka CIP)
    po 2008:     baza ≠ 0     trwale, szersza na koniec kwartałów
```

Przyczyną nie jest brak chętnych do arbitrażu, tylko jego koszt. Po kryzysie wymogi kapitałowe i limity dźwigni sprawiły, że domykanie tej różnicy obciąża bilanse banków, a miejsce w bilansie przestało być darmowe. Baza rozszerza się regularnie na przełomach kwartałów, gdy banki kurczą sumy bilansowe na potrzeby sprawozdań, co widać wprost w danych. Skala bazy dla walut głównych bywała rzędu od pojedynczych do kilkudziesięciu punktów bazowych, zależnie od waluty i momentu. Praktyczny wniosek jest jeden: zabezpieczenie ryzyka walutowego przestało być bezkosztowe. Baza to realny koszt albo dopłata przy przenoszeniu ekspozycji z jednej waluty w drugą, ponad samą różnicę stóp, i dla podmiotu zabezpieczającego dolarową ekspozycję jest twardą pozycją, nie akademicką subtelnością.

Materiał czysto edukacyjny, nie porada inwestycyjna ani zachęta do carry. Stopy pięć i trzy procent w przykładach są umowne i służą arytmetyce, nie prognozie. Wyniki empiryczne opisują przeszłość w badanych próbach i niczego nie gwarantują na przyszłość: ujemne nachylenie regresji bywało niestabilne w czasie, a carry niesie ryzyko gwałtownych obsunięć. Pewna pozostaje tu wyłącznie algebra parytetów, czyli CIP jako tożsamość bezarbitrażowa z poprawką o bazę po 2008 roku oraz UIP jako hipoteza, którą dane systematycznie odrzucają.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
