##Problem 4 /Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return "error"
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if i == 0:
                    maxofleft = nums2[j-1]
                elif j == 0:
                    maxofleft = nums1[i-1]
                else:
                    maxofleft = max(nums1[i-1],nums2[j-1])
                if (m+n)%2 == 1:
                    return maxofleft
                if i == m:
                    minofright = nums2[j]
                elif j == n:
                    minofright = nums1[i]
                else:
                    minofright = min(nums1[i], nums2[j])
                return (maxofleft+minofright)/2
        