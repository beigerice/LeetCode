class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        else:
            temp = [triangle[0][0]+triangle[1][0],triangle[0][0]+triangle[1][1]]
        for i in xrange(2,len(triangle)):
            start = temp[0]+triangle[i][0]  
            end = temp[-1]+triangle[i][-1]           
            for j in xrange(1,i):
                temp[j-1] = min(temp[j-1],temp[j])+triangle[i][j]
            temp.insert(0,start)
            temp[-1] = end
            print temp
        return min(temp)

a = Solution()
print a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
                
