class Solution(object):
    def countBits(self, num):
        result = [0,1]
        x = 1
        temp = 2**x
        if num == 0:
            return [0]
        elif num == 1:
            return result
        else:
            idx = 0
            for i in range(2,num+1):
                if temp == 0:
                    idx = 0
                    x += 1
                    temp = 2**x
                result.append(1+result[idx])
                idx += 1
                temp -= 1
            return result
