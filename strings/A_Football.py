# s = input()
# count = 1
# for i in range(1,len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         count = 1
    
#     if count == 7:
#         print("YES")
#         exit()

# print("NO")
d = {}
for _ in range(int(input())):
    k = input()
    d[k] = 1 + d.get(k,0)
    s = sorted(d.items(),key=lambda x:x[1],reverse=True)
print(s[0][0])