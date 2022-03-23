# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        cur_max = -sys.maxsize
        cur_label = 0
        result = []

        q = deque([(root, 0)])

        while q:
            node, label = q.popleft()

            if cur_label < label:
                result.append(cur_max)
                cur_label = label
                cur_max = -sys.maxsize

            if cur_label == label and cur_max < node.val:
                cur_max = node.val

            if node.right:
                q.append((node.right, label+1))

            if node.left:
                q.append((node.left, label+1))

        result.append(cur_max)

        return result
