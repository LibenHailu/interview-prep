def solution(rubles,ammounts):
    # set start set end
    # set cur_start,cur_end
    # cur_ammount
    # with while update your cur_end till the condition is full filled
    # when breaks check if it is the longer and update your start and end
    # if start and end are not zero that is the longer seuence
    start = None
    end = None

    cur_start = 0
    cur_end = 0
    cur_amount = rubles

    while cur_end < len(ammounts):
        
        if cur_amount < 0:
            while cur_amount < 0 and cur_start < len(ammounts):
                cur_amount -= ammounts[cur_start]
                cur_start += 1

            # pass
        else:
            cur_amount += ammounts[cur_end]
            if end == None and  start == None:
                start = cur_start
                end = cur_end
            elif end - start < cur_end - cur_start:
                start = cur_start
                end = cur_end
            cur_end += 1
    if start == None or end == None:
        return (-1,)
    
    return (start +1 ,end + 1)
        
    # while cur_end < len(ammounts):
    #     cur_amount += ammounts[cur_end]
    #     if cur_amount < 0:
    #         # print(cur_amount,cur_start,cur_end)
    #         while cur_amount < 0 and cur_start < len(ammounts):
    #             cur_amount -= ammounts[cur_start]
    #             cur_start += 1
    #         # cur_amount = rubles
    #         # if cur_start == cur_end:
    #         #     cur_start = cur_end + 1
    #         #     cur_end = cur_start
    #         # else:
    #         #     cur_start = cur_end
    #         #     cur_end = cur_start
    #         # continue
    #     else:
    #         if end == None and  start == None:
    #             start = cur_start
    #             end = cur_end
    #         elif end - start < cur_end - cur_start:
    #             start = cur_start
    #             end = cur_end
    #         cur_end += 1
    # if start == None or end == None:
    #     return (-1,)
    
    # return (start +1 ,end + 1)

# print(solution(10,[-16, 2, -6, 8]))
# print(solution(10,[-16]))
# print(solution( 1000,[-100000, -100000, -100000]))

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        _,rubles = map(int, input().split())
        print(*solution(rubles,list(map(int, input().split()))))



