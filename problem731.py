# problem 731 / my calendar II
class MyCalendarTwo(object):

    def __init__(self):
        self.event = []
        self.double = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i,j in self.double:
            if start < j and end > i:
                return False
        for i,j in self.event:
            if start < j and end >i:
                self.double.append((max(start,i),min(end,j)))
        self.event.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)