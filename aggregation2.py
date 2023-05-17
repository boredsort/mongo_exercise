import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

# Just an example rate, to convert usd to gdp
conversion_rate_usd_to_gdp = 1.3

select_accounts = {"$match": {"account_type": "checking", "balance": {"$gt": 1500}}}

# Organize documents in order from highest balance to lowest.
# -1 means descending order
organize_by_original_balance = {"$sort": {"balance": -1}}


# Return only the acount type & balance fields, plus a new field containing blaance in Great British Pounds(GBP).
# set 1 to include, set 0 to exclude
return_specified_fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gdp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gdp]},
        "_id": 0,
    }
}


# Pipeline is setting the order of process of the document, match should be the first process to identify and filter only the documents necessary
pipeline = [
    select_accounts,
    organize_by_original_balance,
    return_specified_fields
]

results = accounts_collection.aggregate(pipeline)

print(
    "Account type, origingal balance and balance in GDP of checking accounts with original balance greater than $1,500,"
    "in order from highest original balance to lowest: ", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()