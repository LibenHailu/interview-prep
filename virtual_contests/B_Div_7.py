import math


for _ in range(int(input())):
    n = int(input())
    d = n % 7 
    last = n % 10
    if last != 0 and last - d <= 9 and last - d  > 0 and (n - d) % 7 == 0:
        n -= d
    elif last != 0 and last - d <= 9 and (n + (7 - d)) % 7 == 0:
        n += (7 - d)
    elif last + d <= 9 and (n + d) % 7 == 0:
        n += d
    elif last + d <= 9 and (n + (7-d)) % 7 == 0:
        n += (7 - d)
    print(n)