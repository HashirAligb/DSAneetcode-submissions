class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # Regular dictionary

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # Convert count list to a tuple (for dict key)
            
            if key not in res:  # If this letter frequency does not exist in res
                res[key] = []  # Create an empty list
            
            res[key].append(s)  # Append the word to its correct anagram group

        # Return only the values (lists of anagrams)
        return list(res.values())
