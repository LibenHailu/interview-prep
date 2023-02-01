for _ in range(int(input())):
    l = int(input())
    s = input()
    res = 1
    hash_set = set()
    for i in range(1,l):
        if s[i:i+2] in hash_set:
            continue
        res += 1
        hash_set.add(s[i-1:i+1])
    print("NO" if res == l else "YES")