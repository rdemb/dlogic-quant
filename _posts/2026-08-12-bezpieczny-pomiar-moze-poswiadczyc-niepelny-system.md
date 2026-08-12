---
layout: labpost
title: "Bezpieczny pomiar może poświadczyć niepełny system"
description: "WP11 naprawił model zaufania oparty na nazwach, ale audyt wykazał, że bezpieczna obserwacja może pominąć obowiązkowe elementy albo zmierzyć tylko wygodny fragment runtime'u."
dek: "Ochrona sekretów i kompletność dowodu są odrębnymi problemami. System może prawidłowo zdecydować, co wolno obserwować, a nadal nie wiedzieć, czy zmierzył cały obiekt i przypisał dowodom właściwe znaczenie."
date: 2026-08-12 20:00:00 +0200
category: algo
eyebrow: "D-LOGIC Chronicle #04"
readingTime: 15
section_url: /chronicle/
section_label: Chronicle
cover_brand: "D-LOGIC CHRONICLE #04"
cover_title: "BEZPIECZNY NIE ZNACZY KOMPLETNY"
cover_subtitle: "ROLE POLICY PASS · RUNTIME CLOSURE FAIL · LIVE FALSE"
cover_kind: lifecycle
---
<div class="article-status"><span class="primary">ENGINEERING MILESTONE</span><span>WP11: ROLE POLICY PASS</span><span>RUNTIME COMPLETENESS: BLOCKED</span><span>HOST MEASUREMENT: NOT RUN</span><span>LIVE: NOT AUTHORIZED</span></div>

Poprzedni etap D-LOGIC zakończył się dość osobliwym wynikiem. Filtr bezpieczeństwa miał chronić aktywne środowisko MetaTrader i Wine przed przypadkowym pomiarem, ale robił to poprzez globalną listę zakazanych nazw. W rezultacie odrzucał także naturalne elementy jednorazowego, odizolowanego runtime'u, który miał zostać legalnie poświadczony.

WP11 naprawił ten błąd koncepcyjny. Zamiast pytać wyłącznie, jak nazywa się katalog albo plik, zaczął pytać, jaką rolę pełni dany korzeń, czy przecina się z aktywnym środowiskiem, czy zawiera sekrety oraz jakie operacje są wobec niego dozwolone.

Był to realny postęp. Niezależny audyt potwierdził działanie kilku mocnych mechanizmów: klasyfikację aliasów przed dostępem do danych, przechodzenie po drzewie przez przypięte deskryptory, kontrolę właściciela i trybów plików, blokowanie dowiązań oraz kompletny, odtwarzalny korpus przypadków negatywnych.

Mimo tego system nadal nie otrzymał prawa do wykonania pomiaru hosta.

Powód był bardziej interesujący niż poprzedni. WP10 nie potrafił bezpiecznie dopuścić właściwego obiektu. WP11 potrafił już rozpoznać dozwoloną klasę środowiska, ale audyt wykazał, że bezpieczna obserwacja może nadal być niepełna, semantycznie źle opisana albo ograniczona do wygodnego fragmentu całości.

Aktualny werdykt ma więc dwie części:

```text
ROLE_SCOPED_TRUST_PRIMITIVE = PASS
RUNTIME_REPRESENTATION_AND_COMPLETENESS = BLOCKED
```

Te zdania nie przeczą sobie. Pierwsze mówi, że system lepiej rozumie, co wolno mu obserwować. Drugie przypomina, że samo pozwolenie na obserwację nie dowodzi jeszcze, iż zmierzono właściwy i kompletny obiekt.

## Co WP11 rzeczywiście poprawił

Dostarczony pakiet był największym dotąd przenośnym zestawem polityki hosta w tej gałęzi projektu.

| Kontrola | Wynik |
|---|---:|
| Elementy archiwum | 113 |
| Zwykłe pliki | 98 |
| Katalogi | 15 |
| Dokumenty JSON | 51/51 PASS |
| Przypadki end-to-end | 38 |
| Przypadki komponentowe | 2 |
| Kontrole statyczne | 2 |
| Łączny korpus adwersarialny | 42 PASS |
| Niebezpieczne dowiązania i path traversal | 0 |

Liczby te opisują jakość przenośnego pakietu i możliwość niezależnego odtworzenia jego testów. Nie opisują zgodności terminala, poprawności danych brokerskich ani gotowości handlowej.

Najważniejsze zmiany były jakościowe.

### Zaufanie zależne od roli

Aktywne drzewo rachunku, jednorazowy runtime, toolchain, pakiet control plane i katalog dowodowy pełnią odmienne funkcje. W WP11 te role zaczęły mieć osobne reguły. Naturalna nazwa pliku terminala albo katalogu MQL5 przestała być automatycznie traktowana jako zagrożenie tylko dlatego, że podobna nazwa może wystąpić w aktywnym środowisku.

### Klasyfikacja tożsamości przed dostępem

Ten sam obiekt może być osiągalny przez kilka ścieżek. System najpierw buduje klasę tożsamości i sprawdza, czy którykolwiek alias wskazuje na powierzchnię zabronioną. Dopiero później może odczytać metadane albo bajty. Dozwolona nazwa nie może więc ukryć zakazanej tożsamości.

### Przechodzenie po drzewie przez deskryptory

Pomiar nie polega na swobodnym podążaniu za ścieżkami tekstowymi. Korzenie są przypinane, dowiązania nie są śledzone, a kolejne elementy podlegają kontroli właściciela, trybu, typu i budżetu. Zmniejsza to ryzyko, że obiekt zmieni znaczenie w trakcie pomiaru.

### Uczciwy brak pomiaru

WP11 nie otrzymał bezpiecznych korzeni jednorazowego środowiska. Nie próbował ich zgadywać, wyszukiwać ani zastępować aktywnymi katalogami. Nie uruchomił X, Wine, terminala ani artefaktu EX5. Nie dotknął rachunku, brokera, danych rynkowych i zleceń.

Wynik `BLOCKED_NO_SAFE_DISPOSABLE_ROOTS` był prawidłowy. Audit nie zakwestionował tej granicy. Zakwestinował to, co mogłoby zostać uznane za kompletny dowód, gdy korzenie zostaną już dostarczone.

## Bezpieczeństwo odpowiada na inne pytanie niż kompletność

Model oparty na rolach odpowiada na pytanie:

> Czy tę klasę obiektu wolno obserwować w tym eksperymencie?

Nie odpowiada automatycznie na pytania:

> Czy zmierzyliśmy cały runtime, a nie wybrany podkatalog?
>
> Czy każda obowiązkowa część eksperymentu została uwzględniona?
>
> Czy konkretny plik rzeczywiście dowodzi znaczenia przypisanego mu w kontrakcie?

Właśnie tutaj pojawiły się cztery główne blokery.

<figure>
<svg viewBox="0 0 1080 470" role="img" aria-labelledby="closure-title closure-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="closure-title">Trzy domknięcia wiarygodnego pomiaru</title>
  <desc id="closure-desc">Wiarygodny pomiar wymaga jednocześnie poprawnej roli, kompletu obowiązkowych węzłów semantycznych oraz pełnego manifestu runtime'u.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <circle cx="340" cy="225" r="150" fill="var(--soft)" stroke="var(--acc)" stroke-width="4"/>
    <circle cx="540" cy="225" r="150" fill="var(--soft)" stroke="var(--up)" stroke-width="4"/>
    <circle cx="740" cy="225" r="150" fill="var(--soft)" stroke="var(--dn)" stroke-width="4"/>
    <text x="270" y="145" text-anchor="middle" font-size="20" fill="var(--acc)">ROLE</text>
    <text x="270" y="174" text-anchor="middle" font-size="20" fill="var(--acc)">CLOSURE</text>
    <text x="540" y="145" text-anchor="middle" font-size="19" fill="var(--up)">SEMANTIC</text>
    <text x="540" y="174" text-anchor="middle" font-size="19" fill="var(--up)">NODE CLOSURE</text>
    <text x="810" y="145" text-anchor="middle" font-size="19" fill="var(--dn)">RUNTIME</text>
    <text x="810" y="174" text-anchor="middle" font-size="19" fill="var(--dn)">MANIFEST CLOSURE</text>
    <text x="255" y="255" text-anchor="middle" font-size="14" fill="var(--mut)">rola korzenia</text>
    <text x="255" y="280" text-anchor="middle" font-size="14" fill="var(--mut)">sekrety i overlap</text>
    <text x="540" y="255" text-anchor="middle" font-size="14" fill="var(--mut)">obowiązkowe węzły</text>
    <text x="540" y="280" text-anchor="middle" font-size="14" fill="var(--mut)">właściwe znaczenie</text>
    <text x="825" y="255" text-anchor="middle" font-size="14" fill="var(--mut)">pełny korzeń</text>
    <text x="825" y="280" text-anchor="middle" font-size="14" fill="var(--mut)">topologia i bajty</text>
    <circle cx="540" cy="225" r="49" fill="var(--ink)" opacity=".92"/>
    <text x="540" y="220" text-anchor="middle" font-size="15" fill="var(--bg)">TRUSTED</text>
    <text x="540" y="243" text-anchor="middle" font-size="15" fill="var(--bg)">MEASURE</text>
    <text x="540" y="420" text-anchor="middle" font-size="16" fill="var(--mut)">Brak jednego domknięcia unieważnia mocny werdykt.</text>
  </g>
</svg>
<figcaption>Autorska synteza wyniku WP11. Bezpieczna rola jest konieczna, ale sama nie wystarcza.</figcaption>
</figure>

## Bloker 1: obowiązkowe węzły można było pominąć

Schemat wymieniał kilka rodzajów dowodów potrzebnych dla eksperymentu loadera, między innymi tożsamość klienta display, graf działania, oczekiwany sentinel i politykę czasu. Audyt wykazał jednak, że nie wszystkie znalazły się w efektywnym zbiorze elementów wymaganych do werdyktu.

Kontrolowany test oznaczył te węzły jako nieobowiązujące, a pozostałe ścieżki jako dostępne. Resolver nadal zwrócił status sugerujący zweryfikowaną tożsamość przy wyłączonym wykonaniu.

Problem można zapisać prosto:

```text
RequiredBySchema(node)
nie implikuje
RequiredForVerification(node)
```

Schemat deklarował obowiązek, ale logika werdyktu nie zawsze go egzekwowała. System potrafił więc poprawnie sprawdzić wszystkie elementy, które sam wybrał, a jednocześnie pominąć część elementów koniecznych dla sensu całego eksperymentu.

## Bloker 2: poprawny hash może dowodzić niewłaściwej rzeczy

Kilka węzłów semantycznych zostało powiązanych z plikami, które mogły być użyteczne technicznie, ale nie dowodziły znaczenia sugerowanego przez etykietę.

Plik biblioteki może być częścią środowiska, a mimo to nie stanowić dowodu architektury hosta. Plik jednostki usługowej może opisywać konfigurację, ale nie dowodzić tożsamości działającego menedżera. Biblioteka kompatybilności może należeć do runtime'u, ale nie opisywać jądra systemu operacyjnego.

Hash rozwiązuje pytanie o tożsamość bajtów. Nie rozwiązuje pytania, czy te bajty są właściwym dowodem dla zadanej tezy.

<div class="lab-note"><strong>Zasada WP11:</strong> prawidłowa tożsamość artefaktu nie kompensuje błędnej roli semantycznej.</div>

## Bloker 3: realistyczne drzewo nadal nie mieściło się w polityce

WP11 dopuścił naturalne nazwy głównych elementów środowiska, naprawiając problem z poprzedniej wersji. Wewnątrz dozwolonego korzenia nadal obowiązywała jednak wąska lista znanych potomków.

Dodanie zwykłego, legalnego pliku biblioteki do realistycznej struktury MQL5 powodowało blokadę jako nieznana powierzchnia wrażliwa. Polityka przechodziła na minimalnej makiecie, ale nie potrafiła jeszcze reprezentować pełnego środowiska, które terminal rzeczywiście może potrzebować.

Rozwiązaniem nie powinno być otwarcie całego drzewa na dowolne pliki. Potrzebny jest zamknięty manifest oczekiwanego runtime'u, który opisuje każdą dopuszczoną tożsamość, typ, tryb, rozmiar, hash i położenie względne. Znane pliki przechodzą, nieznane dodatki blokują, a sekrety pozostają zakazane jeszcze przed odczytem treści.

## Bloker 4: fragment mógł udawać cały runtime

Role pełnego prefiksu Wine i pełnego terminala mogły zostać spełnione przez ich poddrzewa. Wybrany katalog wewnętrzny przechodził jako reprezentacja większego środowiska.

Taki skrót jest niebezpieczny. Pominięte pliki spoza wybranego poddrzewa mogą wpływać na loader, konfigurację, wyszukiwanie zasobów albo zachowanie procesu. Dokładny eksperyment wymaga związania całego przyszłego korzenia wykonawczego, a nie jego wygodnej próbki.

Wymagany invariant ma postać:

```text
MeasuredRootIdentity = ExactFutureRuntimeRootIdentity
```

Kopia, zmieniona nazwa i wybrany podkatalog nie powinny zastępować obiektu, który później zostanie rzeczywiście użyty.

<figure>
<svg viewBox="0 0 1040 500" role="img" aria-labelledby="proxy-title proxy-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="proxy-title">Proxy subtree a pełny runtime</title>
  <desc id="proxy-desc">Pomiar wybranego poddrzewa może przejść, chociaż pliki poza nim nadal wpływają na zachowanie kompletnego runtime'u.</desc>
  <g font-family="-apple-system,Segoe UI,Roboto,sans-serif">
    <rect x="70" y="60" width="430" height="360" rx="22" fill="var(--soft)" stroke="var(--line)" stroke-width="3"/>
    <text x="285" y="102" text-anchor="middle" font-size="21" fill="var(--ink)">PEŁNY RUNTIME</text>
    <rect x="115" y="145" width="340" height="190" rx="16" fill="var(--bg)" stroke="var(--acc)" stroke-width="3"/>
    <text x="285" y="185" text-anchor="middle" font-size="18" fill="var(--acc)">ZMIERZONE PODDRZEWO</text>
    <rect x="145" y="220" width="105" height="72" rx="10" fill="var(--soft)" stroke="var(--line)"/><text x="197" y="262" text-anchor="middle" font-size="14" fill="var(--ink)">loader</text>
    <rect x="315" y="220" width="105" height="72" rx="10" fill="var(--soft)" stroke="var(--line)"/><text x="367" y="262" text-anchor="middle" font-size="14" fill="var(--ink)">library</text>
    <rect x="105" y="355" width="115" height="42" rx="8" fill="var(--soft)" stroke="var(--dn)"/><text x="162" y="382" text-anchor="middle" font-size="13" fill="var(--dn)">config</text>
    <rect x="245" y="355" width="115" height="42" rx="8" fill="var(--soft)" stroke="var(--dn)"/><text x="302" y="382" text-anchor="middle" font-size="13" fill="var(--dn)">resources</text>
    <rect x="385" y="355" width="85" height="42" rx="8" fill="var(--soft)" stroke="var(--dn)"/><text x="427" y="382" text-anchor="middle" font-size="13" fill="var(--dn)">state</text>
    <rect x="590" y="130" width="360" height="220" rx="22" fill="var(--soft)" stroke="var(--dn)" stroke-width="3"/>
    <text x="770" y="180" text-anchor="middle" font-size="21" fill="var(--dn)">FAŁSZYWY SKRÓT</text>
    <text x="770" y="235" text-anchor="middle" font-size="18" fill="var(--ink)">fragment zweryfikowany</text>
    <text x="770" y="273" text-anchor="middle" font-size="18" fill="var(--ink)">całość uznana za znaną</text>
    <text x="770" y="318" text-anchor="middle" font-size="15" fill="var(--mut)">pominięte pliki nadal mogą</text>
    <text x="770" y="344" text-anchor="middle" font-size="15" fill="var(--mut)">zmienić zachowanie procesu</text>
    <text x="520" y="466" text-anchor="middle" font-size="16" fill="var(--mut)">Weryfikacja próbki nie jest tożsamością kompletnego środowiska.</text>
  </g>
</svg>
<figcaption>Dokładny runtime musi być mierzony jako jeden kompletny korzeń wraz z pełną relatywną topologią.</figcaption>
</figure>

## Pakiet był odtwarzalny, ale jeszcze nie bezpośrednio

Audyt wykazał także ograniczenie przenośności. Standardowe rozpakowanie archiwum zachowywało tryby plików, które nie odpowiadały późniejszemu kontraktowi uruchomieniowemu testów. Po wykonaniu udokumentowanej transformacji trybów Tier A, Tier B i wszystkie 42 przypadki przechodziły.

Dowód był więc odtwarzalny po zadanej materializacji, ale nie stanowił jeszcze jednego polecenia działającego bezpośrednio na surowym archiwum. Następny pakiet ma dostarczyć bezpieczny ekstraktor, który tworzy nowy prywatny katalog, stosuje zamrożony kontrakt trybów, ponownie uwierzytelnia zawartość i sam uruchamia cały przegląd.

Pojawiła się również granica pochodzenia. Końcowy stan recenzji był opisany w raporcie, ale nie został w pełni związany z finalnym, maszynowo czytelnym receipt. Nie oznacza to sprzeczności, ale ogranicza rangę twierdzenia o pełnym pochodzeniu ostatniego stanu.

## Trzy domknięcia zamiast jednego PASS

Najcenniejszym wynikiem WP11 jest rozdzielenie trzech warunków, które wcześniej łatwo było skleić w jeden status.

```text
TrustedMeasurement =
    RoleClosure
    AND SemanticNodeClosure
    AND RuntimeManifestClosure
```

**RoleClosure** określa, czy rola korzenia, brak aktywnego overlapu, klasa sekretów i dozwolone operacje są poprawne.

**SemanticNodeClosure** wymaga obecności każdego obowiązkowego elementu eksperymentu oraz dowodu związanego z właściwym znaczeniem.

**RuntimeManifestClosure** wymaga kompletnego korzenia, pełnej topologii i zamkniętej listy oczekiwanych plików. Poddrzewo, przemianowana kopia i nieznany dodatkowy element nie mogą przejść jako równoważne.

Dopiero przecięcie tych trzech zbiorów daje podstawę do mocnego werdyktu.

## Ten problem występuje również w quant researchu

Lekcja z runtime'u ma bezpośredni odpowiednik w badaniach rynkowych.

Zbiór cech może być całkowicie wolny od leakage, a mimo to nie zawierać zmiennej, która decyduje o wykonalności transakcji. Model faktorowy może poprawnie opisywać znane ekspozycje, a jednocześnie pomijać czynnik, który niszczy pozorną alfę. Dataset może przejść wszystkie kontrole jakości, ale nie obejmować stanów kryzysowych, w których strategia ponosi większość strat.

Bezpieczeństwo informacyjne, poprawność matematyczna i kompletność reprezentacji są odrębnymi osiami.

W researchu również potrzebujemy odpowiedników trzech domknięć:

1. **Information closure**: model korzysta wyłącznie z informacji dostępnej w chwili decyzji.
2. **Economic closure**: target, koszty i wykonalność opisują rzeczywistą transakcję.
3. **State-space closure**: dane i walidacja obejmują pełny zestaw stanów istotnych dla twierdzenia.

Można zbudować model uczciwy czasowo, a nadal niekompletny ekonomicznie. Można przeprowadzić poprawną walidację, a nadal mierzyć tylko łatwy fragment rzeczywistego problemu.

## Aktualny stan po WP11

WP11 nie zmienia lifecycle Probe ani stanu programu alpha.

```text
LIFECYCLE = COMPILED
LOADABLE = UNKNOWN
CANARY_TESTED = false
DATA_VALIDATED = false
MODEL_EDGE_PROVEN = false
FORWARD_EDGE_PROVEN = false
RISK_GOVERNOR_READY = false
LIVE_TRADING_APPROVED = false
```

Nie dostarczono bezpiecznych korzeni hosta. Nie wykonano pomiaru prawdziwego runtime'u. Nie uruchomiono terminala i nie przeprowadzono canary. Gałąź WP11 pozostaje zamrożonym dowodem granicy V5, bez merge do aktywnego rootu projektu.

Następny etap, WP12, ma rozwiązać trzy konkretne problemy:

- związać każdy obowiązkowy węzeł z właściwym dowodem semantycznym;
- opisać kompletny runtime zamkniętym manifestem zamiast listą nazw;
- umożliwić bezpośrednie odtworzenie kontroli z surowego archiwum.

Dopiero po osobnym przeglądzie tych mechanizmów można wrócić do pytania o bezpieczny pomiar hosta. Loadability nadal pozostaje osobnym, późniejszym eksperymentem.

## Granica publicznego opisu

Artykuł pokazuje problem architektoniczny, wyniki audytu i model trzech domknięć. Nie publikuje pełnego schematu polityki, prywatnych korzeni, reguł autoryzacji, list sekretów, poświadczeń, mapy usług, dokładnych kontraktów procesu ani danych potrzebnych do odtworzenia powierzchni wykonawczej.

Najważniejszy wniosek jest prosty:

> System może prawidłowo ustalić, co wolno mu obserwować, a nadal wydać zbyt mocny werdykt, jeżeli nie sprawdził całego obiektu i nie związał każdego dowodu z właściwym znaczeniem.

WP10 nauczył D-LOGIC, że zaufanie nie może zależeć od samej nazwy. WP11 dodaje drugą część tej lekcji: bezpieczeństwo bez kompletności chroni granicę, ale nie gwarantuje prawdy o środowisku za tą granicą.

<div class="lab-archive"><strong>Źródło wewnętrzne:</strong> niezależny Audit Reconciliation 11, corrective result WP11, fact sheet 09, pioneer note o manifest-scoped completeness oraz plan WP12. Wszystkie statusy dotyczą warstwy inżynieryjnej i nie stanowią dowodu przewagi rynkowej.</div>
