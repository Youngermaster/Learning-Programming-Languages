print("#" * 50)
print("Program of grade evaluation.\n")


def evaluation(grade):
    valoration = "Approved"
    if grade < 5:
        valoration = "Suspended"
    return valoration


student = input("Enter the grade of the student: ")
print(evaluation(12), "\n")

############################################

print("#" * 50)
print("DISCO.\n")

age = input("Enter your age: ")

if int(age) < 18:
    print("You can't pass")
elif int(age) > 100:
    print("Incorrect age.")
else:
    print("You can pass.")
