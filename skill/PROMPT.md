Build a world-class, premium Apple-designed web application: "V75 Price Action AI Hub" — an institutional chart audit desk and trade journal for Volatility 75 (V75) price action traders.

DESIGN AESTHETIC — APPLE PRO STUDIO:
- Style: Apple Human Interface Guidelines / visionOS luxury aesthetic. Deep midnight dark mode (#09090B) and crisp off-white light mode (#FBFBFD).
- Surfaces: Ultra-refined glassmorphism with backdrop-blur-2xl, translucent panels (bg-card/75), 1px hairline borders (border-border/40), and soft ambient shadows.
- Typography: SF Pro / Inter display hierarchy with tight tracking, monospaced tabular numerals for prices and R:R ratios.
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
