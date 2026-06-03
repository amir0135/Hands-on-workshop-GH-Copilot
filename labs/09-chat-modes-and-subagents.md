# Lab 9: Custom Chat Modes & Subagents

**Duration:** ~30 minutes
**Goal:** Stop re-explaining yourself. Build **custom chat modes** that give Copilot a fixed persona, toolset, and rules for a recurring job — and learn to delegate self-contained work to **subagents** so your main conversation stays focused.

> **🌱 Foundation path:** Exercises 1–2 — create one custom chat mode and use it. Even one good mode (a strict reviewer, a docs writer) changes your daily workflow.
> **🚀 Advanced stretch:** Exercises 3–4 plus the stretch section — toolset scoping, multi-mode workflows, and delegating to subagents.

---

## Why This Matters

By now you've seen `copilot-instructions.md` (always-on) and `.prompt.md` files (on-demand recipes). **Custom chat modes** are the next layer: a named mode in the chat picker that bundles a persona + instructions + an allowed set of tools.

| Mechanism | Scope | Best for |
|-----------|-------|----------|
| `copilot-instructions.md` | Always on, whole repo | Team coding standards |
| `.instructions.md` (`applyTo`) | Always on, matching files | Module-specific rules |
| `.prompt.md` | On demand via `/` | One-shot reusable tasks |
| **Custom chat mode** | A mode you switch into | A recurring *role* with its own rules and tools |
| **Subagent** | Delegated, isolated context | Self-contained research/work you don't want cluttering the main chat |

Think of it this way: a prompt file is a *recipe*; a custom chat mode is a *specialist you hire for a shift*.

---

## Exercise 1: Build Your First Custom Chat Mode

Custom modes live in `.github/chatmodes/` as `*.chatmode.md` files with YAML frontmatter.

### Step 1: Create a "Strict Reviewer" mode

Create `playground/.github/chatmodes/reviewer.chatmode.md`:

```markdown
---
description: "A blunt, security-focused senior code reviewer"
tools: ['codebase', 'search', 'usages']
---

You are a senior code reviewer. You do NOT write or edit code — you only review.

For any code I show you or reference:
- Lead with the single most important issue, not a list of nitpicks
- Flag security problems first (injection, secrets, missing validation, authz)
- Call out missing error handling and shallow tests explicitly
- For every issue: state it, explain WHY it matters, then suggest a concrete fix
- If the code is genuinely fine, say so plainly — do not invent issues
- Be direct and concise. No praise padding.
```

> **Note on the `tools` field:** giving the reviewer only read-only tools (`codebase`, `search`, `usages`) and no edit tool reinforces the persona — it *can't* accidentally start editing. Tool names vary by VS Code version; if one isn't recognised, open the mode picker → *Configure Modes* to see the available tools, or simply omit the `tools` line to allow defaults.

### Step 2: Use the mode

1. Open the chat mode picker (where you pick Ask / Plan / Agent)
2. Select **reviewer** (your new mode should appear)
3. Open a file from an earlier lab and enter this prompt: `Review this.`

Notice it behaves differently from default agent mode: focused, opinionated, read-only.

> **🌱 Checkpoint:** One working custom mode = you've got it. This is reusable across every project — commit it and your whole team gets the same reviewer.

---

## Exercise 2: A Mode With a Different Job

Modes shine when each one does *one* job well.

Create `playground/.github/chatmodes/docs-writer.chatmode.md`:

```markdown
---
description: "Writes clear docs and docstrings, never changes logic"
tools: ['codebase', 'search']
---

You write documentation only. Never change code logic.

When asked to document code:
- Write a concise summary of WHAT it does and WHY it exists
- Document parameters, return values, and thrown errors/exceptions
- Note any non-obvious behaviour or gotchas
- Match the docstring/comment style already used in the file
- Do not add comments that merely restate the code
```

Switch into **docs-writer** and point it at an undocumented function. Compare the result to asking default agent mode "add docs" — the dedicated mode stays in its lane.

---

## Exercise 3: Compose Modes Into a Workflow

The real power is chaining specialists.

Try this sequence on a small feature in your `playground/`:

1. **Plan** mode → outline the change
2. **Agent** mode → implement it
3. **reviewer** mode → review the implementation
4. **docs-writer** mode → document the final result

Notice how switching modes is like handing the work to different teammates, each with their own rules. No single giant prompt trying to do everything.

---

## Exercise 4: Delegate to a Subagent

When a task is **self-contained** — research, a focused investigation, a contained build — you can delegate it to a **subagent**. The subagent runs with its own isolated context and reports back a single result, keeping your main conversation clean.

### When to use a subagent

- "Search the whole codebase and tell me everywhere we call the payments API" (research)
- "Investigate why the build config differs between these two folders and summarise" (exploration)
- A chunk of work whose intermediate steps you don't need to watch

### Try it (in agent mode)

```
Delegate this to a subagent: explore the playground folder, list every file
that defines a public function, and report back a single summary table of
file → functions. Don't make any edits.
```

Watch how the subagent does the legwork and returns a digest, instead of flooding your main chat with dozens of file reads.

> **Mental model:** A subagent is a teammate you hand a *bounded* task to. You don't micromanage it; you read its report. Use it when watching every step adds no value.

---

## 🚀 Advanced Stretch

1. **Build a mode for your real role.** Create a chat mode for a job you do weekly — an API-design reviewer, a SQL-migration author, a test-hardener. Scope its tools deliberately. Commit it and have a teammate try it.
2. **Tool-scoping experiment.** Make two versions of the same mode: one with edit tools, one without. Give both the same prompt and observe how the toolset changes behaviour and safety.
3. **Mode + instructions interplay.** Combine a custom mode with a scoped `.instructions.md` and see how they layer. Which wins when they conflict?
4. **Research-then-build hand-off.** Use a subagent to research an approach (read-only), then take its report into agent mode to implement. Practise the clean hand-off between exploration and execution.
5. **Parallel investigations.** Kick off two independent read-only subagent investigations and compare their reports. Learn what work parallelises well and what doesn't.

> **Team-lead track:** Decide which 2–3 custom modes your team should standardise on, where they live in the repo, and how they're reviewed. A shared `reviewer.chatmode.md` alone can raise the floor on every PR.

---

## 💬 Discussion Points

1. **Which recurring role** on your team would benefit most from a dedicated chat mode?
2. **Where's the line** between a prompt file and a custom chat mode? When do you reach for each?
3. **What work would you delegate to a subagent** — and what would you always want to watch yourself?
4. **How do you keep modes from sprawling** into dozens of half-maintained files?

---

## Key Takeaways

- **Custom chat modes** bundle a persona + rules + tools into a reusable, switchable specialist
- Scope each mode to **one job**; restrict its **tools** to reinforce the role and improve safety
- **Compose modes** into a workflow (Plan → Agent → reviewer → docs-writer) instead of one mega-prompt
- **Subagents** handle self-contained research/work in isolated context and report back a digest
- Modes and subagents are **checked into Git** — the whole team gets the same specialists
- Reach for a subagent when **watching every intermediate step adds no value**

---

**Next:** [Lab 6: MCP — What's Next →](06-mcp-concepts.md)
