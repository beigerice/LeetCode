class Solution(object):
    def largestRectangleArea(self, height):
        result = 0
        stack = [[0,-1]]
        for i in xrange(len(height)):
            if height[i] >= stack[-1][0]:
                stack.append([height[i],i])
            else:
                while height[i] < stack[-1][0]:
                    result = max(result,stack[-1][0]*(i-stack[-1][1]))
                    temp = stack.pop()
                stack.append([height[i],temp[1]])
        for i in xrange(len(stack)):
            result = max(result,stack[i][0]*(len(height)-stack[i][1]))
        return result

a = Solution()
print a.largestRectangleArea([1,3,2,7,5,8,4,9])
