#problem 45 / jump game II
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0
               
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            #Note 1         
            if i == previous_jump_max:
                jumps += 1 
                previous_jump_max = current_jump_max
                #Note 2            
            if previous_jump_max >= len(nums)-1:
                return jumps
        return jumps

#方法2
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        
        n = len(nums)
        dp = [0] * n
        start_index = 0
        
        for i in range(1,n):
            while start_index + nums[start_index] < i:
                start_index += 1
                
            dp[i] = dp[start_index] + 1
            
            
        return dp[-1]