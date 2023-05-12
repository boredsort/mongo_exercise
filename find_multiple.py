import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']


client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

documents_to_find = {"balance": {"$gt": 4700}}

cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()