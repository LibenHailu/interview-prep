n,k = map(int,input().split())

def recurr(val,turn,res):
    if turn == 0 and len(res) == k and sum(res) == n:
        return res
    
    if turn <= 0:
        return

    recurr(val - 1,turn - 1,res + [1])
    recurr(val - 2,turn - 1,res + [2])
    recurr(val - n,turn - 1,res + [val])

print(recurr(n,k,[]))