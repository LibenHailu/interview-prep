n,h=int(input()),{}
for i in range(n):
	o,n=input().split()
    
	h[n]=h.get(o,o)
	h.pop(o,None)
print(len(h))
for n,o in h.items():
	print(o,n)
 

def inorder(root):
    if not root:
        return
    return [inorder(root.left) + root.val + inorder(root.right)]