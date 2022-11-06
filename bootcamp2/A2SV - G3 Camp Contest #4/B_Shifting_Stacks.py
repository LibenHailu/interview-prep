for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    sum_ = 0
    min_ = 0
    canShift = True
    for i in range(l):
        min_ += i
        sum_ += nums[i]
        if sum_ < min_:
            canShift = False
            
    if canShift:
        print("YES")
    else:
        print("NO")