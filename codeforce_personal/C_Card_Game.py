from itertools import permutations
from traceback import print_tb


for _ in range(int(input())):
    length = int(input())
    nums = [i for i in range(1, length + 1)]
    mid = length//2
    # print(mid)
    per = list(permutations(nums,mid))
    # print(list(permutations(nums,mid)))
    visited = set()
    alice = 0
    bories = 0 
    for val in per:
        if val.sort() not in visited:
            s = set(val)
            if nums[-1] in s: 
                alice += 1
            if nums[0] in s and nums[-1] not in s:
                bories += 1
            visited.add(val.sort())

    
    print(f"{alice % 998244353 } {bories % 998244353 } 1")
