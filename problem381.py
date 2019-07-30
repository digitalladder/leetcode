#problem 381 / insert delete getrandom O(1) - duplicates allowed
#use of collections.defaultdict
import collections
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.pos[val].add(len(self.nums)-1)
        return len(self.pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.pos[val]:
            return False
        idx = self.pos[val].pop()
        self.nums[idx] = self.nums[-1]
        self.pos[self.nums[-1]].add(idx)
        self.pos[self.nums[-1]].discard(len(self.nums)-1)
        self.nums.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        i = random.randint(0,len(self.nums)-1)
        return self.nums[i]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()