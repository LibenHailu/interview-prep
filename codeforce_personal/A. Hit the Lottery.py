# chekc max element 
# always deduce max element
num = int(input())
res = 0
coins = [1, 5, 10, 20, 100]
curr = num
while curr:
    if curr < coins[-1]:
        coins.pop()
    else:
        res += (curr // coins[-1] )
        curr -= (curr // coins[-1] ) * coins[-1]
        
print(res)
# def mc(idx):
#     if idx >= len(cost):
#         return 0
    
#     return min(min(idx + 1) ,min(idx + 2))+cost(i)

# return  min(mc(0),mc(1))

# cost[index] += min(dp[i + 1],dp[i+2])

from itertools import permutations
tc = int(input())

for _ in range(tc):
    perm = list(permutations(range(1,int(input()) + 1)))
    print(len(perm))
    for p in perm:
        print(*p)
