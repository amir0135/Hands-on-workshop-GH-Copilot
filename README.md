# GitHub Copilot — Hands-on Workshop

A hands-on workshop that takes development teams from **everyday Copilot use to advanced agent workflows, team-wide best practices, and quality guardrails** they can apply the very next morning.

> **Built for mixed rooms.** Whether this is your first week with Copilot or you've been driving agent mode for months, every lab has a **🌱 Foundation path** to get you grounded and a **🚀 Advanced stretch** to push you further. Nobody is bored; nobody is lost.

---

## Workshop Goals

By the end of this workshop, participants will be able to:

- Use the **three Copilot modes** (Ask, Plan, Agent) and pick the right one for the job
- Use **agent mode** effectively for multi-file, multi-step development tasks
- Set up **shared custom instructions** that make Copilot behave consistently across the team
- Create **reusable prompt files** for common workflows (reviews, refactoring, onboarding)
- Apply **quality guardrails** to prevent "instant legacy code" from AI-generated output
- Build complete features end-to-end using **agentic workflows**
- Debug failing code and **tame legacy / unfamiliar codebases** with Copilot
- Personalize Copilot with **custom chat modes and subagents**
- Understand what **MCP** enables and when to adopt it
- Ship a real feature in a **team capstone** that ties everything together

---

## Who This Is For

| You are... | You'll get... |
|------------|---------------|
| **New to Copilot** | A guided on-ramp in every lab. Start with the 🌱 Foundation path, follow the exact steps, and build confidence fast. |
| **An everyday user** | The team-scale practices most people miss — instructions, prompt files, review discipline, and agentic workflows. |
| **An advanced user** | 🚀 Advanced stretch challenges in every lab, plus dedicated labs on legacy code, custom chat modes, subagents, and a capstone. |
| **A team lead / champion** | A blueprint for rolling Copilot out consistently across your team, with governance and quality built in. |

> **Pace yourself.** Do the 🌱 Foundation path first. If you finish early, jump straight into the 🚀 Advanced stretch — don't wait for the room. Facilitators float to help wherever you are.

---

## Agenda (09:00–15:30)

| Time | Lab | Focus |
|------|-----|-------|
| 09:00–09:30 | [Lab 0: Getting Aligned](labs/00-getting-aligned.md) | Setup check, skill self-assessment, the three modes, warm-up |
| 09:30–10:15 | [Lab 1: Team Configuration](labs/01-team-configuration.md) | Custom instructions, shared settings, coding standards |
| 10:15–10:25 | ☕ Break | |
| 10:25–11:30 | [Lab 2: Agent Mode Mastery](labs/02-agent-mode-mastery.md) | Agent mode deep dive, the "junior developer" mental model |
| 11:30–12:15 | [Lab 3: Prompt Files & Instructions](labs/03-prompt-files-and-instructions.md) | `.prompt.md`, `.instructions.md`, `applyTo`, skills, memory |
| 12:15–13:00 | 🍽️ Lunch | |
| 13:00–14:00 | [Lab 4: Agentic Feature Development](labs/04-agentic-workflows.md) | End-to-end feature building, spec-to-code, TDD with Copilot |
| 14:00–14:45 | [Lab 5: Quality Guardrails](labs/05-quality-and-review.md) | Preventing bad patterns, review strategies, team consistency |
| 14:45–14:55 | ☕ Break | |
| 14:55–15:20 | [Lab 8: Debugging & Legacy Code](labs/08-debugging-and-legacy-code.md) | Fix failing code, understand & modernize unfamiliar codebases |
| 15:20–15:30 | [Lab 10: Capstone Kickoff](labs/10-capstone.md) + Wrap-up | Team challenge brief, Q&A, what to do Monday morning |
| Bonus / self-paced | [Lab 6: MCP](labs/06-mcp-concepts.md) · [Lab 9: Chat Modes & Subagents](labs/09-chat-modes-and-subagents.md) · [Lab 7: Beyond the Editor](labs/07-advanced-topics.md) · [Lab 10 Capstone](labs/10-capstone.md) | MCP, custom modes, Copilot CLI, Studio / Foundry bridge, full team build |

> **The core arc is Labs 0–5 + 8**, sized to fit the day. Labs 6, 7, 9, and 10 are bonus/self-paced — pick them up if your team moves fast or continue them after the session. The facilitator can flex the back half to the room's energy.

---

## How the Dual-Track Works

Every lab is split so the whole room moves together without holding anyone back:

- **🌱 Foundation path** — the must-do exercises. Clear, step-by-step, language-agnostic. If you do only these, you leave with the core skills.
- **🚀 Advanced stretch** — optional challenges at the end of each lab for people who finish early or already know the basics. These go deeper: harder prompts, edge cases, automation, and team-scale patterns.
- **💬 Discussion points** — table conversations that work for any level and surface real-world tradeoffs.

Look for these icons throughout the labs.

---

## Topics from Participant Requests

Participants asked about specific topics during sign-up. They are blended into the labs where they fit.

| Ask | Where it's covered |
|-----|-------------------|
| Getting started / first steps with Copilot | [Lab 0](labs/00-getting-aligned.md) (🌱 Foundation path throughout) |
| Efficient use of agents, do's and don'ts | [Lab 2](labs/02-agent-mode-mastery.md), [Lab 5](labs/05-quality-and-review.md) |
| Model selection (right model at right time) | [Lab 2 Ex. 7](labs/02-agent-mode-mastery.md#exercise-7-pick-the-right-model) |
| Working with dependent / multiple repositories | [Lab 2 Ex. 8](labs/02-agent-mode-mastery.md#exercise-8-working-across-multiple-repositories) |
| Token reduction (Caveman Mode) | [Lab 3 Ex. 6](labs/03-prompt-files-and-instructions.md#exercise-6-token-conscious-patterns-caveman-mode) |
| Skills (`SKILL.md`), reusable across projects | [Lab 3 Ex. 7](labs/03-prompt-files-and-instructions.md#exercise-7-skills-skillmd--packaging-domain-knowledge) |
| `lessons.md` — saving lessons learned to lower tokens | [Lab 3 Ex. 8](labs/03-prompt-files-and-instructions.md#exercise-8-lessonsmd--stop-re-discovering-the-same-bugs) |
| Persistent memory (user / repo / session) | [Lab 3 Ex. 9](labs/03-prompt-files-and-instructions.md#exercise-9-persistent-memory-built-in) |
| Token reduction checklist | [Lab 3 Ex. 10](labs/03-prompt-files-and-instructions.md#exercise-10-token-reduction-checklist) |
| Agents for requirements & refinement, not just code | [Lab 4 Ex. 5](labs/04-agentic-workflows.md#exercise-5-requirements--refinement-before-code) |
| Architecture work — Mermaid, PlantUML, SysML v2 | [Lab 4 Ex. 6](labs/04-agentic-workflows.md#exercise-6-architecture--diagrams-from-specs) |
| Test automation use cases (non-developers) | [Lab 5 Ex. 7](labs/05-quality-and-review.md#exercise-7-test-automation-track-qa--automation-engineers) |
| Debugging failing code with Copilot | [Lab 8](labs/08-debugging-and-legacy-code.md) |
| Understanding & modernizing legacy / unfamiliar code | [Lab 8](labs/08-debugging-and-legacy-code.md) |
| Custom chat modes & specialized agents | [Lab 9](labs/09-chat-modes-and-subagents.md) |
| Delegating work to subagents | [Lab 9](labs/09-chat-modes-and-subagents.md) |
| MCP integration & tools | [Lab 6](labs/06-mcp-concepts.md) |
| Copilot CLI usage | [Lab 7 §1](labs/07-advanced-topics.md#section-1-github-copilot-cli) |
| Bridge from VS Code → Copilot Studio / Microsoft Foundry | [Lab 7 §2](labs/07-advanced-topics.md#section-2-from-vs-code--copilot-studio--microsoft-foundry) |
| Improving how you phrase a task / prompt | [Lab 2 Ex. 4](labs/02-agent-mode-mastery.md), [Lab 4](labs/04-agentic-workflows.md) |
| Context-aware agents on legacy code | [Lab 1](labs/01-team-configuration.md), [Lab 8](labs/08-debugging-and-legacy-code.md) |

---

## Prerequisites

Before the workshop, every participant must complete the setup in **[PREREQUISITES.md](PREREQUISITES.md)**.

**Summary:**
- VS Code (latest stable — **1.99 or newer**, ideally 1.105+) with GitHub Copilot and GitHub Copilot Chat extensions
- GitHub Copilot license (any tier; Business or Enterprise unlocks the team features in Labs 1, 3, and 9)
- Git installed and configured
- A programming language toolchain installed (.NET, Python, Java, TypeScript — whatever you use daily)
- Agent mode enabled in VS Code settings (the chat mode picker should show **Agent**, **Ask**, **Plan**)

> **New to Copilot?** That's fine — the prerequisites are just about having a working environment. You do not need prior Copilot experience to start. Lab 0 brings everyone to the same baseline.

---

## How This Workshop Works

**Hands-on first.** Every lab has exercises you do yourself in VS Code. Facilitators are available to help, but the goal is learning by doing — not watching slides.

**Dual-track.** Do the 🌱 Foundation path first, then reach for 🚀 Advanced stretch challenges if you have time. Move at your own pace.

**Language-agnostic where possible.** Most labs work regardless of your programming language. Where code is needed, choose the language you use at work. The patterns transfer across languages.

**Team-oriented.** Many exercises involve creating shared configurations that benefit your whole team. Think about your real projects as you work through the labs.

**Progressive.** Labs build on each other. Lab 0 gets everyone aligned, Lab 1 sets up the foundation, Labs 2–3 teach the core skills, Labs 4–5 apply them, Lab 8 handles real-world debugging and legacy code, Lab 9 personalizes Copilot, Lab 6 looks ahead, and Lab 10 ties it all together in a capstone.

---

## Quick Reference

- [Best Practices Cheat Sheet](best-practices.md) — One-page reference for daily use
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [Custom Instructions Reference](https://code.visualstudio.com/docs/copilot/copilot-customization)

---

## Repository Structure

```
README.md                              ← You are here
PREREQUISITES.md                       ← Setup guide (complete before workshop)
best-practices.md                      ← Quick reference for daily use
labs/
  00-getting-aligned.md                ← Lab 0: Setup, self-assessment & warm-up
  01-team-configuration.md             ← Lab 1: Custom instructions & team setup
  02-agent-mode-mastery.md             ← Lab 2: Agent mode deep dive
  03-prompt-files-and-instructions.md  ← Lab 3: Prompt files & reusable instructions
  04-agentic-workflows.md              ← Lab 4: End-to-end agentic development
  05-quality-and-review.md             ← Lab 5: Quality guardrails
  06-mcp-concepts.md                   ← Lab 6: MCP overview (conceptual)
  07-advanced-topics.md                ← Lab 7: Beyond the editor — CLI & Studio/Foundry (bonus)
  08-debugging-and-legacy-code.md      ← Lab 8: Debugging & taming legacy code
  09-chat-modes-and-subagents.md       ← Lab 9: Custom chat modes & subagents
  10-capstone.md                       ← Lab 10: Team capstone challenge
```
