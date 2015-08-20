class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
        for i in xrange(1,n):
            nxt = min(nxt2,nxt3,nxt5)
            ugly.append(nxt)
            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2]*2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3]*3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5]*5
        return ugly[-1]

a = Solution()
print a.nthUglyNumber(17)
