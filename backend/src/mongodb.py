from pymongo.mongo_client import MongoClient

def get_new_db_connection() -> MongoClient:
    CONNECTION_STRING = "mongodb://root:9876512345@localhost:27017"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client


if __name__ == "__main__":
    dbname = get_new_db_connection()
    print('Connected to DB:', dbname.name)