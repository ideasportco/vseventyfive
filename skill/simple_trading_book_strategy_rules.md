# Simple Trading Book: Core Strategy Rules & Execution Checklist

*Extracted directly from "Simple Trading Book: It's soooo simple" (Forex Simplified)*

---

## 1. Core Execution Philosophy (The Golden Law)

The book repeatedly warns against the #1 retail trader mistake across multiple chapters:
> **"Never enter on an immediate breakout of a neckline or level."** (Pages 28, 29, 30, 34)
> Entering immediately on the break leads to frequent bull/bear traps and false breakouts. High-probability execution requires patience: **Breakout → Retest → Confirmation Candle → Entry on Next Candle.**

---

## 2. The 4-Step Trade Verification Checklist

Before taking any trade on V75 or currency charts, the AI / trader must verify all 4 sequential gates:

### Gate 1: Structure & Pattern Identification
- [ ] **Market Context:** Identify the prevailing trend (Uptrend, Downtrend, or Consolidation/Range).
- [ ] **Recognized Pattern:** A clear pattern from the book is formed:
  - **Reversals:** Double Top/Bottom, Head & Shoulders / Inverse H&S, Triple Top/Bottom, Rounding Top/Bottom, Diamond.
  - **Continuations:** Bullish/Bearish Flag, Symmetrical Triangle, Rising/Falling Wedge, Rectangle (Consolidation Box), Pennant, Cup & Handle.
- [ ] **Neckline / Boundary Drawn:** A clear horizontal or slanted neckline connecting at least two valid swing points.

### Gate 2: Clean Breakout (No Premature Entry)
- [ ] **Breakout Candle:** A decisive candle closes *outside* the neckline or beyond the previous structural swing high/low.
- [ ] **Filter Rule:** **DO NOT BUY / SELL HERE.** (Page 29, 30). Hold execution. Do not chase extended momentum.

### Gate 3: Retest & Trigger Candle Confirmation
- [ ] **Retest Price Action:** Price pulls back to touch or test the broken neckline (broken resistance turns support, or broken support turns resistance).
- [ ] **Rejection / Confirmation Candle Formed:** The retest candle closes rejecting the level:
  - **Bullish Reversal / Continuation Trigger:**
    - Hammer (long lower shadow, small upper body) — Page 13
    - Bullish Engulfing (green body completely covers previous red candle) — Page 15
    - Morning Star (3-bar reversal sequence) — Page 14
    - Strong Bullish Climax Candle rejecting the retest zone — Page 28
  - **Bearish Reversal / Continuation Trigger:**
    - Shooting Star (long upper shadow, small lower body) — Page 19
    - Bearish Engulfing (red body completely covers previous green candle) — Page 20
    - Evening Star (3-bar exhaustion sequence) — Page 21
    - Hanging Man / Bearish Climax Candle — Page 18
- [ ] **Indecision Filter:** If the retest forms a Doji (Page 24) or Spinning Top (Page 25), **NO ENTRY** until directional resolution occurs.

### Gate 4: Execution & Risk Management Gate
- [ ] **Entry Timing:** Enter on the **open of the very next candle** following the completed confirmation candle (Page 29: *"Buy on next candle"*).
- [ ] **Stop Loss (SL) Placement:**
  - **Bullish Trades:** Placed strictly below the retest swing low or structural support level (Page 30, 37, 41).
  - **Bearish Trades:** Placed strictly above the previous swing high / retest peak (Page 30: *"place the stop loss above the previous high"*).
  - **Level 1 vs Level 2:** In high-volatility environments (like V75), choose Level 2 (structural invalidation behind the pattern pivot) rather than Level 1 (tight wick) to avoid premature stop-outs (Page 31).
- [ ] **Take Profit (Target) Criteria:**
  - **Pattern Projection:** Target measured by pattern depth/height projected from the neckline breakout point (Pages 36, 41, 46).
  - **Minimum Risk-to-Reward Ratio (1:3):** The setup **MUST** offer a minimum of 1:3 R:R (Page 27: *"Three units of expected gain to one unit of potential loss"*). If the distance to the nearest structural hurdle provides less than 1:2.5 – 1:3, **DISQUALIFY THE TRADE**.

---

## 3. Pattern-Specific Rule Matrix

| Pattern Type | Category | Neckline / Key Level | Entry Trigger | Stop Loss Anchor | Target Projection |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Double Top** (p. 36) | Bearish Reversal | Swing low between the two peaks | Retest of broken neckline + bearish candle | Above the retest peak / swing high | Height of peaks projected down from neckline |
| **Double Bottom** (p. 40) | Bullish Reversal | Swing high between the two troughs | Retest of broken neckline + bullish candle | Below the retest trough / swing low | Height of troughs projected up from neckline |
| **Head & Shoulders** (p. 38) | Bearish Reversal | Line connecting left and right shoulder troughs | Retest of neckline + rejection candle | Above the Right Shoulder high | Vertical distance from Head to Neckline projected down |
| **Inverse H&S** (p. 41) | Bullish Reversal | Line connecting left and right shoulder peaks | Retest of neckline + bullish candle | Below the Right Shoulder low | Vertical distance from Head to Neckline projected up |
| **Symmetrical Triangle** (p. 29, 31) | Continuation | Converging trendlines / previous swing pivot | Breakout + Retest of apex / broken boundary | Behind the opposite triangle swing pivot | Base height of the triangle projected from breakout |
| **Bullish / Bearish Flag** (p. 32, 34) | Trend Continuation | Parallel consolidation channel against the trend | Break of channel boundary + retest of previous high/low | Opposite channel boundary or Level 2 swing pivot | Length of the flagpole projected from breakout point |
| **Rectangle / Consolidation** (p. 33, 43, 46) | Range Breakout | Horizontal Support & Resistance boundaries | Clean exit + retest of horizontal boundary | Back inside the consolidation range | Height of rectangle box projected in breakout direction |
| **Falling Wedge** (p. 37, 42) | Bullish Reversal / Cont. | Downward-sloping converging upper resistance | Breakout of upper resistance + retest | Below the lowest wedge swing point | Widest base of wedge projected upward |
| **Rising Wedge** (p. 39, 45) | Bearish Reversal / Cont. | Upward-sloping converging lower support | Breakdown of lower support + retest | Above the highest wedge swing point | Widest base of wedge projected downward |

---

## 4. Disqualification Checklist (When to NOT Trade)

The AI agent must output **WAIT / NO-TRADE** if any of the following conditions are met:
1. **Middle of the Range:** Price is hovering between support and resistance with no clear boundary contact.
2. **Unconfirmed Breakout:** A candle broke the neckline, but no retest has occurred yet.
3. **Failed Retest:** Price broke out but fell back inside the pattern during the retest candle close.
4. **Sub-par R:R:** The required stop loss distance relative to the next major obstacle offers less than 1:3 R:R.
5. **Indecision at Key Level:** Consecutive Doji or Spinning Top candles at the neckline without directional conviction.