class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        else:
            tank = 0
            i = 0
            result = 0
            while True:
                tank += gas[i]-cost[i]
                if i == len(gas)-1:
                    return result                
                i += 1
                if tank < 0:
                    tank = 0
                    result = i

a = Solution()
print a.canCompleteCircuit([0,1,0,3],[1,1,1,1])
