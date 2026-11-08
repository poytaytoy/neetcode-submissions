def itemAt(matrix, index):
    return matrix[index // len(matrix[0])][index % len(matrix[0])]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (len(matrix) == 0):
            return False 
        
        length = len(matrix) * len(matrix[0])

        left = 0; 
        right = length - 1;

        while (right - left >= 2):
            new_index = left + (right - left) // 2 

            if (itemAt(matrix, new_index) > target):
                right = new_index 
            elif (itemAt(matrix, new_index) < target):
                left = new_index
            else: 
                return True 

        for i in range(left, right + 1):
            if (itemAt(matrix, i) == target):
                return True

        return False

            