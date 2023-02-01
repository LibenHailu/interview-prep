for _ in range(int(input())):
    input()
    x = set()
    y = set()
    for _ in range(3):
        a,b = map(int,input().split())
        x.add(a)
        y.add(b)
    # print(x,y)
    print('YES' if len(x) == 3 or len(y) == 3 else 'NO')