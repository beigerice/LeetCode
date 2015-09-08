class Solution(object):
    def totalNQueens(self, n):
        if n == 1:
            return 1
        if n >= 4:
            cnt = [0]
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
                            if dfs(k+1,board):
                                cnt[0] += 1
                        else:
                            return True
            dfs(0,[0]*n)
            return cnt[0]
        else:
            return 0

a = Solution()
print a.totalNQueens(9)
            
