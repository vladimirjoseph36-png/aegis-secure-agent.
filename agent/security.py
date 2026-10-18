# agent/security.py
# Ce module définit les règles de sécurité (Guardrails) pour l'agent IA.
# Il implémente le principe du "Human-in-the-loop" : l'IA ne peut pas exécuter
# d'actions dangereuses sans l'approbation explicite d'un humain.

# Liste des actions inoffensives que l'IA peut exécuter automatiquement
SAFE_ACTIONS = ["read_file", "search_memory", "get_weather"]

# Liste des actions critiques qui nécessitent une validation humaine
DANGEROUS_ACTIONS = ["send_email", "write_file", "delete_data"]

def verifier_permission(action_name: str) -> dict:
    """
    Vérifie si une action demandée par l'IA est autorisée, bloquée, ou en attente.
    
    Args:
        action_name (str): Le nom de l'outil que l'IA veut utiliser.
        
    Returns:
        dict: Un dictionnaire contenant le statut ('allowed', 'pending_approval', 'denied')
              et un message explicatif.
    """
    if action_name in SAFE_ACTIONS:
        return {
            "status": "allowed", 
            "message": f"Action '{action_name}' is allowed and executed."
        }
    elif action_name in DANGEROUS_ACTIONS:
        return {
            "status": "pending_approval", 
            "message": f"SECURITY: Agent wants to execute '{action_name}'. Human approval required."
        }
    else:
        # Par défaut, toute action inconnue est refusée (Principe de moindre privilège)
        return {
            "status": "denied", 
            "message": f"Action '{action_name}' is unknown. Denied by default."
        }