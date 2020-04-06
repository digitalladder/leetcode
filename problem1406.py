#problem 1406 / stone game III
# dp
#dp[i] means, if we ignore before A[i],what's the highest score that Alex can win over the Bob
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [float('-inf')]*(n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            take = 0
            for k in range(0,3):
                if i+k < n:
                    take += stoneValue[i+k]
                    dp[i] = max(dp[i],take-dp[i+k+1])
        print(dp)
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'

# approach 2
# dp[i] represent the maximum score one can get if he/she takes stones first at the position i
# dp[i] = max(dp[i], suffixSum[i]-suffixSum[k+1] + suffixSum[k+1] - dp[k+1]) = max(dp[i], suffixSum[i] - dp[k+1])，
# for k = i, i+1, i+2
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        suffixSum = [0 for _ in range(n+1)]
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1] + stoneValue[i]
        for i in range(n-1, -1, -1):
            dp[i] = stoneValue[i] + suffixSum[i+1] - dp[i+1]
            for k in range(i+1, min(n, i+3)):
                dp[i] = max(dp[i], suffixSum[i] - dp[k+1])
        if dp[0]*2 == suffixSum[0]:
            return "Tie"
        elif dp[0]*2 > suffixSum[0]:
            return "Alice"
        else:
            return "Bob"