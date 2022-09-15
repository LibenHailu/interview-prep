def solution(chairs,spaces):
    spaces.sort(reverse=True)
    needed = 0
    for i in range(len(spaces)):
        if i == 0:
            needed += 2 * spaces[i] + 1
        elif i == len(spaces) - 1:
            needed += 1
        else:
            needed += spaces[i] + 1
    return needed <= chairs

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        _,chairs = map(int,input().split())
        spaces = list(map(int, input().split()))
        if solution(chairs,spaces):
            print("YES")
        else:
            print("NO")
