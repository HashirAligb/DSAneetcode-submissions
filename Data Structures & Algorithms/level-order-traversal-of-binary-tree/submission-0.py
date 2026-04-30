# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        q = collections.deque() 
        res = []  
        q.append(root)


        while q:  
            lenq = len(q)
            level = [] 

            for i in range(lenq):  
                latest = q.popleft()
                if latest:  
                    level.append(latest.val)
                    q.append(latest.left) 
                    q.append(latest.right)   
            if level: 
                res.append(level) 
        return res 



            
            