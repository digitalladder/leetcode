#problem 1352 / product of the last k numbers
class ProductOfNumbers(object):

    def __init__(self):
        self.lastzerolocation = -1
        self.product = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.product.append(1)
        if num == 0:
            self.lastzerolocation=len(self.product)-1
            self.product[-1] = 1 if len(self.product) == 1 else self.product[-2]
        else:
            self.product[-1] = num if len(self.product) == 1 else self.product[-2]*num
        #print(self.product)
    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = len(self.product) 
        if self.lastzerolocation >= n-k:
            return 0
        else:
            return self.product[-1]/self.product[n-k-1] if n-k-1 >= 0 else self.product[-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)