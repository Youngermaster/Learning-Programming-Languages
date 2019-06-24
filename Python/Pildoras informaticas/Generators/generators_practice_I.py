        # Classic way.
def classic_even_generator(limit):
    number = 1
    evenList = []
    while number < limit:
        evenList.append(number * 2)
        number += 1
    return evenList

print(classic_even_generator(9))

# Generator way.
def even_generator(limit):
    number = 1
    evenList = []
    while number < limit:
        yield number * 2
        number += 1

getEvens = even_generator(9)

print(next(getEvens))
print(next(getEvens))
print(next(getEvens))