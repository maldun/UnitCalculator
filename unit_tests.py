
from __future__ import print_function

class UnitTester(object):

    def testMassUnits(self):

        from UnitCalculator import kg, g, T
        
        print("Test mass Units: ", 
              T(T) == 1.0,
              kg(kg) == 1.0,
              g(g) == 1.0,
              kg(g) == 1000.0, 
              g(kg) == 0.001, 
              T(kg) == 1000.0, 
              T(g) == 1000000.0, 
              kg(T) == 0.001, 
              g(T) == 0.000001)
    
    def testMetricUnits(self):

        from UnitCalculator import km, m, dm, cm, mm
        
        print("Test metric units: ", 
              km(km) == 1.0,
              km(m) == 1e+3, 
              km(dm) == 1e+4,
              km(cm) == 1e+5, 
              km(mm) = 1e+6, 
              m(km) = 1e-3,
              m(m) == 1.0,
              m(dm) == 1e-1,
              m(cm) == 1e-2,
              m(mm) == 1e-3,
              dm(km) == 1e-4,
              dm(m) == 1e-1,
              dm(dm) == 1.0,
              dm(cm) == 1e+1,
              dm(mm) == 1e+2,
              cm(km) == 1e-5,
              cm(m) == 1e-2,
              cm(dm) == 1e-1,
              cm(cm) == 1e+0,
              cm(mm) == 1e+1,
              mm(km) == 1e-6,
              mm(m) == 1e-3,
              mm(dm) == 1e-2,
              mm(cm) == 1e-1,
              mm(mm) == 1e+0
              )

    def testPressureUnits(self):
        
        from UnitCalculator import Pa, MPa

        print("Test pressure units: ",
              Pa(Pa) == 1.0,
              MPa(MPa) == 1.0,
              MPa(Pa) == 1e+3,
              Pa(MPa) == 1e-3)

    def testForceUnits(self):

        from UnitCalculator import kN, N

        print("Test force units: ",
              kN(kN) == 1.0,
              N(N) == 1.0,
              kN(N) == 1e+3,
              N(kN) == 1e-3)

    def __init__(self):

        self.testMetricUnits()
        self.testMassUnits()
        self.testPressureUnits()
        self.testForceUnits()
        
        

UnitTester()
