for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    ans =  1
    for num in nums:
        ans *= num
    ans += n - 1
    print(ans * 2022)