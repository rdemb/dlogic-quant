---
layout: labpost
title: "143 testy przeszły. Poprawny wynik nadal brzmiał: INCONCLUSIVE"
description: "Dlaczego zielony test suite nie dowodzi właściwości, której eksperyment nigdy nie zdołał zaobserwować."
dek: "Eksperyment zatrzymał się przed Wine, terminalem i danymi brokera. To nie był dowód awarii bota, lecz dowód granicy własnej obserwacji."
date: 2026-08-11 13:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #02"
readingTime: 10
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #02"
cover_title: "143 PASS ≠ DOWÓD"
cover_subtitle: "COMPILED · LOADABLE UNKNOWN · CANARY NOT RUN"
cover_kind: lifecycle
---
<div class="article-status"><span class="primary">ENGINEERING MILESTONE</span><span>COMPILED</span><span>LOADABLE: UNKNOWN</span><span>ACCOUNT CONTACT: 0</span><span>LIVE: NOT AUTHORIZED</span></div>

Celem eksperymentu nie było uruchomienie strategii, otwarcie pozycji ani nawet odczytanie pełnego rynku. Miał odpowiedzieć na znacznie węższe pytanie: czy jeden wcześniej skompilowany i kryptograficznie przypięty artefakt daje się załadować w odizolowanym środowisku, a następnie wykonać ograniczony, wyłącznie odczytowy canary na kilku zamrożonych instrumentach.

Pakiet przeszedł 143 testy. Z zewnątrz wyglądało to jak moment, w którym należało wykonać kolejny krok i po prostu „sprawdzić bota”. Właśnie tutaj pojawiła się jednak różnica pomiędzy projektem, który zbiera zielone pola, a systemem, który próbuje zrozumieć, **co właściwie zostało dowiedzione**.

Eksperyment nie dotarł do Wine. Nie uruchomił terminala. Nie załadował artefaktu. Nie rozpoczął canary. Nie połączył się z rachunkiem ani brokerem. Zatrzymał się wcześniej, na warstwie prywatnego serwera obrazu X11, który nie zdołał poprawnie utworzyć własnego gniazda.

Można było więc uczciwie stwierdzić, że ścieżka uruchomieniowa jest nadal zablokowana. Nie można było natomiast powiedzieć, że skompilowany artefakt jest niekompatybilny z terminalem, ponieważ terminal nigdy nie otrzymał okazji, aby go załadować.

<figure>
<svg viewBox="0 0 980 270" role="img" aria-labelledby="chain-title chain-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="chain-title">Łańcuch obserwacji eksperymentu</title>
  <desc id="chain-desc">Eksperyment zatrzymał się na warstwie X11 przed uruchomieniem Wine, terminala, kodu i artefaktu danych.</desc>
  <defs><marker id="a1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="var(--acc)"/></marker></defs>
  <rect x="28" y="82" width="142" height="74" rx="12" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
  <rect x="226" y="82" width="142" height="74" rx="12" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
  <rect x="424" y="82" width="142" height="74" rx="12" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
  <rect x="622" y="82" width="142" height="74" rx="12" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
  <rect x="820" y="82" width="132" height="74" rx="12" fill="var(--soft)" stroke="var(--line)" stroke-width="2"/>
  <path d="M170 119 H220" stroke="var(--acc)" stroke-width="3" marker-end="url(#a1)"/>
  <path d="M368 119 H418 M566 119 H616 M764 119 H814" stroke="var(--mut)" stroke-width="2" stroke-dasharray="7 7" marker-end="url(#a1)"/>
  <text x="99" y="112" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="18" fill="var(--ink)">X11</text>
  <text x="99" y="137" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="var(--dn)">STOP</text>
  <text x="297" y="112" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="18" fill="var(--ink)">WINE</text>
  <text x="297" y="137" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="var(--mut)">NOT STARTED</text>
  <text x="495" y="112" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="17" fill="var(--ink)">TERMINAL</text>
  <text x="495" y="137" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="var(--mut)">NOT STARTED</text>
  <text x="693" y="112" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="17" fill="var(--ink)">ONSTART</text>
  <text x="693" y="137" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="var(--mut)">NOT OBSERVED</text>
  <text x="886" y="112" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="16" fill="var(--ink)">EVIDENCE</text>
  <text x="886" y="137" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="12" fill="var(--mut)">NOT CREATED</text>
  <circle cx="198" cy="119" r="16" fill="var(--dn)"/><path d="M190 111 L206 127 M206 111 L190 127" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <text x="490" y="215" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="15" fill="var(--mut)">Brak obserwacji wyższej warstwy nie jest dowodem jej awarii.</text>
</svg>
<figcaption>Łańcuch przyczynowy eksperymentu. Czerwona granica pokazuje ostatnią warstwę, o której rzeczywiście powstał dowód.</figcaption>
</figure>

## Testy nie głosują

W projektach technicznych liczba testów bardzo łatwo zaczyna pełnić rolę argumentu retorycznego. Dziesięć testów brzmi słabiej niż sto, a sto słabiej niż tysiąc, dlatego zielony licznik stopniowo zaczyna zastępować pytanie o to, czy poszczególne testy obejmują właściwą warstwę systemu.

Tymczasem test nie jest głosem oddanym za ogólną jakość projektu. Dowodzi jedynie kontraktu, który rzeczywiście wykonał. Test parsera może pokazać, że parser odrzuca błędny dokument. Test manifestu może wykazać zgodność hashy. Test źródła może potwierdzić, że w kodzie nie ma wywołania funkcji handlowej. Żaden z nich nie dowodzi jednak, że skompilowany artefakt uruchomi się pod konkretną wersją terminala, jeżeli terminal nigdy nie został wystartowany.

W tym przypadku 143 testy miały realną wartość: zamknęły wcześniejsze luki związane z pochodzeniem źródła, przypięciem konkretnego artefaktu, ograniczeniem powierzchni działania i zachowaniem granicy bez handlu. Nie miały natomiast mocy dowodowej wobec właściwości `LOADABLE`, ponieważ ścieżka obserwacji zatrzymała się przed loaderem.

To rozróżnienie jest ważniejsze niż sam incydent z X11. System, który nie rozpoznaje granicy własnego testu, może publikować coraz bardziej przekonujące liczby, nie zbliżając się do odpowiedzi na pytanie, które naprawdę próbował rozstrzygnąć.

## COMPILED nie oznacza LOADABLE

Wcześniejsza wersja cyklu życia była zbyt gruba. Kod był albo „zbudowany”, albo „niezbudowany”, a pomiędzy kompilacją i canary brakowało osobnego stanu opisującego zgodność konkretnego artefaktu z konkretnym środowiskiem uruchomieniowym.

Po tym eksperymencie rozdzielenie stało się jawne:

| Stan | Co rzeczywiście oznacza |
|---|---|
| **COMPILED** | Źródło zostało poprawnie przetłumaczone do artefaktu przez określony kompilator. |
| **LOADABLE** | Ten jeden, przypięty artefakt uruchomił się pod dokładnie zdefiniowanym runtime’em. |
| **CANARY_TESTED** | Ograniczone wykonanie doszło do końca i wytworzyło kompletny, zweryfikowany artefakt dowodowy. |

Przejście pomiędzy tymi stanami nie jest formalnością. Kompilator i runtime mogą różnić się wersją, zależnościami, zachowaniem loadera albo środowiskiem systemowym. Program może się uruchomić, ale zapisać niepełny plik. Plik może być kompletny składniowo, ale pochodzić z niewłaściwego przebiegu. Każdy z tych problemów wymaga osobnego dowodu.

<div class="lab-note"><strong>Niedozwolony skrót:</strong> COMPILED ⇒ DZIAŁA</div>

Jest wygodny, lecz naukowo pusty. Poprawny łańcuch wygląda raczej tak:

<div class="lab-note"><strong>Poprawny łańcuch:</strong> COMPILED → LOADABLE → CANARY TESTED → DATA VALIDATED</div>

Dopiero później zaczyna się właściwe pytanie o model, przewagę i wykonanie.

## PASS, FAIL i INCONCLUSIVE to trzy różne wyniki

Najważniejsza lekcja tego etapu nie polega na dodaniu kolejnej etykiety do dashboardu, lecz na odróżnieniu trzech logicznie różnych sytuacji.

**PASS** oznacza, że eksperyment dotarł do badanej własności, zaobserwował ją i spełniła wcześniej ustalone kryterium.

**FAIL** oznacza, że eksperyment również dotarł do badanej własności, lecz obserwacja zaprzeczyła wymaganiu.

**INCONCLUSIVE** oznacza, że ścieżka obserwacyjna nie dotarła do miejsca, w którym własność mogła zostać rozstrzygnięta.

<table>
<thead><tr><th>Wynik</th><th>Własność zaobserwowana?</th><th>Kryterium spełnione?</th></tr></thead>
<tbody>
<tr><td>PASS</td><td>Tak</td><td>Tak</td></tr>
<tr><td>FAIL</td><td>Tak</td><td>Nie</td></tr>
<tr><td>INCONCLUSIVE</td><td>Nie</td><td>Nie można ocenić</td></tr>
</tbody>
</table>

Zamiana `INCONCLUSIVE` na `FAIL` jest niebezpieczna, ponieważ przypisuje awarię niewłaściwej warstwie. Zamiana go na `PASS` jest jeszcze gorsza, ponieważ produkuje twierdzenie bez obserwacji. W obu przypadkach projekt traci zdolność uczenia się: naprawia nie ten element albo promuje komponent, którego nigdy nie sprawdził.

## Dystans dowodowy

Można roboczo nazwać **dystansem dowodowym** odległość pomiędzy warstwą faktycznie sprawdzoną a warstwą, o której formułujemy publiczne twierdzenie.

Jeżeli test jednostkowy funkcji obliczającej cechę prowadzi do komunikatu „model działa na rynku”, dystans jest ogromny. Pomiędzy tymi zdaniami znajdują się timestampy, dostępność informacji, budowa targetu, koszty, podział danych, runtime, egzekucja i zachowanie w czasie rzeczywistym.

Jeżeli natomiast twierdzenie brzmi: „funkcja zwróciła oczekiwany wynik dla zamrożonych przypadków syntetycznych”, dystans jest niewielki i dobrze kontrolowany.

Ta koncepcja nie jest nową formalną miarą statystyczną. Jest praktycznym pytaniem red-teamowym:

> Ile niezaobserwowanych warstw znajduje się pomiędzy dowodem, który posiadam, a zdaniem, które chcę opublikować?

Im większa odpowiedź, tym słabsze prawo do mocnego czasownika: „działa”, „potwierdziłem”, „wdrożyłem” albo „odkryłem”.

## Ten sam błąd występuje w researchu alfy

Przypadek infrastruktury ma bezpośredni odpowiednik w badaniach rynkowych. Model może przejść testy jednostkowe, a mimo to używać danych dostępnych dopiero po decyzji. Backtest może działać deterministycznie, lecz pomijać realny spread. Walidacja może być poprawna matematycznie, ale przeprowadzona na zbiorze, który wielokrotnie służył do wyboru hipotezy. Prognoza może trafnie przewidywać zmianę ceny mid, której nie da się kupić ani sprzedać.

W każdym przypadku testy są prawdziwe wewnątrz własnego kontraktu, lecz publiczna interpretacja wykracza poza to, co zaobserwowano.

Dlatego D-LOGIC rozdziela dziś coraz więcej stanów, nawet jeśli z zewnątrz może to wyglądać jak nadmierna ostrożność. Każde dodatkowe przejście w cyklu życia ogranicza możliwość, że sukces jednej warstwy zostanie użyty jako zastępczy dowód dla kolejnej.

## Najbezpieczniejszym wynikiem był brak danych

W eksperymencie nie odczytano rachunku, nie pobrano danych brokera, nie uruchomiono canary i nie wykonano żadnej operacji handlowej. W projekcie nastawionym na szybkie demonstracje można byłoby uznać to za zmarnowany przebieg.

Z perspektywy programu badawczego był to jednak poprawny rezultat. Granica bezpieczeństwa nie została poluzowana tylko po to, aby uzyskać bardziej widowiskowy output, a awaria niższej warstwy nie została przepisana jako dowód o zachowaniu wyższej.

Następny eksperyment powinien więc odpowiedzieć wyłącznie na kolejny nierozstrzygnięty problem: najpierw stworzyć działające, odizolowane środowisko wyświetlania, potem uruchomić minimalny smoke test Wine, a dopiero później dopuścić loader do próby załadowania przypiętego artefaktu. Nadal bez handlu i bez przeskakiwania do weryfikacji danych.

To wolniejszy sposób budowania systemu, ale tylko pozornie. Najwięcej czasu w projektach quant traci się nie na ostrożne testy, lecz na miesiące rozwijania komponentu, któremu zbyt wcześnie przypisano właściwości, których nigdy nie udowodniono.

143 testy przeszły.

Poprawny wynik pozostał jednak prosty:

> **Nie wiadomo jeszcze, czy artefakt jest loadable, ponieważ eksperyment nigdy nie dotarł do loadera.**

To nie jest porażka systemu dowodowego.

To właśnie moment, w którym system dowodowy zadziałał.

<div class="lab-archive"><strong>Status źródłowy:</strong> artykuł opisuje zweryfikowany milestone inżynieryjny z prywatnego archiwum D-LOGIC. Pełne receipts, commity i hashe pozostają w archiwum operacyjnym; publicznie ujawniono wyłącznie liczby oraz wnioski dopuszczone przez claim check.</div>
