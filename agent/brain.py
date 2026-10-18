import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

def ask_nemotron(user_prompt: str, tools_definition: list = None):
    """
    Envoie une requete au modele NVIDIA Nemotron via Nebius.
    """
    messages = [
        {"role": "system", "content": "Tu es un assistant personnel expert. Utilise les outils a ta disposition si necessaire."},
        {"role": "user", "content": user_prompt}
    ]
    
    response = client.chat.completions.create(
        model="nvidia/Nemotron-3-Ultra-550b-a55b",
        messages=messages,
        tools=tools_definition,
        tool_choice="auto" if tools_definition else None,
        temperature=0.1
    )
    return response.choices[0].message

if __name__ == "__main__":
    print("Test de connexion au cerveau Nemotron...")
    result = ask_nemotron("Dis 'Bonjour' en un seul mot.")
    print(f"Reponse de l'IA : {result.content}")