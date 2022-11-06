for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    stack = []
    for i in range(length):
        # if not stack:
        #     stack.append(nums[i])
        # else:
        if stack and abs(stack[-1] - nums[i]) <= 1:
            stack.pop()
            stack.append(nums[i])
        else:
            stack.append(nums[i])

    if len(stack) == 1:
        print("YES")
    else:
        print("NO")            
