def checkInclusion(self, s1: str, s2: str) -> bool:
    count =  [0] * 128

    for c in s1:
        val = ord(c) - 97
        count[val] += 1

    for c in s2:
        val = ord(c) - 97
        count[val] -= 1
        if count[val] < 0:
            return False
    
    return True
        