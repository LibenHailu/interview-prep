# first implement prefix sum
# do binary search on prefix sum

def solution(nums, target):
    # print(nums,target)
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    if nums[left] >= target:
        print(left+1)
    else:
        print(-1)
    # print(nums[left])

if __name__ == "__main__":
    q1 = int(input())
 
    for i in range(q1):
        q2 = list(map(int, input().split()))
        q3 = sorted(list(map(int, input().split())),reverse=True)
        
        prefix = []
        for ind,num in enumerate(q3):
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(num + prefix[-1])

        for i in range(q2[1]):
            solution(prefix, int(input()))