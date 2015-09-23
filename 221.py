class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        elif len(matrix) == 1:
            for i in matrix:
                if i == '1':
                    return 1
            return 0
        else:
            temp = [[0]*len(matrix[0]) for i in xrange(len(matrix))]
            result = [[0]*len(matrix[0]) for i in xrange(len(matrix))]            
            if matrix[0][0] == '1':
                temp[0][0] = [1,1]
                result[0][0] = 1
            else:
                temp[0][0] = [0,0]
            for i in xrange(1,len(matrix)):
                if matrix[i][0] == '1':
                    temp[i][0] = [1,temp[i-1][0][1]+1]
                    result[i][0] = 1
                else:
                    temp[i][0] = [0,0]
            for i in xrange(1,len(matrix[0])):
                if matrix[0][i] == '1':
                    temp[0][i] = [temp[0][i-1][0]+1,1]
                    result[0][i] = 1
                else:
                    temp[0][i] = [0,0]
            for i in xrange(1,len(matrix)):
                for j in xrange(1,len(matrix[0])):
                    if matrix[i][j] == '1':
                        temp[i][j] = [temp[i][j-1][0]+1,temp[i-1][j][1]+1]
                    else:
                        temp[i][j] = [0,0]       
            for i in xrange(1,len(matrix)):
                for j in xrange(1,len(matrix[0])):
                    if matrix[i][j] == '1':
                        result[i][j] = min(result[i-1][j-1],temp[i][j-1][0],temp[i-1][j][1])+1
            toreturn = 0
            for i in xrange(len(matrix)):
                for j in xrange(len(matrix[0])):
                    toreturn = max(toreturn,result[i][j])
            return toreturn**2
                    

a = Solution()
print a.maximalSquare([[1,1]])
