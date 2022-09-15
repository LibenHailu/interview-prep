# what is the behaviour of el1 and el2
# calculate the d/c
from operator import le


for _ in range(int(input())):
    level = list(map(int,input().split()))
    # if level[0] == level[2]:
    #     print(level[0])
    if abs(level[0] - level[2]) == abs((level[1]+1) - level[2]):
        print(3)
    elif abs(level[0] - level[2]) < abs((level[1]+1) - level[2]):
        print(level[0])
    else:
        print(level[1])