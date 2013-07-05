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

    def __init__(self):
        """
        Constructor for deriving SI units.
        Factor is initiated with 1.
        """
        self.factor = 1.0

    def _callHelper(self,other,INSTANCE):
        """
        Help function for __call__ methods.
        Helps avoiding copy & paste tasks.
        """
        if isinstance(other,INSTANCE):
            return self.factor/other.factor
        else:
            raise ValueError("Error: Not the correct units!")

# Distance Units

class MeterUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    def __call__(self,other):
        """
        Call function for Conversion
        EXAMPLE::

            >>> m(cm) = 100.0
            
        """
        return self._callHelper(other,MeterUnit)

class DeciMeterUnit(MeterUnit):

    def __init__(self):

        self.factor = 1e-1

class CentiMeterUnit(MeterUnit):

    def __init__(self):

        self.factor = 1e-2

class MiliMeterUnit(MeterUnit):

    def __init__(self):

        self.factor = 1e-3

m = MeterUnit()
dm = DeciMeterUnit()
cm = CentiMeterUnit()
mm = MiliMeterUnit()

# Mass Units

class KiloGrammUnit(PhysicalUnit):
    """
    Unit for distance in meter 
    """
    def __call__(self,other):
        """
        Call function for Conversion
        EXAMPLE::

            >>> kg(g) = 1000.0
            
        """
        return self._callHelper(other,KiloGrammUnit)

class GrammUnit(KiloGrammUnit):

    def __init__(self):

        self.factor = 1e-3

class TonUnit(KiloGrammUnit):

    def __init__(self):

        self.factor = 1e+3

kg = KiloGrammUnit()
g = GrammUnit()
T = TonUnit()
