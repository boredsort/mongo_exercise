import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGONDB_URI = os.environ["MONGODB_URI"]


client = MongoClient(MONGONDB_URI)

db = client.bank

accounts_collection = db.accounts

# filter
select_accounts = {"account_type": "checking"}

# update
set_field = {"$set": {'minimum_balance': 100}}

result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts)) 

client.close()



