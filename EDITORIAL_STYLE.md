# Zasady redakcyjne D-LOGIC Quant

Ten dokument określa styl wszystkich publicznych treści na stronie. Jego celem jest ograniczenie schematycznego języka, dekoracyjnej interpunkcji i konstrukcji, które brzmią jak automatycznie wygenerowany tekst.

## Interpunkcja i znaki

- Nie używamy pauzy ani półpauzy Unicode w tekście publicznym.
- Nie używamy znaku wielokropka Unicode. W uzasadnionych przypadkach stosujemy trzy zwykłe kropki.
- Nie ozdabiamy zdań strzałkami, checkmarkami ani podobnymi symbolami.
- Zwykły myślnik może pojawić się w nazwie technicznej, zakresie, równaniu lub konstrukcji składniowej, ale nie powinien zastępować normalnego zdania.
- Nawias, dwukropek, przecinek i kropka mają pierwszeństwo przed ozdobnym rozbijaniem wypowiedzi.

## Konstrukcja zdań

- Zdania powinny mieć zróżnicowaną długość. Seria bardzo krótkich zdań jest dopuszczalna tylko wtedy, gdy wynika z rytmu narracji.
- Unikamy mechanicznego kontrastu, w którym po negacji natychmiast pojawia się druga, sloganowa definicja.
- Nie nadużywamy pytań retorycznych ani identycznych przejść pomiędzy sekcjami.
- Słowa takie jak „najważniejszy”, „kluczowy”, „fundamentalny” i „przełomowy” wymagają konkretnego uzasadnienia.
- Każdy akapit powinien rozwijać jedną myśl, a nie powtarzać poprzednie zdanie innymi słowami.

## Ton

- Piszemy jasno, rzeczowo i po polsku, bez napuszonego żargonu.
- Tekst może być narracyjny, ale nie powinien udawać sensacji.
- Metafora ma pomagać zrozumieć mechanizm. Po jej użyciu wskazujemy ograniczenia analogii.
- Wnioski muszą wynikać z materiału. Nie kończymy każdej sekcji sztucznie podniosłą puentą.
- Projekt, hipoteza i analogia nie są przedstawiane jako dowód.

## Standard publikacji

Przed publikacją sprawdzamy:

1. Czy twierdzenia mają źródło albo są jawnie oznaczone jako interpretacja.
2. Czy tekst nie zawiera prywatnych danych, parametrów ani chronionej własności intelektualnej.
3. Czy nagłówki odpowiadają zawartości sekcji.
4. Czy w tekście nie ma zakazanych znaków i powtarzalnych szablonów.
5. Czy artykuł daje czytelnikowi konkretną wartość bez konieczności znajomości całego projektu.

## Kontrola automatyczna

Polecenie:

```bash
python3 tools/editorial_cleanup.py
```

sprawdza publiczne pliki pod kątem zakazanej typografii i raportuje powtarzalne konstrukcje wymagające oceny redaktora. Workflow walidujący stronę uruchamia ten audyt przy każdym pull requeście.
