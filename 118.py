class Solution:
    def generate(self, numRows):
        result = []
        for i in xrange(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                temp = [0]*(i+1)
                temp[0] = 1
                temp[-1] = 1
                for j in xrange(1,i):
                    temp[j] = result[i-1][j-1]+result[i-1][j]
                result.append(temp)
        return result

a = Solution()
print a.generate(10)
