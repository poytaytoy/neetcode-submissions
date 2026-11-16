class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0 

        for i in range(31, -1, -1): 
            if (n - 2**i >= 0):
                n = n - 2**i
                count += 1    

        return count 