from collections import Counter

k = int(input())
count = Counter(input())
res = []
for key in count:
    if count[key] % k == 0:
        res.append(key * (count[key] // k))
    else:
        print(-1)
        exit()
res = res*k
print("".join(res))
