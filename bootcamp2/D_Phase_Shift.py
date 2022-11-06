for _ in range(int(input())):
    l = int(input())
    hash_map = {}
    s = input()
    res = []
    cur = ord('b') if s[0] == 'a' else ord('a')
    for c in s:
        # if ord(c) == 'a':
        #     ord += 1
        # ingoing[ord(c)- ord('a')] = cur
        while chr(cur) in hash_map:
            cur += 1
            print(cur)
        # if not c in hash_map:
        hash_map[chr(cur)] = c
        hash_map[c] = chr(cur)
        res.append(chr(cur))
        # else:
        # res.append(hash_map[c])
    print(res)
        # cur += 1
    # for i in ingoing:
    #     if i:
    #         res.append(chr)
    # print(ingoing
    # )
        
        
