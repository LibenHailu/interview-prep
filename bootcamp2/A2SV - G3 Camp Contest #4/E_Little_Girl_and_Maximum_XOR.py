l,r = map(int,input().split())
res = 0

start,end = l,r
while start < end:
    res = max(res, start ^ end)
    start += 1
    
start,end = l,r
while start < end:
    res = max(res, start ^ end)
    end -= 1

start,end = l,r
while start <= end:
    res = max(res, start ^ end)
    end -= 1
    start += 1

print(res)