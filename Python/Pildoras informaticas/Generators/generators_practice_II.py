 # With the '*' we indicates to Python that we gonna pass indefinite elements
def return_cities(*cities):
    for element in cities:
        yield from element

returned_cities = return_cities("Madrid", "Barcelona", "Moscú", "Santorini")

print(next(returned_cities))
print(next(returned_cities))
print(next(returned_cities))