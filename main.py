from fastapi import FastAPI
from pymongo import MongoClient

# Connect to my Mongo cluster and create a client
client = MongoClient("mongodb+srv://teo_deville:2IJW0bXiZexSSL75@cluster0-csv2v.mongodb.net/test")


db = client.get_database('Insurance')

records = db.Claims
i= records.count_documents({})
print (i)

myquery = { "Author": "Kai Devilleres" }

mydoc = records.find(myquery)
for x in mydoc:
  print(x)

author = x['Author']
claimnumber = x['Claim']['ClaimNumber']

print (author)
print (claimnumber)

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hey! ' + str(author)

    else:
        text = 'Hey ' + name + '!' + i

    return text
