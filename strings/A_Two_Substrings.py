s=input()
u=s.find('AB')
v=s.find('BA')
print("YES" if (u+1 and s.find('BA',u+2)+1) or (v+1 and s.find('AB',v+2)+1)else'NO')