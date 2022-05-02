import os
import sys


def isTriple(nums):
    count = {}
    cur_max = None

    for num in nums:
        if cur_max == None:
            cur_max = num
            count[num] = 1

        elif count[cur_max] >= 3:
            print(cur_max)
            return

        elif num != cur_max and num in count:
            count[num] += 1
            if count[num] >= count[cur_max]:
                cur_max = num

        elif num == cur_max:
            count[num] += 1
        else:
            count[num] = 1

    if count[cur_max] >= 3:
        print(cur_max)

    else:
        print(-1)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    testCases = input().rstrip()

    for i in range(int(testCases)):
        length = input()
        isTriple(list(map(int, input().rstrip().split())))
