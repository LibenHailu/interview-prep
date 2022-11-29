n,s = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if a[0] == 0:
    print("NO")
    exit()
else:
    for i in range(len(a)):
        if i + 1 == s and a[i] == 1:
            print("YES")
            exit()
        elif i+1 > s and a[i] == 1 and b[i] == 1:
            for j in range(i,-1,-1):
                if j + 1 == s and b[j] == 1:
                    print("YES")
                    exit()
            # print("NO")
            # exit()
print("NO")
exit()