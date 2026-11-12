# V75 Assumption Validation Protocols

## Purpose and Safety
These are research tests, not financial advice or proof of a profitable strategy. Use historical data for exploration and a separate untouched period for confirmation. Do not optimize and report results on the same sample. Include realistic spread, execution assumptions, and uncertainty. The proposed thresholds below are hypotheses, not validated settings.

## Shared Evaluation Rules
- Freeze the exact rule version and parameters before each test.
- Define the eligible setup and outcome before inspecting results.
- Use timestamp-ordered data; prohibit look-ahead and survivorship/selection leakage.
- Keep a development period, a validation period, and a final untouched test period. Choose the split by available date range, not by outcome.
- Report sample size, missing data, coverage, confidence intervals where appropriate, and all excluded cases.
- Include transaction costs and sensitivity ranges for spread/slippage. Report results both gross and net of modeled costs.
- Preserve all cases, including losses, ambiguous screenshots, missed triggers, and no-trade decisions.

## 1. Vision Price-Axis Precision
**Question:** Can the chosen vision model read price labels and chart points accurately enough for the intended task?

**Dataset:** Build at least 30 screenshots with independently recorded MT5 price levels and raw candle data. Cover multiple zoom levels, digit lengths, themes, and price-axis placements. Prefer 100+ cases before making a reliability claim; 30 is only a pilot.

**Procedure:** Have the model extract visible axis labels and selected candle OHLC/level values without seeing the ground truth. Two human reviewers independently annotate each screenshot; resolve disagreements before scoring. Measure exact-match rate, absolute error in price units, error in ticks/points, decimal-place errors, and abstention rate.

**Decision:** Predefine tolerances based on the instrument's tick size and whether the value affects an entry/stop. Never use a universal “2% error” threshold: a small percentage can still be many ticks. If a price-critical extraction is uncertain or outside tolerance, require manual numeric confirmation or raw OHLC input and return `WATCH`/`NO_TRADE`, not a guessed level.

## 2. Spread and Stop-Buffer Calibration
**Question:** How do candidate buffers affect stop-out frequency, stop distance, and net expectancy under realistic execution costs?

**Data:** Use timestamped V75 candles plus broker-specific spread/quote data if available. Candle OHLC alone cannot establish actual spread expansion, bid/ask triggers, or slippage. If quote data is unavailable, label the test as a candle-only proxy and do not claim to validate execution safety.

**Procedure:** Freeze setup detection first. Compare candidate buffers, including structural-only, spread-only, spread + 0.2×ATR(14), and a predeclared sensitivity grid. Use ATR available at entry only. For each setup record initial risk, MAE in price and R, whether the stop would be touched, target reached, net outcome, and trade frequency. Model stop execution conservatively and include spread/slippage scenarios.

**Decision:** Compare net expectancy, stop-out rate, median/upper-tail stop distance, and trade count on validation and untouched test windows. Select no “safe” buffer from MAE alone: the buffer trades reduced premature stops against larger losses. If quote/spread data is absent, keep the rule marked unvalidated.

## 3. M5 Stagnation Threshold
**Question:** Is the proposed 8-candle / +1R rule consistent with outcome and risk under a predeclared trade-management policy?

**Procedure:** On each eligible historical trade, calculate time to +1R, time to stop/target, and adverse/favorable excursion. Compare predeclared windows (for example 4, 6, 8, 10, 12 candles) and policies (no time exit, scratch at threshold, or move stop) using walk-forward or separate out-of-sample periods. Count open positions consistently and include costs from earlier exits.

**Metrics:** Net expectancy in R, drawdown, loss size, fraction of winners prematurely exited, fraction of losses avoided, and trade count. Report conditional distributions, not just averages.

**Decision:** Do not pick the best threshold on the final test set. Treat the existing 8-candle threshold as a hypothesis until replicated on untouched periods. Historical candles do not reveal broker execution quality.

## 4. 1:3 Reward-to-Risk Threshold and Trade Frequency
**Question:** What are the trade frequency and net outcome when the strategy uses different target rules?

**Procedure:** Freeze signal and stop logic. Compare predeclared targets such as 1:1.5, 1:2, and 1:3, while also checking whether structural targets occur before the nominal R multiple. Use consistent overlap/position rules and model spread/slippage. Evaluate on chronological development, validation, and untouched test windows.

**Metrics:** Eligible setups, executed-signal count, win rate, average win/loss, net expectancy in R, profit factor, maximum drawdown, time in trade, and uncertainty intervals. Report signals per week/month to assess practical frequency, with the data period stated.

**Decision:** A higher target can lower win rate and frequency; neither high R:R nor low frequency alone proves quality. Keep 1:3 as a policy choice, not an empirical fact, until out-of-sample results support it.

## 5. Price-Action Pattern Edge vs Randomized Nulls
**Question:** Do the precisely specified rules show evidence beyond suitable no-edge baselines on V75?

**Procedure:** First translate each concept into deterministic code or a blinded human annotation protocol. Evaluate the frozen strategy on chronological V75 data. Compare against multiple nulls: shuffled trade outcomes, block-bootstrap or circular-shift returns preserving some serial structure, and simple baseline strategies with matched exposure/risk. A variance-matched random walk alone may be insufficient because it may ignore volatility clustering and serial dependence. Preserve costs and trade-selection rules in every comparison.

**Metrics:** Net expectancy, risk-adjusted return, drawdown, trade frequency, and a distribution of null outcomes; use confidence intervals and correction for multiple parameter tests. Repeat over distinct time windows and report failure as well as success.

**Decision:** If results do not robustly exceed appropriate nulls out of sample after costs, do not claim an edge. Even a positive historical result is not proof of future profitability or that human-trader “traps” explain the pattern. Synthetic feed generation details and broker execution conditions must be independently verified.

## Practical Evidence Status
- **Vision:** requires labeled screenshot/candle pairs and reliability testing.
- **Buffer:** requires quote-level spread and execution data for a real calibration; OHLC-only is a proxy.
- **Stagnation:** requires frozen management policies and out-of-sample comparison.
- **1:3 R:R:** requires outcome distributions and trade-frequency measurement, net of costs.
- **Pattern edge:** requires deterministic definitions and suitable null models; “human order flow” is not assumed.
