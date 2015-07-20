class Solution:
    def countAndSay(self, n):
        seq = [str(1)]
        for i in xrange(n-1):
            temp = [seq[i][0],0]
            toadd = ''
            for digit in seq[i]:
                if digit != temp[0]:
                    toadd += str(temp[1])+temp[0]
                    temp[0] = digit
                    temp[1] = 1
                else:
                    temp[1] += 1
            toadd += str(temp[1])+temp[0]
            seq.append(toadd)
        return seq[-1]

a = Solution()
print a.countAndSay(6)
            
