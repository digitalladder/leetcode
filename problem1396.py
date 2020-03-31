#problem 1396 / design underground system
class UndergroundSystem(object):

    def __init__(self):
        self.station = collections.defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.station[stationName].append((id,t,'ckin'))

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.station[stationName].append((id,t,'ckout'))

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        instation,outstation = [],[]
        total,count = 0,0
        temp = self.station[startStation]
        for st in temp:
            if st[2] == 'ckin':
                instation.append(st)
        temp = self.station[endStation]
        for st in temp:
            if st[2] == 'ckout':
                outstation.append(st)
        for ste in outstation:
            for sts in instation:
                if ste[0] == sts[0]:
                    count += 1
                    total += (ste[1]-sts[1])
        return total/float(count)