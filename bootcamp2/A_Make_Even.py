q = int(input())
for _ in range(q):
    num = input()
    if int(num[-1]) % 2 == 0:
        print(0)
    elif int(num[0]) % 2 == 0:
        print(1)
    else:
        has_even = False
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                has_even = True
                break
        
        if has_even:
            print(2)
        else:
            print(-1)
