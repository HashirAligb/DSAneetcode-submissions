class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # ill get my index and val in a map to mark down all the indexes of my alien dict  
        ordermap = {n : i for i, n in enumerate(order)} 

        for i in range(len(words) - 1): # since we use i + 1
            w1, w2 = words[i], words[i+1] # compare each word

            for j in range(len(w1)): 
                if j == len(w2):    # so if my second word is smaller i know ts not ordered smaller word need to first 
                    return False 
                if w1[j] != w2[j]:  # now once i find a difeering letter i will look thm up on my order map 
                    if ordermap[w1[j]] > ordermap[w2[j]]: # then i can compare if my w1 is smaller cuz if it is then its
                        return False    # not ordered so i return false
                    break  # we break since we only care about the first differing character ***important***
        return True     
