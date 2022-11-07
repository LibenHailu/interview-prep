s = input()
i = 0
dub = "WUB"
res = []
while i < len(s):

    if res and i+3 <= len(s) and s[i:i+3] == dub and res[-1] == " ":
        i += 3
        continue

    elif i+3 <= len(s) and s[i:i+3] == dub:
        i += 3
        res.append(" ")
    else:
        res.append(s[i])
        i += 1

print("".join(res))
