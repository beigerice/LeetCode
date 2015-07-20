from math import ceil,floor

class Solution:
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        else:
            temp = []
            a, b = min(num), max(num)
            size = int(ceil(float(b-a)/(len(num)-1)))
            for i in xrange((b-a)//size+1):
                temp.append([None,None])
            for k in num:
                j = temp[(k-a)//size]
                j[0] = k if j[0] is None else min(j[0],k)
                j[1] = k if j[1] is None else max(j[1],k)
            temp = [j for j in temp if j[0] is not None]
            return max(temp[i][0]-temp[i-1][1] for i in range(1,len(temp)))

a = Solution()
print a.maximumGap([1,1,1,1,1,5,5,5,5,5])
