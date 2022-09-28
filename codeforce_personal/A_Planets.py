from typing import Counter


for _ in range(int(input())):
    length,sec = map(int, input().split())
    count = Counter(list(map(int, input().split())))
    res = 0
    for planet in count:
        res += min(count[planet],sec)
    print(res)