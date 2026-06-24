class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        (row1, col1) = upper left corner
        (row2, col2) = lower right corner
        
        Find the sum of elements within the region in the matrix
        '''
        result = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                result += self.matrix[i][j]
        
        return result
        
        
            




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)