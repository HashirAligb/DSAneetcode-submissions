# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, max_depth):
            if not node:
                return 0

            max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            return max_depth
        return dfs(root, 0)
    
        
