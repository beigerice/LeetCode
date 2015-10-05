class Solution:
    def findKthLargest(self, nums, k):
        def bs(n):
            low = 0
            high = k-1
            while low <= high:
                mid = (low+high)//2
                if result[mid] < n:
                    low = mid+1
                elif result[mid] > n:
                    high = mid-1
                else:
                    return mid
            return low
        result = [0]*k
        for i in xrange(k):
            result[i] = nums[i]
        result.sort()
        for i in xrange(k,len(nums)):
            if nums[i] > result[0]:
                idx = bs(nums[i])
                result.insert(bs(nums[i]),nums[i])
                result.pop(0)
        return result[0]       
