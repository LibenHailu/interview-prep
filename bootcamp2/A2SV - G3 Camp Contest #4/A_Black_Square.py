nums = list(map(int,input().split()))
strip = input()
res = 0
for c in strip:
    res += nums[int(c) - 1]

print(res)