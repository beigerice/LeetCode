class Solution:
    def generateMatrix(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            result = [[0 for x in range(n)] for x in range(n)] 
            def spiral(d,i,j,m):
                result[i][j] = m
                m += 1
                if d == 'right':
                    j += 1
                    if j == n-1 or result[i][j+1] != 0:
                        d = 'down'
                elif d == 'down':
                    i += 1
                    if i == n-1 or result[i+1][j] != 0:
                        d = 'left'
                elif d == 'left':
                    j -= 1
                    if j == 0 or result[i][j-1] != 0:
                        d = 'up'
                elif d == 'up':
                    i -= 1
                    if i == 0 or result[i-1][j] != 0:
                        d = 'right'
                if m <= n*n:
                    return spiral(d,i,j,m)
            spiral('right',0,0,1)
            return result

a = Solution()
print a.generateMatrix(1)
            
