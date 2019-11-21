#problem 1235 / maximum profit in job scheduling
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1      # [s, x] < [s + 1] < [s + 1, x]
            #it's comparing lists, [s+1] in dp, not s+1 in dp[0], so any [s+1, profit] will > [s+1], so the return index-1 corresponds to the last [s, profit]
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]