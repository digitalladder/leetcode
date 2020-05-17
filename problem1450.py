#problem 1450 / number of students doing homework at a given time
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        n = len(startTime)
        number = 0
        for i in range(n):
            if startTime[i] <= queryTime:
                if endTime[i] >= queryTime:
                    number += 1
        return number