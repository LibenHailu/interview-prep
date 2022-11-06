import math


for _ in range(int(input())):
    s = input()
    l = len(s)

    if l % 2 == 0:
        mid = math.ceil(l/2)
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")