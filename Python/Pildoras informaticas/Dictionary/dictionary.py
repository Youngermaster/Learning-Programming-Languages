countries = {"United Kingdom": "London", "Spain": "Madrid", "Italy": "Rome"}

countries["France"] = "Berlin"  # We can add on this way
countries["France"] = "Paris"  # We can modify on this way
countries["India"] = "Delhi"
del countries["India"]
print(countries)

# We can have a dictionary with different types of keys and values
newDictionary = {"Deuchtland": "Berlin", 17: "My age", "Jordan": 23}
print(newDictionary)

# We can create a dictionary with another contiguous structure
myTuple = ("Juan", 23, 12, 1990)
myDictionary = {myTuple[0]: "Name", myTuple[1]: "Age",
                myTuple[2]: "Month", myTuple[3]: "Year"}
print(myDictionary)

# We can have a sub dictionary tuple as a value
dictionaryWithTuple = {23: "Jordan", "Name": "Jordan", "Team": "Chicago",
                       "Rings": {"Seasons": (1991, 1992, 1993, 1996, 1997, 1998)}}

print(dictionaryWithTuple["Rings"])
print(dictionaryWithTuple.keys())
print(dictionaryWithTuple.values())
print(len(dictionaryWithTuple))
