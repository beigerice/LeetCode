class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.accu = [0]
        self.diff = [0]*len(nums)
        for num in nums:
            self.accu += self.accu[-1]+num,
            

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        temp, self.nums[i] = self.nums[i], val
        self.diff[i] += val-temp

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j+1]-self.accu[i]+sum(self.diff[i:j+1])  
