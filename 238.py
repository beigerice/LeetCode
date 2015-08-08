class Solution:
    def productExceptSelf(self, nums):
        result = [1]
        product1 = 1
        for i in xrange(1,len(nums)):
            product1 *= nums[i-1]
            result.append(product1)
        product2 = 1
        for i in xrange(len(nums)-2,-1,-1):
            product2 *= nums[i+1]
            result[i] *= product2
        return result
                        

a = Solution()
print a.productExceptSelf([1,2,3,4])
