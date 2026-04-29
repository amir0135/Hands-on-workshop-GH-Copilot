# GitHub Copilot — Best Practices Cheat Sheet

A one-page reference for daily use. Print it, pin it, share it.

---

## The Golden Rule

> **Review everything. Accept nothing you don't understand.**

---

## Custom Instructions (Set Up Once, Benefit Always)

| File | Purpose | Scope |
|------|---------|-------|
| `.github/copilot-instructions.md` | Team coding standards | Entire repo, always on |
| `.instructions.md` (with `applyTo`) | Module-specific rules | Matching files, always on |
| `.github/prompts/*.prompt.md` | Reusable workflows | On demand via `/` |

**Start with:** `copilot-instructions.md` covering naming, error handling, testing, security.

---

## Choosing the Right Mode

| Task | Mode | Example |
|------|------|---------|
| Quick question | **Ask** | "What does this regex do?" |
| Change specific code | **Edit** | "Add error handling to this function" |
| Build something new | **Agent** | "Create a notification service with these requirements" |
| Multi-file refactoring | **Agent** | "Extract this logic into a service layer" |

---

## Writing Effective Prompts

### Do

- Be specific about requirements, constraints, and expected behavior
- Reference files: `#file:path/to/file.ts`
- Reference the codebase: `#codebase` or `@workspace`
- Include examples of desired output format
- Break large tasks into focused steps

### Don't

- "Make this better" (better how?)
- "Add some tests" (what should they test?)
- "Fix the code" (what's wrong with it?)
- Combine 5+ requirements in one prompt (split them)

---

## The Agentic Development Loop

```
1. Specify  →  Write a short spec or clear requirements
2. Generate  →  Use agent mode to build it
3. Review    →  Read every diff like a pull request
4. Test      →  Run tests, verify behavior
5. Iterate   →  Redirect and refine (at least once)
6. Ship      →  Commit only what you'd approve from a colleague
```

---

## Quality Checklist (Before Every Commit)

- [ ] Code does what was requested
- [ ] Error handling is explicit, not generic
- [ ] Input is validated at system boundaries
- [ ] No hardcoded secrets or credentials
- [ ] No SQL injection or string-concatenated queries
- [ ] Tests verify behavior, not just existence
- [ ] Names are descriptive and consistent
- [ ] No debug artifacts (print statements, console.log)
- [ ] Comments explain "why", not "what"

---

## Common AI Code Smells

| Smell | What it looks like | Fix |
|-------|-------------------|-----|
| Shallow tests | `assert result is not None` | Assert on actual values and behavior |
| Generic catch | `catch (Exception e) { }` | Catch specific exceptions, handle meaningfully |
| Over-commenting | `// increment counter` on `counter++` | Remove obvious comments, keep "why" comments |
| Inconsistent patterns | Different error formats in different files | Use custom instructions to enforce consistency |
| Missing validation | Trusting all input blindly | Validate at every system boundary |
| Copy-paste sprawl | Same logic duplicated across files | Extract into shared functions/services |

---

## Token Management

> With token-based pricing (June 2025+), how Copilot *responds* impacts cost — not just what it generates.

- **Use Caveman Mode** — Add a `.instructions.md` or custom agent that targets 50–70% fewer tokens on chat responses while keeping code quality identical. See [Lab 3, Exercise 6](labs/03-prompt-files-and-instructions.md) and [github/awesome-copilot](https://github.com/github/awesome-copilot)
- **Ask mode for questions** — Don't use Agent mode just to ask a question (Agent costs more tokens)
- **Be specific** — Vague prompts cause longer, more expensive back-and-forth
- **Review at each step** — Catching issues early avoids costly multi-iteration loops

---

## Agent Mode Tips

- **Start small, build up** — Don't ask for everything at once
- **Review at each step** — Not at the end of a 20-file generation
- **Tell it what's wrong** — "The error handling is too generic" > "Try again"
- **Use specs** — Even 5 lines of requirements dramatically improve output
- **It's a junior dev** — Guide it, review it, course-correct it
- **Know when to stop** — If iteration 3+ isn't converging, write it yourself

---

## Team Prompt Files Worth Creating First

1. **`code-review.prompt.md`** — Structured review for security, quality, consistency
2. **`write-tests.prompt.md`** — Generate meaningful tests with edge cases
3. **`refactor.prompt.md`** — Clean up code while preserving behavior
4. **`before-commit.prompt.md`** — Pre-commit quality check
5. **`explain-code.prompt.md`** — Onboarding-friendly code explanations

---

## What to Do Monday Morning

1. Create `.github/copilot-instructions.md` in your team's main repository
2. Add your coding standards, naming conventions, and security rules
3. Create 2-3 prompt files for your team's most common workflows
4. Share with the team via a pull request
5. Iterate based on what works and what doesn't
