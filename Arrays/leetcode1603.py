class solution:
    def __init__(self , big , medium , small):
        self.big  = big
        self.medium = medium
        self.small = small
    def addCar(self , carType ):
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -=1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False
x = solution(1 , 1 , 0)
print(x.addCar(1))
print(x.addCar(2))
print(x.addCar(3))
print(x.addCar(1))
print(x.addCar(1))
