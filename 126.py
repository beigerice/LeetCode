class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        refer = {}
        temp = [{beginWord},{endWord}]
        result = [1,1]
        flag,identifier = 1,0
        wordlist.remove(beginWord)
        wordlist.remove(endWord)
        while temp[0] and temp[1] and flag:
            if len(temp[0]) > len(temp[1]):
                identifier = 1-identifier
                temp.reverse()
                result.reverse()
            new = set()
            for word in temp[0]:
                for i in xrange(len(beginWord)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            newWord = word[:i]+j+word[i+1:]
                            if newWord in temp[1] or newWord in wordlist:
                                if identifier:
                                    k,v = word,newWord
                                else:
                                    k,v = newWord,word
                                if k not in refer:
                                    refer[k] = set()
                                refer[k].add(v)
                                if newWord in temp[1]:
                                    flag = 0
                                elif newWord in wordlist:
                                    new.add(newWord)
            for w in new:
                if w in wordlist:
                    wordlist.remove(w)
            temp[0] = new
            result[0] += 1
        cnt = result[0]+result[1]-1
        result = []
        def dfs(temp):
            if len(temp) == cnt:
                if temp[-1] == beginWord:
                    temp.reverse()
                    result.append(temp)
            else:
                if temp[-1] in refer:
                    for word in refer[temp[-1]]:
                        dfs(temp+[word])
        dfs([endWord])
        return result

a = Solution()
print a.findLadders("red","tax",["ted","tex","red","tax","tad","den","rex","pee"])
