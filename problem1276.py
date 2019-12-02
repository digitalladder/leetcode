#problem 1276 / number of burgers with no waste of ingredients
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        t = tomatoSlices
        c = cheeseSlices
        if t < c*2 or t > c*4 or t%2 != 0:
            return []
        s = (4*c-t)/2
        j = (t-s*2)/4
        return [j,s]