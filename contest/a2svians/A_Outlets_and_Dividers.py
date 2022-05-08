import heapq


def solution(target, outlets):
    if target <= 2:
        return 0

    free = 2
    heap = []
    for outlet in outlets:
        heapq.heappush(heap, -outlet)

    res = 0
    while heap and target > free:
        free -= 1
        free += -heapq.heappop(heap)
        res += 1
    return res if target <= free else -1


if __name__ == '__main__':
    query = int(input())
    for i in range(query):
        q2 = list(map(int, input().rstrip().split()))
        print(solution(q2[0], list(map(int, input().rstrip().split()))))
