from mistralai import Mistral
import json
import re

# Initialise le client Mistral avec ta clé API
from mistralai import Mistral
import json
import re

client = Mistral(api_key="5sMq70QQxP4ryuPzmUZPYMZxj16S5J3n")

def compare_contracts(contract_a: str, contract_b: str) -> dict:
    """
    Compare deux contrats et retourne un JSON avec les différences.
    """

    prompt = f"""
Tu es un expert juridique strict et rigoureux.
Compare les deux contrats suivants et identifie TOUTES les différences.

RÈGLES D'ÉVALUATION DU RISQUE — applique-les dans l'ordre :

1. "illégale" → si la clause est contraire à la loi, nulle de plein droit, abusive, disproportionnée, ou interdite par le Code civil / Code de commerce / droit du travail. Exemples : non-concurrence sans limite raisonnable, exclusion totale de responsabilité, pénalité manifestement excessive.

2. "haut" → si la clause crée un déséquilibre significatif entre les parties, un risque financier important, ou une restriction majeure des droits d'une partie.

3. "moyen" → si la clause modifie substantiellement les conditions initiales (délais, prix, durée) sans être abusive.

4. "léger" → uniquement si la modification est mineure et sans conséquence notable.

IMPORTANT : sois strict. En cas de doute entre deux niveaux, choisis le plus élevé.

Réponds STRICTEMENT au format JSON suivant, sans aucun texte avant ou après :

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

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "system", "content": "Tu es un juriste expert en analyse de contrats. Tu es strict, précis, et tu n'hésites pas à qualifier une clause d'illégale si elle l'est. Tu réponds uniquement en JSON valide, sans texte supplémentaire."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return {"differences": []}
    else:
        return {"differences": []}