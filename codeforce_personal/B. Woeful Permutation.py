from heapq import heapify, heappop


def solution(num):
    return " ".join([str(i) for i in range(num,0,-1)])


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        print(solution(int(input())))
