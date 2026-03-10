from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route qui affiche ton frontend
@app.get("/")
def read_index():
    return FileResponse("../FRONTEND/index.html")


@app.post("/compare")
async def compare(contract1: UploadFile = File(...), contract2: UploadFile = File(...)):

    text1 = (await contract1.read()).decode("utf-8")
    text2 = (await contract2.read()).decode("utf-8")

    # Pour l'instant on renvoie les textes reçus
    return {
        "contract1_text": text1,
        "contract2_text": text2,
        "differences": []
    }