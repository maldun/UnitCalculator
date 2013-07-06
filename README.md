UnitCalculator
==============

Simple Python Module for Unit Conversion
This Module is distributet under MIT License and
should be used freely.

Installation
============

Change into your desired directory (e.g. your home directory) and
execute

git clone https://github.com/maldun/UnitCalculator.git

Usage
=====

We assume here that the module is installed in the home directory.
In Python:

>>> import os
>>> os.chdir(os.path.expanduser("~")) # Assuming that we installed it in home directory
>>> from UnitCalculator import *
>>> m(mm) # Convert m to mm
1000.0
>>> auto_converter(MM_TON) # Start Auto Conversion from m and kg to mm and T
>>> m() # Now converts m to mm by default
1000.0
>>> auto_converter(SI) # Default
>>> m()
1.0
>>> 1000*mm() # 1000mm to SI unit m
1.0

Usage in Code Aster
===================

import sys
sys.path.append(os.path.expanduser("~")) # Assuming that we are in home dir
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
