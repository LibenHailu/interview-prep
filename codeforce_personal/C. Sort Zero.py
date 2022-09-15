from heapq import heapify, heappop


def solution(nums):
    if len(nums) == 1 or len(set(nums)) == 1:
        return 0
    
    i=j = len(nums) - 1
    
    while nums[i] == nums[j]:
        j -= 1
    
    hashset = set(nums[:j+1])
    return len(hashset)


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(list(map (int, input().split()))))
