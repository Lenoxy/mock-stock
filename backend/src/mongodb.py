from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import os

from models import User, Transaction, OwnedStock


CONNECTION_STRING = os.environ.get('DB_CONNECTION', 'mongodb://root:9876512345@localhost:27017')
mongo_client: Database = MongoClient(CONNECTION_STRING).mockstock

def find(collection: Collection, filter = None):
    cursor = collection.find(filter if filter else {})
    entities = []
    for entity in cursor:
        entities.append(instantiate_entity(entity, collection.name))
    return entities


def instantiate_entity(entity_dict, table_name):
    if table_name == "user":
        return User(entity_dict)
    elif table_name == "transaction":
        return Transaction(entity_dict)
    elif table_name == "owned_stock":
        return OwnedStock(entity_dict)
    else:
        raise NotImplementedError("Entity for table does not exist or is not referenced in mongodb.py")
