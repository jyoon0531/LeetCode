# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return 0

            return max(height(node.left), height(node.right))+1
        
        def dfs(node):
            if not node:
                return True
            
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return False
            
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)

        