l = int(input())
p = list(map(int,input().split()))
pi_sum = 0
for pi in p:
    pi_sum += pi / 100
ans = format((pi_sum/l) * 100,'.12f')
# print((pi_sum/l) * 100)
print(ans)