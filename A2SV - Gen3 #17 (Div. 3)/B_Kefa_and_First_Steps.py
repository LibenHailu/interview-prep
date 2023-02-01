n = int(input())
nums = list(map(int,input().split()))

stack = []
ans = 0
for num in nums:
    if not stack:
        stack.append(num)
    elif num >= stack[-1]:
        stack.append(num)
    else:
        stack = []
        stack.append(num)
    ans = max(len(stack),ans)

print(ans)