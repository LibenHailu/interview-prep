import sys


def howMuch(myInput):

    my_sorted = myInput[1]
    my_sorted.sort()

    for i in range(myInput[2]):

        left = 0
        right = len(my_sorted) - 1
        best = 0

        while left <= right:

            mid = left + (right-left)//2

            if myInput[3+i] > my_sorted[mid]:
                left = mid + 1
                best = mid + 1

            elif myInput[3+i] < my_sorted[mid]:
                right = mid - 1

            else:
                left = mid + 1
                best = mid + 1

        print(best)


if __name__ == "__main__":

    myInput = []

    # shop = input()
    # shop.append

    # for i in range(7):
    shop = input()
    myInput.append(int(shop))
    myInput.append(list(map(int, input().split())))

    days = input()
    myInput.append(int(days))

    for i in range(int(days)):
        myInput.append(int(input()))

    howMuch(myInput)
