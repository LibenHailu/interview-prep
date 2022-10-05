
for _ in range(int(input())):
    row,col = map(int,input().split()) 
    if row == 1 or col == 1:
        print(f"{row} {col}")
    
    else:
        print(f"{row - 1} 2")
