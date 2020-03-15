#problem 1383 / maximum performance of a team
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        res,speedsum = 0,0
        for eff, speed in sorted(zip(efficiency,speed),reverse = 1):
            heapq.heappush(heap,speed)
            speedsum += speed
            if len(heap) > k:
                speedsum -= heapq.heappop(heap)
            res = max(res,speedsum*eff)
        return res%(10**9+7)