import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        nxt = []
        for i in xrange(len(primes)):
            heapq.heappush(nxt,(primes[i],0,i))
        for i in xrange(1, n):
            ugly.append(nxt[0][0])
            while nxt and nxt[0][0] == ugly[-1]:
                temp = heapq.heappop(nxt)
                heapq.heappush(nxt,(ugly[temp[1]+1]*primes[temp[2]],temp[1]+1,temp[2]))
        return ugly[-1]           
