class Solution:
    def nextPermutation(self, num):
        for i in xrange(len(num)-2,-1,-1):
            if num[i] < num[i+1]:
                for j in xrange(len(num)-1,i,-1):
                    if num[j] > num[i]:
                        num[i],num[j] = num[j],num[i]
                        break
                num[i+1:] = num[i+1:][::-1]
                break
        else:
            num.reverse()
        print num

a = Solution()
a.nextPermutation([1,3,2])
