def recurr(l,r,arr):
    if r - l  == 1:
        return 0
    mid = (l + r + 1)// 2
    # print(arr,l,r,mid)
    # print(mid)
    maxl = max(arr[l:mid],default=0)
    maxr = max(arr[mid:r],default=0)
    ans = 0
    if maxl > maxr:
        for i in range(l,mid):
            # print(arr,mid,i,l,r)
            ans += 1
            arr[l + i],arr[mid + i] = arr[mid + i], arr[l + i]
            # print(arr)
    
    return ans + recurr(l,mid,arr) + recurr(mid,r,arr)

for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    print(recurr(0,l-1,nums))