#problem 771 / Jewels and Stones
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}
        count = 0
        for i,letter in enumerate(J):
            jewels[letter] = i
        for stone in S:
            if stone in jewels:
                count = count+1
        return count


#2-lines soultion
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jset = set(J)
        return sum(s in Jset for s in S)