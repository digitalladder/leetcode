#problem 1042 / flower planting with no adjacent
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0]*N
        g = [[] for i in range(N)]
        for x,y in paths:
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        for i in range(N):
            res[i] = ({1,2,3,4}-{res[n] for n in g[i]}).pop()
        return res