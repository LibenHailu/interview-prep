for _  in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    isSteep = False
    i = 0
    ans = "YES"
    while i <= n-2: 
        if nums[i] < nums[i+1]:
            isSteep = True
        elif nums[i] > nums[i + 1] and isSteep:
            ans = "NO"
        i += 1
    print(ans)

