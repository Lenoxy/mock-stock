from os import error
from models import User, OwnedStock, Transaction
from datetime import date, timedelta
import mongodb

db = {}
db['users'] = {'lenoxy': User({
    'username': 'lenoxy',
    'password_hash': 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db',
    'money_liquid': 3123.23
})}
db['transactions'] = []
db['owned_stocks'] = {}

# Users
def get_user(username: str) -> User:
    filter = { "username": username }

    collection = mongodb.get_mongo_database().user
    user = collection.find_one(filter)
    if user:
        print(str(user))
        return User(user)
    raise Exception('Could not find user')

def get_users() -> list[User]:
    collection = mongodb.get_mongo_database().user
    cursor = collection.find({})
    users = []
    for user in cursor:
        users.append(User(user))
        print(user['username'])

    return users

def update_money_liquid(user: User) -> User:
    filter = { "username": user.username }
    collection = mongodb.get_mongo_database().user

    if user:
        collection.update_one(filter, { "$set": { 'money_liquid': user.money_liquid } })
        return collection.find_one(filter)
    raise Exception('User could not be updated')

def create_user(user: User) -> User:
    collection = mongodb.get_mongo_database().user
    collection.insert_one({"username": user.username, "password_hash": user.password_hash, "money_liquid": user.money_liquid})
    return user

# Transactions
def get_transactions(username: str) -> list[Transaction]:
    if username in db['users']:
        since_date = date.today() - timedelta(days=5)
        print(since_date)
        return filter(lambda t: t.username == username and t.date >= since_date, db['transactions'])

    raise Exception('User does not exist')

def create_transaction(transaction: Transaction) -> Transaction:
    db['transactions'].push(transaction)
    return transaction

# Owned Stocks
def get_owned_stocks(username: str) -> dict[OwnedStock]:
    if not username in db['owned_stocks']:
        db['owned_stocks'][username] = {}

    return db['owned_stocks'][username]

def update_owned_stocks(owned_stock: OwnedStock) -> list[OwnedStock]:
    if not owned_stock.id in db['owned_stocks'][owned_stock.username]:
        db['owned_stocks'][owned_stock.username][owned_stock.id] = OwnedStock(
            {'id': owned_stock.id, 'username': owned_stock.username, 'amount': 0})

    if db['owned_stocks'][owned_stock.username][owned_stock.id].amount + owned_stock.amount < 0:
        raise Exception("You goin' below zero dude, can't do that")
    db['owned_stocks'][owned_stock.username][owned_stock.id].amount += owned_stock.amount

    return db['owned_stocks'][owned_stock.username]