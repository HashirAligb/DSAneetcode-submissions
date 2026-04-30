# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # so this is a preorder traversal where we will check with a maxval variable whether a child is more of less than its parent 
        # ima have a res variable that becomes local to each recrsuvie callt o count as 1 if its greater than the current maxval and - if its not 
        # ill += to my outside res, when i call my nodes left and right subtree recursively 



        def dfs(node, maxval): 
            if not node: 
                return 0 
            
            res = 1 if node.val >= maxval else 0 
            maxval = max(maxval, node.val) 
            res += dfs(node.left, maxval) 
            res += dfs(node.right, maxval) 

            return res  
        
        return dfs(root, root.val)