---
title: "Reinforcement learning w tradingu. Gdzie pomaga, gdzie zawodzi"
description: "Reinforcement learning uczy agenta polityki działania przez próby i błędy, maksymalizując skumulowaną nagrodę. W tradingu kusi jako naturalny model decyzji sekwencyjnych, ale środowisko jest niestacjonarne, nagroda zaszumiona, a historia to w praktyce jedna ścieżka, więc agent łatwo przeucza się do przeszłości. Gdzie RL realnie pomaga (optymalna egzekucja zleceń, DDQN), a gdzie bywa przereklamowany (bezpośrednie generowanie sygnału kup/sprzedaj). Źródła: Hambly, Xu i Yang; Zhang, Zohren i Roberts; DDQN dla optimal execution."
date: 2026-07-08 16:00:00 +0200
eyebrow: "Edukacja · uczenie maszynowe"
category: edukacja
dek: "Reinforcement learning to nie skrót do przewidywania ceny. Kompendium bez hype'u: na czym polega uczenie agenta polityki działania, dlaczego optymalna egzekucja jest dla RL zadaniem wdzięcznym, a bezpośrednie generowanie sygnału pułapką, i czemu o wszystkim decyduje realizm symulatora oraz kosztów."
readingTime: 8
tags: ["reinforcement learning", "uczenie ze wzmocnieniem", "optimal execution", "egzekucja", "DDQN", "Hambly Xu Yang", "Zhang Zohren Roberts", "deep learning", overfitting, "niestacjonarność", "szeregi czasowe", quant, Forex]
---

> **W skrócie**
>
> - **RL uczy polityki, nie prognozy.** Agent obserwuje stan, wykonuje akcję, dostaje liczbową nagrodę i przez próby i błędy uczy się reguły działania (polityki), która maksymalizuje skumulowaną, zwykle zdyskontowaną nagrodę. W tradingu nagrodą jest najczęściej zysk skorygowany o ryzyko i pomniejszony o koszty.
> - **Trading wygląda jak idealny problem RL, ale rynek łamie założenia.** Decyzje są sekwencyjne, a nagroda jasna, więc sformułowanie kusi. Jednak środowisko jest niestacjonarne, nagroda ekstremalnie zaszumiona, a historia to w praktyce jedna ścieżka, więc agent o dużej pojemności zapamiętuje przeszłość zamiast uczyć się reguły, która uogólni się na przyszłość.
> - **RL naprawdę błyszczy tam, gdzie jest wierny symulator i mierzalny koszt do minimalizacji: optymalna egzekucja dużego zlecenia.** Agent uczy się harmonogramu (ile realizować w każdym oknie), a podejścia typu DDQN generalizują klasyczne modele egzekucji. To jest sterowanie kosztem, a nie prognoza kierunku.
> - **RL bywa przereklamowany tam, gdzie ma wprost wygenerować sygnał kup albo sprzedaj.** Bez sygnału w danych agent dopasowuje się do jednej ścieżki historii, a większość opublikowanych sukcesów nie przeżywa realistycznych kosztów i uczciwego out-of-sample (Hambly, Xu i Yang, 2023; Zhang, Zohren i Roberts, 2020).

**Teza w jednym zdaniu:** reinforcement learning nie omija problemu przewidywania rynku, tylko przenosi trudność na projekt środowiska i nagrody, dlatego działa tam, gdzie istnieje realistyczny symulator i jasny koszt do minimalizacji (egzekucja), a zawodzi tam, gdzie ma z zaszumionej historii wyprodukować kierunek.

## Na czym polega reinforcement learning

Reinforcement learning (uczenie ze wzmocnieniem) opisuje uczenie się przez działanie. Jest agent i jest środowisko. W każdym kroku agent widzi stan środowiska, wybiera akcję, a środowisko odpowiada nową sytuacją i liczbową nagrodą. Agent nie dostaje gotowej instrukcji, co jest dobrym ruchem. Uczy się z konsekwencji: powtarza to, co w dłuższym rozrachunku przynosi wyższą nagrodę, i unika tego, co ją obniża. Celem nie jest maksymalizacja nagrody za jeden krok, tylko skumulowanej nagrody w czasie, zwykle zdyskontowanej, gdzie bliższe nagrody ważą więcej niż odległe.

```
Pętla RL:
  stan  ->  agent wybiera akcję  ->  środowisko zwraca nagrodę + nowy stan
                    ^                                              |
                    |_______________ aktualizacja polityki _______|
Cel: polityka maksymalizująca skumulowaną (zdyskontowaną) nagrodę.
```

Formalnie to zadanie to proces decyzyjny Markowa: zbiór stanów, zbiór akcji, funkcja przejścia i funkcja nagrody. Rozwiązaniem jest polityka, czyli reguła przypisująca akcję do stanu. Dobra polityka maksymalizuje wartość, czyli oczekiwaną sumę przyszłych nagród. Tu pojawia się napięcie między eksploracją a eksploatacją: żeby znaleźć lepszą politykę, agent musi czasem próbować ruchów niepewnych (eksploracja), a nie tylko powtarzać to, co już zna jako dobre (eksploatacja).

Kontrast z klasycznym uczeniem nadzorowanym jest istotny. W nadzorowanym masz etykietę: to zdjęcie przedstawia kota. W RL nie ma etykiety poprawnej akcji, jest tylko odroczona, zaszumiona nagroda po całej sekwencji decyzji. To rodzi problem przypisania zasługi (credit assignment): jeśli nagroda przyszła na końcu, trudno wskazać, która z wcześniejszych akcji naprawdę na nią zapracowała. Deep RL wstawia w to miejsce sieć neuronową jako aproksymator: sieć uczy się albo wartości akcji (rodzina Q-learning, DQN, DDQN), albo bezpośrednio polityki (metody policy gradient). DDQN (Double Deep Q-Network) to wariant, który koryguje znaną skłonność zwykłego DQN do przeszacowywania wartości akcji, i to jego często spotyka się w pracach o egzekucji.

<figure>
<svg viewBox="0 0 660 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif" role="img" aria-label="Petla uczenia ze wzmocnieniem: agent i srodowisko wymieniaja akcje, stan i nagrode">
<defs>
<marker id="rl-arrow" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor" opacity="0.75"/>
</marker>
</defs>
<rect x="125" y="112" width="180" height="96" rx="16" fill="#0b66c3" fill-opacity="0.12" stroke="#0b66c3" stroke-width="2"/>
<text x="215" y="154" text-anchor="middle" font-size="21" font-weight="600" fill="currentColor" opacity="0.85">Agent</text>
<text x="215" y="178" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.6">uczy się polityki</text>
<rect x="425" y="112" width="180" height="96" rx="16" fill="#1a9e6a" fill-opacity="0.12" stroke="#1a9e6a" stroke-width="2"/>
<text x="515" y="154" text-anchor="middle" font-size="21" font-weight="600" fill="currentColor" opacity="0.85">Środowisko</text>
<text x="515" y="178" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.6">rynek, cena, koszt</text>
<path d="M185,112 C185,66 245,66 245,112" fill="none" stroke="currentColor" stroke-width="2" opacity="0.5" marker-end="url(#rl-arrow)"/>
<text x="215" y="52" text-anchor="middle" font-size="12.5" fill="currentColor" opacity="0.7">aktualizacja polityki</text>
<path d="M307,136 C352,82 378,82 423,136" fill="none" stroke="currentColor" stroke-width="2" opacity="0.55" marker-end="url(#rl-arrow)"/>
<text x="365" y="74" text-anchor="middle" font-size="14" fill="currentColor" opacity="0.8">akcja</text>
<path d="M423,184 C378,238 352,238 307,184" fill="none" stroke="currentColor" stroke-width="2" opacity="0.55" marker-end="url(#rl-arrow)"/>
<text x="365" y="256" text-anchor="middle" font-size="14" fill="currentColor" opacity="0.8">stan, nagroda</text>
</svg>
<figcaption>Pętla uczenia ze wzmocnieniem. Agent wysyła do środowiska akcję, środowisko odsyła nowy stan i nagrodę, a agent na tej podstawie aktualizuje politykę i powtarza cykl.</figcaption>
</figure>

## Dlaczego trading kusi jako problem RL

Handel wygląda jak podręcznikowy przykład RL. Decyzje są sekwencyjne: dzisiejsza pozycja, otwarta czy zamknięta, zmienia sytuację, w której podejmujesz jutrzejszą. Jest naturalna nagroda: zysk, najlepiej skorygowany o ryzyko i pomniejszony o koszty. Jest stan: cena, zmienność, wielkość pozycji, czas do zamknięcia sesji. Kusząca obietnica brzmi tak: nie musisz osobno przewidywać ceny i osobno budować reguł wejścia, sizingu oraz wyjścia. Ucz agenta od obserwacji wprost do akcji, a on sam nauczy się kupować, sprzedawać, dokładać i wychodzić, wliczając koszty w nagrodę.

To jest realny powab. Zarządzanie pozycją, koszty transakcyjne i kompromis między zyskiem a ryzykiem da się w RL wyrazić w jednej funkcji nagrody, zamiast sklejać je z osobnych heurystyk. Problem w tym, że elegancja sformułowania nie gwarantuje, że w danych jest czego się uczyć. I tu zaczynają się ściany.

## Dlaczego to jest trudne: cztery ściany

Pierwsza ściana to niestacjonarność. RL w wersji podręcznikowej zakłada, że reguły środowiska (przejścia i nagrody) są stałe. Rynek tego nie spełnia. Reżimy się zmieniają, polityka banków centralnych się zmienia, mikrostruktura się zmienia. Polityka wyuczona w jednym reżimie degraduje się, gdy reżim się obraca. Co gorsza, cel jest ruchomy w sposób adwersaryjny: jeśli jakaś reguła naprawdę zarabia i zostanie odkryta, kapitał ją zamyka.

Druga ściana to zaszumiona nagroda i przypisanie zasługi. Zwrot na krótkim horyzoncie to niemal czysty szum. Agent dostaje sygnał uczący o fatalnym stosunku sygnału do szumu, więc łatwo bierze przypadkowy ciąg zyskownych transakcji za dowód, że jego polityka jest dobra. Przy odroczonej nagrodzie dochodzi pytanie, która z decyzji w sekwencji naprawdę zapracowała na wynik, a które były neutralne albo szkodliwe, tylko zamaskowane przez szczęśliwy koniec.

Trzecia ściana to głód próbek zderzony z jedną ścieżką historii. Algorytmy deep RL potrzebują ogromnej liczby prób, bo w symulatorach gier można rozegrać miliony partii. Historia rynku to w praktyce jedna zrealizowana ścieżka, a najwyżej kilka, jeśli liczyć różne instrumenty. Nie da się jej przeżyć milion razy w niezależnych wariantach. Agent, który dostaje wciąż tę samą przeszłość, uczy się jej na pamięć, zamiast uczyć się reguły, która uogólni się na przyszłość.

Czwarta ściana to sprzężenie zwrotne i kruchość nagrody. Twoje akcje mogą wpływać na środowisko (wpływ na rynek, poślizg), a część stanu jest nieobserwowalna, więc założenie Markowa pęka. Do tego projekt funkcji nagrody jest kruchy: drobna zmiana, inne ważenie ryzyka albo inna kara za koszt, potrafi wyprodukować zupełnie inne zachowanie agenta, czasem takie, które gra artefakty symulatora zamiast realnej przewagi. Przegląd Hambly, Xu i Yang (2023) zbiera te ostrzeżenia w jedno: RL w finansach jest obiecujący, ale głód próbek, niestacjonarność i realizm środowiska to bariery, nie detale.

## Gdzie RL naprawdę błyszczy: optymalna egzekucja

Jest jednak klasa zadań, w której RL dokłada realną wartość, i nie jest to zgadywanie kierunku. To optymalna egzekucja: masz do zrealizowania duże zlecenie i chcesz je wykonać jak najtaniej. Napięcie jest konkretne. Jeśli wrzucisz wszystko naraz, ruszysz rynek przeciw sobie (market impact) i zapłacisz poślizg. Jeśli rozłożysz zlecenie zbyt wolno, wystawiasz się na ryzyko, że cena odjedzie, zanim skończysz (timing risk). Optymalny harmonogram waży jedno przeciw drugiemu.

To zadanie ma cechy, których brakowało przy generowaniu sygnału. Cel jest jasny i mierzalny: minimalizuj koszt realizacji względem punktu odniesienia, na przykład implementation shortfall. Istnieje przyzwoity model środowiska: dynamikę arkusza zleceń da się symulować, a klasyczny wynik Almgrena i Chrissa (2000) daje analityczny punkt startu. RL wchodzi tam, gdzie założenia modelu analitycznego są zbyt sztywne, i uczy się harmonogramu adaptacyjnego, reagującego na bieżący stan rynku. Kierunek tej pracy wyznaczyli już Nevmyvaka, Feng i Kearns (2006), pokazując uczenie ze wzmocnieniem dla egzekucji na danych z arkusza zleceń. Nowsze podejścia (Ning, Lin i Jaimungal) używają właśnie DDQN, żeby agent uczył się, ile realizować w każdym oknie czasowym. Konkretne liczby wyników są tu drugorzędne, bo istotny jest mechanizm: RL nie przewiduje, dokąd pójdzie cena, tylko steruje kosztem realizacji przy danym ruchu.

Dlaczego akurat tu działa: bo mamy wierny symulator, mierzalny koszt i zadanie sterowania, a nie wróżenia. To jest różnica gatunkowa, nie stopnia.

## Gdzie bywa przereklamowany: generowanie sygnału

Najgłośniejsza obietnica RL w tradingu jest też najbardziej ryzykowna: niech agent sam wygeneruje sygnał kup albo sprzedaj, wprost z ceny. Tu wracają wszystkie cztery ściany naraz. Skoro w surowej cenie na krótkim horyzoncie sygnału jest mało, a historia to jedna ścieżka, agent o dużej pojemności najłatwiej minimalizuje stratę treningową przez dopasowanie się do tej jednej ścieżki. Wynik in-sample potrafi wyglądać olśniewająco i wyparowuje out-of-sample.

Praca Zhang, Zohren i Roberts (2020) należy do uczciwszych w tym nurcie: testuje deep RL, zarówno metody wartościowe, jak i policy gradient, na koszyku kontraktów terminowych, z jawnym traktowaniem pozycji i kosztów. Wniosek do zapamiętania nie jest liczbą, tylko dyscypliną: bez starannego uwzględnienia kosztów transakcyjnych i uczciwego podziału na okres uczenia i testu wyniki są nie do obrony, a przewaga, jeśli w ogóle się pojawia, jest krucha i wrażliwa na założenia. RL nie tworzy przewagi tam, gdzie jej nie ma w danych. Jeśli prosty benchmark (persystencja, reguła momentum, model liniowy) nie znajduje sygnału, agent RL najczęściej też go nie znajdzie, tylko lepiej ukryje przeuczenie pod złożonością.

## Symulator i koszty decydują

Ta sama różnica tłumaczy oba przypadki. RL jest dokładnie tak dobry, jak środowisko, w którym się uczy. Przy egzekucji środowisko (arkusz zleceń, koszt, punkt odniesienia) da się wiernie odwzorować, więc polityka uczy się czegoś prawdziwego. Przy generowaniu sygnału środowiskiem jest cała przyszła dynamika ceny, której wiernie odwzorować się nie da, więc agent uczy się głównie właściwości próbki.

Stąd dwie żelazne kontrole. Po pierwsze, koszty: symulacja bez realistycznego spreadu, poślizgu i prowizji produkuje polityki, które żyją z artefaktów, a giną po zderzeniu z rzeczywistym kosztem. Wiele efektownych wyników RL to po prostu edge mniejszy niż koszt, którego symulator nie widział. Po drugie, uczciwy out-of-sample: agent musi być oceniany na danych, których nie dotykał w uczeniu, z zachowaniem kierunku czasu, bo inaczej mierzysz jego pamięć, nie jego umiejętność. Te dwie kontrole obalają większość obietnic szybciej niż jakakolwiek dyskusja o architekturze sieci.

## Co z tego wynika przy stole

Mapa jest spójna z resztą uczenia maszynowego w tradingu. RL to narzędzie sterowania dla dobrze postawionych zadań z mierzalnym kosztem i wiernym symulatorem, a wzorcowym przykładem jest optymalna egzekucja. Nie jest to skrót, który omija problem przewidywania rynku. On ten problem tylko przenosi: z pytania, jak przewidzieć cenę, na pytanie, jak zbudować środowisko i nagrodę. Gdy środowisko jest wierne, RL zamienia trud na wartość. Gdy nie jest, produkuje przekonującego, przeuczonego agenta.

```
Kiedy RL jest właściwym narzędziem:
1. jest wierny symulator środowiska        (egzekucja: tak / kierunek: nie)
2. koszt do minimalizacji jest mierzalny   (implementation shortfall: tak)
3. zadanie to sterowanie, nie wróżenie     (harmonogram zlecenia: tak)
Jeśli 1-3 nie są spełnione, RL najczęściej maskuje przeuczenie.
```

Zanim uwierzy się w dowolną politykę RL, warto zadać trzy pytania. Czy istnieje realistyczny symulator środowiska, czy tylko odtwarzanie jednej ścieżki historii. Czy koszt (spread, poślizg, prowizja) jest w nagrodzie w pełnej wysokości. Czy wynik przeżywa uczciwy out-of-sample z zachowaniem kierunku czasu. Polityka, która przechodzi ten filtr, dotyczy zwykle egzekucji albo sterowania ryzykiem, a nie magicznego kierunku, i to jest jej uczciwe, wąskie miejsce.

To nie jest porada inwestycyjna. To edukacyjna mapa jednego narzędzia: gdzie reinforcement learning w tradingu realnie pomaga (egzekucja, sterowanie kosztem), gdzie jest głównie obietnicą (kierunek z zaszumionej ceny), i jaką dyscypliną (symulator, koszty, uczciwy out-of-sample) odróżnić jedno od drugiego, zanim zaufasz liczbie na wykresie.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
