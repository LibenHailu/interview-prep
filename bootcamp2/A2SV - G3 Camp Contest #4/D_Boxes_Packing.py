from typing import Counter


l = int(input())
nums = list(map(int, input().split()))
count = Counter(nums)
print(max(count.values()))