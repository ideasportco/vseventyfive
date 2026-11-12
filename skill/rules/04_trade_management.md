# Rulebook 04: Trade Management & Stagnation Protocol

## 1. Stagnation Invalidation (The 8-Candle M5 Rule)
Pure price-action breakout-retests rely on prompt follow-through. Once a genuine rejection prints at the neckline, the market should impulsively move away from the level.

- **Threshold**: **8 consecutive M5 candles (40 minutes)** following trade entry.
- **Condition**: If price has not reached at least $+1.0\text{R}$ of open profit, or if price begins printing consecutive doji/micro-candles around the entry neckline:
  - **Action**: The market has lost directional momentum.
  - **Directive**: Move Stop Loss to Break-Even (entry price) or execute an immediate Scratch Market Exit.
  - **Rationale**: Prolonged stagnation at a broken level sharply increases the probability of a structural failure and stop-hunt.

## 2. Trailing & Profit Lock Milestones
- **Milestone 1 (+1.5R)**: Automatically adjust Stop Loss to Break-Even ($+0.1\text{R}$ to cover commissions/spread).
- **Milestone 2 (+2.0R)**: Lock in $+1.0\text{R}$ of profit by trailing stop below the most recent M5 swing low (for longs) or above the most recent swing high (for shorts).
- **Target (+3.0R+)**: Exit full position at predetermined structural target. Do not greedily hold past major opposing levels.
