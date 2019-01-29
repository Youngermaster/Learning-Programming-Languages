arrayx = [1, 4, 34, 1, 4]
poker = 0
nelson = 0
for i in range(5):
    for j in range(5):
        if i == j:
            nelson += 1
        else:
            if arrayx[i] == arrayx[j]:
                poker += 1

print(poker)           

