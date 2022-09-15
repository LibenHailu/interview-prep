from collections import deque

def solution(nums):
    # add them in a queue
    # first check len queue with the len of its set 
    # len(set) == len(queue) ans 0
    # popleft form que add your steps and do the checks

    queue = deque(nums)
    hashSet = set(nums)

    if len(queue) == len(hashSet):
        return 0

    res = 0
    while queue:
        queue.popleft()
        res += 1
        if len(queue) == len(set(queue)):
            return res
    
    return res

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(list(map(int,input().split()))))