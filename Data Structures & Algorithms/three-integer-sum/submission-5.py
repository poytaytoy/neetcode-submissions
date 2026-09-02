class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        
        index_cap = len(numbers)
        
        solution_list = []

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
                pair = solution_list.append([left, right])
                right -= 1

        return solution_list 
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution_list = set()
        stuff = {}

        for i in range(0, len(nums)): 
            
            if nums[i] > 0: 
                break

            target = -nums[i]
            
            for result in self.twoSum(nums[i + 1 :], target):
                solution_list.add(tuple([nums[i], nums[result[0] + i + 1], nums[result[1] + i + 1]]))
                
            
        return list(solution_list)

        



