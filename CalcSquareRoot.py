class CalcSquareRoot():
    def __init__(self, num):
        self.squaredNum = num

        self.center = 1
        self.sqrtCenter = 1

        self.orderConstants = []

    def getCenter(self):
        return self.center

    def setSquaredNum(self, squaredNum):
        self.squaredNum = squaredNum

    def getSquaredNum(self):
        return self.squaredNum

    @staticmethod
    def calculateSquaredNumbers(filename, maxNum):
        squaredNums = []
        for currNum in range(1,maxNum):
            squaredNums.append( str(currNum ** 2) + "," + str(currNum) + "\n")

        centerFile = open(filename, 'w')
        centerFile.writelines(squaredNums)
        centerFile.close()

    def getRoot(self):
        self.calculateTaylorPolynomialConstants()

        total = 0
        for constantIndex in range(len(self.orderConstants)):
            total += self.orderConstants[constantIndex] * (self.squaredNum - self.center) ** constantIndex

        return total

    def findCenter(self, filename):
        centerList = {}
        with open(filename, 'r') as centerFile:
            for currLine in centerFile:
                centerPair = currLine.split(",")
                centerList[ int( centerPair[0] ) ] = int( centerPair[1] )

        newCenter = 1
        for squaredVal in centerList.keys():
            if abs( squaredVal - self.squaredNum ) < abs( newCenter - self.squaredNum ):
                newCenter = squaredVal

        self.center = newCenter
        self.sqrtCenter = centerList[newCenter]
        return newCenter

    def calculateTaylorPolynomialConstants(self):
        self.orderConstants.append( self.sqrtCenter )          # Oth order
        self.orderConstants.append( float(1/2 * (1/self.sqrtCenter)) )          # 1st order
        self.orderConstants.append( float(-1/4 * (1/self.sqrtCenter ** 3))/2  )          # 2nd order
        self.orderConstants.append( float(3/8 * (1/self.sqrtCenter ** 5))/6 )          # 3rd order
        self.orderConstants.append( float(-5/8 * (1/self.sqrtCenter ** 7))/24 )          # 4th order

if __name__ == "__main__":
    val = float(input("Enter a number to find the square root of: "))
    print("---------------")
    testRoot = CalcSquareRoot(val)

    CalcSquareRoot.calculateSquaredNumbers("possibleCenters.txt", 10000)
    print( testRoot.findCenter("possibleCenters.txt") )

    print(f"Square Root of {testRoot.getSquaredNum()}: {testRoot.getRoot()}")
