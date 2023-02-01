for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    a = sorted(nums[1:])
    ans = nums[0]
    for num in a:
        if num > ans:
            ans += (num - ans + 1) // 2

    print(ans) 