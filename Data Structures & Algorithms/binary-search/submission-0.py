class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while (right - left >= 2):
            mid = left + (right - left) // 2

            if (target > nums[mid]):
                left = mid
            elif (target < nums[mid]):
                right = mid 
            else:
                return mid 
        
        if nums[right] == target: 
            return right 
        if nums[left] == target: 
            return left 

        return -1

        