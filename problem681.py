#problem 681 / next closest time
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        cur = 60 * int(time[:2])+int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur+1)%(24*60)
            if all(digit in allowed for block in divmod(cur,60) for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(cur,60))

###
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        #https://leetcode.com/problems/next-closest-time/discuss/190816/Python-simple-20ms-solution
        hour, minute = time.split(":")
        
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        two_digit_values = [a+b for a in nums for b in nums]

        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ":" + two_digit_values[i+1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ":" + two_digit_values[0]
        
        # Return the earliest time of the next day
        return two_digit_values[0] + ":" + two_digit_values[0]