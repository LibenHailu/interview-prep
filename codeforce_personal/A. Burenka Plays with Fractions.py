def solutoin(fractions):
    x = fractions[0] * fractions[3]
    y = fractions[1] * fractions[2]
    if x == y:
        return 0
    elif x != 0 and y % x == 0 or y != 0 and x % y == 0:
        return 1
    else:
        return 2
if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(solutoin(list(map(int,input().split()))))
