import string


size =  {v: i+1 for i,v in enumerate(string.ascii_lowercase)}
# print(size)
for _ in range(int(input())):
    ans = 0
    l = int(input())
    word = input()
    for j in range(l):
        ans = max(ans,size[word[j]])
    print(ans)


        