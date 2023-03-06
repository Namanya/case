
class PrimeGenerator:

    def __init__(self, stop):
        self.stop = stop

    def __next__(self):
        for x in range(2,self.stop):
            for y in range(2 , x):
                if x % y == 0:
                    break
            else:
             x = x + 1
             return x
        raise StopIteration()


g = PrimeGenerator(100)
print(next(g))
print(next(g))


def start_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'jose', 'Randy', 'Anna']

starts_with_r = filter(start_with_r, friends)
print(next(starts_with_r))
print(next(starts_with_r))

friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))
print(next(friends_lower))
print(next(friends_lower))
print(next(friends_lower))
