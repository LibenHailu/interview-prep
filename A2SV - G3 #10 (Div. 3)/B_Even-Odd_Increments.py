tc = int(input())
for _ in range(tc):
    n,q = map(int,input().split())
    nums = list(map(int,input().split()))
    cur_sum = sum(nums)
    count = {0:0,1:0}
    for num in nums:
        if num % 2 == 0:
            count[0] += 1
        else:
            count[1] += 1
    
    for _ in range(q):
        i,x = map(int,input().split())
        if x % 2 == 0:
            cur_sum += count[i] * x
        else:
            cur_sum += count[i] * x
            count[1 - i] += count[i]
            count[i] = 0
        print(cur_sum)

