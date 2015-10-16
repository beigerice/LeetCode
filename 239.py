class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        result = [max(nums[:k])]
        idx = nums.index(result[0])
        heap = [idx]
        for i in xrange(idx+1,len(nums)):
            if i-heap[0] >= k:
                del heap[0]
            if nums[i] < nums[heap[-1]]:
                heap.append(i)
            else:
                while heap and nums[i] >= nums[heap[-1]] and i-heap[-1] <= k:
                    heap.pop()
                heap.append(i)
            if i >= k:
                result.append(nums[heap[0]])
        return result
