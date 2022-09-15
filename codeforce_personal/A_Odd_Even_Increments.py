# accept the input
# hold the len
# take your odd and even
# start form the second index 
# have a variable
for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))
    even = nums[0] % 2
    odd = nums[1] % 2
    samePariry = True
    for i in range(2,length):
        if i % 2 == 0:
            if nums[i] % 2 != even:
                samePariry = False
        else:
            if nums[i] % 2 != odd:
                samePariry = False
    
    if samePariry:
        print("YES")
    else:
        print("NO")