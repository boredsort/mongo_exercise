import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts


new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "12342345",
    "account_type": "checking",
    "balance": 594000,
    "last_updated": datetime.datetime.utcnow()
}

result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f'_id of the inserted document is {document_id}')

client.close()