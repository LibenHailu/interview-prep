for  _ in range(int(input())):
    l,start = input().split()
    l = int(l)
    s = input()
    word = s + s
    ans = 0
    l = 0
    r = 0
    while r < len(word) and l < len(word):
        # print(word,l,r < len(word))
        if word[r] == "g" and word[l] == start:
            ans = max(ans,r - l )
            l = r + 1
        
        if l < len(word) and word[l] != start:
            l += 1
        
        r += 1
        
    print(ans)
