class Solution:
    def spiralOrder(self, matrix):
        def spiral(d,i,j):
            result.append(matrix[i][j])
            temp[i][j] = matrix[i][j]
            if d == 'right':
                if j == n-1 or temp[i][j+1] != '.':
                    d = 'down'
                    i += 1
                else: j += 1
            elif d == 'down':
                if i == m-1 or temp[i+1][j] != '.':
                    d = 'left'
                    j -= 1
                else: i += 1
            elif d == 'left':                
                if j == 0 or temp[i][j-1] != '.':
                    d = 'up'
                    i -= 1
                else: j -= 1
            elif d == 'up':
                if i == 0 or temp[i-1][j] != '.':
                    d = 'right'
                    j += 1
                else: i -= 1
            if len(result) < m*n:
                return spiral(d,i,j)
        result = []       
        if len(matrix) > 0:
            m = len(matrix)
            n = len(matrix[0])
            temp = [['.' for x in range(n)] for x in range(m)]             
            spiral('right',0,0)
        return result

a = Solution()
print a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
