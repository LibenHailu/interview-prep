class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for r in range(len(matrix)):
            for i in range(1,len(matrix[r])):
                matrix[r][i] += matrix[r][i - 1]
        
        for r in range(1,len(matrix)):
            for j in range(len(matrix[r])):
                matrix[r][j] += matrix[r - 1][j]
        
        self.matrix = matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 == 0 and row1 == 0:
            return self.matrix[row2][col2]
        
        elif col1 == 0:
                    return (self.matrix[row2][col2] - self.matrix[row1 - 1][col2])
        
        elif row1 == 0:
            return (self.matrix[row2][col2] - self.matrix[row2][col1 -1])
        
        else:
            return (self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 -1] + self.matrix[row1 - 1][col1 - 1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)