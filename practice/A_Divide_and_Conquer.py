import math
import sys

def findMin(curr):
    it = 0
    while curr % 2 != 0:
        curr = curr // 2
        it += 1
    return  it

for _ in range(int(input())):
    l = int(input())
    nums  = list(map(int,input().split()))
    s = sum(nums)
    ans = sys.maxsize
    if s % 2 != 0:
        for num in nums:
            it = findMin(num)
            print(num,it)
            ans = min(it,ans) 
        print(ans)
    else:
        print(0)
    # for num in nums:
    #     if num % 2 == 0:
    #         count_even += 1
    #         even_min = min(num,even_min)
    #     else:
    #         cout_odd += 1
    #         odd_min = min(num,odd_min)
    
    # if cout_odd % 2 == 0:
    #     print(0)
    # else:
    #     print(int(min(math.log(odd_min + 1,2),math.log(even_min,2))))
