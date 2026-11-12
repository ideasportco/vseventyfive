# Rulebook 02: Candlestick Rejection Triggers

## 1. Purpose
The trigger candle provides real-time verification that buyers (in long setups) or sellers (in short setups) have actively defended the retested boundary.

## 2. Permitted Trigger Formations

### Form A: The Rejection Pin Bar
- **Anatomy**:
  - Small real body located at one extreme of the candle range.
  - Long tail (wick) protruding toward and through the retest level.
  - Rejection tail length must be at least **$2.0 \times$ the real body height**.
  - Opposite tail must be minimal or non-existent ($\le 0.2 \times$ body).
- **Directional Bias**:
  - Long: Long lower wick rejecting broken resistance (new support).
  - Short: Long upper wick rejecting broken support (new resistance).

### Form B: Bullish / Bearish Engulfing
- **Anatomy**:
  - Candle 1 touches or retests the key boundary.
  - Candle 2 opens at or near Candle 1's close and closes with a strong directional body that **completely covers Candle 1's entire body**.
  - Long: Bullish green body engulfs preceding bearish retest candle.
  - Short: Bearish red body engulfs preceding bullish retest candle.

## 3. Strict Disqualification Blacklist
The following candles at the retest level **strictly prohibit entry**:
1. **Doji & Long-Legged Doji**: Open and close virtually identical; indicates equilibrium/indecision, not defense.
2. **Spinning Tops**: Small body centered between two equal-length wicks.
3. **Inside Bars**: Candle completely contained within previous candle's range.
4. **Weak Reversal**: A candle with closing price failing to cross the midpoint of the prior bar.

*Rule: If an indecision candle forms at the retest, maintain a `WATCH` status and wait for the subsequent bar to deliver an authoritative rejection or engulfing close.*
