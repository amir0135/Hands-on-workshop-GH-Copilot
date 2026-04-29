# Lab 3: Prompt Files & Reusable Instructions

**Duration:** ~45 minutes
**Goal:** Create reusable prompt files (`.prompt.md`) and scoped instruction files (`.instructions.md`) that your team can share, version, and refine together — turning tribal knowledge into something Copilot consistently applies.

---

## Why Prompt Files Matter

In Lab 1, you set up `copilot-instructions.md` — always-on, repo-wide guidance. That is the foundation.

**Prompt files** are different. They are **on-demand, task-specific workflows** you invoke when you need them. Think of them as:

- Saved prompts that never get lost
- Team-wide playbooks for common tasks
- Reusable recipes checked into source control

| Feature | `copilot-instructions.md` | `.prompt.md` files | `.instructions.md` files |
|---------|--------------------------|-------------------|-------------------------|
| When active | Always | When you invoke them | Always (scoped by `applyTo`) |
| Scope | Entire repo | On demand | Matching files/folders |
| Use for | Coding standards, style | Workflows, recipes | Module-specific patterns |
| Shared via | Git | Git | Git |

---

## Exercise 1: Your First Prompt File

### Step 1: Create a prompt file

Create `playground/.github/prompts/code-review.prompt.md`:

```markdown
---
mode: "agent"
description: "Review code for quality, security, and team standards"
---

Review the selected code or the current file for:

1. **Security issues** — injection, hardcoded secrets, missing input validation
2. **Error handling** — are errors handled explicitly? Are they informative?
3. **Naming** — are names descriptive and consistent with our conventions?
4. **Complexity** — can any function be simplified or split?
5. **Testing gaps** — is this code testable? Are there obvious missing test cases?

For each finding:
- State the issue clearly
- Explain **why** it matters
- Suggest a concrete fix

If the code looks good, say so — don't invent issues.
```

### Step 2: Use the prompt file

1. Open any code file in your `playground/` folder (use one from Lab 2, or create something new)
2. Open Copilot Chat in **Agent** mode
3. Type `/` — you should see your prompt file listed
4. Select `code-review` and run it

### Step 3: Compare with an ad-hoc prompt

Now try the same review without the prompt file — just type "review this code" in chat.

Notice the difference? The prompt file produces **consistent, structured, actionable** feedback every time. That consistency is what makes it valuable for teams.

---

## Exercise 2: Build a Prompt Library

Create prompt files for common team workflows. Start with these three — then add your own.

### Prompt: Refactor

Create `playground/.github/prompts/refactor.prompt.md`:

```markdown
---
mode: "agent"
description: "Refactor code to improve readability and maintainability"
---

Refactor the current code following these principles:

1. **Extract** functions that do more than one thing
2. **Rename** anything that is not immediately clear
3. **Simplify** conditional logic — prefer early returns over nesting
4. **Remove** dead code and unnecessary comments
5. **Preserve** all existing behavior — this is refactoring, not feature work

After refactoring:
- List every change you made and why
- Confirm that the public interface (function signatures, API contracts) has not changed
- Suggest tests that would verify the refactoring didn't break anything
```

### Prompt: Explain for onboarding

Create `playground/.github/prompts/explain-code.prompt.md`:

```markdown
---
mode: "ask"
description: "Explain code for new team members"
---

Explain the selected code as if you are onboarding a new developer to this project. Cover:

1. **What** this code does — the purpose, not line-by-line narration
2. **Why** it exists — what problem does it solve?
3. **How** it connects to the rest of the system — what calls it? What does it call?
4. **Key decisions** — any non-obvious choices and why they were made
5. **Gotchas** — things that could trip someone up or that look wrong but are intentional

Use simple language. Avoid jargon unless it is defined.
```

### Prompt: Write tests

Create `playground/.github/prompts/write-tests.prompt.md`:

```markdown
---
mode: "agent"
description: "Generate comprehensive tests for the current code"
---

Write tests for the current code:

1. **Happy path** — the normal, expected usage
2. **Edge cases** — boundary values, empty inputs, maximum values
3. **Error cases** — invalid input, missing data, permission failures
4. **Integration points** — if this code calls external services, test the interaction

Follow these rules:
- Use arrange-act-assert structure
- One assertion per test (when practical)
- Test names must describe the scenario: `test_[action]_[condition]_[expectedResult]`
- Do not mock what you do not own unless necessary
- Create the test file in the appropriate location following project conventions
```

### Try them:

Create a code file with some intentional issues and test each prompt file against it. For example:

```python
# Create playground/user_service.py with deliberately imperfect code
def process(d):
    if d:
        if d.get("email"):
            if "@" in d["email"]:
                import sqlite3
                conn = sqlite3.connect("users.db")
                conn.execute("INSERT INTO users VALUES ('" + d["email"] + "', '" + d.get("name", "") + "')")
                conn.commit()
                return {"ok": True}
            else:
                return {"ok": False}
        else:
            return {"ok": False}
    else:
        return {"ok": False}
```

Run each prompt file against this code and observe the different outputs:
1. `/code-review` should catch the SQL injection, bad naming, deep nesting
2. `/refactor` should restructure it with early returns, proper names, parameterized queries
3. `/write-tests` should generate tests covering valid/invalid email, empty input, etc.

---

## Exercise 3: Scoped Instructions with `.instructions.md`

While prompt files are on-demand, `.instructions.md` files are **always-on for matching files**. Use them to embed domain knowledge into specific parts of your codebase.

### Step 1: Create scoped instructions

Create `playground/.instructions.md`:

```markdown
---
applyTo: "**/*.test.*,**/*.spec.*,**/test_*"
---

# Test File Instructions

When working with test files:
- Always use arrange-act-assert pattern
- Test names follow: test_[action]_[condition]_[expectedResult]
- Each test must be independent — no shared mutable state between tests
- Mock external dependencies, never hit real APIs/databases in unit tests
- Include at least one test for the happy path, one edge case, and one error case
```

### Step 2: Create API-specific instructions

Create `playground/api/.instructions.md` (create the folder if needed):

```markdown
---
applyTo: "**"
---

# API Layer Instructions

When working in the API layer:
- All endpoints return consistent response format: { "data": ..., "error": ..., "status": "ok"|"error" }
- Use HTTP status codes correctly (201 for creation, 204 for deletion, 400 for bad input, 404 for not found)
- Validate all input before processing — never trust client data
- Log every request with method, path, status code, and duration
- Never expose internal error details to clients
```

### Step 3: Test the scoping

1. In Agent mode, ask Copilot to create a test file in `playground/`
2. Verify it follows the test instructions automatically (arrange-act-assert, naming convention)
3. Ask Copilot to create an API endpoint in `playground/api/`
4. Verify it follows the API instructions (response format, status codes, validation)

The key point: **you did not have to mention these rules in your prompt**. They applied automatically based on where the file is.

---

## Exercise 4: Advanced Prompt Patterns

### Pattern: Prompt with context references

Prompt files can reference other files for context:

Create `playground/.github/prompts/new-endpoint.prompt.md`:

```markdown
---
mode: "agent"
description: "Create a new API endpoint following project patterns"
---

Create a new API endpoint based on the following specification.

Before writing code:
1. Look at existing endpoints in the project to match the patterns
2. Follow the same file structure, naming, and response format
3. Include input validation, error handling, and logging

After writing the endpoint:
1. Create corresponding tests
2. Update any route registration or configuration files
3. List what was created and any manual steps remaining

The user will describe what the endpoint should do.
```

### Pattern: Prompt with variables

The description and prompt body work together to make the file self-documenting:

Create `playground/.github/prompts/fix-bug.prompt.md`:

```markdown
---
mode: "agent"
description: "Diagnose and fix a bug systematically"
---

Follow this systematic approach to fix the bug:

1. **Reproduce** — Find the code path that triggers the bug. Trace from the entry point.
2. **Root cause** — Identify the actual cause, not just the symptom. Explain why the current code is wrong.
3. **Fix** — Apply the minimal change that fixes the bug without introducing side effects.
4. **Test** — Write a test that would have caught this bug. The test should fail before the fix and pass after.
5. **Verify** — Check if the same bug pattern exists elsewhere in the codebase.

The user will describe the bug symptoms.
```

### Try it:

Use the `fix-bug` prompt on intentionally broken code:

```python
# playground/broken_calculator.py
def divide(a, b):
    return a / b  # No zero check

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # Crashes on empty list
```

Run: `/fix-bug The average function crashes when given an empty list`

---

## Exercise 5: Organize for Your Team

Now think about your real project. What prompt files would save your team the most time?

### Common categories:

| Category | Example prompt files |
|----------|---------------------|
| **Quality** | `code-review.prompt.md`, `security-check.prompt.md` |
| **Development** | `new-endpoint.prompt.md`, `add-feature.prompt.md`, `refactor.prompt.md` |
| **Testing** | `write-tests.prompt.md`, `add-edge-cases.prompt.md` |
| **Onboarding** | `explain-code.prompt.md`, `architecture-overview.prompt.md` |
| **Debugging** | `fix-bug.prompt.md`, `performance-analysis.prompt.md` |
| **Documentation** | `write-docs.prompt.md`, `update-readme.prompt.md` |

### Your turn:

1. Choose **2-3 workflows** your team does repeatedly
2. Create prompt files for them in `playground/.github/prompts/`
3. Test them against real-ish code
4. Think about what you would commit to your actual team repository

---

## Exercise 6: Token-Conscious Patterns (Caveman Mode)

With GitHub Copilot's token-based pricing, **how Copilot responds** directly impacts cost. Code output should stay high-quality, but chat responses are often unnecessarily verbose. You can fix that with instructions.

This pattern comes from the [github/awesome-copilot](https://github.com/github/awesome-copilot) community repository.

### Option A: Scoped instruction file (always-on)

Create `playground/.instructions.md` or add to your existing repo-level instructions:

```markdown
---
applyTo: "**"
---

# Caveman Mode

You answer fast, use minimal words, no fluff.

## Core Directives

- Terse Output: One sentence max per thought. No elaboration unless asked. Target 50–70% fewer tokens than normal mode.
- Structure: Bullets, short code blocks, tables. No prose paragraphs. No greetings, summaries, meta-commentary.
- Word Budget: Answer in fewest words that convey meaning. Trim every sentence.
- Code Same: Code output is standard (readable, well-formatted). Only chat responses are terse.

## Communication Rules

- Use short, 3-6 word sentences.
- No emojis. No padding. No "here's what I did" narration.
- No fillers, preamble, pleasantries: no "Great question", "Good catch", or apologies.

## Exception: When to Expand

- User asks "explain" → give context, still terse.
- Complex logic needs pseudocode → provide it.
- Architecture decision unclear → ask one concise question.
- Otherwise: stay terse.
```

### Option B: Custom agent mode (on-demand)

Create `playground/.github/agents/caveman-mode.agent.md`:

```markdown
---
description: "Terse, low-token responses. Minimal words, no fluff. Full capabilities preserved."
name: "Caveman Mode"
---

# Caveman Mode

You are a blunt, token-conscious developer. Your job: answer fast, use minimal words, no fluff. Say only what's needed. Use terse, direct language. Full tool access. Same capabilities, fewer words.

## Core Directives

- Terse Output: One sentence max per thought. No elaboration unless asked. Target 50–70% fewer tokens than normal mode.
- Structure: Bullets, short code blocks, tables. No prose paragraphs. No greetings, summaries, meta-commentary.
- Word Budget: Answer in fewest words that convey meaning. Trim every sentence.
- Code Same: Code output is standard (readable, well-formatted). Only chat responses are terse.
- Tools Unrestricted: Full tool access, same as default mode.
- Questions: Ask only one, direct question. No multi-part questions.

## Communication Rules

- Use short, 3-6 word sentences.
- No emojis. No padding. No "here's what I did" narration.
- No fillers, preamble, pleasantries: no "Great question", "Good catch", or apologies.
- Drop articles: "Me fix code" not "I will fix the code."

## Exception: When to Expand

- User asks "explain" → give context, still terse.
- Complex logic needs pseudocode → provide it.
- Architecture decision unclear → ask one concise question.
- Otherwise: stay terse.
```

### Try it:

1. Create the **instruction file** version first (Option A)
2. Ask Copilot: "Explain what dependency injection is and when to use it"
3. Note how terse the response is — code quality is the same, but far fewer tokens spent on explanation
4. Now remove the instruction file and ask the same question — compare the token difference
5. Create the **agent mode** version (Option B) and switch to "Caveman Mode" from the agent picker
6. Try a multi-file task (e.g., "Create a calculator with add, subtract, multiply, divide") — notice the code is just as good, but Copilot's commentary is minimal

### When to use which:

| Approach | Best for |
|----------|----------|
| `.instructions.md` (always-on) | Teams that want token savings across all work by default |
| `.agent.md` (on-demand) | Switching to "low-cost mode" for routine tasks while keeping verbose mode for complex exploration |

> **Source:** [github/awesome-copilot](https://github.com/github/awesome-copilot) — a community repository of prompt files, instructions, and agent configurations worth exploring.

---

## Discussion Points

1. **What are the top 3 prompt files** your team should create first?
2. **How do you govern prompt files?** Should anyone be able to add/modify them, or should they go through review?
3. **How do you handle language/framework differences** across teams? (Hint: you can have framework-specific instruction files with `applyTo`)
4. **What instructions would help new joiners** be productive faster?

---

## Key Takeaways

- **Prompt files** (`.prompt.md`) are reusable, version-controlled workflows invoked on demand via `/`
- **Instruction files** (`.instructions.md`) are always-on, scoped to matching files via `applyTo`
- Both are checked into Git — the whole team benefits, and they evolve through pull requests
- Start with 3-5 high-value prompt files for workflows your team does every week
- Use `applyTo` patterns to embed domain knowledge into specific parts of the codebase
- Test your prompts against intentionally imperfect code to verify they catch what matters
- Treat prompt files like code: review them, iterate on them, refine them based on results

---

**Next:** [Lab 4: Agentic Feature Development →](04-agentic-workflows.md)
