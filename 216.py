class Solution(object):
    def combinationSum3(self, k, n):
        if k == 9:
            if n == 45:
                return [[1,2,3,4,5,6,7,8,9]]
            else:
                return []
        if k < 5:
            result = []
            for i in xrange(1,10):
                result.append([i])
            for cnt in xrange(2,k+1):
                temp = []
                for i in xrange(len(result)):
                    for j in xrange(result[i][-1]+1,10):
                        temp.append(result[i]+[j])
                result = temp
            toreturn = []
            for x in result:
                if sum(x) == n:
                    toreturn.append(x)
            return toreturn
        else:
            result = []
            for i in xrange(1,10):
                result.append([i])
            for cnt in xrange(2,10-k):
                temp = []
                for i in xrange(len(result)):
                    for j in xrange(result[i][-1]+1,10):
                        temp.append(result[i]+[j])
                result = temp
            toreturn = []
            for x in result:
                if sum(x) == 45-n:
                    toreturn.append(sorted(list(set([1,2,3,4,5,6,7,8,9])-set(x))))
            return toreturn
