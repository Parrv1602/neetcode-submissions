class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        General idea: Find the sum of the entire matrix in the __init__ function. Why? Because you only find 
        all the sums once and then have O(1) time complexity when calling sumRegion().

        You find the sum of all entries in the matrix as area of a rectangle (e.g.: moving to the next row, entry in this
        row is sum of elements above it and before it). The sum of elements in the same row will be the prefix. 
        But what about the first row, there aren't any rows above it to find the sum of rows as an area? To fix this issue,
        create a row of 0s above the sum Matrix and a column of 0s to the left of the sum Matrix.
        '''
        rows, cols = len(matrix), len(matrix[0])

        #Creating the sum matrix with a row of 0s above the top row and a row of 0s to the left of the leftmost column
        self.sumMatrix = [[0]*(cols+1) for i in range(rows+1)]

        for row in range(rows):
            prefix = 0
            for column in range(cols):
                prefix += matrix[row][column]
                #Since sum is calculated as a rectangle area, going up and down, the col is col+1 because
                #row+1 col+1 is where we want to add the sum of values, so the value above it is the sum of values ABOVE
                value_above_prefix = self.sumMatrix[row][column+1]

                #Why + 1? Because we want to avoid the top row of 0s and the leftmost column of 0s
                self.sumMatrix[row+1][column+1] = prefix + value_above_prefix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right_corner = self.sumMatrix[row2][col2]
        top_sum = self.sumMatrix[row1 - 1][col2]
        left_sum = self.sumMatrix[row2][col1 - 1]

        #The intersection of the top sum and the left column sum is subtracted twice, so re-add it
        intersection = self.sumMatrix[row1 - 1][col1 - 1]
        
        return bottom_right_corner - top_sum - left_sum + intersection


                        
        

            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)