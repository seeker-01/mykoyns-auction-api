from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/search/{coin}")
def search_coin(coin):
    # placeholder for DynamoDB query
    return {"coin": coin, "price": 0}
