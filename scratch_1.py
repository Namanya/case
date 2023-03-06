import random


def capital_index(caps):
    i = []
    for x, y in enumerate(caps):
        if y.isupper():
            i.append(x)
    print(i)


capital_index("Hi TheRe")


def online_count():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",

    }
    x = []
    y = 0
    for name, value in enumerate(statuses):
        if statuses[value] == 'online':
            x.append(value)
            y = len(x)
    print(x)
    print(y)


online_count()


def random_number():
    number = random.randint(0, 101)
    print(number)


def only_ints(a, b):
    if type(a) == int and type(b) == int:
        print(True)
    else:
        print(False)


only_ints(True, 6)