class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
                    j -= 1
                else:
                    while nums[j] == val and i <= j:
                        j -= 1
            else:
                i += 1
        print nums
        return i

a = Solution()
print a.removeElement([3,3,2],1)
            
