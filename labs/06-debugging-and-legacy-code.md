# Lab 6: Debugging & Taming Legacy Code

> **Track:** Core workshop · 7 of 8

**Duration:** ~25 min in-session (core exercises); ~45 min for the full lab self-paced
**Goal:** Use Copilot where it quietly delivers the most day-to-day value: fixing failing code and making sense of unfamiliar, undocumented, or legacy codebases. By the end you'll have a repeatable loop for "I didn't write this and it's broken."

> **🌱 Foundation path:** Exercises 1–3 — reproduce a bug, get Copilot to explain it, and fix it with a test that proves the fix. These are the everyday wins.
> **🚀 Advanced stretch:** Exercises 4–5 plus the stretch section — characterization tests, safe refactoring of code with no tests, and onboarding-by-agent on a real repo.

---

## Why This Matters

Most developers spend far more time reading and fixing code than writing new features. Copilot is exceptional at:

- Explaining code nobody on the team remembers writing
- Forming hypotheses about *why* something fails
- Generating a failing test that reproduces a bug before you fix it
- Refactoring safely once tests exist
- Onboarding you to an unfamiliar repo in minutes instead of days

The risk is the same as everywhere else: it will confidently guess. Your job is to make it **prove** its claims against the actual code and runtime behaviour.

---

## Setup: Plant a Bug to Hunt

We need something broken. In **Agent** mode, generate a small program *with a deliberate, subtle bug* so everyone has a realistic target.

```
In sandbox/debugging, create a small [your language] module that:
- Parses a list of order records (id, quantity, unit_price)
- Computes the total per order and a grand total
- Applies a 10% discount only when an order's total exceeds 100
- Returns a summary object

Then write 4 unit tests. Intentionally introduce ONE subtle off-by-one or
boundary bug (e.g. the discount triggers at >= 100 instead of > 100), but do
NOT tell me where it is. Make sure at least one test still passes so it looks healthy.
```

Run the tests. You should see a mix of passing and failing — or worse, all passing while the logic is subtly wrong. Now you have a realistic bug hunt.

---

## Exercise 1: Make Copilot Explain Before It Fixes

Resist the urge to say "fix it." First, understand.

### Step 1: Ask for an explanation grounded in the code

In **Ask** mode (cheaper, no edits), with the file open:

```
Explain what this module does step by step. Where are the boundary conditions,
and which lines are most likely to contain an off-by-one or comparison bug? 
Don't fix anything yet — just reason about it.
```

### Step 2: Demand evidence

Follow up:

```
For the discount logic specifically: walk through what happens for an order
total of exactly 100. Quote the exact line that decides this.
```

> **Why this matters:** Forcing Copilot to quote the actual line and trace a specific input is how you catch it bluffing. If it can't point to a line, don't trust the explanation.

---

## Exercise 2: Reproduce With a Failing Test

A bug isn't understood until you can reproduce it on demand.

```
Write a single focused test that demonstrates the discount boundary bug —
an input where the current code gives the wrong answer. Name it clearly.
Run it and confirm it fails for the right reason.
```

Review the test. Ask yourself:
- Does the test actually target the bug, or a symptom?
- Is the expected value correct *per the spec*, not per the buggy code?

---

## Exercise 3: Fix It — Minimally

```
Now fix the bug with the smallest possible change. Do not refactor anything else.
Re-run all tests and show me they pass. Explain in one sentence what was wrong.
```

**Review the diff carefully.** The most common Copilot debugging failure is "fixing" the test to match the buggy code, or making a sweeping change that hides the real issue. You want a one-line fix and green tests.

> **🌱 Checkpoint:** If you reproduced the bug with a failing test and fixed it with a minimal change, you've got the core loop: **Understand → Reproduce → Fix → Verify.** That's the foundation. Everything below is stretch.

---

## Exercise 4: Debugging From a Stack Trace / Error

Real bugs usually arrive as an error message. Practise feeding raw signal to Copilot.

### Step 1: Generate a runtime error

```
Add a function to sandbox/debugging that loads order data from a JSON string,
but make it crash with a realistic runtime error on malformed input
(e.g. a missing field). Show me the error/stack trace.
```

### Step 2: Paste the trace and ask for hypotheses

```
Here is the error and stack trace:

[paste the full error]

Give me the three most likely root causes, ranked, with the reasoning for each.
Then tell me what single piece of information would confirm which one it is.
```

### Step 3: Confirm, then fix

Pick the most likely cause, confirm it (add a log, inspect the input), then have Copilot fix it with proper input validation and a regression test.

> **Skill:** Notice the pattern — *hypotheses first, confirmation second, fix third*. This stops you from "fixing" the wrong thing.

---

## Exercise 5: Taming Legacy / Unfamiliar Code

Now the real-world scenario: code with no tests, no docs, and no original author available.

### Step 1: Get a guided tour

Open a file from **one of your real projects** (or generate a deliberately messy, uncommented one). In **Ask** mode:

```
I'm new to this code. Give me:
1. A one-paragraph summary of what this file does
2. Its public surface (what calls in, what it calls out to)
3. The riskiest parts to change and why
4. Three questions I should ask the original author
```

### Step 2: Generate characterization tests

The safe way to change code you don't understand is to *pin its current behaviour* first.

```
Before I refactor this, write characterization tests that capture the CURRENT
behaviour exactly as-is — even if some of it looks wrong. I want a safety net
that tells me if I accidentally change behaviour. Run them and confirm they pass.
```

> **Key idea:** Characterization tests don't assert *correct* behaviour — they assert *current* behaviour. They let you refactor fearlessly and catch accidental changes.

### Step 3: Refactor behind the safety net

```
Now refactor this for readability — better names, smaller functions, early returns —
WITHOUT changing behaviour. The characterization tests must still pass.
Show me the diff and re-run the tests.
```

If a characterization test breaks, you changed behaviour. Decide deliberately: was that intended (a bug fix) or accidental (revert it)?

---

## 🚀 Advanced Stretch

1. **Bisect a regression.** Generate a short git history where one commit introduces a bug, then ask Copilot to help you reason about which change is the likely culprit and why — a manual `git bisect` with an assistant.
2. **Performance debugging.** Generate a function with an accidental O(n²) loop, then ask Copilot to identify the hotspot, explain the complexity, and propose an O(n) rewrite with a benchmark to prove it.
3. **Legacy modernization plan.** Point Copilot at a genuinely old file and ask for a *staged* modernization plan (not a rewrite): step 1 add tests, step 2 extract functions, step 3 introduce types, etc. Have it produce the plan as a checklist you could turn into issues.
4. **Cross-file root cause.** Create a bug whose cause is in a *different* file from where it manifests. Use `@workspace` / `#file` to make Copilot trace the data flow across files to the true source.
5. **Flaky test triage.** Generate a test that fails intermittently (timing/order dependent) and have Copilot diagnose *why* it's flaky and rewrite it to be deterministic — without `sleep()`.

> **Team-lead track:** Draft a "debugging with Copilot" one-pager for your team capturing the Understand → Reproduce → Fix → Verify loop and the characterization-test pattern. Add it to your Lab 1 instructions ideas.

---

## Anti-patterns to Avoid

| Anti-pattern | Why it's dangerous | Do instead |
|--------------|-------------------|------------|
| "Just fix it" with no understanding | You ship a fix you can't explain | Make it explain and quote lines first |
| Letting Copilot edit the test to pass | Hides the bug instead of fixing it | Verify the test encodes the *spec*, not current behaviour |
| Refactoring code with no tests | Silent behaviour changes | Add characterization tests first |
| Trusting the first hypothesis | Often fixes a symptom, not the cause | Ask for ranked hypotheses + a confirmation step |
| Accepting a huge "fix" diff | Real fix is usually tiny | Demand the smallest change that turns tests green |

---

## 💬 Discussion Points

1. **How much do you trust Copilot's explanation** of code you don't understand? How do you verify it?
2. **Where has Copilot saved you the most time** — writing new code, or understanding/fixing existing code?
3. **What's your team's policy** on refactoring AI-touched code that has no tests?
4. **Could characterization tests** change how your team approaches legacy systems?

---

## Key Takeaways

- The everyday win with Copilot is **reading and fixing code**, not just writing it
- Follow the loop: **Understand → Reproduce → Fix → Verify**
- Make Copilot **prove its claims** against actual lines and real inputs — it will confidently guess otherwise
- **Reproduce bugs with a failing test** before fixing; fix with the *smallest* change
- For legacy code, **characterization tests** are your safety net — pin current behaviour, then refactor fearlessly
- Debug from real signal: **hypotheses first, confirmation second, fix third**

---

**Previous:** [Lab 5: Quality Guardrails ←](05-quality-and-review.md) · **Next:** [Lab 7: Capstone Team Challenge →](07-capstone.md)

**Bonus / self-paced:** [Lab 8: MCP →](08-mcp-concepts.md) · [Lab 9: Custom Chat Modes & Subagents →](09-chat-modes-and-subagents.md) · [Lab 10: Beyond the Editor →](10-advanced-topics.md) · [Lab 11: Copilot CLI Deep Dive →](11-copilot-cli.md)
