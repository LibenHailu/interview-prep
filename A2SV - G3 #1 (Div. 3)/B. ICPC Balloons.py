def  solution(solved):
    # iterate through solved problems
    # set res to  0
    # create hashSet
    # if c not in hasset add 2 to res and addit to hashset
    # if it is in hashset add 1
    res = 0
    hashSet = set()
    for c in solved:
        if c not in hashSet:
            res += 2
            hashSet.add(c)
        else:
            res += 1
    return res

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        input()
        print(solution(input()))

    