def soltion(n,m):
    if (n+m)%2==0:
        print("Tonya")
    else:
        print("Burenka")

q = int(input())
for _ in range(q):
    n,m = map(int,input().split())
    soltion(n,m)