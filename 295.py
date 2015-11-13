import bisect
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        bisect.insort(self.nums, num)

    def findMedian(self):
        nums = self.nums
        if len(nums) % 2 == 0:
            return (nums[len(nums)/2] + nums[len(nums)/2-1]) / 2.0
        else:
            return nums[len(nums)/2]
