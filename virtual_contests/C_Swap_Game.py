for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    min_ = min(nums)
    if nums[0] == min_:
        print("Bob")
    else:
        print("Alice")


