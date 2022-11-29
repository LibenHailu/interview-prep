for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    temp = []
    zeros = []
    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            temp.append(num)
    temp.extend(zeros)
    nums = temp
    # print(nums,temp,zeros)
    hash_set = {}
    ans = 0
    for num in nums:
        if num == 0:
            ans += 1
            if hash_set:
                hash_set.pop()
            continue
        elif -num in hash_set:
            ans += 1
            hash_set.remove(-num)
            continue
        else:
            hash_set.add(num)
    if len(hash_set) == 0:
        print(ans)
    else:
        print(0)