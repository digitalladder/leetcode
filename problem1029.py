#problem 1029 / two city scheduling
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x : x[0]-x[1])
        n = len(costs)
        total = 0
        for i in range(n):
            if i < n//2:
                total += costs[i][0]
            else:
                total += costs[i][1]
        return total