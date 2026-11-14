def search_sorted(nums, target: int, left, right) -> int:

    while (right - left > 1): 
        mid = (right + left) // 2
         
        if (nums[mid] > target): 
            right = mid 
        elif (nums[mid] < target): 
            left = mid 
        else:
            return mid 

    for i in range(left, right + 1): 
        if (nums[i] == target):
            return i

    return -1 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1 

        while (right - left > 1):
            mid = (right + left) // 2 

            if (nums[mid] > nums[left]):
                result = search_sorted(nums, target, left, mid)
                if (result != -1):
                    return result
                left = mid

            if (nums[mid] < nums[right]):
                result = search_sorted(nums, target, mid, right)
                if (result != -1):
                    return result
                right = mid
            
            if (nums[mid] < nums[left]):
                right = mid
            elif (nums[mid] > nums[right]):
                left = mid
        
        for i in range(left, right + 1): 
            if (nums[i] == target):
                return i

        return -1 

            

        
        