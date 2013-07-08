UnitCalculator
==============

Simple Python Module for Unit Conversion
This Module is distributet under MIT License and
should be used freely.

Version
=======

Version 0.2

Installation
============

Change into your desired directory (e.g. your home directory) and
execute

git clone https://github.com/maldun/UnitCalculator.git

Usage
=====

We assume here that the module is installed in the home directory.
In (I)Python:

In [1]: import os

In [2]: os.chdir(os.path.expanduser("~"))

In [3]: from UnitCalculator import *

In [4]: kg() # Default

Out[4]: 1.0

In [5]: kg(T) # Convert kg to Ton

Out[5]: 0.001

In [6]: auto_converter(mmNS) # Start automatic conversion to mm and T system

In [7]: kg()

Out[7]: 0.001

In [8]: auto_converter(SI) # Convert to SI

In [9]: 1000*mm() # Convert 1000mm to SI m

Out[9]: 1.0

In [10]: auto_converter(mmNS) 

In [11]: 8050*(kg()/m()**3) # Converts density of steel from kg/m^3 to T/mm^3

Out[11]: 8.05e-09

In [12]: N/m**2 # Since Version 0.2 direct algebra use is also supported

Out[12]: 1e-06

In fact the commands kg(), kg(T), m() etc. only return the conversion factors between two units,
so don't forget the multiplication symbol!

Usage in Code Aster
===================

Add to your .comm file (Assuming the module is installed in home):

import sys

sys.path.append(os.path.expanduser("~"))

from UnitCalculator import *


License
=======

The MIT License (MIT)

Copyright (c) 2013 Stefan Reiterer - stefan.reiterer@magnasteyr.com or maldun.finsterschreck@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
