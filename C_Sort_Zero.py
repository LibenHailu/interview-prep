
for _ in[0]*int(input()):
    n=int(input())
    a=[*map(int,input().split())]
    b=set()
    k=0
    for i in range(1,n):
        if a[i]<a[i-1] or a[i] in b:
            for j in a[k:i]:
                b.add(j)
            k=i
    print(len(b))
