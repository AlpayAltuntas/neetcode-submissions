class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

# find out which array it could even be in 

# binary search that array
        target_array, l, r = -1, 0, len(matrix[0]) - 1
        for i, j in enumerate(matrix):
            if j[0] <= target <= j[-1]:
                target_array = i
                break
        
        while l <= r:
            middle = l + (r - l) // 2
            if target > matrix[target_array][middle]:
                l = middle + 1
            elif target < matrix[target_array][middle]:
                r = middle - 1
            else:
                return True
        return False
        
        