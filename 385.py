class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s == '[]':
            return NestedInteger()
        if s[0] == '[':
            res = NestedInteger()
            idx = 1
            cnt = 0
            for i in range(1,len(s)-1):
                if s[i] == '[':
                    cnt += 1
                elif s[i] == ']':
                    cnt -= 1
                if s[i] == ',' and cnt == 0:
                    res.add(self.deserialize(s[idx:i]))
                    idx = i+1
            res.add(self.deserialize(s[idx:len(s)-1]))
            return res
        else:
            return NestedInteger(int(s))
