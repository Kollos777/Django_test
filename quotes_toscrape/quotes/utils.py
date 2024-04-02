from pymongo import MongoClient

def mydatabase():
    client = MongoClient('mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')
    db = client.mydatabase
    return db
