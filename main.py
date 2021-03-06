import uvicorn
from fastapi import FastAPI

import requests
import os
from dotenv import load_dotenv


from app.choose_stock import GetChampionStock
import app.Utils
import pathlib

from routers import items

#load_dotenv()
#BASE_ID = os.environ.get("BASE_ID")
#TABLE_NAME = os.environ.get("TABLE_NAME")
#API_KEY = os.environ.get("API_KEY")
#
#url = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'
#
## Headers
#headers = {
#    "Authorization": f"Bearer {API_KEY}",
#    "Content-Type": "application/json"
#}
#
#response = requests.get(url, headers=headers)
#airtable_response = response.json()
#
#print(response.json())
#print(airtable_response)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


app.include_router(items.router)



@app.get("/GetStockInfo/{op}")
def GetStockInfo(op):
   results = GetChampionStock(op)
   return {"message": results}

'''
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
'''
