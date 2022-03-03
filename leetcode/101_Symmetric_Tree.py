# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        q = deque([(root, 0)])

        while q:

            node, layer = deque.popleft(q)

            if node.left:
                q.append((node.left, layer + 1))

            if node.right:
                q.append((node.right, layer + 1))

            while len(q) > 0 and q[0][1] == layer:

                node, layer = deque.popleft(q)

                if node.left:
                    q.append((node.left, layer + 1))

                if node.right:
                    q.append((node.right, layer + 1))

            l = 0
            r = len(q)
            #             if (l + r) % 2 == 0:
# #                 rerurn False

#             while l <= r:

#                 if q[l][0].val != q[l][0].val
            mid = (l + r) // 2

            left_part = q[l:mid]
            right_part = q[mid:r]

            if left_part != right_part[::-1]:
                return False

        return True
#             if node.left:
#                 q.append()
#             for i in range(r + 1):
#                 deque.popleft(q)

#             print(node)
