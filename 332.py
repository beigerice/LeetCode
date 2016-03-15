class Solution(object):
    def findItinerary(self, tickets):
        temp = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            temp[a] += b,
        result = []
        def visit(city):
            while temp[city]:
                visit(temp[city].pop())
            result.append(city)
        visit('JFK')
        return result[::-1]
