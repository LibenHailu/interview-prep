

import collections


def solution(n, edges, two, one, fiveH):
    pars = [i for i in range(n)]
    ranks = [1] * n

    def find(n1):
        if n1 != pars[n1]:
            pars[n1] = pars[pars[n1]]
            return find(pars[n1])

        return n1

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)

        if r1 == r2:
            return False

        if ranks[r2] > ranks[r1]:
            pars[r1] = r2
            ranks[r2] += ranks[r1]
        else:
            pars[r2] = r1
            ranks[r1] += ranks[r2]

    for e in edges:
        union(e[0], e[1])

    count = collections.defaultdict(int)
    for i in range(n):
        root_node = find(i)
        count[root_node] += 1

    for kev, val in enumerate(count):
        if val == 1:
            fiveH -= 1
            if fiveH < 0:
                print('NO')
                return
        while val % 4:
            two -= val // 4
            val -= 4 * val // 4

            if two < 0:
                print('NO')
                return

            diff = val % 2

            if diff == 2:
                one -= 1
                if one < 0:
                    print('NO')
                    return
            elif diff == 1:
                fiveH -= 1
                if fiveH < 0:
                    print('NO')
                    return
    print('YES')


if __name__ == '__main__':
    q1 = list(map(int, input().rstrip().split()))
    edges = []
    for i in range(q1[1]):
        edges.append(list(map(int, input().rstrip().split())))
    solution(q1[0], edges, q1[2], q1[3], q1[4])
