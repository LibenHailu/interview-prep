# HAVE A loop 
# when you get something smaller than add to yout strring
#
# tc = int(input())
# for _ in range(tc):

#     res = []
#     word = input()


#     capactity = int(input())
#     for c in word:
#         if ord(c) - 96 <= capactity:
#             res.append(c)
#             capactity -= ord(c) - 96
        
#     print("".join(res))

# use backtracking
# from turtle import back


# tc = int(input())
# for _ in range(tc):
#     len = 0
#     res = []
#     word = input()
#     capactity = int(input())
#     def backtrack(i,curr):
#         if i== len(word) - 1 or capactity == 0:
#             # if len < len(curr):
#             #     len = len(curr)
#             #     res = curr
#             return curr
#         for j in range(i + 1,len(word)):
#             return backtrack(j,curr + [word[i]])
    
#     print(max(len(backtrack(0,[])), len(backtrack(1,[]))))

#     print(res)


# from heapq import heappop, heappush


# tc = int(input())
# for _ in range(tc):
#     res = []
#     word = input()
#     capactity = int(input())
#     needed = 0
#     heap = []
#     for i in  range(len(word)):
#         needed += ord(word[i]) - 96 
#         heappush(heap, ( (- ord(word[i]) - 96 ), i) )
#         res.append(word[i])
    
#     if needed <= capactity:
#         print(word)
#     else:
#         while heap and needed > capactity:
#             print(price,index)
#             price,index = heappop(heap)
#             needed += price
#             del res[index]
        
#         print(*res)


    # for c in word:
    #     if ord(c) - 96 <= capactity:
    #         res.append(c)
    #         capactity -= ord(c) - 96
        
    # print("".join(res))


    # sort the word
    # start form the first add counter add them to dict



    # needed = 0
    # heap = []
    # for i in  range(len(word)):
    #     needed += ord(word[i]) - 96 
    #     heappush(heap, ( (- ord(word[i]) - 96 ), i) )
    #     res.append(word[i])
    
    # if needed <= capactity:
    #     print(word)
    # else:
    #     while heap and needed > capactity:
    #         print(price,index)
    #         price,index = heappop(heap)
    #         needed += price
    #         del res[index]
        
    #     print(*res)



tc = int(input())
for _ in range(tc):
    res = []
    word = input()
    capactity = int(input())

    sorted = ''.join(sorted(str))
    count = dict()
    
    for c in sorted:
        if c not in count and capactity - (ord(c) - 96) > 0:
            count[c] = 1
        elif capactity - (ord(c) - 96) > 0:
            count[c] += 1
        
    for c in word:          
        if c in count and count[c] > 0:
            res.append(c)
            count[c] -= 1
        
    print("".join(res))
 