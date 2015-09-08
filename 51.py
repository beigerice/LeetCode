class Solution(object):
    def solveNQueens(self, n):
        if n == 1:
            return [['Q']]
        if n >= 4:
            result = []
            def dfs(k,board):
                dic = {}
                for i in xrange(k):
                    dic[board[i]] = 1
                    if board[i]-k+i >= 0:
                        dic[board[i]-k+i] = 1
                    if board[i]+k-i <= n:
                        dic[board[i]+k-i] = 1
                for i in xrange(1,n+1):
                    if i not in dic:
                        board[k] = i
                        if k < n-1:
                            dfs(k+1,board)
                        else:
                            temp = []
                            for j in xrange(n):
                                temp.append('.'*(board[j]-1)+'Q'+'.'*(n-board[j]))
                            result.append(temp)
            dfs(0,[0]*n)
            return result
        else:
            return []

a = Solution()
print a.solveNQueens(5)
