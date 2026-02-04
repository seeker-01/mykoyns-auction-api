from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API running"}

@app.get("/search/{coin}")
def search_coin(coin: str):
    # placeholder until DynamoDB is integrated
    return {"coin": coin, "results": []}
