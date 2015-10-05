class Solution(object):
    def solve(self, board):
        dic = {}
        def bfs(x,y):
            if (x,y) not in dic:
                dic[(x,y)] = 1
                if x > 1:
                    if board[x-1][y] == 'O':
                        bfs(x-1,y)
                if x < len(board)-2:
                    if board[x+1][y] == 'O':
                        bfs(x+1,y)
                if y > 1:
                    if board[x][y-1] == 'O':
                        bfs(x,y-1)
                if y < len(board[0])-2:
                    if board[x][y+1] == 'O':
                        bfs(x,y+1)
        if len(board) > 2:
            for i in xrange(len(board[0])):
                if board[0][i] == 'O':
                    bfs(0,i)
                if board[len(board)-1][i] == 'O':
                    bfs(len(board)-1,i)
            for i in xrange(len(board)):
                if board[i][0] == 'O':
                    bfs(i,0)
                if board[i][len(board[0])-1] == 'O':
                    bfs(i,len(board[0])-1)
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if board[i][j] == 'O' and (i,j) not in dic:
                        board[i][j] = 'X'
