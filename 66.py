class Solution(object):
    def plusOne(self, digits):
        for i in xrange(len(digits)-1,-1,-1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
            else:
                digits[i] += 1
                break
        return digits

a = Solution()
print a.plusOne([0])
