# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [(root, 0, 0)]
        sums = 0

        while stack:

            node, parent, grandP = stack.pop()

            if grandP != 0 and grandP % 2 == 0:
                print(node.val)
                sums += node.val

            if node.left:
                stack.append((node.left, node.val, parent))

            if node.right:
                stack.append((node.right, node.val, parent))

        return sums
