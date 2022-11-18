for _ in range(int(input())):
    l = int(input())
    s = input()
    l = 0
    r = 0
    a = 0
    b = 0
    while r < len(s):
        if s[r] == "a":
            a += 1
        elif s[r] == "b":
            b += 1

        if r - l  + 1 == 2 and a == 1 and b == 1:
            print(l+1,r+1)
            break
        
        if r - l  + 1 == 2:
            if s[l] == "a":
                a -= 1
            else:
                b -= 1 
            l += 1
        r += 1
    
    if a != 1 or b != 1:
        print(-1,-1)