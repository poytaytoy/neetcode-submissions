class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for char in s: 
            if char in dict: 
                dict[char] += 1
            else: 
                dict[char] = 1

        for char in t: 
            if char in dict: 
                dict[char] -= 1
            else:   
                return False 

        for (k, v) in dict.items(): 
            if v != 0: 
                return False 

        return True 