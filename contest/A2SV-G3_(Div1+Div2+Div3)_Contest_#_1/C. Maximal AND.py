def soluton(k,nums):
    nums.sort()
    i = 0
    while i < k and i < len(nums):
        print(i,"hey",nums[i] | 2**nums[i])
        nums[i] = nums[i] | 2**nums[i]
        i += 1
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = ans&nums[i]
         
    return ans
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        _,k = map(int,input().split())
        nums = list(map(int, input().split()))
        print(soluton(k,nums))