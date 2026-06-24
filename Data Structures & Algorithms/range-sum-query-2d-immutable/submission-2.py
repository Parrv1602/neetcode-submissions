class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        (row1, col1) = upper left corner
        (row2, col2) = lower right corner
        '''
        result = 0
        '''
        What if I go through arrays in the matrix via a for loop, and sum up only the specific elements
        that are within range
        '''
        temp_index = -1
        
        for row_num in range(row1, row2+1): #Last row is exclusive
            matrix_row = self.matrix[row_num]
            result += sum(matrix_row[col1: col2 + 1])
            
        
        return result
                        
        

            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)