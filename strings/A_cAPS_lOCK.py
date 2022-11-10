s = input()
s = list(s)
if s[0].isupper() and s[len(s) - 1].islower():
    print("".join(s))

if s[0].islower() and s[len(s) - 1].isupper():
    for i in range(len(s)):
        s[i] = s[i].swapcase()
    print("".join(s))

if s[0].islower() and s[len(s) - 1].islower():
    for i in range(len(s)):
        s[i] = s[i].swapcase()
    print("".join(s))