# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        cols = defaultdict(list)  
        min_col, max_col = 0, 0  

        q = deque([(root, 0)])

        while q:    
            node, col = q.popleft() 
            min_col, max_col = min(col, min_col), max(col, max_col)
            cols[col].append(node.val)  
            if node.left: 
                q.append((node.left, col - 1)) 
            if node.right: 
                q.append((node.right, col + 1)) 
        
        return [cols[c] for c in range(min_col, max_col + 1)]



