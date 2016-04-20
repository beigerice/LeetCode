from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        sky = [[-1,0]]
        position = set()
        for building in buildings:
            if building[0] not in position:
                position.add(building[0])
            if building[1] not in position:
                position.add(building[1])
        live = []
        i = 0
        for t in sorted(position):
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live,[-buildings[i][2],buildings[i][1]])
                i += 1
            while live and live[0][1] <= t:
                heappop(live)
            h = -live[0][0] if live else 0
            if h != sky[-1][1]:
                sky.append([t,h])
        return sky[1:]
                
