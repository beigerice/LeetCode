class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        temp = [0]*n
        temp[0] = grid[0][0]
        for i in xrange(1,n):
            temp[i] = temp[i-1]+grid[0][i]
        for i in xrange(1,m):
            temp[0] += grid[i][0]
            for j in xrange(1,n):
                temp[j] = min(temp[j-1],temp[j])+grid[i][j]
        return temp[-1]

a = Solution()
print a.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
