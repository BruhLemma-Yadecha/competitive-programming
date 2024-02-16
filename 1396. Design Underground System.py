class UndergroundSystem(object):

    def __init__(self):
        self.ingress = {} # id -> (name, time)
        self.times = {} # station name -> list of times

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.ingress[id] = (stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        stamp = self.ingress[id]
        elapsed = float(t - stamp[1])
        path = (stamp[0], stationName)
        if path in self.times:
            self.times[path].append(elapsed)
        else:
            self.times[path] = [elapsed]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        l = self.times[(startStation, endStation)]
        print(l)
        return sum(l) / len(l)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)