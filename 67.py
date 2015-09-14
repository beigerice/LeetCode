class Solution(object):
    def addBinary(self, a, b):
        if len(a) < len(b):
            a,b = b,a
        b = '0'*(len(a)-len(b))+b
        result = ''
        temp = 0
        for i in xrange(len(a)-1,-1,-1):
            if int(a[i])+int(b[i]) == 2:
                result = str(temp)+result
                temp = 1
            elif int(a[i])+int(b[i]) == 1:
                result = str(1-temp)+result
            else:
                result = str(temp)+result
                temp = 0
        if temp == 1:
            result = '1'+result
        return result

a = Solution()
print a.addBinary('10','11')
