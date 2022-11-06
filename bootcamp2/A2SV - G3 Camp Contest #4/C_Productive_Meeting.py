import heapq


for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    res = []
    heap = []
    for i in range(l):
        if nums[i] == 0:
            continue
        heapq.heappush(heap,(-nums[i], i + 1))
    
    while len(heap) > 1:
        s1,a1 = heapq.heappop(heap)
        s2,a2 = heapq.heappop(heap)
        res.append((a1,a2))
        s1 += 1
        s2 += 1
        if s1 != 0:
            heapq.heappush(heap,(s1,a1))
        
        if s2 != 0:
            heapq.heappush(heap,(s2,a2))
        
    print(len(res))
    for ans in res:
        print(*ans)

