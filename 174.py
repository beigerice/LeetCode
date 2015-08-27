class Solution:
    def calculateMinimumHP(self, dungeon):
        d = dungeon
        d[0][0] = [[max(1-d[0][0],1),d[0][0]]]
        for i in xrange(1,len(d[0])):
            if d[0][i] >= 0 or d[0][i-1][0][0]+d[0][i-1][0][1]+d[0][i] > 0:
                d[0][i] = [[d[0][i-1][0][0],d[0][i-1][0][1]+d[0][i]]]
            else:
                d[0][i] = [[1-d[0][i-1][0][1]-d[0][i],d[0][i-1][0][1]+d[0][i]]]
        for i in xrange(1,len(d)):
            if d[i][0] >= 0 or d[i-1][0][0][0]+d[i-1][0][0][1]+d[i][0] > 0:
                d[i][0] = [[d[i-1][0][0][0],d[i-1][0][0][1]+d[i][0]]]
            else:
                d[i][0] = [[1-d[i-1][0][0][1]-d[i][0],d[i-1][0][0][1]+d[i][0]]]
        for i in xrange(1,len(d)):
            for j in xrange(1,len(d[0])):
                temp = []
                for k in d[i-1][j]:
                    if d[i][j] > 0 or k[0]+k[1]+d[i][j] > 0:
                        temp.append([k[0],k[1]+d[i][j]])
                    else:
                        temp.append([1-k[1]-d[i][j],k[1]+d[i][j]])
                for k in d[i][j-1]:
                    if d[i][j] > 0 or k[0]+k[1]+d[i][j] > 0:
                        temp.append([k[0],k[1]+d[i][j]])
                    else:
                        temp.append([1-k[1]-d[i][j],k[1]+d[i][j]])
                m = [temp[0][0],temp[0][1]]
                for k in xrange(1,len(temp)):
                    if temp[k][0] < m[0]:
                        m = [temp[k][0],temp[k][1]]
                d[i][j] = [m]
                for k in xrange(len(temp)):
                    if temp[k][0]+temp[k][1] > m[0]+m[1]:
                        d[i][j].append(temp[k])
        return d[-1][-1][0][0]
a = Solution()
print a.calculateMinimumHP()
