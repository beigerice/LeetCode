class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        else:
            n = str(n)
            l = len(n)
            result = 0
            if int(n[0]) == 1:
                result += int(n[1:])+1
            elif int(n[0]) > 1:
                result += 10**(l-1)
            for i in xrange(1,l):
                if int(n[i]) == 0:
                    result += int(n[:i])*10**(l-1-i)                    
                elif int(n[i]) == 1:
                    if i == l-1:
                        result += int(n[:i])*10**(l-1-i)+1
                    else:
                        result += int(n[:i])*10**(l-1-i)+int(n[i+1:])+1
                else:
                    result += (int(n[:i])+1)*10**(l-1-i)            
            return result
                

a = Solution()
print a.countDigitOne(112)
