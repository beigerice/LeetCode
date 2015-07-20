class Solution:
    def largestRectangleArea(self, height):
        result = 0
        temp = []
        temp.append([height[0]])
        for i in xrange(1,len(height)):
            for j in temp:
                if height[i] >= j[0]:
                    j.append(height[i])
                else:
                    print temp
                    result = max(result,j[0]*len(j))
                    temp.remove(j)
            temp.append([height[i]])
        temp = []
        temp.append([height[-1]])
        for i in xrange(len(height)-1,-1,-1):
            for j in temp:
                if height[i] >= j[0]:
                    j.append(height[i])
                else:
                    print temp
                    result = max(result,j[0]*len(j))
                    temp.remove(j)
            temp.append([height[i]])
        return result

a = Solution()
test = []
for i in xrange(1500):
    test.append(i)
print a.largestRectangleArea([1,3,2,7,5,8,4,9])
