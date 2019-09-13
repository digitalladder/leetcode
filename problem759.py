#problem 759 / employee free time

# Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        events = []
        for emp in schedule:
            for itv in emp:
                events.append((itv.start,0))
                events.append((itv.end,1))
        events.sort()
        ans = []
        prev = None
        balance = 0
        for t, cmd in events:
            if balance == 0 and prev is not None:
                ans.append(Interval(prev,t))
            balance += 1 if cmd == 0 else -1
            prev = t
        return ans