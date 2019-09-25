#problem 1011 / capacity to ship packages within D Days
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def can(x):
            count = 1
            ship = 0
            for w in weights:
                if ship + w > x:
                    ship = w
                    count += 1
                else:
                    ship += w
            return count <= D
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = (lo+hi)//2
            if can(mid):
                hi = mid
            else:
                lo = mid+1
        return lo