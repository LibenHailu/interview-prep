# # sort the numbers
# # iterate check all edge cases
# length = int(input())
# nums = list(map(int,input().split()))
# if length == 1:
#     print(abs(nums[0]) - 1)
# else:
#     ans = 0
#     for i in range(length):
#         if i == 0:
#             if nums[i + 1] > 0 and nums[i] < 0:
#                 ans += abs(nums[i]) + 1
#                 nums[i] = 1
#             elif nums[i + 1] < 0 and nums[i] < 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = -1
#             elif nums[i + 1] == 0 and nums[i] < 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = -1
#             else:
#                 ans += abs(nums[i]) + 1
#                 nums[i] = 1
#         else: 
#             if nums[i - 1] > 0 and nums[i] < 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = 1
#             if nums[i - 1] < 0 and nums[i] > 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = 1
#             # if nums[i - 1] > 0 and nums[i] == 0:
#                 ans += 1
#                 nums[i] = 1
#             if nums[i - 1] < 0 and nums[i] < 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = 1
#             if nums[i - 1] > 0 and nums[i] > 0:
#                 ans += abs(nums[i]) - 1
#                 nums[i] = 1
# print(ans)

length = int(input())
ans = 0
isOdd = None
nums = list(map(int,input().split()))
nums.sort()
for i in range(length):
    if nums[i] < 0 and i % 2 != 0: 
        isOdd = False  
    if nums[i] < 0 and i % 2 == 0: 
        isOdd = True
    if nums[i] < 0:
        ans += abs(nums[i]) - 1
    elif nums[i] == 0 and isOdd:
        ans += 1
        isOdd = False
    elif nums[i] == 0 and not isOdd:
        ans += 1
    else:
        ans += abs(nums[i]) - 1
if isOdd:
    ans += 2
print(ans)