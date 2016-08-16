from random import randint
from copy import deepcopy
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        temp = deepcopy(self.nums)
        for i in range(len(temp)-1,-1,-1):
            j = randint(0,i)
            if i != j:
                temp[i],temp[j] = temp[j],temp[i]
        return temp
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
