#Problem 39 /Combination Sum
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        combination = []
        result = []
        self.dfs(candidates, target, combination, result)
        return result
    def dfs(self, candidates, target, combination, result):
        for i,num in enumerate(candidates):
            if num > target:
                return
            if num == target:
                result.append(combination+[num])
                return
            if num < target:
                combination.append(num)
                self.dfs(candidates[i:],target-num,combination,result)
                combination.pop()

#非递归解法
class Solution:
# @param candidates, a list of integers
# @param target, integer
# @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for n in range(start, len(candidates)):
                t = total + candidates[n]
                if t > target:
                    break
                stack.append((t, n, res + [candidates[n]]))
        return result