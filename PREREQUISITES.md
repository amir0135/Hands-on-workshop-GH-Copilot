# Welcome, Let's Get You Set Up 🎉

We're looking forward to spending the day building with you. So we can jump straight into the good stuff (agent mode, prompt files, MCP, and the hands-on exercises), please run through the short setup below **before the workshop**.

It shouldn't take long. If anything misbehaves, give your facilitator a shout ahead of time rather than on the morning. Much easier to sort out together when we're not against the clock.

See you soon. 🙌

## 1. VS Code (Latest Stable — 1.99 or newer, ideally 1.105+)

Download and install from [code.visualstudio.com](https://code.visualstudio.com/).

Verify:
```
code --version
```

> **Minimum required version: 1.99** (when chat modes were introduced).
> **Recommended: the latest stable release** (1.105 or newer at the time of writing). The chat UI evolves quickly — this workshop is written against the current VS Code mode picker which shows **Agent**, **Ask**, and **Plan**.
>
> If your corporate Software Center only offers an older build (for example 1.117 or earlier), please update **before** the workshop:
> - **macOS / personal install:** `Code → Check for Updates…` (or download the latest from the link above)
> - **Windows / managed install:** request the latest stable from your IT team, or install the User-scope build from [code.visualstudio.com](https://code.visualstudio.com/) into your profile if your policy allows it
>
> Older builds may be missing the **Plan** mode, MCP support, or current prompt-file/instructions behavior — and several lab exercises will not work as written.

> **Why VS Code?** This workshop uses VS Code as the common environment. The patterns you learn transfer to JetBrains and Visual Studio, but the exercises are built for VS Code.

## 2. GitHub Copilot Extensions

Install both extensions from the VS Code Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`):

- **GitHub Copilot**: inline completions
- **GitHub Copilot Chat**: chat, agent mode, prompt files

Verify: Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type `GitHub Copilot: Status`. You should see Copilot is active.

## 3. GitHub Copilot License

You need an active **GitHub Copilot Business** or **Enterprise** license. Verify by signing into GitHub in VS Code and checking that Copilot suggestions appear when you type code.

If you see "Copilot is not available" or a subscription prompt, contact your GitHub admin.

## 4. Enable Agent Mode

Agent mode is central to this workshop. On recent VS Code builds it is enabled by default. To confirm:

1. Open Settings (`Ctrl+,` / `Cmd+,`)
2. Search for `chat.agent.enabled`
3. Ensure it is **checked** (enabled)

Verify: Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) and click the mode picker at the bottom-left of the chat input. You should see **Agent**, **Ask**, and **Plan** as options (plus *Configure Custom Agents…*).

> **Heads-up about "Edit" mode.** Older versions of VS Code listed a separate **Edit** mode. In current builds, editing files is handled directly by **Agent** mode, and a new **Plan** mode has taken its slot in the picker. If a lab still says *"Edit mode"*, treat it as **Agent mode**. If your picker only shows *Ask / Edit / Agent*, your VS Code is out of date — please update (see step 1).

## 5. Enable Chat Participant Detection

This helps Copilot automatically route requests to the right tool.

1. Open Settings
2. Search for `chat.participantDetection.enabled`
3. Ensure it is **checked**

## 6. Git

Install Git from [git-scm.com](https://git-scm.com/) if not already installed.

Verify:
```
git --version
```

## 7. Your Programming Language Toolchain

Install the toolchain you use daily. The labs are language-agnostic, but you will write real code in your preferred language during exercises.

| Language | Install | Verify |
|----------|---------|--------|
| .NET | [dotnet.microsoft.com](https://dotnet.microsoft.com/download) | `dotnet --version` |
| Python | [python.org](https://www.python.org/downloads/) | `python --version` |
| Node.js/TypeScript | [nodejs.org](https://nodejs.org/) | `node --version` |
| Java | [adoptium.net](https://adoptium.net/) | `java --version` |

Install the corresponding VS Code extension for your language (C# Dev Kit, Python, etc.).

## 8. Clone This Repository

```bash
git clone https://github.com/hosseinzahed/github-copilot-hands-on-lab.git
cd github-copilot-hands-on-lab
```

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

## Pre-Workshop Checklist

Before you arrive, confirm:

- [ ] VS Code latest stable installed (run `code --version` — must be **1.99 or newer**, ideally 1.105+)
- [ ] GitHub Copilot and GitHub Copilot Chat extensions installed and active
- [ ] Copilot license verified (suggestions appear when coding)
- [ ] Agent mode enabled in settings
- [ ] Git installed
- [ ] Your language toolchain installed
- [ ] This repository cloned locally
- [ ] You can open Copilot Chat and switch between **Agent**, **Ask**, and **Plan** in the mode picker

## Troubleshooting

**Copilot not suggesting anything:**
- Check you are signed into GitHub in VS Code (bottom-left avatar)
- Verify your license at [github.com/settings/copilot](https://github.com/settings/copilot)
- Reload VS Code window (`Ctrl+Shift+P` → "Developer: Reload Window")

**Agent mode not showing, or only Ask / Edit / Agent appear (no Plan):**
- Update VS Code to the latest version (`Code → Check for Updates…`). Minimum 1.99, recommended 1.105+
- Update both Copilot extensions to latest (Extensions panel → check for updates)
- Check `chat.agent.enabled` is true in settings
- Reload the window (`Ctrl+Shift+P` → "Developer: Reload Window") after updating

**My Software Center only has VS Code 1.117 (or older):**
- That build pre-dates the current chat-mode picker and several features used in the labs. Either:
  1. Ask IT to push the latest stable, or
  2. Install the User-scope build from [code.visualstudio.com](https://code.visualstudio.com/) into your own profile (no admin rights needed on most policies).

**Extensions not installing:**
- Check your network/proxy settings allow access to the VS Code Marketplace
- Try installing from VSIX if marketplace is blocked (get VSIX from your facilitator)
