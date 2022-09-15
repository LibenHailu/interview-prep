# add all words and thier count on dic
# calculate for each
for _ in range(int(input())):
    words = int(input())
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()
    d = dict()

    for l in p1:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for l in p2:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for l in p3:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    
    score = []

    p1_score = 0
    for l in p1:
        if d[l] == 1:
            p1_score += 3
        elif d[l] == 2:
            p1_score += 1
   
    p2_score = 0
    for l in p2:
        if d[l] == 1:
            p2_score += 3
        elif d[l] == 2:
            p2_score += 1
    p3_score = 0
    for l in p3:
        if d[l] == 1:
            p3_score += 3
        elif d[l] == 2:
            p3_score += 1
    
    print(p1_score,p2_score,p3_score)