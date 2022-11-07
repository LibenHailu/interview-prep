s = input().lower()
vowels = ["a","e","i","o","u","y"]
res = []
for c in s:
    if c not in vowels:
        res.append("."+c)

print("".join(res))