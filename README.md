# 🛡️ AEGIS: Autonomous AI Agent Cockpit

**Track:** Personal AI
**Tech Stack:** NVIDIA Nemotron (Nebius Token Factory), Python, FastAPI, SQLite, Tailwind CSS.

## Inspiration
The biggest problem with AI agents today is the "black box" — they can execute dangerous actions (like sending emails or deleting files) without permission. We built AEGIS to solve this: a personal AI with persistent memory and **human-in-the-loop security**.

## What it does
1. **Reasoning**: Uses NVIDIA Nemotron (via Nebius Token Factory) to understand user requests and plan actions.
2. **Persistent Memory**: Remembers user facts and preferences using SQLite.
3. **Security Guardrails**: Intercepts dangerous actions. The AI pauses and requires human approval via a futuristic Cockpit UI.

## Architecture
- **Backend**: FastAPI (Python).
- **AI Model**: 
vidia/Nemotron-3-Ultra-550b-a55b on Nebius Token Factory.
- **Security Layer**: A Python middleware (gent/security.py) that checks every 	ool_call against a whitelist/blacklist before execution.
- **Frontend**: A dark-mode cockpit dashboard (HTML/JS/Tailwind).

## How to run
1. Clone the repo.
2. Add NEBIUS_API_KEY to .env.
3. pip install -r requirements.txt
4. python main.py
5. Open http://127.0.0.1:8000.

## Security Demo
When the user asks to send an email, the AI prepares the tool call, but the Python backend blocks it. The Cockpit UI intercepts this and opens a Security Modal for human approval.