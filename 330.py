class Solution(object):
    def minPatches(self, nums, n):
        result = 0
        c = 1
        temp = 0
        for num in nums:
            if num > c:
                while num > c:
                    temp += c
                    result += 1
                    c = temp+1
                    if c > n:
                        return result
            temp += num
            c = temp+1
            if c > n:
                return result
        if c <= n:
            while c <= n:
                temp += c
                result += 1
                c = temp+1
        return result
