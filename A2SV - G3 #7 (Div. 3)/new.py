from collections import Counter


week1 = list(map(int,input().split()))
week2 = list(map(int,input().split()))
count1 = Counter(week1)
count2 = Counter(week2)

res = []
for key in count1:
    if key in count2:
        res += [key] * min(count1[key],count2[key])
    
print(res)
# week1.sort()
# week2.sort()
# p1 = 0
# p2 = 0
# ans = []
# while p1 < len(week1) and p2 < len(week2):
#     if week1[p1] == week2[p2]:
#         ans.append(week1[p1])
#         p1 += 1
#         p2 += 1
#     elif week1[p1] < week2[p2]:
#         p1 += 1
#     else:
#         p2 += 1
# print(ans)