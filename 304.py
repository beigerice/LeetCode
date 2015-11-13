class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.temp = matrix
        for i in xrange(len(matrix)):
            s = 0
            for j in xrange(len(matrix[0])):
                s += matrix[i][j]
                if i == 0:
                    self.temp[i][j] = s
                else:
                    self.temp[i][j] = s+self.temp[i-1][j]
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0:
            if col1 == 0:
                return self.temp[row2][col2]
            else:
                return self.temp[row2][col2]-self.temp[row2][col1-1]
        else:
            if col1 == 0:
                return self.temp[row2][col2]-self.temp[row1-1][col2]
            else:
                return self.temp[row2][col2]-self.temp[row2][col1-1]-self.temp[row1-1][col2]+self.temp[row1-1][col1-1]
