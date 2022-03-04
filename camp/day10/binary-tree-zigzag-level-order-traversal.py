# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        zigzag = []
        bfsDeq = deque([(root, 0)])
        last_depth = 0
        ltr = True
        level = []
        while bfsDeq:
            v, depth = bfsDeq.popleft()
            if depth != last_depth:
                if not ltr:
                    level = level[::-1]
                zigzag.append(level)
                level = []
                ltr = not ltr
                last_depth = depth
            level.append(v.val)
            if v.left:
                bfsDeq.append((v.left, depth+1))
            if v.right:
                bfsDeq.append((v.right, depth+1))

        if not ltr:
            level = level[::-1]
        zigzag.append(level)

        return zigzag
