class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #hacer binary search vertical
        top, bottom = 0, len(matrix) - 1
        row = 0
        while top <= bottom:
            middle = (top + bottom) // 2
            #vertical search to check if the target falls between the first and last element of a row 
            #if so we found our row!
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = middle
                break
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle + 1
        else:
            # If we didn't find a potential row
            row = middle

        #Hacer binary search ya horizontal:) 
        left, right = 0, len(matrix[0])-1
        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] < target:
                left = m + 1
            elif matrix[row][m] > target:
                right = m - 1
            elif matrix[row][m] == target:
                return True
        return False