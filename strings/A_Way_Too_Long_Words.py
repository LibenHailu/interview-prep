for _ in range(int(input())):
    s = input()
    l = len(s)
    if l > 10:
        print("%s%d%s"%(s[0],l - 2,s[-1]))
    else:
        print(s)