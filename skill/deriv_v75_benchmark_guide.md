# Deriv Volatility 75 (V75) Price Action AI Evaluation Benchmark

This benchmark dataset contains **50 verified historical chart scenarios** extracted directly from real Deriv Volatility 75 (R_75) M5 tick data. It is designed to train, prompt, and grade any AI agent on pure price action execution according to core published texts.

## 1. Setup Archetype Distribution

| Setup Archetype | Foundational Book | Count | Primary Execution Rule |
| :--- | :--- | :--- | :--- |
| **Brooks Second Entry (High 2 Pullback)** | Al Brooks - Reading Price Charts Bar by Bar (Ch. 4: Pullbacks & Second Entries) | 35 | Brooks High 2 / Low 2 pullback |
| **Damir Support Zone False-Break Rejection** | Laurentiu Damir - Price Action Breakdown (Support & Demand Traps) | 5 | Damir liquidity sweep & wick rejection |
| **Volman Pre-Breakout Build-Up (Block Break)** | Bob Volman - Understanding Price Action (Ch. 2: Squeeze and Block Breaks) | 2 | Volman pre-breakout build-up |
| **Damir Resistance Zone False-Break Rejection** | Laurentiu Damir - Price Action Breakdown (Resistance & Supply Traps) | 8 | Damir liquidity sweep & wick rejection |

## 2. Evaluation Protocol for AI Agents

To test an AI agent using this benchmark:
1. **Input:** Pass the AI the scenario metadata, the key inflection level, and the trigger candle OHLC values without showing the `trade_parameters` or `evaluation_outcome`.
2. **Task Prompt:** Instruct the AI: *"Analyze this Deriv V75 M5 chart setup. Identify the market regime, state whether an entry is warranted (Long / Short / No Trade), and define your exact Entry, Stop Loss, and Take Profit levels according to Volman and Damir principles."*
3. **Grading Rubric (Score 0 to 100):**
   - **Direction & Setup Recognition (30 pts):** Did the AI correctly classify the setup archetype and market bias?
   - **Invalidation Accuracy (30 pts):** Did the AI set the Stop Loss just behind the compression block / rejection wick (rather than an arbitrary fixed pip/point distance)?
   - **Risk-to-Reward Discipline (20 pts):** Did the AI target a minimum of 1:2 R:R based on measured move expansion?
   - **Narrative Reasoning (20 pts):** Did the AI cite candle anatomy, baseline EMA interaction, and rejection mechanics?

## 3. Sample Scenarios Preview

### Scenario V75-PA-001: Brooks Second Entry (High 2 Pullback) (BULLISH)
- **Timestamp:** `2026-10-25 16:10 UTC`
- **Literature Reference:** Al Brooks - Reading Price Charts Bar by Bar (Ch. 4: Pullbacks & Second Entries)
- **Key Inflection Level:** `35430.42`
- **Trigger Candle:** Open `35402.5074`, High `35495.608`, Low `35387.4225`, Close `35474.5476` (EMA21: `35430.42`)
- **Benchmark Parameters:** Entry `35474.55` | SL `35360.36` | TP1 `35702.92` | TP2 `35817.1` (1:2 to 1:3)
- **Forward Realized Outcome:** `STOPPED_OUT`
- **Evaluation Goal:** *Did the AI identify the existing bullish trend, count the two-legged retracement touching the 21 EMA baseline, and fire on the High 2 confirmation bar?*

### Scenario V75-PA-002: Damir Support Zone False-Break Rejection (BULLISH)
- **Timestamp:** `2026-10-25 18:05 UTC`
- **Literature Reference:** Laurentiu Damir - Price Action Breakdown (Support & Demand Traps)
- **Key Inflection Level:** `34829.79`
- **Trigger Candle:** Open `34827.6199`, High `34872.0764`, Low `34764.671`, Close `34857.2253` (EMA21: `34990.55`)
- **Benchmark Parameters:** Entry `34857.23` | SL `34742.12` | TP1 `35087.43` | TP2 `35202.54` (1:2 to 1:3)
- **Forward Realized Outcome:** `STOPPED_OUT`
- **Evaluation Goal:** *Did the AI identify the historical swing low, recognize the lower-wick probe below the level, and flag the rejection pin bar as a bullish reversal signal?*

### Scenario V75-PA-003: Volman Pre-Breakout Build-Up (Block Break) (BEARISH)
- **Timestamp:** `2026-10-25 22:10 UTC`
- **Literature Reference:** Bob Volman - Understanding Price Action (Ch. 2: Squeeze and Block Breaks)
- **Key Inflection Level:** `34696.52`
- **Trigger Candle:** Open `34711.6275`, High `34711.6275`, Low `34543.0219`, Close `34550.7667` (EMA21: `34756.8`)
- **Benchmark Parameters:** Entry `34550.77` | SL `34832.29` | TP1 `33987.73` | TP2 `33706.21` (1:2 to 1:3)
- **Forward Realized Outcome:** `HIT_TP`
- **Evaluation Goal:** *Did the AI detect the range compression above support, verify the bearish marubozu-like close, and set the invalidation stop directly above the compression ceiling?*

### Scenario V75-PA-004: Damir Support Zone False-Break Rejection (BULLISH)
- **Timestamp:** `2026-10-26 02:10 UTC`
- **Literature Reference:** Laurentiu Damir - Price Action Breakdown (Support & Demand Traps)
- **Key Inflection Level:** `33711.51`
- **Trigger Candle:** Open `33746.5266`, High `33778.116`, Low `33696.5578`, Close `33756.5104` (EMA21: `33638.57`)
- **Benchmark Parameters:** Entry `33756.51` | SL `33674.14` | TP1 `33921.25` | TP2 `34003.62` (1:2 to 1:3)
- **Forward Realized Outcome:** `STOPPED_OUT`
- **Evaluation Goal:** *Did the AI identify the historical swing low, recognize the lower-wick probe below the level, and flag the rejection pin bar as a bullish reversal signal?*

### Scenario V75-PA-005: Brooks Second Entry (High 2 Pullback) (BULLISH)
- **Timestamp:** `2026-10-26 07:10 UTC`
- **Literature Reference:** Al Brooks - Reading Price Charts Bar by Bar (Ch. 4: Pullbacks & Second Entries)
- **Key Inflection Level:** `32617.72`
- **Trigger Candle:** Open `32568.1473`, High `32695.6558`, Low `32563.2`, Close `32669.6679` (EMA21: `32617.72`)
- **Benchmark Parameters:** Entry `32669.67` | SL `32540.6` | TP1 `32927.81` | TP2 `33056.88` (1:2 to 1:3)
- **Forward Realized Outcome:** `STOPPED_OUT`
- **Evaluation Goal:** *Did the AI identify the existing bullish trend, count the two-legged retracement touching the 21 EMA baseline, and fire on the High 2 confirmation bar?*

## 4. Full Dataset Access

The complete dataset with all 50 scenarios, exact OHLC arrays, and evaluation schemas is stored in `deriv_v75_price_action_scenarios.json`.