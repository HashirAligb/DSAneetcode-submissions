class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # starts at index 0, ends before last element 
            result.append(s[j + 1 : j + 1 + length])  #  starts at index 2 rt after j, ends at the 4 + 2 
            i = j + 1 + length  
        return result 



        