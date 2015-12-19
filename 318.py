class Solution(object):
    def maxProduct(self, words):
        result = 0
        nums = []
        for word in words:
            nums.append(sum(1<<(ord(x)-ord('a')) for x in set(word)))
        for i in xrange(len(words)):
            for j in xrange(i+1,len(words)):
                if nums[i] & nums[j] == 0:
                    result = max(result,len(words[i])*len(words[j]))
        return result
