for _ in range(int(input())):
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    row1min,row1max = min(row1),max(row1)
    row2min,row2max = min(row2),max(row2)
    gridmin,gridmax = min(row1min,row2min),max(row1max,row2max)
    if (row1[0] == gridmin and row2[-1] == gridmax) or (row1[0] == gridmax and row2[-1] == gridmin) or (row1[-1] == gridmin and row2[0] == gridmax) or (row1[-1] == gridmax and row2[0] == gridmin):
        print("YES")
        continue
    else:
        print("NO")