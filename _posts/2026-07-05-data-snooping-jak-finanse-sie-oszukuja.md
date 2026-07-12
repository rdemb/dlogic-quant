---
title: "Data snooping. Jak finanse same się oszukują"
description: "Przy poziomie istotności 5% co dwudziesty bezwartościowy test wychodzi „istotny”, więc kto przeszukuje setki wariantów, musi produkować fałszywe odkrycia. Przegląd korekt na wielokrotne testowanie: FWER i FDR po ludzku, haircut Harveya, Liu i Zhu z progiem t powyżej 3, gwarantowany overfitting backtestów u Baileya i López de Prado oraz losy 7846 reguł technicznych na stu latach DJIA."
date: 2026-07-05 15:00:00 +0200
eyebrow: "Edukacja · walidacja"
dek: "Przetestuj tysiąc losowych strategii, a najlepsza i tak będzie wyglądać świetnie. Właściwe pytanie nie brzmi „czy wynik jest dobry”, tylko „czy jest dobry, biorąc pod uwagę liczbę wykonanych prób”. Wielokrotne testowanie wyjaśnione po ludzku: FWER kontra FDR, próg t powyżej 3 dla nowych faktorów i dwa studia przypadku z reguł technicznych."
readingTime: 8
tags: ["data snooping", "wielokrotne testowanie", FWER, FDR, Bonferroni, "Benjamini i Hochberg", "Harvey Liu Zhu", "Reality Check", "publication bias", overfitting, backtest, walidacja, "istotność statystyczna", statystyka, quant, Forex]
category: edukacja
---

> **W skrócie**
>
> - Przy poziomie istotności 5% co dwudziesty test czystego szumu wychodzi „istotny". Fałszywe odkrycia skalują się liniowo z liczbą prób: sto testów bez żadnego realnego efektu daje średnio pięć „odkryć", tysiąc daje około pięćdziesięciu. Kto przeszukuje setki wariantów, musi znaleźć fałszywe perły.
> - Statystyka ma dwie rodziny korekt. FWER pilnuje, żeby nie pojawiło się ani jedno fałszywe odkrycie (korekta Bonferroniego), i przy wielu testach robi się skrajnie konserwatywna. FDR, zaproponowana przez Benjaminiego i Hochberga (1995), kontroluje odsetek fałszywych wśród ogłoszonych odkryć i przy tysiącach testów zachowuje moc.
> - Harvey, Liu i Zhu (Review of Financial Studies, 2016) policzyli haircut dla finansów: po dziesięcioleciach zbiorowego przeszukiwania tych samych danych nowy faktor powinien przekraczać t równe 3 zamiast klasycznych 2, a połowa ogłoszonych w literaturze faktorów jest prawdopodobnie fałszywa.
> - Na regułach technicznych pokazano to w praktyce dwa razy: Reality Check na uniwersum 7846 reguł (Sullivan, Timmermann i White, 1999) oraz kontrola FDR na stu latach DJIA (Bajgrowicz i Scaillet, 2012). Wniosek wspólny: po uczciwej korekcie i poza okresem wyboru przewaga najlepszych reguł znika.

**Teza w jednym zdaniu:** Wynik backtestu albo opublikowanego „odkrycia" nie znaczy nic bez liczby prób, które za nim stoją, bo przy dostatecznie szerokim przeszukiwaniu znalezienie czegoś imponującego w czystym szumie nie jest ryzykiem, tylko gwarancją.

## Problem w jednym obrazie

Przetestuj tysiąc strategii, które z konstrukcji nie mają żadnej przewagi: losowe wejścia, losowe wyjścia, losowe parametry. Posortuj wyniki i pokaż komuś najlepszą. Zobaczy ładną krzywą kapitału, przyzwoity Sharpe i sensowne obsunięcia. Nie dlatego, że w tym tysiącu było odkrycie, tylko dlatego, że maksimum z tysiąca losowych liczb prawie zawsze leży daleko w prawym ogonie rozkładu.

<figure>
<svg viewBox="0 0 640 300" font-family="-apple-system,Segoe UI,Roboto,sans-serif" xmlns="http://www.w3.org/2000/svg"><text x="34" y="30" font-size="13" fill="currentColor">1000 backtestów czystego szumu. Najlepszy i tak wygląda świetnie</text><line x1="92" y1="60" x2="92" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="92" y1="232" x2="604" y2="232" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M88 69 L92 60 L96 69" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><path d="M596 228 L604 232 L596 236" fill="none" stroke="currentColor" stroke-width="1" opacity="0.6"/><text transform="rotate(-90 30 146)" x="30" y="146" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">liczba strategii z takim wynikiem</text><text x="348" y="286" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">wynik backtestu (np. Sharpe)</text><path d="M118 231 C196 231 204 98 254 98 C304 98 312 231 390 231 Z" fill="#0b66c3" opacity="0.14" stroke="none"/><path d="M118 231 C196 231 204 98 254 98 C304 98 312 231 390 231" fill="none" stroke="#0b66c3" stroke-width="2"/><line x1="254" y1="232" x2="254" y2="238" stroke="currentColor" stroke-width="1" opacity="0.6"/><text x="254" y="252" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">0</text><text x="254" y="86" font-size="10.5" fill="currentColor" opacity="0.6" text-anchor="middle">typowy wynik: okolice zera</text><line x1="545" y1="231" x2="545" y2="118" stroke="#0b66c3" stroke-width="2" stroke-dasharray="4 4"/><circle cx="545" cy="110" r="4.4" fill="#0b66c3"/><text x="600" y="84" font-size="10.5" fill="#0b66c3" text-anchor="end">najlepsza z 1000 prób</text><text x="600" y="99" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end">czysty szum, wygląda jak edge</text></svg>
<figcaption>Wyniki tysiąca strategii bez żadnej przewagi układają się w rozkład wokół zera. Maksimum z tysiąca losowań prawie zawsze ląduje daleko w prawym ogonie, więc „najlepsza strategia" wygląda świetnie z samej konstrukcji eksperymentu. Pytanie nie brzmi „czy wynik jest dobry", tylko „czy jest lepszy, niż powinno wypaść najlepsze z N prób na szumie".</figcaption>
</figure>

Stąd jedyne uczciwe pytanie wobec każdego wyniku: nie „czy jest dobry", tylko „czy jest dobry, biorąc pod uwagę, ile prób wykonano, żeby go znaleźć". Ta sama liczba znaczy zupełnie co innego po jednej próbie i po tysiącu. Cała reszta tego tekstu to różne sposoby zadawania tego jednego pytania.

## Co dwudziesty bezwartościowy test wychodzi „istotny"

Klasyczny próg istotności 5% to umowa: godzimy się, że test czegoś, co nie działa, raz na dwadzieścia przypadków pokaże „efekt". Przy pojedynczym, z góry zaplanowanym teście to rozsądny kompromis między czułością a ostrożnością. Przy przeszukiwaniu przestaje nim być, bo oczekiwana liczba fałszywych odkryć rośnie liniowo z liczbą prób.

```
oczekiwane fałszywe odkrycia ≈ N · α   (gdy żaden testowany efekt nie istnieje)

   20 testów · 5%  ≈  1 fałszywe „odkrycie"
  100 testów · 5%  ≈  5
 1000 testów · 5%  ≈ 50
```

Kto przepuszcza przez dane grid stu kombinacji parametrów, przy zerowym edge'u znajdzie średnio pięć „istotnych" wariantów. Kto testuje tysiąc reguł, znajdzie około pięćdziesięciu. To nie jest pech, spisek ani błąd w kodzie, tylko arytmetyka. Problem zaczyna się wtedy, gdy raport pokazuje wyłącznie zwycięzcę, a licznik prób zostaje za kadrem. Odbiorca widzi „istotny wynik" i nie widzi dziewiętnastu prób, które nie wyszły.

## Dwie szkoły korekty: FWER i FDR

Statystyka zna ten problem od dawna i oferuje dwie rodziny odpowiedzi. Różnią się tym, co dokładnie obiecują.

FWER (family-wise error rate) to prawdopodobieństwo, że w całej rodzinie testów pojawi się choćby jedno fałszywe odkrycie. Najprostsza korekta to Bonferroni: przy N testach każdy pojedynczy prowadzisz na poziomie α podzielonym przez N. Obietnica jest mocna, ale cena wysoka. Przy tysiącu testów pojedynczy wynik musi mieć p-value poniżej 0.005%, więc razem z fałszywymi odkryciami wycinasz też większość prawdziwych. To podejście dla sytuacji, w których jedna pomyłka jest niedopuszczalna.

FDR (false discovery rate) odpuszcza perfekcję i kontroluje co innego: oczekiwany odsetek fałszywych wśród odkryć, które ogłaszasz. To pomysł Benjaminiego i Hochberga (1995). Zamiast „zero pomyłek" obiecujesz „wśród tego, co ogłaszam jako odkrycia, najwyżej ustalona część, na przykład 10%, to śmieci".

```
FWER:  P(choćby jedno fałszywe odkrycie) ≤ α
       Bonferroni: każdy test na poziomie α / N

FDR:   oczekiwany odsetek fałszywych wśród ogłoszonych odkryć ≤ q
       Benjamini i Hochberg: posortuj p-value rosnąco, p(1) ≤ p(2) ≤ ... ≤ p(N),
       przyjmij wszystkie do największego k, dla którego p(k) ≤ (k / N) · q
```

Po ludzku: FWER to kontroler, który woli zatrzymać stu uczciwych, byle nie przepuścić jednego oszusta. FDR to kontroler, który przepuszcza ruch, ale pilnuje, żeby wśród przepuszczonych odsetek oszustów nie przekroczył ustalonego poziomu. Przy pojedynczych, kosztownych decyzjach sensowniejszy bywa pierwszy. Przy skanowaniu tysięcy kandydatów naraz (faktory, reguły techniczne, kombinacje parametrów) praktyczniejszy jest drugi, bo zachowuje moc i nadal cokolwiek znajduje, tyle że z jawną etykietą jakości zamiast iluzji pewności.

## Haircut dla finansów: t powyżej 3

Harvey, Liu i Zhu w pracy „...and the Cross-Section of Expected Returns" (Review of Financial Studies, 2016) przyłożyli tę logikę do literatury o faktorach wyjaśniających zwroty akcji. Punkt wyjścia: przez dziesięciolecia setki badaczy przeszukiwały w dużej mierze te same dane, publikując kolejne zmienne, które rzekomo tłumaczą przekrój oczekiwanych zwrotów. Klasyczny próg t około 2, odpowiednik istotności 5%, jest ustawiony tak, jakby test był jeden. Tymczasem testów były tysiące, tylko rozproszone po latach, zespołach i czasopismach.

Wniosek pracy jest ilościowy: po uwzględnieniu skali historycznego przeszukiwania nowe „odkrycie" powinno przekraczać t równe 3, a połowa ogłoszonych w literaturze faktorów jest prawdopodobnie fałszywa. To nie jest zarzut nieuczciwości wobec konkretnych autorów. To rachunek na poziomie systemu: przy takiej liczbie prób w obiegu taka część zwycięzców musi być szumem, nawet jeśli każdy z osobna testował starannie.

## Szuflady pełne wyników nieistotnych

Do rachunku dochodzi publication bias. Czasopisma chętniej publikują wyniki istotne, bo „brak efektu" słabo wygląda w tytule. Wyniki nieistotne lądują w szufladach i nigdy nie trafiają do obiegu. Widzialna literatura jest więc próbą zwycięzców: nawet gdyby każdy badacz wykonał dokładnie jeden uczciwy test, sam filtr publikacji odtworzyłby efekt przeszukiwania, bo do druku przechodzą głównie te jednostkowe testy, które akurat wypadły „istotnie". Czytelnik widzi dwudziesty test, a dziewiętnastu pozostałych nie zobaczy nigdy. Dokładnie dlatego korekta Harveya, Liu i Zhu musi być tak surowa: poprawia nie tylko za próby jednego zespołu, ale za dziesięciolecia prób całej profesji.

## Overfitting gwarantowany matematycznie

Bailey, López de Prado i współautorzy w „Pseudo-Mathematics and Financial Charlatanism" (Notices of the AMS, 2014) doprowadzili tę myśl do końca po stronie backtestów. Ich wynik: przy dostatecznie wielu wypróbowanych konfiguracjach znalezienie strategii z imponującym wynikiem in-sample jest gwarantowane, nawet gdy wszystkie konfiguracje to czysty szum. Oczekiwane maksimum z N prób rośnie wraz z N, więc minimalna długość danych potrzebna, żeby najlepszy wynik dało się odróżnić od szumu, rośnie razem z liczbą prób. Krótkie serie finansowe plus szerokie gridy parametrów to w tej optyce przepis na overfitting pewny, a nie tylko możliwy.

Autorzy piszą wprost, że prezentowanie wyników backtestu bez ujawnienia liczby wypróbowanych konfiguracji to pseudomatematyka i szarlataneria finansowa, stąd tytuł artykułu w czasopiśmie Amerykańskiego Towarzystwa Matematycznego. Praktyczną odpowiedzią są metryki, które jawnie karzą za liczbę prób, na czele z Deflated Sharpe Ratio, rozebranym na części w osobnym artykule: [dlaczego twój Sharpe kłamie](/dlogic-quant/2026/07/09/dlaczego-twoj-sharpe-klamie-deflated-sharpe/).

## Poligon: 7846 reguł technicznych

Najczystszym poligonem tej dyskusji są reguły analizy technicznej, bo łatwo je generować hurtowo. Sullivan, Timmermann i White (Journal of Finance, 1999) zbudowali uniwersum 7846 reguł: średnie kroczące, przebicia kanałów, filtry, poziomy wsparcia i oporu w wielu parametryzacjach. Zamiast pytać „czy ta reguła działa", zapytali „czy najlepsza reguła działa lepiej, niż powinna wypaść najlepsza z 7846 prób na szumie". Do tego służy Reality Check White'a: bootstrapowy test, który porównuje zwycięzcę nie z zerem, tylko z rozkładem zwycięzców całego uniwersum. Na bardzo długiej historii DJIA najlepsza reguła przetrwała tę korektę, ale w najnowszym podokresie ich próby po korekcie nie przetrwało już nic. Wynik, który w pojedynczym teście wyglądał na mocny, po urealnieniu poprzeczki okazywał się cieniem dawnej anomalii.

Bajgrowicz i Scaillet (Journal of Financial Economics, 2012) wrócili do tego samego uniwersum z nowszym narzędziem: kontrolą FDR na około stu latach danych DJIA. Pytanie postawili praktycznie: czy reguły wybrane jako dobre w jednym okresie dawały zarobić w kolejnym, czyli czy inwestor mógł wskazać je zawczasu. Odpowiedź: brak persystencji. Zwycięzcy z przeszłości nie powtarzali wyników poza okresem, w którym ich wybrano, a uwzględnienie kosztów transakcyjnych dobijało resztę. Szerszy przegląd badań nad analizą techniczną: [czy analiza techniczna działa](/dlogic-quant/2026/07/07/czy-analiza-techniczna-dziala-badania/).

## Jedno pytanie: ile prób stoi za tym wynikiem

Praktyczna nauka z całej tej literatury mieści się w jednym odruchu: zanim ocenisz wynik, zapytaj o licznik prób.

Przy cudzych wynikach oznacza to nieufność wobec pojedynczej metryki z nieznanej liczby testów. Sharpe, win rate, profit factor czy „istotność" bez informacji, ile konfiguracji, rynków i okresów przetestowano, to liczba bez mianownika. Ogłoszony faktor z t równym 2.5 wygląda dobrze na tle podręcznika i blado na tle progu 3. Sprzedawca systemu, który pokazuje jeden piękny backtest, niemal na pewno pokazuje maksimum z przeszukiwania, o którym nie mówi.

Przy własnej pracy oznacza to liczenie samego siebie. Każda kombinacja parametrów, każdy filtr, każda zmiana rynku albo okresu, nawet „szybki rzut oka" na wykres z nową hipotezą, to kolejna próba, która podnosi poprzeczkę dla wszystkiego, co znajdziesz później. Kto loguje liczbę prób, rejestruje hipotezy przed testem i trzyma dane out-of-sample do jednorazowego użycia, ten może korzystać z FDR czy deflacji uczciwie i od czasu do czasu naprawdę coś znaleźć. Kto prób nie liczy, ten nie testuje strategii, tylko losuje z prawego ogona i nazywa to badaniem.

To nie jest porada inwestycyjna. To przegląd literatury o wielokrotnym testowaniu, pokazany po to, żeby przed uwierzeniem w jakikolwiek wynik, cudzy albo własny, zadać jedno pytanie: ile prób za nim stoi.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
