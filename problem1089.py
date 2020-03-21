#problem 1089 / duplicate zeros
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count = 0
        j = len(arr)-1
        for i in range(len(arr)):
            if i > j-count:
                break
            if arr[i] == 0:
                if i == j-count:
                    arr[j] = 0
                    j -= 1
                    break
                count += 1
        last = j-count
        for i in range(last,-1,-1):
            if arr[i] != 0:
                arr[i+count] = arr[i]
            else:
                arr[i+count] = 0
                count -= 1
                arr[i+count] = 0