class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(start,n,interval,d):
            if n == 1:
                return start
            if n == 2:
                if d == 'l':
                    return start+interval
                else:
                    return start
            if d == 'l':
                return dp(start+interval,n//2,interval*2,'r')
            else:
                if n%2 == 1:
                    return dp(start+interval,n//2,interval*2,'l')
                else:
                    return dp(start,n//2,interval*2,'l')
        return dp(1,n,1,'l')
