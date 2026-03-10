from openai import OpenAI
import json

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def compare_contracts(contract_a, contract_b):

    prompt = f"""
Tu es un expert juridique.

Compare les deux contrats suivants.

1. Identifie les différences importantes.
2. Explique les modifications.
3. Donne un niveau de risque (low, medium, high).

Retourne UNIQUEMENT un JSON sous cette forme :

{{
 "differences":[
   {{
    "clause":"Nom de la clause",
    "before":"texte ancien",
    "after":"texte nouveau",
    "risk":"low|medium|high",
    "comment":"explication"
   }}
 ]
}}

CONTRAT A:
{contract_a}

CONTRAT B:
{contract_b}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"system","content":"Tu es un juriste expert en analyse de contrats."},
            {"role":"user","content":prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    return json.loads(content)