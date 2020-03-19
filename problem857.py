#problem 857 / minimum cost to hire k workers
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        retio = [0]*n
        for i in range(n):
            retio[i] = float(wage[i])/quality[i]        # float()使计算结果保留小数点
        workers = sorted(zip(retio,quality,wage))
        candidate = []
        qsum = 0
        ans = float('inf')
        for r,q,w in workers:
            heapq.heappush(candidate,-q)
            qsum += q
            if len(candidate) > K:
                qsum += heapq.heappop(candidate)
            if len(candidate) == K:
                ans = min(ans,qsum*r)
        return ans