for _ in range(int(input())):
    k,n = map(int,input().split())
    ans = []
    step = 0
    for _ in range(k):
        if not ans:
            ans.append(1)
            step += 1
        elif (n - (ans[-1] + step)) >= k - (step + 1):
            ans.append(ans[-1] + step) 
            step += 1
        else:
            ans.append(ans[-1] + 1)
            step += 1
    print(*ans)
        