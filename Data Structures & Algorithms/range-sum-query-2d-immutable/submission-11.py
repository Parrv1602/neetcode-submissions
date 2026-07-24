class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        To achieve O(1) time complexity, no searching has to take place in sumRegion method.
        Perform all searching, etc, in the __init__ function once, make the matrix ready, then call the sumRegion for O(1) time complexity.
        Calculate the prefix sums for the matrix in the __init__ method.
        '''
        rows, cols = len(matrix), len(matrix[0]) 
        self.sumMatrix = [[0]*(cols+1) for i in range(rows+1)]

        for row in range(rows):
            prefix = 0
            for col in range(cols):
                prefix += matrix[row][col]
                val_above = self.sumMatrix[row][col+1] #Value above the value that we want to add. row, col is original with padded 0s

                self.sumMatrix[row+1][col+1] = prefix + val_above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        The values in the upper part of the rectangle depend on the values above them, i.e.: the row above.
        To find the sum of the rectangle, subtract the row above and the column beside (why? because the next value depends on the 
        value before (from the prefix), which is the column before).

        Bottom right entry in the sumMatrix has sums of all values til that column and row.
        '''
        #Since sumMatrix is padded by an extra row of 0s, then the rows and columns have to be incremented by 1
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        top_row = self.sumMatrix[row1-1][col2]
        left_column = self.sumMatrix[row2][col1-1]
        double_subtracted = self.sumMatrix[row1-1][col1-1]
        bottom_right = self.sumMatrix[row2][col2]
        return bottom_right - top_row - left_column + double_subtracted



                