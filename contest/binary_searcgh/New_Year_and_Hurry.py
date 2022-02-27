import sys


def howMuch(myInput):
    left = 1
    right = myInput[0]

    while left <= right:

        mid = left + (right-left)//2

        time_needed = 0

        for q in range(1, mid+1):
            time_needed += 5 * q

        if time_needed + myInput[1] > 240:
            right = mid-1

        else:
            left = mid+1

    print(right)


if __name__ == "__main__":
    howMuch(list(map(int, input().split())))
