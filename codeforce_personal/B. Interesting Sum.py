def solution(nums):
    nums.sort()
    return (nums[len(nums)-1] - nums[0]) + (nums[len(nums)-2] - nums[1])

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(list(map(int,input().split()))))