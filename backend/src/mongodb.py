from pymongo.database import Database

def get_mongo_database() -> Database:
    CONNECTION_STRING = "mongodb://root:9876512345@localhost:27017"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client.mockstock


if __name__ == "__main__":
    dbname = get_mongo_database()
    print('Connected to DB:', dbname.name)