class Solution:
    def isValidSudoku(self, board):
        for i in xrange(9):
            temp = {'.':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0} 
            for j in xrange(9):
                temp[board[i][j]] += 1
            for k in xrange(1,10):
                if temp[str(k)] > 1:
                    return False
        for i in xrange(9):
            temp = {'.':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}        
            for j in xrange(9):
                temp[board[j][i]] += 1
            for k in xrange(1,10):
                if temp[str(k)] > 1:
                    return False
        for a in xrange(3):
            for b in xrange(3):
                temp = {'.':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
                for i in xrange(3*a,3*a+3):                
                    for j in xrange(3*b,3*b+3):
                        temp[board[i][j]] += 1
                for k in xrange(1,10):
                    if temp[str(k)] > 1:
                        return False
        return True

a = Solution()
print a.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])
        
