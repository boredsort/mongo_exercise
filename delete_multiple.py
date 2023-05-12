import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

documents_to_delete = {"balance": {"$lt": 2000}}

print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

result = accounts_collection.delete_many(documents_to_delete)

print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: ", str(result.deleted_count))

client.close()