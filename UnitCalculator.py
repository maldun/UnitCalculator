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
