import bisect


a,b = map(int,input().split())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
nums1.sort()
res = []
for num in nums2:
    print(bisect.bisect(nums1,num),end=" ")
    # l,r = 0,len(nums1) - 1
    # best = 0
    # while l <= r and r < len(nums1):
    #     mid =  (l + r) // 2
    #     if nums1[mid] <= num:
    #         best = max(best,mid + 1)
    #         l = mid + 1
    #     # if nums1[mid] <= num:
    #     else:
    #         r = mid - 1
    # print(best,end=" ")
    # print(best)
# print(*res)/