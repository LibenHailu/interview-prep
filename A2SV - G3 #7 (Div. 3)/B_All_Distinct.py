from collections import Counter


for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    count = Counter(nums)
    tot = 0
    for _,val in enumerate(count.values()):
        # print(key,val)
        # if val != 1:
        tot += val
    tot -= len(count)
    print(l - 2 * (tot // 2 + tot % 2))