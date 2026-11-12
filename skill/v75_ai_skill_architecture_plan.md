# V75 Price Action AI Skill: System Architecture & Learning Plan

*A Model-Agnostic, Multi-Modal Trading Intelligence System for Deriv Volatility 75 (V75)*

---

## 1. System Overview

The goal of this system is to provide an AI agent with disciplined, rule-based price action reading capabilities grounded in published literature (*Simple Trading Book*, Volman, Damir), paired with an experiential feedback loop (Before/After screenshot reflections) and empirical backtesting validation.

```
                      +-----------------------------+
                      | User / Backtest Runner      |
                      +--------------+--------------+
                                     |
                                     v
                       [ "Before" Chart Screenshot ]
                                     |
                                     v
                      +-----------------------------+
                      | Multi-Modal AI Skill        |
                      | - 4-Gate Book Checklist     |
                      | - Active Failure Memory     |
                      +--------------+--------------+
                                     |
                                     v
                       [ Logged Trade Prediction ]
                       (Entry, SL, TP, Target R:R)
                                     |
                                     v
                       [ "After" Chart Screenshot ]
                                     |
                                     v
                      +-----------------------------+
                      | Post-Mortem Reflection Engine|
                      | - Outcome: Win / Loss / Miss |
                      | - Diagnosis & Journaling     |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      | Cumulative Case Memory Bank |
                      | (Feeds into future analyses)|
                      +-----------------------------+
```

---

## 2. Before & After Screenshot Learning Loop

This is the core human-like experiential learning mechanism:

### Phase 1: The "Before" Evaluation (Setup Evaluation)
1. **Input:** User submits an MT5 screenshot showing the setup developing (or at the retest).
2. **AI Analysis:**
   - Detects pattern geometry (e.g. Double Bottom, Falling Wedge, Symmetrical Triangle).
   - Verifies the 4 gates (Neckline break, retest touch, rejection candle, >= 1:3 R:R).
   - Retrieves recent failure modes from memory to check for known trap setups.
3. **Prediction Output & Logging:**
   - A unique Trade ID is generated (e.g. `TRD-20261111-001`).
   - Recorded fields: Timestamp, Instrument (`R_75`), Timeframe (e.g. `M5`), Pattern, Direction (`BUY`/`SELL`), Planned Entry, Invalidation/Stop Loss, Target 1, Target 2, Risk-Reward Ratio.
   - Status set to `PENDING_RESOLUTION`.

### Phase 2: The "After" Evaluation (Post-Mortem Resolution)
1. **Input:** User (or automated data feed) uploads the "After" screenshot showing how the candles resolved.
2. **Outcome Classification:**
   - **WIN:** Target hit before invalidation level touched.
   - **LOSS:** Stop loss hit before target.
   - **SCRATCH / INVALIDATED:** Structure broke down before reaching entry or retest failed.
   - **MISSED:** Setup triggered without fulfilling the strict retest rule.
3. **Structured Post-Mortem Diagnosis:**
   - **Success Audit:** Did it reach 1:3 R:R? What was the maximum drawdown during the trade?
   - **Failure Analysis:** Why did it lose?
     - *Execution Error:* Entered before candle closed, or traded into HTF resistance.
     - *Structural Failure:* Retest wick penetrated too deeply (invalidation Level 1 vs Level 2).
     - *Market Regime:* Spread spike, false breakout chop, or momentum exhaustion.

### Phase 3: Case Memory Updates
- Completed trades are saved into `journal/cases/<id>.json`.
- The system periodically updates a concise `rules/memory_lessons.md` summarizing the top 5 most common failure modes on V75, which is injected into the AI's future prompts.

---

## 3. Automated Trade Journal Schema

Each trade entry follows a strict JSON structure:

```json
{
  "trade_id": "V75-2026-M5-042",
  "created_at": "2026-11-11T20:45:00Z",
  "resolved_at": "2026-11-11T22:15:00Z",
  "instrument": "Deriv V75",
  "timeframe": "M5",
  "pattern": "Double Bottom",
  "book_reference": "Simple Trading Book p. 40",
  "setup_details": {
    "neckline_price": 542310.50,
    "breakout_candle_index": 48,
    "retest_confirmation_candle": "Bullish Hammer",
    "entry_price": 542450.00,
    "stop_loss": 541800.00,
    "target_1": 544400.00,
    "projected_rr": 3.0
  },
  "outcome": {
    "status": "WIN",
    "realized_rr": 3.1,
    "bars_to_resolution": 14,
    "max_adverse_excursion_r": -0.32,
    "exit_reason": "Target 1 achieved"
  },
  "post_mortem": {
    "clean_execution": true,
    "lessons_learned": "Retest touched exact neckline within 2 candles. Strong hammer wick provided tight structural anchor.",
    "tag": "textbook_retest"
  }
}
```

---

## 4. Out-of-Sample Backtesting Runner Protocol

To establish statistical proof of profitability without curve-fitting, the repository implements a rigorous evaluation protocol:

### Step 1: Historical Data Partitioning
- 10,000+ M5 historical candles pulled from Deriv WebSocket feed.
- **In-Sample (Train/Calibration - 50%):** Used to calibrate pivot extraction thresholds and verify pattern definitions.
- **Out-of-Sample (Test - 30%):** Strictly unseen data used to run blind setup evaluations.
- **Walk-Forward Validation (20%):** Recent unseen period to test adapting against regime changes.

### Step 2: The Blind Evaluation Runner (`evals/runner.py`)
- The runner slices historical data into rolling windows of 60 bars.
- Bars 1 to 60 are rendered into an MT5-style chart (or passed as OHLCV prompt input).
- Bars 61 to 120 are hidden from the AI.
- The AI must output its decision (`WAIT`, `WATCH`, or `ENTER` with SL/TP).
- If `ENTER` is called, the runner unrolls bars 61 to 120 to check the exact sequence of tick/candle events:
  - Did price hit SL first or TP first?
  - Was there slippage or spread penalty applied?

### Step 3: Statistical Proof & Performance Metrics
The system computes quantitative proof metrics:
1. **Win Rate:** Percentage of triggered trades hitting >= 1:3 R:R.
2. **Profit Factor:** Gross Profits / Gross Losses (Target > 1.8).
3. **Expected Value ($EV$):**
   $$EV = (P_{\text{win}} \times R_{\text{win}}) - (P_{\text{loss}} \times 1.0) - \text{Friction}$$
   *(Must be demonstrably positive over 200+ out-of-sample trades).*
4. **Max Drawdown (R-Multiples):** Deepest consecutive loss streak.
5. **Selective Discipline Score:** Percentage of choppy / non-retest bars correctly filtered as `NO-TRADE`.

---

## 5. Repository Structure

```
v75-price-action-skill/
├── SKILL.md                     # Model-agnostic agent instructions & prompt contract
├── README.md                    # Installation, usage, and MT5 screenshot guide
├── rules/
│   ├── checklist.md             # 4-Gate execution checklist (extracted from Simple Trading Book)
│   ├── patterns.md              # Reversal & continuation geometric definitions
│   └── memory_lessons.md        # Dynamic rolling lessons from trade post-mortems
├── examples/                    # Few-shot visual reference set
│   ├── double_bottom_before.png
│   ├── double_bottom_after.png
│   ├── false_break_trap_before.png
│   └── false_break_trap_after.png
├── journal/                     # Automated Trade Journal
│   ├── pending/                 # Active / unresolved trade logs
│   ├── completed/               # Resolved trade logs with post-mortems
│   └── journal_manager.py       # CLI to log Before/After and update memory
├── evals/                       # Out-of-Sample Evaluation Suite
│   ├── dataset/                 # 500 blind historical V75 chart slices
│   ├── runner.py                # Blind evaluator script
│   └── metrics.py               # EV, Win Rate, Profit Factor calculator
└── scripts/
    └── fetch_deriv_candles.py   # Live/historical V75 WebSocket candle fetcher
```

---

## 6. Practical Trading Mechanics (Deriv V75 Specifics)

To prevent real-world execution failure, the AI skill enforces three mandatory operational protocols:

### A. Spread & Slippage Buffer Rules
- **The Bid/Ask Asymmetry:**
  - On V75, charts plot the **Bid** price by default.
  - Buy orders enter at Ask, stop out at Bid.
  - Sell orders enter at Bid, **stop out at Ask**.
  - *Risk:* If a Sell stop loss is placed flush against a swing high wick, a minor spread expansion will stop out the position even if the chart shows the high was never reached.
- **The Buffer Formula:**
  - **Long (Buy) Stop Loss:**
    $$\text{SL} = \text{Structural Swing Low} - (0.2 \times \text{ATR}_{14})$$
  - **Short (Sell) Stop Loss:**
    $$\text{SL} = \text{Structural Swing High} + \text{Spread Buffer} + (0.2 \times \text{ATR}_{14})$$
  - If ATR is unavailable from the image, add a minimum baseline buffer of **0.1% of index price** (or 50–100 index points on V75) beyond the physical wick tip.

### B. Stagnation & Time-Decay Invalidation (The Momentum Expiration Rule)
- **The Core Premise:**
  - Breakout-retest setups from *Simple Trading Book* rely on directional momentum. Once a confirmation candle closes, price should promptly expand toward Target 1.
  - Lingering at the neckline signifies lack of conviction and drastically increases false-breakout risk.
- **The Rules:**
  - **M5 Invalidation Threshold:** If price fails to advance at least $+1R$ within **8 candles (40 minutes)** following entry, the trade is marked `STAGNANT`.
  - **Action on Stagnation:**
    1. If price is slightly in profit (+0.5R to +0.8R), move Stop Loss immediately to **Break-Even**.
    2. If price prints 3 consecutive indecision/doji candles hugging the neckline, **close the trade at market (Scratch)** rather than holding toward a full -1R stop.
    3. If price closes back inside the original pattern structure on a completed candle, exit immediately.

### C. MT5 Screenshot Capture Specification
For the AI's multimodal vision engine to reliably evaluate setups, user-submitted MT5 screenshots must meet this standard:

1. **Geometry & Scale:**
   - **Symbol & Timeframe:** Top-left header must be visible (e.g. `Volatility 75 Index, M5`).
   - **Price Axis:** Right-hand price scale must be visible to calculate exact stop/entry/target distances.
   - **Time Axis:** Bottom date/time bar visible to calculate candle elapsed time.
2. **Candle Count:**
   - Minimum **40 candles**, maximum **100 candles** visible on screen. Too zoomed-in loses structural context; too zoomed-out turns candle wicks into unreadable single pixels.
3. **Display Settings:**
   - Candlestick mode enabled with standard contrasting colors (e.g. Green/Red or White/Black).
   - Clean charts: Do not cover price action with dense oscillators (RSI, Stochastics, MACD windows). Naked charts with user-drawn support/resistance lines or 20 EMA are ideal.
4. **Multi-Timeframe Submissions:**
   - When pairing charts, submit:
     - **Image 1 (Context):** H1 or H4 showing major macro range boundaries.
     - **Image 2 (Trigger):** M5 or M15 showing the specific neckline breakout, retest, and trigger candle.

---

## 7. Review & Governance Principles

1. **Immutable Rules vs. Reviewed Lessons:**
   - Logged trade outcomes and post-mortems update `rules/memory_lessons.md` as contextual reference notes only.
   - Core strategy rules in `rules/checklist.md` are **never automatically mutated by the AI**. Any change to trading gates requires human review and confirmation.
2. **Empirical Historical Evidence != Guaranteed Future Profit:**
   - Backtest metrics (EV, Win Rate, Profit Factor) establish historical statistical edge and disciplined consistency on past feeds.
   - Backtest results do not guarantee future profitability on live synthetic indices.
