import csv
from models import User, OwnedStock, Transaction
import mongodb
from finance import isNaN


# Users
def get_user(username: str) -> User:
    filter = {"username": username}
 
    collection = mongodb.mongo_client.user
    user = collection.find_one(filter)
    if not user:
        return None
    return User(user)


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
def get_transactions(username: str) -> list[Transaction]:

    transaction_collection = mongodb.mongo_client.transaction
    transactions = mongodb.find(transaction_collection)

    return filter(lambda t: t.username == username and not isNaN(t.stock_price), transactions)


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
        return existing_stock

    # add to existing stock
    owned_stock_collection.update_one(filter, {"$set": {'amount': existing_stock.amount + owned_stock.amount}})
    return existing_stock


# Stock IDs
def get_stock_ids() -> dict[str]:
    with open('src/resources/stock_ids.csv', newline='') as tickers:
        stocks = {}
        reader = csv.reader(tickers)
        for s in list(reader):
            stocks[s[0]] = s[1]
        return stocks

if __name__ == '__main__':
    pass
