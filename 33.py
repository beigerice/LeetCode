class Solution:
    def search(self, nums, target):
        def bs(low,high):
            while low <= high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid+1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    return mid
        low = 0
        high = len(nums)-1
        while low < high-1:
            mid = (low+high)//2
            if nums[mid] < nums[-1]:
                high = mid
            elif nums[mid] > nums[-1]:
                low = mid
        idx = high
        result = [bs(0,idx),bs(idx,len(nums)-1)]
        for i in result:
            if i != None:
                return i
        return -1       
a = Solution()
print a.search([4,5,6,7,0,1,2],0)
