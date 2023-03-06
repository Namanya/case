from collections import namedtuple, deque

account = ('checking', 1850.90)

Account = namedtuple('Account', ['name','balance'])

account = Account('checking', 1850.90)
print(account._asdict())

friends = deque(('rold', 'rolo'))
friends.append('jose')
print(friends)
friends.pop()
print(friends)






