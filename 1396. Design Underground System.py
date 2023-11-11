class UndergroundSystem:
    def __init__(self):
        self.checkin = defaultdict(tuple)
        self.journey = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin[id]
        self.journey[(startStation, stationName)].append(t-startTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.journey[(startStation,endStation)])/len(self.journey[(startStation,endStation)])
