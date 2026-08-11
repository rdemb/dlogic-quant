---
layout: labpost
title: "Najbezpieczniejszy filtr potrafi unieważnić własny eksperyment"
description: "WP10 zamknął najważniejsze luki przenośnego control plane, ale niezależny audyt wykazał, że globalna polityka nazw nie potrafi opisać środowiska, które miała bezpiecznie zmierzyć."
dek: "Pakiet przeszedł kontrolę integralności, statyczny przegląd i odtwarzalny korpus mutacji. Instalacja nadal pozostała zabroniona, ponieważ model zaufania pomylił aktywne środowisko z sekretami z jego jednorazową, odizolowaną kopią."
date: 2026-08-11 19:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #03"
readingTime: 13
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #03"
cover_title: "FILTR ZABLOKOWAŁ DOWÓD"
cover_subtitle: "STATIC PASS · HOST TREE BLOCKED · LIVE FALSE"
cover_kind: lifecycle
---
<div class="article-status"><span class="primary">ENGINEERING MILESTONE</span><span>WP10: STATIC PASS</span><span>HOST TREE: BLOCKED</span><span>EXECUTION: DISABLED</span><span>LIVE: NOT AUTHORIZED</span></div>

Najbardziej interesujący błąd w systemie bezpieczeństwa nie musi otwierać drzwi napastnikowi. Czasem zamyka je tak szczelnie, że legalny eksperyment nie potrafi nawet opisać środowiska, które miał zbadać.

Tak zakończył się Work Package 10 w D-LOGIC. Pakiet był wyraźnym postępem. Po raz pierwszy przenośna warstwa kontrolna tworzyła spójny, niezależnie odtwarzalny obiekt dowodowy, a nie zbiór luźnych bibliotek i deklaracji. Zamknięto istotne luki w ścieżce pomiędzy jednostką uruchomieniową, interfejsem programu, biblioteką, poświadczeniami, pracownikiem i wynikiem. Do archiwum dołączono także korpus negatywnych przypadków, dzięki któremu zewnętrzny recenzent mógł sprawdzić nie tylko scenariusz poprawny, ale również próby obejścia kontraktu.

Mimo tego prawidłowy wynik brzmiał:

```text
PASS_PORTABLE_STATIC_CONTROL_PLANE_PREFLIGHT
HOST_RUNTIME_TREE_TARGET_REPRESENTABLE = FALSE
SAFE_TO_INSTALL = FALSE
SAFE_TO_EXECUTE = FALSE
```

Nie jest to sprzeczność. Pierwsze zdanie dotyczy jakości przenośnego pakietu i statycznego modelu sterowania. Drugie mówi, że polityka pomiaru środowiska hosta nie potrafiła przedstawić naturalnej struktury jednorazowego runtime'u, który miała później poświadczyć. Sukces jednej warstwy odsłonił błąd warstwy następnej.

## Co faktycznie dostarczył WP10

Pakiet został zbudowany jako kanoniczne archiwum z deterministyczną topologią i ograniczonymi trybami plików. Niezależny audyt odtworzył jego integralność bez polegania na aktywnym środowisku VPS.

| Kontrola | Wynik |
|---|---:|
| Elementy archiwum | 54 |
| Zwykłe pliki | 48 |
| Katalogi | 6 |
| Manifest pakietu | 47/47 PASS |
| Dokumenty JSON | 30/30 PASS |
| Tożsamości paczek | 3/3 PASS |
| Przypadki mutacyjne | 17 PASS |
| Dowiązania, urządzenia, FIFO, path traversal | 0 |

Te liczby nie dowodzą gotowości tradingowej. Dowodzą czegoś węższego i nadal wartościowego: dostarczony obiekt był spójny, możliwy do niezależnego sprawdzenia i zawierał własny materiał do testowania odporności kontraktu.

Pakiet poprawił również poprzednią generację w kilku punktach:

1. Wiązał pełną ścieżkę wejścia, a nie wyłącznie pierwszy plik wykonywalny.
2. Wymagał przyjęcia określonych poświadczeń przed dotarciem do twardo wyłączonej granicy wykonania.
3. Rozwiązywał tożsamość artefaktów dowodowych zamiast akceptować dowolny tekst przypominający hash.
4. Łączył czas wyniku z modelem autorytetu czasu.
5. Odtwarzał przypadki negatywne bez potrzeby dostępu do aktywnego terminala, rachunku albo brokera.

Był to zatem najlepszy dotąd przenośny dowód jakości control plane. Nie był to dowód, że pakiet można zainstalować na hoście, załadować do runtime'u lub użyć do jakiegokolwiek działania rynkowego.

<figure>
<svg viewBox="0 0 1040 380" role="img" aria-labelledby="wp10-stack-title wp10-stack-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="wp10-stack-title">Trzy poziomy dowodu WP10</title>
  <desc id="wp10-stack-desc">Pakiet i statyczny control plane przeszły weryfikację. Pomiar drzewa hosta został zablokowany przed instalacją i wykonaniem.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="54" y="70" width="270" height="220" rx="22" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="385" y="70" width="270" height="220" rx="22" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="716" y="70" width="270" height="220" rx="22" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="189" y="112" text-anchor="middle" font-size="20" fill="var(--ink)">PAKIET</text>
    <text x="520" y="112" text-anchor="middle" font-size="20" fill="var(--ink)">CONTROL PLANE</text>
    <text x="851" y="112" text-anchor="middle" font-size="20" fill="var(--ink)">HOST RUNTIME</text>
    <text x="189" y="151" text-anchor="middle" font-size="15" fill="var(--up)">INTEGRITY PASS</text>
    <text x="189" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">manifest, tożsamości,</text>
    <text x="189" y="205" text-anchor="middle" font-size="14" fill="var(--mut)">topologia, mutacje</text>
    <text x="520" y="151" text-anchor="middle" font-size="15" fill="var(--up)">STATIC PASS</text>
    <text x="520" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">wejścia, poświadczenia,</text>
    <text x="520" y="205" text-anchor="middle" font-size="14" fill="var(--mut)">wynik, czas, kolejność</text>
    <text x="851" y="151" text-anchor="middle" font-size="15" fill="var(--dn)">TARGET BLOCKED</text>
    <text x="851" y="181" text-anchor="middle" font-size="14" fill="var(--mut)">polityka nie reprezentuje</text>
    <text x="851" y="205" text-anchor="middle" font-size="14" fill="var(--mut)">naturalnego drzewa runtime'u</text>
    <path d="M324 180 H385 M655 180 H716" stroke="var(--line)" stroke-width="3"/>
    <circle cx="354" cy="180" r="10" fill="var(--up)"/>
    <circle cx="685" cy="180" r="10" fill="var(--dn)"/>
    <text x="520" y="340" text-anchor="middle" font-size="16" fill="var(--mut)">PASS niższej warstwy nie nadaje automatycznie prawa do instalacji następnej.</text>
  </g>
</svg>
<figcaption>WP10 zamknął pakiet i statyczny control plane. Granica przesunęła się do modelu pomiaru środowiska hosta.</figcaption>
</figure>

## Błąd nie znajdował się w archiwum

Raport końcowy prawidłowo zatrzymał się na wyniku `INCONCLUSIVE_READONLY_HOST_MEASUREMENT`. Nie podano dokładnie ograniczonych korzeni drzewa hosta, więc pakiet nie próbował zgadywać, gdzie znajduje się właściwe środowisko.

Niezależny przegląd źródła wykazał jednak problem głębszy. Nawet po dostarczeniu poprawnych korzeni bieżąca polityka nie mogłaby zmierzyć całego środowiska. Globalny filtr nazw uznawał standardowe elementy jednorazowej instalacji terminala i warstwy zgodności za zabronione niezależnie od ich roli.

W uproszczeniu kontrakt zachowywał się tak:

```text
jeżeli nazwa przypomina aktywny runtime:
    odrzuć
```

Taka reguła dobrze brzmi jako ochrona przed przypadkowym wejściem do środowiska zawierającego rachunek, profile i sekrety. Problem powstaje wtedy, gdy ten sam zbiór nazw jest niezbędny w czystej, jednorazowej kopii przeznaczonej właśnie do pomiaru.

Wynik można zapisać prosto:

```text
PolicyAdmits(DisposableRuntime) = false
```

System bezpieczeństwa nie rozróżniał dwóch obiektów o podobnej strukturze nazw:

- aktywnego środowiska, którego nie wolno dotknąć;
- odizolowanej kopii bez sekretów, którą trzeba zmierzyć dokładnie.

## Dlaczego zmiana nazw byłaby fałszywym rozwiązaniem

Pierwszym odruchem mogłoby być skopiowanie plików do katalogów o neutralnych nazwach. Filtr przestałby protestować, a pomiar technicznie doszedłby do końca.

Taki wynik miałby jednak słabą wartość dowodową. System mierzyłby zmodyfikowany odpowiednik, a nie dokładne środowisko późniejszego uruchomienia. Nazwy i położenie plików mogą wpływać na odnajdywanie zasobów, konfigurację, względne ścieżki oraz zachowanie loadera. Nie wolno deklarować zgodności konkretnego runtime'u na podstawie drzewa, które zostało przebudowane wyłącznie po to, aby przejść walidator.

W atestacji liczy się tożsamość obiektu razem z jego istotnym kontekstem. Jeżeli kontekst zostaje zmieniony przed pomiarem, dowód opisuje już inny obiekt.

<div class="lab-note"><strong>Niedozwolony skrót:</strong> filtr przepuścił kopię po zmianie nazw, więc oryginalne środowisko zostało poświadczone.</div>

## Zaufanie powinno zależeć od roli

Poprawka nie polega na usunięciu zabezpieczeń. Wymaga zastąpienia globalnego zakazu modelem, który rozpoznaje rolę każdego korzenia drzewa.

Publicznie można opisać ten podział bez ujawniania prywatnej topologii:

| Rola korzenia | Polityka |
|---|---|
| Aktywne profile i dane rachunku | Zawsze zabronione |
| Aktywne środowisko terminala | Zabronione bez osobnej, przyszłej autoryzacji |
| Jednorazowy runtime bez sekretów | Pomiar wyłącznie odczytowy |
| Jednorazowa warstwa zgodności | Pomiar wyłącznie odczytowy |
| Narzędzia i control plane | Pomiar wyłącznie odczytowy |
| Wyjście dowodowe | Oddzielony zapis, bez nakładania się z wejściem |

Ta zmiana pozwala zadać właściwe pytanie. Nie brzmi ono: „Czy nazwa katalogu wygląda groźnie?”. Brzmi: „Jaką rolę pełni ten konkretny korzeń, kto go utworzył, czy jest jednorazowy, czy zawiera sekrety, czy nakłada się z aktywnym środowiskiem i czy można go zmierzyć bez mutacji?”.

<figure>
<svg viewBox="0 0 1040 500" role="img" aria-labelledby="trust-title trust-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="trust-title">Globalny filtr nazw i model zaufania oparty na roli</title>
  <desc id="trust-desc">Po lewej jeden zakaz odrzuca aktywne oraz jednorazowe środowisko. Po prawej rola rozdziela środowisko aktywne od odizolowanej kopii pomiarowej.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="40" y="54" width="440" height="382" rx="24" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <rect x="560" y="54" width="440" height="382" rx="24" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="260" y="95" text-anchor="middle" font-size="21" fill="var(--dn)">GLOBALNY FILTR NAZW</text>
    <text x="780" y="95" text-anchor="middle" font-size="21" fill="var(--up)">POLITYKA OPARTA NA ROLI</text>

    <rect x="90" y="130" width="340" height="76" rx="14" fill="none" stroke="var(--line)" stroke-width="2"/>
    <rect x="90" y="246" width="340" height="76" rx="14" fill="none" stroke="var(--line)" stroke-width="2"/>
    <text x="260" y="162" text-anchor="middle" font-size="16" fill="var(--ink)">AKTYWNE ŚRODOWISKO</text>
    <text x="260" y="187" text-anchor="middle" font-size="14" fill="var(--dn)">ODRZUCONE</text>
    <text x="260" y="278" text-anchor="middle" font-size="16" fill="var(--ink)">JEDNORAZOWA KOPIA</text>
    <text x="260" y="303" text-anchor="middle" font-size="14" fill="var(--dn)">TAKŻE ODRZUCONA</text>
    <text x="260" y="377" text-anchor="middle" font-size="15" fill="var(--mut)">Ta sama nazwa daje ten sam werdykt.</text>

    <rect x="610" y="130" width="340" height="76" rx="14" fill="none" stroke="var(--dn)" stroke-width="2"/>
    <rect x="610" y="246" width="340" height="76" rx="14" fill="none" stroke="var(--up)" stroke-width="2"/>
    <text x="780" y="162" text-anchor="middle" font-size="16" fill="var(--ink)">AKTYWNE + SEKRETY</text>
    <text x="780" y="187" text-anchor="middle" font-size="14" fill="var(--dn)">ZABRONIONE</text>
    <text x="780" y="278" text-anchor="middle" font-size="16" fill="var(--ink)">JEDNORAZOWE + BEZ SEKRETÓW</text>
    <text x="780" y="303" text-anchor="middle" font-size="14" fill="var(--up)">MIERZALNE READ-ONLY</text>
    <text x="780" y="377" text-anchor="middle" font-size="15" fill="var(--mut)">Rola, pochodzenie i izolacja wyznaczają werdykt.</text>
  </g>
</svg>
<figcaption>Bezpieczeństwo oparte wyłącznie na nazwie nie rozpoznaje kontekstu. Model roli zachowuje twardy zakaz wobec aktywnych sekretów, ale pozwala mierzyć ich odizolowany, jednorazowy odpowiednik.</figcaption>
</figure>

## Fail-closed nie oznacza, że polityka zawsze ma rację

D-LOGIC stosuje zasadę fail-closed. Brak pełnego dowodu zatrzymuje promocję, instalację albo wykonanie. W tym przypadku zasada zadziałała poprawnie, ponieważ błędny model zaufania nie został zamieniony w wygodne `PASS`.

Warto jednak oddzielić dwie rzeczy:

- mechanizm zatrzymania;
- poprawność reguły, która wywołała zatrzymanie.

Mechanizm może działać idealnie, a sama polityka może być zbyt szeroka, źle sformułowana albo niespójna z obiektem, który ma kontrolować. Dobry system nie broni reguł przed krytyką tylko dlatego, że są restrykcyjne. Wymaga, aby restrykcja miała jasny model zagrożenia i nie niszczyła możliwości uzyskania dowodu.

W tym sensie WP10 osiągnął coś ważniejszego od kolejnego zielonego pola. Zbudował wystarczająco precyzyjną powierzchnię przeglądu, aby niezależny audyt mógł wykryć sprzeczność pomiędzy celem pomiaru a polityką dopuszczenia.

## Co powinien zamknąć WP11

Następna wersja kontraktu ma wprowadzić jawne role korzeni i wersjonowaną politykę zaufania. Jednorazowe środowisko będzie mogło zachować naturalną strukturę plików, ale wyłącznie po spełnieniu twardych warunków:

1. Powstaje w nowym albo pustym, prywatnym katalogu.
2. Nie nakłada się z aktywnym terminalem, profilem ani danymi rachunku.
3. Nie zawiera poświadczeń, kluczy, baz logowania ani materiału konta.
4. Jest mierzone bez zapisu do wejściowego drzewa.
5. Dowiązania, aliasy, nakładanie korzeni i ucieczka ścieżki są odrzucane.
6. Obiekt zabroniony pozostaje zabroniony także po odnalezieniu przez inną nazwę lub alias.
7. Wynik pomiaru trafia do osobnej powierzchni dowodowej.

Dopiero po zamknięciu tego kontraktu można wrócić do pytania o zgodność runtime'u i zachowanie prawdziwego managera usług. Nadal nie będzie to dowód jakości danych, modelu ani przewagi.

## Co wiadomo po WP10

| Własność | Stan |
|---|---|
| Integralność pakietu | PASS |
| Przenośny przegląd statyczny | PASS |
| Odtworzenie mutacji | PASS |
| Statyczna ścieżka wejścia i poświadczeń | PASS |
| Pomiar dokładnego drzewa hosta | NIE WYKONANO |
| Możliwość przedstawienia celu przez politykę V4 | FALSE |
| Akceptacja przez rzeczywisty manager usług | UNKNOWN |
| Loadability runtime'u | UNKNOWN |
| Canary | FALSE |
| Dane zwalidowane | FALSE |
| Przewaga modelu | FALSE |
| Forward edge | FALSE |
| Risk Governor | FALSE |
| Zgoda na LIVE | FALSE |

Status `FALSE` przy gotowości live nie odbiera wartości pracy inżynieryjnej. Chroni znaczenie słowa „gotowy”.

## Ta sama pomyłka występuje w badaniach rynku

Problem nazwy i roli ma odpowiednik w analizie finansowej. Ta sama zmienna może być legalną cechą w jednym momencie decyzyjnym i leakage w innym. Ten sam instrument może być celem egzekucji, sensorem rynku albo jedynie duplikatem informacji. Ta sama obserwacja może być dopuszczalna w badaniu retrospektywnym i niedostępna w czasie rzeczywistym.

Globalna reguła pozbawiona kontekstu często daje prosty kod, ale słaby model rzeczywistości. Dlatego architektura D-LOGIC coraz częściej opisuje obiekty przez rolę, czas dostępności, pochodzenie i uprawnienia zamiast przez samą nazwę.

Filtr bezpieczeństwa nauczył system tej samej lekcji, którą wcześniej przynosiły dane rynkowe: klasyfikacja bez kontekstu potrafi być formalnie spójna i praktycznie błędna.

## Publiczny werdykt

WP10 jest realnym sukcesem control plane. Zamknął znaczną część wcześniejszych problemów, stworzył niezależnie odtwarzalny pakiet i przesunął granicę niewiedzy do precyzyjnie określonego kontraktu hosta.

Nie uruchomiono X, Wine, terminala ani artefaktu tradingowego. Nie dotknięto rachunku, brokera, danych rynkowych ani zleceń. Nie wykonano instalacji. Nie udowodniono loadability, canary, jakości danych, przewagi ani gotowości live.

Właściwym wynikiem nie było osłabienie filtra ani ręczne nadanie wyjątku. Właściwym wynikiem było rozpoznanie, że bezpieczeństwo musi modelować rolę i kontekst równie precyzyjnie jak tożsamość pliku.

Dobrze zaprojektowany system nie tylko odrzuca niebezpieczne działania. Potrafi też wykazać, kiedy własna reguła bezpieczeństwa przestała opisywać świat, który miała chronić.

<div class="lab-note"><strong>Stan po publikacji:</strong> pakiet statyczny zaakceptowany, pomiar hosta niegotowy, wykonanie wyłączone, LIVE nieautoryzowane.</div>


## Podstawa dowodowa

Tekst powstał na podstawie zweryfikowanych materiałów projektu z 11 sierpnia 2026 roku:

- raportu niezależnego `D-LOGIC Audit Reconciliation 10`;
- raportu zamknięcia WP10;
- dostarczonego receiptu i kanonicznego archiwum;
- aktualnego katalogu komponentów oraz kroniki architektury.

Prywatne lokalizacje, pełne kontrakty, kod, dane autoryzacyjne i topologia hosta nie są publikowane.
