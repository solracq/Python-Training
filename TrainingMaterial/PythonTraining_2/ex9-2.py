#!/usr/bin/env python3

import sys
import tempconv

temp_str = input("Enter Celsius temp: ") 
c = float(temp_str)
f = tempconv.c2f(c)

print("{0:.1f} C is {1:.1f} F".format(c,f))

