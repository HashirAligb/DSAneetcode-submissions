# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- 1st Base Case: make sure if theres no nodes in both trees, then return True since they match
- 2nd Base: if theres a node in one tree but not on the other, then return False
- I need a helper function that will check the same nodes only
- recurse it with the whole subRoot (since I want that to be fully same in the root tree) 
- Oh yeah recurse the left sub-tree and the right sub-tree of the root tree
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            right = sameTree(p.right, q.right)
            left = sameTree(p.left, q.left)

            return p.val == q.val and right and left 
        
        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        left_side = self.isSubtree(root.left, subRoot)
        right_side = self.isSubtree(root.right, subRoot)

        return left_side or right_side


        


        