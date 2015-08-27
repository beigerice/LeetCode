class Solution(object):
    def findWords(self, board, words):
        def dfs(x,y,word):
            if len(word) == 0: return True
            if x > 0 and temp_board[x-1][y] == word[0]:
                temp,temp_board[x][y] = temp_board[x][y],'#'
                if dfs(x-1,y,word[1:]):
                    return True
                temp_board[x][y] = temp
            if y > 0 and temp_board[x][y-1] == word[0]:
                temp,temp_board[x][y] = temp_board[x][y],'#'
                if dfs(x,y-1,word[1:]):
                    return True
                temp_board[x][y] = temp
            if x < len(temp_board)-1 and temp_board[x+1][y] == word[0]:
                temp,temp_board[x][y] = temp_board[x][y],'#'
                if dfs(x+1,y,word[1:]):
                    return True
                temp_board[x][y] = temp
            if y < len(temp_board[0])-1 and temp_board[x][y+1] == word[0]:
                temp,temp_board[x][y] = temp_board[x][y],'#'
                if dfs(x,y+1,word[1:]):
                    return True
                temp_board[x][y] = temp
        result = []                
        for word in words:
            temp_board = board
            for i in xrange(len(temp_board)):
                for j in xrange(len(temp_board[0])):
                    if temp_board[i][j] == word[0]:
                        if dfs(i,j,word[1:]):
                            result.append(word)
        return result

a = Solution()
print a.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']],["oath","pea","eat","rain"])
