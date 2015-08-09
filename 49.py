class Solution:
    def anagrams(self, strs):
        temp = {}
        for string in strs:
            temp[tuple(sorted(string))] = temp.get(tuple(sorted(string)),[])+[string]
        result = []
        for v in temp.values():
            if len(v) > 1:
                result.extend(v)
        return result
        
