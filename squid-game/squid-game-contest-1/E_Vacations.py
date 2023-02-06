n = int(input())
nums = list(map(int,input().split()))
# prev = None
# total = 0
# for num in nums:
#     if nums == 0:
#         continue
#     elif num == 1 and not prev or num == 1 and prev == 'gym':
#         total += 1
#         prev = 'contest'
#     elif num == 2 and not prev or num == 1 and prev == 'gym':


def dp(index, prev):
    print(index,prev)
    # print(index,prev)
    if index >= len(nums):
        return 0
    
    elif nums[index] == 0:
        return 0 + dp(index + 1 ,prev)
    
    elif nums[index] == 1 and (not prev or prev == 'gym'):
        return 1 + dp(index + 1, 'contest')
    
    elif nums[index] == 2 and not prev or prev == 'contest':
    
        return 1 + dp(index + 1, 'gym')

    elif nums[index] == 3 and prev == 'gym':
        
        return 1 + dp(index + 1, 'contest')
    elif nums[index] == 3 and prev =='contest':
        print(prev)
        return 1 + dp(index + 1,'gym')

    elif nums[index] == 3 and not prev :
        return max(1 + dp(index + 1, 'gym'), 1 + dp(index + 1 , 'contest'))
    else:
        return 0 + dp(index + 1,prev)

print(n - (dp(0,'') )  )