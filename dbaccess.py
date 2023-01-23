from pymongo import MongoClient
import os

async def getclient() -> MongoClient:
    db_url = os.environ["db_url"]
    db=os.environ["db_name"]

    client = pymongo.MongoClient(db_url)
    return client
    