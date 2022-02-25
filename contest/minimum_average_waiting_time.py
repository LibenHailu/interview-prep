# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import heapq

# #
# # Complete the 'minimumAverage' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts 2D_INTEGER_ARRAY customers as parameter.
# #


# def minimumAverage(customers):
#     # Write your code here
#     h = []
#     for order in customers:
#         heapq.heappush(h, [order[1], order[0]])

#     l = []
#     while h:
#         time, arrival = heapq.heappop(h)
#         if not l:
#             l.append(time + arrival - 0)
#         l.append(l[len(l) - 1] + time + arrival - 0)

#     sum = sum(l)

#     return sum//len(l)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     customers = []

#     for _ in range(n):
#         customers.append(list(map(int, input().rstrip().split())))

#     result = minimumAverage(customers)

#     fptr.write(str(result) + '\n')

#     fptr.close()
import heapq
from os import times_result


def minimumAverage(customers):
    # Write your code here
    left = 0
    print(customers)
    total_time = 0
    current_time = 0
    h = []

    if not h:
        heapq.heappush(h, [customers[left][1], customers[left][0]])

    while h:
        arrival, time_taken = heapq.heappop(h)
        current_time += time_taken
        total_time = current_time - arrival

        print(current_time)
        print(total_time)

        while left < len(customers)-1 and time_taken > customers[left][0]:
            left += 1
            heapq.heappush(h, [customers[left][1], customers[left][0]])

    return total_time / len(customers)


print(minimumAverage([[0, 3], [1, 9], [2, 6]]))
