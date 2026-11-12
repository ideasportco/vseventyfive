# VSEVENTYFIVE — V75 Price Action AI Auditor

An open, rule-based AI skill pack and web app for auditing **Volatility 75 (V75)** chart screenshots.
Any vision AI (Claude, ChatGPT, Gemini, or a free local model) can use it. You don't need to train or fine-tune anything: the AI reads the rules from this repo every time.

Every chart goes through a strict **4-gate checklist** and gets one verdict: **ENTER**, **WATCH**, or **NO_TRADE**.

| Gate | Checks |
|---|---|
| 1. Structure | Trend, key level, pattern, 3-touch trendline, 200 EMA bias, flag slope |
| 2. Breakout & Retest | Candle body close beyond the level, then a retest |
| 3. Trigger | Pin bar, engulfing, or railway track at the retest |
| 4. Risk | Stop + (spread + 0.2 × ATR) buffer, minimum 1:3 reward-to-risk |

> Educational tool only. Not financial advice. Synthetic indices are high risk.

---

## Repository layout

```
skill/                      ← The portable "brain". No code needed.
  AUDITOR_PROMPT.md         ← Paste as system prompt / custom instructions
  SKILL.md                  ← Full auditor specification
  rules/
    01_breakout_retest.md
    02_candlestick_triggers.md
    03_risk_and_buffers.md
    04_trade_management.md
    05_universal_price_action.md   ← 3-touch, 200 EMA, H&S, wedges, flags, triangles
  schemas/                  ← JSON output schemas (evaluation, journal)
  cases/                    ← Reference case template + governance
  evals/ scripts/           ← Blind evaluation runner, Deriv candle downloader
src/                        ← Web app: Audit Desk, Review Log, local AI worker API
```

---

## Use it with Claude (Projects)
1. Create a new Project at claude.ai.
2. **Project knowledge** → upload `skill/SKILL.md` and every file in `skill/rules/`.
3. **Project instructions** → paste the contents of `skill/AUDITOR_PROMPT.md`.
4. Start a chat and attach an MT5 screenshot.

## Use it with ChatGPT (Custom GPT)
1. Explore GPTs → **Create** → **Configure**.
2. **Instructions** → paste `skill/AUDITOR_PROMPT.md`.
3. **Knowledge** → upload `skill/SKILL.md` and `skill/rules/*.md`.
4. Save, share the link, and send it a chart.

On free plans without Projects/GPTs, paste `AUDITOR_PROMPT.md` + `rules/05_universal_price_action.md` as your first message, then attach the chart.

## Use it free and offline (Ollama)
```sh
ollama pull qwen2.5vl
# then send the chart image with skill/AUDITOR_PROMPT.md + SKILL.md as the system prompt
```
LM Studio works the same way with any vision model.

## Run the web app
Requires [Bun](https://bun.sh) (or Node 20+).
```sh
git clone <your-repo-url>
cd <repo>
bun install
bun run dev
```
The app includes the Audit Desk (upload, cloud or local AI review, Gate 4 calculator) and the Review Log.
Local AI workers can pull pending reviews from `GET /api/public/reviews/queue` and submit results to `POST /api/public/reviews/:id/verdict` using an `X-Api-Key` header.

## Tests
```sh
bunx vitest run
```
The deterministic risk math (buffers, R:R, break-even, stagnation) is unit-tested.

---

## Sources
- Classical price action (Laurentiu Damir, Bob Volman, *Simple Trading Book*) — rules 01–04.
- T. Chiparange, *Universal Price Action V1* (Supreme Traders) — rule 05.

Rules are summaries and adaptations, not reproductions of the books.

## Contributing
Rule changes need evidence across multiple journaled cases (see `skill/cases/GOVERNANCE.md`). One trade never changes a rule. Open an issue with charts and outcomes.

## License
MIT — see `LICENSE`.
