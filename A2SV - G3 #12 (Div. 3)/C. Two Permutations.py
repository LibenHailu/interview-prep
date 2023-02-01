for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if n == a and a == b:
        print("Yes")
        continue
    nums = [i for i in range(1,n+1)]
    if len(nums[a:-b]) < 2:
        print("No")
    else:
        print("Yes") 