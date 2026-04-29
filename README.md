# GitHub Copilot — Advanced Hands-on Workshop

An advanced, hands-on workshop for development teams who already use GitHub Copilot and want to **level up with agent workflows, team-wide best practices, and quality guardrails** they can apply immediately.

> This is not an introduction to Copilot. Participants should already be familiar with basic Copilot features (inline completions, Copilot Chat). This workshop focuses on **how teams work together with Copilot to ship better code, faster**.

---

## Workshop Goals

By the end of this workshop, participants will be able to:

- Use **agent mode** effectively for multi-file, multi-step development tasks
- Set up **shared custom instructions** that make Copilot behave consistently across the team
- Create **reusable prompt files** for common workflows (reviews, refactoring, onboarding)
- Apply **quality guardrails** to prevent "instant legacy code" from AI-generated output
- Build complete features end-to-end using **agentic workflows**
- Understand what **MCP** enables and when to adopt it (conceptual — no hands-on)

---

## Agenda (Full Day)

| Time | Lab | Focus |
|------|-----|-------|
| 09:00–09:30 | [Lab 0: Getting Aligned](labs/00-getting-aligned.md) | Verify setup, learn the three modes, warm-up exercise |
| 09:30–10:15 | [Lab 1: Team Configuration](labs/01-team-configuration.md) | Custom instructions, shared settings, coding standards |
| 10:15–10:30 | Break | |
| 10:30–11:30 | [Lab 2: Agent Mode Mastery](labs/02-agent-mode-mastery.md) | Agent mode deep dive, the "junior developer" mental model |
| 11:30–12:15 | [Lab 3: Prompt Files & Reusable Instructions](labs/03-prompt-files-and-instructions.md) | `.prompt.md`, `.instructions.md`, `applyTo`, team prompt libraries |
| 12:15–13:15 | Lunch | |
| 13:15–14:15 | [Lab 4: Agentic Feature Development](labs/04-agentic-workflows.md) | End-to-end feature building, spec-to-code, TDD with Copilot |
| 14:15–14:30 | Break | |
| 14:30–15:15 | [Lab 5: Quality Guardrails](labs/05-quality-and-review.md) | Preventing bad patterns, review strategies, team consistency |
| 15:15–15:45 | [Lab 6: MCP — What's Next](labs/06-mcp-concepts.md) | Conceptual overview, governance, when to adopt |
| 15:45–16:00 | Wrap-up & Discussion | Q&A, action items, what to do Monday morning |

---

## Prerequisites

Before the workshop, every participant must complete the setup in **[PREREQUISITES.md](PREREQUISITES.md)**.

**Summary:**
- VS Code (latest stable) with GitHub Copilot and GitHub Copilot Chat extensions
- GitHub Copilot license (Business or Enterprise)
- Git installed and configured
- A programming language toolchain installed (.NET, Python, Java, TypeScript — whatever you use daily)
- Agent mode enabled in VS Code settings

---

## How This Workshop Works

**Hands-on first.** Every lab has exercises you do yourself in VS Code. Facilitators are available to help, but the goal is learning by doing — not watching slides.

**Language-agnostic where possible.** Most labs work regardless of your programming language. Where code is needed, choose the language you use at work. The patterns transfer across languages.

**Team-oriented.** Many exercises involve creating shared configurations that benefit your whole team. Think about your real projects as you work through the labs.

**Progressive.** Labs build on each other. Lab 0 gets everyone aligned, Lab 1 sets up the foundation, Labs 2–3 teach the core skills, Labs 4–5 apply them to real workflows, and Lab 6 looks ahead.

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
  00-getting-aligned.md                ← Lab 0: Setup verification & warm-up
  01-team-configuration.md             ← Lab 1: Custom instructions & team setup
  02-agent-mode-mastery.md             ← Lab 2: Agent mode deep dive
  03-prompt-files-and-instructions.md  ← Lab 3: Prompt files & reusable instructions
  04-agentic-workflows.md              ← Lab 4: End-to-end agentic development
  05-quality-and-review.md             ← Lab 5: Quality guardrails
  06-mcp-concepts.md                   ← Lab 6: MCP overview (conceptual)
```
