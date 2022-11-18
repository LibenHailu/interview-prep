"""
You are given 2 arrays representing the stock prices of a big tech company for 2 consecutive weeks, week1 and week2. 
A price is called k-repeating if the stock was sold for that price for k weeks consecutive weeks. 

Example: week1= [4,9,5], week2= [9,4,9,8,4]
Prices 4 and 9 are 2-repeating because the stock has been sold for price 4 and price 9 in both weeks.
Return all 2-repeating prices. A price must appear in your result array as many times as it appears in its minimum appearance. 
[4,9]
week1 = [4,5,9]
pointer1 = 2
week2 = [4,4,5,8,9]
pointer2 = 4

week1 = n
week2 = m
Time = o(m+n)+o(nlogn)+o(mlogm)
res = [2:0](min(n,m))

week1 = [2,2]
o(n)
week1 = [2,2,2]
o(m)
res = [2,2]
Time = O(m + n)
Space = 
"""
week1 = list(map(int,input().split()))
week2 = list(map(int,input().split()))
dict = {}
res = []
for num in week1:
    if num in dict:
        dict[num] +=1
    else:
        dict[num] = 1
for i in range(len(week2)):
    if week2[i] in dict:
        dict[week2[i]] -=1
        res.append(week2[i])
        if dict[week2[i]] == 0:
            del dict[week2[i]]
print(res)
    

    
    

