for _ in range(int(input())):
    n = int(input())
    down = True
    ans = 1
    i,j = 1,1
    # l = n - 2
    while i != n and j != n:
        if down:
            i += 1
            ans += (i * j)
            down = False
        else:
            j += 1
            ans += (i * j)
            down = True
    ans += n *n 
    ans *= 2022
    print(ans % 1000000007)