class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftRow, rightRow = 0, len(matrix) - 1

        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2

            if matrix[midRow][0] > target:
                rightRow = midRow - 1
            
            elif matrix[midRow][len(matrix[0]) - 1] < target:
                leftRow = midRow + 1

            else:

                leftCol, rightCol = 0, len(matrix[0]) - 1
                while leftCol <= rightCol:
                    mid = (leftCol + rightCol) // 2

                    if matrix[midRow][mid] == target:
                        return True
                    elif matrix[midRow][mid] < target:
                        leftCol = mid + 1
                    else:
                        rightCol = mid - 1

                return False

        return False