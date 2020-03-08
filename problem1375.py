#problem 1375 / bulb switcher III
class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        n = len(light)
        count = 1
        maxlight = light[0]
        for i in range(n-1):
            maxlight = max(maxlight,light[i])
            if maxlight == i+1:
                count += 1
        return count