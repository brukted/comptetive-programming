# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode, history=(1, 1)) -> int:
        if not root:
            return 0

        nweg = 0

        if history[1] % 2 == 0:  # This node's grand parent is even
            nweg += root.val

        history = root.val, history[0]  # Make prev parent granny

        nweg += self.sumEvenGrandparent(root.left, history)
        nweg += self.sumEvenGrandparent(root.right, history)

        return nweg
