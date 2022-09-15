from itertools import permutations
for _ in range(int(input())):
    length = int(input())
    name = input()
    if length != 5:
        print("NO")
    else:
        hashSet= ([''.join(p)  for p in permutations("Timur")])
        if name in hashSet:
            print("YES")
        else:
            print("NO")
