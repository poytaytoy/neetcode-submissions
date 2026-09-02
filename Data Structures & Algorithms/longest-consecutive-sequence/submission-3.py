class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            return 0
                
        stuff = set() 

        for num in nums:
            stuff.add(num)

        stuff_list = list(stuff)

        longest_chain = 1

        for num in stuff_list: 
            if num - 1 in stuff: 
                continue 

            new_num = num 
            chain_count = 0

            while new_num in stuff: 
                
                chain_count += 1 

                new_num = new_num + 1 

            if chain_count > longest_chain: 
                longest_chain = chain_count 

        return longest_chain


             

            