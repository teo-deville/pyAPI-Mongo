from fastapi import FastAPI
from pymongo import MongoClient
from starlette.responses import StreamingResponse

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

# http://127.0.0.1:8000/my-first-api?name=Teo

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hey! ' + str(author) + 'Your Claim# is ' + claimnumber

    else:
        text = 'Hey ' + name + '!'

    return text

# http://127.0.0.1:8000/get-iris

@app.get("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    return iris

# http://127.0.0.1:8000/plot-iris?
@app.get("/plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")