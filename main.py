import pandas as pd
from fastapi import FastAPI, Request
from dbaccess import getclient
import os

# instantiate the API
app = FastAPI()


async def readCsv(csvFile):
    storedb = getclient[os.environ["db_name"]]
    storecollection = storedb["storeCollection"]
    df = pd.read_csv(csvFile, engine="pyarrow")
    await storecollection.insert_many(df.to_dict('records'))
     

@app.post("/events/csvs")
async def root(request: Request):
    event_data = await request.json()
    await readCsv(event_data);
   

