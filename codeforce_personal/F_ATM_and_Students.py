for _ in range(int(input())):
    n, s = map(int, input().split())
    arr = [-1] + list(map(int, input().split()))
    maxSoFar = x = y = 0
    left = 1
    curr = s
    for right in range(1, n + 1):
        curr += arr[right]
        while curr < 0:
            curr -= arr[left]
            left += 1
        if right - left + 1 > maxSoFar:
            maxSoFar = right - left + 1
            x = left
            y = right
    print(f'{x} {y}' if maxSoFar else -1)