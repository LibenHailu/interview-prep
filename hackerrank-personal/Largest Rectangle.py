
def largestRectangle(h):
    # Write your code here
    # if len(h) < 3:
    #     return 0
    h += [0]
    s = []
    ma = 0
    for i in range(0, len(h)):
        j = i
        while len(s) > 0 and s[-1][0] >= h[i]:
            val, j = s.pop()
            print(s,i,j,val,ma)
            ma = max(ma, (i - j) * val)
        s.append([h[i], j])
        # print(s)
    return ma

# print(largestRectangle([1, 2, 3, 4, 5]))
print(largestRectangle([11, 11, 10, 10, 10]))
# print(largestRectangle([1, 2, 3, 4, 5]))