class Solution(object):
    def solveSudoku(self, board):
        row = {}
        column = {}
        square = {}
        temp = []
        for i in xrange(9):
            row[i] = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            column[i] = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            square[i] = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}           
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != '.':
                    row[i][board[i][j]] = 1
                    column[j][board[i][j]] = 1
                    square[(i//3)*3+j//3][board[i][j]] = 1
                else:
                    temp.append([i,j])
        strlist = ['1','2','3','4','5','6','7','8','9']
        def dfs(idx):
            for i in strlist:
                if row[temp[idx][0]][i] == 0 and column[temp[idx][1]][i] == 0 and square[(temp[idx][0]//3)*3+temp[idx][1]//3][i] == 0:
                    if idx < len(temp)-1:
                        row[temp[idx][0]][i],column[temp[idx][1]][i],square[(temp[idx][0]//3)*3+temp[idx][1]//3][i] = 1,1,1
                        board[temp[idx][0]] = board[temp[idx][0]][:temp[idx][1]]+i+board[temp[idx][0]][temp[idx][1]+1:]
                        if dfs(idx+1):
                            return True
                        row[temp[idx][0]][i],column[temp[idx][1]][i],square[(temp[idx][0]//3)*3+temp[idx][1]//3][i] = 0,0,0
                        board[temp[idx][0]] = board[temp[idx][0]][:temp[idx][1]]+'.'+board[temp[idx][0]][temp[idx][1]+1:]
                    else:
                        board[temp[idx][0]] = board[temp[idx][0]][:temp[idx][1]]+i+board[temp[idx][0]][temp[idx][1]+1:]
                        return True
        dfs(0)
        print board

a = Solution()
a.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
