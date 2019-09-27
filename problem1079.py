#problem 1079 / letter tile possibilities
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = {''}
        for t in tiles:
            res |= {d[:i] + t + d[i:] for d in res for i in range(len(d) + 1)}
        return len(res)-1

#recursion
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if not tiles or len(tiles) == 1:
            return len(tiles)
        
        H = collections.Counter(tiles)
        count = 0
        for remaining in range(1, len(tiles) + 1):
            tmp_res = self.helper(H, remaining)
            count += tmp_res
        return count
    
    def helper(self, H, remaining):
        if remaining == 0:
            return 1
        
        count = 0
        for key in H.keys():
            if H[key] <= 0:
                continue
            H[key] -= 1
            count += self.helper(H, remaining - 1)
            H[key] += 1
        return count