# accept nums
# calculate lcm and gcd
from itertools import permutations


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a * b) // gcd(a,b)    
for _ in range(int(input())):

    num = int(input())
    res = 0
    for i in range(1,num+1):
        for j in range(i,num+1):
            if lcm(i,j)/gcd(i,j) <= 3:
                res += 1
    print(res)
    