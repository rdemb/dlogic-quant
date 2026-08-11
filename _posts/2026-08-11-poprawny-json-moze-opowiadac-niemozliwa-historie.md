---
layout: labpost
title: "Poprawny JSON może opowiadać niemożliwą historię"
description: "Dlaczego podpis, poprawny schemat i zielony walidator nadal nie wystarczają, jeżeli dowód nie zgadza się z przebiegiem zdarzeń."
dek: "Walidator zaakceptował wynik LOADABLE, chociaż wszystkie fazy runtime były oznaczone jako niewykonane albo zablokowane. Format był poprawny. Znaczenie - niemożliwe."
date: 2026-08-11 11:00:00 +0200
category: research
eyebrow: "D-LOGIC Research Note #01"
readingTime: 11
section_url: /research/
section_label: Research
cover_brand: "D-LOGIC RESEARCH NOTE #01"
cover_title: "POPRAWNY FORMAT. ZŁY SENS."
cover_subtitle: "CRYPTOGRAPHY · SCHEMA · SEMANTICS · CAUSAL PROOF"
cover_kind: evidence
---
<div class="article-status"><span class="primary">RESEARCH NOTE</span><span>NON-EXECUTING</span><span>SEMANTIC BLOCKER</span><span>LOADABLE: UNKNOWN</span><span>LIVE: NOT AUTHORIZED</span></div>

Dokument wyglądał wiarygodnie. Miał prawidłową strukturę, pola o oczekiwanych nazwach, wartości zgodne z typami i ciągi znaków przypominające poprawne hashe. Walidator potrafił go odczytać, a wynik końcowy mówił `PASS`. Według tego samego dokumentu cykl życia komponentu miał już osiągnąć stan `LOADABLE`.

Wystarczył jednak jeden test sprzeczności, aby cała historia przestała mieć sens.

Wszystkie fazy runtime były oznaczone jako `NOT_RUN` albo `BLOCKED`. Wpisano niewłaściwy sentinel dziennika, powtórzono identyfikatory faz, a część timestampów biegła w odwrotnej kolejności. Mimo tego agregat pozostawał zielony.

JSON był poprawny.

Opisywane zdarzenie było niemożliwe.

Ten przypadek doprowadził w D-LOGIC do rozróżnienia, które wykracza poza pojedynczy walidator i dotyczy praktycznie każdego systemu opartego na automatycznych dowodach, podpisach, manifestach oraz wynikach generowanych przez wiele warstw:

> **Poprawność formatu nie jest tym samym co spójność dowodu, a spójność dowodu nie jest jeszcze kompletnością jego przyczynowej historii.**

## Cztery poziomy zaufania

Wiele systemów bezpieczeństwa kończy analizę na dwóch pytaniach. Czy bajty zostały podpisane przez właściwy klucz? Czy dokument spełnia schemat?

Oba są konieczne, ale nie wystarczają.

<figure>
<svg viewBox="0 0 900 470" role="img" aria-labelledby="layers-title layers-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="layers-title">Cztery poziomy zaufania do dowodu</title>
  <desc id="layers-desc">Od podpisanych bajtów przez schemat i spójność semantyczną do kompletności przyczynowej.</desc>
  <rect x="115" y="42" width="670" height="72" rx="14" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
  <rect x="145" y="140" width="610" height="72" rx="14" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
  <rect x="175" y="238" width="550" height="72" rx="14" fill="var(--soft)" stroke="#c18400" stroke-width="3"/>
  <rect x="205" y="336" width="490" height="72" rx="14" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
  <text x="450" y="75" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="19" font-weight="700" fill="var(--ink)">1. Integralność kryptograficzna</text>
  <text x="450" y="98" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">Czy to dokładnie te bajty i czy podpisał je właściwy podmiot?</text>
  <text x="450" y="173" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="19" font-weight="700" fill="var(--ink)">2. Poprawność składniowa</text>
  <text x="450" y="196" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">Czy dokument ma wymagane pola, typy i dozwolone wartości?</text>
  <text x="450" y="271" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="19" font-weight="700" fill="var(--ink)">3. Spójność semantyczna</text>
  <text x="450" y="294" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">Czy wszystkie twierdzenia mogą być jednocześnie prawdziwe?</text>
  <text x="450" y="369" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="19" font-weight="700" fill="var(--ink)">4. Kompletność przyczynowa</text>
  <text x="450" y="392" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">Czy dowód obejmuje całą drogę od intencji do skutku?</text>
  <path d="M450 114 V136 M450 212 V234 M450 310 V332" stroke="var(--mut)" stroke-width="2" stroke-dasharray="5 5"/>
</svg>
<figcaption>Podpis i schemat chronią formę. Dopiero dwie kolejne warstwy chronią znaczenie oraz zgodność z realnym przebiegiem działania.</figcaption>
</figure>

### 1. Integralność kryptograficzna

Podpis może dowodzić, że określone bajty zostały zatwierdzone przez posiadacza konkretnego klucza i nie uległy zmianie. Nie odpowiada jednak na pytanie, czy osoba podpisująca powinna była zaakceptować ich znaczenie ani czy opisane działanie jest bezpieczne.

Można poprawnie podpisać dokument zawierający logiczną sprzeczność. Kryptografia wiernie chroni wówczas sprzeczność przed modyfikacją.

### 2. Poprawność składniowa

Schemat sprawdza, czy istnieją wymagane pola, czy liczba jest liczbą, status należy do dozwolonego zbioru, a identyfikator ma oczekiwany format. Dzięki temu usuwa całe klasy błędów i powinien być traktowany jako obowiązkowy element infrastruktury dowodowej.

Schemat nie rozumie jednak automatycznie relacji między polami. Może zaakceptować `aggregate_status=PASS` oraz pięć faz `NOT_RUN`, jeżeli każde z tych pól oddzielnie jest legalne.

### 3. Spójność semantyczna

Ta warstwa pyta, czy dokument opisuje możliwy stan świata. Jeżeli komponent ma zostać uznany za loadable, odpowiednie fazy muszą rzeczywiście dojść do punktu załadowania. Jeżeli raport twierdzi, że wykryto sentinel w logu, sentinel powinien zostać wyprowadzony z tego samego, rozwiązanego obiektu logu, a nie przyjęty jako niezależny tekst dostarczony przez autora wyniku.

Status końcowy nie może być osobną opinią pliku. Powinien być **wyliczony** z dowodów niższego poziomu.

### 4. Kompletność przyczynowa

Nawet wewnętrznie spójny raport może być niepełny, jeżeli jego model świata pomija fragment rzeczywistej ścieżki działania. Można zbudować doskonałą listę kontrolną, według której pozostał jeden blocker, podczas gdy poza słownikiem checklisty istnieją inne obowiązki, których nikt jeszcze nie nazwał.

W kolejnym przeglądzie D-LOGIC pojawił się właśnie taki problem. W zamrożonym modelu zamknięcia środowiska jeden element był oznaczony jako nierozstrzygnięty. Niezależna analiza pełnej ścieżki odkryła jednak, że jednostka systemowa przekazywała argument odrzucany przez własny program, warstwa uruchomieniowa nie dochodziła do zweryfikowanych bibliotek, przekazanie poświadczeń nie było zrealizowane, a pola przypominające hashe nie musiały prowadzić do istniejących obiektów dowodowych.

Lista była poprawna wewnątrz własnego języka. Problem polegał na tym, że język nie obejmował całej czynności.

## Hash nie jest dowodem tylko dlatego, że wygląda jak hash

Ciąg sześćdziesięciu czterech znaków szesnastkowych może mieć kształt SHA-256, ale sam kształt nie dowodzi istnienia pliku, jego niezmienności ani związku z opisywanym eksperymentem.

Aby identyfikator stał się dowodem, potrzebny jest resolver, który potrafi:

- odnaleźć dokładny, niezmienny obiekt,
- sprawdzić jego rozmiar i hash,
- potwierdzić rolę w konkretnym przebiegu,
- związać go z fazą, czasem oraz kontekstem,
- odrzucić brakujące, zduplikowane i pochodzące z innego przebiegu artefakty.

Dopiero wtedy komunikat „log ma taki hash” można przekształcić w twierdzenie „ten dokładny log był podstawą tego dokładnego wyniku”.

Podobny problem występuje w researchu rynkowym. Nazwa pliku `final_dataset_v7_clean.parquet` nie dowodzi, że dane są point-in-time, wolne od survivorship bias ani dostępne w momencie decyzji. Obecność kolumny `timestamp` nie mówi jeszcze, czy oznacza czas zdarzenia, odbioru, przetworzenia czy późniejszej rewizji.

Etykieta i format są początkiem audytu, nie jego końcem.

## Zamknięta checklista może być perfekcyjnie niekompletna

Najbardziej niebezpieczne listy kontrolne nie są oczywiście błędne. Są precyzyjne, konsekwentne i dobrze testowane, ale nie reprezentują wszystkich istotnych zależności.

Można to przedstawić jako dwa różne rodzaje zamknięcia:

**zamknięcie słownikowe** - wszystkie pola, które istnieją w aktualnym modelu, mają określony status;

**zamknięcie przyczynowe** - każda konieczna część realnej ścieżki od intencji do działania i dowodu jest reprezentowana, połączona oraz sprawdzona.

<figure>
<svg viewBox="0 0 940 360" role="img" aria-labelledby="closure-title closure-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="closure-title">Zamknięta checklista i pominięta ścieżka przyczynowa</title>
  <desc id="closure-desc">Wewnątrz modelu pozostał jeden blocker, ale poza modelem znajdują się pominięte obowiązki dowodowe.</desc>
  <rect x="76" y="48" width="420" height="252" rx="20" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
  <text x="286" y="82" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="19" font-weight="700" fill="var(--ink)">ZAMKNIĘTY MODEL</text>
  <circle cx="150" cy="140" r="17" fill="var(--up)"/><circle cx="235" cy="140" r="17" fill="var(--up)"/><circle cx="320" cy="140" r="17" fill="var(--up)"/><circle cx="405" cy="140" r="17" fill="var(--dn)"/>
  <path d="M142 140 l6 6 12-15 M227 140 l6 6 12-15 M312 140 l6 6 12-15" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M397 132 l16 16 M413 132 l-16 16" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  <text x="286" y="206" text-anchor="middle" font-family="ui-monospace,Consolas,monospace" font-size="17" fill="var(--ink)">„JEDEN BLOCKER”</text>
  <text x="286" y="240" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">prawda wewnątrz obecnego słownika</text>
  <circle cx="650" cy="78" r="14" fill="#c18400"/><circle cx="782" cy="122" r="14" fill="#c18400"/><circle cx="624" cy="206" r="14" fill="#c18400"/><circle cx="805" cy="254" r="14" fill="#c18400"/><circle cx="706" cy="310" r="14" fill="#c18400"/>
  <path d="M496 126 C560 102 586 86 636 80 M496 170 C600 160 696 136 768 124 M496 210 C548 208 576 207 610 206 M496 244 C620 246 712 252 791 254 M496 274 C580 302 628 310 692 310" stroke="var(--mut)" stroke-width="2" stroke-dasharray="6 6" fill="none"/>
  <text x="704" y="28" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="18" font-weight="700" fill="var(--ink)">POMINIĘTE OBOWIĄZKI</text>
  <text x="704" y="344" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,sans-serif" font-size="13" fill="var(--mut)">brakujące węzły nie mogą stać się blockerami, dopóki model ich nie reprezentuje</text>
</svg>
<figcaption>Kompletność modelu należy oceniać względem realnej ścieżki działania, a nie tylko względem pól, które wcześniej zdecydowaliśmy się zapisać.</figcaption>
</figure>

## Quant ma dokładnie ten sam problem

Systemy badawcze potrafią być wewnętrznie poprawne i jednocześnie niekompletne wobec mechanizmu rynku.

Model czynnikowy może wykazać residual alpha, ponieważ istotna wspólna ekspozycja nie znalazła się w jego słowniku. Portfel siedmiuset instrumentów może wyglądać na zdywersyfikowany, jeżeli mierzymy liczbę symboli, ale nie reprezentujemy jednego czynnika płynnościowego łączącego większość pozycji. Backtest może przejść wszystkie zakodowane zasady, chociaż koszty wykonania zostały całkowicie pominięte. Target może być obliczony prawidłowo, ale korzystać z informacji, która stała się znana dopiero po decyzji.

W każdym przypadku system może uczciwie raportować:

> „Wszystkie znane mi warunki zostały spełnione”.

Najważniejsze pytanie brzmi jednak:

> „Czy znałeś wszystkie warunki konieczne do uzasadnienia twierdzenia?”

To pytanie jest niewygodne, ponieważ nie ma skończonej odpowiedzi. Nie da się udowodnić absolutnej kompletności modelu rzeczywistości. Można natomiast systematycznie zmniejszać ryzyko pominięcia poprzez analizę pełnej ścieżki przyczynowej, red-team, kontrprzykłady, niezależne implementacje i celowe mutacje dowodów.

## Evidence-carrying action

Jednym z kierunków, które wynikły z tego etapu, jest traktowanie bezpiecznej czynności nie jako samego polecenia, ale jako obiektu niosącego własne warunki oraz wymagany dowód.

Na poziomie publicznym można opisać tę ideę następująco:

1. intencja jest precyzyjnie typowana i ograniczona do jednego rodzaju działania;
2. konkretne artefakty oraz kontekst są przypięte przed autoryzacją;
3. czynność może zostać wykorzystana tylko raz;
4. każda faza zwraca określony rodzaj dowodu;
5. status końcowy jest wyprowadzany z rozwiązanych artefaktów, a nie deklarowany niezależnie;
6. brak, sprzeczność albo niewłaściwy kontekst powodują twarde zatrzymanie.

Nie publikuję dokładnego protokołu, grafu stanów, sposobu przekazywania poświadczeń ani prywatnej topologii wykonawczej. Wartością publiczną jest zasada: **autoryzacja powinna obejmować nie tylko to, co wolno zrobić, ale również to, jak później udowodnimy, że wykonano dokładnie tę czynność i nic więcej**.

## Dlaczego nie jest to przesadna biurokracja

Na małej skali łatwiej zaufać logowi, plikowi i własnej pamięci. W systemie rozwijanym przez wiele agentów, narzędzi i iteracji pojawia się jednak problem kompozycji. Każda warstwa może być lokalnie poprawna, a mimo to cała ścieżka pozostaje przerwana albo niejednoznaczna.

Agent generuje pakiet. Inny proces waliduje schemat. Kolejna warstwa podpisuje request. Runtime tworzy log. Parser wyciąga sentinel. Agregator przypisuje status. Jeśli choć jedno z tych przejść nie jest związane z dokładnym artefaktem i kontekstem, końcowy wynik może wyglądać profesjonalnie, choć nie opisuje realnego przebiegu.

To samo dotyczy modeli quant. Pipeline może prawidłowo wykonywać wszystkie funkcje, a jednak łączyć feature z niewłaściwym czasem, target z niemożliwą ceną wykonania lub wynik ze zużytym holdoutem. Im bardziej zautomatyzowany jest system, tym mniejsza jest szansa, że człowiek przypadkiem zauważy sprzeczność na ekranie.

Automatyzacja nie zmniejsza potrzeby dowodu. Zwiększa wymagania wobec jego struktury.

## Zielony wynik powinien być konsekwencją, nie polem do wypełnienia

Najważniejsza zmiana architektoniczna wynikająca z tego doświadczenia jest prosta do opisania:

> status najwyższego poziomu nie powinien być przyjmowany jako niezależna wartość, jeżeli może zostać jednoznacznie wyprowadzony z dowodów niższego poziomu.

`LOADABLE` powinno wynikać z konkretnych faz, właściwego logu, prawidłowego sentinela, braku błędów loadera, zgodności kontekstu i zaufanego czasu. `DATA_VALIDATED` powinno wynikać z testów dokładnego podzbioru danych, nie z ogólnej reputacji źródła. `MODEL_EDGE_PROVEN` musi być konsekwencją właściwej walidacji, kosztów i niezależnego wyniku, a nie wartością ustawianą przez proces, który właśnie zakończył trening.

Im mniej swobody ma system w opowiadaniu własnego sukcesu, tym większa szansa, że jego zielony status będzie znaczył coś poza samym plikiem.

Poprawny JSON może opowiadać niemożliwą historię.

Dobry system dowodowy musi więc sprawdzać nie tylko, czy dokument daje się odczytać, ale także czy opisany świat mógł istnieć, czy wskazane artefakty istnieją naprawdę oraz czy model obejmuje pełną drogę od intencji do skutku.

Dopiero wtedy format zaczyna nieść znaczenie.

<div class="lab-archive"><strong>Status źródłowy:</strong> tekst łączy dwa zweryfikowane przeglądy statycznej infrastruktury D-LOGIC. Nie doszło do instalacji, wykonania, kontaktu z terminalem, brokerem ani rynkiem. Opisane zasady są publiczną syntezą; szczegółowy protokół autoryzacji i topologia runtime’u pozostają prywatne.</div>
