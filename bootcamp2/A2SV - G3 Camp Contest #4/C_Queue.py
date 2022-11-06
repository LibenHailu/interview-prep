
l = int(input())
res = [0] * l
start = 0
end = 0
count = 0
se = {}
es = {}
for _ in range(l):
    s,e = map(int,input().split())
    if s == 0:
        res[1] = e
        start = 1
        se[s] = e
        es[e] = s
        count += 1
    elif e == 0:
        res[l - 2] = s
        end = l - 2
        se[s] = e
        es[e] = s
        count+=1
    else:
        se[s] = e
        es[e] = s


while  count < l:
# print("here",es,end)
    if res[start] in se and start + 2 < l:
        res[start + 2] = se[res[start]]
        start += 2
        count += 1
    if res[end] in es and end - 2 <= 0:
        res[end - 2] = es[res[end]]
        end -= 2
        count += 1

print(*res)