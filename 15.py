class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0)+1
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if -nums[i]-nums[j] in dic:
                    if -nums[i]-nums[j] > nums[j]:
                        result.append([nums[i],nums[j],-nums[i]-nums[j]])
                    elif -nums[i]-nums[j] == nums[j]:
                        if nums[j] != 0:
                            if dic[nums[j]] >= 2:
                                result.append([nums[i],nums[j],-nums[i]-nums[j]])
                        else:
                            if dic[0] >= 3:
                                result.append([0,0,0])
        return result
