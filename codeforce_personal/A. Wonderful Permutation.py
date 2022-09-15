def solution(k,nums):
    res = 0 
    for i in range(1,k+1):
        if nums.index(i) > k - 1:
            res += 1
    return res

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        _,k = map(int,input().split())
        nums = list(map (int, input().split()))
        print(solution(k,nums))
