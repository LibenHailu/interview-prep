import sys


for _ in range(int(input())):
    n,l = map(int,input().split())
    words = []
    for i in range(n):
        words.append(input())
    res = sys.maxsize
    for i in range(n - 1):
        for j in range(i+1,n):
            count = 0
            for k in range(l):
                count += abs( ord(words[i][k]) - ord(words[j][k]) )
            res = min(count,res)
    print(res)