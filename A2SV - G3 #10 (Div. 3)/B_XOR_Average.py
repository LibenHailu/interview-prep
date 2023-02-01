for _ in range(int(input())):
    n = int(input())
    print(*[1] if n == 1 else [1 + n % 2] + [2]*(n-2) + [3 - n % 2])