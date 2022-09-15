def solution(brackets):
    stack = []
    for c in brackets:
        if not stack:
            stack.append(c)
        elif stack and c == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)

    return len(stack)//2

if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        _ = input()
        print(solution(input()))
