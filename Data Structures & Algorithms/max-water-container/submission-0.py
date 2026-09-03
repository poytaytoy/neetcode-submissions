class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAreas = -1 

        left = 0 
        right = len(heights) - 1

        while (left < right):
            volume = (right - left) * min(heights[left] , heights[right]) 

            if volume > maxAreas: 
                maxAreas = volume 

            if heights[right] > heights[left]: 
                left += 1
            else: 
                right -= 1

        return maxAreas

            