for i in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    first = second = 0
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    res = []
    for num in nums:
        if num != first:
            res.append(num - first)
        else:
            res.append(num - second)
    print(*res)
        