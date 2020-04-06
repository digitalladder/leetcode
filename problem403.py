#problem 403 / frog jump
# dp / hashmap
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dic = {}
        for i in range(len(stones)):
            dic[stones[i]] = set()
        dic[stones[0]].add(0)
        for i in range(len(stones)):
            for k in dic[stones[i]]:
                for step in range(k-1,k+2):
                    if step > 0 and stones[i]+step in dic:
                        dic[stones[i]+step].add(step)
        return len(dic[stones[len(stones)-1]]) > 0