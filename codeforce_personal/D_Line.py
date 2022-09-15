# have two pointer
# calculate 

for _ in range(int(input())):
    length = int(input())
    arr = [0]*length
    seq = input()
    for i in range(len(seq)):
        if seq[i] == 'L':
            arr[i] = i
        else:
            arr[i] = len(seq) - (i + 1)
    # print(arr)
    sum_ = sum(arr)
    res = sum_
    # resList = []
    # for i in range(len(seq)//2):
    #     if seq[i] == 'L':
    #         res -= arr[i]
    #         res += (len(seq) - 1)   - i
    #         resList.append(res)
    #     else:
    #         resList.append(res)
    # # for j in range(len(seq)//2,len(seq)):
    # #     if seq[j] == 'R':
    # #         res -= arr[j]
    # #         res += (len(seq)//2 + (len(seq)//2 - j) )
    # #         resList.append(res)
    # #     else:
    # #         resList.append(res)
    # print(resList)
    l = 0
    r = len(seq) - 1
    resList = []
    count = 0
    while l <= r :
        if seq[l] == "R":
            # resList.append(res)
            count += 1
            l += 1
            # continue
            # uLeft = 1
        if seq[r] == "L":
            # resList.append(res)
            count += 1
            r -= 1
            # continue
            # uRight = -1
        # uLeft = 0
        # uRight = 0
        if seq[l] != "R":
            res -= arr[l]
            res += len(seq) - (l + 1)
            cur_max = max(resList)
            v = max(res, cur_max)
            resList.append(v)
            #  step = "right"
            l += 1
            # uLeft = 1
            
        if seq[r] != "L":
            res -= arr[r]
            res += r
            cur_max = max(resList,0)
            v = max(res, cur_max)
            resList.append(v)
            r -= 1
            # uRight = -1
        # else:
        #     count += 1
        #     r -= 1
        #     l += 1



        # l += uLeft
        # r += uRight
    # resList.extend([resList[-1]]*count)
    cur_max = max(resList)
    for i in range(len(resList),length):
        resList.append(cur_max)
    print(*resList,count,cur_max)



