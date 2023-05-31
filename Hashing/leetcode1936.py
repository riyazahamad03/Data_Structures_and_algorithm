class UnderGroundSystem:
    def __init__(self) -> None:
        self.checkInMap = {}
        self.totalRoute = {}
    def checkIn(self , id : int , stationName : str , t : int):
        self.checkInMap[id] = (stationName , t)
    def checkOut(self , id : int , end : str , t : int):
        start , time = self.checkInMap[id]
        route = (start , end)
        if route not in self.totalRoute:
            self.totalRoute[route] = [0 , 0]
        self.totalRoute[route][0] += t - time
        self.totalRoute[route][1] += 1
    def getAverageTime(self, start : str , end : str):
        tot,count = self.totalRoute[(start , end)]
        return tot / count
x = UnderGroundSystem()
x.checkIn(45,"Leyton",3)
x.checkIn(32,"Paradise",8)
x.checkIn(27,"Leyton",10)
x.checkOut(45,"Waterloo",15)
x.checkOut(27,"Waterloo",20)
x.checkOut(32,"Cambridge",22)
