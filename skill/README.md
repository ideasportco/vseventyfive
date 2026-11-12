# V75 Price Action AI Skill — Research Scaffold

A model-agnostic repository scaffold for screenshot-based V75 price-action review, before/after journaling, and cautious evaluation. This is a research and educational tool, not a trading bot or a claim of profitability.

## Contents
- `SKILL.md`: Input contract, sequential gates, management hypotheses, and output format.
- `rules/`: Modular breakout/retest, candle, risk/buffer, and trade-management rules.
- `schemas/`: JSON Schemas for screenshot verdicts and before/after journal entries.
- `cases/`: Case review template and governance for reviewed lessons.
- `evals/validation_protocols.md`: Empirical protocols for five unvalidated assumptions.
- `scripts/`: Historical candle download request and a simple blind verdict-agreement runner.

## Important status
The numerical thresholds in the rules (including `0.2×ATR`, 8 candles, and 1:3 R:R) are **provisional hypotheses**, not calibrated V75 facts. The book-derived rules are interpretations and require human review against the source material. The downloader and runner have not been executed against live services or validated on a complete dataset. No profitability claim is made.

## Suggested initial use
1. Have a user submit a clean chart screenshot. If exact prices matter, require the user to confirm them in text or provide candle data.
2. Evaluate using the current version of `SKILL.md` and record evidence plus limitations.
3. If the user later shares an outcome screenshot, add a case entry; retain it as unreviewed until a person checks the outcome.
4. Validate signal definitions and assumptions on chronological data with costs, then preserve a final untouched test period.

## Scope and safety
- The downloader requests public historical candle data only and never places orders.
- No broker login or automatic execution is included.
- Do not infer real order flow from a synthetic price chart.
- Backtests are historical evidence and cannot prove future performance.
