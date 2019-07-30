#problem 42 / trapping rain water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        l = len(height)
        left_max = [0]*l
        right_max = [0]*l
        left_max[0] = height[0]
        for i in range(l):
            left_max[i] = max(height[i],left_max[i-1])
        right_max[l-1] = height[l-1]
        for i in range(l-2,-1,-1):
            right_max[i] = max(height[i],right_max[i+1])
            
        for i in range(1,l-1):
            ans += min(left_max[i],right_max[i]) - height[i]
        
        return ans

#
#Second method, more simple
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        left_max = right_max = 0
        ans = 0
        while i<j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if left_max <= right_max:
                ans += (left_max-height[i])
                i += 1
            else:
                ans += (right_max-height[j])
                j -= 1
        return ans