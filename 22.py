class Solution(object):
    def generateParenthesis(self, n):
        result = [[1,'(']]
        if n == 0:
            return []
        for i in xrange(2*n-1):
            for j in xrange(len(result)):
                if result[j][0] < n:
                    if 2*result[j][0] > len(result[j][1]):
                        result.append([result[j][0],result[j][1]+')'])                      
                    result[j][0] += 1
                    result[j][1] += '('                  
                else:
                    result[j][1] += ')'
        toreturn = []
        for i in result:
            toreturn.append(i[1])
        return toreturn

a = Solution()
print a.generateParenthesis(3)
        
