# 🛡️ AEGIS: Autonomous AI Agent Cockpit

**Track:** Personal AI
**Tech Stack:** NVIDIA Nemotron (Nebius Token Factory), Python, FastAPI, SQLite, Tailwind CSS.

## Inspiration
The biggest problem with AI agents today is the "black box" — they can execute dangerous actions (like sending emails or deleting files) without permission. We built AEGIS to solve this: a personal AI with persistent memory and **human-in-the-loop security**.

## What it does
1. **Reasoning**: Uses NVIDIA Nemotron (via Nebius Token Factory) to understand user requests and plan actions.
2. **Persistent Memory**: Remembers user facts and preferences using SQLite.
3. **Security Guardrails**: Intercepts dangerous actions. The AI pauses and requires human approval via a futuristic Cockpit UI.

## 🚀 How we used Nebius & NVIDIA
This project is built entirely on the Nebius and NVIDIA ecosystem:
- **Nebius Token Factory**: We used the Token Factory API to serve the model. The fact that it's OpenAI-compatible significantly accelerated our workflow, allowing us to use standard Python SDKs without complex integration.
- **NVIDIA Nemotron**: We used the 
vidia/Nemotron-3-Ultra-550b-a55b model. Its advanced reasoning capabilities were crucial for accurately parsing user intents and correctly formatting the JSON arguments for the tools (e.g., extracting the email, subject, and body).
- **Other Nebius Tools**: The project is designed to be easily deployable on Nebius AI Cloud for production.

## 📝 Feedback on Nebius & NVIDIA
- **Nebius Token Factory**: The onboarding was incredibly fast. Having 1,000 free API units allowed us to prototype without worrying about costs. The inference speed of the Nemotron model was impressive.
- **NVIDIA Nemotron**: The model's ability to follow instructions and output structured JSON (for tool calling) was excellent. It understood complex multi-step requests and maintained context effectively.

## Architecture
- **Backend**: FastAPI (Python).
- **Security Layer**: A Python middleware (gent/security.py) that checks every 	ool_call against a whitelist/blacklist before execution. (This is enforced at the code level, not just via system prompts).
- **Frontend**: A dark-mode cockpit dashboard (HTML/JS/Tailwind).

## How to run
1. Clone the repo.
2. Add NEBIUS_API_KEY to .env.
3. pip install -r requirements.txt
4. python main.py
5. Open http://127.0.0.1:8000.

## Security Demo
When the user asks to send an email, the AI prepares the tool call, but the Python backend blocks it. The Cockpit UI intercepts this and opens a Security Modal for human approval.