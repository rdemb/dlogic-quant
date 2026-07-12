---
title: "Dane rynkowe: od ticku do świecy. Na czym operuje kod"
description: "Tick to zdarzenie z czterema polami: bid, ask, czas i wolumen, a świeca OHLC to ten strumień spakowany w interwał: open pierwszy, high najwyższy, low najniższy, close ostatni. Poza barami czasowymi istnieją bary zdarzeniowe (tick, volume, dollar), które López de Prado w Advances in Financial Machine Learning (2018) opisuje jako próbkowanie bliższe aktywności rynku. Do tego struktury MqlTick i MqlRates z MQL5 pole po polu oraz resampling ticków do OHLCV w pandas metodą resample(15min).agg."
date: 2026-07-11 09:00:00 +0200
eyebrow: "Programowanie · dane"
dek: "Kod nie widzi wykresu, widzi liczby: strumień ticków i zagregowane świece. Ten tekst pokazuje, czym jest jedno i drugie, jak świeca powstaje z ticków, jak wyglądają pola MqlTick i MqlRates oraz jak zresamplować ticki do OHLC w pandas. Bez obietnic, sama struktura danych, na której operuje każdy skrypt."
readingTime: 8
tags: ["dane rynkowe", programowanie, dane, OHLC, tick, MQL5, pandas, resampling, "bary zdarzeniowe", "López de Prado", mikrostruktura, Forex, edukacja]
category: edukacja
---

> **W skrócie**
>
> - Tick to najmniejsze zdarzenie rynku: bid, ask, znacznik czasu i wolumen. Spread to ask minus bid, mid to średnia z obu. W FX nie ma centralnego wolumenu, więc MT5 podaje tick_volume, czyli liczbę zmian kwotowania, a nie realny wolumen obrotu.
> - Świeca OHLC to strumień ticków spakowany w interwał: open to pierwszy tick w oknie, high najwyższy, low najniższy, close ostatni. Bar czasowy próbkuje po zegarze, niezależnie od tego, ile działo się w środku.
> - Obok barów czasowych istnieją bary zdarzeniowe: tick bars, volume bars, dollar bars. López de Prado (Advances in Financial Machine Learning, 2018, rozdział 2) opisuje je jako próbkowanie bliższe aktywności rynku, o zwrotach bliższych rozkładowi normalnemu. To własność próbki, nie obietnica zysku.
> - Reszta to higiena danych: strefa czasu serwera wyznacza, gdzie zamyka się świeca dzienna, weekend zostawia dziurę, a OHLC liczone z bid nie zawiera kosztu ask. Znaczniki czasu trzeba dopasować, zanim cokolwiek się policzy.

**Teza w jednym zdaniu:** kod rynkowy operuje na dwóch obiektach, tickach i świecach OHLC, gdzie świeca to zawsze agregat ticków po jakiejś osi (czasie, liczbie ticków, wolumenie), więc zanim policzy się wskaźnik czy koszt, trzeba wiedzieć, jak dane zostały spróbkowane i z której strony rynku (bid, ask, mid) pochodzą.

## Tick: najmniejsze zdarzenie rynku

Kod nie widzi świecy na wykresie. Widzi strumień liczb. Najmniejsza z nich to tick: pojedyncze zdarzenie, w którym zmienia się kwotowanie. Tick ma zwykle cztery pola: cenę kupna (bid), cenę sprzedaży (ask), znacznik czasu i wolumen. Bid to cena, po której rynek kupi od ciebie, ask to cena, po której sprzeda tobie, a różnica ask minus bid to spread. Środek między nimi, mid równy (bid plus ask) podzielone przez dwa, jest wygodną ceną odniesienia, bo nie zależy od strony transakcji.

Ticki nie przychodzą w równych odstępach. W spokojną noc może być kilka na minutę, na publikacji danych makro kilkaset na sekundę. Ta nieregularność jest fundamentalną cechą danych wysokiej częstotliwości, co szczegółowo opisują Dacorogna i współautorzy w An Introduction to High-Frequency Finance (2001). Znacznik czasu bywa podawany w milisekundach, bo na aktywnym rynku sekunda to za mało, żeby rozróżnić kolejność zdarzeń.

Osobna pułapka dotyczy wolumenu. Rynek walutowy jest zdecentralizowany, nie ma jednej giełdy ani wspólnej taśmy transakcji, więc nie istnieje kanoniczny wolumen obrotu. To, co MT5 nazywa wolumenem świecy, to najczęściej wolumen tickowy, czyli liczba zmian kwotowania w oknie, a nie liczba realnie zawartych kontraktów. Bywa użyteczny jako miara aktywności, ale mylenie go z prawdziwym wolumenem to klasyczny błąd.

## Świeca OHLC: strumień ticków spakowany w czas

Patrzenie na surowe ticki jest niepraktyczne, bo jest ich za dużo. Dlatego pakuje się je w świece, znane też jako bary. Świeca OHLC opisuje całe okno czasu czterema liczbami: open to cena pierwszego ticku w oknie, high to najwyższa, low to najniższa, close to cena ostatniego ticku. Do tego dochodzi wolumen, czyli liczba ticków albo suma wolumenów w oknie.

Zależność jest jednokierunkowa: ze strumienia ticków da się złożyć świecę, z gotowej świecy nie odzyska się ticków, które ją utworzyły. Świeca to kompresja stratna. Widać to na jednym oknie:

```
Okno 15:00:00 do 15:14:59  (cena mid)
  15:00:03   1.08210   pierwszy tick   →  open
  15:04:11   1.08255   najwyzszy       →  high
  15:09:40   1.08190   najnizszy       →  low
  15:14:52   1.08230   ostatni tick    →  close
  liczba tickow: 1240                  →  volume (tickowy)
```

Ta sama operacja działa na każdym interwale. Świeca pięciominutowa i godzinna różnią się tylko szerokością okna, mechanika jest identyczna.

## Bary czasowe kontra bary zdarzeniowe

Świeca z poprzedniej sekcji to bar czasowy: okno wyznacza zegar. To najpopularniejszy sposób próbkowania i zarazem najbardziej arbitralny, bo rynek nie działa równomiernie w czasie. Godzina europejskiego popołudnia potrafi zmieścić tyle samo obrotu, co cała azjatycka noc, a mimo to obie dostają tyle samo barów.

Stąd bary zdarzeniowe, które próbkują nie po zegarze, lecz po aktywności. Trzy typowe warianty:

- tick bars: nowa świeca co ustaloną liczbę ticków, na przykład co 500,
- volume bars: nowa świeca co ustalony wolumen,
- dollar bars: nowa świeca co ustaloną wartość w walucie obrotu.

Marcos López de Prado poświęca im rozdział drugi Advances in Financial Machine Learning (2018). Argument jest statystyczny: gdy próbkuje się rynek proporcjonalnie do tego, ile się na nim dzieje, ciąg zwrotów jest bliższy rozkładowi normalnemu i bardziej zbliżony do niezależnych obserwacji, niż przy próbkowaniu po zegarze. To ta sama idea, którą Dacorogna i współautorzy (2001) nazywają czasem biznesowym: zegar, który przyspiesza, gdy rynek jest aktywny. Kluczowe zastrzeżenie: to jest własność próbki, sposób pocięcia tych samych danych, a nie żaden sygnał ani obietnica przewagi. Bary zdarzeniowe nie sprawiają, że strategia zarabia, zmieniają tylko statystyczne własności wejścia, na którym liczy się resztę.

## MqlTick i MqlRates: dane w MQL5

Terminal MetaTrader 5 udostępnia oba obiekty jako struktury języka MQL5. Tick to MqlTick, świeca to MqlRates. Poniżej pola dokładnie tak, jak definiuje je dokumentacja MQL5 (docs.mql5.com):

```
// --- MqlTick: pojedynczy tick (jedno zdarzenie kwotowania) ---
struct MqlTick
{
  datetime time;        // czas ostatniej aktualizacji ceny
  double   bid;         // biezacy bid
  double   ask;         // biezacy ask
  double   last;        // cena ostatniej transakcji (Last)
  ulong    volume;      // wolumen dla ceny Last
  long     time_msc;    // czas w milisekundach
  uint     flags;       // flagi ticku (co sie zmienilo)
  double   volume_real; // wolumen z wieksza dokladnoscia
};

// --- MqlRates: pojedyncza swieca OHLC ---
struct MqlRates
{
  datetime time;        // czas otwarcia swiecy
  double   open;        // otwarcie
  double   high;        // maksimum
  double   low;         // minimum
  double   close;       // zamkniecie
  long     tick_volume; // wolumen tickowy (liczba tickow)
  int      spread;      // spread w punktach
  long     real_volume; // wolumen rzeczywisty (jesli dostepny)
};

// --- pobranie biezacego ticku ---
MqlTick t;
if(SymbolInfoTick(_Symbol, t))
{
  double spread = t.ask - t.bid;         // spread w cenie
  double mid    = (t.ask + t.bid) / 2.0; // srodek rynku
}

// --- skopiowanie 100 ostatnich swiec M15 do tablicy ---
MqlRates rates[];
ArraySetAsSeries(rates, true);           // indeks 0 = najswiezsza swieca
int copied = CopyRates(_Symbol, PERIOD_M15, 0, 100, rates);
// rates[0].close = zamkniecie ostatniej swiecy M15
```

Dwa pola wymagają komentarza. spread w MqlRates jest liczbą całkowitą wyrażoną w punktach, nie w cenie, bo tak przechowuje go terminal. tick_volume to omawiany wcześniej wolumen tickowy, a real_volume bywa zerowy, jeśli broker nie dostarcza rzeczywistego wolumenu, co na rynku walutowym jest regułą. Funkcja CopyRates kopiuje gotowe świece do tablicy, a SymbolInfoTick zwraca ostatni tick. To są dwa punkty wejścia, przez które kod w MQL5 w ogóle dotyka danych rynkowych.

## Strefy czasu, sesje i dziury weekendowe

Znacznik czasu nie znaczy nic bez strefy. Serwer brokera pracuje we własnej strefie i to ona, a nie strefa lokalna, wyznacza, gdzie zamyka się świeca dzienna i gdzie przebiega granica doby. Dwaj brokerzy na tych samych danych bazowych mogą pokazać inne świece D1, jeśli mają inne przesunięcie serwera. Dlatego liczba świec dziennych w tygodniu bywa różna: przy jednym przesunięciu wychodzi pięć, przy innym pojawia się szczątkowa świeca niedzielna z kilku godzin po otwarciu.

Rynek walutowy handluje w trybie ciągłym przez dobę, ale nie przez weekend. Handel zamyka się w piątek około 17:00 czasu Nowego Jorku i wraca w niedzielę wieczorem, więc w danych jest regularna dziura. Kod, który nie uwzględnia tej przerwy, policzy fałszywą świecę weekendową albo zmienność rozjechaną na luce cenowej między piątkowym zamknięciem a niedzielnym otwarciem. Sesje handlowe, azjatycka, londyńska i nowojorska, nakładają się i rozchodzą, przez co ta sama godzina serwera oznacza inny stan płynności w zależności od pory roku i zmian czasu letniego.

## Jakość danych: luki, spread i strona rynku

Zanim policzy się cokolwiek, dane trzeba sprawdzić. Trzy rzeczy psują je najczęściej.

Luki. Brak ticków w oknie to nie zero, to brak danych. Weekend, święto, awaria feedu: każde z nich zostawia pustą świecę, którą trzeba świadomie usunąć albo oznaczyć, a nie wypełnić zerem, bo zero zaniży zmienność i zafałszuje każdą średnią.

Strona rynku. Większość historycznych szeregów OHLC jest budowana z bid. To wygodne, ale niespójne z tym, jak wygląda transakcja: kupno realizuje się po ask, więc świeca z bid nie zawiera kosztu wejścia po stronie kupna. Kto liczy koszt albo backtest na cenach bid, a wchodzi po ask, systematycznie zaniża koszt o mniej więcej spread. Mid usuwa asymetrię strony, ale nie jest ceną, po której da się zawrzeć transakcję. Wybór bid, ask czy mid to decyzja, nie szczegół.

Dopasowanie znaczników czasu. Tick z godziny 15:14:59,900 należy do świecy piętnastominutowej otwartej o 15:00, a nie do następnej. Reguła jest umowna, ale musi być spójna: przedział półotwarty, zamknięty z jednej strony. W praktyce kod przypisuje tick do okna po znaczniku czasu, więc niedopasowanie stref albo zaokrąglenie milisekund potrafi przesunąć zdarzenie o jedno okno i cicho zafałszować close.

## Resampling ticków do OHLC w pandas

Ta sama agregacja w Pythonie sprowadza się do jednej metody. Biblioteka pandas grupuje szereg czasowy metodą resample, po czym na każdym oknie liczy funkcje agregujące. Mapowanie jest dokładnie takie, jak w definicji świecy: open to first, high to max, low to min, close to last.

```
import pandas as pd

# ticki: kolumny bid, ask; indeks = znacznik czasu (datetime)
ticks = pd.read_csv("ticks.csv", parse_dates=["time"]).set_index("time")

# cena odniesienia: mid = srodek miedzy bid i ask
ticks["mid"] = (ticks["bid"] + ticks["ask"]) / 2

# agregacja: 15-minutowa swieca OHLC z kolumny mid
#   open  = pierwszy tick w oknie   (first)
#   high  = najwyzszy               (max)
#   low   = najnizszy               (min)
#   close = ostatni tick w oknie    (last)
bars = ticks["mid"].resample("15min").agg(
    open="first",
    high="max",
    low="min",
    close="last",
)

# wolumen tickowy = liczba tickow w oknie
bars["volume"] = ticks["mid"].resample("15min").count()

# puste okna (weekend, luki) daja NaN, wiec je usuwamy
bars = bars.dropna()
```

Kilka szczegółów, które ratują przed cichym błędem. Etykieta 15min zastąpiła dawne 15T, wycofane w nowszych wersjach pandas, co odnotowuje dokumentacja pandas (metoda resample). Domyślnie okno jest zamknięte i etykietowane od lewej strony, czyli świeca nosi znacznik początku okna, a przedział obejmuje start i wyklucza koniec. Puste okna dają NaN i trzeba je usunąć, inaczej trafią do dalszych obliczeń jako fałszywe świece. Gotowym skrótem na to samo jest metoda resample(...).ohlc(), która od razu zwraca kolumny open, high, low, close, ale jawne agg pokazuje, co dzieje się pod spodem.

To materiał czysto edukacyjny o strukturze danych rynkowych, nie porada inwestycyjna. Kod pokazuje, jak wygląda tick i świeca oraz jak jedno przechodzi w drugie, a nie jak zarabiać. Żaden sposób próbkowania, czasowy czy zdarzeniowy, nie tworzy przewagi sam z siebie: decyduje o statystycznych własnościach danych, na których dopiero potem liczy się wszystko inne.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
