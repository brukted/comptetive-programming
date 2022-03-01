"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node', depth=0) -> int:
        if not root:
            return 0

        depth += 1
        max_depth = depth

        if not root.children:
            return max_depth

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child, depth))

        return max_depth
