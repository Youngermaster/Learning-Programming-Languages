myTuple = ("Juan", 23, 12, 1930, 12)
myNewList = list(myTuple)  # Convert a tuple in a list

anotherList = ["Juan", 232, 1212, 1930]
anotherTuple = tuple(anotherList)  # Convert a list in a tuple

print(myTuple, "And its lenght is: ", len(myTuple))  # Prints my tuple and its length
print("Juan" in myTuple)  # Prints a bool if the element is or not
print(myTuple.count(12))  # Prints how many times is the parameter
print(myTuple.index("Juan"))  # Print a int -> the first occurrence of the String value

# Unitary tuple
unitaryTuple = ("Juan",)  # Whit the comma.
print(unitaryTuple)

# Empaneled de tuple
empaquetedTuple = "Juan", 13, 432, 132
print(empaquetedTuple)

# unpaqueted de tuple
name, age, month, year, day = myTuple
print("Name: {} Age: {} Month: {} Year: {} Day: {}" \
      .format(name, age, month, year, day))
