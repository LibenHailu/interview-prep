for _ in range(int(input())):
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    p = list(map(int,input().split()))
    z = list(sorted(zip(p,h)))
    i = 0
    m = max(h)
    dmg = k
    while i < len(p) and k != 0:
        if z[i][1] > dmg:
            k = max(0,k - z[i][0])
            dmg += k 
        else:
            i += 1
    
    if dmg < m:
        print("NO")
    else:
        print("YES")
