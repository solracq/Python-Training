#!/usr/bin/env python3
"""
Print the date of the first Wednesday of each month
"""
import calendar

YEAR = 2013

for month_num in range(1,13):
    mcal = calendar.monthcalendar(2013, month_num)
    # if Wed of 1st week != 0, then 1st Wed
    # is in 1st week, otherwise 2nd week
    if mcal[0][calendar.WEDNESDAY] != 0:
        week = mcal[0]
    else:
        week = mcal[1]

    wed_date = week[calendar.WEDNESDAY]
    print("Month {0:2d}: First Wednesday: {1}".format(month_num, wed_date))