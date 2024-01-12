# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(parent):
            if parent:
                parent.left, parent.right = invert(parent.right), invert(parent.left)
                return parent
        
        return invert(root)
