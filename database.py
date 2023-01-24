from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://abrahamdefacto:abraham123@cluster0.esdcv2e.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
