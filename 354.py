class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x:(x[0],-x[1]))
        temp = [envelopes[0]]
        for i in xrange(1,len(envelopes)):
            if envelopes[i][0] > temp[-1][0] and envelopes[i][1] > temp[-1][1]:
                temp.append(envelopes[i])
            elif envelopes[i][0] >= temp[-1][0] and envelopes[i][1] < temp[-1][1]:
                low, high = 0, len(temp)
                while low < high:
                    mid = (low+high)//2
                    if temp[mid][1] < envelopes[i][1]:
                        low = mid+1
                    else:
                        high = mid
                if temp[low][1] > envelopes[i][1]:
                    temp[low] = envelopes[i]
        return len(temp)
