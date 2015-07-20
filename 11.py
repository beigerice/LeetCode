##class Solution:
##    def maxArea(self, height):
##        result = 0
##        temp = enumerate(height)
##        temp = sorted(temp,key=lambda x:x[1],reverse=True)
##        m1 = temp[0][0]
##        m2 = temp[0][0]
##        for i in xrange(1,len(height)):
##            if result > temp[i][1]*(len(height)-1):
##                break
##            result = max(temp[i][1]*abs(temp[i][0]-m1),temp[i][1]*abs(temp[i][0]-m2),result)
##            m1 = max(temp[i][0],m1)
##            m2 = min(temp[i][0],m2)            
##        return result

class Solution:
    def maxArea(self, height):
        result = 0
        i = 0
        j = len(height)-1
        m = 0
        while i <= j:
            if min(height[i],height[j]) > m:
                if result < min(height[i],height[j])*(j-i):
                    result = min(height[i],height[j])*(j-i)
                    m = min(height[i],height[j])
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result 

a = Solution()
test = []
for i in xrange(1,15000):
    test.append(i)
print a.maxArea(test)
