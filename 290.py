class Solution(object):
    def wordPattern(self, pattern, str):
        if len(pattern) == 0:
            return False
        dic = {}
        words = str.split()
        if len(words) != len(pattern):
            return False
        for i in xrange(len(words)):
            if pattern[i] not in dic:
                if words[i] not in dic.values():
                    dic[pattern[i]] = words[i]
                else:
                    return False
            else:
                if dic[pattern[i]] != words[i]:
                    return False
        return True
