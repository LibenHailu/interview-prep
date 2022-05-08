def solution(heights):
    res = 0
    stack = []

    for height in heights:
        if not stack:
            stack.append(height)

        else:
            while stack and height > stack[-1]:
                res += 1
                stack.pop()
            stack.append(height)

    return res


if __name__ == '__main__':
    query = int(input())
    for i in range(query):
        q2 = input()
        print(solution(list(map(int, input().rstrip().split()))))
