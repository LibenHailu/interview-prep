# maintain bad indexies
for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    bad =  set()
    good = []
    for i in range(length-2,-1,-1):
        if nums[i] > nums[i + 1]:
            bad.add(nums[i])
            if nums[i] in good:
                while good[-1] != nums[i]:
                    bad.add(good.pop())
        else:
            good.append(nums[i])

    print(len(bad))
