from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from transformer import transformar_pedidos

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/pedidos")
def get_pedidos():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return transformar_pedidos(data)
    except Exception as e:
        return {"error": str(e)}
