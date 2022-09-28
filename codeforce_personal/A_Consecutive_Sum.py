# have 2 max heap for even and odd
# from collections import defaultdict
# import heapq
for _ in range(int(input())):
    l,k = map(int, input().split())
    nums  = list(map(int,input().split()))
    ans = [0]*k

    for i in range(l):
        ans[i % k] = max(ans[i  % k], nums[i])
    print(sum(ans))    
    