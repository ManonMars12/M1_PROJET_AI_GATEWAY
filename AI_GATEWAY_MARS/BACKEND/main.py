from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from extractor import extract_text
from ai_compare import compare_contracts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_index():
    return FileResponse("../FRONTEND/index.html")

@app.post("/compare")
async def compare(contract1: UploadFile = File(...), contract2: UploadFile = File(...)):

    # Extraction texte
    try:
        text1 = extract_text(contract1)
        text2 = extract_text(contract2)
    except Exception as e:
        return {"differences": [], "error": f"Impossible d'extraire le texte : {str(e)}"}

    # Appel Mistral
    result = compare_contracts(text1, text2)

    # ⚡ Assurer que le champ differences existe pour le frontend
    if "differences" not in result:
        result["differences"] = []

    return result