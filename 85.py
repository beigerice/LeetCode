class Solution(object):
    def maximalRectangle(self, matrix):
        toreturn = 0
        if not matrix:
            return 0
        m = [0]*len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '1':
                    m[j] += 1
                else:
                    m[j] = 0
            toreturn = max(toreturn,self.largestRectangleArea(m))
        return toreturn
                    
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
