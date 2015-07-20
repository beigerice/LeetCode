class Solution:
    def climbStairs(self, n):
        temp = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in xrange(n-2):
                temp.append(temp[i]+temp[i+1])
            return temp[-1]            
            
a = Solution()
print a.climbStairs(4)
