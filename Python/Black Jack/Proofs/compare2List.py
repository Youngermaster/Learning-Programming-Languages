hand_1 = [("Juan", "1"), ("Manuel", "2"), ("Young", "3"), ("Hoyos", "4")]
hand_2 = [("Manuel", "2"), ("Juan", "1"), ("Hoyos","4"), ("Young", "2")]

"for i in len(hand_1):"
if hand_1 == hand_2:
    print ("Excelent")
else:
    print ("Nope")

print(True)

for i in range(5):
    print(i)

def compare_two_hands(hand_1, hand_2):
    if len(hand_1) == len(hand_2):
        comparator_counter = 0        
        for i in range(len(hand_2)):
            for j in range(len(hand_1)):
                if hand_1[i] == hand_2[j]:
                    comparator_counter += 1

        if comparator_counter == len(hand_1):
            return True
        else:
            return False
    else:
        return False
        
def compare_value_between_two_hands(hand_1, hand_2):
    if len(hand_1) == len(hand_2):
        comparator_counter = 0
        for i in range(len(hand_2)):
            for j in range(len(hand_1)):
                if hand_1[i][0] == hand_2[j][0]:
                    comparator_counter += 1

        if comparator_counter == len(hand_1):
            print("The hands have the same value.")
        else:
            print("The hands doesn't have the same value.")
    else:
        print("The hands doesn't have the same value.")
        
condition = compare_two_hands(hand_1, hand_2)
compare_value_between_two_hands(hand_1,hand_2)
print(condition)

arrray[5] = 0
arrray += 10
arrray += 15
arrray += 321

for i in range(3):
    print(arrray[i])