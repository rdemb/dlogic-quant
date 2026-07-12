---
title: "Obsługa zleceń i błędów w MQL5: retcode, requote, poślizg"
description: "Jak w MQL5 zbudowane jest pojedyncze zlecenie i jego wynik: struktura MqlTradeRequest oraz odpowiedź MqlTradeResult z polem retcode. Tekst tłumaczy najważniejsze kody powrotu handlu (TRADE_RETCODE_DONE, REQUOTE, PRICE_OFF, NO_MONEY, INVALID_STOPS, TRADE_DISABLED i inne), tryby wypełnienia FOK, IOC oraz RETURN, znaczenie pola deviation przy poślizgu, oraz po co wołać OrderCheck przed OrderSend. Na końcu retry z limitem, idempotencja przeciw dublowaniu zleceń i koncepcja self-healing. To higiena wykonania, nie strategia zarobkowa."
date: 2026-07-12 19:00:00 +0200
eyebrow: "Programowanie · MQL5"
category: edukacja
dek: "Zlecenie w MetaTrader 5 to nie kliknięcie, tylko struktura danych wysłana do serwera, która wraca z kodem wyniku. Ten tekst pokazuje, jak czytać ten kod, kiedy ponawiać, a kiedy odpuścić, i jak nie wysłać tego samego zlecenia dwa razy. Cała rzecz dotyczy higieny wykonania, nie tego, w którą stronę zagrać."
readingTime: 10
tags: [programowanie, MQL5, "obsługa błędów", OrderSend, retcode, requote, poślizg, MqlTradeRequest, "kody powrotu", ORDER_FILLING, egzekucja, edukacja]
---

> **W skrócie**
>
> - Zlecenie w MQL5 to struktura MqlTradeRequest wysłana funkcją OrderSend, a odpowiedź serwera wraca w MqlTradeResult. Pole retcode w wyniku niesie kod powrotu handlu i to ono, a nie sam zwrot funkcji, mówi, co naprawdę się stało.
> - Kod TRADE_RETCODE_DONE (10009) oznacza wykonanie. Wartości takie jak REQUOTE (10004), PRICE_OFF (10021), PRICE_CHANGED (10020), NO_MONEY (10019), INVALID_STOPS (10016) czy TRADE_DISABLED (10017) mają różne przyczyny i różne właściwe reakcje.
> - Tryb wypełnienia wybiera się świadomie: FOK (całość albo nic), IOC (tyle, ile dostępne, reszta anulowana), RETURN (reszta zostaje jako zlecenie). Dozwolone tryby zależą od symbolu, czyta się je z SYMBOL_FILLING_MODE.
> - Pole deviation ustala maksymalny dopuszczalny poślizg ceny w punktach. Zbyt małe generuje serie requote, zbyt duże z góry godzi się na gorsze wykonanie.
> - Retry musi mieć limit i sens: PRICE_CHANGED lub REQUOTE można ponowić po odświeżeniu ceny kilka razy, ale NO_MONEY albo TRADE_DISABLED to stany, których ponawianie nie naprawi. Idempotencja i sprawdzanie stanu chronią przed dublami.

**Teza w jednym zdaniu:** Poprawna obsługa zlecenia w MQL5 polega na przeczytaniu pola retcode z MqlTradeResult, dopasowaniu reakcji do konkretnego kodu powrotu, ponawianiu tylko tego, co ma szansę się udać, i pilnowaniu stanu tak, aby to samo zlecenie nie poszło dwa razy; to higiena wykonania, nie źródło przewagi.

## Zlecenie i wynik: dwie struktury

W MQL5 pojedyncza operacja handlowa to wypełnienie jednej struktury i wysłanie jej na serwer. Wejściem jest MqlTradeRequest, wyjściem MqlTradeResult. Zgodnie z dokumentacją MQL5 request opisuje, co ma się stać, a result niesie odpowiedź serwera handlowego.

Najważniejsze pola MqlTradeRequest to: action (typ operacji, na przykład TRADE_ACTION_DEAL dla natychmiastowej egzekucji), symbol, volume w lotach, price (cena, przy której zlecenie ma zostać wykonane), sl i tp jako ceny Stop Loss oraz Take Profit, type (kierunek, ORDER_TYPE_BUY albo ORDER_TYPE_SELL), type_filling (tryb wypełnienia) oraz deviation, czyli maksymalne dopuszczalne odchylenie ceny w punktach. Pole magic znakuje zlecenie identyfikatorem EA.

W odpowiedzi MqlTradeResult liczą się: retcode (kod powrotu serwera), deal i order (tickety, jeśli powstały), volume oraz price potwierdzone przez brokera, a także bid i ask, które przy rekwotowaniu niosą aktualne ceny rynku. Pole comment domyślnie zawiera opis kodu powrotu.

Kluczowa rzecz na start: funkcja OrderSend zwraca wartość logiczną, ale, jak podkreśla dokumentacja MQL5, true oznacza jedynie, że zlecenie przeszło sprawdzenie po stronie terminala i zostało wysłane. Prawdziwy los transakcji jest w polu retcode struktury result. Dlatego nigdy nie wystarczy sprawdzić samego zwrotu OrderSend, trzeba odczytać retcode.

## Kody powrotu: co znaczy retcode

Odpowiedź serwera koduje liczba retcode. Zestaw wartości pochodzi z dokumentacji MQL5, dział kody powrotu handlu, i nie należy ich zgadywać. Pełnym sukcesem jest jeden kod, TRADE_RETCODE_DONE. Reszta to informacja, dlaczego się nie udało.

```
10009  TRADE_RETCODE_DONE               zlecenie wykonane (pelny sukces)
10008  TRADE_RETCODE_PLACED             zlecenie oczekujace zlozone
10010  TRADE_RETCODE_DONE_PARTIAL       wykonano tylko czesc wolumenu
10004  TRADE_RETCODE_REQUOTE            rekwotowanie, cena sie zmienila
10020  TRADE_RETCODE_PRICE_CHANGED      ceny zmienione
10021  TRADE_RETCODE_PRICE_OFF          brak kwotowan do przetworzenia
10019  TRADE_RETCODE_NO_MONEY           za malo srodkow na operacje
10016  TRADE_RETCODE_INVALID_STOPS      bledne poziomy SL/TP
10015  TRADE_RETCODE_INVALID_PRICE      bledna cena w zleceniu
10014  TRADE_RETCODE_INVALID_VOLUME     bledny wolumen
10030  TRADE_RETCODE_INVALID_FILL       bledny tryb wypelnienia
10017  TRADE_RETCODE_TRADE_DISABLED     handel wylaczony
10018  TRADE_RETCODE_MARKET_CLOSED      rynek zamkniety
10031  TRADE_RETCODE_CONNECTION         brak polaczenia z serwerem
10012  TRADE_RETCODE_TIMEOUT            zlecenie anulowane przez timeout
10024  TRADE_RETCODE_TOO_MANY_REQUESTS  zbyt czeste zadania
10027  TRADE_RETCODE_CLIENT_DISABLES_AT autotrading wylaczony w terminalu
10026  TRADE_RETCODE_SERVER_DISABLES_AT autotrading wylaczony przez serwer
```

Warto pogrupować te kody według właściwej reakcji, nie według numeru. Pierwsza grupa to stany przejściowe, które mija czas i nowa cena: REQUOTE, PRICE_CHANGED, PRICE_OFF, czasem TIMEOUT. Tu ponowienie po odświeżeniu ceny bywa uzasadnione, ale z limitem. Druga grupa to błędy wejścia: INVALID_STOPS, INVALID_PRICE, INVALID_VOLUME, INVALID_FILL. Ich ponawianie w tej samej formie nic nie da, bo problem tkwi w treści zlecenia, trzeba poprawić parametry albo odpuścić. Trzecia grupa to twarde blokady: NO_MONEY, TRADE_DISABLED, MARKET_CLOSED, CLIENT_DISABLES_AT, SERVER_DISABLES_AT. Tu ponawianie jest bezcelowe, właściwą reakcją jest zapis w logu i zatrzymanie prób.

## Tryby wypełnienia: FOK, IOC, RETURN

Pole type_filling decyduje, co serwer zrobi, gdy nie może wypełnić całego wolumenu od razu. Dokumentacja MQL5 opisuje trzy główne tryby. ORDER_FILLING_FOK, czyli Fill or Kill, wykonuje zlecenie tylko w całości, a jeśli pełny wolumen nie jest dostępny, zlecenie nie wchodzi wcale. ORDER_FILLING_IOC, czyli Immediate or Cancel, bierze tyle, ile jest dostępne w rynku, a niewypełnioną resztę anuluje. ORDER_FILLING_RETURN nie anuluje reszty, pozostały wolumen zostaje dalej przetwarzany jako zlecenie. Istnieje też ORDER_FILLING_BOC (Book or Cancel) dla zleceń limit i stop-limit, który wymusza pasywne wystawienie w arkuszu.

Wybór nie jest dowolny. Zbiór trybów dopuszczonych dla danego instrumentu czyta się z właściwości SYMBOL_FILLING_MODE przez SymbolInfoInteger, a tryb egzekucji symbolu dodatkowo ogranicza możliwości, na przykład Market Execution wyklucza RETURN. Podanie trybu spoza dozwolonego zbioru kończy się kodem INVALID_FILL. Dlatego wartość type_filling ustawia się na podstawie tego, co zgłasza symbol, a nie na sztywno. Klasa CTrade ze Standard Library dobiera tryb automatycznie, co dla większości EA jest wystarczające.

## Poślizg cenowy i pole deviation

Poślizg to różnica między ceną, o którą prosi zlecenie, a ceną, po której realnie zostaje wykonane. Na szybkim rynku cena potrafi zmienić się między wysłaniem zlecenia a jego przyjęciem przez serwer. Pole deviation w MqlTradeRequest ustala, jak dużą taką różnicę zlecenie akceptuje. Dokumentacja MQL5 definiuje je jako maksymalne odchylenie ceny podane w punktach.

To jest kompromis, nie parametr do maksymalizacji. Zbyt małe deviation oznacza, że przy każdym drgnięciu ceny serwer odpowie kodem REQUOTE albo PRICE_CHANGED, a zlecenie nie wejdzie. Zbyt duże deviation z góry godzi się na wykonanie po zauważalnie gorszej cenie. Wartość dobiera się do zmienności i płynności instrumentu, inną dla spokojnego majora, inną dla ruchliwej pary w chwili publikacji danych. Przy egzekucji przez CTrade odpowiada za to metoda SetDeviationInPoints.

## Dlaczego OrderCheck przed OrderSend

Zanim zlecenie poleci na serwer, można je sprawdzić lokalnie. Funkcja OrderCheck, jak podaje dokumentacja MQL5, weryfikuje, czy jest dość środków na wykonanie operacji i czy struktura zlecenia jest wypełniona poprawnie. Wynik trafia do struktury MqlTradeCheckResult, która niesie własny retcode oraz projekcję stanu konta po operacji: balance, equity, profit, margin, margin_free i margin_level.

Sens tego kroku jest prosty: OrderCheck łapie część problemów, na przykład brak środków albo błędny wolumen, bez wysyłania czegokolwiek na serwer i bez obciążania limitu żądań. Nie zastępuje jednak odczytu retcode po OrderSend, bo warunki rynku mogą zmienić się między sprawdzeniem a wysłaniem. To sito wstępne, nie gwarancja. Dla operacji wrażliwych na koszt i na limity requestów tani lokalny check przed właściwym strzałem jest rozsądną higieną.

## Retry z rozsądkiem i idempotencja

Ponawianie zlecenia jest uzasadnione tylko dla stanów przejściowych i tylko z twardym limitem. Rozsądny wzorzec to kilka prób, nie więcej, z odświeżeniem ceny przed każdą kolejną i z krótką przerwą między nimi. REQUOTE i PRICE_CHANGED to typowi kandydaci do retry, bo znaczą jedynie, że cena uciekła. Pętla bez limitu na REQUOTE to błąd, bo w ruchu cena będzie uciekać dalej, EA zaleje serwer żądaniami i prędzej czy później dostanie TOO_MANY_REQUESTS.

Druga strona tej samej monety to idempotencja, czyli pewność, że jedna intencja rodzi najwyżej jedno zlecenie. Groźny jest scenariusz, w którym OrderSend zgłasza błąd połączenia albo timeout, a zlecenie mimo to zostało przyjęte przez serwer. Ślepe ponowienie otwiera wtedy drugą, niechcianą pozycję. Obrona jest dwuwarstwowa: przed wysłaniem sprawdzić, czy własna pozycja o danym magic już nie istnieje, a po niejasnym błędzie najpierw odczytać stan konta, zanim cokolwiek się ponowi. Magic number jest tu podstawą, bo pozwala odróżnić własne zlecenia od obcych.

## Self-healing: pojednanie stanu bota z brokerem

Automat trzyma w pamięci obraz tego, co uważa za swój stan: czy ma otwartą pozycję, jaki ma wolumen, gdzie stoją SL i TP. Broker trzyma stan prawdziwy. Te dwa obrazy potrafią się rozjechać: po zerwaniu połączenia, po częściowym wypełnieniu (DONE_PARTIAL), po zadziałaniu stopa w czasie, gdy EA nie liczył, albo po ręcznej ingerencji człowieka na koncie.

Koncepcja self-healing polega na tym, że EA nie ufa własnej pamięci, tylko okresowo odpytuje broker o rzeczywisty stan i godzi obie wersje. W praktyce znaczy to: na starcie i cyklicznie przejść po PositionsTotal oraz OrdersTotal, odfiltrować wpisy po magic i symbolu, a obraz świata odtworzyć z danych serwera, nie z lokalnych zmiennych. Jeśli pamięć mówi jedno, a broker drugie, prawdą jest broker. Taki mechanizm nie generuje zysku, ale chroni przed najgorszą klasą błędów wykonania, czyli działaniem na nieaktualnym obrazie pozycji. Warto to podkreślić, że to porządkowanie wykonania, nie strategia.

## Kompletny wzorzec order_send z obsługą wyniku

Poniższy fragment składa te zasady w jeden minimalny wzorzec: wypełnienie MqlTradeRequest, wstępny OrderCheck, wysłanie z ograniczonym retry i rozdzieleniem reakcji według retcode. To ilustracja mechaniki wykonania, nie strategia z przewagą.

```mql5
//+------------------------------------------------------------------+
//| Wzorzec egzekucji: OrderSend z obsluga retcode i retry z limitem.|
//| Higiena wykonania, NIE strategia zarobkowa.                      |
//+------------------------------------------------------------------+
input long   InpMagic     = 20260712; // magic: izolacja wlasnych zlecen
input ulong  InpDeviation = 20;       // dopuszczalny poslizg w punktach
input int    InpMaxRetry  = 3;        // twardy limit ponowien

//+------------------------------------------------------------------+
//| Zwraca true, gdy kod powrotu to stan przejsciowy (mozna ponowic).|
//+------------------------------------------------------------------+
bool IsRetryable(uint code)
  {
   return(code == TRADE_RETCODE_REQUOTE       ||  // 10004
          code == TRADE_RETCODE_PRICE_CHANGED ||  // 10020
          code == TRADE_RETCODE_PRICE_OFF     ||  // 10021
          code == TRADE_RETCODE_TIMEOUT);         // 10012
  }
//+------------------------------------------------------------------+
//| Wysyla zlecenie rynkowe BUY z SL/TP. Zwraca true tylko przy DONE.|
//+------------------------------------------------------------------+
bool SendMarketBuy(double lots, double sl, double tp)
  {
   for(int attempt = 1; attempt <= InpMaxRetry; attempt++)
     {
      // 1) Swieza cena przed KAZDA proba (poprzednia mogla sie zdezaktualizowac).
      double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);

      MqlTradeRequest req; ZeroMemory(req);
      MqlTradeResult  res; ZeroMemory(res);

      req.action       = TRADE_ACTION_DEAL;    // natychmiastowa egzekucja
      req.symbol       = _Symbol;
      req.volume       = lots;
      req.type         = ORDER_TYPE_BUY;
      req.price        = ask;
      req.sl           = sl;
      req.tp           = tp;
      req.deviation    = InpDeviation;         // maks. poslizg w punktach
      req.magic        = InpMagic;
      req.type_filling = ORDER_FILLING_IOC;    // reszta anulowana, nie zawisa

      // 2) Sito wstepne: srodki i poprawnosc struktury, bez wysylki na serwer.
      MqlTradeCheckResult chk; ZeroMemory(chk);
      if(!OrderCheck(req, chk))
        {
         PrintFormat("OrderCheck odrzucil: retcode=%u %s",
                     chk.retcode, chk.comment);
         return(false);                        // np. NO_MONEY: nie ma po co strzelac
        }

      // 3) Wlasciwa wysylka. Zwrot bool NIE wystarcza, liczy sie res.retcode.
      OrderSend(req, res);

      if(res.retcode == TRADE_RETCODE_DONE)    // 10009: jedyny pelny sukces
        {
         PrintFormat("Wykonane: deal=%I64u po cenie %.5f",
                     res.deal, res.price);
         return(true);
        }

      if(IsRetryable(res.retcode))             // stan przejsciowy: ponow z limitem
        {
         PrintFormat("Proba %d/%d, retcode=%u %s, ponawiam po nowej cenie",
                     attempt, InpMaxRetry, res.retcode, res.comment);
         Sleep(200);                           // krotka przerwa, nie zalewamy serwera
         continue;
        }

      // 4) Inny kod (INVALID_STOPS, TRADE_DISABLED, NO_MONEY...) NIE do retry.
      PrintFormat("Blad nieponawialny: retcode=%u %s, przerywam",
                  res.retcode, res.comment);
      return(false);
     }

   Print("Wyczerpano limit ponowien, zlecenie NIE weszlo");
   return(false);
  }
//+------------------------------------------------------------------+
```

Wzorzec czyta się jako mapę reakcji, nie jako gotowca. Cena jest pobierana świeżo przed każdą próbą, OrderCheck odsiewa oczywiste braki środków i błędy struktury, a po OrderSend decyduje wyłącznie res.retcode. Sukces to jeden kod, DONE, stany przejściowe idą do ograniczonej pętli, a wszystko inne kończy próby i trafia do logu. W wersji produkcyjnej pole type_filling powinno wynikać z odczytu SYMBOL_FILLING_MODE dla danego symbolu, a nie być ustawione na sztywno, żeby uniknąć kodu INVALID_FILL na instrumentach, które nie dopuszczają IOC.

Materiał czysto edukacyjny o mechanice wykonania zleceń, nie porada inwestycyjna ani gotowy bot do handlu. Opisana obsługa retcode, trybów wypełnienia i poślizgu to higiena egzekucji, która nie tworzy przewagi rynkowej; decyzja o wejściu i całe ryzyko zostają po stronie człowieka. Kody powrotu, pola struktur i tryby wypełnienia podano zgodnie z dokumentacją MQL5 (OrderSend, MqlTradeRequest, MqlTradeResult, kody powrotu handlu, ORDER_FILLING). Każdy automat wymaga własnych testów na danych historycznych i na rachunku demo, zanim dotknie realnych pieniędzy.

OBSERVE_ONLY · MANUAL_DECISION_ONLY · NO_AUTO_TRADING
