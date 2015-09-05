class Solution(object):
    def hIndex(self, citations):
        temp = [0]*(len(citations)+1)
        for i in xrange(len(citations)):
            if citations[i] <= len(citations):
                temp[citations[i]] += 1
            else:
                temp[-1] += 1
        toadd = temp[-1]
        for i in xrange(len(temp)-2,-1,-1):
            toadd += temp[i]
            temp[i] = toadd
        for i in xrange(len(temp)-1,-1,-1):
            if temp[i] >= i:
                return i

a = Solution()
print a.hIndex([1,3,1])
