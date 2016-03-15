class Solution(object):
    def longestIncreasingPath(self, matrix):
        result = {}
        def dfs(x,y):
            if (x,y) in result:
                return result[(x,y)]
            temp = 0
            if x > 0:
                if matrix[x-1][y] > matrix[x][y]:
                    if (x-1,y) in result:
                        temp = max(temp,result[(x-1,y)]+1)
                    else:
                        temp = max(temp,dfs(x-1,y)+1)
            if x < len(matrix)-1:
                if matrix[x+1][y] > matrix[x][y]:
                    if (x+1,y) in result:
                        temp = max(temp,result[(x+1,y)]+1)
                    else:
                        temp = max(temp,dfs(x+1,y)+1)
            if y > 0:
                if matrix[x][y-1] > matrix[x][y]:
                    if (x,y-1) in result:
                        temp = max(temp,result[(x,y-1)]+1)
                    else:
                        temp = max(temp,dfs(x,y-1)+1)
            if y < len(matrix[0])-1:
                if matrix[x][y+1] > matrix[x][y]:
                    if (x,y+1) in result:
                        temp = max(temp,result[(x,y+1)]+1)
                    else:
                        temp = max(temp,dfs(x,y+1)+1)
            temp = max(1,temp)
            result[(x,y)] = temp
            return temp
        toreturn = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                toreturn = max(toreturn,dfs(i,j))
        return toreturn
