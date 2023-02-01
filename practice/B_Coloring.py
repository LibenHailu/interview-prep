for _ in range(int(input())):
    n,m,k = map(int,input().split())
    nums = list(map(int,input().split()))
    if m * k < n:
        print("NO")
        continue
    
    count = 0
    for num in nums:
        if num == k:
            count += 1

    if count < dn/k:
        print("NO")
    else:
        print("YES")