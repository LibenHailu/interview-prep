for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    print("YNeos"[nums[0]!=1::2])