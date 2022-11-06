r1,c1,r2,c2 = map(int,input().split())
rock = bishop = king = 0
rock = (r1 != r2) + (c1 != c2)
if (r1 - r2 ) % 2 == (c1 - c2) % 2:
    bishop = 1 if abs(r1 - r2) == abs(c1 - c2) else 2
else:
    bishop = 0
king = max(abs(r1 - r2), abs(c1 - c2))
print(f"{rock} {bishop} {king}") 