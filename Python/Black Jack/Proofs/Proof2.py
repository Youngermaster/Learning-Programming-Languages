poker = 0

value_array = [1, 2, 5, 1, True]
var = 0
for y in range(5):
    if ~y == 0:
        if value_array[0] == value_array[y]:
            poker += 1
    if ~y == 1:        
        if value_array[1] == value_array[y]:
            poker += 1
    if ~y == 2:        
        if value_array[2] == value_array[y]:
            poker += 1
    if ~y == 3:        
        if value_array[3] == value_array[y]:
            poker += 1
    if ~y == 4:        
        if value_array[4] == value_array[y]:
            poker += 1        

if value_array[4] == value_array[3]:
    print("GG")

if poker == 2:
    print("2 es un par")
    #return 2
elif poker == 3:
    print("3 es un trio")
    #return 3
elif poker == 4:
    print("4 es un poker")
    #return 4
elif poker == 5:
    print("5 es un full")
    #return 5
else:
    print(poker)
    #return 0