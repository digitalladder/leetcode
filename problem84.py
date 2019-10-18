#problem 84 / largest rectangle in histogram
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = [-1]
        maxarea = 0
        for i in xrange(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                maxarea = max(maxarea,heights[h]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            h = stack.pop()
            maxarea = max(maxarea,heights[h]*(len(heights)-stack[-1]-1))
        return maxarea