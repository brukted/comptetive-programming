# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        vals = []
        def discover_tree(node = root):
            if not node:
                return
            vals.append(node.val)
            discover_tree(node.left)
            discover_tree(node.right)
        discover_tree()
        vals.sort()
        
        i = 0
        
        def correct_tree(node = root):
            nonlocal i
            if node.left:
                correct_tree(node.left)
            node.val = vals[i]
            i += 1
            if node.right:
                correct_tree(node.right)
        
        correct_tree()