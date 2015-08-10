class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        if nums[0] < nums[-1]:
            return nums[0]
        while low < high-1:
            mid = (low+high)//2
            if nums[mid] < nums[-1] or nums[mid] < nums[0]:
                high = mid
            elif nums[mid] > nums[-1] or nums[mid] > nums[0]:
                low = mid
            else:
                return min(nums[low:high+1])
        return nums[high]

a = Solution()
print a.findMin([1])
