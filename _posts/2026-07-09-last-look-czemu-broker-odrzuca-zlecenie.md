---
title: "Last look. Czemu broker może odrzucić twoje zlecenie"
description: "Na rynku FX kwotowana cena nie zawsze jest wykonalna. Last look to krótkie okno, w którym dostawca płynności, już po otrzymaniu zlecenia, sprawdza jego ważność i cenę, a potem może je przyjąć, odrzucić albo zmienić. Tekst tłumaczy genezę mechanizmu, różnicę między wariantem symetrycznym a asymetrycznym oraz to, jak FX Global Code (zasada 17) i wytyczne GFXC wymuszają przejrzystość. Bez zmyślonych liczb, sama mechanika i zasady."
date: 2026-07-09 22:30:00 +0200
eyebrow: "Edukacja · egzekucja"
dek: "Kwota na ekranie bywa zaproszeniem do transakcji, nie gwarancją. Dostawca płynności ma last look, krótkie okno na sprawdzenie i odrzucenie zlecenia. Skąd się to wzięło, czemu wariant asymetryczny jest sporny i co mówi o tym FX Global Code. Dla detalisty rzecz o tym, że odrzucenie to nie zawsze błąd platformy."
readingTime: 7
tags: ["last look", "FX Global Code", GFXC, egzekucja, "dostawca płynności", "rynek OTC", rekwotowanie, "odrzucenie zlecenia", "price tolerance", asymetria, broker, Forex, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Last look to krótkie okno, w którym dostawca płynności, już po otrzymaniu twojego zlecenia, sprawdza je względem własnej kwoty i może je przyjąć, odrzucić albo zaproponować nową cenę. Kwotowana cena nie jest więc twardą obietnicą wykonania, tylko zaproszeniem do transakcji.
> - Mechanizm wyrósł z budowy rynku FX. Nie ma jednej giełdy, ceny płyną do wielu platform naraz, a między momentem kwotowania a dotarciem zlecenia mija czas. Last look miał chronić kwotującego przed nieaktualną ceną i przed graczami, którzy polują na spóźnione kwoty.
> - Sporny jest wariant asymetryczny. Gdy cena zdąży ruszyć się na twoją korzyść, zlecenie częściej odpada, a gdy ruszy się na korzyść dostawcy, zwykle przechodzi. To układ przypominający darmową opcję po stronie kwotującego, dlatego FX Global Code w zasadzie 17 wymaga przejrzystości i zakazuje wykorzystywania informacji z twojego zlecenia w oknie sprawdzenia.
> - Dla detalisty wniosek jest praktyczny. Odrzucenie albo rekwotowanie to nie zawsze błąd platformy, często to normalna mechanika rynku, zwłaszcza w szybkim rynku wokół danych. Warto znać politykę egzekucji swojego brokera i o nią pytać.

**Teza w jednym zdaniu:** Na zdecentralizowanym rynku FX kwotowana cena bywa zaproszeniem do transakcji, a nie gwarancją jej wykonania, bo po drugiej stronie działa last look, krótkie okno na sprawdzenie i ewentualne odrzucenie zlecenia, a granicę między kontrolą ryzyka a nadużyciem wyznaczają dopiero zasady FX Global Code.

## Kwotowanie to jeszcze nie transakcja

Na giełdzie akcji intuicja jest prosta. Widzisz cenę w arkuszu, wysyłasz zlecenie, dostajesz wykonanie po tej cenie albo lepszej. Kwota, którą widać, jest wiążąca, bo po drugiej stronie stoi konkretne zlecenie w centralnym arkuszu.

Rynek walutowy działa inaczej. Znaczna część obrotu odbywa się poza giełdą, w modelu OTC, gdzie ceny nie pochodzą z jednego arkusza, tylko są strumieniowane przez wielu dostawców płynności do wielu platform naraz. Kwota, którą masz na ekranie, to zwykle propozycja tego dostawcy, ważna w danym mgnieniu. I tu wchodzi last look. Dostawca płynności, po tym jak twoje zlecenie do niego dotrze, ma krótkie okno (nazywane oknem last look albo czasem przetrzymania), w którym może jeszcze sprawdzić zlecenie względem swojej aktualnej ceny i zdecydować, czy je przyjmie, odrzuci, czy odeśle nową kwotę. Innymi słowy, między kliknięciem a wykonaniem jest jeszcze jeden krok, którego na giełdzie nie ma.

## Skąd się wziął last look

Geneza jest techniczna, nie złowroga. Skoro rynek jest rozproszony, ta sama cena dostawcy trafia jednocześnie do wielu odbiorców, agregatorów i platform. Między chwilą, gdy dostawca ją opublikował, a chwilą, gdy dotarło do niego twoje zlecenie, mija czas: milisekundy transmisji przez sieć, przez agregatora, przez kolejki. W tym czasie rynek mógł się ruszyć, a kwota, którą widziałeś, mogła się już zdezaktualizować.

To otwiera pole do gry szybkościowej. Uczestnik z bardzo niskim opóźnieniem potrafi wyłapać kwotę, która jest już spóźniona względem rynku, i systematycznie zawierać transakcje po cenie korzystnej dla siebie, a niekorzystnej dla kwotującego. W żargonie mówi się o toksycznym przepływie i o arbitrażu opóźnień. Last look powstał jako mechanizm obronny: zanim dostawca zaangażuje kapitał, chce się upewnić, że cena, po której ma zawrzeć transakcję, dalej odpowiada rzeczywistości, oraz że samo zlecenie jest ważne i mieści się w limitach kredytowych. W świecie strumieniowych kwot rozsyłanych do wielu anonimowych odbiorców taki końcowy sprawdzian był odpowiedzią rynku na własną fragmentację.

## Dwa sprawdzenia w jednym oknie

W ujęciu FX Global Code last look ma służyć do dwóch rzeczy i tylko do nich.

Pierwsze to sprawdzenie ważności. Dostawca potwierdza, że zlecenie jest technicznie poprawne, prawdziwe i mieści się w ustalonych limitach (na przykład kredytowych). To warstwa czysto porządkowa.

Drugie to sprawdzenie ceny. Dostawca porównuje cenę z twojego zlecenia z ceną, którą oferowałby w tym momencie. Kluczowe jest pojęcie tolerancji cenowej (price tolerance): z góry ustalonego progu, o ile rynek może się ruszyć, zanim zlecenie zostanie odrzucone. Jeśli ruch mieści się w tolerancji, zlecenie przechodzi. Jeśli cena uciekła poza próg, dostawca może odmówić albo odesłać nową kwotę, czyli rekwotować. Zgodnie z zasadami okno takiego sprawdzenia powinno być możliwie krótkie i wykorzystywane tylko do tych dwóch celów, a nie do czekania i przyglądania się, dokąd pójdzie rynek.

## Asymetria, czyli dlaczego akurat twoje zlecenie odpada

Tu leży sedno kontrowersji. Sprawdzenie ceny można stosować symetrycznie albo asymetrycznie.

Symetryczne znaczy: dostawca odrzuca zlecenie, jeśli cena ruszyła się poza tolerancję w dowolną stronę, niezależnie od tego, czy ruch był na jego, czy na twoją korzyść. Próg działa w obie strony tak samo.

Asymetryczne znaczy: odrzucenie następuje głównie wtedy, gdy ruch ceny jest niekorzystny dla dostawcy (a więc korzystny dla ciebie), natomiast gdy ruch jest korzystny dla dostawcy, zlecenie zostaje wykonane. Efekt jest łatwy do nazwania. Kwotujący zatrzymuje transakcje, na których zaczyna zarabiać, a odrzuca te, na których zaczyna tracić. To układ przypominający darmową opcję: dostawca ma korzyść z ruchów w jedną stronę, a jest zabezpieczony przed ruchami w drugą, przez cały czas trwania okna last look. Właśnie dlatego zlecenia, które od razu poszły przeciw dostawcy, są statystycznie częściej odrzucane niż te, które od razu poszły w jego stronę. To nie przypadek ani awaria, to konsekwencja asymetrii.

## Dlaczego to budzi spory

Pierwszy problem jest pojęciowy. Kwotowanie, którego nie zawsze da się wykonać, podważa sens samej kwoty. Jeśli publikowana cena jest atrakcyjna właśnie dlatego, że jest chroniona prawem do odmowy, to porównywanie dostawców po samej cenie może wprowadzać w błąd. Odrzucenie ma dla odbiorcy realny koszt: traci moment, rynek zdążył się ruszyć, a ponowne wejście często wypada gorzej.

Drugi problem dotyczy tego, co dzieje się z informacją o twoim zleceniu w oknie sprawdzenia. Skoro dostawca przez chwilę trzyma zlecenie, zanim odpowie, pojawia się pokusa, by ten czas i tę wiedzę wykorzystać do własnego handlu, zanim jeszcze klientowi odpowie. To już nie jest kontrola ryzyka, tylko przewaga informacyjna kosztem klienta. Historia egzekucji nadzorczych wobec dużych instytucji pokazała, że akurat ten obszar bywał nadużywany, i to on w dużej mierze wymusił późniejsze zaostrzenie zasad. Napięcie sprowadza się do jednego pytania: czy last look jest uczciwym sprawdzianem, czy wygodną opcją do podglądania cudzego przepływu.

## Jak branża to reguluje: FX Global Code i zasada 17

Odpowiedzią rynku jest FX Global Code, zbiór zasad dobrej praktyki dla hurtowego rynku walutowego, utrzymywany przez Global Foreign Exchange Committee (GFXC). Kodeks nie jest ustawą, to dobrowolny standard, do którego instytucje przystępują przez deklarację zgodności. Powstał w 2017 roku i jest okresowo przeglądany, z aktualizacjami w 2021 i 2024 roku.

Last look reguluje wprost zasada 17. Jej trzon jest następujący. Last look powinien być używany jako mechanizm kontroli ryzyka, służący do potwierdzenia ważności zlecenia oraz do sprawdzenia ceny, a nie do innych celów. Uczestnik rynku stosujący last look powinien być przejrzysty co do jego użycia i udostępniać klientom stosowne informacje. Kodeks oczekuje, że informacja z twojego zlecenia nie będzie w oknie last look wykorzystywana do handlu na twoją niekorzyść, a wcześniejsze wytyczne wprost określały takie działanie jako niezgodne z dobrą praktyką rynkową. Jeśli dostawca stosuje sprawdzenie asymetryczne, powinien to ujawnić i umieć wyjaśnić. Okno powinno być tak krótkie, jak to praktycznie możliwe.

Wokół samego kodeksu GFXC wydał materiały pomocnicze poświęcone last look, w tym raport i wytyczne opisujące dobre praktyki oraz arkusze ujawnień (disclosure cover sheets), które mają ułatwić klientom porównywanie polityk różnych dostawców: czy stosują last look, jaki jest charakter sprawdzeń, czy są symetryczne, jaki jest typowy czas przetrzymania. Osobnym wątkiem jest model cover and deal, czyli sposób obsługi zlecenia, w którym dostawca najpierw zabezpiecza pozycję na rynku, a dopiero potem zawiera transakcję z klientem, zamiast brać ją od razu na własną książkę z ryzykiem. GFXC opisuje ten model w swoich materiałach właśnie po to, by klient wiedział, według jakiego mechanizmu jego zlecenie jest realizowane. Sensem całości nie jest zakaz last look, tylko wymóg, żeby był przejrzysty i ograniczony do kontroli ryzyka.

Źródła do samodzielnego sprawdzenia: FX Global Code w edycji z 2024 roku (zasada 17), materiały i raport GFXC o last look wraz z arkuszami ujawnień oraz materiały GFXC o modelu cover and deal.

## Co z tego wynika dla detalisty

Detalista rzadko styka się z dostawcami płynności bezpośrednio. Handlujesz z brokerem, który albo sam jest animatorem rynku i kwotuje ci ze swojej książki, albo przekazuje zlecenia dalej, do dostawców, którzy z kolei stosują u siebie last look. Dlatego odrzucenie czy rekwotowanie, które widzisz na własnej platformie, może pochodzić z twojego brokera albo z wyższego piętra łańcucha. Znajomy z terminala MT5 komunikat o rekwotowaniu lub o braku ceny to ta sama mechanika o warstwę niżej.

Praktyczny wniosek jest taki, że odrzucenie albo rekwotowanie nie jest automatycznie dowodem awarii ani oszustwa. Bywa nią, ale bardzo często jest normalną konsekwencją tego, jak działa rynek, zwłaszcza w szybkich warunkach: wokół publikacji danych makro, w pierwszych sekundach po zaskoczeniu, przy skokach zmienności, gdy tolerancja cenowa łatwo zostaje przekroczona. W takich chwilach rekwoty i odrzucenia rosną z definicji, bo cena naprawdę ucieka między twoim kliknięciem a dotarciem zlecenia.

Co z tym zrobić w praktyce. Poznaj politykę egzekucji swojego brokera i pytaj o konkrety: czy stosuje last look, czy sprawdzenie jest symetryczne, jaki jest typowy czas przetrzymania, jak wyglądają statystyki odrzuceń, czy broker jest sygnatariuszem FX Global Code. Czytaj dokumenty o realizacji zleceń i o najlepszym wykonaniu. Odróżniaj powtarzalny wzorzec odrzuceń akurat wtedy, gdy rynek idzie na twoją korzyść (to sygnał wart uwagi i pytań), od pojedynczych rekwotów w gorącym rynku (to zwykle mechanika, nie spisek). Wiedza o tym, że kwota bywa zaproszeniem, a nie gwarancją, sama w sobie zmienia sposób, w jaki interpretujesz to, co widać na platformie.

To nie jest porada inwestycyjna. To wyjaśnienie mechaniki egzekucji na rynku FX i zasad, które ją regulują, po to, żeby odróżniać normalne działanie rynku od realnego problemu, zanim wyciągniesz wniosek o swojej platformie albo brokerze.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
