import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


from bson.objectid import ObjectId


load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

document_to_delete = {"_id": ObjectId("645e3c32baa38863516127f7")}

print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

result = accounts_collection.delete_one(document_to_delete)

print("Searching for the target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()