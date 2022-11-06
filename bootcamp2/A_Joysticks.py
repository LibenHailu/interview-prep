from functools import lru_cache

a,b = map(int,input().split())

@lru_cache(None)
def recur(a,b):
    # if a <= 2 or b  <= 2:
    #     return 1
    if a <=  0 or b <= 0:
        return 0

    return max(1 + recur(a + 1,b - 2), 1 + recur(a - 2,b + 1))

if a == 1 and b == 1:
    print(0)
else:
    print(recur(a,b))