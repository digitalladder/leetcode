#problem 253 /meeting rooms II
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x[0])
        track = []
        room = 0
        for interval in intervals:
            if not track or track[0] > interval[0]:
                room = room+1
            else:
                heapq.heappop(track)
            heapq.heappush(track,interval[1])
            
        return room