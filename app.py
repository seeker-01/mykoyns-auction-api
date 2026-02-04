from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/search/{coin}")
def search_coin(coin: str):
    return {"coin": coin, "results": []}
