

import itertools


def solution(tc_num, tc):
    for i in range(tc_num):
        perms = list(itertools.permutations(
            [i for i in range(int(tc[i][0]))]))
        # print(perms)
        count = 0
        for j in perms:
            red = []
            blue = []
            for k in j:
                red.append(tc[i][1][k])
                blue.append(tc[i][2][k])
            strRed = "".join(red)
            strBlue = "".join(blue)
            strRed = strRed.lstrip("0")
            strBlue = strBlue.lstrip("0")

            if int(strRed) > int(strBlue):
                count += 1
            elif int(strRed) < int(strBlue):
                count -= 1

        if count > 0:
            print('RED')
        elif count < 0:
            print('BLUE')
        else:
            print('EQUAL')


if __name__ == "__main__":
    test_case_numbers = input()
    test_cases = []

    for i in range(int(test_case_numbers)):
        tc = []
        for i in range(3):
            tc.append(input())
        test_cases.append(tc)

    solution(int(test_case_numbers), test_cases)
