def solution(word):
    days = 1
    hashSet = set()
    for c in word:
        if c in hashSet:
            continue
        elif c not in hashSet and len(hashSet) < 3:
            hashSet.add(c)
            continue

        else:
            hashSet.clear()
            hashSet.add(c)
            days += 1
    
    return days
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(solution(input()))