for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    s1 = []
    s2 = []
    for num in nums:
        if num < 0:
            s2.append(num)
        else:
            s1.append(num)
    
    print(abs(sum(s1) - abs(sum(s2))))
