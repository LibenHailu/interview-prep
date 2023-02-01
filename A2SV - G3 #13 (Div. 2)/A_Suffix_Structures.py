from collections import Counter


s = input()
t = input()
sorted_s = ''.join(sorted(s))
sorted_t = ''.join(sorted(t))

if sorted_s == sorted_t:
    print("array")
    exit()

n = 0
for i in range(len(s)):
    if n < len(t):
        n += t[n] == s[i]

if n == len(t):
    print("automaton")
    exit()

count_s = Counter(s)
count_t = Counter(t)
for key in count_t:
    if key not in count_s:
        print("need tree")
        exit()
    if count_s[key] < count_t[key]:
        print("need tree")
        exit()
print("both")

# if sorted_t in sorted_s:
#     print("both")
#     exit()
# print("hey t",sorted_t)
# print("hey s",sorted_s)
