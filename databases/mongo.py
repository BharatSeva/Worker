import pymongo
mongo_client = pymongo.MongoClient('mongodb://rootuser:rootuser@localhost:27017')


def insert_mongodb(data, collection, db="db"):
    try:

        # Print logs in console
        print("DB:", db, "Collection:", collection, "category:", data)


        mongo_db = mongo_client[db]
        mongo_collection = mongo_db[collection]
        mongo_collection.insert_one(data)
    except Exception as e:
        print(f"MongoDB insert Error: {e}")

# def insert_hip_logs(data, collection):
#     try:
#         mongo_db = mongo_client['hip_logs']
#         mongo_collection = mongo_db[collection]
#         mongo_collection.insert_one(data)
#     except Exception as e:
#         print(f"MongoDB Error: {e}")


# mongo_client.close()


