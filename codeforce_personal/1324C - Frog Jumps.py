test_cases = int(input())
for i in range (test_cases):
    board = list(map(len, input().split('R')))
    print(max(board) + 1)