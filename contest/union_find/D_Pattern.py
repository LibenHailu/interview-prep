n = int(input())
p = []
for i in range(n):
    p.append(list(input()))

first = p[0]

for i in range(1,len(p)):
    for j in range(len(p[i])):
        if p[i][j] == '?' or first[j] == p[i][j]:
            continue
        elif first[j] == "?" and first[j] != p[i][j]:
            first[j] = p[i][j]
        else:
            first[j] = "."

for i in range(len(first)):
    if first[i] == ".":
        first[i] = "?"
    elif first[i] == "?":
        first[i] = "a"

print("".join(first))
