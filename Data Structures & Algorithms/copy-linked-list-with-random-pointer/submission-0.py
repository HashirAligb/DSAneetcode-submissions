"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first I wanna create a hashmap, to mapp all the current nodes to a copy of them 
        # next I wanna do another pass through the original nodes in the hashmap and use their next, and random vals 
        # to be able to map the clones of those next and randoms to my copy.next and copy.random 
        # edge case tho is what f a node.nex is null, for that I wanna initialize my hashmap ith a None : None 

        # only error I made was copy is a local var so dont forget to re initialize it in second while loop 

        hashmap = {None : None} 

        curr = head 

        while curr: 
            copy = Node(curr.val) 
            hashmap[curr] = copy 
            curr = curr.next 
        
        curr = head 
        while curr:   
            copy = hashmap[curr]
            copy.next = hashmap[curr.next] 
            copy.random = hashmap[curr.random] 
            curr = curr.next
        
        return hashmap[head] 
