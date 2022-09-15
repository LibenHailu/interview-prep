def soution(k,nums):
    hashSet= set([i for i in range(k+1)])
    res = 0
    for num in nums:
        if hashSet.issubset(set(num)):
            res += 1
    
    return res

if __name__ == "__main__":
    n,k = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append([int(i) for i in input()])
    
    print(soution(k,nums))
