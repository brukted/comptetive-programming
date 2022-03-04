# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        dq = deque([(root, 0)])
        last_depth = 0
        level = []

        def calculate_level_avg():
            ans.append(sum(level) / len(level))

        while dq:
            v, depth = dq.popleft()
            if depth != last_depth:
                calculate_level_avg()
                level.clear()
                last_depth = depth

            level.append(v.val)
            if v.left:
                dq.append((v.left, depth+1))
            if v.right:
                dq.append((v.right, depth+1))

        calculate_level_avg()
        return ans
