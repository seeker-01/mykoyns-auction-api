from fastapi import FastAPI
import boto3
from boto3.dynamodb.conditions import Key

app = FastAPI()

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('mykoyns-auction-prices')

@app.get("/")
def home():
    return {"status": "API running"}

@app.get("/search/{coin}")
def search_coin(coin):

    response = table.query(
        KeyConditionExpression=Key('coin_name').eq(coin)
    )

    return response.get('Items', [])