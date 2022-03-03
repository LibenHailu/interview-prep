# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []

        q = deque([(root, 0)])

        d = defaultdict(list)

        while q:

            node, layer = deque.popleft(q)

            d[layer].append(node.val)

            if node.left:
                q.append((node.left, layer+1))

            if node.right:
                q.append((node.right, layer+1))

        for key, value in d.items():

            if key % 2 != 0:
                print(value)
                res.append(value[::-1])
            else:
                res.append(value)

        return res
