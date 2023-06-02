class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def distanceKRec(node, distance = -1):
            if node.val == target.val:
                distance = k
            
            if node.left:
                distance = max(distanceKRec(node.left, distance - 1), distance)
            
            if node.right:
                right = distanceKRec(node.right, distance - 1)  
                
                if right > distance:
                    distance = right
                    if node.left:
                        distanceKRec(node.left, distance - 1)
            
            if distance == 0:
                ans.append(node.val)
            
            return distance - 1
            
        distanceKRec(root)
        return ans
            
            
            