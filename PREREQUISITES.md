# Prerequisites — Complete Before the Workshop

Complete **all** steps below before the workshop day. If you get stuck, reach out to your facilitator ahead of time — do not wait until the morning of the workshop.

---

## 1. VS Code (Latest Stable)

Download and install from [code.visualstudio.com](https://code.visualstudio.com/).

Verify:
```
code --version
```

> **Why VS Code?** This workshop uses VS Code as the common environment. The patterns you learn transfer to JetBrains and Visual Studio, but the exercises are built for VS Code.

---

## 2. GitHub Copilot Extensions

Install both extensions from the VS Code Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`):

- **GitHub Copilot** — inline completions
- **GitHub Copilot Chat** — chat, agent mode, prompt files

Verify: Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type `GitHub Copilot: Status`. You should see Copilot is active.

---

## 3. GitHub Copilot License

You need an active **GitHub Copilot Business** or **Enterprise** license. Verify by signing into GitHub in VS Code and checking that Copilot suggestions appear when you type code.

If you see "Copilot is not available" or a subscription prompt, contact your GitHub admin.

---

## 4. Enable Agent Mode

Agent mode is central to this workshop. Enable it in VS Code:

1. Open Settings (`Ctrl+,` / `Cmd+,`)
2. Search for `chat.agent.enabled`
3. Ensure it is **checked** (enabled)

Verify: Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) and check that the mode selector at the top shows **Agent** as an option alongside Ask and Edit.

---

## 5. Enable Chat Participant Detection

This helps Copilot automatically route requests to the right tool.

1. Open Settings
2. Search for `chat.participantDetection.enabled`
3. Ensure it is **checked**

---

## 6. Git

Install Git from [git-scm.com](https://git-scm.com/) if not already installed.

Verify:
```
git --version
```

---

## 7. Your Programming Language Toolchain

Install the toolchain you use daily. The labs are language-agnostic, but you will write real code in your preferred language during exercises.

| Language | Install | Verify |
|----------|---------|--------|
| .NET | [dotnet.microsoft.com](https://dotnet.microsoft.com/download) | `dotnet --version` |
| Python | [python.org](https://www.python.org/downloads/) | `python --version` |
| Node.js/TypeScript | [nodejs.org](https://nodejs.org/) | `node --version` |
| Java | [adoptium.net](https://adoptium.net/) | `java --version` |

Install the corresponding VS Code extension for your language (C# Dev Kit, Python, etc.).

---

## 8. Clone This Repository

```bash
git clone https://github.com/hosseinzahed/github-copilot-hands-on-lab.git
cd github-copilot-hands-on-lab
```

---

## 9. Recommended VS Code Settings

These settings optimize your Copilot experience for the workshop. Open Settings JSON (`Ctrl+Shift+P` → "Preferences: Open User Settings (JSON)") and add:

```jsonc
{
  // Copilot inline suggestions
  "editor.inlineSuggest.enabled": true,

  // Auto-save to reduce friction during agent mode
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,

  // Show Copilot completions alongside other suggestions
  "editor.suggest.showInlineCompletions": true
}
```

---

## Pre-Workshop Checklist

Before you arrive, confirm:

- [ ] VS Code latest stable installed
- [ ] GitHub Copilot and GitHub Copilot Chat extensions installed and active
- [ ] Copilot license verified (suggestions appear when coding)
- [ ] Agent mode enabled in settings
- [ ] Git installed
- [ ] Your language toolchain installed
- [ ] This repository cloned locally
- [ ] You can open Copilot Chat and switch between Ask, Edit, and Agent modes

---

## Troubleshooting

**Copilot not suggesting anything:**
- Check you are signed into GitHub in VS Code (bottom-left avatar)
- Verify your license at [github.com/settings/copilot](https://github.com/settings/copilot)
- Reload VS Code window (`Ctrl+Shift+P` → "Developer: Reload Window")

**Agent mode not showing:**
- Update VS Code to the latest version
- Update both Copilot extensions to latest
- Check `chat.agent.enabled` is true in settings

**Extensions not installing:**
- Check your network/proxy settings allow access to the VS Code Marketplace
- Try installing from VSIX if marketplace is blocked (get VSIX from your facilitator)
