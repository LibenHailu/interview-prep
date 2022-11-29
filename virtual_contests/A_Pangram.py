l = int(input())
s = input()
if l < 26:
    print("NO")
else:
    set_len = len(set(s.lower())) 
    if set_len == 26:
        print("YES")
    else:
        print("NO")