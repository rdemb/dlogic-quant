---
title: "Skąd naprawdę bierze się pieniądz. Kredyt, banki i mit mnożnika"
description: "Większość pieniądza w gospodarce nie pochodzi z drukarni banku centralnego, tylko powstaje w bankach komercyjnych w chwili udzielenia kredytu: kredyt tworzy depozyt. Tekst rozkłada mechanikę kreacji pieniądza, obala podręcznikowy mit mnożnika depozytowego i pokazuje, że bank centralny steruje ceną pieniądza, a nie jego ilością. Źródła: Bank of England 2014 i Modern Money Mechanics, w tle Pozsar o shadow bankingu."
date: 2026-07-09 20:00:00 +0200
eyebrow: "Edukacja · pieniądz"
dek: "Podręcznik mówi, że bank bierze twój depozyt i pożycza go dalej, mnożąc pieniądz przez rezerwę. To odwrócona bajka. W rzeczywistości to kredyt tworzy depozyt, a nowy pieniądz powstaje z niczego w chwili podpisania umowy. Rozłożona na części mechanika, którą opisał Bank of England, a której polski internet niemal nie tłumaczy."
readingTime: 8
tags: [pieniądz, "kreacja pieniądza", kredyt, "banki komercyjne", "mnożnik depozytowy", "bank centralny", rezerwy, "baza monetarna", "Bank of England", "Modern Money Mechanics", Pozsar, "shadow banking", makroekonomia, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Większość pieniądza w nowoczesnej gospodarce tworzą banki komercyjne, udzielając kredytu. Bank of England (2014) podaje, że w gospodarce brytyjskiej fizyczna gotówka to około 3% szerokiego pieniądza, a depozyty bankowe około 97%. Te depozyty w większości powstały jako druga strona udzielonych kredytów, a nie jako oszczędności wpłacone do kasy.
> - Podręcznikowy mnożnik depozytowy to mit. Banki nie pożyczają cudzych depozytów obłożonych rezerwą. Udzielając kredytu, jednocześnie dopisują nowy depozyt na koncie kredytobiorcy, a rezerw dobierają dopiero potem. Przyczynowość biegnie odwrotnie, niż uczy szkoła: to kredyt tworzy depozyt, a nie depozyt kredyt.
> - Bank centralny steruje ceną pieniądza (stopą procentową), a nie jego ilością. W normalnych czasach dostarcza tyle rezerw, ile system potrzebuje po ustalonej stopie. Część głównych banków centralnych w ogóle nie ma wymogu rezerw obowiązkowych, co samo w sobie przewraca szkolny wzór na mnożnik.
> - Pieniądz to czyjś dług. Depozyt to zobowiązanie banku wobec ciebie, a rezerwy i gotówka to zobowiązanie banku centralnego. Spłata kredytu niszczy pieniądz: depozyt znika z bilansu. Stąd dwie warstwy, baza monetarna (pieniądz banku centralnego) i pieniądz bankowy (depozyty), przy czym tego drugiego jest znacznie więcej.

**Teza w jednym zdaniu:** Pieniądza w gospodarce nie dodrukowuje głównie bank centralny, tylko tworzą go banki komercyjne w akcie udzielania kredytu, a rezerwy i stopa procentowa ustalają cenę tego procesu, nie jego twardy limit.

## Szkolna wersja, w którą wierzy większość

Standardowy podręcznik do ekonomii opowiada to tak. Wpłacasz do banku 1000. Bank musi trzymać część jako rezerwę, powiedzmy 10%, więc odkłada 100, a pozostałe 900 pożycza komuś innemu. Te 900 trafia na kolejny rachunek, tam znów 10% ląduje w rezerwie, a 810 rusza dalej w świat. I tak w kółko, coraz mniejszymi kawałkami, aż z pierwotnego 1000 powstaje wielokrotność depozytów. Suma tej geometrii to znany wzór na mnożnik.

```
MIT (podręcznikowy mnożnik depozytowy):

  wpłata 1000 → rezerwa 100 → kredyt 900
                             → rezerwa 90  → kredyt 810
                                            → rezerwa 81 → kredyt 729 → ...

  suma depozytow = 1000 / stopa_rezerwy = 1000 / 0.10 = 10000
  mnoznik = 1 / stopa_rezerwy = 10
```

Historia jest schludna, mechaniczna i łatwa do narysowania na tablicy. Wynika z niej wygodny obraz świata: bank centralny ustala bazę, a mnożnik automatycznie rozdmuchuje ją w kredyty i depozyty. Kłopot w tym, że jako opis tego, co dzieje się naprawdę, ta historia ma odwróconą przyczynowość. Bank of England poświęcił w 2014 roku osobny artykuł w kwartalniku (McLeay, Radia, Thomas, "Money creation in the modern economy") właśnie temu, żeby to sprostować.

## Jak to działa naprawdę: kredyt tworzy depozyt

Kiedy bank udziela kredytu, nie sięga do skarbca po cudze oszczędności i nie przesuwa niczyich pieniędzy. Wykonuje dwa zapisy księgowe naraz. Po stronie aktywów pojawia się należność (kredytobiorca jest teraz winien bankowi), a po stronie pasywów pojawia się nowy depozyt na rachunku tego kredytobiorcy. Ten depozyt to świeży pieniądz, którego sekundę wcześniej nie było nigdzie w gospodarce. Bilans banku po prostu puchnie po obu stronach jednocześnie.

```
Bank udziela kredytu 100:

  AKTYWA                    PASYWA
  +100 nalezosc kredytowa   +100 depozyt kredytobiorcy  ← nowy pieniadz

  bilans rosnie po obu stronach o 100
```

To jest sedno, które Modern Money Mechanics (klasyczna broszura Fed z Chicago) pokazuje na prostych zapisach księgowych typu T: banki budują depozyty, zwiększając kredyty, a nie odwrotnie. Bank of England ujmuje to jednym zdaniem: za każdym razem, gdy bank udziela kredytu, jednocześnie tworzy odpowiadający mu depozyt na rachunku kredytobiorcy, a tym samym tworzy nowy pieniądz. Kredytobiorca wydaje ten depozyt, sprzedawca dostaje go na swoje konto i od tej chwili nowy pieniądz krąży w gospodarce nieodróżnialny od jakiegokolwiek innego.

Dlatego proporcja z Banku Anglii nie jest ciekawostką, tylko puentą. Skoro depozyty bankowe to około 97% szerokiego pieniądza, a większość z nich powstała jako druga strona kredytu, to znaczy, że gros pieniądza w obiegu został stworzony przez prywatne banki, nie wytłoczony przez mennicę.

## Skąd wziął się mit i dlaczego jest odwrócony

Skąd zatem opowieść o mnożniku, skoro księgowo to kredyt idzie pierwszy? Bierze się z pomylenia pojedynczego banku z całym systemem. Owszem, gdy jeden bank udzieli kredytu, a kredytobiorca przeleje pieniądze do innego banku, pierwszy bank musi rozliczyć tę płatność rezerwami, więc rezerwy fizycznie są mu potrzebne. Ale w skali całego systemu rezerwy nie znikają, tylko przechodzą z jednego banku do drugiego. Suma się nie kurczy, zmienia się tylko właściciel.

Kluczowa różnica dotyczy kolejności zdarzeń. W bajce o mnożniku najpierw jest rezerwa, a potem, jako jej pochodna, kredyt. W rzeczywistości najpierw jest decyzja kredytowa i powstający depozyt, a rezerw bank dobiera dopiero potem, pożyczając je na rynku międzybankowym albo od banku centralnego. Rezerwy nie są zbiornikiem, z którego wypływają kredyty. Rezerwy podążają za kredytem.

```
RZECZYWISTOSC (odwrocona przyczynowosc):

  decyzja kredytowa → nowy depozyt → dopiero potem bank szuka rezerw
                                     (rynek miedzybankowy lub bank centralny)

  rezerwy NIE sa mnozone w kredyty; to kredyty pociagaja za soba rezerwy
```

Bank of England mówi to wprost: w normalnych czasach bank centralny nie ustala ilości pieniądza w obiegu i pieniądz banku centralnego nie jest mnożony w kredyty i depozyty. Cała strzałka przyczynowa z podręcznika jest odwrócona.

## Rezerwy i bank centralny: cena, nie ilość

Czym więc są rezerwy i po co bank centralny? Rezerwy to rachunki, które banki komercyjne trzymają w banku centralnym. Służą do dwóch rzeczy: do rozliczania płatności między bankami oraz do wypłaty gotówki, gdy klienci jej zażądają. To pieniądz wyższej warstwy, którym banki płacą sobie nawzajem, ale którego zwykły człowiek nigdy nie dotyka.

Bank centralny nie steruje ilością tego pieniądza w sposób, w jaki wyobraża to sobie mnożnik. Ustala stopę procentową i, żeby utrzymać rynkową stopę międzybankową przy swoim celu, dostarcza tyle rezerw, ile system tego dnia potrzebuje. Innymi słowy ustala cenę (stopę), a ilość rezerw dopasowuje się do popytu. To jest odwrotność szkolnej opowieści, w której bank centralny ustala ilość, a rynek dopasowuje cenę.

Wpływ na tworzenie pieniądza jest więc pośredni. Podnosząc stopę, bank centralny czyni kredyt droższym, przez co mniej pożyczek się opłaca i wolniej powstają nowe depozyty. Obniżając stopę, robi odwrotnie. To dźwignia cenowa, a nie zawór ilościowy. Najlepszy dowód, że mnożnik nie jest prawem natury, jest instytucjonalny: część głównych banków centralnych w ogóle nie ma wymogu rezerw obowiązkowych. Jeśli w mianowniku wzoru na mnożnik można postawić zero, to wzór nie opisuje niczego mechanicznego.

Warto tu od razu rozbroić nieporozumienie wokół luzowania ilościowego. Gdy bank centralny prowadzi QE, tworzy rezerwy, żeby kupić za nie obligacje. To zamienia jeden aktyw (obligację) na inny (rezerwy) w bilansie sektora bankowego, ale nie jest tym samym co dopisanie depozytów obywatelom. QE pompuje bazę monetarną, co nie przekłada się automatycznie na pieniądz bankowy w rękach ludzi, bo tamten wciąż powstaje dopiero wtedy, gdy ktoś zaciągnie kredyt.

## Co naprawdę ogranicza tworzenie pieniądza

Jeśli banki tworzą pieniądz jednym zapisem księgowym, to co powstrzymuje je przed tworzeniem go w nieskończoność? Bank of England wskazuje trzy realne hamulce, i żaden z nich nie jest podręcznikową rezerwą.

Pierwszy to opłacalność i konkurencja. Kredyt niesie ryzyko i koszt, a banki rywalizują o kredytobiorców. Bank, który rozdaje kredyty bez opamiętania, poniesie straty i przegra z rozsądniejszymi. Drugi to popyt na kredyt i zachowanie samych gospodarstw oraz firm. Pieniądz można też zniszczyć: gdy ludzie spłacają długi zamiast zaciągać nowe, depozyty znikają szybciej, niż powstają. Trzeci to polityka pieniężna, czyli wspomniana cena kredytu ustalana stopą procentową.

Do tego dochodzi regulacja, a w niej najważniejszy jest kapitał, nie rezerwa. Tym, co naprawdę limituje, ile bank może pożyczyć, są wymogi kapitałowe, czyli ilość własnych funduszy zdolnych pochłonąć straty. To kapitał, a nie zapas rezerw, jest wiążącym ograniczeniem współczesnego banku. Podręcznik przez dekady wskazywał palcem na niewłaściwą pozycję bilansu.

## Pieniądz to dług: warstwy i hierarchia

Pod tym wszystkim leży jedna prosta obserwacja księgowa. Każda forma pieniądza jest czyimś zobowiązaniem, czyli czyimś długiem. Depozyt na twoim koncie to zobowiązanie banku wobec ciebie, obietnica wypłaty gotówki na żądanie. Gotówka i rezerwy to z kolei zobowiązanie banku centralnego. Nie istnieje pieniądz, który nie byłby jednocześnie czyimś pasywem.

Z tego wyrasta hierarchia, warstwowa piramida. Na dole leży pieniądz banku centralnego, czyli baza monetarna, na którą składają się gotówka w obiegu oraz rezerwy banków. Nad nią rozciąga się znacznie szersza warstwa pieniądza bankowego, czyli depozytów tworzonych przez banki komercyjne. To, czego używasz na co dzień, prawie zawsze pochodzi z tej górnej, większej warstwy.

```
WARSTWY PIENIADZA (hierarchia zobowiazan):

  PIENIADZ BANKOWY   depozyty gospodarstw i firm     ← wiekszosc pieniadza
     (pasywo banku komercyjnego)
  ─────────────────────────────────────────────
  BAZA MONETARNA     gotowka + rezerwy bankow        ← mniejsza warstwa
     (pasywo banku centralnego)
```

Skoro pieniądz powstaje jako dług, to znika, gdy dług jest spłacany. Kiedy kredytobiorca oddaje kredyt, bank kasuje należność po stronie aktywów i jednocześnie kasuje depozyt po stronie pasywów. Pieniądz nie wraca do żadnego skarbca, on po prostu przestaje istnieć.

```
Splata kredytu 100:

  AKTYWA                    PASYWA
  −100 nalezosc kredytowa   −100 depozyt              ← pieniadz znika

  bilans kurczy sie po obu stronach; pieniadz zostaje zniszczony
```

Dlatego zdanie pieniądz to dług nie jest hasłem ideologicznym, tylko opisem księgowania. Pieniądz jest elastyczny: rośnie, gdy sektor bankowy udziela kredytu, i kurczy się, gdy kredyt jest spłacany albo gdy popyt na niego zamiera.

## Shadow banking: ten sam mechanizm poza bankiem

Ta sama logika wychodzi poza mury regulowanych banków. Prace Pozsara i współpracowników z nowojorskiego Fed (o systemie bankowości równoległej i o instytucjonalnych pulach gotówki) opisują, jak kredyt i instrumenty przypominające pieniądz powstają także w tak zwanym shadow bankingu. Udziały funduszy rynku pieniężnego, transakcje repo czy papiery komercyjne oparte na aktywach pełnią dla wielkich inwestorów rolę substytutu depozytu, czyli są traktowane jak pieniądz.

To rozszerzenie tego samego mechanizmu, nie inny mechanizm. Tworzenie kredytu połączone z transformacją terminów i płynności zachodzi tam poza gwarancją depozytów i poza standardową siatką bezpieczeństwa banku centralnego, co czyni tę warstwę bardziej kruchą, o czym boleśnie przypomniał kryzys 2008. Dla porządku tej mapy wystarczy zapamiętać jedno: pieniądz i jego substytuty potrafią powstawać także tam, gdzie nie sięga słowo bank, wszędzie tam, gdzie ktoś udziela kredytu i buduje na nim zobowiązanie traktowane jak środek płatniczy.

## Co z tego wynika

Największy praktyczny wniosek jest taki, że potoczne drukowanie pieniędzy jest mylącym skrótem. Zdecydowana większość kreacji pieniądza to rozproszona akcja kredytowa tysięcy prywatnych banków, a nie prasa drukarska banku centralnego. Ilość pieniądza jest w dużej mierze endogeniczna, to znaczy odpowiada na popyt na kredyt i na skłonność banków do jego udzielania, a nie jest pokrętłem, które bank centralny przekręca wprost.

To zmienia sposób czytania kilku gorących tematów. Rezerwy wykreowane przez QE nie zamieniają się automatycznie w depozyty i wydatki, więc mechaniczne wiązanie bazy monetarnej z inflacją bywa myleniem warstw. Dług i pieniądz to zaś dwie strony tej samej kartki, bo pieniądz rodzi się jako dług i umiera wraz z jego spłatą. Kto to rozumie, ten czyta impulsy kredytowe i cykle płynności jako proces napędzany ceną i popytem, a nie jako podręcznikowy mnożnik, który miałby działać sam z siebie.

To nie jest porada inwestycyjna. To wykład mechaniki pieniądza, oparty na dokumentach banków centralnych, żebyś rozumiał, skąd bierze się pieniądz i kredyt w gospodarce, zanim zaczniesz doszukiwać się ich wpływu na rynki.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
