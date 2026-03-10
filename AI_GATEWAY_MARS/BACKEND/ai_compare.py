from mistralai import Mistral
import json
import re

# Initialise le client Mistral avec ta clé API
client = Mistral(api_key="5sMq70QQxP4ryuPzmUZPYMZxj16S5J3n")

def compare_contracts(contract_a: str, contract_b: str) -> dict:
    """
    Compare deux contrats et retourne un JSON avec les différences.
    """

    prompt = f"""
Tu es un expert juridique.
Compare les deux contrats suivants.
1. Identifie les différences importantes.
2. Explique les modifications.
3. Donne un niveau de risque (léger, moyen, haut).

Répond STRICTEMENT au format JSON suivant, sans aucun texte supplémentaire :

{{
 "differences":[
   {{
    "clause":"Nom de la clause",
    "before":"texte ancien",
    "after":"texte nouveau",
    "risk":"léger|moyen|haut",
    "comment":"explication"
   }}
 ]
}}

CONTRAT A:
{contract_a}

CONTRAT B:
{contract_b}
"""

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "system", "content": "Tu es un juriste expert en analyse de contrats."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    # Nettoyer le contenu pour éviter les sauts de ligne ou texte extra
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return {"differences": []}
    else:
        return {"differences": []}