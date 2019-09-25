#problem 1200 / minimum absolute difference
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        dif = arr[1] - arr[0]
        for i in range(len(arr)-1):
            j = i+1
            sub = arr[j]-arr[i]
            if sub < dif:
                dif = sub
                ans = []
                ans.append([arr[i],arr[j]])
            elif sub == dif:
                ans.append([arr[i],arr[j]])
        return ans