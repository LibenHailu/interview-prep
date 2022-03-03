# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        q = deque([root])

        while q:
            length = len(q)
            sum = 0

            count = 0
            while count < length:
                node = deque.popleft(q)
                sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                count += 1

            res.append(sum/length)

        return res
