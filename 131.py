class Solution(object):
    def partition(self, s):
        refer = {}
        refer[0] = [[s[0]]]
        for i in range(1,len(s)):
            temp = []
            for j in refer[i-1]:
                temp.append(j+[s[i]])
            if s[:i+1] == s[:i+1][::-1]:
                temp.append([s[:i+1]])
            for j in range(1,i):
                if s[j:i+1] == s[j:i+1][::-1]:
                    for k in refer[j-1]:
                        temp.append(k+[s[j:i+1]])
            refer[i] = temp
        return refer[len(s)-1]
