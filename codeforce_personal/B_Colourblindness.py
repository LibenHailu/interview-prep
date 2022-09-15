# for each input 
# create 2 row list
# iterate throught both and change b to g
# check equlaity
for _ in range(int(input())):
    length = int(input())
    row1 = list(input())
    row2 = list(input())
    for i in range(len(row1)):
        if row1[i] == 'B':
            row1[i] = 'G'
    for i in range(len(row2)):
        if row2[i] == 'B':
            row2[i] = 'G'
    
    if row1 == row2:
        print("YES")
    else:
        print("NO")