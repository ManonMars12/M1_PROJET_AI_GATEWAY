import httpx
import json
import re
import os
from dotenv import load_dotenv

# Charge le .env
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


MISTRAL_API_KEY = "5sMq70QQxP4ryuPzmUZPYMZxj16S5J3n"

def compare_contracts(contract_a: str, contract_b: str):
    response = httpx.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "system",
                    "content": "Tu es un juriste expert en analyse de contrats. Tu es strict, précis, et tu n'hésites pas à qualifier une clause d'illégale si elle l'est. Tu réponds uniquement en JSON valide, sans texte supplémentaire."
                },
                {
                    "role": "user",
                    "content": f"""
Tu es un expert juridique strict et rigoureux.
Compare les deux contrats suivants et identifie TOUTES les différences.

RÈGLES D'ÉVALUATION DU RISQUE :
1. "illégale" → clause contraire à la loi, nulle de plein droit, abusive
2. "haut" → déséquilibre significatif, risque financier important
3. "moyen" → modification substantielle des conditions initiales
4. "léger" → modification mineure sans conséquence notable

Réponds STRICTEMENT au format JSON :
{{
  "differences": [
    {{
      "clause": "Nom de la clause",
      "before": "texte ancien",
      "after": "texte nouveau",
      "risk": "léger|moyen|haut|illégale",
      "comment": "explication juridique précise"
    }}
  ]
}}

CONTRAT A :
{contract_a}

CONTRAT B :
{contract_b}
"""
                }
            ]
        },
        timeout=60
    )
    
    content = response.json()["choices"][0]["message"]["content"]
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return {"differences": []}
    return {"differences": []}
