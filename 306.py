class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(1,len(num)):
            for j in xrange(i+1,len(num)):
                if num[i] == '0'and j-i > 1:
                    continue
                idx1,idx2,idx3 = 0,i,j
                while idx3 <= len(num):
                    temp = int(num[idx1:idx2])+int(num[idx2:idx3])
                    if temp != int(num[idx3:idx3+len(str(temp))]) or num[idx3] == '0':
                        break
                    idx1,idx2,idx3 = idx2,idx3,idx3+len(str(temp))
                    if idx3 == len(num):
                        return True
        return False
