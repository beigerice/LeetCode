class Solution:
    def trap(self, height):
        if len(height) <= 2:
            return 0
        result = 0
        idx = -1
        valley = []
        peak = height[0]        
        for i in xrange(1,len(height)):
            if height[i] >= peak:
                for j in xrange(len(valley)):
                    result += peak-valley[j]
                valley = []
                peak = height[i]
                idx = i
            else:
                valley.append(height[i])
        valley = []
        peak = height[-1]        
        for i in xrange(len(height)-2,idx-1,-1):
            if height[i] >= peak:
                for j in xrange(len(valley)):
                    result += peak-valley[j]
                valley = []
                peak = height[i]
            else:
                valley.append(height[i])                
        return result

a = Solution()
print a.trap([1,2,1])

