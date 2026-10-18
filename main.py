from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent.brain import ask_nemotron
from agent.security import verifier_permission
import uvicorn
import json
import logging

# Configuration du logger pour suivre les erreurs en production
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SecureAgent")

app = FastAPI(title="AEGIS Secure Agent")

@app.get("/")
def read_root():
    return FileResponse("index.html")

class ChatRequest(BaseModel):
    message: str

# Définition des outils (Tools)
tools = [
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email.",
            "parameters": {
                "type": "object",
                "properties": {
                    "recipient": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["recipient", "subject", "body"]
            }
        }
    }
]

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        # 1. On verifie que le message n'est pas vide
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

        # 2. Appel au cerveau (Nemotron)
        logger.info(f"Received request: {request.message}")
        message = ask_nemotron(request.message, tools_definition=tools)

        # 3. Si l'IA décide d'appeler un outil
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            action_name = tool_call.function.name
            
            # 4. Validation du payload JSON (Si le modèle hallucine, on bÉPAKE)
            try:
                args = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError:
                logger.warning("Model returned invalid JSON.")
                return {
                    "ai_response": "Error: The AI provided malformed arguments. Please try again.",
                    "security": {"status": "error", "message": "Invalid JSON"}
                }

            # 5. ON VÉRÆIFIE LES PERMISSIONS (Garde-fou)
            permission = verifier_permission(action_name)
            
            return {
                "ai_response": f"Agent wants to execute: {action_name}",
                "arguments": json.dumps(args),
                "security": permission
            }
        
        # 6. Si réponse normale (sans action dangereuse)
        return {
            "ai_response": message.content,
            "security": {"status": "no_action", "message": "No action."}
        }

    except Exception as e:
        # 7. GLOBAL ERROR HANDLING (Si tout case, le serveur ne plante pas)
        logger.error(f"Server error: {str(e)}")
        if "isolate" in str(e).lower():
            return {
                "ai_response": "Network Error: Unable to reach the Nebius API. Please check your connection.",
                "security": {"status": "error", "message": "API Unreachable"}
            }
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    logger.info("Starting AEGIS on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)