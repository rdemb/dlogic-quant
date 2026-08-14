# D-LOGIC Quant Research Lab

[![Validate Jekyll site](https://github.com/rdemb/dlogic-quant/actions/workflows/validate-site.yml/badge.svg)](https://github.com/rdemb/dlogic-quant/actions/workflows/validate-site.yml)

Publiczne laboratorium badawcze i polskojęzyczna baza wiedzy o rynkach, statystyce, mikrostrukturze, ryzyku oraz budowie systemów quant.

**Strona:** [rdemb.github.io/dlogic-quant](https://rdemb.github.io/dlogic-quant/)  
**Stan projektu:** [Public Truth Map](https://rdemb.github.io/dlogic-quant/status/)  
**Kronika:** [D-LOGIC Chronicle](https://rdemb.github.io/dlogic-quant/chronicle/)  
**Kanał RSS:** [feed.xml](https://rdemb.github.io/dlogic-quant/feed.xml)

## Czym jest D-LOGIC

D-LOGIC dokumentuje drogę od hipotezy do dowodu. Publikowane są decyzje architektoniczne, audyty, falsyfikacje, wyniki negatywne, ograniczenia oraz materiały edukacyjne. Zielony test, działający interfejs albo dobry backtest nie są przedstawiane jako dowód przewagi rynkowej.

Repozytorium zawiera źródła publicznej witryny. Nie zawiera kompletnej prywatnej implementacji systemu transakcyjnego ani danych pozwalających odtworzyć jego logikę wykonawczą.

## Główne obszary

- **D-LOGIC Chronicle** - decyzje, audyty, pivoty i kolejne etapy budowy systemu.
- **Research** - jakość danych, leakage, koszty, baseline, holdout governance i falsyfikacja.
- **Baza wiedzy** - statystyka, matematyka, mikrostruktura, makro, ryzyko i programowanie.
- **Public Truth Map** - rozdzielenie faktów, hipotez, ambicji, blokad i następnych gate'ów.
- **Narzędzia** - proste kalkulatory edukacyjne działające lokalnie w przeglądarce.

## Standard publikacji

Każda publiczna zmiana przechodzi przez pull request i automatyczną walidację:

1. kontrolę źródeł i niedozwolonej typografii,
2. build Jekylla zgodny z GitHub Pages,
3. kontrolę artefaktu publikacyjnego,
4. sprawdzenie lokalnych odnośników, zasobów i identyfikatorów HTML,
5. kontrolę, czy pliki utrzymaniowe nie wyciekły do witryny.

Status techniczny nie zastępuje statusu naukowego. Aktualne granice twierdzeń są utrzymywane na stronie [Stan projektu](https://rdemb.github.io/dlogic-quant/status/).

## Granica publikacji

Publiczne są:

- problem badawczy i metodologia,
- kryteria falsyfikacji,
- wyniki oraz ich ograniczenia,
- status artefaktów i decyzji.

Prywatne pozostają między innymi pełne definicje cech i targetów, parametry, wagi, progi, dane rachunku, konfiguracja bezpieczeństwa, topologia infrastruktury oraz reguły egzekucji.

## Struktura repozytorium

| Ścieżka | Rola |
|---|---|
| `_posts/` | artykuły, Chronicle i notatki badawcze |
| `_layouts/` | szablony stron i wpisów |
| `assets/` | style, obrazy i skrypty używane przez witrynę |
| strony `*.html` | sekcje, mapy treści i narzędzia |
| `.github/workflows/` | automatyczna walidacja pull requestów |
| `.github/scripts/` | narzędzia kontroli jakości, wykluczone z publikacji |

## Uruchamianie kontroli źródeł

```bash
python3 .github/scripts/validate_editorial.py
```

Pełny build i kontrola wyrenderowanej witryny są wykonywane w GitHub Actions przy każdym pull requeście oraz po zmianie `main`.

## Zastrzeżenie

Materiały mają charakter badawczy i edukacyjny. Nie są poradą inwestycyjną, sygnałem transakcyjnym ani obietnicą wyniku. Każda zmiana statusu wykonawczego wymaga odrębnej, audytowalnej ścieżki dowodowej i jest publikowana w Public Truth Map.

## Kontakt

Krótsze publikacje i informacje o nowych materiałach: [@takitamrafal](https://x.com/takitamrafal).
