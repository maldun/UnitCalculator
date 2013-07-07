
from __future__ import print_function

class UnitTester(object):

    def testMassUnits(self):

        from UnitCalculator import kg, g, T
        
        print("Test mass Units:", kg(g) == 1000.0, g(kg) == 0.001, T(kg) == 1000.0,
              T(g) == 1000000.0, kg(T) == 0.001, g(T) == 0.000001)
    
    def __init__(self):

        self.testMassUnits()

UnitTester()
