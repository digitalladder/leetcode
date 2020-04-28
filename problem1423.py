#problem 1423 / maximum points you can obtain from cards
# sliding window
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        remain = n-k
        i,j = 0,remain
        tempval = 0
        for k in range(i,j):
            tempval += cardPoints[k]
        minimum = tempval
        while j < n:
            tempval -= cardPoints[i]
            tempval += cardPoints[j]
            i += 1
            j += 1
            minimum = min(minimum,tempval)
        return sum(cardPoints)-minimum