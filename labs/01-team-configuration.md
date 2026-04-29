# Lab 1: Team Configuration & Custom Instructions

**Duration:** ~45 minutes
**Goal:** Set up Copilot so it produces consistent, high-quality output that matches your team's standards — without every developer having to repeat the same instructions.

---

## Why This Matters

Without shared configuration, every developer gets different results from Copilot. One person gets clean code with proper error handling. Another gets a different naming convention. A third gets no tests. **Custom instructions solve this** by giving Copilot a shared understanding of how your team works.

---

## Exercise 1: Create Repository-Level Instructions

The `.github/copilot-instructions.md` file tells Copilot how to behave for **everyone working in this repository**. This is checked into source control and shared with the team.

### Step 1: Create the file

Create a folder called `playground` inside this repository. This is where you will do all your lab exercises.

```bash
mkdir -p playground/.github
```

### Step 2: Write your first instructions file

Create `playground/.github/copilot-instructions.md` with the following content. **Read each section carefully** — these are the types of instructions that matter most for team consistency:

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
2. Ask: `Create a function that fetches user data from a REST API and handles the response`
3. Observe that the generated code follows your instructions — meaningful names, explicit error handling, no hardcoded values
4. Now ask the same question **without** the instructions file (temporarily rename it). Compare the results.

> **Key Takeaway:** The instructions file is your team's "coding standards for Copilot." It compounds — once set up, every developer benefits automatically.

---

## Exercise 2: Understand Instruction Scope & Hierarchy

Copilot instructions have a hierarchy. Understanding it helps you apply the right level of guidance.

| Scope | File | Who benefits | Use for |
|-------|------|-------------|---------|
| **Repository** | `.github/copilot-instructions.md` | Everyone on the project | Coding standards, architecture patterns, tech stack rules |
| **Folder** | `.github/copilot-instructions.md` in any subfolder, or `.instructions.md` files | Anyone working in that area | Module-specific patterns (e.g., "this folder uses repository pattern") |
| **Personal** | VS Code user settings | Just you | Personal preferences (verbosity, language, editor habits) |

### Try it:

1. Create a subfolder in your playground: `mkdir -p playground/api`
2. Create `playground/api/.instructions.md` with:

```markdown
# API Layer Instructions
- All API endpoints must return consistent response envelopes: `{ data, error, status }`
- Use middleware for authentication — do not check auth in individual handlers
- All endpoints must validate input before processing
```

3. Open Copilot Chat in Agent mode, make sure your working context is the `playground/api` folder
4. Ask: `Create a POST endpoint for creating a new user`
5. Notice how Copilot combines both the repository-level and folder-level instructions

---

## Exercise 3: Configure VS Code Settings for Your Team

Some Copilot behaviors are controlled by VS Code settings. Teams should align on these.

### Recommended team settings

Create `playground/.vscode/settings.json`:

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

1. Open `playground/.github/copilot-instructions.md`
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

**Next:** [Lab 2: Agent Mode Mastery →](02-agent-mode-mastery.md)
