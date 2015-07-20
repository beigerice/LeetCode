import operator
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        temp = {}
        if obstacleGrid[0][0] == 0:
            temp[(0,0)] = 1
        else:
            temp[(0,0)] = 0
        for i in xrange(1,m):
            if obstacleGrid[0][i] == 0:
                temp[(0,i)] = temp[(0,i-1)]
            else:
                temp[(0,i)] = 0
        for i in xrange(1,n):
            if obstacleGrid[i][0] == 0:
                temp[(i,0)] = temp[(i-1,0)]
            else:
                temp[(i,0)] = 0
        for i in xrange(1,m):
            for j in xrange(1,n):
                if obstacleGrid[j][i] == 0:
                    temp[(j,i)] = temp[(j-1,i)]+temp[(j,i-1)]
                else:
                    temp[(j,i)] = 0
        return temp[(n-1,m-1)]

a = Solution()
print a.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
                    
