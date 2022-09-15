r,c = map(int,input().split())
if r == 1 and c == 1:
    print(0)
if c == 1:
    print(1)
else:
    print((c-1)*r)