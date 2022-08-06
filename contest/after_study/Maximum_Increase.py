def solution(nums):
    res = 0
    cur = 1
    for i in range(1,len(nums)):
        if nums[i - 1]  < nums[i]:
            cur += 1
        else:
            res = max(res,cur)
            cur = 1

    res = max(res,cur)
    return res

if __name__ == '__main__':
    
    input()
    input1 = list(map(int, input().rstrip().split()))
    print(solution(input1))

