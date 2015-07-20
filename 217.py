class Solution:
    def containsDuplicate(self, nums):
        result = {}
        for num in nums:
            result[num] = result.get(num,0)+1
            if result[num] >= 2:
                return True
        return False
