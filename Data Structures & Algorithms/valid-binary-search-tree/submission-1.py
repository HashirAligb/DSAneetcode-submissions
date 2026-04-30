# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # i have a left, right and root. 
        # my node, the left, the right are my initial parameters 

        def valid(node, left, right): 
            if not node: 
                return True 
            if not (left < node.val and node.val < right): 
                return False  
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right)) 
        
        return valid(root, float('-inf'), float('inf'))

