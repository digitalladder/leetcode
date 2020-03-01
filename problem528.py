#problem 528 / random pick with weight
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.n = len(w)
        self.pre = [0]*self.n
        self.pre[0] = w[0]
        for i in range(1,self.n):
            self.pre[i] = self.pre[i-1]+w[i]
        self.num = self.pre[-1]
        
    def pickIndex(self):
        """
        :rtype: int
        """
        idx = random.randint(0,self.num-1)
        for i in range(self.n):
            if self.pre[i] > idx:
                return i                        #用二分法可以加快

#二分法
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.n = len(w)
        self.pre = [0]*self.n
        self.pre[0] = w[0]
        for i in range(1,self.n):
            self.pre[i] = self.pre[i-1]+w[i]
        self.num = self.pre[-1]
        
    def pickIndex(self):
        """
        :rtype: int
        """
        idx = random.randint(0,self.num-1)
        return bisect.bisect_right(self.pre,idx)        #一定要用 _right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()