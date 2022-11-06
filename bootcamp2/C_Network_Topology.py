from collections import Counter, defaultdict
from itertools import count

L,E = map(int,input().split())
hash_map = defaultdict(int)
for _ in range(E):
    s,e = map(int,input().split())
    hash_map[s] += 1
    hash_map[e] += 1
val = sorted(hash_map.values())
hash_set = set(val)
# c = Counter(val)
# print(hash_set)
if len(hash_set) == 1 and 2 in hash_set:
    print("ring topology")
elif len(hash_set) == 2 and 2 in hash_set and 1 in hash_set:
    print("bus topology")
elif len(hash_set) == 2 and 1 in hash_set and val[-2] == 1:
    # print(hash_set)
    print("star topology")
else:
    print("unknown topology")
