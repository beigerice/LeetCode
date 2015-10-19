class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        i = 0
        while i < len(nums)-2:
            j,k = i+1,len(nums)-1
            while j < k:
                if abs(result-target) > abs(nums[i]+nums[j]+nums[k]-target):
                    result = nums[i]+nums[j]+nums[k]                
                if nums[i]+nums[j]+nums[k] == target:
                    return target
                elif nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
            while i < len(nums)-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return result
