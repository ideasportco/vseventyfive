# V75 Price Action AI Hub: Master Progress & Apple-Style Handoff Pack

> **Purpose:** This document is a complete, self-contained handoff specification and copy-paste prompt pack. You can supply this directly to a new Lovable account or project to seamlessly resume, build, and polish the **V75 Price Action AI Chart Auditor** with a signature, ultra-premium Apple-inspired visual and interaction design.

---

## Part 1: Project Vision & Core Engine

### 1.1 What We Are Building
A specialized, institutional-grade chart evaluation web app and trade journal tailored for **Deriv Volatility 75 (V75)** synthetic index price action trading. 

The system operates as an **objective AI Trading Desk Auditor** based on the foundational principles of pure price action books (Al Brooks, Bob Volman, Laurentiu Damir, Steve Nison, and *Forex Simplified*):
1. **Multimodal Screenshot Ingestion:** Traders upload MetaTrader 5 (MT5) chart screenshots (M5 execution, with optional H1/H4 context).
2. **The 4-Gate Decision Engine:**
   - **Gate 1 (Market Structure):** Identifies macro swing highs/lows, breakout levels, or chart patterns (Double Tops/Bottoms, Head & Shoulders, Flags, Consolidation Boxes).
   - **Gate 2 (Breakout Confirmation):** Demands a clean candle body close *beyond* the structural boundary (wick-only violations fail).
   - **Gate 3 (Retest & Trigger):** Requires price to return to the broken level and print an explicit rejection candle (pin bar, hammer, engulfing, railway track) in the direction of the trade.
   - **Gate 4 (Execution Buffers & 1:3 R:R):** Validates that the stop loss incorporates synthetic spread buffers (`Spread + 0.2 × ATR(14)`) beyond the invalidation wick, and that the projected structural target provides at least a **1:3 Reward-to-Risk ratio**.
3. **Dual Model Architecture:**
   - **External AI:** Native cloud vision review evaluated instantly against the full prompt contract.
   - **Local AI Worker:** An asynchronous queue (`/api/public/reviews/queue` and `/api/public/reviews/:id/verdict`) protected by API key auth so traders can run local vision LLMs (Llama 3.2 Vision, Qwen2-VL, Claude Desktop, LM Studio) or private automated scripts.
4. **Before/After Trade Journal & Reflection Loop:** Upload the initial setup chart for pre-trade audit, then upload the outcome chart later to evaluate win/loss excursions, stagnation flags, and post-trade lessons.

---

## Part 2: Premium Apple Design System & Aesthetic Directives

To match the world-class fidelity of Apple hardware showcases and macOS/visionOS flagship software, the entire user interface must adhere to the following design system:

### 2.1 Aesthetic Archetype: Apple Pro Studio / Cupertino Glass
- **Visual Feel:** Refined, distraction-free, luxurious, and ultra-crisp. Like Apple's Final Cut Pro, Logic Pro, or the Apple Developer app.
- **Glassmorphism & Surface Depth:**
  - Layered frosted glass panels with `backdrop-blur-2xl` and subtle translucent fills (`bg-zinc-900/60` dark, `bg-white/70` light).
  - Hairline borders: ultra-subtle 1px borders (`border-white/10` in dark mode, `border-black/5` in light mode).
  - Diffuse ambient shadows: multi-layered soft drop shadows (`shadow-[0_20px_50px_rgba(0,0,0,0.25)]`).
- **Typography:**
  - SF Pro / Inter display hierarchy with tight letter-spacing (`tracking-tight` on headings).
  - Monospaced tabular numerals (`font-mono tabular-nums`) for currency values, price levels, ATR, and R:R ratios to ensure zero horizontal jitter during recalculations.
- **Color Palette:**
  - **Base:** Deep Space Gray / Midnight OLED dark canvas (`#09090B` / `#121214`) and pristine Pure Snow / Off-White light canvas (`#FBFBFD` / `#F5F5F7`).
  - **Verdict Accent System:**
    - `ENTER`: Apple Electric Emerald (`#30D158` / `#34C759`) with soft emerald glow.
    - `WATCH`: Apple Warm Amber / Marigold (`#FF9F0A` / `#FF9500`).
    - `NO-TRADE`: Apple Vivid Crimson (`#FF453A` / `#FF3B30`).
    - `Accent Primary`: Apple Pro Blue (`#0071E3` / `#0A84FF`).
- **Micro-Interactions & Motion:**
  - Fluid spring physics transitions (`transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]`).
  - Tactile drag-and-drop zone with smooth file-hover scale (`scale-[1.01]`) and subtle glowing neon border on drag-over.
  - Interactive Chart Inspector: full-screen image expander with fluid zoom/pan, crosshair coordinate inspection, and collapsible right-hand verdict inspector drawer.
  - Segmented control pills with smooth sliding background indicator for switching between "All Reviews", "ENTER", "WATCH", and "Local Queue".

---

## Part 3: What Has Been Built So Far (Current Workspace State)

### 3.1 Repository Assets & Specifications (17 Verified Files)
1. `SKILL.md`: Core system prompt contract defining prompt requirements and schema outputs.
2. `rules/01_breakout_retest.md`: Breakout identification, candle close rules, retest logic.
3. `rules/02_candlestick_triggers.md`: Pin bars, engulfing bars, railway tracks, wick-to-body ratios.
4. `rules/03_risk_and_buffers.md`: Spread buffer formula (`Spread + 0.2 × ATR`), synthetic slippage protection, 1:3 R:R minimum.
5. `rules/04_trade_management.md`: M5 8-candle time stagnation rule, break-even shift rules.
6. `schemas/evaluation.json`: JSON Schema enforcing verdict, gate statuses, levels, and limitations.
7. `schemas/journal_entry.json`: Schema for tracking pre-trade and post-trade outcomes.
8. `cases/CASE_TEMPLATE.md` & `case_governance.md`: Protocol for post-mortem reviews without rule pollution.
9. `evals/validation_protocols.md`: Empirical protocols for vision price scale verification and synthetic edge testing.
10. `scripts/download_v75_candles.py`: Deriv WebSocket historical candle downloader.
11. `scripts/run_eval_benchmark.py`: Blind scenario evaluation test runner.
12. `v75_complete_project_backup.json` & `.md`: Complete durable backups published in the workspace.

### 3.2 Working Web Application ("Chart Review Hub")
- **Tech Stack:** TanStack Start, React 19, TypeScript, Tailwind CSS, shadcn/ui components, Lovable Cloud (Supabase Postgres & Storage).
- **Core Endpoints Implemented:**
  - `POST /api/reviews` (Upload chart image, choose External AI or Local AI review).
  - `GET /api/public/reviews/queue` (Poll pending reviews for local worker LLMs).
  - `POST /api/public/reviews/:id/verdict` (Submit worker evaluation with API key authentication).
- **Embedded Prompt Engine:** `src/lib/server/skill-prompt.ts` compiles the complete 4-gate rules into the system prompt for native AI evaluation.

---

## Part 4: Complete Copy-Paste Prompt for New Lovable Account

Copy the entire block below and paste it as the first message into your new Lovable project:

```text
Build a world-class, premium Apple-designed web application: "V75 Price Action AI Hub" — an institutional chart audit desk and trade journal for Volatility 75 (V75) price action traders.

DESIGN AESTHETIC — APPLE PRO STUDIO:
- Style: Apple Human Interface Guidelines / visionOS luxury aesthetic. Deep midnight dark mode (#09090B) and crisp off-white light mode (#FBFBFD).
- Surfaces: Ultra-refined glassmorphism with backdrop-blur-2xl, subtle translucent panels (bg-card/75), 1px hairline borders (border-border/40), and soft ambient shadows.
- Typography: SF Pro/Inter display hierarchy with tight tracking, monospaced tabular numerals for prices and R:R ratios.
- Accents: Apple Emerald (#30D158) for ENTER, Warm Amber (#FF9F0A) for WATCH, Crimson (#FF453A) for NO-TRADE, and Apple Blue (#0A84FF) for actions.
- Motion: Fluid spring transitions, smooth pill tabs, tactile drag-and-drop with glow border, and a responsive chart inspector with smooth zoom/pan modal.

CORE FEATURES TO BUILD:

1. CHART AUDIT & UPLOAD DESK:
   - Drag-and-drop MT5 screenshot uploader with image preview, timeframe selector (M1, M5, M15, H1, H4), and reviewer mode toggle ("Native AI Vision" vs "Local AI Queue").
   - Instant multimodal evaluation engine that enforces the strict 4-Gate Price Action Strategy:
     * Gate 1: Structure/Pattern Identification (Breakout boundary, Key S/R level).
     * Gate 2: Breakout Candle Body Close beyond level (wick-only breaks fail).
     * Gate 3: Retest of broken level + Reversal Trigger Candle (pin bar, engulfing, railway track).
     * Gate 4: Spread Buffer (Spread + 0.2 ATR) & strict 1:3 minimum Reward-to-Risk ratio.
   - Evaluator returns a strictly formatted Verdict Badge (ENTER, WATCH, NO-TRADE), confidence score, gate-by-gate pass/fail breakdown, precise trade parameters (Entry, Stop Loss with spread buffer, Target), and trade management notes (e.g. 8-candle M5 stagnation rule).

2. SHARED LOCAL & EXTERNAL AI WORKER API:
   - Secure endpoints for local AI workers (Ollama, LM Studio, Claude Desktop):
     * GET /api/public/reviews/queue (fetches pending reviews awaiting local verdict).
     * POST /api/public/reviews/:id/verdict (submits verdict matching the evaluation JSON schema, authenticated via X-Api-Key).
   - "Local AI Worker Setup" modal inside the app providing ready-to-run Python and cURL worker scripts and API key management.

3. INTERACTIVE CHART INSPECTOR & REVIEW LOG:
   - Grid and Table view of past chart reviews with filterable pills (All, ENTER, WATCH, NO-TRADE, Local vs Cloud).
   - Clicking a review opens a macOS-style split inspector: high-res chart on the left with pan/zoom, and expandable audit card on the right displaying all 4 gates, invalidation levels, and detected patterns.

4. BEFORE & AFTER TRADE REFLECTION JOURNAL:
   - Ability to pair an "After Trade" outcome screenshot with the original pre-trade audit.
   - Tag trade outcome: Win (+3R Target hit), Scratch (Stagnation/Break-even exit), or Loss (Stop hit).
   - Reflection field that logs lessons learned and stores them in a searchable Case Memory database to track historical edge without polluting core strategy rules.

5. USER AUTHENTICATION & CLOUD DATABASE:
   - Lovable Cloud authentication (email/password and social login) so each trader has their own private chart reviews, journal entries, and personal API keys, while supporting public demo reviews.

Start by setting up the database tables (reviews, journal_entries, api_keys), configuring storage buckets for chart screenshots, and building the Apple-styled desktop layout.
```

---

## Part 5: Step-by-Step Continuation Roadmap

When starting the new Lovable project with the prompt above, follow this sequence:

| Phase | Milestone | Expected Deliverable |
|---|---|---|
| **Phase 1** | **Apple Visual System & Layout** | Navigation bar with blurred glass header, theme toggle, hero drag-and-drop zone, and segmented verdict filter tabs. |
| **Phase 2** | **Backend & Vision Review Engine** | Supabase database schema for reviews, chart storage bucket, and multimodal review execution with the 4-gate prompt contract. |
| **Phase 3** | **Local AI API & Worker Modal** | API key generation in user settings, queue polling endpoint, and copyable Python worker script for local models. |
| **Phase 4** | **Before/After Journaling Loop** | Outcome linking, excursion logging (+1R time, max adverse excursion), and post-mortem review cards. |
| **Phase 5** | **Polish & Micro-Interactions** | Framer motion spring effects, keyboard shortcuts (`Cmd+U` upload, `Esc` close modal), and high-resolution chart pan/zoom. |

---

## Part 6: Strategy Reference Quick Cheat-Sheet

| Element | Rule / Formula | Failure Condition |
|---|---|---|
| **Gate 1: Structure** | Must identify key swing high/low, neckline, or consolidation boundary on visible chart. | Chaotic mid-range chop without clear boundary. |
| **Gate 2: Breakout** | Must have at least one candle body close entirely beyond the structural line. | Wick-only penetration followed by immediate close back inside. |
| **Gate 3: Retest & Trigger** | Retest touches broken level; prints rejection candle (wick >= 2x body or engulfing body). | Price blows through retest level without hesitation. |
| **Gate 4: Buffer & R:R** | Stop Loss = Invalidation Pivot + Spread Buffer (`Spread + 0.2 × ATR`). Target >= 3 × Risk. | Target < 3x Risk or stop sits flush on wick without spread buffer. |
| **Stagnation Rule** | Position must achieve at least +1R within 8 candles on M5 (40 mins). | Stalls at neckline for 8+ candles -> move stop to break-even or scratch. |

---
*End of Master Progress & Apple Handoff Pack.*
