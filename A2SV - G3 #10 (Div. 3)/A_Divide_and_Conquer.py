import math
import sys


for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    even_min = sys.maxsize
    odd_min = sys.maxsize
    odd_count = 0
    for num in nums:
        if num % 2 != 0:
            odd_count += 1
            odd_min = min(odd_min,num)
        else:
            even_min = min(even_min,num)
    
    if odd_count % 2 != 0:
        print(min(math.log(even_min), math.log(odd_min + 1) // 2))
    else:
        print(0)
