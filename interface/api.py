
from fastapi import FastAPI
from generation.myth_generator import MythGenerator

app = FastAPI()

@app.get("/generate")
def generate_myth(pantheon_size: int = 5):
    mg = MythGenerator()
    myth = mg.generate_full_myth(pantheon_size=pantheon_size)
    return myth
