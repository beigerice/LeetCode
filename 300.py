class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 0
        temp = [nums[0]]
        for i in xrange(1,len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                low, high = 0, len(temp)
                while low < high:
                    mid = (low+high)//2
                    if temp[mid] < nums[i]:
                        low = mid+1
                    else:
                        high = mid
                temp[low] = min(temp[low],nums[i])
        return len(temp)
