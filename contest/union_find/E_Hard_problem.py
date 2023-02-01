# from functools import lru_cache
# import sys


# n = int(input())
# cost = list(map(int,input().split()))
# words = []
# for _ in range(n):
#     words.append(input())

# @lru_cache()
# def recur(i,c,s):
#     # print(i,c,s)
#     if i >= len(words):
#         return c
#     rev = str(words[i][::-1])
#     if str(words[i]) < s and rev >= s:
#         return min(recur(i+1,sys.maxsize,str(words[i])),recur(i+1,c+cost[i],rev))
#     elif str(words[i]) >= s and str(rev) < s:
#         return min(recur(i+1,c ,str(words[i])),recur(i+1,sys.maxsize,rev))
#     elif str(words[i]) < s and rev < s:
#         return -sys.maxsize
#     else:
#         return min(recur(i+1,c,str(words[i])),recur(i+1,c+cost[i],rev))
    
#     # else:
#     #     rev = words[i]
    
# res = recur(0,0,"")
# if res != -sys.maxsize:
#     print(res)
# else:
#     print(-1)
n=int(input())
z=(10**9)*n+1
c=list(map(int,input().split()))
s=[input() for i in range(n)]
mat=[[z,z] for i in range(n)]
mat[0][0]=0
mat[0][1]=c[0]
for i in range(1,n):
	s2=s[i][::-1]
	s1=s[i-1][::-1]
	a,b,p,q=z,z,z,z
 
	if s[i]>=s[i-1]:
		a=mat[i-1][0]
	if s[i]>=s1:
		b=mat[i-1][1]
	mat[i][0]=min(a,b)
	
	if s2>=s[i-1]:
		p=mat[i-1][0]
	if s2>=s1:
		q=mat[i-1][1]
	mat[i][1]=c[i]+min(p,q)
res=min(mat[n-1][0],mat[n-1][1])
if res>=z:
	print(-1)
else:
	print(res)
