def solution(nums):
    left = 0
    counter = 0
    while left < len(nums) - 1:
        if  nums[left] == 0:
            left += 1

        else:
            nums[left +1  + nums[left+1:].index(min(nums[left+1:]))] += 1
            nums[left] -= 1
            if nums[left] == 0:
                left += 1
            counter += 1
    print(counter)

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        nums = list(map(int, input().rstrip().split()))
        solution(nums)
            