class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        bfs = []
        for c in coins:
            bfs.append(c)
        visited = [True]+[False]*amount
        result = 0
        while bfs:
            result += 1
            temp = []
            for x in bfs:
                if x == amount:
                    return result
                for c in coins:
                    if x+c <= amount:
                        if not visited[x+c]:
                            temp.append(x+c)
                            visited[x+c] = True
            bfs = temp
        return -1
