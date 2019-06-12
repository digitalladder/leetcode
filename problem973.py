#problem 973 //K Closest Points to Origin
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def sort(i,j,K):
            if i >= j:
                return
            n = random.randint(i,j)
            points[i],points[n] = points[n],points[i]
            mid = partition(i,j)
            if K < mid-i+1:
                sort(i,mid-1,K)
            elif K > mid-i+1:
                sort(mid+1,j,K-(mid-i+1))
        def dist(i):
            return points[i][0]**2+points[i][1]**2
        def partition(i,j):
            pivot = dist(i)
            head = i
            i = i+1
            while True:
                while i < j and dist(i) < pivot:
                    i = i+1
                while i <= j and dist(j) >= pivot:
                    j = j-1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]

            points[head],points[j] = points[j],points[head]
            return j
        
        sort(0,len(points)-1,K)
        return points[:K]