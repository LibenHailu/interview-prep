for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    if min(nums) == nums[0]:
        print("Bob")
    else:
        print("Alice")