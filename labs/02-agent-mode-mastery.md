# Lab 2: Agent Mode Mastery

**Duration:** ~60 minutes
**Goal:** Move beyond basic chat into agent mode — Copilot's most powerful interface for real development work. Learn when to use it, how to guide it, and how to think about it as a **junior developer on your team**.

---

## Agent Mode vs Ask vs Edit

Before diving in, understand the three Copilot Chat modes and when each is the right choice:

| Mode | What it does | Best for |
|------|-------------|----------|
| **Ask** | Answers questions, explains code | Understanding existing code, learning, quick questions |
| **Edit** | Modifies specific files you point it to | Targeted changes to known files, refactoring a specific function |
| **Agent** | Autonomously plans and executes multi-step tasks across your workspace | Building features, creating new files, running commands, multi-file changes |

**Agent mode** can:
- Read and write multiple files
- Run terminal commands (with your approval)
- Search your codebase for context
- Create new files and folders
- Iterate on its own work

> **Mental model:** Agent mode is a **junior developer** sitting next to you. It is fast, eager, and capable — but it needs direction, review, and course correction. You are the senior developer.

---

## Exercise 1: Your First Agent Task

### Step 1: Start a fresh agent session

1. Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`)
2. Switch to **Agent** mode (dropdown at the top of the chat panel)
3. Make sure you are working in the `playground` folder

### Step 2: Give agent mode a clear task

Type this prompt:

```
Create a simple REST API with the following:
- A data model for "Task" with fields: id, title, description, status (todo/in-progress/done), created_at
- CRUD endpoints (create, read, update, delete, list all)
- Input validation on create and update
- In-memory storage (no database needed)
- A basic health check endpoint

Use [your language: Python/FastAPI, .NET, Node.js/Express, etc.]
```

### Step 3: Observe and learn

Watch how agent mode works:

- **Does it plan first?** Good agents explain what they will do before doing it.
- **Does it create multiple files?** Agent mode should scaffold a proper project structure.
- **Does it ask to run commands?** It may want to initialize a project, install packages, etc.
- **Review every action.** Click "Accept" or "Reject" on each proposed change. This is your code review.

### Step 4: Review the output

Before accepting everything, ask yourself:
- Does the code follow your instructions from Lab 1?
- Is the error handling adequate?
- Would you approve this in a pull request?

If something is off, **tell the agent**:

```
The error handling in the create endpoint is too generic. 
Use specific error types and return appropriate HTTP status codes.
```

> **Key Insight:** The quality of agent output depends on the quality of your instructions and your willingness to iterate. Do not accept mediocre output.

---

## Exercise 2: Multi-File Operations

Agent mode shines when tasks span multiple files. This is where it dramatically outperforms basic chat.

### Step 1: Extend your API

Using the API from Exercise 1, give this prompt:

```
Add the following to the Task API:
1. A middleware/filter that logs every request (method, path, status code, duration)
2. A configuration system that reads settings from environment variables (PORT, LOG_LEVEL)
3. CORS configuration that allows requests from any localhost port
4. Update the main entry point to use all of the above
```

### Step 2: Notice the multi-file behavior

Agent mode should:
- Modify the existing main file
- Create new files for middleware/logging
- Create or update configuration files
- Keep everything consistent

### Step 3: Verify consistency

Ask the agent:

```
Show me how all these pieces connect. Walk me through the request flow 
from incoming HTTP request to response.
```

This forces the agent to verify its own work. If it finds inconsistencies, it will fix them.

---

## Exercise 3: Terminal Integration

Agent mode can run terminal commands — this is critical for real development workflows.

### Step 1: Ask agent to run your project

```
Run the API and verify it starts correctly. Show me how to test the health check endpoint.
```

Agent mode will:
1. Propose a terminal command to start the server
2. **Ask for your approval** before running it (this is a safety feature — always review)
3. Verify the output
4. Suggest a curl/test command

### Step 2: Ask agent to fix issues

If the server doesn't start (missing dependencies, port conflict, etc.), tell the agent:

```
The server failed to start. Here's the error: [paste error]
Fix the issue and try again.
```

Watch how it diagnoses and fixes problems — this iterative loop is where agent mode saves the most time.

### Step 3: Run tests

```
Create a simple test that verifies the health check endpoint returns 200.
Run the test and make sure it passes.
```

---

## Exercise 4: The Junior Developer Mental Model

This exercise teaches the most important skill: **how to direct agent mode effectively**.

### Bad prompts (too vague):

```
❌ "Make this better"
❌ "Add some tests"
❌ "Fix the code"
```

### Good prompts (specific, scoped, clear):

```
✅ "Add input validation to the create task endpoint. Title must be non-empty 
   and under 200 characters. Description is optional but if provided must be 
   under 2000 characters. Return 400 with a clear error message for invalid input."

✅ "Write unit tests for the task creation endpoint covering:
   1. Successful creation with all fields
   2. Creation with only required fields
   3. Rejection of empty title
   4. Rejection of title over 200 characters"

✅ "Refactor the request logging middleware to also track:
   - Request body size
   - Response body size  
   - Add a correlation ID header to each request for tracing"
```

### Practice:

Try each of these prompts with your API and compare the results:

1. **Vague:** `Add error handling`
2. **Specific:** `Add error handling to the update endpoint: return 404 if the task doesn't exist, return 400 if the status value is not one of todo/in-progress/done, and return 500 with a generic message for unexpected errors. Log the full error internally but don't expose it to the client.`

Notice how the specific prompt produces exactly what you need, while the vague prompt produces generic, potentially wrong code.

---

## Exercise 5: Course Correction and Iteration

Agent mode is iterative. You will almost never get perfect output on the first try — and that's fine. The key is knowing how to steer.

### Step 1: Start with a request that will need refinement

```
Add pagination to the list tasks endpoint.
```

### Step 2: Review and redirect

The agent will produce something. Now iterate:

```
Change the pagination to use cursor-based pagination instead of offset-based.
The cursor should be the task ID. Return a "next_cursor" field in the response.
```

### Step 3: Add constraints

```
Also add a maximum page size of 100 items. If the client requests more than 100,
cap it at 100 without returning an error. Default page size should be 20.
```

### Step 4: Ask for edge cases

```
What happens when there are no more results? Make sure the response clearly 
indicates this is the last page.
```

> **Pattern:** Start broad → review → narrow → review → add constraints → review. This mirrors how you would work with a junior developer: give them the task, review their work, guide them to improve it.

---

## Exercise 6: Context Management

Agent mode uses context from your workspace to make better decisions. Learn to control what context it sees.

### Using `#file` and `#codebase`

Try these:

```
Look at #file:playground/api/routes.py and add rate limiting to all endpoints.
```

```
#codebase How is error handling done in this project? Are there any inconsistencies?
```

### Using `@workspace`

```
@workspace What patterns are used for input validation across the project?
```

### Adding context explicitly

When the agent doesn't have enough context, give it:

```
Here is our API response format standard:
- Success: { "data": ..., "status": "ok" }
- Error: { "error": { "code": "...", "message": "..." }, "status": "error" }

Refactor all endpoints to use this format consistently.
```

---

## Exercise 7: Pick the Right Model

Copilot lets you choose the underlying model per chat (model selector at the bottom of the chat panel). The right choice saves tokens and gives better results.

### Quick decision guide

| Task | Model class | Why |
|------|------------|-----|
| Quick completion, simple refactor, "what does this regex do" | Fast / mini (e.g. GPT-4o-mini, Haiku-class) | Cheap, low-latency |
| General coding, multi-file edits | Default flagship (GPT-4.1, Claude Sonnet) | Best balance of cost and capability |
| Hard reasoning, architecture, gnarly bugs | Premium / reasoning (Claude Opus, o-series) | Worth the cost when stakes are high |
| Long codebase exploration | Large-context model | Avoid losing context across many files |

### Try it

Run *the same* prompt in two different models on a piece of your playground code:

```
Review this file for security issues, performance, and maintainability. Be specific.
```

Compare quality of findings, latency, and (if your plan exposes it) token cost.

### Rules of thumb

- **Default to the mid-tier model.** Right for ~80% of work.
- **Escalate to a reasoning model** when you've iterated twice and still aren't converging.
- **Drop to a fast model** for trivial completions and lookup-style questions.
- **Never use a reasoning model for `git status`-level questions** — it's expensive and slower.

---

## Exercise 8: Working Across Multiple Repositories

Real systems span repos. Here's how to give agent mode enough context without dragging everything in.

### Pattern A: Multi-root workspace

VS Code supports multi-root workspaces. Open all related repos in one window:

```
File → Add Folder to Workspace…
```

Save it as `myproject.code-workspace`. Now `#codebase` and `@workspace` see all of them.

### Pattern B: Contracts as the boundary

When you can't open both repos, copy the API contract (OpenAPI spec, `.proto`, type definitions) from the other repo into a `contracts/` folder in the current one:

```
Implement a client for the API defined in #file:contracts/orders-api.yaml.
Match the patterns of existing clients in #codebase.
```

Keep `contracts/` updated via a small CI sync job.

### Pattern C: GitHub MCP (if approved)

The GitHub MCP server lets Copilot search and read other repos directly. Governance considerations are covered in [Lab 6](06-mcp-concepts.md).

### Try it

1. Open this workshop repo plus *one of your real repos* as a multi-root workspace
2. Ask: `@workspace What patterns differ between these two projects?`
3. Notice how Copilot reasons across both

---

## Common Mistakes with Agent Mode

| Mistake | Why it's a problem | What to do instead |
|---------|-------------------|-------------------|
| Accepting everything without review | You ship code you don't understand | Review every change like a PR |
| Prompts that are too large | Agent loses focus, produces inconsistent output | Break large tasks into 2-3 focused prompts |
| Not iterating | First output is rarely perfect | Review → redirect → refine |
| Ignoring terminal output | Agent may run commands that fail silently | Always check command output |
| No custom instructions | Agent uses generic patterns | Set up Lab 1 instructions first |
| Treating it as magic | Leads to frustration | It's a junior dev — guide it, don't expect perfection |

---

## Discussion Points

1. **When would you NOT use agent mode?** (Quick lookups, simple renames, understanding code — use Ask or Edit instead)
2. **How do you decide when to stop iterating** and just fix it yourself?
3. **What's your strategy for reviewing agent output** before committing?
4. **How would you onboard a new team member** to use agent mode effectively?

---

## Key Takeaways

- Agent mode is for **multi-step, multi-file tasks** — not everything
- Think of it as a **junior developer**: capable but needs direction and review
- **Specific prompts** produce dramatically better results than vague ones
- **Always review** before accepting — you own the code, not the agent
- **Iterate**: start broad, review, narrow, review, constrain
- **Terminal integration** makes agent mode a real development partner, not just a text generator
- **Context matters**: use `#file`, `@workspace`, and explicit context to guide the agent
- **Pick the right model** for the task — default mid-tier, escalate when stuck, drop to fast for trivia
- **Multi-root workspaces** are the simplest way to give agents context across dependent repos

---

**Next:** [Lab 3: Prompt Files & Reusable Instructions →](03-prompt-files-and-instructions.md)
