n, d = map(int, input().split())
s = input()
res = 0
i = 0
if '0' * d in s:
    print(-1)
    exit()
while i < n - 1:
    if s[i] == '1':
        i += d
        res += 1
    else:
        i -= 1
print(res) 