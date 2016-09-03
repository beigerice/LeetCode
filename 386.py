class Solution(object):
    def lexicalOrder(self, n):
        def dfs(start,n,res):
            for i in xrange(start,start+10):
                if i<= n and len(res) < n:
                    res.append(i)
                    if i * 10 <= n: dfs(i*10,n,res)
        res = []
        dfs(1,n,res)
        return res
