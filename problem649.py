#problem 649 / dota2 senate
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_queue = collections.deque()
        d_queue = collections.deque()
        for i,party in enumerate(senate):
            if party == 'D':
                d_queue.append(i)
            else:
                r_queue.append(i)
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if d < r:
                d_queue.append(d+len(senate))
            else:
                r_queue.append(r+len(senate))
        if len(r_queue) == 0:
            return 'Dire'
        else:
            return 'Radiant'