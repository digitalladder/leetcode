#problem 11 / Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxvolum = 0
        i,j = 0,len(height)-1
        while j > i:
            if height[i] > height[j]:
                vl = height[j]*(j-i)
                maxvolum = max(maxvolum,vl)
                j = j-1
            else:
                vl = height[i]*(j-i)
                maxvolum = max(maxvolum,vl)
                i = i+1
        return maxvolum