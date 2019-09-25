#problem 875 / koko eating bananas
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def possible(k): 
            h = 0
            for p in piles:
                h += (p-1)//k+1
            return h <= H
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo+hi)//2
            if possible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
                