
from calendar import FRIDAY, MONDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY


tests = int(input())
# print(tests)
 
for _ in range(tests):
    l, r, a = list(map(int, input().split()))
    if l//a == r//a:
        print((r//a)+(r%a))
    else:
        print(max((r//a)+(r%a),((r//a)-1 + a-1)))


