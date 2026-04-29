# Lab 0: Getting Aligned

**Duration:** ~30 minutes
**Goal:** Make sure everyone is set up, on the same page, and has a shared baseline before we start the hands-on labs.

---

## Part 1: Verify Your Setup (10 min)

Before anything else, confirm your environment is ready. Work through this checklist and flag your facilitator if anything fails.

### Checklist

- [ ] **VS Code** is open and running the latest stable version
  - Check: `Help → About` or `code --version` in terminal
- [ ] **GitHub Copilot** extension is installed and showing the Copilot icon in the bottom status bar
- [ ] **GitHub Copilot Chat** extension is installed
- [ ] **You are signed into GitHub** in VS Code (bottom-left profile icon)
- [ ] **Copilot is active** — open any code file and start typing. You should see ghost-text suggestions
- [ ] **Agent mode is available** — open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) and check the mode dropdown at the top. You should see **Ask**, **Edit**, and **Agent**
- [ ] **Your language toolchain** is installed — run the relevant version command in terminal:

```bash
dotnet --version    # .NET developers
python --version    # Python developers
node --version      # Node.js/TypeScript developers
java --version      # Java developers
```

- [ ] **This repository is cloned** and open in VS Code

### If something is missing

Don't wait — raise your hand now. Refer to [PREREQUISITES.md](../PREREQUISITES.md) for installation steps. Facilitators can help troubleshoot.

---

## Part 2: Know Your Copilot Modes (10 min)

This workshop focuses heavily on **agent mode**, but you should understand all three modes and when to use each. Try each one now.

### Mode 1: Ask

Open Copilot Chat and make sure the mode is set to **Ask**.

Try:
```
What is the difference between async and await?
```

**Ask** is for questions — explaining code, answering technical questions, learning. It does NOT change files.

### Mode 2: Edit

Switch to **Edit** mode.

1. Create a file `playground/hello.py` (or `.cs`, `.ts`, `.java` — your language) with a simple function:

```python
def greet(name):
    return "Hello, " + name
```

2. Select the function, then in Copilot Chat (Edit mode) type:

```
Add type hints and handle the case where name is empty
```

**Edit** modifies specific code you point it to. It works on the files and selections you reference.

### Mode 3: Agent

Switch to **Agent** mode.

Type:
```
Create a playground/calculator file with add, subtract, multiply, and divide functions. 
Include error handling for division by zero. Use [your language].
```

**Agent** plans and executes autonomously — it creates files, writes code, and can run terminal commands. This is the primary mode for this workshop.

> **Review the diff before accepting.** Agent mode will show you proposed changes. Get in the habit of reading them carefully — this is the single most important skill you will practice today.

---

## Part 3: How We Will Work Today (5 min)

Read through these ground rules so the workshop runs smoothly.

### The playground folder

All exercises use a `playground/` folder inside this repository. Create it now if it doesn't exist:

```bash
mkdir -p playground
```

This keeps your experiments organized and separate from the lab instructions.

### Your language, your choice

Unless a lab specifies otherwise, use **the programming language you use at work**. The patterns are the same regardless of language. Pick one and stick with it for the day.

### Review everything

Every time Copilot proposes a change, **read the diff**. Ask yourself:
- Does this code do what I asked?
- Would I approve this in a code review?
- Does it follow our team's standards?

If the answer is no — tell Copilot what to fix. That iteration loop is the core skill.

### Ask for help

If you are stuck for more than 5 minutes, ask your facilitator. The goal is learning the patterns, not debugging environment issues.

### Think about your real work

Throughout the day, keep asking: *How would I use this on my actual project?* The most valuable output of this workshop is the custom instructions and prompt files you create for your team — not the playground code.

---

## Part 4: Quick Warm-up (5 min)

One final exercise to make sure Copilot is working end-to-end before we start the real labs.

### In Agent mode, try this:

```
In the playground folder, create a simple "FizzBuzz" implementation in [your language]. 
Then create a test file with at least 5 test cases covering normal numbers, 
multiples of 3, multiples of 5, and multiples of 15. Run the tests.
```

If this works — Copilot creates the files, writes the tests, and runs them — you are ready for the workshop.

If it doesn't, troubleshoot now:
- **Copilot doesn't create files?** → Ensure you're in Agent mode, not Ask
- **Terminal commands fail?** → Check your language toolchain is installed
- **Tests don't run?** → Make sure your test framework is available (pytest, xunit, jest, etc.)

---

## You're Ready

Once your warm-up exercise is complete:

1. Keep the `playground/` folder — you will use it for every lab
2. Delete or keep the FizzBuzz files — they were just a setup check
3. Move on to **[Lab 1: Team Configuration →](01-team-configuration.md)**

---

**Next:** [Lab 1: Team Configuration →](01-team-configuration.md)
