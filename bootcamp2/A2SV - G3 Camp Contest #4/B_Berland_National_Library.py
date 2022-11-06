from re import L


l = int(input())
id = []
for i in range(l):
    sign,num = input().split()
    if sign == "+":
        id.append(int(num))
    else:
        id.append(- int(num))
max_ = 0
hashSet = set()
for i in range(l):
    # print(-id[i] in hashSet)
    if id[i] < 0:
        if  -id[i] in hashSet: 
            # nums[i] = nums[i - 1] - 1
            hashSet.remove(-id[i])
        else:
            max_ = max_ + 1
    else:
        hashSet.add(id[i])
    max_ = max(max_, len(hashSet))
print(max_)