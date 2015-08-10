class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        while low < high-1:
            mid = (low+high)//2
            if nums[mid] < nums[-1]:
                high = mid
            elif nums[mid] > nums[-1]:
                low = mid
        return min(nums[high],nums[low])

a = Solution()
print a.findMin([4,5,6,7,0,1,2])
