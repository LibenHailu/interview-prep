for _  in range(int(input())):
    s = int(input())
    l,r = 0, s*3 - 1
    count = 0
    res = []
    while l < r:
        count += 1
        res.append(l+1)
        res.append(r+1)
        l += 3
        r -= 3
    
    print(count)
    print(*res)