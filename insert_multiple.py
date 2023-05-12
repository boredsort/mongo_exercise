import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)


db = client.bank


accounts_collection = db.accounts

new_accounts = [
    {
        "account_id": "mdb12345",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 69000,
    },
    {
        "account_id": "mdb134555",
        "account_holder": "Bruce Wayne",
        "account_type": "savings",
        "balance": 4505805690
    }
]

result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()