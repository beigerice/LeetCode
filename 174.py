class Solution:
    def calculateMinimumHP(self, dungeon):
        dungeon[0][0] = [max(1-dungeon[0][0],1),dungeon[0][0]]
        for i in xrange(1,len(dungeon[0])):
            if dungeon[0][i] >= 0 or dungeon[0][i-1][0]+dungeon[0][i-1][1]+dungeon[0][i] > 0:
                dungeon[0][i] = [dungeon[0][i-1][0],dungeon[0][i-1][1]+dungeon[0][i]]
            else:
                dungeon[0][i] = [dungeon[0][i-1][0]+1-dungeon[0][i-1][0]-dungeon[0][i-1][1]-dungeon[0][i],dungeon[0][i-1][1]+dungeon[0][i]]
        for i in xrange(1,len(dungeon)):
            if dungeon[i][0] >= 0 or dungeon[i-1][0][0]+dungeon[i-1][0][1]+dungeon[i][0] > 0:
                dungeon[i][0] = [dungeon[i-1][0][0],dungeon[i-1][0][1]+dungeon[i][0]]
            else:
                dungeon[i][0] = [dungeon[i-1][0][0]+1-dungeon[i-1][0][0]-dungeon[i-1][0][1]-dungeon[i][0],dungeon[i-1][0][1]+dungeon[i][0]]
        for i in xrange(1,len(dungeon)):
            for j in xrange(1,len(dungeon[0])):
                if dungeon[i-1][j][0] < dungeon[i][j-1][0]:
                    x = dungeon[i-1][j]
                elif dungeon[i-1][j][0] == dungeon[i][j-1][0]:
                    if dungeon[i-1][j][1] > dungeon[i][j-1][1]:
                        x = dungeon[i-1][j]
                    else:
                        x = dungeon[i][j-1]
                else:
                    x = dungeon[i][j-1]
                if dungeon[i][j] >= 0 or x[0]+x[1]+dungeon[i][j] > 0:
                    dungeon[i][j] = [x[0],x[1]+dungeon[i][j]]
                else: 
                    dungeon[i][j] = [x[0]+1-x[0]-x[1]-dungeon[i][j],x[1]+dungeon[i][j]]
        print dungeon
        return dungeon[-1][-1][0]        
                
a = Solution()
print a.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
