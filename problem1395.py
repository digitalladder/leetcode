#problem 1395 / count number of teams
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        ascend = [[0]*n for i in range(4)]
        decend = [[0]*n for i in range(4)]
        res = 0
        for i in range(n):
            ascend[1][i] = 1
            decend[1][i] = 1
        for j in range(2,4):
            for r in range(1,n):
                for l in range(0,r):
                    if rating[l] < rating[r]:
                        ascend[j][r] += ascend[j-1][l]
                    if rating[l] > rating[r]:
                        decend[j][r] += decend[j-1][l]
                if j == 3:
                    res += (ascend[j][r]+decend[j][r])
        return res