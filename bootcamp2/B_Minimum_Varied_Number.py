from random import randrange


for _ in range(int(input())):
    n = int(input())
    ans = []
    cand = [9,8,7,6,5,4,3,2,1]

    for i in cand:
        if n - i < 0:
            continue
        n -= i
        ans.append(str(i))
    
    ans.reverse()
    print("".join(ans))
