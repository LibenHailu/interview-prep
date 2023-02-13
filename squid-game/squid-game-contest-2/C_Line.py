for _ in range(int(input())):
    k = int(input())
    curr_sum = 0 
    s = input()
    n = len(s) - 1
    ans = []
    for i,v in enumerate(s):
        if v == 'L':
            curr_sum += i 
            ans.append((n - i) - i)
        else:
            curr_sum += n - i 
            ans.append( i - (n -i))
    ans.sort(reverse=True)
    for num in ans:
        if num > 0:
            curr_sum += num
        print( curr_sum, end = " ")
    print()
    # ans = []
    # left,right = 0,k - 1
    # while k:
    #     cur_left = 0
    #     cur_right = 0
    #     if s[left] == 'L':
    #         cur_left = curr_sum - left - 0 + k - 1 - left 
    #     if s[right] == 'R':
    #         cur_right = curr_sum - k - 1 - right + right
    #     if cur_left > cur_right:
    #         curr_sum = cur_left
    #         left += 1
            
    #     elif cur_left < cur_right:
    #         curr_sum = cur_right
    #         # ans.append(cur)
    #         right -= 1
    #     k  -= 1
    #     # else:
    #     #     right -= 1
    #     #     left += 1
    #     ans.append(curr_sum)
    # print(ans)