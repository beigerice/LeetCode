class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        sList = list(s)
        i = 0
        j = len(sList)-1
        while i < j:
            if sList[i] not in vowels:
                i += 1
            else:
                if sList[j] not in vowels:
                    j -= 1
                else:
                    sList[i],sList[j] = sList[j],sList[i]
                    i += 1
                    j -= 1
        return ''.join(sList)
