# have two adj list
# for _ in range(int(input())):
#     floors = int(input())
#     tourch = [[0] * (i + 1) for i in range(floors) ]
#     bright = [[0] * (i + 1) for i in range(floors) ]
#     for i,floor in enumerate(bright):
#         for j,room in enumerate(floor):
#             if room !=  i + 1:
#                 tourch[i][j] = 1
#                 bright[i][j] = i + 1
#                 if i+1 < floors and j + 1 < floors: 
#                     if bright[i +1][j] == i + 1 or bright[i +1][j + 1] == i +1:
#                         bright[i +1][j] += 1
#                     else:
#                         bright[i +1][j] = i + 1

#                         bright[i +1][j + 1] = i + 1

#     for t in tourch:
#         print(*t)  
for _ in range(int(input())):
    floors = int(input())
    tourch = [[0] * (i + 1) for i in range(floors) ]
    for t in tourch:
        t[0] = 1
        t[-1] = 1
        print(*t)