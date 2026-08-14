---
layout: labpost
title: "340 prób później. Hash zaczął prowadzić do dowodu"
description: "WP13 zamknął konkretny blocker WP12: każdy obowiązkowy identyfikator dowodowy w syntetycznym pakiecie rozwiązuje się do uwierzytelnionego obiektu, a fałszywe substytucje failują zamknięte."
dek: "Dobry następca nie powinien tylko dodawać testów. Powinien sprawić, aby dokładnie ten błąd, który wcześniej przeszedł, stał się niemożliwy do zaakceptowania tą samą ścieżką."
date: 2026-08-14 07:30:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #06"
readingTime: 13
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #06"
cover_title: "HASH ZACZĄŁ PROWADZIĆ DO DOWODU"
cover_subtitle: "WP13 ACCEPTED / 340 MUTATIONS / RUNTIME STILL UNKNOWN"
cover_kind: evidence
---
<div class="article-status"><span class="primary">WP13 ACCEPTED</span><span>340/340 MUTATIONS</span><span>EVIDENCE OBJECT CLOSURE: PASS</span><span>REAL RUNTIME: NOT TESTED</span></div>

WP12 zakończył się wynikiem, który trudno byłoby wymyślić jako lepszy test uczciwości całego programu. Trzydzieści kontroli przechodziło, archiwum było odtwarzalne, a resolver potrafił jednocześnie zaakceptować obowiązkowe hashe, które nie prowadziły do żadnego istniejącego obiektu. Błąd został opisany precyzyjnie, zamrożony w maszynowym receipt i przekazany do kolejnego work package bez zmiany jego znaczenia.

WP13 miał jedno główne zadanie: sprawić, aby `EvidenceResolved` oznaczało rzeczywiście rozwiązany dowód.

Niezależny audyt potwierdził wykonanie tego zakresu na poziomie kontrolowanego pakietu syntetycznego. Raw archive replay zwrócił `PASS_WP13_DIRECT_ARCHIVE_REPLAY`, a pełny korpus obejmował 340 mutacji resolvera, dwie kontrole komponentowe i trzy predykaty statyczne. Wszystkie przeszły bez importowania repozytorium, bez uruchamiania runtime'u i bez dostępu do sieci.

Wynik jest mocny, ponieważ odpowiada bezpośrednio na wcześniejszy kontrprzykład. Identyfikatory trzydziestu czterech obowiązkowych węzłów prowadzą teraz do uwierzytelnionych obiektów zawartych w paczce albo do typowanych syntetycznych receipts, a podmiany na poprawnie wyglądające, ale nieistniejące hashe failują zamknięte.

## Co zostało niezależnie odtworzone

Dostarczone archiwum zawierało 88 elementów, w tym 78 plików i 10 katalogów. Kontrole canonical gzip i USTAR przeszły. Zewnętrzny replay działał wyłącznie na bajtach paczki, nie importował repozytorium i nie wykonywał żadnego kodu badanego runtime'u.

| Kontrola | Wynik |
|---|---:|
| Mandatory semantic nodes | 34 |
| Evidence objects | 34 |
| Full-resolver mutations | 340/340 PASS |
| Component checks | 2/2 PASS |
| Static predicates | 3/3 PASS |
| Unsafe archive members | 0 |
| Runtime execution | 0 |
| Repository import | 0 |

Niezależna inspekcja potwierdziła zgodność hashy, rozmiarów i trybów plików, content-addressed identities, zamknięte zależności oraz acykliczny graf dependency. Dodatkowo replay przeszedł pod harnessami odmawiającymi tworzenia procesów i dostępu do sieci, co ogranicza możliwość, że weryfikator po cichu pobierał brakujące dane albo wykonywał zewnętrzne narzędzia.

<figure>
<svg viewBox="0 0 1060 470" role="img" aria-labelledby="wp13-title wp13-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="wp13-title">Zmiana pomiędzy WP12 i WP13</title>
  <desc id="wp13-desc">W WP12 część hashy kończyła się na metadanych. W WP13 każdy obowiązkowy identyfikator prowadzi do uwierzytelnionego obiektu lub typowanego receipt.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="55" y="55" width="430" height="330" rx="22" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <rect x="575" y="55" width="430" height="330" rx="22" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="270" y="98" text-anchor="middle" font-size="22" fill="var(--ink)">WP12</text>
    <text x="790" y="98" text-anchor="middle" font-size="22" fill="var(--ink)">WP13</text>
    <rect x="110" y="135" width="320" height="58" rx="12" fill="none" stroke="var(--acc)" stroke-width="2"/>
    <rect x="630" y="135" width="320" height="58" rx="12" fill="none" stroke="var(--acc)" stroke-width="2"/>
    <text x="270" y="170" text-anchor="middle" font-size="16" fill="var(--ink)">hash + typed metadata</text>
    <text x="790" y="170" text-anchor="middle" font-size="16" fill="var(--ink)">hash + typed metadata</text>
    <line x1="270" y1="193" x2="270" y2="260" stroke="var(--dn)" stroke-width="4" stroke-dasharray="9 8"/>
    <line x1="790" y1="193" x2="790" y2="260" stroke="var(--up)" stroke-width="4"/>
    <circle cx="270" cy="300" r="48" fill="var(--dn)" opacity=".16"/>
    <circle cx="790" cy="300" r="48" fill="var(--up)" opacity=".18"/>
    <text x="270" y="307" text-anchor="middle" font-size="25" fill="var(--dn)">?</text>
    <text x="790" y="307" text-anchor="middle" font-size="15" fill="var(--up)">OBJECT</text>
    <text x="270" y="365" text-anchor="middle" font-size="14" fill="var(--dn)">format mógł wystarczyć</text>
    <text x="790" y="365" text-anchor="middle" font-size="14" fill="var(--up)">identity resolves to bytes</text>
  </g>
</svg>
<figcaption>WP13 nie awansował syntetycznego kontraktu do realnego pomiaru hosta. Zamknął jednak dokładnie tę lukę, w której identyfikator mógł zostać nazwany rozwiązanym dowodem bez wskazania obiektu.</figcaption>
</figure>

## Dlaczego 340 mutacji ma znaczenie

Sama liczba testów nadal nie jest argumentem. Znaczenie wynika z tego, że mutacje przechodziły przez pełny resolver, którego sukces był badanym twierdzeniem. Wcześniejszy fałszywy hash nie został zastąpiony nowym testem pobocznym. Został skierowany do tej samej ścieżki, która buduje pozytywny werdykt, i został odrzucony.

To rozróżnienie jest istotne. Projekt może posiadać setki kontroli pomocniczych, a nadal nie testować głównej ścieżki decyzyjnej. WP13 odtwarzał pełny spec z obiektów zawartych w archiwum, budował kontrakt, uruchamiał resolver i przeliczał receipt. Mutacje nie kończyły się na poziomie pojedynczego parsera, ale docierały do kompletnego werdyktu.

## Obiekt dowodowy ma własną tożsamość

Po WP13 obowiązkowy dowód nie jest już wyłącznie zbiorem pól opisujących, czym powinien być. Musi mieć tożsamość możliwą do rozwiązania w dostarczonej paczce:

- konkretny obiekt i jego bajty,
- typ,
- rozmiar,
- tryb,
- hash,
- relację zależności,
- rolę semantyczną,
- miejsce w acyklicznym grafie.

Dopiero taki zestaw pozwala odróżnić zdanie „system operacyjny został opisany” od zdania „ten konkretny obiekt jest dowodem użytym do uzasadnienia węzła HOST_OS”.

<figure>
<svg viewBox="0 0 1060 440" role="img" aria-labelledby="object-title object-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="object-title">Minimalny łańcuch obiektu dowodowego</title>
  <desc id="object-desc">Węzeł semantyczny wskazuje identyfikator, identyfikator rozwiązuje się do obiektu, obiekt ma uwierzytelnione bajty i zamknięte zależności.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="45" y="160" width="210" height="90" rx="16" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="305" y="160" width="210" height="90" rx="16" fill="var(--soft)" stroke="var(--acc)" stroke-width="3"/>
    <rect x="565" y="160" width="210" height="90" rx="16" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <rect x="825" y="160" width="190" height="90" rx="16" fill="var(--soft)" stroke="var(--up)" stroke-width="3"/>
    <text x="150" y="198" text-anchor="middle" font-size="16" fill="var(--ink)">SEMANTIC NODE</text>
    <text x="150" y="226" text-anchor="middle" font-size="13" fill="var(--mut)">what must be proven</text>
    <text x="410" y="198" text-anchor="middle" font-size="16" fill="var(--ink)">CONTENT ID</text>
    <text x="410" y="226" text-anchor="middle" font-size="13" fill="var(--mut)">hash + type</text>
    <text x="670" y="198" text-anchor="middle" font-size="16" fill="var(--ink)">OBJECT BYTES</text>
    <text x="670" y="226" text-anchor="middle" font-size="13" fill="var(--mut)">size + mode + digest</text>
    <text x="920" y="198" text-anchor="middle" font-size="16" fill="var(--ink)">DEPENDENCIES</text>
    <text x="920" y="226" text-anchor="middle" font-size="13" fill="var(--mut)">closed and acyclic</text>
    <line x1="255" y1="205" x2="305" y2="205" stroke="var(--acc)" stroke-width="4"/>
    <line x1="515" y1="205" x2="565" y2="205" stroke="var(--acc)" stroke-width="4"/>
    <line x1="775" y1="205" x2="825" y2="205" stroke="var(--up)" stroke-width="4"/>
    <text x="530" y="98" text-anchor="middle" font-size="19" fill="var(--ink)">EvidenceResolved wymaga przejścia całego łańcucha</text>
    <text x="530" y="330" text-anchor="middle" font-size="15" fill="var(--mut)">Brak dowolnego ogniwa zatrzymuje pozytywny werdykt</text>
  </g>
</svg>
<figcaption>Content address ma wartość dowodową dopiero wtedy, gdy można rozwiązać go do określonego obiektu oraz sprawdzić jego miejsce w zamkniętym grafie zależności.</figcaption>
</figure>

## Czego WP13 nadal nie dowodzi

Pakiet pozostaje syntetyczny. Nie zmierzono realnego jednorazowego Wine prefixu ani runtime'u MT5. Nie załadowano EX5, nie dotknięto rachunku, nie pobrano danych brokera i nie uruchomiono żadnej ścieżki zleceń.

Statusy pozostały bez zmian:

```text
SYNTHETIC_NOT_RUNTIME_EVIDENCE = true
LIFECYCLE = COMPILED
LOADABLE = UNKNOWN
CANARY_TESTED = false
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
RISK_GOVERNOR_READY = false
LIVE_TRADING_APPROVED = false
```

Również provenance ma granicę. Finalny source commit WP13 pozostał lokalny i nie został wypchnięty do połączonego GitHuba, dlatego repozytoryjne ancestry i czystość worktree są deklaracjami source-side. Nie podważa to replayu archiwum wykonanego z surowych bajtów, ale nie wolno mieszać tych dwóch klas dowodu.

## Zamknięcie blockera nie jest zaproszeniem do kolejnych warstw

Po akceptacji WP13 program nie uruchomił automatycznie WP14. Szeroka rozbudowa Evidence Plane została zamrożona. Kolejne prace dowodowe mają wracać tylko wtedy, gdy konkretny blocker jest wymagany przez autoryzowany gate danych, produktu albo wykonania.

To świadoma korekta priorytetów. System dowodowy ma chronić rozwój produktu i badań, nie zastępować ich niekończącą się sekwencją coraz bardziej abstrakcyjnych attestation packages.

WP13 pokazuje, jak powinien wyglądać zdrowy cykl inżynieryjny:

1. pozytywny pakiet tworzy mocne twierdzenie,
2. red-team znajduje minimalny kontrprzykład,
3. kontrprzykład zostaje zamrożony,
4. następca prowadzi go przez pełną ścieżkę,
5. stary błąd staje się niemożliwy do zaakceptowania,
6. projekt zatrzymuje się zamiast ogłaszać gotowość wyższego poziomu.

Hash zaczął prowadzić do dowodu. Dowód nadal nie prowadzi do realnego runtime'u, przewagi ani prawa do handlu. Właśnie ta różnica stanowi sens Chronicle.

<div class="lab-archive"><strong>Granica ujawnienia:</strong> tekst opisuje niezależnie zaakceptowany zakres WP13 oraz publiczną strukturę Evidence Object Closure. Nie publikuje prywatnego store'u obiektów, pełnego specu, manifestów, kontraktów hosta ani danych wykonawczych.</div>
