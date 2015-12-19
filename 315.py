class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def bs(x):
            low = 0
            high = len(temp)-1
            while low <= high:
                mid = (low+high)//2
                if temp[mid] >= x:
                    high = mid-1
                elif temp[mid] < x:
                    low = mid+1
            return low
        result = []
        temp = []
        for i in xrange(len(nums)-1,-1,-1):
            idx = bs(nums[i])
            temp.insert(idx,nums[i])
            result.insert(0,idx)
        return result

a = Solution()
print a.countSmaller([5,2,6,1,12,3,4,5,7,21,1,2,3])
