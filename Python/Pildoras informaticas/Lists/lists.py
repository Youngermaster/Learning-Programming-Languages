myList = ["Juan", "Cesar", "Pecho Frío", "Daniel"]

print(myList[2])  # Print the second position
print(myList[-3])  # Print from back
print(myList[0:3])  # Print from the position 0 to the position 3
print(myList)  # Print the full list

myList.append("Sara")  # Insert to the end of the list

print(myList[1:])  # It prints from 1 to the end

myList.insert(2, "Pedro")  # Insert in the position 2 of the list

print(myList)

myList.extend(["Name 1", "Name 2", "Name 3"])  # Add another list to the list

myList.append("Sara")  # Insert to the end of the list

print(myList.index("Sara"))  # Print a int -> the first occurrence of the String value

print("PEPES" in myList)  # Print a boolean

print("Cesar" in myList)  # Print a boolean

newList = ["Maria", 2, True, 12.0]  # We can add any element to the list

newList.append(13231.321)
newList.extend(["Name 1", "Name 2", "Name 3"])  # Add another list to the list

newList.pop()  # It removes the last element

print(newList)

newList += myList  # Add a list

print(newList)

exampleList = ["Proof", False, 132.23] * 3  # We triple the list

print(exampleList)
