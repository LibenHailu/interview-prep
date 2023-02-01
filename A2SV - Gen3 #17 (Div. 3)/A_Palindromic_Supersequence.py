# from collections import Counter


s = input()
print(s+s[::-1])
# l = len(s)

# if l % 2 == 0:
#     left,right = s[0:l//2], s[l//2:l]
#     leftCount = Counter(left)
#     rightCount = Counter(right)
#     for key,val in leftCount.items():
#         if key not in rightCount:
#             rightCount[key] = val
#         elif val != rightCount[key]:
#             rightCount[key] = max(rightCount[key],val)
#             leftCount[key] = rightCount[key]
#     for key,val in rightCount.items():
#         if key not in leftCount:
#             leftCount[key] = val
#         elif val != leftCount[key]:
#             leftCount[key] = max(leftCount[key],val)
#             rightCount[key] = leftCount[key]
    
#     ans = []
#     for key,val in leftCount.items():
#         ans.append(key * val)

#     res = ''.join(ans)
#     res = ''.join(sorted(res))
#     print(res + res[::-1])
# else:
#     left,right = s[0:l//2 - 1], s[l//2 + 1:l]
#     leftCount = Counter(left)
#     rightCount = Counter(right)
#     for key,val in leftCount.items():
#         if key not in rightCount:
#             rightCount[key] = val
#         elif val != rightCount[key]:
#             rightCount[key] = max(rightCount[key],val)
#             leftCount[key] = rightCount[key]
#     for key,val in rightCount.items():
#         if key not in leftCount:
#             leftCount[key] = val
#         elif val != leftCount[key]:
#             leftCount[key] = max(leftCount[key],val)
#             rightCount[key] = leftCount[key]
    
#     ans = []
#     for key,val in leftCount.items():
#         ans.append(key * val)

#     res = ''.join(ans)
#     res = ''.join(sorted(res))
#     print(res +s[l//2] +  res[::-1])
#     # print(left,'and',right)
