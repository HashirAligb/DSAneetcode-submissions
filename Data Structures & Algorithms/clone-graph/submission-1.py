"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        oldtoNew = {}  

        # initialize hashmap and save all the nodes to themself in it first 
        # then have a base case to see if the node copy is alr in the hashmap. 
        # explore the nodes neighbors and if the neighbo has one of its neighbors alr in the hashmap that show their connection 
        # next we return when we finish up that given nodes neighbors dfs's abnd tricly to te next node to create a clone of  
        # when we finally reach the final node it will recursively go back to the very first which then explores it, then we see 
        # that its connected asw 


        def dfs(node): 
            if node in oldtoNew: 
                return oldtoNew[node] 
            
            copy = Node(node.val) 
            oldtoNew[node] = copy 

            for i in node.neighbors: 
                copy.neighbors.append(dfs(i)) 
            return copy  

        return dfs(node) if node else None 


            