from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    node = os.environ.get("NODE_NAME", "Entorno Local")
    return {
        "sistema": "POS Cafetería Independiente",
        "servidor": node,
        "menu_clasicos": ["Espresso", "Flat White", "Latte con Caramelo Salado"]
    }