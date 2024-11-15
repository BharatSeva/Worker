import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
MONGORURL = os.getenv("MONGODB_URL")

mongo_client = pymongo.MongoClient(MONGORURL)
def insert_mongodb(data, collection, db="db"):
    try:
        # Print logs in console
        print("DB:", db, "Collection:", collection, "category:", data)
        mongo_db = mongo_client[db]
        mongo_collection = mongo_db[collection]
        mongo_collection.insert_one(data)
        # mongo_collection.
    except Exception as e:
        print(f"MongoDB insert Error: {e}")


def update_mongodb(filter, data, collection, db="db"):
    try:
        print("DB: ", db, "Collection: ", collection, "category: ", data)
        mongo_db = mongo_client[db]
        mongo_collection = mongo_db[collection]
        mongo_collection.update_one(data)
    except Exception as e:
        print(f"MongoDB update Error {e}")