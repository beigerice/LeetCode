class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2147483647
        int_min = -2147483648
        str = str.strip()
        if not str:
            return 0
        sign, i = 1, 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            num = num*10+ord(str[i])-ord('0')
            if num > int_max:
                break
            i += 1
        return min(max(sign*num, int_min), int_max)        
