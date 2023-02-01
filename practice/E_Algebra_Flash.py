import sys


n,m = map(int,input().split())
nums = list(map(int,input().split()))
coins = list(map(int,input().split()))
nums = [sys.maxsize] + nums
for i in range(2,len(nums)):
    
