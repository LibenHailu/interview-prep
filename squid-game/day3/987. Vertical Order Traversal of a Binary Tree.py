# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        heap = []
        res = []
        def dfs(row,col,node):
            heappush(heap,(col,row,node.val))
            if node.right:
                dfs(row + 1,col + 1, node.right)
            if node.left:
                dfs(row + 1, col - 1,node.left)
        dfs(0,0,root)
        cur = 0
        while heap:
            
            c,r,val = heappop(heap)
            if not res:
                cur = c
                res.append([val])
            else:
                if c == cur:
                    res[-1].append(val)
                else:
                    cur = c
                    res.append([val])
        
        return res