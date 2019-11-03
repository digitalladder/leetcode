#problem 1217 / play with chips
class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        even,odd = 0,0
        for chip in chips:
            if chip%2 == 0:
                even += 1
            else:
                odd += 1
        return min(even,odd)