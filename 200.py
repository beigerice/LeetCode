class Solution(object):
    def numIslands(self, grid):
        def dfs(x,y):
            for (a,b) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if a >= 0 and a <= len(grid)-1 and b >= 0 and b <= len(grid[0])-1 and grid[a][b] == '1':
                    grid[a][b] = '#'
                    dfs(a,b)
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i,j)
        return result
