import sys


def solution(poses):
    res = sys.maxsize
    res = min(res,abs(poses[1] - poses[0]) + abs(poses[2] - poses[0]))
    res = min(res,abs(poses[0] - poses[2]) + abs(poses[1] - poses[2]))
    res = min(res,abs(poses[0] - poses[1]) + abs(poses[2] - poses[1]))
    return res

        

if __name__ == "__main__":
    print(solution(list(map(int, input().rstrip().split()))))

