from os import error
from model.User import User
from model.Transaction import Transaction
from model.OwnedStock import OwnedStock
from datetime import date, timedelta

db = {}
db['users'] = {'lenoxy': User({
    'username': 'lenoxy',
    'password_hash': 'password1234',
    'money_liquid': 3123.23
})}
db['transactions'] = []
db['owned_stocks'] = {}

# Users
def get_user(username: str) -> User:
    users = db['users']
    if username in users:
        return users[username]
    
    raise Exception('Could not find user')

def get_users() -> list[User]:
    return db['users'].values()

def update_user(user: User) -> User:
    users = db['users']
    if user.username in users:
        users[user.username].money_liquid = user.money_liquid
        return users[user.username]
    raise Exception('User could not be updated')

def create_user(user: User) -> User:
    users = db['users']
    if not user.username in users:
        users[user.username] = user
        return user
    raise Exception('User could not be created')

# Transactions
def get_transactions(username: str) -> list[Transaction]:
    if username in db['users']:
        since_date = date.today() - timedelta(days=5)
        print(since_date)
        return filter(lambda t: t.username == username and t.date >= since_date, db['transactions'])

    raise Exception('User does not exist')

def create_transacition(transaction: Transaction):
    db['transactions'].push(transaction)

# Owned Stocks
def get_owned_stocks(username: str) -> dict[OwnedStock]:
    if username in db['owned_stocks']:
        return db['owned_stocks'][username]

def update_owned_stocks(owned_stock: OwnedStock) -> list[OwnedStock]:
    if not owned_stock.username in db['owned_stocks']:
        db['owned_stocks'][owned_stock.username] = {}

    db['owned_stocks'][owned_stock.username][owned_stock.id].amount = owned_stock.amount