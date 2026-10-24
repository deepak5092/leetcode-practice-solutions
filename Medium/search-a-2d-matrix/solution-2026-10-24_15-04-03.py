class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            mid_elem = matrix[row][col]
            
            if mid_elem == target:
                return True
            elif mid_elem > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False