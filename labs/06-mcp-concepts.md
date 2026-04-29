# Lab 6: MCP — What's Next (Conceptual)

**Duration:** ~30 minutes
**Goal:** Understand what the Model Context Protocol (MCP) enables, when your team should consider adopting it, and what governance is needed — without installing or configuring anything.

> **This lab is intentionally conceptual.** MCP requires security review, approval workflows, and infrastructure decisions that are beyond the scope of a hands-on workshop. The goal here is to give you the knowledge to have an informed conversation with your team about if and when to adopt MCP.

---

## What is MCP?

**Model Context Protocol (MCP)** is a standard that lets AI assistants like Copilot use external tools and data sources — reliably, securely, and with maintained context across interactions.

Think of it as a **plugin system for Copilot**. Without MCP, Copilot can only see your open files and workspace. With MCP, Copilot can:

- Query your Azure resources
- Search your GitHub repositories
- Read documentation from external sources
- Interact with APIs and services
- Browse web pages
- Run database queries

### How it works (simplified)

```
You (prompt) → Copilot → MCP Server → External Service
                                    ← Response
              Copilot ← MCP Server
You ← (answer with real data)
```

1. You ask Copilot a question that requires external data
2. Copilot recognizes it needs a tool and calls an **MCP server**
3. The MCP server connects to the external service (Azure, GitHub, a database, etc.)
4. The response flows back through the MCP server to Copilot
5. Copilot uses that data to give you a grounded, accurate answer

### Example: Without vs. With MCP

**Without MCP:**
```
You: "What resources are in my Azure resource group?"
Copilot: "I don't have access to your Azure account. You can use `az group list` to check."
```

**With MCP (Azure server enabled):**
```
You: "What resources are in my Azure resource group?"
Copilot: "Your resource group 'rg-production' contains: 1 App Service, 1 SQL Database, 
1 Key Vault, and 1 Storage Account. Here are the details..."
```

---

## What MCP Servers Exist?

MCP servers are available for many services. Here are the most relevant categories:

| Category | Examples | What they enable |
|----------|---------|-----------------|
| **Cloud** | Azure MCP | Query resources, costs, metrics, deployments |
| **Source Control** | GitHub MCP | Search code, list PRs, read issues, commit history |
| **Databases** | PostgreSQL, SQL Server | Query data, explore schemas, analyze tables |
| **Documentation** | Microsoft Learn, custom docs | Ground answers in your actual documentation |
| **Testing** | Playwright MCP | Browser automation, UI testing, web scraping |
| **Monitoring** | Application Insights | Query logs, metrics, traces |

> **Registry:** You can explore available MCP servers at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

---

## When Should Your Team Adopt MCP?

MCP is powerful but introduces new considerations. Use this decision framework:

### Good reasons to adopt MCP

- Developers frequently context-switch between Copilot and external tools (Azure portal, GitHub web, dashboards)
- You want Copilot to give answers grounded in **your** data, not generic knowledge
- You have well-defined, read-heavy workflows (querying resources, searching docs, exploring data)
- Your organization has approved the MCP servers you want to use

### Reasons to wait

- Your team is still learning basic Copilot workflows (do Labs 1-5 first)
- The MCP servers you need require security review or approval
- You primarily need write operations (MCP is strongest for read workflows today)
- The server you need doesn't exist yet or is in preview

### Decision matrix

```
Are you comfortable with Labs 1-5 patterns?
  No → Focus on custom instructions, agent mode, prompt files first
  Yes ↓

Does an MCP server exist for your use case?
  No → Wait for the ecosystem to mature, or build a custom server
  Yes ↓

Has your org approved MCP server usage?
  No → Start the approval conversation (share governance considerations below)
  Yes ↓

→ Pilot MCP with a small team, measure impact, then expand
```

---

## Governance Considerations

Before adopting MCP, your team and organization should address:

### Security

- **Authentication:** How does the MCP server authenticate to external services? (OAuth, API keys, CLI sessions)
- **Data exposure:** What data flows through the MCP server? Is any of it sensitive?
- **Least privilege:** Can you scope the MCP server to read-only access? Can you limit which resources it can access?
- **Audit trail:** Can you log what queries the MCP server executes?

### Organizational

- **Approval process:** Who approves MCP server installation? (IT security, platform team, individual developers?)
- **Allowed servers:** Should there be an approved list of MCP servers?
- **Configuration management:** How are MCP server settings managed across teams? (User settings, workspace settings, org-level policies?)
- **Cost:** Some MCP servers may incur API costs (e.g., querying Azure resources). Who pays?

### Technical

- **Network access:** Can the MCP server reach the required endpoints from developer machines?
- **Proxy/firewall:** Will corporate proxies block MCP server traffic?
- **Version management:** How are MCP server updates handled?
- **Reliability:** What happens when an MCP server is down? Does it block developer workflows?

---

## How MCP Connects to What You Learned Today

Everything from Labs 1-5 works **independently** of MCP. MCP is an **additive capability** — it makes Copilot smarter by giving it access to real data, but the core practices don't change:

| What you learned | Without MCP | With MCP |
|-----------------|-------------|----------|
| Custom instructions | Control code style and patterns | Same — plus you can add instructions about how to use MCP data |
| Agent mode | Multi-file generation, terminal commands | Same — plus agents can query external systems |
| Prompt files | Reusable workflows | Same — plus prompts can reference MCP tools for grounded answers |
| Quality guardrails | Review, test, verify | Same — MCP doesn't change your quality bar |

**The foundation you built today is the prerequisite for MCP.** Teams that adopt MCP without custom instructions and quality practices will just get bad code faster, but now with real data mixed in.

---

## What MCP Does NOT Do

Common misconceptions:

- **MCP does NOT replace your security model.** It uses your existing authentication (Azure CLI login, GitHub sign-in). It does not create backdoors.
- **MCP does NOT give Copilot autonomous access.** You still approve every action. Copilot proposes using a tool; you see what it will do and confirm.
- **MCP does NOT make Copilot infallible.** It can still misinterpret data, make wrong conclusions, or produce incorrect code. Your review discipline still matters.
- **MCP does NOT require code changes.** It extends Copilot's capabilities through configuration, not code.

---

## Next Steps for Your Team

If your team wants to explore MCP after this workshop:

### Immediate (this week)
1. Share the governance considerations with your IT security team
2. Identify 1-2 MCP servers that would save your team the most context-switching
3. Check if those servers are already approved or in your organization's evaluation pipeline

### Short-term (next month)
4. Run a small pilot with 2-3 developers using one MCP server (GitHub MCP is usually the easiest to approve)
5. Document what works and what doesn't
6. Create team guidelines for MCP usage

### Medium-term (next quarter)
7. Expand to additional MCP servers based on pilot results
8. Create custom instructions that reference MCP tools
9. Build prompt files that combine agent mode with MCP queries

---

## Discussion Points

1. **Which MCP server would give your team the biggest productivity boost?**
2. **What would the approval process look like** in your organization?
3. **What are the risks** of MCP in your specific context? How would you mitigate them?
4. **How would you measure** whether MCP actually improves productivity?
5. **What custom MCP servers** might you want to build for internal tools or data?

---

## Key Takeaways

- MCP is a **standard protocol** that lets Copilot use external tools and data
- It is an **additive capability** — everything you learned today works without it
- **Governance first** — don't install MCP servers before addressing security, authentication, and organizational approval
- **Start small** — pilot with one server, measure impact, then expand
- **The foundation matters more** — custom instructions, agent mode skills, and quality guardrails are the prerequisite for successful MCP adoption

---

## Resources

- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- [MCP Servers registry](https://github.com/modelcontextprotocol/servers)
- [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)

---

**Back to:** [Workshop README →](../README.md)
