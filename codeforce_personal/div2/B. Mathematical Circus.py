def ckt(n,k):
    hashSet  = set()
    res = []
    for i in range(2,n + 1,2):
        # hashSet.add((i,i-1))
        # hashSet.add((i-1,i))

        if ((i + k) * i - 1) % 4 == 0:
            res.append((i,i-1))
        if((i - 1 + k) * i ) % 4 == 0:
            res.append((i-1,i))
    
    
    # for t in hashSet:
    #     if ((t[0] + k) * t[1]) % 4 == 0:
    #         res.append(t)
    
    if not res:
        print("NO")
    
    else:
        print("YES")
        for t in res:
            print(*t)

q = int(input())
for _ in range(q):
    n,k = map(int, input().split())
    ckt(n,k)