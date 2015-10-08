class Solution(object):
    def calculateMinimumHP(self, dungeon):
        temp = dungeon[:]
        for i in xrange(len(dungeon)-1,-1,-1):
            for j in xrange(len(dungeon[0])-1,-1,-1):
                if i == len(dungeon)-1:
                    if j == len(dungeon[0])-1:
                        temp[i][j] = max(1-dungeon[i][j],1)
                    else:
                        temp[i][j] = max(max(1,temp[i][j+1])-dungeon[i][j],1) 
                else:
                    if j == len(dungeon[0])-1:
                        temp[i][j] = max(max(1,temp[i+1][j])-dungeon[i][j],1)
                    else:
                        temp[i][j] = max(max(1,min(temp[i][j+1],temp[i+1][j]))-dungeon[i][j],1)
        return temp[0][0]
a = Solution()
print a.calculateMinimumHP()
