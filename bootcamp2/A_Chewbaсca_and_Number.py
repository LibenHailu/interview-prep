num = input()
res = []
for i in range(len(num)):
    if i == 0 and 9 - int(num[i]) == 0:
        res.append(num[i])
    else:
        val = int(num[i])
        res.append(num[i] if val < 9 - val else str(9-val))

print("".join(res))