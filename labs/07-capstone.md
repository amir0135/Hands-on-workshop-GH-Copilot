# Lab 7: Capstone — Build & Ship a Feature as a Team

> **Track:** Core workshop · 8 of 8 — capstone

**Duration:** ~15 min kickoff in-session, then self-paced / team build (45–90 min)
**Goal:** Put the entire day together. In a small team (or solo), take a feature from idea to reviewed, tested, documented code — using your instructions, prompt files, custom modes, and the agentic loop. This is where the skills stop being exercises and become *how you work*.

> **🧭 Jumping in cold?** The capstone is the one lab that explicitly draws on earlier work. You can still do it standalone — wherever the checklist references Labs 1, 3, 4, or 9, just do that step from scratch inline (e.g. "create a `copilot-instructions.md` now" instead of "use the one from Lab 1"). Expect the build to take a bit longer the first time.

**Quick start:**

```bash
mkdir -p sandbox/specs sandbox/.github/prompts sandbox/.github/chatmodes
code sandbox     # open sandbox as the workspace root
```

> **Everyone participates.** 🌱 Newcomers own the spec, tests, and review checklist — high-value, no deep coding required. 🚀 Advanced users drive the agentic build and the custom modes. Mixed teams produce the best results.

---

## How It Works

1. **Form teams of 2–4** (or go solo). Mix experience levels if you can.
2. **Pick ONE challenge** from the menu below (or bring your own real feature).
3. **Use everything from today.** The scoring rewards process, not just working code.
4. **Timebox it.** Quality of process over quantity of features. A small, well-built, well-reviewed feature beats a sprawling broken one.
5. **Demo for 3 minutes** at the end: show the spec, the diff, the tests, and one thing Copilot got wrong that you caught.

---

## Challenge Menu

Pick the one that's closest to your real work.

### Challenge A — URL Shortener Service
A service that accepts a long URL and returns a short code; resolving the code redirects.
- Validate input URLs; reject malformed ones
- Generate collision-free short codes
- Track hit counts per code
- List all shortened URLs with their stats
- In-memory storage; no real persistence required

### Challenge B — Expense Splitter
Given a group and a list of expenses, compute who owes whom.
- Add people and expenses (payer, amount, participants)
- Compute net balances per person
- Produce a minimal set of "settle-up" transactions
- Handle edge cases: uneven splits, a person in zero expenses, rounding

### Challenge C — Feature Flag Evaluator
A small library that decides if a feature is on for a given user.
- Flags with rules: all-on, all-off, percentage rollout, user allowlist
- Deterministic bucketing (same user → same result)
- Validate flag configs; reject contradictory rules
- Explain *why* a flag evaluated the way it did (for debugging)

### Challenge D — Your Real Backlog Item
Bring a genuine small feature or bug from your actual project. Often the most valuable option.

---

## The Process (use the whole day's toolkit)

Work the agentic loop deliberately. Tick these off as you go:

- [ ] **Spec first** ([Lab 4](04-agentic-workflows.md)) — write a short spec in `sandbox/specs/` before any code
- [ ] **Refine requirements** ([Lab 4 Ex. 5](04-agentic-workflows.md#exercise-5-requirements--refinement-before-code)) — have Copilot interview you / poke holes in the spec
- [ ] **Instructions active** ([Lab 1](01-team-configuration.md)) — your `copilot-instructions.md` is in place and shaping output
- [ ] **Diagram the design** ([Lab 4 Ex. 6](04-agentic-workflows.md#exercise-6-architecture--diagrams-from-specs)) — a quick Mermaid sequence or flow diagram, reviewed before coding
- [ ] **Build incrementally** ([Lab 2](02-agent-mode-mastery.md), [Lab 4](04-agentic-workflows.md)) — small agent steps, review every diff like a PR
- [ ] **Tests that verify behaviour** ([Lab 5](05-quality-and-review.md)) — not just "no exception thrown"
- [ ] **Run a review pass** ([Lab 5](05-quality-and-review.md) / [Lab 9](09-chat-modes-and-subagents.md)) — use your `code-review.prompt.md` or **reviewer** chat mode
- [ ] **Debug honestly** ([Lab 6](06-debugging-and-legacy-code.md)) — when something breaks: Understand → Reproduce → Fix → Verify
- [ ] **Document it** ([Lab 9](09-chat-modes-and-subagents.md)) — docs-writer mode or a docs prompt on the final result
- [ ] **Capture a lesson** ([Lab 3](03-prompt-files-and-instructions.md)) — add one line to `lessons.md` about something that surprised you

---

## Roles for a Balanced Team

Rotate or split by comfort level:

| Role | Owns | Great for |
|------|------|-----------|
| **Spec & requirements** | The spec, edge cases, acceptance criteria | 🌱 Newcomers, PMs, analysts |
| **Driver** | Runs agent mode, steers the build | 🚀 Comfortable users |
| **Reviewer** | Reviews every diff, runs the review prompt/mode | Anyone — this is the key skill |
| **QA** | Owns tests and the debugging loop | QA / automation folks, 🌱 newcomers |
| **Scribe** | Captures lessons, prompts that worked, the demo notes | Anyone |

> The **Reviewer** role is non-negotiable on every team. Someone must read the diffs.

---

## Scoring Rubric (self-assess or facilitator-judged)

Process beats output. 100 points:

| Criterion | Points | What we're looking for |
|-----------|-------:|------------------------|
| Spec-first | 15 | A real spec existed before code; requirements were refined |
| Review discipline | 20 | Every diff was reviewed; at least one Copilot mistake was caught and fixed |
| Test quality | 20 | Tests verify behaviour and cover edge cases, not just the happy path |
| Use of customization | 15 | Instructions / prompt files / a custom mode actively shaped the work |
| Debugging method | 10 | When something broke, the Understand → Reproduce → Fix → Verify loop was used |
| Working feature | 10 | It runs and does what the spec says |
| Documentation & lesson | 10 | Final code is documented; one lesson captured |

> A team that ships less but reviews rigorously and catches Copilot's mistakes **scores higher** than a team that vibe-codes a bigger feature. That's the entire point of the day.

---

## The 3-Minute Demo

Each team shows:

1. **The spec** — what you set out to build
2. **The diff** — one part Copilot nailed, one part you had to redirect
3. **The tests** — run them live
4. **The catch** — the most important thing Copilot got wrong that your review caught
5. **One takeaway** — what you'll do differently on Monday

---

## 🚀 Advanced Stretch (for teams that finish early)

1. **Add a second feature** that forces a refactor of the first — exercise the agent on *changing* existing code.
2. **Wire in a custom chat mode** you built in Lab 9 as a required gate before "done."
3. **Generate a PR description** with Copilot summarising the change, the tests, and the review findings.
4. **Token retro** — review your transcript and identify where you wasted tokens; rewrite one prompt to be 50% leaner.

---

## 💬 Debrief

As a whole room:

1. **What surprised you** about working this way for a full feature?
2. **Where did review catch the most value?**
3. **What will you set up first** on your real repo on Monday — instructions, a prompt file, or a custom mode?
4. **What's your team's biggest risk** with Copilot, and which practice from today most reduces it?

---

## Key Takeaways

- The day's skills only matter when **combined on real work** — that's what the capstone proves
- **Process discipline** (spec, review, tests, honest debugging) is what makes Copilot a multiplier instead of a debt machine
- **Everyone has a role** — review and QA are as valuable as driving the agent
- The best outcome isn't the biggest feature; it's the team that **caught what Copilot got wrong**
- Leave with **one concrete thing to set up Monday morning**

---

**Previous:** [Lab 6: Debugging & Taming Legacy Code ←](06-debugging-and-legacy-code.md) · **Back to:** [Workshop README →](../README.md)

**Bonus / self-paced:** [Lab 8: MCP →](08-mcp-concepts.md) · [Lab 9: Custom Chat Modes & Subagents →](09-chat-modes-and-subagents.md) · [Lab 10: Beyond the Editor →](10-advanced-topics.md) · [Lab 11: Copilot CLI Deep Dive →](11-copilot-cli.md)
