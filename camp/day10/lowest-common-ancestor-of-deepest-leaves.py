# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeavesRec(self, node, depth=0):
        left = node.left
        right = node.right
        # Leaf node
        if not (left or right):
            return (node, depth)

        left_deep = self.lcaDeepestLeavesRec(
            left, depth + 1) if left else (None, -1)
        right_deep = self.lcaDeepestLeavesRec(
            right, depth + 1) if right else (None, -1)

        if left_deep[1] > right_deep[1]:
            return left_deep
        elif right_deep[1] > left_deep[1]:
            return right_deep
        else:
            return (node, right_deep[1])

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.lcaDeepestLeavesRec(root)[0]
