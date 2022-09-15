#

#     for i in range(1,27):
#         hashMap[chr(96+i)] = i
#     word = input()
#     res = []
#     for i in range(len(word)):
#         if hashMap[word[i]] <= hashMap[word[0]]:
#             res.append(i+1)
    
#     print(*res)
# 0

# have a hashmap
# add index of them
# sort the hashmap
# calculate the difference

from collections import defaultdict
import itertools
for _ in range(int(input())):
    wordMap = defaultdict(list)
    hashMap = dict()
    for i in range(1,27):
        hashMap[chr(96+i)] = i

    word = input()
    for i in range(len(word)):
        wordMap[word[i]].append(i+1)
    
    if word[0] > word[len(word) - 1]:
        wordMap = dict(sorted(wordMap.items(),key=lambda x:x[0],reverse=True))
    else:
        wordMap = dict(sorted(wordMap.items(),key=lambda x:x[0]))
    
    res = []
    price = 0
    for i in list(itertools.chain.from_iterable(wordMap.values())):
        # if not res and ord(word[i - 1]) <= ord(word[0]) or ord(word[i - 1]) <= ord(word[len(word) - 1]):
        #     res.append(i)

        if ord(word[i - 1]) <= ord(word[0]) or ord(word[i - 1]) <= ord(word[len(word) - 1]):
            if res:
                price += abs(hashMap[word[i-1]] - hashMap[word[res[-1] -1]])
            res.append(i)
    
    print(*(price,len(res)))
    print(*res)

