class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def dp(begin,end):
            if (begin,end) not in cache:
                if begin == end:
                    cache[(begin,end)] = 0
                elif end - begin == 1:
                    cache[(begin,end)] = begin
                elif end - begin == 2:
                    cache[(begin,end)] = begin+1
                else:
                    temp = []
                    for i in range(begin+1,end):
                        temp.append(i+max(dp(begin,i-1),dp(i+1,end)))
                    cache[(begin,end)] = min(temp)
            return cache[(begin,end)]
        return dp(1,n)
