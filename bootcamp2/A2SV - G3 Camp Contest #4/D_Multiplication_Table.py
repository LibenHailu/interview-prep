r,c,k = map(int,input().split())

def isEnough(x):
    count = 0
    for i in range(1,r+1):
        count += min(x//i,c)
    
    return count >= k

left,right = 0, r * c
while left < right:
    mid = (left + right) // 2

    if isEnough(mid):
        right = mid
    else:
        left = mid + 1

print(left)

