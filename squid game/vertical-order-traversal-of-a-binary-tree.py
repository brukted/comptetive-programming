# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def recusrsiveSolve(node=root, row=0, col=0):
            if node is None:
                return

            ans.append((col, row, node.val))

            recusrsiveSolve(node.left, row + 1, col - 1)
            recusrsiveSolve(node.right, row + 1, col + 1)

        recusrsiveSolve()
        ans.sort()

        _ans = [[]]
        last = ans[0][0]

        for i in ans:
            if i[0] == last:
                _ans[-1].append(i[2])
            else:
                _ans.append([i[2]])
                last = i[0]

        return _ans
