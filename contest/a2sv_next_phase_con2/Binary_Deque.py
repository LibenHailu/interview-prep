import sys
 
 
def solution(l1,l2):
    if l1[1] == sum(l2):
        return 0
    def minStep(n,curSum,total,step):
        if curSum ==  total:
            return step
        if not n:
            return sys.maxsize
        return min(minStep(n[1:],curSum- n[0],total,step+1),minStep(n[:len(n)-1],curSum-n[len(n)-1],total,step+1))
    steps = minStep(l2,sum(l2),l1[1],0)
    return  steps if steps != sys.maxsize else -1
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        l1 = list(map(int, input().rstrip().split()))
        l2 = list(map(int, input().rstrip().split()))
        print(solution(l1,l2))
 