#problem 332 reconstruct itinerary
import collections
import heapq
#dfs
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)
        dfs('JFK')
        return route[::-1]

#dfs use heapq
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itin = [] # in reverse sequence
        if tickets:    
            dic = {}
            for from_city, to_city in tickets:
                if from_city not in dic:
                    dic[from_city] = []
                heapq.heappush(dic[from_city], to_city)            
            
            def dfs(city):
                if city in dic:
                    while dic[city]:
                        dfs(heapq.heappop(dic[city]))
                itin.append(city)
            
            dfs("JFK")               
        return itin[::-1]

#iterative
def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]
