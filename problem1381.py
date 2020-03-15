#problem 1381 / design a stack with increment operation
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.size = maxSize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        temp = self.stack.pop()
        return temp
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k,len(self.stack))):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)