class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        temp = 0
        result = len(nums)
        i = 0
        j = 0
        while temp < s:
            if j == len(nums):
                return 0
            temp += nums[j]
            j += 1
        if j == len(nums) and temp == s:
            return j
        else:
            while j <= len(nums):
                while temp >= s:
                    temp -= nums[i]
                    i += 1
                result = min(result,j-i+1)
                print i,j
                while temp < s:
                    if j == len(nums):
                        return result                        
                    temp += nums[j]
                    j += 1

a = Solution()
print a.minSubArrayLen(11,[1,2,3,4,5])
            
                    
                    
