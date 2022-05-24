from math import factorial
from time import time

class CalcRoot():
    def __init__(self, num, power):
        self.originalVal = num
        
        # Format: (center, root of center) it should be a known root
        self.center = (1,1)
        self.power = power

    def getCenter(self):
        return self.center

    def getPower(self):
        return self.power

    def getOriginalValue(self):
        return self.originalVal

    def getRoot(self, degree):
        exp = 1/self.power
        constantMultiple = 1
        numerator = 1
        root = 0
        for n in range(degree):
            constant = constantMultiple * (self.center[1] ** numerator / factorial(n))
            root += constant * ((self.originalVal - self.center[0]) ** n)

            numerator -= self.power
            constantMultiple *= exp
            exp -= 1

        return root

    def setCenter(self):
        beginingVal = 1
        endVal = int( self.originalVal )
        previousVal = 0

        while abs( endVal-beginingVal ) > 1:
            halfwayVal = int( beginingVal + (endVal - beginingVal)/2 )
            squaredHalfwayVal = halfwayVal ** self.power

            if previousVal == halfwayVal:
                self.center = ( squaredHalfwayVal, halfwayVal )
                return

            if squaredHalfwayVal > self.originalVal:
                endVal = halfwayVal
            elif squaredHalfwayVal < self.originalVal:
                beginingVal = halfwayVal
            else:
                self.center = (squaredHalfwayVal, halfwayVal)
                return
            
            previousVal = halfwayVal

        if abs(self.originalVal - endVal ** self.power) < abs(self.originalVal - beginingVal ** self.power):
            self.center = (endVal ** self.power, endVal)
        else:
            self.center = (beginingVal ** self.power, beginingVal)

if __name__ == "__main__":
    while True:
        ans = input("Integer> ")
        if ans.lower() == "q":
            print("Bye!")
            break

        power = input("Power> ")
        testRoot = CalcRoot(int( ans ), int( power ))
        startTime = time()
        testRoot.setCenter()
        print(f"Center: {testRoot.getCenter()}")
        print(f"Root: {testRoot.getRoot(10)}")
        print(f"Time Spent: {(time() - startTime) * 1000} ms")
