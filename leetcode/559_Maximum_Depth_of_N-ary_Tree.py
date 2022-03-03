"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        max_depth = 1

        stack = [(root, 1)]

        while stack:

            new_root, depth = stack.pop()

            max_depth = max(max_depth, depth)

            for child in new_root.children:
                stack.append((child, depth + 1))

        return max_depth
