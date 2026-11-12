# Rulebook 03: Risk, Buffers & Mathematical Expectancy

## 1. The Synthetic Spread & Slippage Asymmetry
In MT5, charts plot the **Bid price** exclusively. 
- A **Long trade** enters at the Ask and closes at the Bid (Stop Loss triggers at Bid).
- A **Short trade** enters at the Bid and closes at the Ask (Stop Loss triggers at Ask).

Because short stops trigger at the Ask price, placing a stop loss flush against a swing high wick guarantees premature stop-outs during spread spikes, even if the chart never visibly touches the level.

## 2. Invalidation Buffer Formula
For all setups, calculate Stop Loss with a structural buffer:

### Long Positions:
$$\text{Stop Loss} = \text{Low of Retest Pivot Wick} - (\text{Spread} + 0.2 \times \text{ATR}(14))$$

### Short Positions:
$$\text{Stop Loss} = \text{High of Retest Pivot Wick} + (\text{Spread} + 0.2 \times \text{ATR}(14))$$

*Fallback*: If ATR(14) is unavailable from chart OCR, apply a baseline buffer equal to $1.5 \times$ the observable broker spread.

## 3. Reward-to-Risk (R:R) Mandate
- Potential profit target is measured from Entry to the next major structural swing level or 100% measured pattern projection.
- Strict Threshold:
  $$\text{R:R} = \frac{|\text{Target Price} - \text{Entry Price}|}{|\text{Entry Price} - \text{Stop Loss}|} \ge 3.0$$
- **Enforcement**:
  - If calculated R:R is $< 3.0$, the trade must be **rejected** (`NO-TRADE`).
  - No compromises: Never artificially tighten the stop loss inside structural invalidation just to manufacture a 1:3 ratio.
