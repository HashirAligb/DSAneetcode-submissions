# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # so I know that i will use a queue to continously get the rightmost element 
        # i will loop through the current length og the queue to keep updting a varible, so that when it reaches 
        # the end of the bs level traversal, he rightmost node is the last to be casted into that va which i can then add into my res 
        # however as i cast my rightmost variable i also want to append my eft and right children of that node to my queue 


        q = collections.deque([root]) 
        res = []
        while q:  
            rightvar = None 
            qlen = len(q)
            for i in range(qlen): 
                node = q.popleft() 
                if node: 
                    rightvar = node 
                    q.append(node.left) 
                    q.append(node.right) 
            if rightvar: 
                res.append(rightvar.val) 
        return res 