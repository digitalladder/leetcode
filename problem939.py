#problem 939 / minimum area rectangle
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        col = collections.defaultdict(list)
        for x,y in points:
            col[x].append(y)
        lastx = {}
        ans = float('inf')
        for c in sorted(col):
            temp = col[c]
            temp.sort()
            for i in range(len(temp)):
                for j in range(i):
                    if (temp[j],temp[i]) in lastx:
                        ans = min(ans,(temp[i]-temp[j])*(c-lastx[temp[j],temp[i]]))
                    lastx[temp[j],temp[i]] = c
        return ans if ans<float('inf') else 0

# approach 2
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s = set(map(tuple,points))
        ans = float('inf')
        for i in range(len(points)):
            for j in range(i):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                    if (points[i][0],points[j][1]) in s and (points[j][0],points[i][1]) in s:       #注意这里tuple里元素的顺序
                        ans = min(ans,abs(points[i][0]-points[j][0])*abs(points[i][1]-points[j][1]))
        return ans if ans < float('inf') else 0