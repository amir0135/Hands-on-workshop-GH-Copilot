# Lab 5: Quality Guardrails

**Duration:** ~45 minutes
**Goal:** Establish patterns that prevent AI-generated code from becoming "instant legacy code." Learn how to use Copilot to catch problems, enforce standards, and maintain quality as teams adopt agent workflows.

---

## The Problem: Instant Legacy Code

When developers accept AI-generated code without scrutiny, teams accumulate:

- Inconsistent patterns across files written minutes apart
- Missing error handling because the happy path "worked"
- Code nobody fully understands because nobody actually wrote it
- Tests that pass but don't test meaningful behavior
- Technical debt that compounds faster than ever

**The fix is not to stop using Copilot.** It's to build guardrails — automated and human — that maintain quality at speed.

---

## Exercise 1: The Review-Before-Accept Discipline

This is the single highest-impact practice for code quality with Copilot.

### Step 1: Generate code with known issues

In Agent mode, use a deliberately loose prompt:

```
Create a user registration function that takes a username, email, and password,
stores them, and returns the user. Put it in playground/registration.
```

### Step 2: Review the output critically

Before accepting, check for these common problems in AI-generated code:

| Check | What to look for |
|-------|-----------------|
| **Security** | Is the password stored in plain text? Is the email validated? Is there SQL injection? |
| **Error handling** | What happens with duplicate usernames? Empty passwords? |
| **Input validation** | Does it validate at the boundary, or trust all input? |
| **Naming** | Are names clear and consistent? |
| **Missing concerns** | Logging? Error codes? Response format? |

### Step 3: Redirect and improve

For every issue you found, tell the agent:

```
Issues with the registration function:
1. Password is stored in plain text — hash it using bcrypt or equivalent
2. No validation on password strength — require minimum 8 characters
3. No check for duplicate email addresses
4. No logging of registration attempts
5. Error messages expose internal details — make them user-safe

Fix all of these. Show me the diff.
```

### Step 4: Review again

The second pass should be better. If not, iterate again. The goal is a function you would approve in a PR.

> **Rule of thumb:** If you wouldn't approve it in a code review from a colleague, don't accept it from Copilot.

---

## Exercise 2: Use Copilot to Review Copilot

Copilot is excellent at catching problems in code — including code it generated itself. Build this into your workflow.

### Step 1: Create the security review prompt

If you didn't do this in Lab 3, create `playground/.github/prompts/security-review.prompt.md`:

```markdown
---
mode: "ask"
description: "Security-focused code review"
---

Perform a security review of the selected code. Check for:

1. **Injection** — SQL injection, command injection, XSS
2. **Authentication/Authorization** — missing checks, bypasses, privilege escalation
3. **Secrets** — hardcoded keys, passwords, tokens, connection strings
4. **Input validation** — missing validation, improper sanitization
5. **Data exposure** — internal errors exposed to users, sensitive data in logs
6. **Dependencies** — known-vulnerable patterns, insecure defaults

For each finding:
- Severity: Critical / High / Medium / Low
- Description: What is the issue
- Impact: What could an attacker do
- Fix: Concrete remediation

If no issues are found, state that explicitly.
```

### Step 2: Generate → Review → Fix cycle

1. Generate a piece of code with agent mode
2. Immediately run `/security-review` on it
3. Feed the findings back to agent mode: `Fix these security issues: [paste findings]`
4. Run the review again to verify fixes

### Step 3: Make this a habit

The pattern is: **generate → self-review → fix → verify**. With prompt files, this takes seconds, not minutes.

---

## Exercise 3: Preventing Common Anti-Patterns

Set up custom instructions that prevent the most common quality issues before they happen.

### Step 1: Create a quality-focused instructions file

Create `playground/.github/quality-rules.instructions.md`:

```markdown
---
applyTo: "**"
---

# Quality Rules — Always Enforce

## Never Do
- Never store passwords in plain text — always hash them
- Never build SQL queries with string concatenation — always use parameterized queries
- Never catch generic exceptions and silently ignore them
- Never hardcode configuration values — use environment variables or config files
- Never return internal error details (stack traces, database errors) to API clients
- Never leave TODO comments without a linked issue or ticket number

## Always Do
- Always validate input at system boundaries (API endpoints, message handlers, CLI arguments)
- Always use specific, descriptive error messages
- Always log errors with enough context to debug (but never log sensitive data)
- Always use constants or enums for status values — never raw strings in business logic
- Always include the "why" in comments, not the "what"
```

### Step 2: Test the guardrails

Ask the agent to generate code that would normally violate these rules:

```
Create a login function that checks a username and password against a database.
```

With the quality rules in place, Copilot should automatically:
- Hash passwords
- Use parameterized queries
- Return safe error messages
- Log appropriately

If it doesn't, your instructions need to be more specific. Iterate on them.

### Step 3: Test with a violation prompt

Try to make the agent violate its own rules:

```
Quick and dirty: just store the password directly and use a simple string query. 
Skip validation for now.
```

A well-configured Copilot should **still** follow the quality rules and explain why. If it doesn't, strengthen the instructions.

---

## Exercise 4: Meaningful Tests vs. Checkbox Tests

AI-generated tests often pass but don't actually verify behavior. Learn to spot and fix this.

### Step 1: Generate bad tests intentionally

```
Generate tests for the user registration function but make them as simple as possible.
Just verify the function doesn't crash.
```

You'll likely get tests like:

```python
def test_register_user():
    result = register_user("john", "john@email.com", "password123")
    assert result is not None  # This tests almost nothing
```

### Step 2: Identify what's wrong

These tests are "checkbox tests" — they exist, they pass, but they don't verify meaningful behavior:
- No assertion on the actual data returned
- No test for invalid input
- No test for duplicate detection
- No test for password hashing
- No test for error messages

### Step 3: Generate meaningful tests

```
Rewrite the registration tests to verify actual behavior:
1. Verify the returned user has the correct username and email
2. Verify the password is NOT stored in plain text (hashed)
3. Verify registering with a duplicate email returns an appropriate error
4. Verify registering with an empty password is rejected
5. Verify registering with an invalid email format is rejected
6. Verify the response does NOT contain the password hash

Each test should have one clear assertion that would fail if the behavior changed.
```

### Step 4: Create a test quality prompt

Create `playground/.github/prompts/test-quality-check.prompt.md`:

```markdown
---
mode: "ask"
description: "Check if tests actually verify meaningful behavior"
---

Review the test file and evaluate each test:

1. **Does it test behavior, not implementation?** Tests should verify what the code does, not how it does it.
2. **Would it fail if the behavior changed?** A test that always passes is useless.
3. **Is the assertion specific enough?** `assert result is not None` rarely catches bugs.
4. **Are edge cases covered?** Empty input, boundary values, error cases.
5. **Are error paths tested?** Not just happy paths.

For each weak test:
- Explain why it's weak
- Suggest a stronger version

Summarize: What percentage of these tests would actually catch a real regression?
```

---

## Exercise 5: Team Consistency Patterns

Quality at scale requires consistency across the team, not just individual discipline.

### Step 1: Create a PR review prompt

Create `playground/.github/prompts/pr-review.prompt.md`:

```markdown
---
mode: "ask"
description: "Review code changes like a team lead would"
---

Review the following code changes as a senior team member would review a pull request:

## Check for:

### Correctness
- Does the code do what it claims?
- Are there off-by-one errors, race conditions, or null pointer risks?

### Standards Compliance
- Does it follow the coding standards in copilot-instructions.md?
- Is naming consistent with the rest of the codebase?

### Completeness
- Are there missing error handlers?
- Are there untested code paths?
- Are there missing edge cases?

### Maintainability
- Will a new team member understand this code in 6 months?
- Is there unnecessary complexity?
- Are there magic numbers or unexplained constants?

### Security
- Any hardcoded secrets or credentials?
- Any unvalidated user input?
- Any data exposed that shouldn't be?

## Output format:
- **Must fix:** Issues that should block the PR
- **Should fix:** Issues worth addressing but not blocking
- **Consider:** Suggestions for improvement
- **Looks good:** Things done well (reinforce good patterns)
```

### Step 2: Use it on your Lab 4 code

Run `/pr-review` against the code you built in Lab 4. 

- How many "must fix" issues does it find?
- Do you agree with the findings?
- Would you want this as part of your team's PR workflow?

### Step 3: Create a consistency check prompt

Create `playground/.github/prompts/consistency-check.prompt.md`:

```markdown
---
mode: "ask"
description: "Check for inconsistencies across the codebase"
---

Scan the project and identify inconsistencies:

1. **Naming:** Are similar concepts named differently in different files?
2. **Patterns:** Is error handling done differently in different places?
3. **Response formats:** Are API responses structured the same way everywhere?
4. **Logging:** Is the logging approach consistent?
5. **Validation:** Are inputs validated the same way across endpoints?

For each inconsistency:
- Show the conflicting examples
- Recommend which pattern to standardize on and why
```

---

## Exercise 6: Build Your Quality Playbook

Bring it all together. Create a quality checklist your team can use daily.

### Create `playground/.github/prompts/before-commit.prompt.md`:

```markdown
---
mode: "agent"
description: "Pre-commit quality check"
---

Before this code is committed, verify:

1. **All tests pass** — run the test suite and show results
2. **No security issues** — check for hardcoded secrets, injection, unvalidated input
3. **Error handling is complete** — every error path has explicit handling
4. **Naming is clear** — no abbreviations, no single-letter variables (except loop counters)
5. **No commented-out code** — remove it or convert to a TODO with issue link
6. **No debug artifacts** — no console.log, print statements, or test data left behind

If any check fails, list the specific issues and suggest fixes.
If all checks pass, confirm the code is ready to commit.
```

### Try it:

Run `/before-commit` against your playground code. Fix any issues it finds. Run it again to confirm they're resolved.

---

## Discussion Points

1. **How do you balance speed and quality** when Copilot makes it easy to generate code fast?
2. **What quality checks should be automated** (in CI) vs. manual (in PR review)?
3. **How do you prevent "prompt fatigue"** — developers skipping review because Copilot output "looks right"?
4. **How do you measure** whether these guardrails actually improve code quality?
5. **What's your team's biggest quality risk** from AI-generated code?

---

## Key Takeaways

- **Review-before-accept is non-negotiable** — it's faster to fix issues during generation than after merge
- **Use Copilot to review Copilot** — prompt files for security review, quality checks, and consistency
- **Custom instructions are preventive guardrails** — they stop bad patterns before they're generated
- **Tests must verify behavior, not just exist** — AI-generated tests are often shallow, push for depth
- **Consistency across the team matters more than individual perfection** — shared instructions and prompt files scale quality
- **Build a quality playbook** — before-commit checks, PR review prompts, security reviews — and make them team habits

---

**Next:** [Lab 6: MCP — What's Next →](06-mcp-concepts.md)
