class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        temp = [{beginWord},{endWord}]
        result = [1,1]
        while temp[0] and temp[1]:
            if len(temp[0]) > len(temp[1]):
                temp.reverse()
                result.reverse()
            new = set()
            for word in temp[0]:
                for i in xrange(len(beginWord)):
                    for j in string.lowercase:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord in temp[1]:
                            return result[0]+result[1]
                        if newWord in wordList:
                            new.add(newWord)
                            wordList.remove(newWord)
            temp[0] = new
            result[0] += 1
        return 0
