# iterate form back
# if not in set add it to set
# the first is set + 1 is the ans
for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    hash_set = set()
    ans = 0
    for i in range(length-1,-1,-1):
        if nums[i] not in hash_set:
            hash_set.add(nums[i])
        else:
            ans = max(ans, i+1)

    print(ans)