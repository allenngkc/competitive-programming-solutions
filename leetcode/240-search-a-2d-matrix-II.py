class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = 0, len(matrix[0])-1
        while rows < len(matrix) and cols >= 0:
            if matrix[rows][cols] > target:
                cols -= 1
            elif matrix[rows][cols] < target:
                rows += 1
            else:
                return True
        return False