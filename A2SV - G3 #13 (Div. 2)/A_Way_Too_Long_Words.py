for _ in range(int(input())):
    s = input()
    if len(s)  < 11:
        print(s)
    else:
        l = len(s) - 2
        print(f'{s[0]}{l}{s[len(s) - 1]}')