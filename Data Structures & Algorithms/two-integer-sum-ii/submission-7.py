class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index_cap = len(numbers)
        
        pair = [-1001, -1001]

        left = 0 
        right = len(numbers) - 1

        while left < right: 
            bum = numbers[left] + numbers[right]

            if bum > target: 
                right -= 1
                continue 

            if bum < target: 
                left += 1
                continue 

            if bum == target: 
                pair = [left + 1, right + 1]
                break; 

        return pair 