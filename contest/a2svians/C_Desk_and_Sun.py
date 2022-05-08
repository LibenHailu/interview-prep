def solution(edges, affected):
    res = 0

    for edge in edges:
        if affected[0] <= edge[0] <= affected[2] and affected[1] <= edge[1] <= affected[3]:
            res += 1

    return res


if __name__ == '__main__':
    q1 = list(map(int, input().rstrip().split()))
    q2 = []
    for i in range(q1[0]):
        q2.append(list(map(int, input().rstrip().split())))
    for j in range(q1[1]):
        print(solution(q2, list(map(int, input().rstrip().split()))))
