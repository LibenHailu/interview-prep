for _ in range(int(input())):
    l = int(input())
    s = input()
    hasOne = s[0] == '1'
    ans = []
    for c in range(1,len(s)):
        if s[c] == '0':
            ans.append('+')
        elif s[c] == '1' and hasOne:
            ans.append('-')
            hasOne = False
        else:
            ans.append('+')
            hasOne = True
    
    print(''.join(ans))
        