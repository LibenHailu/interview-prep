for i in range(int(input())):
    n = int(input())
    num = input()
    left,right = 0,n-1
    while left <= right:
        if num[left] == num[right]:
            break
        left += 1
        right -= 1
    
    print(right - left + 1)