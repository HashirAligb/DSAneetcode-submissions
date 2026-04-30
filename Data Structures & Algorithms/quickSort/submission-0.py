"""
Input:
pairs = [(4, "cat"), (1, "bird"), (2, "dog"), (3, "bird")]

pivot = (3, "bird")
(2, "dog") 

<----- pivot ----->
smaller      bigger


Output: (4, "cat"), (1, "bird")



"""
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def _qs_(lo, hi):
            if hi <= lo:
                return  

            pivot = pairs[hi]
            left = lo

            for i in range(lo,hi):
                if pairs[i].key < pivot.key:
                    temp = pairs[left]
                    pairs[left] = pairs[i]
                    pairs[i] = temp
                    left += 1
            
            # move pivot between left and right 
            pairs[hi] = pairs[left]
            pairs[left] = pivot

            _qs_(lo, left - 1)
            _qs_(left+1, hi)

        if not pairs:
            return pairs

        _qs_(0, len(pairs)-1)
        return pairs




