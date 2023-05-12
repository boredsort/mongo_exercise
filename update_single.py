import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

document_to_update = {"_id": ObjectId("645dfe33e80b82ee85458618")}

add_to_balance = {"$inc": {"balance": 100}}

# Print the Original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Update the document
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()