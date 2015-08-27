class Solution(object):
    def exist(self, board, word):
        def dfs(x,y,word):
            if len(word) == 0: return True
            if x > 0 and board[x-1][y] == word[0]:
                temp,board[x] = board[x],board[x][:y]+'#'+board[x][y+1:]
                if dfs(x-1,y,word[1:]):
                    return True
                board[x] = temp
            if y > 0 and board[x][y-1] == word[0]:
                temp,board[x] = board[x],board[x][:y]+'#'+board[x][y+1:]
                if dfs(x,y-1,word[1:]):
                    return True
                board[x] = temp
            if x < len(board)-1 and board[x+1][y] == word[0]:
                temp,board[x] = board[x],board[x][:y]+'#'+board[x][y+1:]
                if dfs(x+1,y,word[1:]):
                    return True
                board[x] = temp
            if y < len(board[0])-1 and board[x][y+1] == word[0]:
                temp,board[x] = board[x],board[x][:y]+'#'+board[x][y+1:]
                if dfs(x,y+1,word[1:]):
                    return True
                board[x] = temp
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,word[1:]):
                        return True
        return False           
                

a = Solution()
print a.exist(["aa"], "aa")
