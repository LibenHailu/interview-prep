from cmath import cos


l = int(input())
s = input()
cost = list(map(int,input().split()))
res = []
ans = 0

for i in range(l):
    if s[i] == "h" and len(res) <= 1:
        if not res:
            res.append(cost[i])
        else:
            res[0] += cost[i]
    elif s[i] == "a" and len(res) <= 2:
        if len(res) == 1:
            res.append(cost[i])
        else:
            res[1] += cost[i]
    
    elif s[i] == "r" and len(res) <= 3:
        if len(res) == 2:
            res.append(cost[i])
        else:
            res[2] += cost[i]
    
    elif s[i] == "d" and len(res) <= 4:
        if len(res) == 3:
            res.append(cost[i])
        else:
            res[3] += cost[i]
    elif s[i] == "h" and len(res) == 4:
        ans += min(res)
        res = []
        # if not res:
        res.append(cost[i])
        # else:
        #     res[0] += cost[i]
        # print(res)
if len(res) == 4:
    print(ans +  min(res))
else:
    print(ans)