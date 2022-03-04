# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dq = deque([(root, 0)])
        palindrom_stack = []
        last_depth = 0

        def is_stack_symmetric():
            i = 0
            j = len(palindrom_stack) - 1
            while i <= j:
                if palindrom_stack[i] != palindrom_stack[j]:
                    return False
                i += 1
                j -= 1
            return True

        while dq:
            v, depth = dq.popleft()
            # Depth change detected
            if depth != last_depth:
                last_depth = depth
                if not is_stack_symmetric():
                    return False
                palindrom_stack.clear()

            palindrom_stack.append(v.val if v else None)
            if v == None:
                continue
            dq.append((v.left, depth+1))
            dq.append((v.right, depth+1))

        return is_stack_symmetric()
