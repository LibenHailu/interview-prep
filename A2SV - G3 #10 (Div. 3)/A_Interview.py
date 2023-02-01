l = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
or_a = or_b = 0
for i in a:
    or_a |= i

for j in b:
    or_b |= j

print(or_a + or_b)
