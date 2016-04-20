class Solution(object):
    def jump(self, nums):
        n, cur_max, next_max, steps = len(nums), 0, 0, 0
        for i in xrange(n):
            if i > cur_max:
                steps += 1
                cur_max = next_max
                if cur_max >= n: break
            next_max = max(next_max, nums[i] + i)
        return steps
