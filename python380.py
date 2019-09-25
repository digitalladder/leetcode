#problem 380 / insert delete getrandom O(1)
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx = self.pos[val]
            self.nums[idx],self.pos[self.nums[-1]] = self.nums[-1],idx
            self.nums.pop()
            self.pos.pop(val,0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randint(0,len(self.nums)-1)
        return self.nums[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()