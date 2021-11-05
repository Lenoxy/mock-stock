import csv
from datetime import date, timedelta

import mongodb
from models import User, OwnedStock, Transaction

collection = mongodb.mongo_client.user
if not collection.find_one({"username": 'lenoxy'}):
    collection.insert_one({
        'username': 'lenoxy',
        'password_hash': 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db',
        'money_liquid': 6969.69
    })


# Users
def get_user(username: str) -> User:
    filter = {"username": username}

    collection = mongodb.mongo_client.user
    user = collection.find_one(filter)
    if user:
        return User(user)
    raise Exception('Could not find user')


def get_users() -> list[User]:
    return mongodb.find(mongodb.mongo_client.user)


def update_money_liquid(user: User) -> User:
    filter = {"username": user.username}
    user_collection = mongodb.mongo_client.user

    if user:
        user_collection.update_one(filter, {"$set": {'money_liquid': user.money_liquid}})
        return user_collection.find_one(filter)
    raise Exception('User could not be updated')


def create_user(user: User) -> User:
    filter = {"username": user.username}

    collection = mongodb.mongo_client.user
    if collection.find_one(filter):
        raise Exception('User already exists')

    user_collection = mongodb.mongo_client.user
    user_collection.insert_one(
        {"username": user.username, "password_hash": user.password_hash, "money_liquid": user.money_liquid})
    return user


# Transactions
def get_transactions(user: User) -> list[Transaction]:
    since_date = date.today() - timedelta(days=5)

    transaction_collection = mongodb.mongo_client.transaction
    transactions = mongodb.find(transaction_collection)
    print(transactions[0].username)

    return filter(lambda t: t.username == user.username and t.date >= since_date, transactions)


def create_transaction(transaction: Transaction) -> Transaction:
    transaction_collection = mongodb.mongo_client.transaction
    transaction_collection.insert_one(transaction.to_dict())
    return transaction


# Owned Stocks
def get_owned_stocks(username: str) -> dict[OwnedStock]:
    owned_stock_collection = mongodb.mongo_client.owned_stock
    owned_stocks = mongodb.find(owned_stock_collection, {'username': username})
    result = {}
    for owned_stock in owned_stocks:
        result[owned_stock.id] = owned_stock
    return result


def update_owned_stock(owned_stock: OwnedStock) -> OwnedStock:
    filter = {'username': owned_stock.username, 'id': owned_stock.id}
    owned_stock_collection = mongodb.mongo_client.owned_stock
    existing_stock = owned_stock_collection.find_one(filter)

    # If stock isn't in DB yet
    if not existing_stock:
        if owned_stock.amount < 0:
            raise Exception("You goin' below zero dude, can't do that")
        owned_stock_collection.insert_one(owned_stock.to_dict())
        return owned_stock

    existing_stock = OwnedStock(existing_stock)
    # If update would give negative number
    if existing_stock.amount + owned_stock.amount < 0:
        raise Exception("You goin' below zero dude, can't do that")

    if existing_stock.amount + owned_stock.amount == 0:
        owned_stock_collection.remove(filter)

    # add to existing stock
    owned_stock_collection.update_one(filter, {"$set": {'amount': existing_stock.amount + owned_stock.amount}})
    return existing_stock


# Stock IDs
def get_stock_ids() -> list[str]:
    with open('src/resources/stock_ids.csv', newline='') as tickers:
        reader = csv.reader(tickers)
        for s in list(reader):
            yield s[0]
