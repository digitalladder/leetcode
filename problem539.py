#problem 539 / minimum time difference
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        arr = []
        for time in timePoints:
            temp = time.split(':')
            t = int(temp[0])*60+int(temp[1])
            arr.append(t)
        arr = sorted(arr)
        res = 1440
        for i in range(len(arr)-1):
            res = min(res,arr[i+1]-arr[i])
            if min == 0:
                return 0
        res = min(res,arr[0]+1440-arr[-1])
        return res