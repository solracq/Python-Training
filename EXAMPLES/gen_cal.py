#!/usr/bin/env python3
"""

@author: jstrick
Created on Tue Mar 12 11:48:02 2013

"""
import calendar

tcal = calendar.TextCalendar()

print(tcal.formatmonth(1776,7))
print()

print(repr(tcal.formatmonth(1776,7)))
print()

print(tcal.formatmonth(2000,1,3,2))
print()