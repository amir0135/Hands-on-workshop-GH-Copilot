# Lab 1: Team Configuration & Custom Instructions

> **Track:** Core workshop · 2 of 8

**Duration:** ~45 minutes
**Goal:** Set up Copilot so it produces consistent, high-quality output that matches your team's standards — without every developer having to repeat the same instructions.

> **🧭 Jumping in cold?** This lab is fully standalone. Minimum setup: Copilot active in VS Code (see [Lab 0](00-getting-aligned.md#part-1-verify-your-setup-10-min)) and this repo cloned. You'll create the `sandbox/` folder inside this lab — no prior lab artefacts required.

**Quick start:**

```bash
mkdir -p sandbox/.github
code sandbox     # open sandbox as the workspace root
```

> **🌱 Foundation path:** Exercises 1–2 — create a `copilot-instructions.md` and watch Copilot's behaviour change. That alone is a career-long skill.
> **🚀 Advanced stretch:** Jump to the stretch section at the end for layered instructions, `applyTo` scoping, and measuring instruction effectiveness.

---

## Why This Matters

Without shared configuration, every developer gets different results from Copilot. One person gets clean code with proper error handling. Another gets a different naming convention. A third gets no tests. **Custom instructions solve this** by giving Copilot a shared understanding of how your team works.

---

## Exercise 1: Create Repository-Level Instructions

The `.github/copilot-instructions.md` file tells Copilot how to behave for **everyone working in this repository**. This is checked into source control and shared with the team.

### Step 1: Create the file

Create a folder called `sandbox` inside this repository. This is where you will do all your lab exercises.

```bash
mkdir -p sandbox/.github
```

> **⚠️ Open `sandbox` as your workspace root.** Copilot only auto-discovers `.github/copilot-instructions.md` relative to the folder open as your workspace root. So open the **`sandbox` folder itself** in VS Code (**File → Open Folder…**, or **Add Folder to Workspace…**). Throughout this lab, "workspace root" = the `sandbox` folder, so `sandbox/.github/copilot-instructions.md` is discovered as `.github/copilot-instructions.md`.

### Step 2: Write your first instructions file

Create `sandbox/.github/copilot-instructions.md` with the following content. **Read each section carefully** — these are the types of instructions that matter most for team consistency:

```markdown
# Copilot Instructions

## Code Style
- Use meaningful, descriptive variable and function names. No abbreviations.
- Keep functions small — each function should do one thing.
- Prefer early returns over deeply nested conditionals.

## Error Handling
- Always handle errors explicitly. Never silently swallow exceptions.
- Use typed/specific exceptions, not generic catch-all handlers.
- Include meaningful error messages that help with debugging.

## Testing
- When generating new functions, suggest corresponding unit tests.
- Use descriptive test names that explain the scenario and expected outcome.
- Prefer arrange-act-assert structure in tests.

## Documentation
- Add a brief doc comment to public functions explaining what they do and why.
- Do not add obvious comments like "// increment counter" on `counter++`.

## Security
- Never hardcode secrets, API keys, or passwords.
- Validate all external input at system boundaries.
- Use parameterized queries for database operations.
```

### Step 3: Verify it works

1. Open Copilot Chat in **Agent** mode
2. Enter this prompt: `Create a function that fetches user data from a REST API and handles the response`
3. Observe that the generated code follows your instructions — meaningful names, explicit error handling, no hardcoded values
4. Now ask the same question **without** the instructions file (temporarily rename it). Compare the results.

> **Key Takeaway:** The instructions file is your team's "coding standards for Copilot." It compounds — once set up, every developer benefits automatically.

---

## Exercise 2: Understand Instruction Scope & Hierarchy

Copilot instructions have a hierarchy. Understanding it helps you apply the right level of guidance.

| Scope | File | Who benefits | Use for |
|-------|------|-------------|---------|
| **Repository** | `.github/copilot-instructions.md` | Everyone on the project | Coding standards, architecture patterns, tech stack rules |
| **Scoped (path-based)** | `.github/instructions/<name>.instructions.md` with an `applyTo` glob | Anyone editing matching files | Module-specific patterns (e.g. "files under `api/` use the repository pattern") |
| **Personal** | VS Code user settings | Just you | Personal preferences (verbosity, language, editor habits) |

> **How scoped instructions are discovered:** VS Code looks for `*.instructions.md` files in the **`.github/instructions/`** folder at your workspace root. Each file's `applyTo` frontmatter is a glob that decides **which files it activates for** — based on the path of the file you're editing, *not* which folder the instructions file sits in. A bare `.instructions.md` dropped into a random subfolder is **not** discovered.

### Try it:

1. Create the scoped-instructions folder: `mkdir -p sandbox/.github/instructions`
2. Create `sandbox/.github/instructions/api.instructions.md` with:

```markdown
---
applyTo: "api/**"
---

# API Layer Instructions
- All API endpoints must return consistent response envelopes: `{ data, error, status }`
- Use middleware for authentication — do not check auth in individual handlers
- All endpoints must validate input before processing
```

3. Create a file under the path the glob targets, e.g. `sandbox/api/users.py` (so the workspace-relative path is `api/users.py`)
4. With that file open, in Agent mode enter: `Create a POST endpoint for creating a new user`
5. Notice how Copilot combines both the repository-level instructions **and** the scoped `api/**` instructions — automatically, because the file you're editing matches `applyTo`

---

## Exercise 3: Configure VS Code Settings for Your Team

Some Copilot behaviors are controlled by VS Code settings. Teams should align on these.

### Recommended team settings

Create `sandbox/.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/copilot-instructions.md" }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "text": "Check for security vulnerabilities, performance issues, and deviations from our coding standards." }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    { "text": "Generate tests using arrange-act-assert pattern. Include edge cases and error scenarios. Use descriptive test names." }
  ]
}
```

### Try it:

1. Select a block of code in any file
2. Right-click → "Copilot: Review and Comment"
3. Notice it follows your review instructions
4. Right-click → "Copilot: Generate Tests"
5. Notice it follows your test generation instructions

---

## Exercise 4: Instructions for Real Projects

Now apply what you learned to a **real** scenario. Think about your actual project at work.

### Write instructions for your team:

1. Open `sandbox/.github/copilot-instructions.md`
2. Add sections relevant to **your** team's stack and standards:

**Examples to consider:**

```markdown
## Architecture
- We use [clean architecture / hexagonal / MVC / etc.]
- Business logic goes in the service layer, never in controllers
- Database access goes through repository classes only

## Our Tech Stack
- Backend: [.NET 8 / Python 3.12 / Node.js 20 / etc.]
- Database: [PostgreSQL / SQL Server / etc.]
- Testing: [xUnit / pytest / Jest / etc.]
- CI/CD: [GitHub Actions / Azure DevOps / etc.]

## Naming Conventions
- [PascalCase for classes, camelCase for methods / snake_case for everything / etc.]
- API endpoints: [/api/v1/resource-name / etc.]
- Database tables: [PascalCase / snake_case / etc.]

## What We Do NOT Want
- No auto-generated comments that just repeat the code
- No TODO comments without a linked issue
- No console.log / print statements in production code
```

3. Test your instructions by asking Copilot to generate code that would typically violate your standards
4. Iterate: If Copilot doesn't follow an instruction, make it more specific

---

## 🚀 Advanced Stretch

Finished the core exercises? Push further:

1. **Layer instructions with `applyTo`.** Create a scoped `sandbox/.github/instructions/tests.instructions.md` with `applyTo: "**/*.test.*,**/*_test.*"` that adds testing-only rules (e.g. "every test must assert behaviour, not just absence of errors"). Then open a file whose name matches (e.g. `sandbox/calculator.test.py`) and confirm the rules only activate for test files, not for ordinary source files.
2. **Write a "house style" that's genuinely opinionated.** Encode a real, slightly controversial convention from your team (e.g. "no inheritance more than one level deep", "functions over 30 lines must be justified in a comment"). Generate code and see if Copilot honours it.
3. **Measure effectiveness.** Generate the same feature *with* and *without* your instructions file (rename it temporarily). Diff the two outputs. Quantify what the instructions actually changed — this is the evidence you'll use to sell adoption to your team.
4. **Instruction conflicts.** Deliberately add two contradicting rules and observe how Copilot resolves them. Learn where to be precise and where over-specifying backfires.
5. **Onboarding angle.** Draft the 5 instructions that would most help a brand-new hire produce code that passes your review on day one. This is the highest-leverage list most teams never write down.

> **Team-lead track:** Sketch the rollout plan — who owns the file, how changes are reviewed, and how you'll keep it from rotting. Capture it; you'll want it for [Lab 7 (Capstone)](07-capstone.md) and for your real team rollout.

---

## Discussion Points

After completing the exercises, discuss with your table:

1. **What instructions would have the biggest impact** on your team's code quality?
2. **What patterns keep repeating** in code reviews that Copilot could enforce?
3. **How would you roll this out** — PR to your repo? Team discussion first?
4. **What should NOT go in instructions?** (things that change too often, subjective preferences, etc.)

---

## Key Takeaways

- `.github/copilot-instructions.md` is your team's **single most impactful Copilot configuration**
- Instructions compound: set them up once, every developer benefits on every task
- Be specific and opinionated — vague instructions produce vague results
- Layer instructions: repo-wide standards + folder-specific patterns
- Test your instructions — ask Copilot to do things and verify it follows them
- Review and iterate — treat instructions like code, evolve them with the team

---

**Previous:** [Lab 0: Getting Aligned ←](00-getting-aligned.md) · **Next:** [Lab 2: Agent Mode Mastery →](02-agent-mode-mastery.md)
