from math import comb


from itertools import combinations
def solution(nums):
    combs = list(combinations(nums,3))
    # hashSet = set(nums)

    for comb in combs:
        curRes = list(comb)
        curRes.append(comb[0]+comb[1])
        curRes.append(comb[0]+comb[2])
        curRes.append(comb[1]+comb[2])
        curRes.append(comb[0]+comb[1]+comb[2])
        curRes.sort()

        if curRes == nums:
            return comb

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        nums = list(map(int, input().rstrip().split()))
        result = solution(nums)
        print(*result)
