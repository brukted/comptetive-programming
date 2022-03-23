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
        
        ans = []
        bfs_deque = deque([(root,0)])
        last_max = float("-inf")
        last_level = 0
        while bfs_deque:
            node , level = bfs_deque.popleft()
            if level != last_level:
                ans.append(last_max)
                last_level = level
                last_max = float("-inf")
                
            last_max = max(last_max,node.val)
            if node.left:
                bfs_deque.append((node.left,level+1))
            if node.right:
                bfs_deque.append((node.right,level+1))
        
        if last_max != float("-inf"):
            ans.append(last_max)
        return ans
