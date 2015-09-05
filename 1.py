class Solution:
    def twoSum(self, num, target):
        temp = {n:pos for pos,n in enumerate(num) }
        for i,n in enumerate(num):
            if temp.get(target-n):
                return (i+1, temp[target-n]+1)
