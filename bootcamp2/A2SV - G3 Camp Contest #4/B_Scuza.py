# from collections import defaultdict


# for _  in range(int(input())):
#     n,q = map(int,input().split())
#     steps = list(map(int,input().split()))
#     questions = list(map(int,input().split()))

#     hash = defaultdict(int)
#     hash[steps[0]] = steps[0]
#     prefix = [steps[0]]
#     for i in range(1,n):
#         if steps[i] > steps[i - 1]:
#             hash[steps[i]] = hash[prefix[i - 1]] + steps[i]
#             prefix.append(steps[i])
#         elif steps[i] <= steps[i - 1]:
#             hash[steps[i - 1]] += steps[i]
#             prefix.append(steps[i - 1])
    
#     print(prefix,hash)
#     res = []
#     for n in questions:
#         if n == 0:
#             res.append(0)
#             continue

#         left,right = 0, len(prefix) - 1
#         while left < right:
#             mid = (right + left) // 2
#             if prefix[mid] == n:
#                 res.append(hash[prefix[mid]])
#                 break
#             elif n < prefix[mid]:
#                 right = mid
#             else:
#                 left = mid + 1

#         if prefix[mid] != n:
#             if left == 0 and n >= hash[prefix[left]]:
#                 res.append(hash[prefix[left]])
#             else:
#                 for i in range(left,-1,-1):
#                     if n >= hash[prefix[i]]:
#                         res.append(hash[prefix[i]])
#                         break

#     print(*res)

for _ in range(int(input())):
  n, q = list(map(int, input().split()))
  steps = list(map(int, input().split()))
  questions = [(int(x), i) for i, x in enumerate(input().split())]
  questions.sort()
  res = [0] * len(questions)
 
  l = 0
  total = 0
  for k, i in questions:
    while l < n and steps[l] <= k:
      total += steps[l]
      l += 1
    res[i] = total
  print(*res)
