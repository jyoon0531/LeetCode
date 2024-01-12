# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        answer = []

        def dfs(node):
            if node.val == val:
                answer.append(node)
            elif node.val < val and node.right:
                dfs(node.right)
            elif node.val > val and node.left:
                dfs(node.left)

        dfs(root)

        return answer[0] if answer else None 
        

