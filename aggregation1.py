import os 
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

# select accounts with balance of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

# separate the doucments by account type and calcuate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# create an aggregation pipeline on list, the order is very important to lessen the processed documents
# match stage if important the be early in the pipeline to lessen the documents being processed later in the pipeline
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance
]

results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings account with balances of less than $1000", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()