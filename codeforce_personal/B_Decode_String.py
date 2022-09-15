# start form the back
# use while loop
# strip the upfront two string
# add to list
# return the string reversed

import code


for _ in range(int(input())):
    length = int(input()) - 1
    coded = input()
    hashMap = dict()
    for i in range(1,27):
        hashMap[i] = chr(96+i)

    res = []
    while length >= 0:
        if int(coded[length]) == 0:
            key = int(coded[length - 2:length])
            res.append(hashMap[key])
            length -= 3
        else:
            key = int(coded[length])
            res.append(hashMap[key])
            length -= 1
    # print(res)
    print("".join(res[::-1]))
    
