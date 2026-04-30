# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # input a tree 
        # a list of levels  
        # i wanna use a queue to maintain lvls. 
        # i wanna also make sure tht i can track the lvls. 
        # ill ad the left and the right nodes, if the node is none empty 
        # then when i append to result list i wont append level if its empty 

        q = collections.deque() 
        res = []  
        q.append(root)

        while q: 
            length = len(q)
            level = []  

            for i in range(length):  
                node = q.popleft()
                if node: 
                    level.append(node.val) 
                    q.append(node.left) 
                    q.append(node.right)  
            if level: 
                res.append(level) 
        return res 



            



            
            