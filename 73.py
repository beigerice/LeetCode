class Solution:
    def setZeroes(self, matrix):
        for i in xrange(len(matrix)):
            flag = 0
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    for a in xrange(len(matrix)):
                        if a != i:
                            if matrix[a][j] != 0:
                                matrix[a][j] = '*'
                    if flag == 0:
                        for b in xrange(len(matrix[i])):
                            if matrix[i][b] != 0:
                                matrix[i][b] = '*'
                            flag = 1
##        for i in xrange(len(matrix)):
##            for j in xrange(len(matrix[i])):
##                if matrix[i][j] == 0:
##                    matrix[i] = [0]*len(matrix[i])
##                    break
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0

        print matrix

a = Solution()
a.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
