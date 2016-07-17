class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def dfs(preVal,curVal,num,preExp,curExp):
            if num == '' and preVal+curVal == target:
                res.append(preExp+curExp)
                return
            for i in range(1,len(num)+1):
                dfs(preVal+curVal,int(num[:i]),num[i:],preExp+curExp,'+'+num[:i])
                dfs(preVal+curVal,-int(num[:i]),num[i:],preExp+curExp,'-'+num[:i])
                dfs(preVal,curVal*int(num[:i]),num[i:],preExp,curExp+'*'+num[:i])
                if num[0] == '0':
                    break
        for i in range(1,len(num)+1):
            dfs(0,int(num[:i]),num[i:],'',num[:i])
            if num[0] == '0':
                break
        return res
