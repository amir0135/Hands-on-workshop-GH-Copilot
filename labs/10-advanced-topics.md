# Lab 10: Beyond the Editor — CLI & the Bridge to Studio / Foundry

> **Track:** Bonus / self-paced

**Duration:** ~30 minutes (bonus / self-paced)
**Goal:** Cover two topics that don't fit naturally in the main labs — using Copilot **outside the editor** (CLI), and the path from `your custom agent in VS Code` to a **deployed agent** in Copilot Studio or Microsoft Foundry.

> Most participant questions from sign-up are now blended into Labs 1–9. This bonus lab handles the two that genuinely live outside the core flow.

---

## Section 1: GitHub Copilot CLI

Copilot is not just in the editor — there's a CLI for terminal-driven workflows.

### Install

```bash
gh extension install github/gh-copilot
```

(Requires the [GitHub CLI](https://cli.github.com/) `gh` to be installed and signed in.)

### The two commands you'll actually use

```bash
# "How do I do X in the shell?"
gh copilot suggest "find all files larger than 100MB modified in the last week"

# "What does this command do?"
gh copilot explain "find . -type f -size +100M -mtime -7"
```

### When CLI beats chat

- You're already in the terminal and don't want to context-switch
- You want a one-shot answer, not a conversation
- You're scripting / automating — CLI output is pipeable

### Pair it with agent mode

Use the CLI for fast shell intent ("how do I rebase onto main?"), then drop into agent mode in VS Code when the task crosses files.

### Try it

1. Install the extension
2. Run `gh copilot suggest "show disk usage by folder, sorted descending"`
3. Run `gh copilot explain "tar -czf - dir | ssh host 'tar -xzf - -C /tmp'"`
4. Pipe a suggestion into execution: review first, then run

> **Note:** The standalone GitHub Copilot CLI binary (`copilot`) and the `gh copilot` extension are evolving fast. Check `gh copilot --help` and the [Copilot CLI docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli) for current capabilities.

> **Want more?** [Lab 11: Copilot in the Terminal — The CLI Deep Dive](11-copilot-cli.md) is the advanced, experienced-user track: agentic CLI sessions, scripting and piping, MCP in the terminal, custom instructions headless, and CI automation.

---

## Section 2: From VS Code → Copilot Studio / Microsoft Foundry

You build & test agents in VS Code. When the agent needs to run *for other people, without you sitting at the keyboard*, it graduates to Copilot Studio or Microsoft Foundry.

### Mental model

| Layer | What it is | Lives in |
|-------|-----------|----------|
| **Copilot in VS Code** | Coding assistant for *you* | Your editor |
| **Custom agent (`.agent.md`)** | A specialized chat mode for your team | Your repo |
| **Copilot Studio agent** | A business-facing agent (e.g. HR bot, support bot) | Microsoft 365 / Teams |
| **Foundry agent** | A hosted, programmable agent with tools and an API | Azure AI Foundry |

### Decision: where does your agent belong?

```
Is the agent for you / your dev team only?
  Yes → Stay in VS Code as a .agent.md / SKILL.md
  No ↓

Is the audience employees in Teams / M365?
  Yes → Copilot Studio
  No ↓

Does the agent need to run programmatically (API, scheduled, embedded in an app)?
  Yes → Microsoft Foundry
```

### From `.agent.md` to a deployed agent

1. **Prototype** as a custom agent in VS Code (`.github/agents/<name>.agent.md`)
2. **Iterate** on instructions, tools, and example prompts using your team
3. **Decide the deployment surface** (table above)
4. **Migrate the system prompt and tool definitions** — both platforms accept Markdown-style instructions
5. **Wire up tools** — in Foundry, via the agent SDK; in Studio, via connectors and Power Platform actions

### Skills already in this workspace

This workspace ships with skills (and an agent) that handle the migration end-to-end:

- **`vscode-microsoft-foundry`** — end-to-end workflow for developing Foundry agent apps: scaffold, build, add tools, choose a model, deploy, evaluate
- **`microsoft-foundry`** — deploys, evaluates, and manages Foundry agents (Docker build, ACR push, batch eval, prompt optimization)
- **`AIAgentExpert`** (agent) — generates, debugs, evaluates, and deploys agents using the Microsoft Agent Framework
- **`foundrytk-quick-start`** — Foundry Toolkit (formerly AI Toolkit / AITK) walkthrough for VS Code
- **`microsoft-365-agents-toolkit`** — builds, tests, and deploys Microsoft 365 agents (Teams, Declarative Agents, Custom Engine Agents)

> **Prerequisites for the deploy step:** the *scaffold* exercise below works with no setup. To actually **deploy** to Foundry you need: an Azure subscription with access to Azure AI Foundry, a Foundry project, the [Azure Developer CLI (`azd`)](https://aka.ms/azd) and `az` signed in (`az login`), and Docker running. Without these, stop after the scaffold step — the generated code is still the useful takeaway.

### Try it

```
Use the vscode-microsoft-foundry skill to scaffold a simple agent that answers
questions about our product catalog.
Don't deploy yet — just generate the local code so I can review it.
```

Then, when you're ready to deploy (requires the prerequisites above):

```
Use the microsoft-foundry skill to deploy the agent we scaffolded to my Foundry project.
```

### Boundary

Don't try to do *everything* in VS Code. Once your agent has multiple users, scheduled triggers, or business connectors, that's Studio / Foundry territory. The skills above handle the migration.

---

## Where Everything Else Went

The earlier draft of this lab covered model selection, multi-repo work, skills/memory, diagrams, requirements, and test automation. Those topics have all been blended into the main labs:

| Topic | Now lives in |
|-------|-------------|
| Model selection (right model, right time) | [Lab 2 Exercise 7](02-agent-mode-mastery.md#exercise-7-pick-the-right-model) |
| Multi-repo / dependent repositories | [Lab 2 Exercise 8](02-agent-mode-mastery.md#exercise-8-working-across-multiple-repositories) |
| `SKILL.md` for domain knowledge | [Lab 3 Exercise 7](03-prompt-files-and-instructions.md#exercise-7-skills-skillmd--packaging-domain-knowledge) |
| `lessons.md` to stop re-discovering bugs | [Lab 3 Exercise 8](03-prompt-files-and-instructions.md#exercise-8-lessonsmd--stop-re-discovering-the-same-bugs) |
| Persistent memory (user / repo / session) | [Lab 3 Exercise 9](03-prompt-files-and-instructions.md#exercise-9-persistent-memory-built-in) |
| Token reduction checklist | [Lab 3 Exercise 10](03-prompt-files-and-instructions.md#exercise-10-token-reduction-checklist) |
| Requirements & refinement workflows | [Lab 4 Exercise 5](04-agentic-workflows.md#exercise-5-requirements--refinement-before-code) |
| Architecture diagrams (Mermaid / PlantUML / SysML) | [Lab 4 Exercise 6](04-agentic-workflows.md#exercise-6-architecture--diagrams-from-specs) |
| Test automation track (QA-focused) | [Lab 5 Exercise 7](05-quality-and-review.md#exercise-7-test-automation-track-qa--automation-engineers) |

---

## Resources

- [Copilot CLI docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- [Microsoft Foundry](https://ai.azure.com/)
- [Copilot Studio](https://copilotstudio.microsoft.com/)
- [github/awesome-copilot](https://github.com/github/awesome-copilot)

---

**See also (bonus / self-paced):** [Lab 8: MCP →](08-mcp-concepts.md) · [Lab 9: Custom Chat Modes & Subagents →](09-chat-modes-and-subagents.md) · [Lab 11: Copilot CLI Deep Dive →](11-copilot-cli.md)

**Back to:** [Workshop README →](../README.md)
