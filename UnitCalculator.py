# The MIT License (MIT)
#
# Copyright (c) 2013 Stefan Reiterer  - stefan.reiterer@magnasteyr.com or maldun.finsterschreck@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This Module enables unit conversion

class PhysicalUnit(object):
    """
    Base class for physical units.
    """

    def __init__(self,factor = 1.0):
        """
        Constructor for deriving SI units.
        Factor is initiated with 1.
        """
        self.factor = factor

    def __call__(self,other = None):
        """
        Call method that can be passed on
        """
        if other is None: # SelfConversion
            other = auto_converter.getCorrectUnit(self)

        if isinstance(other,type(self)):
            return self.factor/other.factor
        else:
            raise ValueError("Error: Not the correct units!")

# Distance Units

class MeterUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    pass 

# Mass Units

class KiloGrammUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    pass

# Pressure Units

class PascalUnit(PhysicalUnit):
    """
    Unit for pressure in Pascal 
    """
    pass

# Class for Force

class NewtonUnit(PhysicalUnit):
    """
    Unit for force in Newton 
    """
    pass


m = MeterUnit()
dm = MeterUnit(1e-1)
cm = MeterUnit(1e-2)
mm = MeterUnit(1e-3)

kg = KiloGrammUnit()
g = KiloGrammUnit(1e-3)
T = KiloGrammUnit(1e+3)

Pa = PascalUnit()
MPa = PascalUnit(1e+6)

N = NewtonUnit()
# Unit Systems

class UnitSystem(object):

    def getDistance(self):
        return self._distance

    def getMass(self):
        return self._mass

    def getPressure(self):
        return self._pressure

    def getForce(self):
        return self._force

class SystemeInternationale(UnitSystem):
    """
    Container class for SI units
    """
    def __init__(self):
        
        self._distance = m
        self._mass = kg
        self._pressure = Pa 
        self._force = N

class MilimiterAndTon(UnitSystem):
    """
    Container class for SI units
    with distance in mm and
    mass in tons
    """
    def __init__(self):
        
        self._distance = mm
        self._mass = T
        self._pressure = MPa 
        self._force = N

# Class for autoconversion

class UnitAutoConverter(object):
    """
    Class for autoconversion of unit systems
    """

    def __init__(self,unit_system):
        """
        Init method stores the
        unit system of the choice
        """
        self._unitSystem = unit_system

    def setUnitSystem(self,unit_system):
        """
        Resets the unit system
        """
        self._unitSystem = unit_system

    def __call__(self,unit_system):
        """
        Call method changes unit system 
        """
        self.setUnitSystem(unit_system)

    def getCorrectUnit(self,unit):
        """
        gets a object of unit type
        and returns the corresponding
        unit of the unit system
        """
        if isinstance(unit,MeterUnit):
            return self._unitSystem.getDistance()
        elif isinstance(unit,KiloGrammUnit):
            return self._unitSystem.getMass()
        elif isinstance(unit,PascalUnit):
            return self._unitSystem.getPressure()
        elif isinstance(unit,NewtonUnit):
            return self._unitSystem.getForce()
        else:
            raise ValueError("Error: Not a valid unit!")
    
SI = SystemeInternationale()
MM_TON = MilimiterAndTon()

auto_converter = UnitAutoConverter(SI)
