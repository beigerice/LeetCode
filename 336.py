class Solution(object):
    def palindromePairs(self, words):
        result = []
        refer1 = {}
        refer2 = {}
        sp = -1
        for i in range(len(words)):
            if words[i] == "":
                sp = i
            key_pre = words[i][::-1]
            refer1[key_pre] = i
            for j in range(1,len(words[i])):
                key = words[i][j:]
                if key not in refer2:
                    refer2[key] = []
                refer2[key].append(i)
        for i in range(len(words)):
            if sp != -1 and sp != i and words[i] == words[i][::-1]:
                result.append([i,sp])
                result.append([sp,i])
            key = words[i][::-1]
            if key in refer2:
                for idx in refer2[key]:
                    temp = words[i]+words[idx]
                    if temp == temp[::-1] and i != idx:
                        result.append([i,idx])
            for j in range(1,len(words[i])+1):
                if words[i][:j] in refer1:
                    idx = refer1[words[i][:j]]
                    temp = words[i]+words[idx]
                    if temp == temp[::-1] and i != idx:
                        result.append([i,idx])
        return result
