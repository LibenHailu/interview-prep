l = int(input())
nums = list(map(int,input().split()))
# left = right = 0
res = 0
# while left < l and right < l:
#     if nums[right] >= nums[left]:
#         right += 1
#         res = max(res,(right - left) + 1)
#     else:
#         left = right

# print(res)
stack = []
for num in nums:
    if not stack:
        stack.append(num)
    else:
        if num >= stack[-1]:
            stack.append(num)
            res = max(res,len(stack))
        else:
            stack = []
            stack.append(num)
            res = max(res,len(stack))
print(max(res,len(stack)))
