class Solution(object):
    def letterCombinations(self, digits):
        dic = {'0':' ','1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return []
        result = [""]
        if not digits.isdigit():
            return result            
        for digit in digits:
            word = dic[digit]
            temp = []
            for i in word:
                for j in result:
                    temp.append(j+i)
            result = temp
        return result   

a = Solution()
print a.letterCombinations("234")
            
