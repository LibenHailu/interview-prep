
from collections import defaultdict
from email.policy import default
from selectors import BaseSelector
import sys
from typing import Counter


l = int(input())
s = input()
hash_set = Counter(s)
check = defaultdict(int)
left = right = 0
check[s[0]] = 1
left, right = 0,0
res = sys.maxsize
while left <= right and right < l:
    if check.keys() == hash_set.keys():
        res = min(res,right - left + 1)
        check[s[left]] -= 1
        if check[s[left]] == 0:
            del check[s[left]]
        left += 1
    else:
        right += 1
        if right <= l - 1:
            check[s[right]] += 1
print(res)
