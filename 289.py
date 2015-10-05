class Solution(object):
    def gameOfLife(self, board):
        def count(x,y):
            cnt = 0
            for a,b in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                if a >= 0 and a <= len(board)-1 and b >= 0 and b <= len(board[0])-1 and board[a][b] == 1:
                    cnt += 1
            return cnt
        result = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 0  and count(i,j) == 3:
                    result.append([i,j])
                if board[i][j] == 1:
                    if count(i,j) < 2 or count(i,j) > 3:
                        result.append([i,j])
        for x in result:
            board[x[0]][x[1]] = 1-board[x[0]][x[1]]
