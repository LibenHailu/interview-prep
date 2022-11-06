def isUnique(s):
    check = 0

    for c in s:
        val = ord(c) - 97
        if check & (1 << val) != 0:
            return False
        check |= 1 << val
    
    return True

print(isUnique(input()))