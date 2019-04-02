#problem 70 /Climbing Stairs
#DP with memory
class Solution:
    def climbStairs(self, n):
        memo = [0]*(n+1)
        x = self.ways(0,n,memo)
        return x
    def ways(self,i,n,memo):
        if i>n:
            return 0
        if i == n:
            return 1
        if memo[i]>0:
            return memo[i]
        memo[i] = self.ways(i+1,n,memo)+self.ways(i+2,n,memo)
        return memo[i]
#DP with memory version 2 using hashing
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}  #初始字典，一个台阶和两个台阶的情况，相当于递归推出条件
        x = self.ways(n,memo)
        return x
    def ways(self,n,memo):
        if n not in memo:
            memo[n] = self.ways(n-1,memo)+self.ways(n-2,memo)
        return memo[n]

#DP bottom to top
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0] = 1
        res[1] = 2
        for i in range(2,n):
            res[i] = res[i-1]+res[i-2]
        return res[n-1]