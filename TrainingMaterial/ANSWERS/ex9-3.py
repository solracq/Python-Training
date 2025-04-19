#!/usr/bin/env python3

import tempconv

while True:
	c = input('Enter Celsius temp: ')
	if c.lower() == 'q':
		break
	c = float(c)
	f = tempconv.c2f(c)
	print('{0:.1f} C is {1:.1f} F\n'.format(c,f))

