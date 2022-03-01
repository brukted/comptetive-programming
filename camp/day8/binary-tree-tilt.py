# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt_sum = 0

        def findTiltRec(node):
            """
            returns subTreeSum
            """
            nonlocal tilt_sum

            left_sum = findTiltRec(node.left) if node.left else 0
            right_sum = findTiltRec(node.right) if node.right else 0

            tilt_sum += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        if root:
           findTiltRec(root)

        return tilt_sum
