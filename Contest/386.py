class Solution(object):
    def lexicalOrder(self, n):
        res = []
        def print_numbers(k, n):
            for i in range (0, 10):
                if (k+i)<= n:
                    res.append(k+i)
                    print_numbers((k+i)*10, n)
        for k in range (1, 10):
            if k <= n:
                res.append(k)
                print_numbers(k*10, n)
        return res
            
a = Solution()
print a.lexicalOrder(50)
