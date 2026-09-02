class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index_cap = len(numbers)
        
        pair = [-1001, -1001]

        for i in range(0, index_cap):
            if (i >= index_cap):
                break

            saver = numbers[i]
            
            end_loop = False 
        
            for j in range(index_cap - 1, i, -1):
                bum = numbers[j] + saver

                if bum > target: 
                    index_cap = j

                if bum < target: 
                    break

                if bum == target: 
                    pair = [i + 1, j + 1]
                    end_loop = True 
                    break; 
            
            if end_loop: 
                break

        return pair 