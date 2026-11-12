# Rule 05 — Universal Price Action & Dynamic Confluence

Source: T. Chiparange, *Universal Price Action V1* (Supreme Traders). Adapted for V75 M5/H1.
These rules **refine** Gates 1–4. They never loosen them: the 1:3 minimum R:R and spread + 0.2 × ATR buffer from Rule 03 still apply.

## 5.1 Three-Touch Trendline Rule (Gate 1)
- Touch 1 and Touch 2 are anchors only. They draw the line. **No trade on touch 1 or 2.**
- A trendline becomes tradable on **Touch 3**:
  - Bounce: a rejection trigger (Rule 02: pin bar, engulfing, railway track) closes away from the line.
  - Break: a full-body close through a 3-touch line, then a retest from the other side (Rule 01).
- Anchors must be outer swing lows (uptrend) or outer swing highs (downtrend). Lines cut through candle bodies are invalid.
- Tag: `3_TOUCH_TRENDLINE`.

## 5.2 200 EMA Bias & Confluence (Gate 1 grading)
- Price above the 200 EMA → long setups only. Below → short setups only.
- A flat 200 EMA running through price = no bias → maximum verdict is `WATCH`.
- Touch 3 or a horizontal key level that meets the 200 EMA in the same zone = **A+ confluence** (raise confidence, never skip a gate).
- Trading directly into an opposing 200 EMA within 1R of entry = obstacle; R:R must be measured to the EMA, not beyond.
- The 200 EMA is the one permitted overlay; other indicators stay banned (SKILL.md §2).
- Tag: `200_EMA_CONFLUENCE`.

## 5.3 Breakout Body-Close Standard (Gate 2)
- A breakout counts only on a candle **body close** beyond the level on the traded timeframe. Wicks through do not count.
- Retest: price returns to the broken level and rejects it (wick tests the level, body closes on the breakout side).
- Failure: a body close back inside the old range during the retest = fakeout → `NO_TRADE`.

## 5.4 Reversal Structures (Gate 1–3)
Applies to Head & Shoulders, Inverse H&S, Double Top/Bottom, Rising/Falling Wedge.
- Valid only at swing extremes after an extended move, never mid-range.
- H&S: shoulders should overlap horizontally. A bearish H&S neckline sloping up (lower-left to upper-right) is preferred; a steeply down-sloping neckline is weak. If validity is questionable → `NO_TRADE`.
- **Never** enter while the right shoulder or second peak is still forming.
- Entry: body close through the neckline/boundary, then **retest entry** (preferred method).
- Pattern-within-a-pattern: a wedge break often builds the right shoulder of a larger H&S. Note it in `patterns`.
- Tags: `HEAD_SHOULDERS`, `DOUBLE_TOP_BOTTOM`, `WEDGE`.

## 5.5 Stop Placement (Gate 4)
- Conservative: beyond the whole right shoulder / pattern extreme.
- Preferred: beyond the **last swing high/low of the retest**, plus the Rule 03 buffer. This tighter stop is what produces large R multiples.
- Never place the stop inside the retest swing.

## 5.6 Targets (Gate 4)
- Conservative: the first key opposing support/resistance.
- Measured objective: pattern height (head → neckline, bottom → neckline, widest triangle width) projected from the **breakout point**.
- Measured objectives are zones, not exact prices. Prefer a target where the objective meets a key level.
- R:R is calculated to the **nearer** of the two. Below 1:3 → `NO_TRADE`.

## 5.7 Flag Orientation Filter (Gate 1)
- A bull flag must slope **down** (against the uptrend). A bear flag must slope **up**.
- An upward-sloping "flag" in an uptrend (or downward in a downtrend) is exhaustion, not continuation → `NO_TRADE`, tag `FLAG_EXHAUSTION_TRAP`.
- Flag pole must be a sharp impulse; flag should retrace less than half the pole.

## 5.8 Triangles (Gate 1)
- Ascending triangle: flat resistance + rising lows, inside an uptrend for continuation.
- Descending triangle: flat support + falling highs, inside a downtrend for continuation.
- Trade the body-close break + retest of the flat side. Target = widest width projected from breakout.
- Tag: `TRIANGLE`.

## 5.9 Account Risk
- The guide permits 2–5% risk; this skill caps risk at **1–2% per trade** for V75 volatility. Calculate size from stop distance, never the reverse.

## Setup Tags (add to `patterns` in the evaluation)
`3_TOUCH_TRENDLINE`, `200_EMA_CONFLUENCE`, `BREAKOUT_RETEST`, `HEAD_SHOULDERS`, `DOUBLE_TOP_BOTTOM`, `WEDGE`, `TRIANGLE`, `BULL_FLAG`, `BEAR_FLAG`, `FLAG_EXHAUSTION_TRAP`
