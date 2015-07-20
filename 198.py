class Solution:
    def rob(self, num):        
        if len(num) == 0:
            return 0
        elif len(num) == 1:
            return num[0]
        elif len(num) == 2:
            return max(num)
        else:
            result1 = num[0]
            result2 = max(num[0],num[1])
            for i in xrange(2,len(num)):
                result1,result2 = result2,max(result1+num[i],result2)
            return result2 

a = Solution()
test = []
for i in xrange(1,15001):
    test.append(i)
print a.rob([1,3,2,4,7,6])
