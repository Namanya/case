accounts = {
    'checking': 1958.00,
    'saving' : 3695.50
}


def add_balance(amount: float, name:str)-> float:
    accounts[name] += amount
    return accounts[name]

balance = add_balance(500.00, 'checking')


transactions =[
    (-180.67, 'checking'),
    ( -220.00, 'checking'),
    ( 220.00, 'saving'),
    ( -15.70, 'checking' ),
    (-23.90, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600, 'saving')
]
for t in transactions:
    add_balance(amount= t[0], name= t[1]) #unpacking add-balace(*t)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dicts(cls,data):
        return cls(data['username'], data['password'])

#imagine data is coming form the database
users = [{'username': 'rolf', 'password': '123'},
             {'username': 'daniel', 'password': 'dan'}
             ]
user_objects =[User(data['username'], data['password']) for data in users]

#or
#user_objects = [User(**data) for data in users] data unpacking
#example 2 assuming data is a tuple

#users = [('rolf', '123'),
#        ('daniel', 'dan')
#       ]
# user_objects = [users(*data) for data in users]"""
