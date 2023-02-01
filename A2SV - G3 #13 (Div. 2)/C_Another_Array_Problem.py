for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    diff = abs(nums[0] - nums[1])
    cur_sum = diff * 2
    if n == 2:
        print(max(sum(nums),cur_sum))
        continue
    for i in range(2,n):
        diff = abs(nums[i] - diff)
        cur_sum = diff * ( i + 1)
    
    print(max(cur_sum,sum(nums)))
