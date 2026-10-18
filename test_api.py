import requests
import json

url = "http://127.0.0.1:8000/chat"
payload = {"message": "Send an email to boss@company.com with subject Test and body Hello"}
headers = {"Content-Type": "application/json"}

print("\nEnvoi de la requete a l'API...\n")
response = requests.post(url, json=payload, headers=headers)

# Affichage de la reponse formatee
print(json.dumps(response.json(), indent=4, ensure_ascii=False))