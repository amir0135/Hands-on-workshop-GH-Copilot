# Lab 11: Copilot in the Terminal — The CLI Deep Dive

> **Track:** Bonus / self-paced (advanced)

**Duration:** ~40 minutes (bonus / self-paced, advanced)
**Goal:** Go beyond "ask the terminal a question." Drive real, multi-step work from the command line with the **GitHub Copilot CLI** — agentic edits, scripting, piping, MCP servers, custom instructions, and CI/automation — and know exactly when the terminal beats the editor.

> **🧭 Jumping in cold?** This lab is fully standalone. Minimum setup: a terminal, Node.js, and a GitHub account with Copilot access. No prior lab artefacts required, though [Lab 10 §1](10-advanced-topics.md#section-1-github-copilot-cli) is a gentler intro if you've never used a Copilot CLI before.

**Quick start:**

```bash
node --version                                    # need Node.js installed
npm install -g @github/copilot                    # the standalone agentic CLI
copilot --version                                 # then run `copilot` to start a session
```

> **This lab assumes you're comfortable already.** It's written for experienced users who live in the shell, script their workflows, and want Copilot where their hands already are. If you've never touched the CLI, skim [Lab 10 §1](10-advanced-topics.md#section-1-github-copilot-cli) first.
>
> **🌱 Foundation path:** Exercises 1–2 — install, and run your first agentic session.
> **🚀 Advanced stretch:** Exercises 3–9 — scripting, piping, MCP, custom instructions, CI, skill determinism, custom subagents, and context compaction.

---

## Why This Matters

The editor is great when you're *reading and writing code*. But a huge slice of an experienced engineer's day is **shell intent**: rebasing, bisecting, wrangling logs, scripting one-off migrations, wiring CI. Context-switching to a chat panel for those breaks flow.

The Copilot CLI brings the **agentic loop** — plan, run tools, edit files, check results — into the terminal itself. Same model, same reasoning, no mouse.

| Surface | Best for |
|---------|----------|
| **VS Code agent mode** | Multi-file feature work where you're reading diffs as they land |
| **Copilot CLI (agentic)** | Shell-centric tasks, scripted/automated runs, headless/CI, remote boxes over SSH |
| **`gh copilot suggest/explain`** | One-shot "what's the command / what does this do" lookups |

---

## Two Tools, Don't Confuse Them

There are **two** distinct things called "Copilot CLI":

1. **`gh copilot`** — an extension to the GitHub CLI (`gh`). Lightweight. `suggest` and `explain` only. Great for quick lookups.
2. **`copilot`** — the standalone **GitHub Copilot CLI**, an agentic coding tool that can read/edit files, run commands, and use MCP servers. This is the powerful one.

This lab focuses on the standalone `copilot` agent, with `gh copilot` as the quick-lookup sidekick.

---

## Exercise 1: Install & Authenticate

### The standalone agent

```bash
# npm (cross-platform)
npm install -g @github/copilot

# verify
copilot --version
```

Launch the interactive session from any repo:

```bash
cd your-project
copilot
```

On first run it walks you through authentication (browser device flow against your Copilot license). Inside the session, useful slash commands:

```text
/help        list commands
/login       authenticate
/model       switch the underlying model
/clear       reset the conversation context
/exit        quit
```

### The quick-lookup sidekick

```bash
gh extension install github/gh-copilot   # requires gh, signed in
gh copilot suggest "find files >100MB modified this week"
gh copilot explain "find . -type f -size +100M -mtime -7"
```

> **Check it works:** run `copilot` in a throwaway repo, type `What does this project do?`, and confirm it reads files before answering.

---

## Exercise 2: Your First Agentic Session

This is the part that's genuinely different from `suggest`. The agent can **plan, edit files, and run commands** — with your approval.

In a sandbox repo, start `copilot` and try a real task:

```text
Add a .editorconfig with 2-space indent for JS/TS and 4-space for Python,
and a Makefile target `fmt` that runs the right formatter per language.
Show me the plan before changing anything.
```

Watch the loop: it proposes a plan → asks before writing files → runs a check. You stay in control.

### Approval modes — know them before you script

The agent asks permission before mutating actions by default. You can widen that:

| Mode | Behaviour | Use when |
|------|-----------|----------|
| **Interactive (default)** | Prompts before edits / command execution | Day-to-day work |
| **Allow-listed tools** | Pre-approve specific tools/commands | Repeated trusted ops |
| **Full auto** (e.g. `--allow-all-tools`) | No prompts | **Sandboxed / CI only** |

> ⚠️ **Never run full-auto on your main machine against a repo you care about, or anything touching production.** Full-auto belongs in a container, a throwaway clone, or CI with a scoped token. Treat it like `curl | sudo bash`.

---

## Exercise 3: Programmatic & Scripted Runs 🚀

The agent has a non-interactive mode — pass a prompt and let it run to completion. This is where it becomes a building block.

```bash
# one-shot, print the result and exit
copilot -p "Summarise the open TODOs in this repo grouped by file" 

# feed it from a pipe
git log --oneline -20 | copilot -p "Draft a CHANGELOG entry from these commits"
```

Compose it into real shell workflows:

```bash
# Generate a commit message from staged changes
git diff --cached | copilot -p "Write a conventional-commits message for this diff" 

# Triage a failing test, capture the explanation to a file
pytest -x 2>&1 | copilot -p "Explain the first failure and propose a fix" > triage.md
```

> **Mindset shift:** once Copilot is `stdin → stdout`, it's just another Unix filter. Pipe into it, pipe out of it, redirect it, background it.

### Try it

1. Pipe `git diff --cached` into `copilot -p` to draft a commit message.
2. Pipe your build/test output into it and ask for the root cause.
3. Save the output to a file and review before acting — **never auto-apply blind.**

---

## Exercise 4: Custom Instructions in the CLI 🚀

The agent honours the **same `.github/copilot-instructions.md`** you built in [Lab 1](01-team-configuration.md). Your team's coding standards travel with you into the terminal — no extra setup.

1. In a repo that has `copilot-instructions.md`, start `copilot`.
2. Ask it to scaffold a small module.
3. Confirm it follows your house style (naming, error handling, test conventions) without being told.

This is the payoff of centralising standards: editor, CLI, and CI all read the same source of truth. Your `.instructions.md` (`applyTo`) and `AGENTS.md` conventions apply here too.

> **💬 Discussion:** if your instructions only ever get tested in the editor, do they actually hold up headless? Run them through the CLI to find the gaps.

---

## Exercise 5: MCP Servers in the CLI 🚀

The CLI agent is an **MCP client** too (see [Lab 8](08-mcp-concepts.md) for concepts). You can give the terminal agent the same external tools — GitHub, a database, your own server.

- Configure MCP servers via the CLI's config (use `/mcp` inside the session, or the MCP config file the CLI reads).
- The same trust rules apply: **only connect servers you trust**, prefer read-only/scoped tokens, and remember MCP uses your existing auth — it's not a backdoor.

### Try it

```text
/mcp
```

Inspect which servers are wired up, then ask a question that forces a tool call (e.g. "list my open PRs in this repo" against the GitHub MCP server) and watch the agent invoke the tool.

> The CLI's strength: an MCP-powered agent on a **remote/headless box** where there's no editor at all — a build server, a jump host, a container.

---

## Exercise 6: Headless & CI Automation 🚀

The non-interactive mode + full-auto + a scoped token = Copilot as a **CI step**. Powerful, and easy to get wrong.

A sketch of a guarded CI usage:

```yaml
# pseudo-workflow — adapt to your CI
- name: Copilot triage on failure
  if: failure()
  env:
    COPILOT_TOKEN: ${{ secrets.COPILOT_CLI_TOKEN }}
  run: |
    pytest -x 2>&1 | tee out.log || true
    copilot -p "Read out.log, identify the root cause, and post a concise summary" \
      --allow-all-tools > triage.md
    cat triage.md
```

### Guardrails for automated runs — non-negotiable

- **Scope the token.** Least privilege; never a personal admin token.
- **Sandbox it.** Container or ephemeral runner, not a shared host.
- **No silent writes to protected branches.** Have it open a PR / draft a comment a human approves — don't let it push.
- **Log everything.** Capture the full transcript as a build artifact.
- **Cap the blast radius.** Read-only where you can; explicit allow-lists where you can't.

> ⚠️ **Prompt-injection is real in automation.** If the agent ingests issue text, logs, or web content, that content can try to hijack it. Keep write scope minimal and keep a human in the approval path for anything that ships.

---

## Exercise 7: Making Skill Invocation Deterministic 🚀

Skills (`SKILL.md` files) are loaded by **description matching**, not hard rules. In the editor that's usually fine — but in the CLI, headless and scripted runs expose the flakiness: the *same* prompt can invoke a skill on one run and silently skip it on the next. When that skill carries your house rules, a skipped invocation means wrong output with no error.

### See the non-determinism

In a repo that has at least one skill wired up, run the *same* triggering prompt several times in fresh sessions. The CLI prints each tool call it makes to stdout, so a skill invocation shows up as a `skill` tool call line in the transcript — watch for it:

```bash
for i in 1 2 3; do
  echo "--- run $i ---"
  copilot -p "Create a new expense report for last week's travel" --allow-all-tools 2>&1 \
    | grep -iE "skill|expense-report" || echo "(skill NOT invoked)"
done
```

For the authoritative record, the CLI also logs skill loading to `~/.copilot/logs/`. Inspect the newest log after a run:

```bash
grep -i "skill" "$(ls -t ~/.copilot/logs/process-*.log | head -1)" | head
```

> **Note:** `--log-level debug` writes to the log files in `~/.copilot/logs/`, **not** to stdout — so don't expect debug output in your pipe. Use the stdout tool-call lines for a quick check, and the log files for the full picture.

You'll often see the skill load on some runs and not others. That variance is the problem.

### Pin it down

Don't rely on the model *choosing* to load the skill. Make it deterministic:

| Technique | What it does |
|-----------|--------------|
| **Name the skill explicitly in the prompt** | `"Using the expense-report skill, …"` removes the matching gamble |
| **Tighten the skill `description`** | Front-load exact trigger phrases users actually type; drop vague language |
| **Promote critical rules to instructions** | Anything that *must* always apply belongs in `copilot-instructions.md` / `AGENTS.md`, which load every turn — skills are opt-in, instructions are not |
| **Gate in scripts** | After a scripted run, assert the skill actually fired (grep the transcript) and fail loudly if it didn't |

### Try it

1. Run the loop above and count how many of 3 runs actually loaded the skill.
2. Rewrite the skill's `description` to lead with the exact phrase you used, and re-run. Did consistency improve?
3. Move the one rule you *cannot* afford to skip out of the skill and into `AGENTS.md`. Confirm it now applies every time, skill or no skill.

> **Rule of thumb:** skills are for *discoverable, optional* expertise. If something must happen on every relevant turn, an instruction file is the deterministic home — a skill is not.

---

## Exercise 8: Build Your Own Agents & Delegate Properly 🚀

The CLI agent can spawn **subagents** — scoped, stateless workers that go off, do a bounded job, and report back a single result. Done well, this keeps your main context clean and parallelises work. Done badly, it's a black box that burns tokens and returns mush.

### Define a custom agent

Custom agents are **agent profile** files — Markdown with YAML frontmatter — that the CLI discovers automatically from:

- `.github/agents/<name>.agent.md` — repository-level (travels with the repo)
- `~/.copilot/agents/<name>.agent.md` — user-level (all your projects)

The frontmatter sets `name`, `description`, and an optional `tools` list (omit `tools` to grant all). Tool aliases include `read`, `edit`, `write`, `search`, `shell`, and `fetch`. Start one minimal:

```markdown
---
name: test-fixer
description: Runs the test suite, diagnoses the first failure, and proposes a minimal fix. Read-mostly; never pushes.
tools: ["read", "edit", "shell"]
---
You fix exactly one failing test at a time. Always show the failing output
first, then the smallest diff that makes it pass. Never touch unrelated files.
Never run destructive git commands.
```

Invoke it three ways: `/agent` inside an interactive session, by naming it in a prompt ("Use the test-fixer agent to…"), or via the command line:

```bash
copilot --agent test-fixer -p "Find and fix the first failing test."
```

### Delegate well — the rules that matter

A subagent is **stateless** and **can't ask follow-ups**: it gets one prompt and returns one message. So delegation quality lives entirely in how you brief it.

| Do | Why |
|----|-----|
| **Give one bounded objective** | "Find and fix the failing auth test" — not "improve the codebase" |
| **State what to return** | Tell it the exact shape of the answer (a diff, a file list, a yes/no + reason) |
| **Say read-only vs. write** | The parent knows intent; the subagent doesn't — spell it out |
| **Scope its tools** | Fewer tools = less to go wrong; a research agent needs no write access |
| **Parallelise only independent work** | Two subagents touching the same files will collide |

### When to delegate vs. do it inline

- **Delegate** when the task is *searchy* or *exploratory* ("where is X handled across the repo?") — you get the answer without dragging dozens of file reads into your main context.
- **Delegate** independent chunks you can run in parallel.
- **Do it inline** when you need to watch every diff land, or when the work is tightly coupled and benefits from shared context.

### Try it

1. Create the `test-fixer` agent above in `.github/agents/` and invoke it with `copilot --agent test-fixer -p "…"` on a deliberately broken test.
2. Write a **research-only** agent (`tools: ["read", "shell"]`, no `edit`) that maps how a feature flows through the code and returns *only* a file list + one-line summary each.
3. Note the built-in agents the CLI ships with — run `/agent` in an interactive session to see **Explore**, **Task**, **Research**, **Code review**, and more. Compare your `test-fixer` against the built-in **Task** agent.

> **The delegation test:** if you can't write the subagent's task in one self-contained paragraph with a defined output, it's not ready to delegate — clarify it first, or keep it inline.

---

## Exercise 9: Compacting Context the Right Way 🚀

Long sessions fill the context window. The two reflexes most people reach for are both weak:

- **"Caveman" `/clear`** — nukes *everything*, including the useful state you'd built up. Cheap but you lose the thread.
- **Auto-compact / the compact command** — summarises, but bluntly: it often drops the exact constraints, file paths, and decisions you most need to keep, and you don't control what survives.

Neither is good enough for serious multi-hour work. Here's better.

### Strategy 1: Externalise state to a file (durable memory)

Don't keep the plan in the context window — keep it on disk and let the agent re-read it.

```text
Write the current plan, decisions made, and open questions to NOTES.md.
From now on, treat NOTES.md as the source of truth and update it as we go.
```

Now `/clear` is safe: the state lives in `NOTES.md`, and you reseed a fresh session with `Read NOTES.md and continue`. You decide what persists, not the summariser.

### Strategy 2: Delegate the context-heavy part

The big context consumer is usually *exploration* — dozens of file reads. Push that into a subagent (Exercise 8): it reads 40 files in its *own* context and returns a 10-line summary into yours. Your main window stays lean.

### Strategy 3: Scope the session to the task

Start a **fresh session per logical unit of work** rather than one marathon session. Smaller, focused sessions never approach the limit, so you rarely need to compact at all. Pair this with Strategy 1 to carry the thread across sessions.

### Strategy 4: Curated compaction, not blunt compaction

If you *do* compact, drive it yourself so the right things survive:

```text
Before we compact: summarise into a checkpoint that MUST retain —
exact file paths touched, decisions and their rationale, and remaining TODOs.
Drop tool output and exploration. Output as a block I can paste to reseed.
```

That's the difference between *you* choosing what's load-bearing and the tool guessing.

### Try it

1. Mid-task, have the agent write `NOTES.md`, then `/clear` and reseed with `Read NOTES.md and continue`. Did you lose anything important?
2. Move your next big exploration into a subagent and watch your main context stay small.
3. Compare blunt `/compact` vs. the curated checkpoint prompt above — which retained the file paths and decisions you actually needed?

> **Mental model:** the context window is RAM, not disk. Anything you can't afford to lose belongs on disk (`NOTES.md`, instructions, the repo itself) — then compaction is cheap because nothing important lived only in RAM.

---

## When the CLI Beats the Editor — Cheat Sheet

| Situation | Reach for |
|-----------|-----------|
| "What's the flag for…" / "explain this command" | `gh copilot suggest` / `explain` |
| Shell-heavy task, you're already in the terminal | `copilot` interactive |
| Scripted/repeatable generation (commit msgs, changelogs) | `copilot -p` in a pipe |
| Remote box / SSH session, no editor | `copilot` on the host |
| CI triage, auto-summaries | `copilot -p --allow-all-tools` (sandboxed) |
| Multi-file feature with live diff review | **VS Code agent mode** (not the CLI) |

---

## 🚀 Advanced Stretch: Build a Reusable Copilot Shell Function

Wrap a common workflow in a shell function so the whole team gets it for free:

```bash
# ~/.zshrc or ~/.bashrc
# AI-assisted commit: stage, draft message, let you edit before committing
aicommit() {
  git add -A
  local msg
  msg=$(git diff --cached | copilot -p "Write a conventional-commits message for this diff. Output only the message.")
  git commit -e -m "$msg"   # -e opens your editor to review/tweak before saving
}
```

Then `aicommit` becomes muscle memory. Share useful ones with the team as snippets.

> **Keep the human gate.** Note the `-e` — it opens the message in your editor so you review before the commit lands. Automation that removes *all* review is how bad commits ship.

---

## Discussion Points

- **💬** Where in *your* daily workflow does context-switching to the editor actually cost you? Those are CLI candidates.
- **💬** What's your team's policy for full-auto / headless runs? Who owns the token and where does it run?
- **💬** Should AI-drafted commit messages and PR descriptions be labelled as such? What does your team prefer?

---

## Resources

- [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- [`gh copilot` extension](https://github.com/github/gh-copilot)
- [Lab 8: MCP Concepts](08-mcp-concepts.md) — MCP fundamentals the CLI reuses
- [Lab 1: Team Configuration](01-team-configuration.md) — the instructions the CLI honours

---

**See also (bonus / self-paced):** [Lab 8: MCP →](08-mcp-concepts.md) · [Lab 9: Custom Chat Modes & Subagents →](09-chat-modes-and-subagents.md) · [Lab 10: Beyond the Editor →](10-advanced-topics.md)

**Back to:** [Workshop README →](../README.md)
